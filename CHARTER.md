# CHARTER.md
# Engineering — Charter
# Status: Living document. Append only. A rule may be refined. Its bar may never be lowered.
# Authority: Highest document in this repository.

---

## Purpose

This repository holds the engineering principles and standards that apply to
everything built under this practice: software, hardware, firmware,
documentation, and the processes that produce them.

It is a seed. It starts small and grows only by recorded decision.

**North Star** (aspiration, not a commitment to any programme): make
productive capability, intelligence, infrastructure and access to resources
steadily more abundant, affordable, safe, sustainable and widely owned, on
Earth and beyond it. We pursue this through systems whose claims rest on
physical reality and evidence, which people can inspect, repair, replace and
own, and whose benefits reach the people who use them. Ambition sets the
direction; measured evidence sets the pace (ENG-DEC-016).

## Grounding

The practice is grounded in **physical reality and evidence**: what a
system does in the world, measured, is what counts, and every claim rests on
evidence someone else can check (ENG-DEC-016).

For software, the ground is **Unix**: an ecosystem of small, composable
tools, joined by plain text, that run on anything from a coffee machine to a
space station (ENG-P-13).

The aim is **industrial discipline**, so that the process holds under
pressure, and **institutional truth**, so that what the records say is what
happened. Paradigms such as SOLID are tools within that ground, not the
ground itself.

## Scope

Every project, current and future. Current projects:

| Project   | Kind     | Location                         |
|-----------|----------|----------------------------------|
| contextos | software | ~/Desktop/contextos              |
| phasectl  | software | ~/Desktop/phasectl               |
| agent-dispatch-protocol (ADP) | specification | ~/Desktop/adp-protocol |
| fid       | software | ~/Desktop/fid                    |
| factory-protocol | documentation | ~/Desktop/factory-protocol |

New projects are added to CONFORMANCE.md on creation, not later.

## Authority Order

1. CHARTER.md
2. PRINCIPLES.md
3. standards/ENG-STD-*.md
4. A project's own governance documents (e.g. contextos KERNEL_SPEC.md, DISCIPLINE.md)

These are four layers (ENG-DEC-016):

| Layer | Holds | Lives in |
|-------|-------|----------|
| Portfolio doctrine | North Star, ground, principles, decision rules | CHARTER.md, PRINCIPLES.md |
| Domain standards | Software, hardware, and later AI, robotics, manufacturing, space | standards/ENG-STD-*.md, written only when a project in that domain exists |
| Product requirements | Mission, stakeholders, boundaries, guarantees | Each project, by its own process (ENG-STD-002 §5) |
| Implementation contracts | RFCs, specifications, interfaces, tests, evidence | Each project, by its own process |

**Never a runtime dependency.** No product depends on this repository to
build or run (ENG-DEC-007). The one exception is the shared commit check,
called at CI time pinned to a commit (ENG-DEC-009). A project chooses its
own language, architecture, process and specification format within these
rules.

A project's documents govern **what** that project is. This repository governs
**how** things are built. Where both speak to the same thing:

- **Tighten, never lower the bar.** A project MAY impose stricter rules. It
  MUST NOT relax a rule stated here.
- **Deviation is visible.** A project that cannot meet a standard records a
  waiver in its own decision register, citing the ENG-STD clause, the reason,
  and the condition under which the waiver ends. A silent deviation is a violation.

## Amendment

- All documents here are append-only in spirit: rules are refined or
  superseded, never deleted.
- Every change to a principle or standard has a DECISIONS.md entry.
- Uncertainty resolves in favour of the existing rule.
- **The bar.** A rule's bar is the evidence, traceability and accountability
  it demands. A rule may be refined; its bar may never be lowered. Changing
  who or what performs a step, or aligning a term with the meaning an
  external standard gives it, is a refinement when the bar is kept or
  raised. The decision making such a change states, for each of the three,
  why it is not lower (ENG-DEC-016).

## External Standards

ISO, IEC, IEEE, and IETF documents cited here are **reference models**. This
practice borrows their structure and vocabulary. It does not claim
certification or formal compliance with any of them. See REFERENCES.md for
exactly what is taken from each.

## Amendment Log

| Date       | Change          | Ref          |
|------------|-----------------|--------------|
| 2026-11-07 | Initial version | ENG-DEC-001  |
| 2026-11-08 | Grounding section: Unix, industrial discipline, institutional truth | ENG-DEC-005 |
| 2026-11-15 | Scope: add adp-protocol, fid, factory-protocol | ENG-DEC-008 |
| 2026-11-22 | Purpose: North Star, as aspiration | ENG-DEC-016 |
| 2026-11-22 | Grounding: physical reality and evidence; Unix as the software ground | ENG-DEC-016 |
| 2026-11-22 | "Never weakened" becomes "the bar may never be lowered", with the bar defined | ENG-DEC-016 |
| 2026-11-22 | Authority Order: four layers; never a runtime dependency | ENG-DEC-016 |
