# ENG-STD-003 — Design: Unix Discipline, Interface Contracts, SOLID
Status: ACTIVE · Refs: Unix philosophy (McIlroy, 1978), POSIX (IEEE Std 1003.1 / ISO/IEC/IEEE 9945), SOLID (R. C. Martin), ISO/IEC/IEEE 42010 · Related: ENG-P-07, ENG-P-13, contextos DECISION-003 (no formal DbC) · Refined by: ENG-DEC-005

The ground is Unix: small tools, plain text, composition. Interface contracts
make the composition safe. SOLID is one way to express the same discipline
inside a single codebase. It is a means, not the foundation.

Every rule here is testable, and each has a hardware equivalent where one
applies.

## 0. Unix discipline (the ground)

0.1 **One tool, one job.** A tool, module, or board MUST state its purpose in
    one sentence. A second "and…" means split it.
0.2 **Text is the interface.** Inputs, outputs, configuration, and records
    SHOULD be plain text: line-oriented, human-readable, diffable. A
    machine format (e.g. `--json`) is an addition, never a replacement.
0.3 **Compose.** A tool MUST read from stdin or named files, write results to
    stdout, and write diagnostics to stderr. stdout stays clean for piping.
0.4 **Quiet on success, loud on failure.** A tool prints nothing unasked on
    success. On failure it says what failed and exits non-zero.
0.5 **Exit codes are contract.** 0 means success. Every non-zero code a tool
    can return is documented.
0.6 **Smallest substrate.** Each tool MUST state the smallest environment it
    runs on: POSIX shell, libc, interpreter, MCU class, RAM. It MUST NOT need
    more than it declares. Platform specifics live behind an adapter
    ("coffee machine to space station").
0.7 **Mechanism, not policy.** Tools provide mechanism. Policy lives in
    plain-text configuration the operator owns.
0.8 **Built to be replaced.** Any tool can be swapped for another that
    honours the same text contract (Liskov at system scale, §3).
0.9 *Hardware:* a device exposes a line-oriented text console (serial/UART
    or equivalent) for status and diagnostics. Status codes are documented
    like exit codes. Boards compose through standard buses.

**Check:** `tool < input > out 2> err; echo $?` behaves as documented. The
tool runs on its declared minimum substrate in CI or on a bench.

## 1. S — Single Responsibility
1.1 A module MUST have one reason to change, stated in one sentence in its header or contract.
1.2 *Hardware:* a functional block (power, MCU, I/O, comms) MUST be separable
    on the schematic by sheet or hierarchical block.
**Check:** the stated sentence describes the module accurately. A second "and…" means split it.

## 2. O — Open/Closed
2.1 New behaviour SHOULD be added by extension (new implementation of an
    existing interface, new phase file, new connector) and not by editing a stable core.
2.2 *Hardware:* expansion goes through defined headers or buses, not by reworking the core layout.
**Check:** adding a provider, connector, or variant touches no core file other than a registry.

## 3. L — Liskov Substitution
3.1 Every implementation of an interface MUST pass the same contract test suite.
3.2 *Hardware:* a substitute part MUST satisfy the original part's datasheet
    limits used in the design (second-source rule, ENG-P-10).
**Check:** a shared contract test runs against every implementation.

## 4. I — Interface Segregation
4.1 Interfaces MUST expose only what their consumers use. Split wide interfaces by consumer.
4.2 *Hardware:* connectors and buses carry only the signals that cross the boundary.
**Check:** no consumer implements stubs that raise "not supported" for half an interface.

## 5. D — Dependency Inversion
5.1 Core logic MUST depend on interfaces it owns, not on vendor SDKs, drivers, or concrete stores.
5.2 *Hardware:* firmware core logic depends on a HAL, not on register addresses.
**Check:** vendor imports appear only in adapter modules.

## 6. Interface contracts
6.1 Every public interface (API endpoint, CLI command, module boundary, connector,
    board-to-board link) MUST document:
    - **Accepts:** inputs, preconditions, ranges, units
    - **Guarantees:** outputs, postconditions, timing, invariants
    - **Refuses:** rejected inputs and the exact error, code, or state produced
6.2 Refusals MUST be explicit and tested (ENG-P-08).
6.3 For a CLI tool, the contract includes stdin/stdout/stderr usage and every
    exit code (§0.3–0.5).

## 7. Architecture description
7.1 Each project SHOULD keep one ARCHITECTURE.md that names its stakeholders, their
    concerns, and the views that address those concerns (ISO/IEC/IEEE 42010 structure, lightweight).
