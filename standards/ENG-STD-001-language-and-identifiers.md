# ENG-STD-001 — Normative Language and Identifiers
Status: ACTIVE · Refs: RFC 2119, RFC 8174, ISO 8601, ISO/IEC/IEEE 24765, SemVer 2.0.0

## 1. Normative keywords
1.1 Requirements MUST use RFC 2119 keywords, interpreted per RFC 8174: they are
    normative only when written in UPPERCASE.
1.2 Authors MUST use MUST / MUST NOT for invariants, SHOULD / SHOULD NOT for defaults that
    may be departed from with a recorded reason, and MAY for options.
1.3 Normative documents (RFC, SPEC, STD) MUST NOT state implementation status.
    Status belongs in a conformance statement (ENG-STD-006).

## 2. Identifiers
2.1 Every governed entry MUST have a stable identifier that is never reused.
2.2 Repository-level IDs MUST carry the `ENG-` prefix so they never collide with project IDs:

| Kind       | Here (engineering) | In a project (e.g. contextos) |
|------------|--------------------|-------------------------------|
| Principle  | ENG-P-NN           | —                             |
| Standard   | ENG-STD-NNN        | —                             |
| Decision   | ENG-DEC-NNN        | DECISION-NNN                  |
| RFC / SPEC | —                  | RFC-NNN / SPEC-NNN            |
| Invariant  | —                  | INV-NNN-NN                    |
| Violation  | ENG-V-NNN          | V-NNN-NN                      |

2.3 IDs MUST NOT be renumbered. A retired ID stays retired.

## 3. Dates, times, versions
3.1 Dates MUST be ISO 8601 (`YYYY-MM-DD`). Timestamps MUST be ISO 8601 with a UTC offset.
3.2 Released artifacts MUST be versioned with SemVer 2.0.0. Hardware revisions
    SHOULD use `REV <letter>` for the board and SemVer for firmware.
3.3 Relative dates ("last week", "Thursday") MUST NOT appear in governed documents.
3.4 A project MUST stay at major version 0 (`0.y.z`) until the governor declares
    it market-ready in a project decision; `1.0.0` MUST NOT be released without
    that decision. Before it, a breaking change MUST bump the minor version and
    any other change MUST bump the patch version, as Cargo reads `0.y.z`.
    Versions already released at `1.0.0` or above keep their numbers and MUST
    NOT be renumbered (ENG-DEC-014).

## 4. Vocabulary
4.1 Where a term exists in ISO/IEC/IEEE 24765 (systems and software engineering
    vocabulary), it SHOULD be used in that sense; otherwise the local meaning
    MUST be defined explicitly.

## Enforcement
| Clause | Mechanism |
|--------|-----------|
| 2.x, 3.1 | Hook / CI regex (planned per project) |
| 1.x, 4.1 | Review |
| 3.4 | Review; only the governor tags releases (ENG-STD-005 §5.1) |

Amended: 2026-11-22 — §3.4 added: major version 0 until the governor declares a project market-ready (ENG-DEC-014).
Amended: 2026-11-22 — RFC 2119 keywords added to requirement clauses that lacked one, meaning unchanged (ENG-DEC-015, Q-004).
