# CONFORMANCE.md
# Cross-project conformance against ENG-STD-*
# Vocabulary: conformant / partial / not yet / n/a / not assessed (ENG-STD-006 §2.4)
# Every non-"not assessed" row cites evidence. Date of last update: 2026-11-15

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

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not yet | No RFC/SPEC directory. Design lives in docs/internal/DESIGN.md |
| ENG-STD-003 Design / SOLID | partial | `LLMProvider` ABC in src/phasectl/provider.py (D, O). Indexer behind a binary contract |
| ENG-STD-004 Clean code | partial | CONTRIBUTING.md: why-only comments, no new deps without reason. No pinned linter |
| ENG-STD-005 Change control | not yet | Git log: free-form messages, no anchors (e.g. cbdcfda, c2a4749). No hooks |
| ENG-STD-006 Registers | not yet | Only docs/internal/DECISION-CONTINUITY-FOLLOWUPS.md. No VIOLATIONS or ICS |
| ENG-STD-007 Quality model | not assessed | — |

Note: phasectl CONTRIBUTING.md says "There is no pytest suite yet", but
`tests/` contains pytest files. This is a doc-accuracy gap, recorded here for the
project to triage.

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

Read at bff71b4 (main, 2026-11-15), before adoption. Registered by ENG-DEC-008.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not yet | No RFC or SPEC at bff71b4 (`git ls-tree -r --name-only bff71b4 \| grep -iE 'rfc\|spec'` → none). conformance/README.md specifies the scoring formula, with vectors, but has no RFC 2119 keywords (`grep -cE '\b(MUST\|SHOULD\|MAY)\b' conformance/README.md` → 0) and no RFC. A spec draft is in open PR #15 and is not merged |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not yet | §6.1: .github/workflows/ci.yml runs `cargo test` and the Python unittest suite. No formatter or linter is pinned or run (`grep -nE 'fmt\|clippy\|ruff\|black\|flake8' .github/workflows/*.yml Cargo.toml bindings/python/pyproject.toml` → no match; no rustfmt.toml). Other clauses not assessed |
| ENG-STD-005 Change control | partial | GitHub ruleset `main-branch-integrity` active on the default branch since 2026-10-20: deletion, non_fast_forward, pull_request, required checks (`gh api repos/praveenprk/fid/rulesets/25491223`, 2026-11-15). Gaps: 0 of 43 non-merge commits carry an anchor (`git log --no-merges --format=%s bff71b4`). 20 non-merge commits went straight to main, the last 2d30e81 on 2026-10-18 (`git log --first-parent --no-merges bff71b4`). 23 commit messages carry Co-authored-by lines (`git log --format=%B bff71b4 \| grep -ciE 'co-authored-by'`). No hooks, no AGENTS.md |
| ENG-STD-006 Registers | not yet | No DECISIONS.md, VIOLATIONS.md, or ICS at bff71b4 (`git ls-tree -r --name-only bff71b4 \| grep -iE 'decision\|violation\|ics'` → none) |
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
