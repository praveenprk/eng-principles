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
2.3 Severity is CRITICAL, HIGH, MEDIUM or LOW. Grading MUST follow these
    rules, in order (ENG-DEC-013, replacing the earlier MUST/SHOULD grading):
    a. The violation matches an OpenSSF Scorecard check: that check's risk
       level (e.g. Branch-Protection High, Pinned-Dependencies Medium).
    b. Otherwise it matches an OpenSSF Best Practices passing-level
       criterion: MUST → HIGH, SHOULD → MEDIUM, SUGGESTED → LOW.
    c. Otherwise it is the project's or eng-principles' own rule: HIGH if
       it changes behaviour, affects personal data, or breaks a compliance
       obligation; otherwise MEDIUM, or the governor rules.
    d. A security-related violation (ENG-STD-005 §2.5) is never below HIGH,
       whatever a–c give. It is CRITICAL when a known vulnerability (a CVE
       or advisory) is present in released code.
    A rule is broken when what is on the default branch or released does
    not meet it. The severity entry names the rule (a–d) and its source.
2.4 Conformance status vocabulary: `conformant` / `partial` / `not yet` / `n/a`.
    `conformant` requires evidence (test ID or commit). `not assessed` is allowed only in the cross-project CONFORMANCE.md.
    Refined by ENG-DEC-015: a project's own ICS MAY also use `not
    assessed`. Each such row MUST state why it is not assessed and what
    assessing it needs. A `not assessed` row without both is a violation
    of this clause.
2.5 One fact lives in one register. No parallel trackers (contextos DECISION-004).

## 3. Cross-project conformance
3.1 This repository's CONFORMANCE.md records each project's status against each ENG-STD.
3.2 It is updated whenever a project's adoption state changes, with evidence.
Amended: 2026-11-22 — §2.3 severity graded by OpenSSF placement, then impact; security never below HIGH (ENG-DEC-013).
Amended: 2026-11-22 — §2.4 refined: `not assessed` in a project ICS, with a reason (ENG-DEC-015, Q-001).
