# CONFORMANCE.md
# Cross-project conformance against ENG-STD-*
# Vocabulary: conformant / partial / not yet / n/a / not assessed (ENG-STD-006 §2.4)
# Every non-"not assessed" row cites evidence. Date of last update: 2026-11-23


## Maturity (ENG-STD-009)

One row per deliverable, each with the date it was read (ENG-STD-009 §4.2).

| Deliverable | Kind | Level | Read | Evidence (commit) | Blocks the next level |
|-------------|------|-------|------|-------------------|-----------------------|
| fid | software | L3 | 2026-11-23 | a460eab: release v0.2.0; tests incl. tests/conformance.rs; calibration results committed under calibration/results/; CI green | L4: a dated, committed record of runs in real use |
| phasectl | software | L3 | 2026-11-23 | b91611a: tag v0.1.0; SPEC-001..003 with tests; field-test runner (tests/field/); CI green | L4: field-test runs committed as a dated record |
| contextos | software | L3 | 2026-11-23 | c757698: 35 Python test files; CI green; daily use by the governor, not yet recorded | L4: a dated, committed record of runs in daily use |
| contextos factory | software | L2 | 2026-11-23 | contextos 53db88c: factory/supervisor.sh and factory/protocol/state-machine; one committed run, factory/gates/WID-20260520-001/transitions.log. No tests of the supervisor; other runs' records are in .factory/, git-ignored, which no one else can check | L3: tests of supervisor.sh against the state machine, passing on real work items |
| agent-dispatch-protocol | specification | L2 | 2026-11-23 | 5167c83: ADP-0/1/2; 101 conformance vector files checked against JSON schemas in CI; no implementation | L3: one implementation passes every vector (ADP issue #28) |
| factory-protocol | documentation | L2 | 2026-11-23 | 1340fa7: describes the contextos factory (row above) | L3: the factory reaches L3 |
| eng-principles audit | software | L3 | 2026-11-23 | d887b6c: audit/selftest.py in CI; runs daily against six real repositories; dashboard deployed to GitHub Pages. Runs are not committed: dashboard.yml deploys and commits nothing | L4: a dated, committed record of audit runs |
| eng-principles standards | documentation | L2 | 2026-11-23 | Takes the level of what it describes: the governed deliverables, lowest L2 (ADP, factory) | L3: every governed deliverable at L3 |

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

Read at 6262e06 (origin/main, 2026-11-16), after adoption (phasectl
DECISION-001, PR #12), RFC-001 (PR #13) and the shared commit check (PR #16).
Source of truth: phasectl docs/conformance/phasectl-ICS.md.
Before adoption, at cbdcfda: no RFC/SPEC, free-form commits, no hooks, no
registers.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | partial | docs/rfc/RFC-001 and docs/specs/SPEC-001..003, merged with tests before code (PR #13). Gaps: behaviour from before adoption has no RFC/SPEC (phasectl V-ENG-002-01, OPEN); PR #11 bypassed the gates (V-ENG-002-02, OPEN). phasectl's ICS still says not yet for this row |
| ENG-STD-003 Design / SOLID | partial | `LLMProvider` ABC (phasectl DECISION-004). Indexer is a plain binary contract (DECISION-003). README: progress to stderr, stdout clean |
| ENG-STD-004 Clean code | partial | CONTRIBUTING.md: why-only comments, no new deps without reason. Gaps: no linter or formatter in CI (V-ENG-004-02); api.py swallows an exception (V-ENG-004-01) |
| ENG-STD-005 Change control | conformant | .github/workflows/commit-check.yml calls eng-principles' shared check pinned to 74e7e76 (ENG-DEC-009). Ruleset `main-branch-integrity` requires `commit-check / check`, with linear history, no force push, no deletion (`gh api repos/praveenprk/phasectl/rulesets/25829218`, 2026-11-16). scripts/hooks/ vendored at 74e7e76, test 36/36. AGENTS.md. b3a2376 stays unanchored (phasectl V-ENG-005-02, resolved forward only) |
| ENG-STD-006 Registers | conformant | docs/DECISIONS.md (DECISION-001..006), docs/VIOLATIONS.md, docs/conformance/phasectl-ICS.md |
| ENG-STD-007 Quality model | not assessed | — |

The CONTRIBUTING.md gap noted before adoption ("no pytest suite yet") was
fixed in phasectl PR #12.

## agent-dispatch-protocol (ADP)

Renamed from adp-protocol on 2026-11-21 (governor); GitHub redirects the old
URL, and the Pages site moved to praveenprk.github.io/agent-dispatch-protocol/.
Read at 39abefb (origin/main, 2026-11-15). Registered by ENG-DEC-008.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not yet | ENG-STD-002 §5 (ENG-DEC-015) lets the project meet the gates through its own process. ADP-0 §5.1–§5.4 at 5167c83 is that process: proposal, then SPEC text, then conformance vectors with one passing and one failing per changed rule, then schema and implementation, then informative and register (`spec/ADP-0.md` §5.4). Missing: the project decision recording that mapping once (§5.2), including how the failing-vector-first exit (§5.3) is shown when §5.4 lets steps 1–3 land in one commit. No such decision found (`gh api search/code?q=ENG-STD-002+repo:praveenprk/agent-dispatch-protocol` → 0) |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | partial | ENG-STD-004 §0 (ENG-DEC-015) makes scripts/ci/, scripts/hooks/ and the `run:` steps of .github/workflows/adp.yml code. Met at 5167c83: §7.2, Python dependencies pinned in CI (`adp.yml` line 31: jsonschema==4.26.0, pyyaml==6.0.3) and actions pinned to commits. Gap: §6.1, no formatter or linter for Python or shell runs in CI (`adp.yml` runs only hook tests and the check scripts), and the project has not recorded which languages §6.1 binds (§0.2) |
| ENG-STD-005 Change control | partial | scripts/hooks/commit-msg, pre-push, test. AGENTS.md §Roles names the maintainer as the only one who merges. .github/workflows/adp.yml job `commits`. GitHub ruleset `adp-ruleset` active on the default branch: deletion, non_fast_forward, pull_request (merge only), required checks commits/schema/defects (`gh api repos/praveenprk/adp-protocol/rulesets/27276641`, 2026-11-15). Gap: 2 of 26 non-merge commits carry no anchor, 6042e27 and 739d2cb (`git log --no-merges --format='%h %s' 39abefb`), both from before ADP-0 |
| ENG-STD-006 Registers | not assessed | — Not decided by ENG-DEC-015. The project keeps DEFECTS.md (ADP-0 §4) and proposals/ in place of VIOLATIONS.md and DECISIONS.md, and has no ICS. DEFECTS.md holds 17 entries: 15 OPEN, 2 RESOLVED (ADP-D-005, ADP-D-012) (`git show 39abefb:DEFECTS.md \| grep -E '^Status +:' \| sort \| uniq -c`). Whether these registers satisfy §1 is not stated. Assessing it needs a governor ruling on whether DEFECTS.md and proposals/ stand in for VIOLATIONS.md and DECISIONS.md, and an ICS |
| ENG-STD-007 Quality model | not assessed | — |

## fid

Read at 24001db (main, 2026-11-16), after adoption (fid DECISION-001, PR #18)
and the shared commit check (fid DECISION-006, PR #20).
Registered by ENG-DEC-008. Source of truth: fid docs/conformance/fid-ICS.md.
Before adoption, at bff71b4: no SPEC, no registers, 0 of 43 non-merge
commits anchored, 23 with Co-authored-by lines (fid docs/VIOLATIONS.md).

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | conformant | spec/draft-kumar-fid-00.md is the RFC and SPEC (fid DECISION-001). Every normative section is tested or a listed gap, 31 traced (spec/TRACEABILITY.md, CI). `spec-ref` requires behaviour changes to cite the draft. Merged in fid #7 (c3768e1). Releases v0.1.0 and v0.1.1 predate the gate (fid V-ENG-002-01, resolved forward only) |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not yet | §6.1: no formatter or linter pinned or run in CI (fid V-ENG-004-01) |
| ENG-STD-005 Change control | conformant | .github/workflows/commit-check.yml calls eng-principles' shared check pinned to 74e7e76 (ENG-DEC-009, fid DECISION-006). Ruleset `main-branch-integrity` requires rust, python, spec, spec-ref, `commit-check / check` and GitGuardian, with linear history (`gh api repos/praveenprk/fid/rulesets/25491223`, 2026-11-16). History before adoption stays unanchored (fid V-ENG-005-01, -02, resolved forward only) |
| ENG-STD-006 Registers | partial | docs/DECISIONS.md, docs/VIOLATIONS.md, docs/conformance/fid-ICS.md, mapped onto spec/gaps.json and issues (fid DECISION-001). DECISION-001 is PROPOSED |
| ENG-STD-007 Quality model | not assessed | — |

## factory-protocol

Read at 1340fa7 (main, 2026-11-15). Registered by ENG-DEC-008.

| Standard | Status | Evidence |
|----------|--------|----------|
| ENG-STD-001 Language & IDs | not assessed | — |
| ENG-STD-002 Lifecycle gates | not yet | ENG-STD-002 §5.4 (ENG-DEC-015): a documentation-only project applies §3 with its trivial class recorded once. Missing at 1340fa7: that project decision; the repository has no DECISIONS.md (`git ls-files` lists LICENSE, NOTICE, README.md, factory-protocol.html, index.html) |
| ENG-STD-003 Design / SOLID | not assessed | — |
| ENG-STD-004 Clean code | not yet | The repository has no source tree, but index.html and factory-protocol.html each carry an inline `<script>` (`grep -c '<script' index.html factory-protocol.html` → 1, 1). Under ENG-STD-004 §0 (ENG-DEC-015) both are code. Missing at 1340fa7: no CI at all (no .github/ in `git ls-files`), so neither §6.1 nor a proportionate record of which languages it binds (§0.2) exists |
| ENG-STD-005 Change control | partial | GitHub ruleset `factory-protocol-ruleset` active on the default branch: deletion, non_fast_forward, pull_request, required checks (`gh api repos/praveenprk/factory-protocol/rulesets/27276808`, 2026-11-15). The only commit straight to main is 6767f6e "Initial commit" (`git log --first-parent --no-merges 1340fa7`). Gaps: 0 of 4 non-merge commits carry an anchor (e.g. 13ad193 "chore: license under Apache-2.0 with NOTICE"). No hooks, no AGENTS.md (`git ls-files`) |
| ENG-STD-006 Registers | not yet | No DECISIONS.md, VIOLATIONS.md, or ICS. `git ls-files` at 1340fa7 lists only LICENSE, NOTICE, README.md, factory-protocol.html, index.html |
| ENG-STD-007 Quality model | not assessed | — |
