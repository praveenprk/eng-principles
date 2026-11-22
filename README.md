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
| [ENG-STD-008](standards/ENG-STD-008-contributor-readiness.md) | Contributor readiness: what an experienced OSS contributor expects; measured on the [dashboard](https://praveenprk.github.io/eng-principles/) |
| [ENG-STD-009](standards/ENG-STD-009-evidence-and-maturity.md) | Evidence and maturity: L0–L6, mapped to TRL, read per kind of deliverable |

## Adopting in a new project
1. Copy `templates/` into the project's `docs/`.
2. Create DECISIONS.md, VIOLATIONS.md, and an ICS (ENG-STD-006).
3. Put the project's `types` and `anchors` in `scripts/hooks/` (copy them
   from `hooks/` and edit for the project's registers; add an `ISSUE - -`
   line if issues are anchors). Call the shared check from a workflow,
   pinned to a full commit SHA (ENG-DEC-009, ENG-STD-005 §1.5):
   ```yaml
   on:
     pull_request:
       types: [opened, synchronize, reopened, edited]
   jobs:
     commit-check:
       uses: praveenprk/eng-principles/.github/workflows/commit-check.yml@<sha>
       with:
         config: scripts/hooks
   ```
   Then require `commit-check / check` in the default branch's rules.
   Optional, for feedback before pushing: copy `hooks/` itself into
   `scripts/hooks/`, run `hooks/test` and `scripts/hooks/install`.
4. Put agent instructions in `AGENTS.md`. Tool-specific files only point to it (ENG-STD-005 §6).
5. Add a section for the project to [CONFORMANCE.md](CONFORMANCE.md).
6. Branches `main` (default) and `stable` (ENG-STD-005 §2.3–2.5, ENG-DEC-012):
   create `stable` at the latest release; rules on `main` (pull request,
   required checks, squash or rebase, linear history) and on `stable`
   (pull request, required checks, merge commits only); `docs/QUESTIONS.md`
   from templates/question.md; a `Q` line in `anchors`; require
   `commit-check / questions` on `main`; a `security` label; say in
   AGENTS.md who merges where.

## Changing this repository
Every change needs an ENG-DEC entry. Commits follow ENG-STD-005 with ENG-* anchors.
