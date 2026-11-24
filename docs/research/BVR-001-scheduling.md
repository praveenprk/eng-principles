# BVR-001 — Scheduling as a portfolio abstraction: build versus reuse

Status   : RESEARCH INPUT. Not a decision. Nothing here binds a project.
Date     : 2026-11-23
Principle: ENG-P-14 Look before you build (operating systems first, OSTEP)
Author   : engineering-ab (eng-principles session), for the governor
Asked by : the governor, 2026-11-23: "I need this scheduler stuff also
           abstractable … traditional OS job schedulers and algos are not
           enough for AI-assisted workflows. be it software or robotics and
           large scale where automation needs to be there in the future."

Every row below says how it was verified (REFERENCES.md levels). **Fact**
means a claim about the source, at the level shown, read on 2026-11-23.
Quotation marks are used only for text read at the source.
**Judgment** means this record's reasoning. **Hypothesis** means a claim
still to be tested.

## 1. The question

Is there a scheduling layer that every project here (agent dispatch,
factory gates, software builds and, later, robots and plants) can share?
Should it be reused, integrated, adapted, procured, done with
collaborators, researched, or built?

## 2. What existing systems already solve

| Source | What it solves (fact; quoted only where primary) | Level |
|--------|-------------------------------|-------|
| OSTEP, ch. 7–10 ([site](https://pages.cs.wisc.edu/~remzi/OSTEP/)): CPU Scheduling, Multi-level Feedback, Lottery Scheduling, Multi-CPU Scheduling; ch. 6 Direct Execution | The base set: turnaround against response time; learning priority from behaviour when job length is unknown (MLFQ); proportional share; multiprocessor affinity; preemption through a timer | chapter list: primary. Content: secondary (from the governor's PDF, not re-read here) |
| Linux SCHED_DEADLINE ([kernel docs](https://docs.kernel.org/scheduler/sched-deadline.html)) | "basically an implementation of the Earliest Deadline First (EDF) scheduling algorithm", with CBS; per-task "runtime", "period" and "deadline" | primary |
| Kubernetes scheduling framework ([docs](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/)) | Scheduling policy is added as plug-ins at fixed extension points, among them QueueSort, Filter, Score, Reserve, **Permit** and Bind; the mechanism stays fixed | secondary (from a summary of the page) |
| Temporal ([docs](https://docs.temporal.io/workflows)) | Workflows "can run—and keep running—for years, even if the underlying infrastructure fails"; after a crash "Temporal will automatically recreate its pre-failure state" | primary |
| Ray ([docs](https://docs.ray.io/en/latest/ray-core/scheduling/index.html)) | Strategies DEFAULT, SPREAD, placement groups, node affinity; CPU, GPU, memory and custom resources | primary |
| A2A protocol ([spec](https://a2a-protocol.org/latest/specification/)) | The specification says tasks "may involve human-in-the-loop scenarios" (§1.1–1.2). Its TaskState table includes working, completed, failed, rejected and **TASK_STATE_INPUT_REQUIRED**, where the agent waits for user input | human-in-the-loop: primary. The state list: secondary (from a summary) |
| ROS 2 executors ([docs](https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Executors.html)) | Callback scheduling in robots | unverified: the site refused automated reads |
| Borg ([Google Research](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/)), Slurm, HTCondor, Airflow, Argo Workflows | Cluster and batch scheduling at scale; DAG workflows | sources reachable; content not read this pass |
| agent-dispatch-protocol (this portfolio) | Dispatching work to agents, with conformance vectors | primary (ADP-0/1/2 in this portfolio) |

## 3. What AI-assisted work adds (judgment, to be tested)

The governor said classical schedulers "are not enough". Read against the
sources above, the gap is less in the algorithms than in what the
scheduler has to know about. AI-assisted work differs in these ways:

| # | Property of the work | Nearest existing answer | Gap (hypothesis) |
|---|----------------------|-------------------------|------------------|
| 1 | **Unknown, heavy-tailed duration and cost** (tokens, money, retries) | MLFQ learns priority from behaviour (OSTEP ch. 8); CBS bounds a budget (SCHED_DEADLINE) | Budgets are in money and tokens, not CPU time; nobody schedules on them across tools |
| 2 | **Waiting on a human** (a governor's ruling, a review) as a normal state | A2A TASK_STATE_INPUT_REQUIRED; Kubernetes `Permit`; Temporal waits for years | Human attention is a scarce resource with its own queue. Batching rulings ("review by exception", contextos RFC-032) is a scheduling decision |
| 3 | **Evidence gates**: a step may only start when evidence exists | Kubernetes Filter and Permit; workflow DAGs | A gate predicate over records (questions OPEN, checks green, levels per ENG-STD-009) is not a standard plugin anywhere found |
| 4 | **Preemption costs context**: stopping an agent loses state | Temporal recreates state by replay; OS context switch | Agent context is large and lossy; resuming means a handoff (phasectl's domain) |
| 5 | **Authority bounded by evidence** (ENG-P-15): for physical work, the envelope limits what may be scheduled | SCHED_DEADLINE admission control; real-time executors | Admission control that consults a safety envelope and a safe state is domain work, not a general scheduler |
| 6 | **Many peers coordinating**, as tonight's sessions do (review, fix, relay) | A2A; ADP | Who may take which work item is today settled by messages, not by a register |

## 4. Options (ENG-P-14)

| Option | What it would mean | Judgment |
|--------|--------------------|----------|
| Reuse | Adopt one system (e.g. Temporal) for everything | Covers durability (rows 2, 4), but not evidence gates or envelopes. It would also tie every product to one runtime: lock-in, against systems people can replace (ENG-P-13, the North Star) |
| **Integrate** | Keep mechanisms where they live (OS, Kubernetes, Temporal, ROS 2); write the *policy* as plug-ins at their existing extension points | Fits the Unix ground: small parts, a written contract. Most of rows 1–3 fit Filter, Permit or Score style hooks |
| Adapt | Fork an existing scheduler | Not justified by any gap found |
| Procure | Buy a commercial orchestrator | No requirement yet that only a vendor meets |
| Collaborate | Work with A2A or similar protocol groups | Worth it for row 6 once ADP has an implementation (ADP L3) |
| **Research** | State the policy contract first: the inputs a scheduler needs (budget, evidence gate, human queue, envelope) as a written interface | Needed before any build: rows 1–6 are hypotheses |
| Build | A new portfolio scheduler | Not justified now; nothing found that requires a new mechanism |

## 5. Recommendation

**Research, then Integrate.** Do not build a scheduler. Write down, as a
contract and not as code, the scheduling *policy inputs* that AI-assisted
work adds:
- a cost budget in tokens or money;
- an evidence gate;
- a human-attention queue;
- for physical systems, the operating envelope and safe state.

Then map each input to an existing extension point: OS and SCHED_DEADLINE
for time, Kubernetes Permit and Filter for admission, Temporal or a
workflow engine for durable waits, and A2A or ADP for agent hand-offs. Build
only where no extension point fits, and record why.

The likeliest first home for that contract is agent-dispatch-protocol, which
already dispatches agent work and has conformance vectors. That is a
proposal for ADP's own process, not a decision here.

## 6. What would change this recommendation

- A real workload where integrating at existing extension points fails a
  measured requirement (latency, cost, safety). That would be evidence for
  Adapt or Build.
- Reading the unread sources (ROS 2 executors, Borg, Slurm) and finding a
  policy layer that already covers rows 1–3.

## 7. Not done in this pass

- No source was read in full. The levels above say how far each was read.
- No experiment was run.
- Robotics real-time scheduling (ROS 2 executors, real-time Linux) was not
  verified at source.
