# QUESTIONS.md — eng-principles

Open questions for the governor, one entry per question, in the format of
templates/question.md. This repository runs the register it gives every
project (ENG-DEC-010, refined by ENG-DEC-012; ENG-STD-005 §2.4): an entry is
added by the pull request that raises it, the governor answers on that pull
request, and the `questions` check (hooks/check-questions, run by
.github/workflows/governance.yml through commit-check.yml) fails while any
entry is OPEN. An answer that changes a standard becomes an ENG-DEC entry in
DECISIONS.md. Entries are never deleted (ENG-STD-006 §2.1).

---

### Q-001
Scenario : A maintainer fills in fid's conformance statement and reaches
           ENG-STD-003. Nobody has yet checked fid against the design rules,
           so the maintainer writes `not assessed`, as fid-ICS.md (5 rows) and
           phasectl-ICS.md (2 rows) already do, and as audit/projects.json
           does for agent-dispatch-protocol's `registers` check. ENG-STD-006
           §2.4 says `not assessed` is allowed only in the cross-project
           CONFORMANCE.md, so every one of those rows breaks the standard,
           and the only honest alternatives are a guess or `not yet`.
Options  : A — Refine ENG-STD-006 §2.4: a project ICS MAY use `not assessed`;
               each such row MUST state why it is not assessed and what
               assessing it needs. Changes: §2.4 gains one sentence;
               existing fid and phasectl rows become conformant once they
               carry a reason (follow-up in those repositories);
               CONFORMANCE.md and the audit are unchanged.
           B — Keep §2.4 as written: project ICS files MUST NOT use `not
               assessed`. Changes: none here; fid and phasectl replace each
               such row with an assessed status (`not yet` with what is
               missing, at least); the audit's ADP `registers` override is
               cross-project and stays.
Recommend: A, because §2.4 today forbids what both project ICS files and this
           repository's own audit already write, and B pushes maintainers to
           write `not yet` for rows nobody has looked at, which states a
           finding that was never made (ENG-P-06). A tightens the use with a
           mandatory reason rather than loosening it, and ENG-STD-008 §3.1
           already uses `not assessed` for a check the audit cannot read.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : OPEN

### Q-002
Scenario : A contributor wants to change a rule in agent-dispatch-protocol, a
           repository that holds a specification and its conformance
           vectors, not a product. ENG-STD-002 §1 says every change passes
           RFC → SPEC → TEST → BUILD → REFINE, but does not say what an RFC
           or a BUILD is in a repository whose deliverable is the text
           itself. ADP-0 §5.4 has its own process (proposal → normative text
           → conformance vectors → schema/implementation → informative
           artifacts and registers). CONFORMANCE.md leaves ENG-STD-002
           `not assessed` for agent-dispatch-protocol and factory-protocol
           for this reason; fid conforms only through its own DECISION-001.
Options  : A — Add ENG-STD-002 §5 "Equivalent change processes": a
               specification project MAY satisfy §1 through its own process
               when it records the mapping once as a project decision (RFC ↔
               proposal; SPEC ↔ normative text before and after; TEST ↔
               conformance vectors, at least one passing and one failing per
               changed rule; BUILD ↔ schema or reference implementation;
               REFINE ↔ informative artifacts and registers). The order of
               §1.1 MUST be kept. A documentation-only project applies §3
               (proportionality) with its trivial class recorded once.
               Reference implementation: ADP-0 §5.4. Changes: ENG-STD-002
               gains §5; the ENG-STD-002 rows for agent-dispatch-protocol and
               factory-protocol can be graded (agent-dispatch-protocol still
               has to record its mapping decision).
           B — No equivalence: specification and documentation projects
               keep RFC/SPEC/TEST/BUILD/REFINE artifacts under those names.
               Changes: none here; agent-dispatch-protocol and
               factory-protocol are graded `not yet` against §1 until they
               add those artifacts.
           C — Declare ENG-STD-002 `n/a` for specification and
               documentation projects. Changes: §1 gains an exclusion; the
               two rows become `n/a`. This weakens a rule (CHARTER:
               Amendment), so it needs the governor to accept that
               explicitly.
Recommend: A, because §1.2 already lets a project add gates but not
           rename them, so a spec project cannot conform today however
           disciplined its process; ADP-0 §5.4 already runs the same order
           under other names; and A keeps the gate order and the
           failing-test-first rule, so nothing is weakened.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : OPEN

### Q-003
Scenario : A contributor opens factory-protocol, a documentation repository
           with no source tree, and finds index.html and
           factory-protocol.html each carrying an inline `<script>`. In
           agent-dispatch-protocol they find `run:` steps in
           .github/workflows/ and shell under scripts/ci/. Does ENG-STD-004
           (naming, error handling, a pinned formatter and linter) apply to
           those lines? CONFORMANCE.md leaves ENG-STD-004 `not assessed` for
           both repositories for this reason.
Options  : A — Code is any executable text: source files, scripts, inline
               `<script>` in documents, and `run:` steps in CI workflows.
               ENG-STD-004 applies to all of it, proportionately (a
               two-line `run:` step is held to §4 errors and §7
               dependencies, not to a separate formatter). Changes: a scope
               paragraph in ENG-STD-004; the factory-protocol and
               agent-dispatch-protocol ENG-STD-004 rows can be graded.
           B — Code is only what lives in a source tree (src/, lib/, a
               package). Changes: a scope paragraph in ENG-STD-004
               excluding everything else; the two rows become `n/a`.
               Executable text outside a source tree is then unreviewed by
               any standard.
Recommend: A, because a script runs whether or not it sits in src/; a `run:`
           step that swallows an error (ENG-STD-004 §4.1) breaks CI the same
           way, and an inline script ships to every reader of the page.
           "Proportionately" keeps it from demanding a linter for two
           lines; that is the same latitude ENG-STD-002 §3 already gives.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : OPEN

### Q-004
Scenario : A reviewer checks a project against ENG-STD-005 and finds the
           default branch unprotected. ENG-STD-001 §1.1 says a requirement
           is normative only when written with an UPPERCASE RFC 2119
           keyword, and §2.2 reads "The default branch is protected." with
           no keyword. By this repository's own rule that sentence is a
           description, not a requirement, and the project can argue it
           broke nothing. The scan below finds the same gap in clauses of
           all eight standards.
Options  : A — Add a keyword to every numbered requirement clause that lacks
               one, without changing its meaning: absolutes ("only", "is
               protected", "is immutable", "every", "never", "no …") become
               MUST / MUST NOT; stated defaults become SHOULD. Changes: the
               clauses listed below, each standard gains an `Amended:` line;
               nothing is renumbered and the PR body carries a before/after
               table.
           B — Leave the text as is and refine ENG-STD-001 §1.1 so that
               numbered clauses in standards/ are normative whatever their
               case. Changes: one sentence in ENG-STD-001; no other text
               changes, but MUST and SHOULD can no longer be told apart in
               those clauses, so every one of them reads as MUST.
           C — Answer A, but clause by clause for the ones marked J below,
               where the governor picks MUST or SHOULD.
Recommend: A, with the governor ruling the J clauses (that is, C for those
           only), because A is the rule ENG-STD-001 §1.1 already states and
           only makes the text match it; B would erase the MUST/SHOULD
           distinction the standards depend on (ENG-STD-001 §1.2). For J
           clauses the recommended keyword is given, but the choice changes
           what a project must do, so it is the governor's.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : OPEN

Clauses with a requirement and no RFC 2119 keyword, scanned at 3ed6f10
(`J` = MUST versus SHOULD is a real judgment; `!` = see the note below the
table). Clauses that already carry a keyword for every requirement they state
are not listed. Purely definitional or informative sentences (ENG-STD-008
§1.1, §1.2, §2.3) are not listed.

| Standard | Clause | Text today (shortened) | Keyword proposed |
|----------|--------|------------------------|------------------|
| ENG-STD-001 | §1.2 | "Use MUST / MUST NOT for invariants, SHOULD … MAY for options." | MUST use |
| ENG-STD-001 | §2.1 | "Every governed entry has a stable, never-reused identifier." | MUST have |
| ENG-STD-001 | §2.2 | "Repository-level IDs carry the `ENG-` prefix" | MUST carry |
| ENG-STD-001 | §3.4 | "A project stays at major version 0 … `1.0.0` is released only with that decision … never renumbered" | MUST stay; MUST NOT release `1.0.0` without; MUST bump; MUST NOT renumber |
| ENG-STD-001 | §4.1 J | "use it in that sense, or define the local meaning explicitly" | SHOULD use … or MUST define |
| ENG-STD-002 | §2.1–§2.5 | "RFC closed: problem statement, options …" (exit conditions, five clauses) | a gate MUST NOT close until … (each) |
| ENG-STD-002 | §3.2 | "decided by the project's governor and recorded once … It is not decided per change." | MUST be decided … and recorded; MUST NOT be decided per change |
| ENG-STD-002 | §4.1 ! | "Work found to have bypassed a gate: stop, open a CRITICAL violation, write the missing RFC/SPEC …" | MUST stop, open, write |
| ENG-STD-003 | §0.2 | "A machine format … is an addition, never a replacement." (first sentence already SHOULD) | MUST NOT replace |
| ENG-STD-003 | §0.3 | "stdout stays clean for piping." (rest already MUST) | MUST stay |
| ENG-STD-003 | §0.4 J | "A tool prints nothing unasked on success. On failure it says what failed and exits non-zero." | SHOULD print nothing; MUST exit non-zero |
| ENG-STD-003 | §0.5 | "0 means success. Every non-zero code … is documented." | MUST mean; MUST be documented |
| ENG-STD-003 | §0.6 J | "Platform specifics live behind an adapter" (rest already MUST) | SHOULD live |
| ENG-STD-003 | §0.7 J | "Tools provide mechanism. Policy lives in plain-text configuration the operator owns." | SHOULD |
| ENG-STD-003 | §0.8 J | "Any tool can be swapped for another that honours the same text contract" | SHOULD be replaceable |
| ENG-STD-003 | §0.9 J | Hardware: "a device exposes a line-oriented text console … Status codes are documented" | SHOULD expose; MUST document |
| ENG-STD-003 | §2.2 | Hardware: "expansion goes through defined headers or buses" (pairs §2.1 SHOULD) | SHOULD go |
| ENG-STD-003 | §4.2 | Hardware: "connectors and buses carry only the signals that cross the boundary" (pairs §4.1 MUST) | MUST carry only |
| ENG-STD-003 | §5.2 | Hardware: "firmware core logic depends on a HAL" (pairs §5.1 MUST) | MUST depend |
| ENG-STD-003 | §6.3 | "For a CLI tool, the contract includes stdin/stdout/stderr usage and every exit code" | MUST include |
| ENG-STD-004 | §1.2 J | "Booleans read as predicates" | SHOULD read |
| ENG-STD-004 | §1.3 | Hardware: "Names describe function …, not pin numbers." (first sentence already MUST) | MUST describe |
| ENG-STD-004 | §2.1 J | "A function does one thing at one level of abstraction." | SHOULD do |
| ENG-STD-004 | §2.2 | "Default limits … Exceeding these needs a stated reason in review." | SHOULD stay within; exceeding MUST state a reason |
| ENG-STD-004 | §2.3 J | "Pure decision logic is separated from I/O" | SHOULD be separated |
| ENG-STD-004 | §2.4 J | "No flag arguments that switch behaviour." | MUST NOT (absolute) or SHOULD NOT |
| ENG-STD-004 | §3.1 | "Comments explain why, not what." | SHOULD explain |
| ENG-STD-004 | §3.3 | "Requirement references in code use anchors" | MUST use |
| ENG-STD-004 | §4.2 J | "Error messages state what failed, with which input, and what the caller can do." | SHOULD state |
| ENG-STD-004 | §5.1 | "Tests are first-class code under the same rules." | MUST follow the same rules |
| ENG-STD-004 | §5.2 J | "Test names state the requirement under test" | SHOULD state |
| ENG-STD-004 | §5.3 | "Skips without a reason are not permitted." (first sentence already MUST) | MUST NOT skip without a reason |
| ENG-STD-004 | §7.1 | "Every new dependency or BOM part is justified in the change that adds it" | MUST be justified |
| ENG-STD-004 | §7.2 J | "Versions are pinned for applications. Libraries declare ranges." | MUST pin; SHOULD declare ranges |
| ENG-STD-005 | §1.1 | "Format: `type(scope): description — ANCHOR`" | MUST follow |
| ENG-STD-005 | §1.2 | "Types: feat fix …" (adding types already MAY) | MUST be one of |
| ENG-STD-005 | §2.1 | "Pattern: `type/ANCHOR-short-description`" | MUST follow |
| ENG-STD-005 | §2.2 | "The default branch is protected. No direct pushes, no force-pushes." | MUST be protected; MUST NOT allow direct pushes or force-pushes |
| ENG-STD-005 | §2.3 ! | "Only a human merges." with its ENG-DEC-012 refinement ("Only a human merges into `stable` and merges security-related changes") | MUST on the refined text only |
| ENG-STD-005 | §2.4 | "`stable` … changes only by a pull request from `main` … by a human. Nothing is committed to either directly." (last sentence already MUST NOT) | MUST change only by; MUST NOT commit directly |
| ENG-STD-005 | §2.5 | "It carries the label `security`, and only a human merges it." | MUST carry; MUST be merged only by a human |
| ENG-STD-005 | §3.1 ! | "Every change to the default branch is reviewed before merge … A human approves." with its ENG-DEC-012 refinement | MUST on the refined text only |
| ENG-STD-005 | §3.2 | "A fix to a recorded violation updates the violation register in the same change." | MUST update |
| ENG-STD-005 | §4.1 | Hardware: "Each board revision has a change list …" | MUST have |
| ENG-STD-005 | §4.2 | Hardware: "Released fabrication outputs … are immutable … never edited in place." | MUST NOT be edited |
| ENG-STD-005 | §5.1 | "A release is a signed tag `vX.Y.Z` … The tag is on `stable`" | MUST be; MUST reference; MUST be on |
| ENG-STD-005 | §6.3 | "Rules that bind agents also bind humans. AGENTS.md names who may push and merge. It never grants …" | MUST bind; MUST name; MUST NOT grant |
| ENG-STD-006 | §2.1 | "Entries are never deleted. Superseded decisions are marked SUPERSEDED …" | MUST NOT be deleted; MUST be marked |
| ENG-STD-006 | §2.2 | "A resolved violation records the date and the commit …" | MUST record |
| ENG-STD-006 | §2.3 | "The severity entry names the rule (a–d) and its source." (grading already MUST) | MUST name |
| ENG-STD-006 | §2.4 | "`conformant` requires evidence … `not assessed` is allowed only in …" (second sentence: see Q-001) | MUST cite evidence |
| ENG-STD-006 | §2.5 | "One fact lives in one register. No parallel trackers." | MUST live; MUST NOT keep |
| ENG-STD-006 | §3.1 | "This repository's CONFORMANCE.md records each project's status …" | MUST record |
| ENG-STD-006 | §3.2 | "It is updated whenever a project's adoption state changes, with evidence." | MUST be updated |
| ENG-STD-007 | §2.1 | "the governor walks the table … A row without evidence is `not yet`, not omitted." | MUST walk; MUST be `not yet` |
| ENG-STD-008 | §2.1 | "Each check has an id, a level …, and the project kinds …" | MUST have |
| ENG-STD-008 | §2.2 | "The checks are implemented in audit/audit.py … CI fails if they differ." | MUST be implemented; MUST list the same ids |
| ENG-STD-008 | §3.1 | "Each check reports pass, fail, n/a, or not assessed … never passed or failed." | MUST report; MUST NOT be passed or failed |
| ENG-STD-008 | §3.2 | "Only the governor rules on a check … A ruling is recorded in audit/projects.json" | MUST rule only; MUST be recorded |
| ENG-STD-008 | §3.3 | "A project registers its gaps as violations …" | MUST register |
| ENG-STD-008 | §4.1 | "dashboard.yml runs the audit daily and on every merge …, and publishes" | MUST run; MUST publish |
| ENG-STD-008 | §4.2 | "A private repository shows its name and statuses only, never evidence." | MUST NOT show evidence |

Notes on the `!` clauses:
- ENG-STD-005 §2.3 and §3.1: the ruling A7 as first drafted said to make
  "Only a human merges" a MUST. ENG-DEC-012 has since refined both clauses
  (an automated contributor MAY merge into `main`; a human approves each
  promotion to `stable` and each security-related change). A MUST on the
  base sentence would contradict that refinement, so the keyword goes on the
  refined text only and the base sentence stays as history.
- ENG-STD-002 §4.1 says to open a CRITICAL violation. ENG-STD-006 §2.3 (ENG-
  DEC-013) now grades our own rules HIGH or MEDIUM, and CRITICAL only for a
  known vulnerability in released code. Adding MUST to §4.1 as written would
  make two MUST clauses disagree on the severity. Q-004 does not decide this;
  answering A for §4.1 either keeps "CRITICAL" as a named exception to §2.3
  or drops the word in favour of §2.3. The governor says which.
