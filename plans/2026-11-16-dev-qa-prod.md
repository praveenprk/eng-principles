# Plan — develop, qa, main: agent integrates, governor judges

Date    : 2026-11-16
Status  : PARKED (starts after the open items below are closed)
Anchor  : ENG-STD-005 §2
Owner   : PK (governor)

## Outcome

The agent keeps working without waiting on the governor for every merge.
The governor spends time only on judgment, in one place, with the questions
asked as real-world scenarios.

## Flow

| Branch | Who merges into it | What it holds | Governor's role |
|--------|--------------------|---------------|-----------------|
| `develop` | Agent, once the required checks pass | Integrated work, with open questions and pending judgments recorded, not resolved | None |
| `qa` | Agent opens the `develop` → `qa` PR; the governor merges | A batch ready for judgment | Answers the questions, gives judgments, accepts or sends back |
| `main` (prod) | Governor only | What is released | Merges `qa` → `main`, tags releases |

## Questions and judgments

- Every open question or pending judgment is recorded when the agent merges
  into `develop`, not left in chat. Where they live (a register file, or
  issues with a label) is decided in the ENG-DEC.
- Each is asked as a scenario: "A user does X in situation Y. Should the
  tool do A or B?" Each has the options, the agent's recommendation, and
  what changes with each answer.
- At `qa`, the governor answers each one. Answers become DECISION entries or
  severity confirmations in the project's registers, as today.
- Nothing reaches `main` with an open question.

## What has to change

1. **ENG-STD-005 §2.3** ("Only a human merges") is narrowed to: only a human
   merges into `qa` and the default branch. This needs a new ENG-DEC
   (standards are append-only: refine, never weaken without a decision).
2. **Host rules per project:** rulesets for `develop` (PR + required checks;
   the agent may merge), `qa` and `main` (PR + required checks; governor
   only).
3. **Agent guard** (governor-gate): allows merges into `develop` and feature
   branches; denies merges into `qa` and `main`.
4. **AGENTS.md** in each project: the flow, and where questions are recorded.
5. **Releases** (ENG-STD-005 §5): tags come from `main` only.

## Open design points (for the ENG-DEC)

- Squash or merge commits for `develop` → `qa` → `main` promotions, given
  that fid and phasectl require linear history on `main`.
- Whether `qa` is a long-lived branch or a release PR from `develop`.
- Where the questions register lives.

## Starts after

- phasectl V-ENG-004-02: CI runs tests, formatter, linter.
- fid V-ENG-004-01: formatter and linter pinned and run in CI.
- fid 0.2.0 release (DECISION-005).
