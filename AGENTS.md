# AGENTS.md — eng-principles

Instructions for every automated contributor, whatever its model or tool.
This file is the protocol. Tool-specific files (CLAUDE.md and the like) only
point here (ENG-STD-005 §6).

This repository holds the cross-project engineering principles and standards.
Read CHARTER.md first.

- Principles and standards are append-only. Refine or supersede them. Never delete or weaken a rule.
- Every change to PRINCIPLES.md or standards/ needs a new ENG-DEC entry in DECISIONS.md.
- Do not mark anything `conformant` in CONFORMANCE.md without a cited test, commit, or file.
- Do not claim ISO/IEC certification or compliance. These standards are reference models only (ENG-DEC-004).
- Work on a branch named `type/ANCHOR-description`. Never commit to `main`.
- Commit format: `type(scope): description — ENG-…`. No co-author or AI attribution lines.
- Install the hooks before committing: `hooks/install`. Never bypass them (`--no-verify` is a violation).
- Roles (ENG-STD-005 §2.6). Merge into `main`: the human governor only, because this
  repository has not yet moved to `main` and `stable` (ENG-DEC-012); an automated
  contributor does not merge here. Push to `main`: the human governor only. Release:
  none yet (the repository is untagged); when it is, a human releases on a release record.
