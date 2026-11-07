# ENG-STD-004 — Construction: Clean Code and Clean Schematics
Status: ACTIVE · Refs: Clean Code (R. C. Martin), ISO/IEC 25010 (maintainability), IPC-2221, IEC 60617

Rules are falsifiable. Where a number is given, it is a default. A project MAY
tighten it, or MAY loosen it only by recorded waiver (CHARTER: Deviation is visible).

## 1. Naming
1.1 Names MUST state intent in the domain's vocabulary. No unexplained abbreviations except well-known ones (id, url, i2c).
1.2 Booleans read as predicates (`is_signed`, `has_provenance`).
1.3 *Hardware:* every net that leaves a sheet MUST be named. Names describe function (`VBAT_SENSE`, `I2C1_SDA`), not pin numbers.

## 2. Functions and modules
2.1 A function does one thing at one level of abstraction.
2.2 Default limits: function ≤ 40 lines, ≤ 4 parameters, nesting ≤ 3. Exceeding these needs a stated reason in review.
2.3 Pure decision logic is separated from I/O (contextos DECISION-001 pattern: one read, one pure decision).
2.4 No flag arguments that switch behaviour. Write two functions.

## 3. Comments
3.1 Comments explain **why**, not what. (Already the phasectl style rule.)
3.2 A comment that restates the code MUST be deleted. A comment that contradicts the code is a defect.
3.3 Requirement references in code use anchors (`# INV-007-01`), so a grep finds every implementation site.

## 4. Errors
4.1 Errors MUST NOT be silently swallowed. Each catch either handles the error, adds context and re-raises, or refuses (fail closed, ENG-P-08).
4.2 Error messages state what failed, with which input, and what the caller can do.

## 5. Tests
5.1 Tests are first-class code under the same rules.
5.2 Test names state the requirement under test (`test_inv_001_03_rejected_claim_never_reaches_resolver`).
5.3 Expected-fail tests MUST cite a violation ID. Skips without a reason are not permitted.

## 6. Formatting and static checks
6.1 Each project MUST pin one formatter and one linter per language and run them in CI. Style debates end there.
6.2 *Hardware:* ERC and DRC MUST pass with zero unwaived errors before fabrication. Waivers are listed in the revision notes.

## 7. Dependencies
7.1 Every new dependency or BOM part is justified in the change that adds it (ENG-P-09).
7.2 Versions are pinned for applications. Libraries declare ranges.

## Enforcement
| Clause | Mechanism |
|--------|-----------|
| 2.2, 6.1 | Linter / formatter in CI |
| 6.2 | EDA tool ERC/DRC |
| 5.3 | CI grep: every xfail has a V-ID |
| 1, 3, 4 | Review |
