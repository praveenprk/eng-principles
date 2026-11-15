# CONFORMANCE.md
# Cross-project conformance against ENG-STD-*
# Vocabulary: conformant / partial / not yet / n/a / not assessed (ENG-STD-006 §2.4)
# Every non-"not assessed" row cites evidence. Date of last update: 2026-11-16

## contextos

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | partial | RFC 2119 MUST/MUST NOT used throughout docs/specs. IDs stable. No `ENG-` anchors are accepted by commit-msg regex yet |
| ENG-STD-002 Lifecycle gates | conformant | docs/DISCIPLINE.md §3 (adds DESIGN gate). factory/supervisor.sh |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not assessed | No pinned formatter or linter observed at repo root |
| ENG-STD-005 Change control | conformant | scripts/hooks/commit-msg, pre-commit, pre-push. Git log shows anchored commits (e.g. 13225f5 — RFC-031) |
| ENG-STD-006 Registers | conformant | docs/DECISIONS.md, docs/VIOLATIONS.md, docs/conformance/ContextOS-ICS.md |
| ENG-STD-007 Quality model | not assessed | — |

## phasectl

Read at b3a2376 (origin/main, 2026-11-16), after adoption (phasectl
DECISION-001, PR #12). Source of truth: phasectl docs/conformance/phasectl-ICS.md.
Before adoption, at cbdcfda: no RFC/SPEC, free-form commits, no hooks, no
registers.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not yet | No RFC/SPEC (phasectl V-ENG-002-01). RFC-001 and SPEC-001..003 are in open PRs #14 and #15 |
| ENG-STD-003 Design / SOLID | partial | `LLMProvider` ABC (phasectl DECISION-004). Indexer is a plain binary contract (DECISION-003). README: progress to stderr, stdout clean |
| ENG-STD-004 Clean code | partial | CONTRIBUTING.md: why-only comments, no new deps without reason. Gaps: no linter or formatter in CI (V-ENG-004-02); api.py swallows an exception (V-ENG-004-01) |
| ENG-STD-005 Change control | partial | scripts/hooks/ (commit-msg, pre-push, test 20/20). AGENTS.md. Branch protection and ruleset on main. Gap: b3a2376 reached main unanchored through a GitHub merge, where local hooks do not run. Registered in open PR #13 (V-ENG-005-02). phasectl's ICS on main still says conformant, so it is behind until #13 merges |
| ENG-STD-006 Registers | conformant | docs/DECISIONS.md (DECISION-001..005), docs/VIOLATIONS.md, docs/conformance/phasectl-ICS.md |
| ENG-STD-007 Quality model | not assessed | — |

The CONTRIBUTING.md gap noted before adoption ("no pytest suite yet") was
fixed in phasectl PR #12.

## adp-protocol

Read at 39abefb (origin/main, 2026-11-15). Registered by ENG-DEC-008.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not assessed | — How the RFC/SPEC/TEST/BUILD gates apply to a specification-only repository is not stated. ADP-0 §5 (proposals) is the project's own change process |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not assessed | — The repository has code (scripts/ci/, scripts/hooks/), but whether ENG-STD-004 binds a specification repository's tooling is not stated |
| ENG-STD-005 Change control | partial | scripts/hooks/commit-msg, pre-push, test. AGENTS.md §Roles names the maintainer as the only one who merges. .github/workflows/adp.yml job `commits`. GitHub ruleset `adp-ruleset` active on the default branch: deletion, non_fast_forward, pull_request (merge only), required checks commits/schema/defects (`gh api repos/praveenprk/adp-protocol/rulesets/27276641`, 2026-11-15). Gap: 2 of 26 non-merge commits carry no anchor, 6042e27 and 739d2cb (`git log --no-merges --format='%h %s' 39abefb`), both from before ADP-0 |
| ENG-STD-006 Registers | not assessed | — The project keeps DEFECTS.md (ADP-0 §4) and proposals/ in place of VIOLATIONS.md and DECISIONS.md, and has no ICS. DEFECTS.md holds 17 entries: 15 OPEN, 2 RESOLVED (ADP-D-005, ADP-D-012) (`git show 39abefb:DEFECTS.md \| grep -E '^Status +:' \| sort \| uniq -c`). Whether these registers satisfy §1 is not stated |
| ENG-STD-007 Quality model | not assessed | — |

## fid

Read at 99ff3c6 (main, 2026-11-16), after adoption (fid DECISION-001, PR #18).
Registered by ENG-DEC-008. Source of truth: fid docs/conformance/fid-ICS.md.
Before adoption, at bff71b4: no SPEC, no registers, 0 of 43 non-merge
commits anchored, 23 with Co-authored-by lines (fid docs/VIOLATIONS.md).

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | conformant | spec/draft-kumar-fid-00.md is the RFC and SPEC (fid DECISION-001). Every normative section is tested or a listed gap, 31 traced (spec/TRACEABILITY.md, CI). `spec-ref` requires behaviour changes to cite the draft. Merged in fid #7 (c3768e1). Releases v0.1.0 and v0.1.1 predate the gate (fid V-ENG-002-01, resolved forward only) |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not yet | §6.1: no formatter or linter pinned or run in CI (fid V-ENG-004-01) |
| ENG-STD-005 Change control | partial | Ruleset `main-branch-integrity` requires rust, python, spec, spec-ref, commit-check and GitGuardian (`gh api repos/praveenprk/fid/rulesets/25491223`, 2026-11-16). `commit-check` checks the PR title and every commit on GitHub (scripts/commit_check.py). Gap: history before adoption stays unanchored (fid V-ENG-005-01, -02) |
| ENG-STD-006 Registers | partial | docs/DECISIONS.md, docs/VIOLATIONS.md, docs/conformance/fid-ICS.md, mapped onto spec/gaps.json and issues (fid DECISION-001). DECISION-001 is PROPOSED |
| ENG-STD-007 Quality model | not assessed | — |

## factory-protocol

Read at 1340fa7 (main, 2026-11-15). Registered by ENG-DEC-008.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not assessed | — How the gates apply to a documentation-only repository is not stated |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not assessed | — The repository has no source tree, but index.html and factory-protocol.html each carry an inline `<script>` (`grep -c '<script' index.html factory-protocol.html` → 1, 1). Whether that is code under ENG-STD-004 is not stated |
| ENG-STD-005 Change control | partial | GitHub ruleset `factory-protocol-ruleset` active on the default branch: deletion, non_fast_forward, pull_request, required checks (`gh api repos/praveenprk/factory-protocol/rulesets/27276808`, 2026-11-15). The only commit straight to main is 6767f6e "Initial commit" (`git log --first-parent --no-merges 1340fa7`). Gaps: 0 of 4 non-merge commits carry an anchor (e.g. 13ad193 "chore: license under Apache-2.0 with NOTICE"). No hooks, no AGENTS.md (`git ls-files`) |
| ENG-STD-006 Registers | not yet | No DECISIONS.md, VIOLATIONS.md, or ICS. `git ls-files` at 1340fa7 lists only LICENSE, NOTICE, README.md, factory-protocol.html, index.html |
| ENG-STD-007 Quality model | not assessed | — |
