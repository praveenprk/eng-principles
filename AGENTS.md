# AGENTS.md — eng-principles

Instructions for every automated contributor, whatever its model or tool.
This file is the protocol. Tool-specific files (CLAUDE.md and the like) only
point here (ENG-STD-005 §6).

This repository holds the cross-project engineering principles and standards.
Read CHARTER.md first.

- Principles and standards are append-only. Refine or supersede them. Never delete a rule or lower its bar (CHARTER: The bar).
- Every change to PRINCIPLES.md or standards/ needs a new ENG-DEC entry in DECISIONS.md.
- Do not mark anything `conformant` in CONFORMANCE.md without a cited test, commit, or file.
- Do not claim ISO/IEC certification or compliance. These standards are reference models only (ENG-DEC-004).
- Work on a branch named `type/ANCHOR-description`. Never commit to `main`.
- Commit format: `type(scope): description — ENG-…`. No co-author or AI attribution lines.
- Install the hooks before committing: `hooks/install`. Never bypass them (`--no-verify` is a violation).
- Roles (ENG-STD-005 §2.6, ENG-DEC-012), effective when the `stable` branch exists.
  Until then the governor alone merges into `main`. Merge into `main`: an automated
  contributor merges its pull request once every required check passes, no Q-NNN is
  OPEN, and the pull request is not labelled `security`; a `security` pull request
  waits for the governor, who merges it. Push to `main`: nobody; every change arrives
  by pull request. Promote `main` → `stable`: the human governor, with a merge commit,
  on a release record. Tag: the human governor, on `stable` only.
