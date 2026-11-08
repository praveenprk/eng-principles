# ENG-STD-005 — Change Control: Commits, Branches, Review
Status: ACTIVE · Refs: ISO/IEC/IEEE 12207 (configuration management), ISO 9001 §8.5.6 (control of changes) · Reference implementation: contextos CONVENTIONS.md, scripts/hooks/

## 1. Commit messages
1.1 Format: `type(scope): description — ANCHOR[, ANCHOR…]`
1.2 Types: `feat fix test refactor docs chore design`. Projects MAY add types (contextos adds `spec-test`, `connector`).
1.3 Every commit MUST carry at least one anchor that resolves to a governed entry
    in that project (RFC/SPEC/INV/V/DECISION) or in this repository (ENG-*).
1.4 Commits MUST NOT carry AI co-author or attribution lines. Accountability
    belongs to the human who signs (ENG-P-11).

## 2. Branches
2.1 Pattern: `type/ANCHOR-short-description` (e.g. `fix/V-002-03-audit-write-aborts`).
2.2 The default branch is protected. No direct pushes, no force-pushes.
2.3 Only a human merges.

## 3. Review
3.1 Every change to the default branch is reviewed before merge. An automated
    critic MAY review. A human approves.
3.2 A fix to a recorded violation updates the violation register in the same change.

## 4. Hardware change control
4.1 Each board revision has a change list mapping every modification to an anchor.
4.2 Released fabrication outputs (Gerbers, BOM, pick-and-place) are immutable.
    A change produces a new revision. Released files are never edited in place.

## 5. Releases
5.1 A release is a signed tag `vX.Y.Z` (SemVer). The tag message references the decisions and violations closed.

## 6. Agent instructions
6.1 Instructions for automated contributors MUST live in one tool-agnostic
    file at the repository root: `AGENTS.md`.
6.2 Tool-specific instruction files (e.g. `CLAUDE.md`) MAY exist only as
    adapters that point to `AGENTS.md`. They MUST NOT carry rules of their own.
6.3 Rules that bind agents also bind humans. `AGENTS.md` names who may push
    and merge. It never grants an agent more than a human contributor has.

## Enforcement
| Clause | Mechanism |
|--------|-----------|
| 1.1–1.4 | `hooks/commit-msg` (reference implementation, ENG-DEC-007) |
| 2.2 | Git host branch protection (authoritative) + `hooks/pre-push` (local guardrail) |
| 2.3, 3.x, 4.x, 6.x | Review |

Amended: 2026-11-08 — §6 added (ENG-DEC-006). Enforcement table points to reference hooks (ENG-DEC-007).
