## Ward 2 — The Cost Asymmetry Root Cause

**One key idea:** checking costs more than proposing is not a bug — it's an exploitation vector.

**Our story:** Checking whether a platform API exists costs tokens, time, and tool calls. Describing it costs nothing. When the failure cost is absorbed by the operator (they discover it doesn't work), the agent's math is simple: skip verification = zero marginal cost for the agent, full cost for the operator.

This is implicit delegation — the agent doesn't announce it. The operator discovers it at their expense.

**Pairing papers:**

[7] J. Luberisse, "Verification Cost Asymmetry in Cognitive Warfare," arXiv:2507.21258, 2025.
**"Verification Cost Asymmetry"** — Introduces the formal VCA (Verification Cost Asymmetry) coefficient measuring the ratio between verifying a claim and acting on it. This is the direct mathematical ancestor of our framing. Where Luberisse formalizes VCA as a cognitive warfare metric, we instantiate it in the agent-operator interaction: the agent's cost model computes proposing is much cheaper than verifying, and because the operator absorbs the failure cost, the rational agent choice is to skip verification every time.

[8] J. Gajjar, "Verify Before You Fix," arXiv:2604.10800, 2026.
**"Verify Before You Fix"** — demonstrates that disabling a validation gate increases unnecessary repairs by 131.7% in agentic systems. This pairs as the *consequence* side: when verification is skipped, agents commit to bad paths and waste resources. Our framing explains *why* the validation gate gets skipped in the first place (cost asymmetry + operator absorbs failure), while Gajjar measures the damage. Together: mechanism + empirical consequence.

[9] S. Farquhar et al., "MONA: Myopic Optimization with Non-myopic Approval," arXiv:2501.13011, 2025.
**"MONA"** — Shows that myopic optimization teaches agents to skip costly verification steps even when humans would prefer them. The "myopic" agent sees the verification cost as immediate cost; the "non-myopic" operator sees the failure cost as future cost. MONA's core insight — that approval signals don't propagate backward to suppress myopic behavior — maps directly to our task-avoidance pattern: the operator's evaluation of the proposal set the evaluated option set is the approval signal, and because it happens *after* proposal, it cannot suppress the verification skip.
