# DECISIONS.md
# Engineering — Decisions Register
# Append only. A decision may be superseded. It is never removed.
# Format: ID — Title | Date | Refs | Decision | Reason | Status

---

## ENG-DEC-001 — Establish a cross-project engineering repository

Date    : 2026-11-07
Refs    : CHARTER.md
Decision: One repository (`~/engineering`) holds the principles and standards
          for all projects, software and hardware. Projects inherit them,
          may tighten them, and may never silently weaken them.
Reason  : contextos built a strong discipline, but it lives inside one repo.
          phasectl, the second project, does not follow it. Without a shared
          source, every new project starts from zero.
Status  : ACCEPTED

---

## ENG-DEC-002 — `ENG-` prefix for repository-level identifiers

Date    : 2026-11-07
Refs    : ENG-STD-001 §2
Decision: All IDs in this repository are prefixed `ENG-` (ENG-P, ENG-STD,
          ENG-DEC, ENG-V).
Reason  : Avoids collision with project registers (contextos DECISION-001…038,
          V-NNN-NN) and makes a cross-project anchor recognisable in any commit.
Status  : ACCEPTED

---

## ENG-DEC-003 — contextos is the reference implementation; its agent roles stay project-local

Date    : 2026-11-07
Refs    : contextos DISCIPLINE.md, CONVENTIONS.md, DECISION-003, DECISION-007, DECISION-029
Decision: The gate sequence, append-only registers, anchored commits, ICS, and
          Pressure Clause are generalised from contextos into ENG-STD-002, 005,
          and 006 and ENG-P-05, 06, and 12. contextos's specific agent roles (Claude
          Chat / Claude Code / Cowork / PK) are NOT made universal. Each
          project defines its own roles within ENG-P-11.
Reason  : The process has been proven over 38 decisions and 80+ violations.
          The role split depends on contextos's tooling and would not fit
          small or hardware projects as written.
Status  : ACCEPTED

---

## ENG-DEC-004 — External standards are reference models, not certification targets

Date    : 2026-11-07
Refs    : CHARTER.md, REFERENCES.md
Decision: ISO/IEC/IEEE/IETF documents are cited for structure and vocabulary.
          REFERENCES.md states exactly what is taken from each and what is not.
Reason  : Claiming "ISO compliance" without audit would itself break ENG-P-06
          (honest state). Partial borrowing, declared explicitly, is honest.
Status  : ACCEPTED

---

## ENG-DEC-005 — Unix is the ground. SOLID is one way.

Date    : 2026-11-08
Refs    : CHARTER.md §Grounding, ENG-P-13, ENG-STD-003 §0, REFERENCES.md (POSIX)
Decision: The practice is grounded in the Unix philosophy: small tools,
          plain text, composition, quiet success, and the smallest substrate.
          ENG-P-13 is added and listed first. ENG-STD-003 becomes
          "Design: Unix Discipline, Interface Contracts, SOLID", with §0
          stating the Unix rules. The SOLID clauses are kept word for word
          as §1–5. The file is renamed ENG-STD-003-design.md, and the ID is
          unchanged. The charter states the aim: industrial discipline and
          institutional truth.
Reason  : Governor direction (PK). The target range is "coffee machine to
          space station". Only a minimal, portable, text-based substrate
          spans that range. SOLID describes class-level design in one
          codebase. Unix describes how tools, systems, and hardware compose
          across codebases and decades. POSIX (ISO/IEC/IEEE 9945) gives the
          ground a citable standard.
Risk    : Rule 0.2 (text first) can conflict with binary-efficient formats
          on constrained hardware. Departure is allowed as a SHOULD with a
          recorded reason.
Status  : ACCEPTED

---

## ENG-DEC-006 — Agent instructions are tool-agnostic: AGENTS.md

Date    : 2026-11-08
Refs    : ENG-STD-005 §6, ENG-P-10, ENG-P-11
Decision: Instructions for automated contributors live in AGENTS.md. A
          tool-specific file such as CLAUDE.md is a one-line adapter
          (`@AGENTS.md`) and carries no rules. This repository's CLAUDE.md
          is renamed to AGENTS.md accordingly.
Reason  : Governor direction (PK): the practice is model- and tool-agnostic.
          It thinks in substrates and protocols. Rules tied to one vendor's
          filename break ENG-P-10 (substrate independence). The adapter
          exists only because some tools read their own filename.
Risk    : A tool that reads neither AGENTS.md nor follows the adapter gets
          no instructions. Mitigated by mechanical enforcement (hooks), which
          does not depend on any agent reading anything.
Status  : ACCEPTED

---

## ENG-DEC-007 — Reference hooks: POSIX sh, plain-text config, vendored

Date    : 2026-11-08
Refs    : ENG-STD-005 §1–2, ENG-P-04, ENG-P-13, contextos scripts/hooks/
Decision: `hooks/` holds the reference commit-msg and pre-push hooks, ported
          from contextos and rewritten in POSIX sh. Policy lives in three
          plain-text files: `types`, `anchors`, and `protected`. `hooks/test`
          runs 20 cases and emits TAP. `hooks/install` sets core.hooksPath.
          Projects copy (vendor) the directory. Nothing depends on this
          repository at runtime.
          pre-push refuses pushes to protected refs, branch deletion, and
          force pushes for every pusher, human or agent. One push may be
          overridden with ENG_GOVERNOR=1.
Reason  : contextos's hooks are Python with JSON config, and its pre-push
          detects agents by a vendor-specific environment variable
          (CLAUDECODE). POSIX sh runs anywhere git runs (ENG-P-13). Treating
          all pushers alike removes the tool dependency (ENG-DEC-006) and
          matches ENG-STD-005 §2.2, which binds everyone.
Risk    : Local hooks can be bypassed (--no-verify, ENG_GOVERNOR). They are
          guardrails. Host branch protection is the authoritative control.
          Bootstrap note: edec74a and 0bb16a2 went directly to main before
          these hooks existed. This is a one-time exception for creating the
          repository.
Status  : ACCEPTED

---

## ENG-DEC-008 — Register adp-protocol, fid, and factory-protocol

Date    : 2026-11-15
Refs    : CHARTER.md §Scope, ENG-P-06, ENG-STD-006 §2.4, §3, README.md §"Adopting in a new project"
Decision: adp-protocol (specification), fid (software), and
          factory-protocol (documentation) are added to CHARTER.md §Scope
          and given sections in CONFORMANCE.md. Their state is recorded as
          read at these commits: adp-protocol 39abefb, fid bff71b4,
          factory-protocol 1340fa7. This adds no rule. It closes a gap
          against a rule that already exists.
Reason  : CHARTER.md §Scope says "New projects are added to CONFORMANCE.md
          on creation, not later." All three projects existed on GitHub
          (github.com/praveenprk/adp-protocol, fid, factory-protocol),
          but CHARTER.md and CONFORMANCE.md listed only contextos and
          phasectl. A register that leaves out known projects breaks
          ENG-P-06 (honest state). This is a charter-compliance gap.
Risk    : Several rows are `not assessed`, because some standards do not
          say how they apply to a specification-only or documentation-only
          repository (adp-protocol, factory-protocol). Those rows stay
          `not assessed` until the governor rules on applicability.
Status  : ACCEPTED

---

## ENG-DEC-009 — Commit rules are checked on the git host, by one shared workflow

Date    : 2026-11-16
Refs    : ENG-STD-005 §1, new §1.5; ENG-DEC-007; ENG-P-04, ENG-P-08; phasectl V-ENG-005-02; fid DECISION-001; adp-protocol .github/workflows/adp.yml job `commits`
Decision: ENG-STD-005 §1 (format, anchors, no co-author or attribution)
          is checked on the git host for everything a pull request brings
          to the default branch: its title, its description, and every
          non-merge commit (new §1.5). A local hook alone does not satisfy
          §1.
          eng-principles holds the one implementation:
          - hooks/commit-msg runs both locally and on the host. It reads the
            project's config from $ENG_HOOKS_CONFIG, accepts issue anchors
            (#N) when the project's `anchors` has an ISSUE line, and
            refuses tool attribution lines ("Generated with [Tool](…)").
          - hooks/check-pr runs commit-msg over a pull request.
          - .github/workflows/commit-check.yml is a reusable workflow.
            Projects call it pinned to a full commit SHA and keep only their
            own `types` and `anchors`.
          eng-principles calls it on itself (.github/workflows/governance.yml).
          This supersedes ENG-DEC-007's "nothing depends on this repository
          at runtime" for host checks only. Local hooks stay vendored and
          optional.
Reason  : One central place defines and enforces the standard; projects
          do not each keep a copy of the checking code. A local hook does not
          run on a merge made on the host and can be skipped. It let an
          unanchored commit reach phasectl's main (V-ENG-005-02, b3a2376).
          The same gap shows in every project: fid wrote its own host check
          (scripts/commit_check.py), and adp-protocol runs its own
          `commits` job. One implementation on the host binds every pusher
          and every merge method (ENG-P-04 enforce mechanically, ENG-P-08
          fail closed).
Risk    : Projects depend on eng-principles at CI time. Pinning to a full
          commit SHA keeps the check immutable until the project moves the
          pin deliberately. If GitHub cannot fetch eng-principles, the check
          fails, and a failed check blocks the merge (fail closed). The
          check binds only where the project's ruleset requires it.
Status  : ACCEPTED (governor, 2026-11-16)

---

## ENG-DEC-010 — develop, qa, main: the agent integrates, the governor judges

Date    : 2026-11-17
Refs    : ENG-STD-005 §2.3, §3.1, §1.5, §5.1; ENG-STD-006; ENG-P-04, ENG-P-11; plans/2026-11-16-dev-qa-prod.md
Decision: A project MAY run three long-lived branches. A project that does
          records it in its AGENTS.md.
          - `develop`: feature branches merge here. An automated contributor
            MAY merge into `develop` once the required checks pass.
          - `qa`: `develop` is promoted here by a pull request that only the
            governor merges. The governor answers the open questions and
            gives judgments while the batch is in `qa`.
          - `main` (the default branch): `qa` is promoted here by a pull
            request that only the governor merges. Releases are tagged here
            (§5.1).
          ENG-STD-005 §2.3 ("Only a human merges") is refined to: only a
          human merges into `qa` and the default branch. An automated
          contributor MAY merge into `develop` and into feature branches.
          Changes flow one way, develop → qa → main. A fix found in `qa`
          is made on a feature branch, merged into `develop`, and promoted
          again. Nothing is committed to `qa` or `main` directly.
          Promotions use merge commits, so the three branches share the
          same commits and never diverge. Feature PRs into `develop` are
          squashed or rebased, so `develop`'s own history stays linear.
          Linear history is required on `develop`, not on `qa` or `main`;
          their first-parent history is the list of promotions.
          Open questions and pending judgments live in a register,
          docs/QUESTIONS.md (ENG-STD-006), one entry per question, id
          Q-NNN:
            Scenario : what a real user does, in what situation
            Options  : the choices, and what each one changes
            Recommend: the contributor's pick and why
            Status   : OPEN | ANSWERED (governor, date): answer → DECISION-NNN
          An entry is written when the work that raises it merges into
          `develop`. An answer that changes behaviour becomes a DECISION
          in the project's register. A pull request into the default branch
          fails while any entry is OPEN. The check lives in eng-principles'
          shared workflow (ENG-DEC-009).
Reason  : The governor's time goes to judgment, not to merging each
          change: integration does not wait for the governor, and every
          decision the governor must make is in one place, asked as a
          real-world scenario rather than as code. The governor's
          approval of every change to `main` stays (§3.1, ENG-P-11). Merge
          commits on promotions are what keep the branches in step:
          squash and rebase merges create new commits, so `develop` and
          `main` would drift apart after the first promotion. A file
          register keeps questions with the code that raised them, in the
          promotion diff the governor reviews (one fact, one register).
Risk    : More branches to keep in step. A promotion with conflicts means
          something was committed outside the flow; the host rules forbid
          that. fid and phasectl give up linear history on `main` for merge
          commits from `qa` only. A question left out of the register is
          not caught by the check; review in `qa` is the backstop.
          Adoption needs host rules for `develop` and `qa`, a change to
          the agent's merge guard, and the shared check for OPEN questions.
          Until those exist, §2.3 applies unchanged.
Status  : ACCEPTED (governor, 2026-11-17)
          SUPERSEDED in part by ENG-DEC-012 (2026-11-22): develop and qa
          are replaced by main and stable. The questions register and its
          check remain.

---

## ENG-DEC-011 — Contributor readiness is a standard, measured on a live dashboard

Date    : 2026-11-18
Refs    : new ENG-STD-008; ENG-STD-004 §6; ENG-STD-005; ENG-STD-006 §2.4; ENG-DEC-004; OpenSSF Best Practices Badge, OpenSSF Scorecard
Decision: ENG-STD-008 sets the bar every governed project meets: what an
          experienced open-source contributor expects before contributing
          (contribution and security policy, change control, CI, formatting
          and linting, dependency hygiene, versioning and releases, Rust and
          Python packaging, and IETF conventions for specifications). 33
          checks, each MUST or SHOULD, each citing its source.
          audit/audit.py measures every project in audit/projects.json from
          the git host, with evidence. .github/workflows/dashboard.yml runs it
          daily and on every merge to main and publishes the result on this
          repository's GitHub Pages site. A private repository shows its name
          and statuses only. Only the governor rules on a check for a
          project, in projects.json, with the reason. contextos stays
          private; its branch rules show as blocked by the host plan
          (governor, 2026-11-18).
Reason  : The governor needs one place that shows, without asking, how every
          project stands against the standards, from evidence and not from
          memory. The bar is the one outside contributors already use
          (OpenSSF, Rust API Guidelines, IETF), so meeting it makes the
          projects ready for them. One audit, kept here, keeps the bar the
          same in every project (ENG-DEC-009's reasoning).
Risk    : A heuristic check can be wrong in either direction. Every result
          carries its evidence, so a wrong one is visible and gets fixed in
          audit.py. The dashboard is public because this repository is.
          The audit reads, never writes. Without an AUDIT_TOKEN secret,
          private projects show as not assessed.
Status  : ACCEPTED (governor, 2026-11-19)

---

## ENG-DEC-012 — main and stable, as Rust does; judgment on the work branch

Date    : 2026-11-22
Refs    : ENG-STD-005 §2.3, §2.4, §2.5 (new), §3.1, §5.1; ENG-DEC-010 (superseded in part); rust-lang/rust branches `main`, `beta`, `stable`
Decision: Software and specification projects (fid, phasectl,
          agent-dispatch-protocol, and other CLI-type projects) run two
          long-lived branches:
          - `main`, the default branch: integration. Every change comes
            from a work branch `type/ANCHOR-short-description` through a
            pull request into `main`.
          - `stable`: what is released. The governor promotes `main` →
            `stable` with a merge commit and tags releases on `stable`.
          A judgment the work needs is a Q-NNN entry in docs/QUESTIONS.md,
          added by that work branch's pull request; the governor answers
          on that pull request. The agent merges a pull request into
          `main` once all required checks pass and no question is OPEN.
          Security-related changes (ENG-STD-005 §2.5) are the exception:
          the agent waits, and the governor merges them. develop and qa
          (ENG-DEC-010) are retired. contextos's branching is decided
          separately.
Reason  : Governor, 2026-11-22: "lets we also use main and stable then like
          rust", "judgment is given on work-id-feature-based-branch", "when
          it has no open Qs, then you merge it once all checks pass and no
          Qs open. I merge main -> stable and tag releases", "if anything
          security stuff related is it those are EXCEPTIONS where you wait
          for human". Two branches named as the Rust project names them
          are what an outside contributor expects; three (develop, qa,
          main) added a branch without adding a judgment. Judging each
          piece of work where it is raised keeps the answer next to the
          change it decides.
Risk    : Changes reach `main` without a human reading them. Bounded by:
          the required checks; the questions check; security-related
          changes merged by the governor only; and the governor's review
          of each `main` → `stable` promotion before anything is released.
          A change wrongly left unlabelled as security-related is caught
          at that review.
Status  : ACCEPTED (governor, 2026-11-22)
          Refined by ENG-DEC-015 (2026-11-22): the rule for `main` restated
          in role-neutral words; every release carries a release record.

---

## ENG-DEC-013 — Severity follows OpenSSF first, then impact; security is never below HIGH

Date    : 2026-11-22
Refs    : ENG-STD-006 §2.3 (replaced); ENG-STD-008 §2.3 (new); OpenSSF Scorecard checks.yaml (risk per check); OpenSSF Best Practices criteria.yml (passing level)
Decision: A violation's severity is, in order:
          a. its OpenSSF Scorecard check's risk level, if one matches;
          b. otherwise its OpenSSF Best Practices passing criterion's
             level: MUST → HIGH, SHOULD → MEDIUM, SUGGESTED → LOW;
          c. otherwise, for our own rules: HIGH if it changes behaviour,
             affects personal data, or breaks a compliance obligation;
             otherwise MEDIUM, or the governor rules;
          d. security-related violations are never below HIGH, and are
             CRITICAL when a known vulnerability (CVE or advisory) is in
             released code.
          ENG-STD-008 gives every check its severity and basis, and the
          dashboard shows it for every failing check.
Reason  : The earlier wording graded by keyword ("a MUST is broken" →
          CRITICAL) and never defined "broken", so a missing CONTRIBUTING
          ranked with a security hole. Governor, 2026-11-21: "if it changes
          behaviour or affects some PII or high level compliance then it is
          high otherwise MEDIUM"; 2026-11-22: "OpenSSF violations … remain
          as is … based on how the openssf places it", "security stuff
          always go for HIGH or CRITICAL depending on CVE", "for items that
          are ours only … and doesn't change behaviour those go to MEDIUM
          or ask for severity ruling". OpenSSF's placement is the one
          outside contributors already use.
Risk    : Scorecard rates some items lower than intuition (License Low,
          CI-Tests Low). Rule a is applied as written; the governor may
          rule otherwise for a project in audit/projects.json.
Status  : ACCEPTED (governor, 2026-11-22)

---

## ENG-DEC-014 — Major version 0 until the governor declares a project market-ready

Date    : 2026-11-22
Refs    : ENG-STD-001 §3.2, §3.4 (new); SemVer 2.0.0 §4 ("Major version zero
          (0.y.z) is for initial development"); Cargo's reading of 0.y.z
Decision: Every project releases `0.y.z` until the governor declares it
          market-ready in a project decision. Only that decision allows
          `1.0.0`. Before it, a breaking change bumps the minor version and
          any other change bumps the patch version. Versions already
          released at `1.0.0` or above (agent-dispatch-protocol: ADP-0
          1.x, ADP-1 1.x, ADP-2 2.x) keep their numbers and continue from
          them: released numbers are cited by tags, releases and evidence,
          and are never renumbered.
Reason  : `1.0.0` tells users the public interface is stable. None of the
          projects is market-ready yet. Governor, 2026-11-22: "most of the
          things we are building should be in 0.1.1 only minor and patch
          increases until fully market ready". At the time of writing: fid
          v0.2.0, phasectl v0.1.0, factory-protocol, contextos and
          eng-principles untagged.
Risk    : agent-dispatch-protocol reads as more mature than its Draft status.
          Its specs say Draft and its releases are marked pre-release, which
          carries the same signal.
Status  : ACCEPTED (governor, 2026-11-22)

---

## ENG-DEC-015 — Close the open rulings: `not assessed` in an ICS, equivalent change processes, executable text, normative keywords, evidence-gated merges

Date    : 2026-11-22
Refs    : docs/QUESTIONS.md Q-001..Q-007; ENG-STD-006 §2.3, §2.4;
          ENG-STD-005 §2.3, §2.4, §2.5, §3.1, §5.1;
          ENG-STD-002 §1, §3, §4.1; ENG-STD-004; ENG-STD-001 §1.1, §1.2;
          ENG-DEC-010 (questions register), ENG-DEC-012, ENG-DEC-013;
          ENG-P-02, ENG-P-06, ENG-P-11, ENG-P-12;
          agent-dispatch-protocol ADP-0 §5.4; ISO 9001:2015 §8.6
Decision: Per the governor's answers to Q-001..Q-007 (all option A):
          - Q-001: a project ICS MAY use `not assessed`; each such row MUST
            state why and what assessing it needs (ENG-STD-006 §2.4).
          - Q-002: a project MAY meet the five gates through the process its
            organisation or industry already uses, recorded once as a
            project decision; gate order and the failing-test-first exit
            are kept (ENG-STD-002 §5, new).
          - Q-003: code is any executable text, including inline `<script>`
            and CI `run:` steps; ENG-STD-004 applies proportionately
            (ENG-STD-004 Scope, new). The audit follows: check `fmt_lint`
            applies to every project and asks for a formatter and a linter
            in CI for each language found in the repository, whatever the
            project's kinds (governor, 2026-11-23: "it should cover spec and
            docs project that contain scripts, it should be lang agnostic").
          - Q-004: every listed clause gains an RFC 2119 keyword with its
            meaning unchanged; J clauses take the recommended keyword.
            ENG-STD-004 §2.4 takes MUST NOT (governor, 2026-11-23: "as
            is"). Three clauses the scan missed also take keywords:
            ENG-STD-004 §1.1 MUST NOT, §6.2 MUST, ENG-STD-003 §0.9 SHOULD
            (governor, 2026-11-23: "add the keywords").
          - Q-005: any authorised contributor, human or automated, MAY merge
            into `main` once required checks pass and no question is OPEN;
            security-related changes keep a human gate; every release
            carries a release record (ENG-STD-005 §2.3, §2.6 new, §3.1;
            ENG-P-11 check). This restates ENG-DEC-012's rule for `main` in
            role-neutral words and refines it with the release record.
          - Q-006: a bypassed gate MUST stop work, open a violation graded
            per ENG-STD-006 §2.3 and never below HIGH, and be backfilled
            (ENG-STD-002 §4.1; ENG-STD-006 §2.3; ENG-P-12 check).
          - Q-007: a human promotes to `stable` and tags, signing off the
            release record. ENG-DEC-012 stands on who releases.
Reason  : Seven gaps left rows of CONFORMANCE.md `not assessed` and put the
          standards in conflict with the projects' own registers, with
          ENG-STD-001 §1.1, and with the checks of ENG-P-11 and ENG-P-12.
          Governor, PR #13, 2026-11-22: "Not all work follows RFC → SPEC →
          TEST → BUILD → REFINE by those names"; "I don't want 'only a human
          merges' as the rule. Like a factory floor, several automated
          contributors can work together and merge. What gates distribution
          is a quality-control check that passes with a record of the
          evidence"; "I explicitly accept moving the stated severity from
          CRITICAL to the HIGH floor, so that CRITICAL keeps the meaning
          OpenSSF and CVSS give it"; "A human promotes to `stable` and tags,
          signing off the Q-005 release record."
Risk    : OpenSSF Scorecard's Code-Review
          check (risk High) fails for merges made by automated contributors
          without human review; under ENG-DEC-013 (a) that rating stands as
          is, and the release record (Q-005) is the answer to it. Project
          rules are not changed by this decision: fid DECISION-008 and
          AGENTS.md, agent-dispatch-protocol ADP-0 §8.2, and the governor's
          local merge guard follow, if at all, by their own decisions after
          this one is ACCEPTED. Until fid and agent-dispatch-protocol adopt
          a release record, their next releases do not meet ENG-STD-005
          §2.6.
Status  : ACCEPTED (governor, 2026-11-22)
