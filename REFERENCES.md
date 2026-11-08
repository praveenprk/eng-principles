# REFERENCES.md
# External standards register — what is taken from each, and what is not.

These are reference models (CHARTER: External Standards). No certification is claimed.

| Reference | What we take | Where used | Not taken |
|-----------|--------------|------------|-----------|
| Unix philosophy (McIlroy, BSTJ 1978; Kernighan & Pike, 1984) | One job per tool, text streams, composition, quiet success | ENG-P-13, ENG-STD-003 §0 | — |
| POSIX — IEEE Std 1003.1 / ISO/IEC/IEEE 9945 | Portable shell, utilities, and system interface as the baseline substrate | ENG-STD-003 §0.6 | Full conformance testing |
| RFC 2119 + RFC 8174 | MUST/SHOULD/MAY semantics, uppercase-only | ENG-STD-001 | — |
| ISO 8601 | Date/time format | ENG-STD-001 | — |
| SemVer 2.0.0 | Release versioning | ENG-STD-001, 005 | — |
| ISO/IEC/IEEE 24765 | Shared vocabulary | ENG-STD-001 | — |
| ISO/IEC/IEEE 12207 | Software lifecycle process names; configuration management | ENG-STD-002, 005 | Full process set, tailoring formalities |
| ISO/IEC/IEEE 15288 | System (incl. hardware) lifecycle stages | ENG-STD-002 | Full process set |
| ISO/IEC/IEEE 29148 | Characteristics of good requirements | ENG-STD-002 §2.2 | Document templates |
| ISO/IEC/IEEE 42010 | Stakeholders, concerns, and views for architecture | ENG-STD-003 §7 | Formal ADL/metamodel |
| SOLID (Martin) | Five design rules, made testable. One expression of the Unix ground, not the ground | ENG-STD-003 §1–5 | — |
| Clean Code (Martin) | Naming, functions, comments, errors | ENG-STD-004 | Numeric dogma; our limits are defaults |
| ISO/IEC 25010:2023 | Nine product-quality characteristics | ENG-STD-007 | Quality-in-use model (for now) |
| ISO/IEC/IEEE 29119 | Test vocabulary, test-basis traceability | ENG-STD-007 | Documentation set |
| ISO 9001:2015 | Control of changes (§8.5.6), documented information (§7.5) | ENG-STD-005, 006 | QMS certification |
| ISO/IEC 27001:2022 | Statement of Applicability shape → ICS | ENG-STD-006 | ISMS |
| ISO/IEC 9646, RFC 7942 | Implementation conformance statement | ENG-STD-006 | — |
| IEC 61508 | Hazard analysis structure for safety-relevant hardware | ENG-STD-007 §3 | SIL certification |
| IPC-2221 | Generic PCB design rules | ENG-STD-004 §6.2 | — |
| IEC 60617 | Schematic graphical symbols | ENG-STD-004 | — |
