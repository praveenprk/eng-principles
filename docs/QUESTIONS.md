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
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A. A project ICS may use `not assessed`, provided each such row
           states why it is not assessed and what assessing it needs." → ENG-DEC-015

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
Recommend: A, widened to any project and any recognised process: the five
           gates are read as exit conditions (ENG-STD-002 §2), and a project
           MAY meet them through the process its organisation or industry
           already uses (e.g. the IETF RFC process, the V-model, the ISO/IEC/
           IEEE 12207 life-cycle processes, Stage-Gate, an agile definition
           of done) when it records the mapping once as a project decision.
           The order of §1.1 and the failing-test-first exit of §2.3 MUST be
           kept. Because §1.2 lets a project add gates but not rename them, a
           specification project cannot conform today however disciplined its
           process; ADP-0 §5.4 already runs the same order under other names.
           Nothing is weakened: the exit conditions are unchanged, only the
           names of the artifacts that meet them.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A, as widened in the entry. Not all work follows RFC → SPEC → TEST
           → BUILD → REFINE by those names. A project may meet the gates
           through whatever process its organisation or industry already
           uses, provided it records the mapping once and keeps the gate
           order and the failing-test-first exit. This lays the foundation
           for that. It does not build any specific process mapping now." → ENG-DEC-015

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
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A. All executable text is code under ENG-STD-004, including inline
           `<script>` and CI `run:` steps. It is applied proportionately." → ENG-DEC-015

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
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A. Add a keyword to every listed clause without changing its
           meaning. For the clauses marked J, use the recommended keyword
           in each row." → ENG-DEC-015

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
  base sentence would contradict that refinement. Their wording is the
  subject of Q-005; Q-004 applies to them as Q-005 is answered.
- ENG-STD-002 §4.1 says to open a CRITICAL violation. ENG-STD-006 §2.3 (ENG-
  DEC-013) now grades our own rules HIGH or MEDIUM, and CRITICAL only for a
  known vulnerability in released code. Adding MUST to §4.1 as written would
  make two MUST clauses disagree on the severity. Its wording is the subject
  of Q-006.

### Q-005
Scenario : A software line runs like a factory floor: several automated
           contributors build, check and merge work into `main` all day. At
           the end, a quality-control station checks the result, and only
           what passes, with a record of the evidence, is packed for
           distribution. ENG-STD-005 §2.3 ("Only a human merges") and ENG-P-11
           ("Check: Merges, releases, and hardware sign-offs carry a human
           approver") say a person must merge. ENG-DEC-012 already lets the
           agent merge into `main`, so the standard and the principle's check
           disagree today. Nothing states what evidence a release needs.
           This question covers merges into `main` and the evidence a release
           carries. Who may perform a release is Q-007.
Options  : A — Gate merges on evidence, not on who performs them, and give
               every release a record:
               ENG-STD-005 §2.3: any authorised contributor, human or
               automated, MAY merge into `main`; a merge MUST NOT happen
               until every required check passes and no question is OPEN.
               This restates ENG-DEC-012's rule for `main` in role-neutral
               words; it does not change who releases.
               New §2.6 Release record: a release (promotion to `stable` and
               its tag) MUST NOT happen without a release record stating the
               commit, every required check's result at that commit, the open
               violations, and who authorised the release. AGENTS.md MUST
               record which roles may merge and which may release.
               Security-related changes (§2.5) keep a human gate: only a
               human merges them. ENG-STD-005 §2.5 and ENG-DEC-013 (d) are
               unchanged.
               ENG-P-11 Check refined to match ENG-DEC-012, which refined
               ENG-STD-005 §2.3 but never this check: releases,
               security-related merges and hardware sign-offs carry a named
               human approver; other merges carry evidence and trace to a
               named human accountable for the line.
               Reference models: ISO 9001:2015 §8.6 (release of products:
               evidence of conformity, traceability to the person authorising
               release); SLSA provenance and in-toto attestations as the
               future form of the release record.
           B — Keep a human at every merge: revert ENG-DEC-012's agent merge
               into `main` and make "Only a human merges" a MUST.
Recommend: A, because the gate that protects users is the evidence at
           release, not who pressed merge. A records the evidence, keeps a
           named person answerable for each release and each security change,
           and makes ENG-P-11 and ENG-STD-005 agree again. Known cost, stated
           honestly: OpenSSF Scorecard's Code-Review check (risk High) scores
           human review of changes, and under ENG-DEC-013 (a) its rating is
           taken as is, with no override, so a line where only machines merge
           shows HIGH on the dashboard. That already follows from ENG-DEC-012.
           The release record is the answer to that finding, not a way to
           hide it.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A. I don't want 'only a human merges' as the rule. [...] merges
           into `main` are gated on evidence, not on who performs them, and
           every release carries a release record. Security-related
           changes keep a human gate. I accept the stated cost: Scorecard's
           Code-Review check will show HIGH for machine-only merges, and the
           release record is our answer to that finding." → ENG-DEC-015

### Q-006
Scenario : A reviewer finds that a feature was built without its SPEC. ENG-
           STD-002 §4.1 and ENG-P-12's check say to open a CRITICAL violation.
           ENG-STD-006 §2.3 (ENG-DEC-013) grades our own rules HIGH or MEDIUM
           and keeps CRITICAL for a known vulnerability in released code, as
           CVSS, OpenSSF and security advisories use the word. The reviewer
           cannot satisfy both.
Options  : A — ENG-STD-002 §4.1 becomes: "Work found to have bypassed a gate
               MUST stop. A violation MUST be opened, graded per ENG-STD-006
               §2.3, and never below HIGH. The missing artifacts MUST be
               backfilled honestly before work continues." ENG-STD-006 §2.3
               gains the HIGH floor for a bypassed gate. ENG-P-12's check says
               "recorded as a violation of at least HIGH severity". Severity
               is then defined in one place (ENG-STD-006 §2.5, one fact in one
               register). ISO audit practice calls a bypassed required gate a
               major nonconformity; HIGH is that floor. The floor only adds:
               a bypass that is security-related (e.g. a branch rule or a
               required check skipped, ENG-STD-005 §2.5) stays under
               ENG-DEC-013 (d), never below HIGH and CRITICAL for a known
               vulnerability in released code; no bypass grades MEDIUM.
           B — Keep CRITICAL for a bypassed gate as a named exception in
               ENG-STD-006 §2.3. CRITICAL then means two different things.
Recommend: A, because CRITICAL keeps the meaning outside readers already give
           it, severity stays in one register, and a bypass can never grade
           below HIGH. Moving from CRITICAL to HIGH lowers a stated severity,
           which CHARTER (Amendment) counts as weakening unless the governor
           accepts it explicitly.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A. [...] I explicitly accept moving the stated severity from
           CRITICAL to the HIGH floor, so that CRITICAL keeps the meaning
           OpenSSF and CVSS give it." → ENG-DEC-015

### Q-007
Scenario : The factory floor of Q-005 runs all day. At the end, an automated
           quality-control station has the release record for a commit:
           every required check green, the open violations listed. The
           product could be packed and shipped now. Today the governor
           promotes `main` to `stable` and signs the tag (ENG-DEC-012,
           governor 2026-11-22: "I merge main -> stable and tag releases";
           ENG-STD-005 §2.3, §2.4, §5.1). May the station release it?
Options  : A — A human releases. The release record of Q-005 is the evidence
               the human signs off. Changes: none beyond Q-005; ENG-DEC-012
               stands as written.
           B — An authorised automated station MAY promote to `stable` and
               tag when the release record is complete, under a named human
               accountable for the station. Changes: ENG-DEC-012 SUPERSEDED
               in part (who releases); ENG-STD-005 §2.3, §2.4, §5.1 refined;
               ENG-P-11 Check refined. Excluded until ruled separately:
               security-related changes (§2.5), and anything that drives a
               physical actuator (agent-dispatch-protocol ADP-2 R2/R3,
               unruled). Needs first: a release signing identity for the
               station, which is itself a security-related change (§2.5),
               since Scorecard's Signed-Releases check (risk High) and
               fid's V-ENG-008-01 are met today by the governor's signed tag.
Recommend: A now, because B needs a signing identity and provenance that do
           not exist yet, and would supersede a ruling the governor made the
           day before. Q-005's release record is the step that makes B
           possible later; B can be asked again as its own question once a
           signing identity and attestations exist.
Raised by: this pull request (docs/ENG-DEC-015-open-rulings)
Status   : ANSWERED (governor, 2026-11-22, PR #13 comment 7084073611):
           "A, for now. A human promotes to `stable` and tags, signing off the
           Q-005 release record. Automated release can be raised again as
           its own question once a signing identity and attestations
           exist." → ENG-DEC-015

### Q-008
Scenario : A robotics engineer joins and opens CHARTER.md to learn what the
           practice is for. The Purpose section lists software, hardware,
           firmware and documentation, and nothing says why the portfolio
           exists or where it is heading. The North Star review
           (2026-11-23) proposes one paragraph, labelled as aspiration, so
           that no programme becomes a commitment by being named.
Options  : A — Add to CHARTER Purpose, labelled aspiration: "Make productive
               capability, intelligence, infrastructure and access to
               resources steadily more abundant, affordable, safe,
               sustainable and widely owned, on Earth and beyond it. We
               pursue this through systems whose claims rest on physical
               reality and evidence, which people can inspect, repair,
               replace and own, and whose benefits reach the people who use
               them. Ambition sets the direction; measured evidence sets the
               pace." No programme is named in the charter.
           B — Leave Purpose as is; keep the North Star in the review only.
Recommend: A. The governor called the proposed text "good" in session on
           2026-11-23; this entry asks for confirmation on the PR. Naming no
           programme keeps the charter true whatever any programme's
           feasibility turns out to be.
Raised by: this pull request (docs/ENG-DEC-016-north-star-foundation)
Status   : ANSWERED (governor, 2026-11-22, PR #14 comment 7086345693):
           "Q-008 — A. Add the North Star paragraph to CHARTER Purpose,
           labelled as aspiration and naming no programme." → ENG-DEC-016

### Q-009
Scenario : A contributor designing an agricultural droid reads that the
           practice is "grounded in Unix" (CHARTER Grounding; ENG-P-13 "the
           ground"). Unix tells them how to compose the droid's software,
           but nothing about soil, torque, batteries or a child walking into
           the field. For physical systems the ground is physics.
Options  : A — CHARTER Grounding: physical reality and evidence are the
               ground; Unix is the software ground. ENG-P-13 is renamed
               "Unix discipline (the software ground)", its rules unchanged.
           B — Keep Unix as the ground of everything.
Recommend: A. The governor ruled it in session on 2026-11-23: "ground is
           physical reality and evidence", "unix as the software ground";
           this entry asks for confirmation on the PR. Every ENG-P rule
           survives unchanged; only what sits beneath them changes.
Raised by: this pull request (docs/ENG-DEC-016-north-star-foundation)
Status   : ANSWERED (governor, 2026-11-22, PR #14 comment 7086345693):
           "Q-009 — A. The ground is physical reality and evidence. Unix is the
           software ground, and ENG-P-13 is renamed accordingly with its
           rules unchanged." → ENG-DEC-016

### Q-010
Scenario : ENG-DEC-015 replaced a human merge step with an evidence gate and
           moved a severity from CRITICAL to a HIGH floor. Each time, the
           governor had to accept explicitly that this was not "weakening" a
           rule, because the charter says a rule "may never be weakened" and
           never says what weakening is. The same question will return every
           time a step changes hands or a term is aligned with an external
           standard.
Options  : A — Replace the word, in CHARTER (header and "Tighten, never
               weaken"), PRINCIPLES.md header and AGENTS.md: "A rule may be
               refined. Its bar may never be lowered." The bar is the
               evidence, traceability and accountability the rule demands.
               Changing who or what performs a step, or aligning a term with
               the meaning an external standard gives it, is a refinement
               when the bar is kept or raised; the decision making such a
               change states why for each of the three. The AGENTS.md Roles
               line is not touched.
           B — Keep "weakened", undefined, and accept each case explicitly.
Recommend: A. The governor, in session on 2026-11-23: "instead of 'weakened'
           use something else word", then "bar may never be lowered is fine,
           keep it". A adds a test every such change must pass, so the rule
           itself is tightened, not loosened.
Raised by: this pull request (docs/ENG-DEC-016-north-star-foundation)
Status   : ANSWERED (governor, 2026-11-22, PR #14 comment 7086345693):
           "Q-010 — A. Replace 'weakened' with 'A rule may be refined. Its bar
           may never be lowered.' The bar is the evidence, traceability and
           accountability a rule demands." → ENG-DEC-016

### Q-011
Scenario : A contributor starts writing a job scheduler for agents without
           checking that operating systems solved most of it decades ago. A
           robot team ships a manipulator whose software follows every
           ENG-STD rule, but nothing required its operating envelope or safe
           state. A cheap droid passes every test and cannot be repaired by
           the farmer who owns it. Today's principles catch none of the
           three.
Options  : A — Add or extend three principles:
               1. Look before you build (new): before original work, existing
                  knowledge and technology are searched and a reuse, integrate,
                  adapt, procure, collaborate, research or build decision is
                  recorded. Operating systems are the first prior art for
                  scheduling, isolation, protection, recovery and replaceable
                  interfaces (OSTEP).
               2. Authority is bounded by evidence (extends ENG-P-08 and
                  ENG-P-11 to physical systems): autonomy stays inside a
                  validated operating envelope with a defined safe state, and
                  shrinks as evidence of deviation grows; the domain sets the
                  envelope.
               3. Lifecycle and access are design inputs (new): energy,
                  materials, maintenance, lifecycle cost, repairability and
                  ownership are assessed and recorded at SPEC. Recorded
                  assessments, reviewed, not pass/fail gates.
           B — Add none now; wait for a project in a physical domain.
Recommend: A. The governor, in session on 2026-11-23: principles 2, 4 and 5
           "good"; doctrine table "agree"; "what problems OS has solved we
           just replicate and make superbly integrable". A sets direction
           without writing any domain standard ahead of a project.
Raised by: this pull request (docs/ENG-DEC-016-north-star-foundation)
Status   : ANSWERED (governor, 2026-11-22, PR #14 comment 7086345693):
           "Q-011 — A. Add the three principles as framed: look before you
           build, with operating systems as the first prior art; authority
           bounded by evidence for physical systems; and lifecycle and
           access as recorded design assessments." → ENG-DEC-016

### Q-012
Scenario : A second engineering organisation wants to adopt eng-principles
           for its own robots. It asks two things: which rules bind it and
           which stay its own, and whether its products will need this
           repository to build or run.
Options  : A — CHARTER Authority Order gains the four layers: portfolio
               doctrine (CHARTER, PRINCIPLES), domain standards (ENG-STD-*,
               written only when a project in that domain exists), product
               requirements and implementation contracts (each project, by
               its own process, ENG-STD-002 §5). And: no product depends on
               this repository to build or run (ENG-DEC-007); the only
               exception is the shared commit check at CI time, called pinned
               to a commit (ENG-DEC-009).
           B — Leave the Authority Order as is.
Recommend: A. It is what the repository already does, written down so a
           second organisation can rely on it; the governor's review of the
           North Star dispatch accepted the four layers.
Raised by: this pull request (docs/ENG-DEC-016-north-star-foundation)
Status   : ANSWERED (governor, 2026-11-22, PR #14 comment 7086345693):
           "Q-012 — A. Write the four governance layers and the rule that no
           product depends on this repository at runtime into the CHARTER
           Authority Order, with the CI-time exception of ENG-DEC-009." →
           ENG-DEC-016

### Q-013
Scenario : A partner from a space programme reads that fid is "mature" and
           asks what that means. Today nothing in the standards says. The
           North Star review proposed seven levels, L0 (vision) to L6
           (replicable, sustainable scale), and validation 1 placed the six
           live projects on them (2026-11-23): fid, phasectl, contextos L3;
           agent-dispatch-protocol L2; factory-protocol L3 through the
           factory it describes; none at L4.
Options  : A — New standard ENG-STD-009 Evidence and maturity: L0 vision; L1
               scientific feasibility; L2 engineering feasibility; L3
               demonstrated prototype; L4 integrated validation; L5
               operational deployment; L6 replicable, sustainable scale. Each
               level is mapped to the Technology Readiness Levels of ISO
               16290 (L1 ≈ TRL 1–2, L2 ≈ 3–4, L3 ≈ 5–6, L4 ≈ 7, L5 ≈ 8–9,
               L6 beyond TRL, where manufacturing readiness applies), so a
               partner reads our levels in their own terms. A level advances
               only on met acceptance criteria and named evidence; agent
               confidence, demos, simulation alone or code volume never
               advance it. The mapping is checked against ISO 16290's text
               before the standard cites it.
           B — A level scale of our own, without the TRL mapping.
           C — No scale yet.
Recommend: A. The governor, in session on 2026-11-23: "good starting point
           now", "it will be more detailed in future". Mapping to TRL avoids
           duplicating an existing industry scale (North Star dispatch §10).
Raised by: this pull request (docs/ENG-DEC-017-maturity-scale)
Status   : ANSWERED (governor, 2026-11-23, PR #15 comment 7087064034):
           "Q-013 — A. Adopt ENG-STD-009 with L0–L6 mapped to ISO 16290 TRL. A
           level advances only on met acceptance criteria and named
           evidence." → ENG-DEC-017

### Q-014
Scenario : Validation 1 could not place three projects on a scale written
           for physical prototypes: what is a "relevant environment" for a
           CLI, a "prototype" of a specification, or the maturity of a web
           page that documents a process?
Options  : A — ENG-STD-009 says how each kind of deliverable reads the scale:
               Software: L3 passes its tests on real inputs; L4 runs in a
               real operating environment, the governor's own daily use
               included, with a dated, committed record of runs, inputs,
               results and issues; L5 is used beyond its author with
               incidents tracked; L6 just works at any scale it meets.
               Specification (after IETF practice, RFC 7942): L2 every rule
               is decidable by conformance vectors; L3 one implementation
               passes every vector; L4 two independent implementations
               interoperate; L5 implementers other than the authors run it in
               production; L6 stable and widely adopted.
               Documentation: takes the level of what it describes; a page
               describing an untested process stays at that process's level.
           B — One reading for all kinds.
Recommend: A. The governor, in session on 2026-11-23, on software: "my daily
           use count go with default", the record "go with Default", and L6
           as software "that just works at galactic scale"; on documentation:
           option B of the review (takes the level of what it describes),
           confirmed by the factory running inside contextos. The
           specification ladder is this review's proposal; the governor said
           "okay I am listening" and has not ruled on it.
Raised by: this pull request (docs/ENG-DEC-017-maturity-scale)
Status   : ANSWERED (governor, 2026-11-23, PR #15 comment 7087064034):
           "Q-014 — A. Each kind of deliverable has its own reading of the
           scale." Software counts the governor's daily use, with a dated,
           committed record; documentation takes the level of what it
           describes; specifications use the ladder L2 vectors, L3 one
           implementation, L4 two interoperating, L5 others in production.
           → ENG-DEC-017

### Q-015
Scenario : eng-principles holds both an audit tool that runs daily and a set
           of standards with no running form. contextos holds a product and
           the factory that builds it. One level per repository cannot
           describe either. And a level needs a home: if it lives in two
           places, the two will disagree.
Options  : A — A level belongs to a deliverable, not a repository. Each
               project's levels live in one place: a Maturity table in this
               repository's CONFORMANCE.md, one row per deliverable, with
               the level, the evidence at a named commit, and what blocks
               the next level (ENG-STD-006 §2.5, one fact in one register).
           B — One level per repository, in CONFORMANCE.md.
Recommend: A. The governor, in session on 2026-11-23, on levels per
           deliverable: "yes correct". CONFORMANCE.md already holds each
           project's evidence-backed status, so adding a table there keeps
           one register.
Raised by: this pull request (docs/ENG-DEC-017-maturity-scale)
Status   : ANSWERED (governor, 2026-11-23, PR #15 comment 7087064034):
           "Q-015 — A. Levels belong to deliverables, not repositories, and are
           recorded in one Maturity table in CONFORMANCE.md." → ENG-DEC-017

### Q-016
Scenario : The governor accepted Q-013 option A, which said the TRL mapping
           "is checked against ISO 16290's text before the standard cites
           it". ENG-STD-009 was merged citing ISO 16290 in its header, §2.1
           and REFERENCES.md, after a check against ESA's published level
           headings only. The full standard is paywalled and was not read.
           An independent review found this after the merge: the condition
           of the governor's ruling was not met.
Options  : A — Hold the citation until the check is done: remove the "Nearest
               TRL" column, the ISO 16290 reference in the header and the
               REFERENCES.md row; restore them in the change that records a
               check against the standard's own text.
           B — The governor narrows the condition: the mapping is to level
               headings only, and a check against those headings as ESA
               publishes them is sufficient. ENG-STD-009 §2.2 already says
               this; the decision records that the governor accepted it.
           C — Obtain ISO 16290:2013 and check the mapping now, keeping the
               citation once the check is recorded.
Recommend: A. It keeps the bar of the governor's own ruling without anyone
           lowering it; nothing depends on the TRL column today. B is the
           governor's to give, not the agent's to assume. C is A plus a
           purchase.
Raised by: this pull request (fix/ENG-DEC-018-maturity-corrections)
Status   : ANSWERED (governor, 2026-11-23, PR #16 comment 7087583540):
           "Q-016 A" → ENG-DEC-018

### Q-017
Scenario : The Maturity table placed the eng-principles standards at L2,
           "the lowest of the deliverables it governs". ENG-STD-009 §3.3
           says a document takes the level of what it describes, but not
           which level when it describes several deliverables at different
           levels. The independent review of PR #16 found this was a new
           rule written into a register, not into the standard.
Options  : A — §3.3 gains: a document that describes several deliverables
               takes the lowest of their levels.
           B — Such a document is not placed until it describes one
               deliverable.
           C — It takes the level of most of the deliverables it describes.
Recommend: A. A claim is only as strong as its weakest evidence (ENG-P-06);
           the lowest level cannot overstate.
Raised by: PR #18 (fix/ENG-DEC-018-review-followups)
Status   : ANSWERED (governor, 2026-11-24, given in the engineering-fa
           session and relayed; PR #18 comment 7139324060): "Q-017 A"
           → ENG-DEC-019

### Q-018
Scenario : An auditor asks where ENG-STD-007's "nine product-quality
           characteristics" come from, and whether anyone here has read ISO/IEC
           25010:2023. Nobody has: iso.org refuses automated reads and the text
           is paywalled. Today REFERENCES.md names standards without saying
           where each was read or how far, and ISO 16290 was cited from a
           summary (Q-016). The governor asked that citations be grounded:
           "be specific and redirect me to the real standard", public
           summaries such as ESA's where available, and a maintained list of
           what must be bought.
Options  : A — Adopt contextos's register policy (RFC-032 RP-7) as prior art
               (ENG-P-14). CHARTER External Standards states the rule.
               REFERENCES.md gains Source and Verified columns, with levels
               primary / abstract-only / secondary / unverified. No rule
               relies on content beyond what was read. Paywalls do not block.
               docs/PROCUREMENT.md lists what to obtain, by priority, with the
               free route first and prices carrying their own verification
               level. The governor decides purchases.
           B — Links only, no levels or procurement list.
Recommend: A. It is the governor's request, and contextos has run this policy
           since 2026-11-08. This pull request applies A. It shows that of 22
           references only RFC 2119/8174 has been read at its primary source;
           six more are free to read (POSIX, SemVer, RFC 7942, OSTEP, the 1978
           BSTJ article, SEVOCAB); the rest are paywalled, and four of those
           (ISO 16290, 29148, 25010, 12207) carry content our rules rely on.
Raised by: PR #19 (docs/ENG-DEC-019-citation-grounding), carried into
           the PR that replaces it
Status   : ANSWERED (governor, 2026-11-24, given in the engineering-fa
           session and relayed; PR #19 comment 7139325034): "Q-018 A"
           → ENG-DEC-020
