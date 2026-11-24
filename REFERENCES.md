# REFERENCES.md
# External standards register — what is taken from each, and what is not.

These are reference models (CHARTER: External Standards). No certification is claimed.

Each row names its source and how far it was verified (ENG-DEC-019): **primary**, read at the
source; **abstract-only**, paywalled and read from the official listing or abstract;
**secondary**, not seen at the source; **unverified**, no adequate source read. Dates are 2026-11-23
unless stated. Standards to be bought are in docs/PROCUREMENT.md. iso.org refuses automated
reads (HTTP 403), so ISO editions are confirmed by a human or through a national body.

| Reference | What we take | Where used | Not taken | Source | Verified (level, date) |
|-----------|--------------|------------|-----------|--------|------------------------|
| Unix philosophy (McIlroy, BSTJ 1978; Kernighan & Pike, 1984) | One job per tool, text streams, composition, quiet success | ENG-P-13, ENG-STD-003 §0 | — | [BSTJ 57(6) 1978, pp. 1899–1904](https://archive.org/details/bstj57-6-1899) (free); Kernighan & Pike 1984: book | secondary: the article is free at the link; not re-read 2026-11-23. Book: procurement |
| POSIX — IEEE Std 1003.1 / ISO/IEC/IEEE 9945 | Portable shell, utilities, and system interface as the baseline substrate | ENG-STD-003 §0.6 | Full conformance testing | [Open Group Base Specifications Issue 8 = IEEE Std 1003.1-2024](https://pubs.opengroup.org/onlinepubs/9799919799/) (free online) | edition: primary; content not re-read |
| RFC 2119 + RFC 8174 | MUST/SHOULD/MAY semantics, uppercase-only | ENG-STD-001 | — | [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) | primary (contextos, 2026-11-07; reachable 2026-11-23) |
| ISO 8601 | Date/time format | ENG-STD-001 | — | iso.org (returned 403 to automated reads) | unverified: edition not confirmed. Procurement |
| SemVer 2.0.0 | Release versioning | ENG-STD-001, 005 | — | [semver.org 2.0.0](https://semver.org/spec/v2.0.0.html) (free) | secondary: free at the link; not re-read |
| ISO/IEC/IEEE 24765 | Shared vocabulary | ENG-STD-001 | — | [SEVOCAB](https://pascal.computer.org/sev_display/index.action), IEEE Computer Society and ISO/IEC JTC 1/SC 7 (definitions free) | secondary: SEVOCAB serves the definitions; edition (2017 front matter linked) not confirmed |
| ISO/IEC/IEEE 12207 | Software lifecycle process names; configuration management | ENG-STD-002, 005 | Full process set, tailoring formalities | iso.org/standard/90219 | secondary: 12207:2026 (Ed. 2) is in force per contextos (2026-11-08); iso.org returned 403. Procurement |
| ISO/IEC/IEEE 15288 | System (incl. hardware) lifecycle stages | ENG-STD-002 | Full process set | iso.org (returned 403) | unverified: edition not confirmed. Procurement |
| ISO/IEC/IEEE 29148 | Characteristics of good requirements | ENG-STD-002 §2.2 | Document templates | iso.org/standard/72089 | abstract-only: 29148:2018, per contextos (2026-11-07); the characteristics list itself unverified. Procurement |
| ISO/IEC/IEEE 42010 | Stakeholders, concerns, and views for architecture | ENG-STD-003 §7 | Formal ADL/metamodel | iso.org (returned 403) | unverified: edition not confirmed. Procurement |
| SOLID (Martin) | Five design rules, made testable. One expression of the Unix ground, not the ground | ENG-STD-003 §1–5 | — | Martin, books | secondary. Procurement |
| Clean Code (Martin) | Naming, functions, comments, errors | ENG-STD-004 | Numeric dogma; our limits are defaults | Martin, Clean Code (2008), book | secondary. Procurement |
| ISO/IEC 25010:2023 | Nine product-quality characteristics | ENG-STD-007 | Quality-in-use model (for now) | iso.org (returned 403) | unverified: the nine characteristics not read at source. Procurement |
| ISO/IEC/IEEE 29119 | Test vocabulary, test-basis traceability | ENG-STD-007 | Documentation set | iso.org (returned 403) | unverified. Procurement |
| ISO 9001:2015 | Control of changes (§8.5.6), documented information (§7.5) | ENG-STD-005, 006 | QMS certification | iso.org (returned 403) | unverified: clause numbers §8.5.6, §7.5 not read at source. Procurement |
| ISO/IEC 27001:2022 | Statement of Applicability shape → ICS | ENG-STD-006 | ISMS | iso.org (returned 403) | unverified. Procurement |
| ISO/IEC 9646, RFC 7942 | Implementation conformance statement | ENG-STD-006 | — | [RFC 7942](https://www.rfc-editor.org/rfc/rfc7942); ISO/IEC 9646: iso.org | RFC: secondary, free, not re-read. 9646: unverified |
| RFC 7942 | Judging a specification by its implementations | ENG-STD-009 §3.2 | The Implementation Status section format | [RFC 7942](https://www.rfc-editor.org/rfc/rfc7942) (free) | secondary: free at the link; not re-read |
| IEC 61508 | Hazard analysis structure for safety-relevant hardware | ENG-STD-007 §3 | SIL certification | [IEC 61508-1:2010 Ed. 2.0](https://webstore.iec.ch/en/publication/5515), CHF 380 | edition and price: primary (2026-11-23); content: secondary. Procurement |
| IPC-2221 | Generic PCB design rules | ENG-STD-004 §6.2 | — | ipc.org | unverified. Procurement |
| IEC 60617 | Schematic graphical symbols | ENG-STD-004 | — | IEC 60617 database (subscription) | unverified. Procurement |
| OSTEP (Arpaci-Dusseau, Operating Systems: Three Easy Pieces) | Operating systems as first prior art: scheduling, isolation, protection, recovery | ENG-P-14 | — | [pages.cs.wisc.edu/~remzi/OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) (free) | secondary: free at the link; the governor holds the PDF |
