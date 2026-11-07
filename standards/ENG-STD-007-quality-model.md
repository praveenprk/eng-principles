# ENG-STD-007 — Product Quality Model
Status: ACTIVE · Refs: ISO/IEC 25010:2023, ISO/IEC/IEEE 29119 (testing), IEC 61508 (functional safety, hardware where applicable)

## 1. Quality characteristics
1.1 Every SPEC SHOULD state which ISO/IEC 25010 characteristics it constrains and
    how each is measured. Characteristics with no stated constraint are explicitly "no requirement".

| Characteristic (25010:2023) | Example falsifiable requirement |
|-----------------------------|---------------------------------|
| Functional suitability | Every SPEC invariant has a passing test |
| Performance efficiency | p95 latency of X ≤ N ms at M rps; idle current ≤ N µA |
| Compatibility | Works with providers A, B, C via one interface |
| Interaction capability | Every CLI command has `--help` and a non-zero exit on error |
| Reliability | Recovers from crash without data loss (ledger replay) |
| Security | Secrets never written to logs; fail closed on auth error |
| Maintainability | ENG-STD-004 limits hold; coverage ≥ project floor |
| Flexibility | Runs on macOS + Linux; vendor swap touches adapters only |
| Safety | Hazard list exists; each hazard has a mitigation and a test |

## 2. Release review
2.1 Before a release, the governor walks the table for the changed scope and
    records the result in the release notes. A row without evidence is `not yet`, not omitted.

## 3. Safety-relevant hardware
3.1 Hardware that can cause injury, fire, or property damage MUST have a hazard
    analysis before BUILD (ENG-STD-002 gate 4). IEC 61508 is the reference model
    for structure. Formal SIL assessment is out of scope unless a project's decision register adopts it.
