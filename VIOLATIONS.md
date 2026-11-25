# VIOLATIONS.md — eng-principles
# Where this repository has broken its own rules (ENG-STD-006). Append-only:
# entries are never deleted; a resolved entry records the date and the commit
# that resolved it (§2.2). Severity follows ENG-STD-006 §2.3 and names its rule.
# Format: templates/violation.md, with "Rule says" for a rule of this repository.
#
# Only violations already on record are listed: each cites where it was found
# and what resolved it. The register was started on 2026-11-26.

### ENG-V-001
Rule says : ENG-STD-009 §2.3: "A level advances only when the acceptance
            criteria of the next level are met and the evidence is named at a
            commit, a record or a measurement."
Repo did  : PR #15 (merged 0e7ba68, 2026-11-22) placed the eng-principles
            audit at L5 and the contextos factory at L3 in the CONFORMANCE.md
            Maturity table. Neither had the evidence: no committed audit run
            record (L4), no use beyond the author (L5), and the factory's L3
            records were git-ignored. Found by an independent review of #15,
            recorded in ENG-DEC-018.
Severity  : MEDIUM — ENG-STD-006 §2.3 c: eng-principles' own rule; it changes
            no behaviour and touches no personal data
Impact    : Readers of the Maturity table trusted levels the evidence did not
            support
Fix       : Levels corrected (audit L3, factory L2, factory-protocol L2,
            standards L2), each row dated (ENG-DEC-018)
When      : PR #16
Status    : RESOLVED — 2026-11-22, f92be8c (PR #16)
Anchor    : ENG-STD-009, ENG-DEC-018

### ENG-V-002
Rule says : The redaction rule for private repositories (governor,
            2026-11-18; audit/render.py `public()`): a private repository
            keeps its name and statuses on the public dashboard, never
            evidence text or its HEAD commit.
Repo did  : dashboard.yml published the raw report.json to GitHub Pages,
            including evidence and HEAD for every repository it could read.
            Found and fixed in PR #29. No private evidence was published:
            the audit token could not read a private repository at any time
            before the fix (AUDIT_TOKEN was created after #29 merged, and
            contextos still read `readable: false`).
Severity  : HIGH — ENG-STD-006 §2.3 d: security-related (ENG-STD-005 §2.5),
            so never below HIGH; not CRITICAL, as no advisory applies and
            nothing private was exposed
Impact    : Once a token could read a private repository, its evidence and
            HEAD would have been public
Fix       : report.json published only through `render.py --public`
            (PR #29). An unreadable repository is also treated as private,
            so redaction never depends on readability (PR #33).
When      : PR #29, hardened in PR #33
Status    : RESOLVED — 2026-11-24, 030ed11 (PR #29)
Anchor    : ENG-STD-008

### ENG-V-003
Rule says : ENG-STD-004 §6.1, as enforced by the `lint` check (PR #21):
            Python is formatted by the pinned ruff. ENG-STD-006 §2.3: a rule
            is broken when what is on the default branch does not meet it.
Repo did  : A merge skew. PR #20 merged first (8d64fd2, 2026-11-24 17:18Z),
            with Python in audit/ that ruff would reformat; no formatting
            check existed yet. PR #21 merged 72 seconds later (8ac97b3,
            17:19Z) and made `ruff format --check` a check. Its CI run had
            not seen #20's code. From 8ac97b3, main failed `lint`. Found and
            fixed in PR #29.
Severity  : MEDIUM — ENG-STD-006 §2.3 c: eng-principles' own rule; no
            behaviour changed
Impact    : Every pull request failed `lint` until the fix merged
Fix       : audit/ formatted with the pinned ruff (PR #29). Guard against a
            repeat: the main ruleset's "require branches to be up to date
            before merging" (strict status checks, now off), the governor's
            setting
When      : PR #29
Status    : RESOLVED — 2026-11-24, 030ed11 (PR #29)
Anchor    : ENG-STD-004
