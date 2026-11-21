# ENG-STD-008 — Contributor Readiness
Status: ACTIVE (ENG-DEC-011) · Refs: OpenSSF Best Practices Badge (passing level), OpenSSF Scorecard, GitHub community standards, SemVer 2.0.0, Keep a Changelog 1.1.0, Rust API Guidelines, PEP 621, IETF BCP 14 (RFC 2119, RFC 8174), RFC 3552, ISO/IEC/IEEE 12207, 29119, 29148

## 1. Purpose
1.1 A project meets this standard when an experienced open-source
    contributor (a large Rust or Python project's maintainer, say) finds
    on arrival everything they expect before contributing. That covers
    how to contribute and report a vulnerability, how changes are
    controlled, what CI enforces, how versions and releases work, and,
    for a specification, the IETF conventions.
1.2 The cited standards are reference models. Meeting a check is not
    certification or compliance with them (ENG-DEC-004).

## 2. Checks
2.1 Each check has an id, a level (MUST / SHOULD, RFC 2119), and the
    project kinds it applies to: `rust`, `python`, `spec`, `docs`,
    `standards`, or all. A project lists its kinds in audit/projects.json.
2.2 The checks are implemented in audit/audit.py, from the git host's
    current state, with evidence. The table below and that file list the
    same ids; CI fails if they differ.

| Id | Group | Check | Level | Applies to | Reference |
|----|-------|-------|-------|------------|-----------|
| `readme` | Front door | README | MUST | all | OpenSSF BP: description, interact |
| `license` | Front door | OSI licence, detected | MUST | all | OpenSSF BP: floss_license |
| `contributing` | Front door | CONTRIBUTING | MUST | all | OpenSSF BP: contribution |
| `coc` | Front door | Code of conduct | SHOULD | all | GitHub community standards |
| `security` | Front door | SECURITY.md (private reporting) | MUST | all | OpenSSF BP: vulnerability_report_process |
| `issue_tpl` | Front door | Issue templates | SHOULD | all | GitHub community standards |
| `pr_tpl` | Front door | PR template | SHOULD | all | GitHub community standards |
| `about` | Front door | Description and topics | SHOULD | all | GitHub community standards |
| `agents` | Change control | AGENTS.md | MUST | all | ENG-STD-005 §6 |
| `rules` | Change control | Default branch protected | MUST | all | ENG-STD-005 §2.2; ISO/IEC/IEEE 12207 6.3.5 |
| `commit_check` | Change control | Shared commit check required | MUST | all | ENG-STD-005 §1.5 (ENG-DEC-009) |
| `registers` | Change control | Decisions, violations, ICS | MUST | all | ENG-STD-006 |
| `ci` | Quality | CI on every PR | MUST | all | OpenSSF BP: test_continuous_integration |
| `ci_green` | Quality | CI green on default branch | MUST | all | OpenSSF BP: test |
| `required` | Quality | Build/test checks required to merge | MUST | all | ENG-STD-004 §6; OpenSSF Scorecard: Branch-Protection |
| `tests` | Quality | Automated tests | MUST | all | OpenSSF BP: test; ISO/IEC/IEEE 29119 |
| `fmt_lint` | Quality | Formatter and linter in CI | MUST | rust, python | ENG-STD-004 §6.1; OpenSSF BP: warnings |
| `dependabot` | Security | Automated dependency updates | SHOULD | all | OpenSSF Scorecard: Dependency-Update-Tool |
| `pinned` | Security | Actions pinned to a commit | SHOULD | all | OpenSSF Scorecard: Pinned-Dependencies |
| `perms` | Security | Least-privilege workflow token | MUST | all | OpenSSF Scorecard: Token-Permissions |
| `supply` | Security | Dependency vulnerability audit | SHOULD | rust, python | OpenSSF Scorecard: Vulnerabilities |
| `changelog` | Versioning | CHANGELOG | MUST | rust, python, spec | Keep a Changelog 1.1.0; OpenSSF BP: release_notes |
| `semver` | Versioning | SemVer release tags | MUST | rust, python | SemVer 2.0.0; ENG-STD-005 §5.1 |
| `releases` | Versioning | Release page per tag | SHOULD | rust, python | OpenSSF BP: release_notes |
| `signed` | Versioning | Latest tag signed | MUST | rust, python | ENG-STD-005 §5.1; OpenSSF Scorecard: Signed-Releases |
| `cargo_meta` | Rust | Cargo.toml metadata complete | MUST | rust | Rust API Guidelines C-METADATA |
| `msrv` | Rust | MSRV declared and tested | MUST | rust | Rust API Guidelines; cargo rust-version |
| `docs` | Rust | Public API documented (missing_docs) | SHOULD | rust | Rust API Guidelines C-CRATE-DOC |
| `pyproject` | Python | pyproject metadata complete | MUST | python | PEP 621 |
| `py_min` | Python | Minimum Python tested in CI | MUST | python | PEP 621 requires-python |
| `bcp14` | Specification | BCP 14 keywords (RFC 2119 + 8174) | MUST | spec | IETF BCP 14 |
| `seccons` | Specification | Security Considerations | MUST | spec | IETF RFC 3552 |
| `trace` | Specification | Requirements trace to tests | MUST | spec | ISO/IEC/IEEE 29148 (traceability) |

## 3. Status and rulings
3.1 Each check reports `pass`, `fail`, `n/a` (does not apply), or `not
    assessed` (ENG-STD-006 §2.4). A repository the audit cannot read is
    `not assessed`, never passed or failed.
3.2 Only the governor rules on a check for a project (e.g. that a
    project's own registers stand in for ENG-STD-006, or that a host limit
    blocks a check). A ruling is recorded in audit/projects.json under
    `overrides`, with the reason, and shows on the dashboard.
3.3 A failing MUST is a gap. A project registers its gaps as violations
    (ENG-STD-006) and closes them through its normal change process.

## 4. Dashboard
4.1 `.github/workflows/dashboard.yml` runs the audit daily and on every
    merge to `main`, and publishes the result (audit/render.py) on this
    repository's GitHub Pages site. The page is the current state of every
    governed project.
4.2 A private repository shows its name and statuses only, never evidence.

## Enforcement
| Clause | Mechanism |
|--------|-----------|
| 2.x | audit/audit.py, on the dashboard (measured, not blocking) |
| 2.2 (table = code) | `governance.yml` job `audit-selftest` |
| 3.3 | Review; each project's violation register |
