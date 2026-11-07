# ENG-STD-003 — Design: SOLID and Interface Contracts
Status: ACTIVE · Refs: SOLID (R. C. Martin), ISO/IEC/IEEE 42010 · Related: ENG-P-07, contextos DECISION-003 (no formal DbC)

SOLID is stated here as **testable rules**, each with a hardware equivalent.
Contracts are expressed as accepts / guarantees / refuses (ENG-P-07), not in
formal Design-by-Contract tooling, consistent with contextos DECISION-003.

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

## 7. Architecture description
7.1 Each project SHOULD keep one ARCHITECTURE.md that names its stakeholders, their
    concerns, and the views that address those concerns (ISO/IEC/IEEE 42010 structure, lightweight).
