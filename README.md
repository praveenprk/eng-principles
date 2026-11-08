# engineering

The engineering principles and standards for everything built here: software,
hardware, firmware, docs, and process. Projects inherit these rules. They may
make them stricter, and they may never make them weaker without saying so.

## Read in this order
1. [CHARTER.md](CHARTER.md): scope, authority, how this repo changes
2. [PRINCIPLES.md](PRINCIPLES.md): 13 principles, Unix discipline first, each with a check
3. [standards/](standards/): the enforceable rules
4. [REFERENCES.md](REFERENCES.md): which ISO/IEC/IEEE/IETF standards we borrow from, and what we leave out
5. [CONFORMANCE.md](CONFORMANCE.md): where each project stands, with evidence
6. [DECISIONS.md](DECISIONS.md): why this repository is the way it is

## Standards
| ID | Topic |
|----|-------|
| [ENG-STD-001](standards/ENG-STD-001-language-and-identifiers.md) | Normative language, IDs, dates, versions |
| [ENG-STD-002](standards/ENG-STD-002-lifecycle-gates.md) | RFC → SPEC → TEST → BUILD → REFINE (software + hardware) |
| [ENG-STD-003](standards/ENG-STD-003-design.md) | Unix discipline (ground), interface contracts, SOLID |
| [ENG-STD-004](standards/ENG-STD-004-construction-clean-code.md) | Clean code, clean schematics |
| [ENG-STD-005](standards/ENG-STD-005-change-control.md) | Commits, branches, review, hardware revisions |
| [ENG-STD-006](standards/ENG-STD-006-registers-and-conformance.md) | DECISIONS / VIOLATIONS / ICS registers |
| [ENG-STD-007](standards/ENG-STD-007-quality-model.md) | ISO/IEC 25010 quality model, safety |

## Adopting in a new project
1. Copy `templates/` into the project's `docs/`.
2. Create DECISIONS.md, VIOLATIONS.md, and an ICS (ENG-STD-006).
3. Copy `hooks/` into the project (e.g. `scripts/hooks/`), edit `anchors`,
   `types`, and `protected` for the project's registers, then run `hooks/test`
   and `scripts/hooks/install`.
4. Put agent instructions in `AGENTS.md`. Tool-specific files only point to it (ENG-STD-005 §6).
5. Add a section for the project to [CONFORMANCE.md](CONFORMANCE.md).

## Changing this repository
Every change needs an ENG-DEC entry. Commits follow ENG-STD-005 with ENG-* anchors.
