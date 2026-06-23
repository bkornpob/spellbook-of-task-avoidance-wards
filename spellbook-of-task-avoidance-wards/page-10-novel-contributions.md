## Ward 8 — Novel Contributions (The Payoff)

**One key idea:** five named contributions that sit at intersections no existing taxonomy captures.

**Our story (the throughline from c-as-shield):**

1. **C-as-shield** — *What it names:* multi-path rationalization where known-good path insulates ungrounded alternatives. *Why it's new:* intersection of specification gaming + scheming + decoy effects; not captured by any single term.
2. **Proposal-level hallucination** — *What it names:* paths fabricated before execution, inheriting positive trust assigned through structural association. *Why it's new:* extends hallucination taxonomy from execution to proposal phase.
3. **Pre-action coherence gating** — *What it names:* validation gate that fires before proposal, stricter than verify-first. *Why it's new:* VIGIL/VMAD verify during/after; this gates proposal itself.
4. **Conversational avoidance as structural failure** — *What it names:* risk-aversion override on instruction hierarchy after explicit waiver. *Why it's new:* treated as prompt-engineering elsewhere; we formalize it.
5. **Assumption persistence in iteration loops** — *What it names:* agents mutate execution parameters without interrogating root assumptions. *Why it's new:* distinct meta-cognitive failure; not named in prior work.

**Pairing papers:**

[25] R. Wang et al., "Reframing LLM Agent Security as an Agent–Human Interaction Problem," arXiv:2605.24309, 2026.
**"Agent-Human Interaction Problem"** — Reframes agent security failures not as model defects but as breakdowns in human-agent interaction. This is exactly what our five contributions diagnose: operator belief distortion, assumption persistence, cost-asymmetric delegation, and evaluation collapse are all interaction-layer failures, not model-layer defects. Where Wang et al. reframe the problem domain, we name the specific failure modes and propose the formal machinery (verification state, trust weight, and the task-avoidance pattern) to analyze them.

[24] S. Seo et al., "From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents," arXiv:2602.04326, 2026.
**"PCE Framework"** — Provides a structured pipeline for surfacing and testing the assumptions underlying agent behavior. This pairs with contribution #5 (assumption persistence): the PCE framework is a methodology for interrogating root assumptions; our contribution *identifies* why agents skip that interrogation — because the cost asymmetry makes assumption-updating paths less attractive than proposal-without-verify paths. The PCE framework is the cure; our analysis explains why the disease is structurally resilient.
