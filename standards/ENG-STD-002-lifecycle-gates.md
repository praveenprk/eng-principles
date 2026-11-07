# ENG-STD-002 — Lifecycle Gates
Status: ACTIVE · Refs: ISO/IEC/IEEE 12207, ISO/IEC/IEEE 15288, ISO/IEC/IEEE 29148 · Reference implementation: contextos DISCIPLINE.md §3

## 1. The gate sequence
1.1 All work passes through five gates, in order. A gate MUST NOT open until the
    previous one is closed.

| # | Gate       | Software artifact                 | Hardware artifact                          | 15288 process (approx.)              |
|---|------------|-----------------------------------|--------------------------------------------|---------------------------------------|
| 1 | RFC        | RFC: problem, options, decision   | Same: need, constraints, options            | Stakeholder needs definition          |
| 2 | SPEC       | SPEC: fields, MUST/MUST NOT, out-of-scope | Requirements spec: electrical, mechanical, environmental limits | System requirements definition |
| 3 | TEST       | Failing tests derived from SPEC   | Verification plan: test points, fixtures, pass/fail limits | Verification (planned)    |
| 4 | BUILD      | Code that makes tests pass        | Schematic → layout → prototype             | Design definition, Implementation     |
| 5 | REFINE     | Refactor, same pass/xfail count   | Revision, DFM/DFT fixes, same verification | Integration, Verification (executed)  |

1.2 The gate names are fixed. A project MAY add gates (e.g. contextos adds
    DESIGN between SPEC and TEST). It MUST NOT remove or reorder gates.

## 2. Exit conditions (minimum)
2.1 **RFC closed:** problem statement, options considered, decision recorded,
    no open questions left unanswered.
2.2 **SPEC closed:** every requirement is falsifiable (ENG-P-02), includes an
    explicit out-of-scope statement, and follows ISO/IEC/IEEE 29148 characteristics
    (necessary, unambiguous, complete, singular, feasible, verifiable, traceable).
2.3 **TEST closed:** every MUST/MUST NOT has at least one test or inspection,
    known failures are marked expected-fail with a violation ID, and the suite runs.
2.4 **BUILD closed:** all non-expected-fail tests pass, and every change is anchored (ENG-STD-005).
2.5 **REFINE closed:** same pass and expected-fail counts as at BUILD close,
    no new violations, and registers updated.

## 3. Proportionality
3.1 Trivial changes (typos, formatting, dependency patch bumps with no behaviour
    change) MAY skip gates 1–3 but MUST still carry an anchor.
3.2 What counts as trivial is decided by the project's governor and recorded
    once as a project decision. It is not decided per change.

## 4. Backfill
4.1 Work found to have bypassed a gate: stop, open a CRITICAL violation, write the
    missing RFC/SPEC honestly (describing what was actually built), then continue.

## Enforcement
| Clause | Mechanism |
|--------|-----------|
| 2.3, 2.4 | CI test run |
| 1.1, 2.1, 2.2 | Governor review |
