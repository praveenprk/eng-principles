# CONFORMANCE.md
# Cross-project conformance against ENG-STD-*
# Vocabulary: conformant / partial / not yet / n/a / not assessed (ENG-STD-006 §2.4)
# Every non-"not assessed" row cites evidence. Date of last update: 2026-11-07

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
