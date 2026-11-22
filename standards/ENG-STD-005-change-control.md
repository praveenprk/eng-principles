# ENG-STD-005 — Change Control: Commits, Branches, Review
Status: ACTIVE · Refs: ISO/IEC/IEEE 12207 (configuration management), ISO 9001 §8.5.6 (control of changes) · Reference implementation: contextos CONVENTIONS.md, scripts/hooks/

## 1. Commit messages
1.1 Format: `type(scope): description — ANCHOR[, ANCHOR…]`
1.2 Types: `feat fix test refactor docs chore design`. Projects MAY add types (contextos adds `spec-test`, `connector`).
1.3 Every commit MUST carry at least one anchor that resolves to a governed entry
    in that project (RFC/SPEC/INV/V/DECISION) or in this repository (ENG-*).
1.4 Commits MUST NOT carry AI co-author or attribution lines. Accountability
    belongs to the human who signs (ENG-P-11).
1.5 §1.1–1.4 MUST be checked on the git host for everything a change brings
    to the default branch: the pull request's title and description, and
    every non-merge commit, whatever the merge method. A local hook alone
    does not satisfy §1.

## 2. Branches
2.1 Pattern: `type/ANCHOR-short-description` (e.g. `fix/V-002-03-audit-write-aborts`).
2.2 The default branch is protected. No direct pushes, no force-pushes.
2.3 Only a human merges.
    Refined by ENG-DEC-012 (superseding ENG-DEC-010's develop and qa): an
    automated contributor MAY merge a pull request into the default branch
    (`main`) once the required checks pass and no question is OPEN, unless
    the change is security-related (§2.5). Only a human merges into
    `stable` and merges security-related changes.
2.4 A project runs two long-lived branches, as Rust does with `main` and
    `stable`:
    - `main`, the default branch: integration. Every pull request targets
      it, from a work branch (§2.1).
    - `stable`: what is released. It changes only by a pull request from
      `main`, merged with a merge commit, by a human.
    Nothing is committed to either directly. A question for the governor
    is added to docs/QUESTIONS.md (templates/question.md) by the pull
    request that raises it; the governor answers on that pull request. A
    pull request into `main` MUST NOT merge while any entry is OPEN.
2.5 A change is security-related when it touches: vulnerability reports
    or fixes (SECURITY.md, an advisory, a dependency bumped for a known
    vulnerability); credentials, secrets or workflow token permissions;
    branch rules or required checks; or code that authenticates,
    authorizes, encrypts, signs or checks integrity. It carries the label
    `security`, and only a human merges it.

## 3. Review
3.1 Every change to the default branch is reviewed before merge. An automated
    critic MAY review. A human approves.
    Refined by ENG-DEC-012: on `main`, the required checks and an automated
    critic review each change; a human approves each promotion to `stable`
    and each security-related change (§2.5).
3.2 A fix to a recorded violation updates the violation register in the same change.

## 4. Hardware change control
4.1 Each board revision has a change list mapping every modification to an anchor.
4.2 Released fabrication outputs (Gerbers, BOM, pick-and-place) are immutable.
    A change produces a new revision. Released files are never edited in place.

## 5. Releases
5.1 A release is a signed tag `vX.Y.Z` (SemVer). The tag message references the decisions and violations closed.
    The tag is on `stable` (ENG-DEC-012).

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
| 1.1–1.5 | `.github/workflows/commit-check.yml` on the git host, required by the project's branch rules (authoritative, ENG-DEC-009) + `hooks/commit-msg` locally (optional, the same code, ENG-DEC-007) |
| 2.2 | Git host branch protection (authoritative) + `hooks/pre-push` (local guardrail) |
| 2.3 | Git host rules per branch (authoritative) + the agent's merge guard + review |
| 2.4 | `commit-check.yml` job `questions`, required on `main` (authoritative, ENG-DEC-010, ENG-DEC-012) + host rules + review |
| 2.5 | `security` label; the agent's local guard refuses to merge a pull request carrying it; review |
| 3.x, 4.x, 6.x | Review |

Amended: 2026-11-08 — §6 added (ENG-DEC-006). Enforcement table points to reference hooks (ENG-DEC-007).
Amended: 2026-11-16 — §1.5 added: commit rules checked on the git host by one shared workflow (ENG-DEC-009).
Amended: 2026-11-17 — §2.3 refined and §2.4 added: develop, qa, main flow with a questions register (ENG-DEC-010).
Amended: 2026-11-22 — §2.3, §2.4, §3.1, §5.1 refined and §2.5 added: `main` and `stable`, work branches, security changes merged by a human (ENG-DEC-012, superseding ENG-DEC-010's develop and qa).
