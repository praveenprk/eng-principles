# Contributing to eng-principles

Thank you for looking. This repository holds the engineering principles and
standards that every project here inherits. The full rules for every
contributor, human or automated, are in [AGENTS.md](AGENTS.md). This page is
the short version.

## Before you start

- **Read [CHARTER.md](CHARTER.md).** A rule may be refined; its bar may never
  be lowered (CHARTER: The bar).
- **Is it already known?** Check the [issues](https://github.com/praveenprk/eng-principles/issues),
  [DECISIONS.md](DECISIONS.md) and [docs/QUESTIONS.md](docs/QUESTIONS.md).

## How a change gets in

1. **Questions first.** A change that needs the governor's judgment opens a
   `Q-NNN` entry in docs/QUESTIONS.md, with options and a recommendation, and
   a `PROPOSED` ENG-DEC entry in DECISIONS.md. The `questions` check fails
   while any entry is OPEN; that is intended.
2. **The governor answers on the pull request.** Only then is the answer
   recorded and the decision marked ACCEPTED. A contributor never marks a
   question answered. Text applied before the answer is marked "pending Q-NNN".
3. **Every change to PRINCIPLES.md or standards/** has an ENG-DEC entry and an
   Amended or Amendment Log line.

## Your pull request

- **Branch:** `type/ANCHOR-description`, from `main`. Never commit to `main`.
- **Title and every commit:** `type(scope): description — ANCHOR`.
  - Types: feat, fix, test, refactor, docs, chore, design.
  - An anchor is a register entry that exists: `ENG-DEC-016`, `ENG-STD-009`,
    `ENG-P-14`, `Q-016`.
- **Install the hooks once per clone:** `hooks/install`. Never bypass them.
- **No co-author or tool-attribution lines** in commits or the description.
- **Merging:** the human governor merges into `main` (AGENTS.md: Roles).

## Checks you can run locally

```sh
sh hooks/test                 # hook tests
sh hooks/check-questions      # fails while a question is OPEN
python3 audit/selftest.py     # audit self-test, offline
```

## Citations

Cite an external standard only as far as you have read it, and say how far
(REFERENCES.md). Do not copy licensed text.
