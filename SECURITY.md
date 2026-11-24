# Security policy

## Supported versions

eng-principles is not released yet; it has no tags. Only the current `main`
is supported.

## Reporting a vulnerability

Please report privately. Do not open a public issue.

Use GitHub's private vulnerability reporting:
**[Report a vulnerability](https://github.com/praveenprk/eng-principles/security/advisories/new)**
(the repository's Security tab → "Report a vulnerability").

If you cannot use GitHub, email the maintainer at
**justpraveenhere@protonmail.com**, with "eng-principles security" in the
subject.

Include:

- what is affected: the shared commit check, a hook, the audit or
  dashboard, or a rule in the standards;
- what an attacker can do, and the steps or input that show it;
- any fix you suggest.

You will get an answer in the advisory thread, or by email. Once a fix is
merged, the advisory is published with credit to you, unless you ask not to
be named.

## In scope

- **The shared commit check** (`.github/workflows/commit-check.yml` and
  `hooks/`). Other projects run it in their CI, pinned to a commit
  (ENG-DEC-009). A way to make it pass a commit it should refuse, or to run
  code it should not, is in scope.
- **The audit and dashboard** (`audit/`, `dashboard.yml`). This includes
  evidence from a private repository appearing on the public dashboard, and
  misuse of the token the audit reads with.
- **A rule whose wording lowers a security bar** that the CHARTER says may
  never be lowered.

## Not a vulnerability

- A project that does not meet a standard. That is a conformance gap: open
  an issue, or see the dashboard.
- The standards are reference models. They claim no certification
  (CHARTER: External Standards).
