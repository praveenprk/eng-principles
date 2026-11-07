# ENG-STD-006 — Registers and Conformance
Status: ACTIVE · Refs: ISO/IEC 9646 (PICS), RFC 7942, ISO/IEC 27001 Statement of Applicability, ISO 9001 §7.5 (documented information) · Reference implementation: contextos docs/DECISIONS.md, docs/VIOLATIONS.md, docs/conformance/ContextOS-ICS.md

## 1. Required registers
Every project MUST keep three registers. All three are append-only.

| Register       | Answers                                   | Template |
|----------------|-------------------------------------------|----------|
| DECISIONS.md   | What was decided, why, and at what known risk? | templates/decision.md |
| VIOLATIONS.md  | Where does the artifact not meet its own spec? | templates/violation.md |
| CONFORMANCE.md (ICS) | Which requirements are met, and with what evidence? | templates/ics.md |

## 2. Rules
2.1 Entries are never deleted. Superseded decisions are marked SUPERSEDED and point to their replacement.
2.2 A resolved violation records the date and the commit or revision that resolved it.
2.3 Severity: CRITICAL (a MUST is broken now), HIGH (a MUST is degraded),
    MEDIUM (a SHOULD is broken), LOW (debt). Grading MUST follow these definitions.
2.4 Conformance status vocabulary: `conformant` / `partial` / `not yet` / `n/a`.
    `conformant` requires evidence (test ID or commit). `not assessed` is allowed only in the cross-project CONFORMANCE.md.
2.5 One fact lives in one register. No parallel trackers (contextos DECISION-004).

## 3. Cross-project conformance
3.1 This repository's CONFORMANCE.md records each project's status against each ENG-STD.
3.2 It is updated whenever a project's adoption state changes, with evidence.
