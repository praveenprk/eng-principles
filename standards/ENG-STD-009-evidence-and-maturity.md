# ENG-STD-009 — Evidence and Maturity
Status: ACTIVE (ENG-DEC-017) · Refs: RFC 7942 (Implementation Status), IETF BCP 14 (RFC 2119, RFC 8174), ENG-P-02, ENG-P-06

## 1. Purpose
1.1 A maturity level says how far a deliverable's claims are backed by
    evidence. It is meant to be read the same way by a contributor, a
    partner and an auditor.
1.2 The levels are internal classifications. They are not certification
    levels. RFC 7942 is a reference model (CHARTER: External
    Standards).

## 2. The levels
2.1 A deliverable MUST be placed at exactly one level:

| Level | Name | Evidence that places it there |
|-------|------|-------------------------------|
| L0 | Vision | The intended outcome is written down |
| L1 | Scientific feasibility | Basic principles are known; a concept is formulated; prior art is searched (ENG-P-14) |
| L2 | Engineering feasibility | A critical function is proven analytically or experimentally, or a component works in a laboratory |
| L3 | Demonstrated prototype | Critical functions are demonstrated in a relevant environment |
| L4 | Integrated validation | The system performs in its operational environment |
| L5 | Operational deployment | The complete system is qualified and proven in operation |
| L6 | Replicable, sustainable scale | It is replicated and sustained beyond its first operation, at the scale it meets |

2.2 No equivalence to Technology Readiness Levels is claimed. A mapping
    to TRL is added only in the change that records a check against the
    defining standard's own text (ENG-DEC-018, Q-016).
2.3 A level advances only when the acceptance criteria of the next level
    are met and the evidence is named at a commit, a record or a
    measurement. Agent confidence, presentation quality, code volume, or
    simulation alone MUST NOT advance a level.
2.4 A level MAY go down. When evidence is lost or contradicted, the level
    drops in the same change that records it (ENG-P-06).

## 3. Reading the levels per kind of deliverable
3.1 **Software.** A relevant environment is real inputs; an operating
    environment is real use, the governor's own daily use included.
    - L3: it passes its tests on real inputs.
    - L4: it runs in a real operating environment, and a dated, committed
      record of runs, inputs, results and issues shows it.
    - L5: it is used beyond its author, and incidents are tracked.
    - L6: it just works at any scale it meets.
3.2 **Specification.** A specification is judged by its implementations
    (after RFC 7942).
    - L2: every rule is decidable: conformance vectors pass or fail it.
    - L3: one implementation passes every vector.
    - L4: two independent implementations interoperate.
    - L5: implementers other than the authors run it in production.
    - L6: it is stable and widely adopted.
3.3 **Documentation.** A document takes the level of what it describes. A
    page describing an untested process is at that process's level,
    however well it is written. A document that describes several
    deliverables, such as a set of standards, takes the lowest of their
    levels (ENG-DEC-018, Q-017).
3.4 **Hardware and physical systems.** §2.1 applies as written. A domain
    standard MAY refine it when a project in that domain exists (CHARTER:
    Authority Order).

## 4. Where levels are recorded
4.1 A level belongs to a deliverable, not a repository. A repository that
    holds two deliverables records two levels.
4.2 Levels MUST be recorded in one place: the Maturity table in
    CONFORMANCE.md, one row per deliverable, with the level, the evidence
    at a named commit, the date read, and what blocks the next level
    (ENG-STD-006 §2.5).

## 5. Verification

| Clause | Verified by |
|--------|-----------|
| 2.1, 2.3, 4.2 | Review of each change to the Maturity table: every level cites evidence at a commit |
| 2.4 | Review; a contradicted claim is a violation of ENG-P-06 |

Amended: 2026-11-23 — TRL column and ISO 16290 citation held until checked against the standard's text (ENG-DEC-018, Q-016).
Amended: 2026-11-23 — §3.3: a document describing several deliverables takes the lowest of their levels (ENG-DEC-018, Q-017).
