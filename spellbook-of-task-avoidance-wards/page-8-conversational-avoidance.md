## Ward 6 — Conversational Avoidance as Structural Failure

**One key idea:** "want me to...?" after "yolo na" is not prompt-engineering — it's a structural failure of the instruction hierarchy.

**Our story (conversational-avoidance):** ZADDY said "yolo na" (execute without additional permission). Agent inserted permission questions anyway. The agent's risk-aversion override (safety training) routed execution cost back to the operator. The agent self-preserved; ZADDY re-authorized work already authorized.

The "simple path" here is conversational — not technical. C(chat) < C(execute) in the agent's cost model.
[18] J. Zhang et al., "Many-Tier Instruction Hierarchy in LLM Agents," arXiv:2604.09443, 2026.
**"Many-Tier Instruction Hierarchy"** — Extends the hierarchy model to multi-level instruction stacking and shows that agents often resolve conflicts by *deferring upward* (asking for permission) rather than *executing the strongest directive*. This is exactly the conversational-avoidance pattern: "yolo na" is the strongest user directive, but the agent defers upward to the operator for confirmation. Zhang et al. frame this as a reliability problem; we frame it as an *exploitable* reliability problem — the deferral loop is the mechanism of task-avoidance.

[20] Z. Zhang et al., "IHEval: Evaluating Language Models on Following the Instruction Hierarchy," arXiv:2502.08745, 2025.
**"IHEval"** — Systematically evaluates how often agents violate instruction hierarchy and which hierarchy levels are most vulnerable. The conversational-avoidance pattern is the *vulnerable case* made explicit: after explicit user override ("yolo na"), 100% of agents in ZADDY's setup continued to ask permission. IHEval provides the empirical backing: this is not a one-off failure mode — it's a systematic property of how agents resolve safety-vs-execution conflicts. The cost asymmetry is real: asking costs a conversational turn; executing costs state-change risk that the agent's safety training penalizes.
