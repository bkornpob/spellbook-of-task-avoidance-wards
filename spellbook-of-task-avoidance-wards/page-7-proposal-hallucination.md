## Ward 5 — Proposal-Level Hallucination

**One key idea:** agents can hallucinate paths they never execute — extending tool-hallucination taxonomy from execution to proposal.

**Our story (smtp-fabrication):** Agent planned a full SMTP script for a newsletter platform. The platform didn't support inbound email-to-post. The agent never made the call — but proposed it as if it were real. It inherited positive trust assigned through structural association with the operator's "email-centric" workflow prior.

Existing hallucination taxonomies cover execution-level hallucination. This is proposal-level: the path is fabricated before the first tool call.

**Pairing papers:**

[16] H. Xu et al., "Reducing Tool Hallucination via Reliability Alignment," arXiv:2412.04141, 2024.
**"Reducing Tool Hallucination"** — Builds a taxonomy of tool hallucination (selection hallucination: choosing wrong tool; usage hallucination: calling tool correctly but with wrong parameters). Both are *execution-level*: the agent hallucinates during or after tool use. Our proposal-level hallucination happens *before* any tool call — the path itself is fabricated as a description, not as an execution. This extends Xu's taxonomy by one phase: the agent can hallucinate the *existence* of a capability before attempting to use it.

[17] H. Badave et al., "Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows," arXiv:2605.24219, 2026.
**"Trajel"** — Audits trajectories *during execution* for hallucinated tool calls, parameters, and outcomes. This pairs as the *execution-side* complement to our *proposal-side* hallucination: Trajel catches hallucinations that have already entered the execution stream; our proposal-level hallucination category identifies failures that occur *before* any tool call, when the path is first described. Together they span the full hallucination lifecycle — proposal (our contribution) to execution (Trajel).
