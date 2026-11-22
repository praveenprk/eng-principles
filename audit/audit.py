#!/usr/bin/env python3
"""audit — measure each project against ENG-STD-008 (contributor readiness).

Reads only from the git host (gh api), never clones. One JSON report on
stdout: per project, per check, a status (pass / fail / n/a / not assessed)
with evidence. Every check names the standard it comes from; the check ids
are the ids in ENG-STD-008. Nothing here claims certification or
compliance (ENG-DEC-004): these are reference models.

A repository the token cannot read is reported "not assessed", never
passed or failed. A governor ruling in projects.json ("overrides") replaces
a check's result and says why.

Usage: audit/audit.py audit/projects.json > report.json
Substrate: Python 3.11+ standard library, gh (authenticated).
"""

import base64
import json
import re
import subprocess
import sys
import tomllib
from datetime import datetime, timezone

SHA = re.compile(r"@[0-9a-f]{40}(\s|$)")
SEMVER_TAG = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-[0-9A-Za-z.-]+)?$")


def gh(path):
    """GET a GitHub API path. None on 404 or any error."""
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


class Repo:
    def __init__(self, owner, name):
        self.full = f"{owner}/{name}"
        self.meta = gh(f"repos/{self.full}") or {}
        self.default = self.meta.get("default_branch", "main")
        tree = gh(f"repos/{self.full}/git/trees/{self.default}?recursive=1") or {}
        self.paths = [t["path"] for t in tree.get("tree", []) if t["type"] == "blob"]
        self._text = {}

    def has(self, *patterns):
        """First path matching any regex (case-insensitive), or None."""
        for p in self.paths:
            for pat in patterns:
                if re.fullmatch(pat, p, re.I):
                    return p
        return None

    def text(self, path):
        if path not in self._text:
            c = gh(f"repos/{self.full}/contents/{path}?ref={self.default}")
            self._text[path] = base64.b64decode(c["content"]).decode("utf-8", "replace") if c and "content" in c else ""
        return self._text[path]

    def workflows(self):
        return {p: self.text(p) for p in self.paths if re.fullmatch(r"\.github/workflows/[^/]+\.ya?ml", p)}


def result(status, evidence):
    return {"status": status, "evidence": evidence}


def ok(cond, yes, no):
    return result("pass", yes) if cond else result("fail", no)


# ---------------------------------------------------------------- checks
# Each check: id, group, title, level (MUST / SHOULD), ref, kinds (None = all), fn(repo, ctx)

def c_readme(r, x):
    p = r.has(r"README(\.md|\.rst|\.txt)?")
    return ok(p, p, "no README at the root")


def c_license(r, x):
    spdx = (r.meta.get("license") or {}).get("spdx_id")
    return ok(spdx and spdx != "NOASSERTION", f"LICENSE ({spdx})", "no license GitHub can identify")


def c_contributing(r, x):
    p = r.has(r"(\.github/|docs/)?CONTRIBUTING(\.md)?")
    return ok(p, p, "no CONTRIBUTING.md")


def c_coc(r, x):
    p = r.has(r"(\.github/|docs/)?CODE_OF_CONDUCT(\.md)?")
    return ok(p, p, "no CODE_OF_CONDUCT.md")


def c_security(r, x):
    p = r.has(r"(\.github/|docs/)?SECURITY(\.md)?")
    return ok(p, p, "no SECURITY.md: no private way to report a vulnerability")


def c_issue_tpl(r, x):
    p = r.has(r"\.github/ISSUE_TEMPLATE/.+", r"\.github/ISSUE_TEMPLATE\.md")
    return ok(p, p, "no issue templates")


def c_pr_tpl(r, x):
    p = r.has(r"(\.github/)?PULL_REQUEST_TEMPLATE(\.md)?", r"\.github/PULL_REQUEST_TEMPLATE/.+")
    return ok(p, p, "no pull request template")


def c_about(r, x):
    d, t = r.meta.get("description"), r.meta.get("topics") or []
    return ok(d and t, f"description and {len(t)} topics", "missing " + " and ".join(
        [s for s, v in (("description", d), ("topics", t)) if not v]))


def c_agents(r, x):
    p = r.has(r"AGENTS\.md")
    return ok(p, p, "no AGENTS.md")


def c_registers(r, x):
    found = [n for n, pat in (("decisions", r"(docs/)?DECISIONS\.md"), ("violations", r"(docs/)?(VIOLATIONS|DEFECTS)\.md"),
                              ("ICS", r"(docs/conformance/.*ICS.*\.md|CONFORMANCE\.md)")) if r.has(pat)]
    return ok(len(found) == 3, ", ".join(found), "missing: " + ", ".join(
        sorted({"decisions", "violations", "ICS"} - set(found))))


def c_ruleset(r, x):
    if r.meta.get("private") and gh(f"repos/{r.full}/rules/branches/{r.default}") is None:
        return result("fail", "blocked: GitHub offers no branch rules for a private repository on the free plan")
    rules = gh(f"repos/{r.full}/rules/branches/{r.default}") or []
    types = {ru["type"] for ru in rules}
    prot = gh(f"repos/{r.full}/branches/{r.default}/protection")
    need = {"pull_request", "non_fast_forward", "deletion"}
    if need <= types:
        return result("pass", "ruleset: " + ", ".join(sorted(need)))
    if prot and not (prot.get("allow_force_pushes") or {}).get("enabled") and not (prot.get("allow_deletions") or {}).get("enabled") \
            and prot.get("required_pull_request_reviews") is not None:
        return result("pass", "classic branch protection")
    return result("fail", "default branch rules lack: " + ", ".join(sorted(need - types)))


def required_checks(r):
    ctx = set()
    for ru in gh(f"repos/{r.full}/rules/branches/{r.default}") or []:
        if ru["type"] == "required_status_checks":
            ctx |= {c["context"] for c in ru["parameters"]["required_status_checks"]}
    prot = gh(f"repos/{r.full}/branches/{r.default}/protection") or {}
    ctx |= set(((prot.get("required_status_checks") or {}).get("contexts")) or [])
    return ctx


def c_commit_check(r, x):
    wf = any("eng-principles/.github/workflows/commit-check.yml@" in t for t in r.workflows().values())
    req = "commit-check / check" in x["required"]
    return ok(wf and req, "shared check, required", "shared check " + ("not required" if wf else "not called"))


def c_ci(r, x):
    wfs = [p for p, t in r.workflows().items() if "pull_request" in t]
    return ok(wfs, ", ".join(sorted(wfs)), "no workflow runs on pull requests")


def c_ci_green(r, x):
    runs = gh(f"repos/{r.full}/commits/{r.default}/check-runs?per_page=100") or {}
    done = [c for c in runs.get("check_runs", []) if c["status"] == "completed" and c["conclusion"] not in ("skipped", "neutral")]
    if not done:
        return result("fail", f"nothing verifies {r.default} after a merge: no checks ran on its HEAD")
    bad = sorted({c["name"] for c in done if c["conclusion"] != "success"})
    return ok(not bad, f"{len(done)} checks green on {r.default} HEAD", "failing on HEAD: " + ", ".join(bad))


def c_required_checks(r, x):
    extra = x["required"] - {"commit-check / check", "commit-check / questions", "GitGuardian Security Checks"}
    return ok(extra, "required: " + ", ".join(sorted(extra)), "no build or test check is required to merge")


# Languages ENG-STD-004 §6.1 binds, detected from the repository itself, not
# from the project's kinds: code is any executable text (ENG-STD-004 §0,
# ENG-DEC-015). Each entry: name, path regex, formatter (label, CI regex),
# linter (label, CI regex). A language not listed here is not detected; add it
# here, with its usual formatter and linter.
LANGUAGES = [
    ("Rust", r".+\.rs", ("cargo fmt", r"cargo fmt"), ("clippy", r"cargo clippy")),
    ("Python", r".+\.pyi?", ("ruff format/black", r"\bruff\b|\bblack\b"), ("ruff/flake8/pylint", r"\bruff\b|flake8|pylint")),
    ("Shell", r".+\.(sh|bash)", ("shfmt", r"\bshfmt\b"), ("shellcheck", r"\bshellcheck\b")),
    ("JavaScript/TypeScript", r".+\.(m?js|cjs|jsx|tsx?)", ("prettier/biome/deno fmt", r"\bprettier\b|\bbiome\b|deno fmt"),
     ("eslint/biome/deno lint", r"\beslint\b|\bbiome\b|deno lint")),
    ("Go", r".+\.go", ("gofmt", r"\bgofmt\b|go fmt"), ("go vet/golangci-lint/staticcheck", r"go vet|golangci-lint|staticcheck")),
]
SHEBANG = re.compile(r"#!\s*(?:/usr/bin/env\s+)?(?:\S*/)?(sh|bash|dash|zsh|python3?|node)\b")
SCRIPT_DIRS = re.compile(r"(?:^|.*/)(?:hooks|scripts|bin)/(?:[^/]+/)*[^/.]+")


def languages(paths, text):
    """Languages present as executable text: by extension; extensionless
    files under hooks/, scripts/ or bin/ by their shebang; HTML pages that
    carry an inline <script> as JavaScript. Returns {name: example path}."""
    found = {}
    for p in paths:
        for name, pat, _, _ in LANGUAGES:
            if name not in found and re.fullmatch(pat, p, re.I):
                found[name] = p
        if SCRIPT_DIRS.fullmatch(p) and not p.startswith(".git"):
            m = SHEBANG.match(text(p)[:120])
            if m:
                name = {"python": "Python", "python3": "Python", "node": "JavaScript/TypeScript"}.get(m.group(1), "Shell")
                found.setdefault(name, p)
        if re.fullmatch(r".+\.html?", p, re.I) and "JavaScript/TypeScript" not in found and re.search(r"<script\b(?![^>]*\bsrc=)", text(p), re.I):
            found["JavaScript/TypeScript"] = p + " (inline <script>)"
    return found


def c_fmt_lint(r, x):
    found = languages(r.paths, r.text)
    if not found:
        return result("n/a", "no executable text found")
    t = "\n".join(r.workflows().values())
    have, miss = [], []
    for name, _, fmt, lint in LANGUAGES:
        if name in found:
            for label, pat in (fmt, lint):
                (have if re.search(pat, t) else miss).append(f"{name}: {label}")
    langs = ", ".join(f"{n} (e.g. {p})" for n, p in found.items())
    return ok(not miss, f"{langs}; in CI: " + ", ".join(have), f"{langs}; not in CI: " + ", ".join(miss))


def c_tests(r, x):
    p = r.has(r"tests/.+\.(rs|py)", r".*/tests?/.+\.(rs|py)", r".*test_.+\.py", r"conformance/.+\.json", r"hooks/test")
    return ok(p, f"e.g. {p}", "no tests found")


def c_dependabot(r, x):
    p = r.has(r"\.github/dependabot\.ya?ml", r"renovate\.json5?", r"\.github/renovate\.json5?")
    return ok(p, p, "no automated dependency updates")


def c_actions_pinned(r, x):
    uses = [(p, u.strip()) for p, t in r.workflows().items() for u in re.findall(r"uses:\s*(\S+)", t) if not u.startswith("./")]
    if not uses:
        return result("n/a", "no third-party actions")
    loose = [u for _, u in uses if not SHA.search(u + " ") and "praveenprk/" not in u]
    return ok(not loose, f"{len(uses)} actions pinned", f"{len(loose)} of {len(uses)} actions not pinned to a commit, e.g. {loose[0]}" if loose else "")


def c_token_perms(r, x):
    wfs = r.workflows()
    if not wfs:
        return result("n/a", "no workflows")
    loose = [p for p, t in wfs.items() if not re.search(r"^permissions:", t, re.M)]
    return ok(not loose, "top-level permissions in every workflow", "no top-level permissions: " + ", ".join(loose))


def c_changelog(r, x):
    p = r.has(r"CHANGELOG(\.md)?", r"docs/CHANGELOG\.md")
    return ok(p, p, "no CHANGELOG.md")


def c_semver_tags(r, x):
    tags = [t["name"] for t in gh(f"repos/{r.full}/tags?per_page=100") or []]
    sv = [t for t in tags if SEMVER_TAG.match(t)]
    x["semver_tags"] = sv
    if not tags:
        return result("fail", "no tags: no release yet")
    return ok(len(sv) == len(tags), f"{len(sv)} SemVer tags, latest {sv[0]}" if sv else "", "tags not vX.Y.Z: " + ", ".join(t for t in tags if t not in sv)[:80])


def c_releases(r, x):
    sv = x.get("semver_tags") or []
    if not sv:
        return result("n/a", "no release tags")
    rel = {rel["tag_name"] for rel in gh(f"repos/{r.full}/releases?per_page=100") or []}
    miss = [t for t in sv if t not in rel]
    return ok(not miss, f"release page for each of {len(sv)} tags", "no release page for: " + ", ".join(miss))


def c_signed_tag(r, x):
    sv = x.get("semver_tags") or []
    if not sv:
        return result("n/a", "no release tags")
    ref = gh(f"repos/{r.full}/git/ref/tags/{sv[0]}") or {}
    obj = ref.get("object", {})
    if obj.get("type") != "tag":
        return result("fail", f"{sv[0]} is a lightweight tag (no message, no signature)")
    tag = gh(f"repos/{r.full}/git/tags/{obj['sha']}") or {}
    v = (tag.get("verification") or {}).get("verified")
    return ok(v, f"{sv[0]} signed and verified", f"{sv[0]} annotated but not signed")


def cargo(r):
    p = r.has(r"Cargo\.toml")
    if not p:
        return None
    try:
        return tomllib.loads(r.text(p))
    except tomllib.TOMLDecodeError:
        return None


def c_cargo_meta(r, x):
    c = cargo(r)
    if c is None:
        return result("n/a", "no root Cargo.toml")
    pkg = c.get("package", {})
    need = ["description", "license", "repository", "readme", "keywords", "categories", "rust-version"]
    miss = [k for k in need if not pkg.get(k)]
    return ok(not miss, "Cargo.toml: " + ", ".join(need), "Cargo.toml lacks: " + ", ".join(miss))


def c_msrv_ci(r, x):
    c = cargo(r)
    msrv = (c or {}).get("package", {}).get("rust-version")
    if not msrv:
        return result("n/a" if c is None else "fail", "no rust-version declared")
    t = "\n".join(r.workflows().values())
    return ok(re.search(rf"\b{re.escape(msrv)}(\.\d+)?\b", t), f"CI builds on the MSRV {msrv}", f"rust-version {msrv} is declared but CI never builds with it")


def c_supply_chain(r, x):
    t = "\n".join(r.workflows().values())
    if "rust" in x["kinds"]:
        return ok(re.search(r"cargo[- ](deny|audit)|rustsec", t), "cargo-deny/audit in CI", "no cargo-deny or cargo-audit in CI")
    if "python" in x["kinds"]:
        return ok(re.search(r"pip-audit|safety|osv-scanner", t), "dependency audit in CI", "no pip-audit/osv-scanner in CI")
    return result("n/a", "no package dependencies")


def c_docs_lint(r, x):
    lib = r.has(r"src/lib\.rs")
    if not lib:
        return result("n/a", "no library crate")
    c = cargo(r) or {}
    lints = json.dumps(c.get("lints", {}))
    return ok("missing_docs" in r.text(lib) or "missing_docs" in lints, "missing_docs lint on", "public API docs not enforced (no missing_docs lint)")


def c_pyproject(r, x):
    p = r.has(r"pyproject\.toml", r".+/pyproject\.toml")
    if not p:
        return result("n/a" if "python" not in x["kinds"] else "fail", "no pyproject.toml")
    try:
        proj = tomllib.loads(r.text(p)).get("project", {})
    except tomllib.TOMLDecodeError:
        return result("fail", "pyproject.toml does not parse")
    need = ["name", "version", "description", "readme", "license", "requires-python", "urls"]
    miss = [k for k in need if not proj.get(k)]
    return ok(not miss, f"{p}: " + ", ".join(need), f"{p} lacks: " + ", ".join(miss))


def c_py_min(r, x):
    p = r.has(r"pyproject\.toml", r".+/pyproject\.toml")
    if not p:
        return result("n/a", "no pyproject.toml")
    req = tomllib.loads(r.text(p)).get("project", {}).get("requires-python", "")
    m = re.search(r">=\s*(3\.\d+)", req)
    if not m:
        return result("fail", "no requires-python lower bound")
    t = "\n".join(r.workflows().values())
    return ok(re.search(rf"['\"]?{re.escape(m.group(1))}['\"]?", t), f"CI tests Python {m.group(1)} (the minimum)", f"requires-python >={m.group(1)} but CI never runs {m.group(1)}")


def spec_files(r):
    return [p for p in r.paths if re.fullmatch(r"(spec|docs/specs?)/[^/]+\.md", p) and "README" not in p.upper()]


def c_bcp14(r, x):
    files = spec_files(r)
    if not files:
        return result("fail", "no specification documents under spec/")
    hit = [p for p in files if "{::boilerplate bcp14" in r.text(p)
           or (re.search(r"RFC\s*2119", r.text(p)) and re.search(r"RFC\s*8174", r.text(p)))]
    return ok(hit, f"BCP 14 (RFC 2119 + 8174) in {hit[0]}" if hit else "", "no spec cites both RFC 2119 and RFC 8174")


def c_security_considerations(r, x):
    files = spec_files(r)
    hit = [p for p in files if re.search(r"^#+\s*(\d+(\.\d+)*\.?\s*)?Security Considerations", r.text(p), re.M | re.I)]
    return ok(hit, f"Security Considerations in {hit[0]}" if hit else "", "no Security Considerations section (RFC 3552)")


def c_traceability(r, x):
    p = r.has(r".*TRACEABILITY.*\.md", r"scripts/ci/check_conformance\.py", r"spec/traceability\.py")
    return ok(p, p, "no requirement-to-test trace")


CHECKS = [
    # id, group, title, level, ref, kinds, fn
    ("readme", "Front door", "README", "MUST", "OpenSSF BP: description, interact", None, c_readme),
    ("license", "Front door", "OSI licence, detected", "MUST", "OpenSSF BP: floss_license", None, c_license),
    ("contributing", "Front door", "CONTRIBUTING", "MUST", "OpenSSF BP: contribution", None, c_contributing),
    ("coc", "Front door", "Code of conduct", "SHOULD", "GitHub community standards", None, c_coc),
    ("security", "Front door", "SECURITY.md (private reporting)", "MUST", "OpenSSF BP: vulnerability_report_process", None, c_security),
    ("issue_tpl", "Front door", "Issue templates", "SHOULD", "GitHub community standards", None, c_issue_tpl),
    ("pr_tpl", "Front door", "PR template", "SHOULD", "GitHub community standards", None, c_pr_tpl),
    ("about", "Front door", "Description and topics", "SHOULD", "GitHub community standards", None, c_about),
    ("agents", "Change control", "AGENTS.md", "MUST", "ENG-STD-005 §6", None, c_agents),
    ("rules", "Change control", "Default branch protected", "MUST", "ENG-STD-005 §2.2; ISO/IEC/IEEE 12207 6.3.5", None, c_ruleset),
    ("commit_check", "Change control", "Shared commit check required", "MUST", "ENG-STD-005 §1.5 (ENG-DEC-009)", None, c_commit_check),
    ("registers", "Change control", "Decisions, violations, ICS", "MUST", "ENG-STD-006", None, c_registers),
    ("ci", "Quality", "CI on every PR", "MUST", "OpenSSF BP: test_continuous_integration", None, c_ci),
    ("ci_green", "Quality", "CI green on default branch", "MUST", "OpenSSF BP: test", None, c_ci_green),
    ("required", "Quality", "Build/test checks required to merge", "MUST", "ENG-STD-004 §6; OpenSSF Scorecard: Branch-Protection", None, c_required_checks),
    ("tests", "Quality", "Automated tests", "MUST", "OpenSSF BP: test; ISO/IEC/IEEE 29119", None, c_tests),
    ("fmt_lint", "Quality", "Formatter and linter in CI, per language detected", "MUST", "ENG-STD-004 §0, §6.1; OpenSSF BP: warnings", None, c_fmt_lint),
    ("dependabot", "Security", "Automated dependency updates", "SHOULD", "OpenSSF Scorecard: Dependency-Update-Tool", None, c_dependabot),
    ("pinned", "Security", "Actions pinned to a commit", "SHOULD", "OpenSSF Scorecard: Pinned-Dependencies", None, c_actions_pinned),
    ("perms", "Security", "Least-privilege workflow token", "MUST", "OpenSSF Scorecard: Token-Permissions", None, c_token_perms),
    ("supply", "Security", "Dependency vulnerability audit", "SHOULD", "OpenSSF Scorecard: Vulnerabilities", ("rust", "python"), c_supply_chain),
    ("changelog", "Versioning", "CHANGELOG", "MUST", "Keep a Changelog 1.1.0; OpenSSF BP: release_notes", ("rust", "python", "spec"), c_changelog),
    ("semver", "Versioning", "SemVer release tags", "MUST", "SemVer 2.0.0; ENG-STD-005 §5.1", ("rust", "python"), c_semver_tags),
    ("releases", "Versioning", "Release page per tag", "SHOULD", "OpenSSF BP: release_notes", ("rust", "python"), c_releases),
    ("signed", "Versioning", "Latest tag signed", "MUST", "ENG-STD-005 §5.1; OpenSSF Scorecard: Signed-Releases", ("rust", "python"), c_signed_tag),
    ("cargo_meta", "Rust", "Cargo.toml metadata complete", "MUST", "Rust API Guidelines C-METADATA", ("rust",), c_cargo_meta),
    ("msrv", "Rust", "MSRV declared and tested", "MUST", "Rust API Guidelines; cargo rust-version", ("rust",), c_msrv_ci),
    ("docs", "Rust", "Public API documented (missing_docs)", "SHOULD", "Rust API Guidelines C-CRATE-DOC", ("rust",), c_docs_lint),
    ("pyproject", "Python", "pyproject metadata complete", "MUST", "PEP 621", ("python",), c_pyproject),
    ("py_min", "Python", "Minimum Python tested in CI", "MUST", "PEP 621 requires-python", ("python",), c_py_min),
    ("bcp14", "Specification", "BCP 14 keywords (RFC 2119 + 8174)", "MUST", "IETF BCP 14", ("spec",), c_bcp14),
    ("seccons", "Specification", "Security Considerations", "MUST", "IETF RFC 3552", ("spec",), c_security_considerations),
    ("trace", "Specification", "Requirements trace to tests", "MUST", "ISO/IEC/IEEE 29148 (traceability)", ("spec",), c_traceability),
]


# Severity of a failing check (ENG-DEC-013, ENG-STD-006 §2.3): an OpenSSF
# Scorecard check's own risk; otherwise an OpenSSF Best Practices passing
# criterion (MUST HIGH, SHOULD MEDIUM, SUGGESTED LOW); otherwise ours (HIGH if
# behaviour, personal data or compliance is affected, else MEDIUM). Security
# items are never below HIGH. The basis is shown next to each severity.
SEVERITY = {
    "readme": ("HIGH", "OpenSSF BP MUST: description_good"),
    "license": ("LOW", "OpenSSF Scorecard: License (Low)"),
    "contributing": ("HIGH", "OpenSSF BP MUST: contribution"),
    "coc": ("MEDIUM", "ours (OpenSSF BP silver only)"),
    "security": ("HIGH", "security floor (Scorecard: Security-Policy, Medium)"),
    "issue_tpl": ("MEDIUM", "ours"),
    "pr_tpl": ("MEDIUM", "ours"),
    "about": ("MEDIUM", "ours"),
    "agents": ("MEDIUM", "ours"),
    "rules": ("HIGH", "OpenSSF Scorecard: Branch-Protection (High)"),
    "commit_check": ("MEDIUM", "ours"),
    "registers": ("MEDIUM", "ours"),
    "ci": ("LOW", "OpenSSF Scorecard: CI-Tests (Low)"),
    "ci_green": ("HIGH", "ours: a red default branch can ship broken behaviour"),
    "required": ("HIGH", "OpenSSF Scorecard: Branch-Protection (High)"),
    "tests": ("HIGH", "OpenSSF BP MUST: test"),
    "fmt_lint": ("HIGH", "OpenSSF BP MUST: warnings"),
    "dependabot": ("HIGH", "OpenSSF Scorecard: Dependency-Update-Tool (High)"),
    "pinned": ("HIGH", "security floor (Scorecard: Pinned-Dependencies, Medium)"),
    "perms": ("HIGH", "OpenSSF Scorecard: Token-Permissions (High)"),
    "supply": ("HIGH", "OpenSSF Scorecard: Vulnerabilities (High); CRITICAL if a known vulnerability is present"),
    "changelog": ("HIGH", "OpenSSF BP MUST: release_notes"),
    "semver": ("LOW", "OpenSSF BP SUGGESTED: version_semver"),
    "releases": ("MEDIUM", "ours"),
    "signed": ("HIGH", "OpenSSF Scorecard: Signed-Releases (High)"),
    "cargo_meta": ("MEDIUM", "ours"),
    "msrv": ("MEDIUM", "ours"),
    "docs": ("MEDIUM", "ours"),
    "pyproject": ("MEDIUM", "ours"),
    "py_min": ("MEDIUM", "ours"),
    "bcp14": ("MEDIUM", "ours"),
    "seccons": ("HIGH", "security floor (RFC 3552)"),
    "trace": ("MEDIUM", "ours"),
}
SEVERITIES = ("CRITICAL", "HIGH", "MEDIUM", "LOW")


def audit(owner, name, kinds, overrides):
    r = Repo(owner, name)
    readable = bool(r.meta)
    x = {"kinds": set(kinds), "required": required_checks(r) if readable else set()}
    out = []
    for cid, group, title, level, ref, applies, fn in CHECKS:
        if not readable:
            res = result("not assessed", "repository not readable with this token")
        elif cid in overrides:  # a check the governor has not decided is reported as such
            res = result(overrides[cid]["status"], overrides[cid]["why"])
        elif applies and not (set(applies) & x["kinds"]):
            res = result("n/a", "does not apply to " + "/".join(sorted(kinds)))
        else:
            try:
                res = fn(r, x)
            except Exception as e:  # a check that cannot run is reported, never silently passed
                res = result("fail", f"check could not run: {type(e).__name__}")
        sv, basis = SEVERITY[cid]
        out.append({"id": cid, "group": group, "title": title, "level": level, "ref": ref,
                    "severity": sv, "severity_basis": basis, **res})
    scored = ("pass", "fail")
    must = [c for c in out if c["level"] == "MUST" and c["status"] in scored]
    should = [c for c in out if c["level"] == "SHOULD" and c["status"] in scored]
    return {
        "name": name,
        "url": f"https://github.com/{r.full}",
        "kinds": sorted(kinds),
        "private": r.meta.get("private", False),
        "readable": readable,
        "head": (gh(f"repos/{r.full}/commits/{r.default}") or {}).get("sha", "")[:7],
        "must": [sum(c["status"] == "pass" for c in must), len(must)],
        "should": [sum(c["status"] == "pass" for c in should), len(should)],
        "gaps": {v: sum(c["status"] == "fail" and c["severity"] == v for c in out) for v in SEVERITIES},
        "checks": out,
    }


def main():
    cfg = json.load(open(sys.argv[1]))
    report = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        "projects": [audit(cfg["owner"], p["name"], p["kinds"], p.get("overrides", {})) for p in cfg["projects"]],
    }
    json.dump(report, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
