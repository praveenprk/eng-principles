# PRINCIPLES.md
# Engineering — Core Principles
# Status: Append only. A principle may be refined. It may never be weakened or removed.

Each principle has a statement, a reason, and a **check**: how anyone can
tell whether it is being followed. A principle without a check is a wish.

IDs are never renumbered. ENG-P-13 was added after ENG-P-01..12, but it is
the ground the others rest on, so it is listed first.

---

## ENG-P-13 — Unix discipline (the ground)
Build small tools that do one thing, speak plain text, compose through
pipes, stay quiet on success, fail loudly, and run on the smallest substrate
they can.
**Why:** Small composable parts outlive frameworks, vendors, and paradigms.
Plain text outlives every file format. A tool that runs on a coffee machine
also runs on a space station.
**Check:** ENG-STD-003 §0. Each tool states its purpose in one sentence, its
I/O contract, its exit codes, and its minimum substrate, and all four hold.

---

## ENG-P-01 — Intent before artifact
Write down the problem and the contract before building the thing.
**Why:** Code, boards, and enclosures are expensive to change once they exist. Written intent is cheap to change.
**Check:** Every non-trivial artifact traces to a written requirement (RFC/SPEC or equivalent). See ENG-STD-002.

## ENG-P-02 — Every rule is falsifiable
A requirement that cannot fail a test or an inspection is not a requirement.
**Why:** Untestable rules turn into opinion, and opinion gives way under pressure.
**Check:** Each MUST/MUST NOT has at least one test, inspection, or measurement bound to it.

## ENG-P-03 — Every change is traceable
Every change carries a reason that resolves to a governed entry.
**Why:** Without a recorded reason, history is just a sequence of diffs, and no one can tell why anything changed.
**Check:** Commit and revision messages carry an anchor that resolves. See ENG-STD-005.

## ENG-P-04 — Enforce mechanically
A rule that a machine can check is checked by a machine (hook, CI, linter, DRC/ERC).
**Why:** Willpower erodes. A rule kept in a hook keeps holding when attention lapses.
**Check:** Each standard lists which of its clauses are machine-enforced and which are reviewed.

## ENG-P-05 — History is append-only
Decisions, violations, and principles are superseded, never deleted.
**Why:** Rewriting history destroys the evidence needed to understand present state.
**Check:** Registers contain no deletions. Superseded entries point forward.

## ENG-P-06 — Honest state
Known gaps are recorded (VIOLATIONS register, xfail tests, ICS `not yet`). A
conformance claim needs evidence.
**Why:** A system that hides its defects cannot be trusted about anything else.
**Check:** No `conformant` mark without a test or commit reference.

## ENG-P-07 — Interfaces are contracts
Every module, service, board, and connector publishes what it **accepts**,
what it **guarantees**, and what it **refuses**.
**Why:** Sharp interfaces let parts change on either side without the change spreading.
**Check:** Public interfaces have a contract section. Refusals are explicit, not undefined behaviour.

## ENG-P-08 — Fail closed
When a check cannot complete, the system refuses rather than proceeds.
**Why:** A failure that leaks is worse than a failure that halts.
**Check:** Error paths are tested. Default states (software flags, hardware pull-ups/resets) are the safe state.

## ENG-P-09 — Fewest moving parts
Add no dependency, component, abstraction, or process without a stated reason.
**Why:** Every part is a liability: something that can fail, be compromised, or need maintenance.
**Check:** New dependencies and new BOM parts are justified in the change that adds them.

## ENG-P-10 — Substrate independence
Core guarantees do not depend on a particular vendor, model, tool, or part.
**Why:** Vendors, models, and parts change faster than the guarantees they are meant to support.
**Check:** Vendor-specific code sits behind an interface. Critical parts have a second source or a documented single-source risk.

## ENG-P-11 — A human is accountable
At every threshold where consequences outlast the moment, a named human signs off.
AI and automation contribute. They do not hold authority.
**Why:** Accountability has to rest with someone who can be held to it.
**Check:** Merges, releases, and hardware sign-offs carry a human approver.

## ENG-P-12 — Pressure does not open gates
Deadlines, demos, customers, and "just this once" are not bypass conditions.
**Why:** If pressure can open a gate, the gate offers no protection.
**Check:** Work done without an open gate is recorded as a CRITICAL violation and backfilled honestly.

---

## Amendment Log

| Date       | Change                                    | Ref         |
|------------|-------------------------------------------|-------------|
| 2026-11-07 | Initial 12 principles, derived from contextos practice | ENG-DEC-001, ENG-DEC-003 |
| 2026-11-08 | Add ENG-P-13 Unix discipline as the ground | ENG-DEC-005 |
