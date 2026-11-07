# CHARTER.md
# Engineering — Charter
# Status: Living document. Append only. A rule may be refined. It may never be weakened.
# Authority: Highest document in this repository.

---

## Purpose

This repository holds the engineering principles and standards that apply to
everything built under this practice: software, hardware, firmware,
documentation, and the processes that produce them.

It is a seed. It starts small and grows only by recorded decision.

## Scope

Every project, current and future. Current projects:

| Project   | Kind     | Location                         |
|-----------|----------|----------------------------------|
| contextos | software | ~/Desktop/contextos              |
| phasectl  | software | ~/Desktop/phasectl               |

New projects are added to CONFORMANCE.md on creation, not later.

## Authority Order

1. CHARTER.md
2. PRINCIPLES.md
3. standards/ENG-STD-*.md
4. A project's own governance documents (e.g. contextos KERNEL_SPEC.md, DISCIPLINE.md)

A project's documents govern **what** that project is. This repository governs
**how** things are built. Where both speak to the same thing:

- **Tighten, never weaken.** A project MAY impose stricter rules. It MUST NOT
  relax a rule stated here.
- **Deviation is visible.** A project that cannot meet a standard records a
  waiver in its own decision register, citing the ENG-STD clause, the reason,
  and the condition under which the waiver ends. A silent deviation is a violation.

## Amendment

- All documents here are append-only in spirit: rules are refined or
  superseded, never deleted.
- Every change to a principle or standard has a DECISIONS.md entry.
- Uncertainty resolves in favour of the existing rule.

## External Standards

ISO, IEC, IEEE, and IETF documents cited here are **reference models**. This
practice borrows their structure and vocabulary. It does not claim
certification or formal compliance with any of them. See REFERENCES.md for
exactly what is taken from each.

## Amendment Log

| Date       | Change          | Ref          |
|------------|-----------------|--------------|
| 2026-11-07 | Initial version | ENG-DEC-001  |
