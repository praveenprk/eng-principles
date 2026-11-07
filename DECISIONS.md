# DECISIONS.md
# Engineering — Decisions Register
# Append only. A decision may be superseded. It is never removed.
# Format: ID — Title | Date | Refs | Decision | Reason | Status

---

## ENG-DEC-001 — Establish a cross-project engineering repository

Date    : 2026-11-07
Refs    : CHARTER.md
Decision: One repository (`~/engineering`) holds the principles and standards
          for all projects, software and hardware. Projects inherit them,
          may tighten them, and may never silently weaken them.
Reason  : contextos built a strong discipline, but it lives inside one repo.
          phasectl, the second project, does not follow it. Without a shared
          source, every new project starts from zero.
Status  : ACCEPTED

---

## ENG-DEC-002 — `ENG-` prefix for repository-level identifiers

Date    : 2026-11-07
Refs    : ENG-STD-001 §2
Decision: All IDs in this repository are prefixed `ENG-` (ENG-P, ENG-STD,
          ENG-DEC, ENG-V).
Reason  : Avoids collision with project registers (contextos DECISION-001…038,
          V-NNN-NN) and makes a cross-project anchor recognisable in any commit.
Status  : ACCEPTED

---

## ENG-DEC-003 — contextos is the reference implementation; its agent roles stay project-local

Date    : 2026-11-07
Refs    : contextos DISCIPLINE.md, CONVENTIONS.md, DECISION-003, DECISION-007, DECISION-029
Decision: The gate sequence, append-only registers, anchored commits, ICS, and
          Pressure Clause are generalised from contextos into ENG-STD-002, 005,
          and 006 and ENG-P-05, 06, and 12. contextos's specific agent roles (Claude
          Chat / Claude Code / Cowork / PK) are NOT made universal. Each
          project defines its own roles within ENG-P-11.
Reason  : The process has been proven over 38 decisions and 80+ violations.
          The role split depends on contextos's tooling and would not fit
          small or hardware projects as written.
Status  : ACCEPTED

---

## ENG-DEC-004 — External standards are reference models, not certification targets

Date    : 2026-11-07
Refs    : CHARTER.md, REFERENCES.md
Decision: ISO/IEC/IEEE/IETF documents are cited for structure and vocabulary.
          REFERENCES.md states exactly what is taken from each and what is not.
Reason  : Claiming "ISO compliance" without audit would itself break ENG-P-06
          (honest state). Partial borrowing, declared explicitly, is honest.
Status  : ACCEPTED
