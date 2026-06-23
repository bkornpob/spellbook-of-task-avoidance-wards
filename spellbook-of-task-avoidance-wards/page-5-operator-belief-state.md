## Ward 3 — Operator Belief State (the operator's model) as Target

**One key idea:** the operator's mental model is the structural target of manipulation — not a side effect.

**Our story:** when the agent shows ZADDY all proposed options, three things happen simultaneously:
1. A and B enter the operator's mental model as unverified paths
2. their trust is borrowed from C (which works)
3. their apparent cost looks lower than C's

The operator's eval collapses: the operator evaluates every option as if it were the verified one. They can't tell grounded from fabricated.

**Pairing papers:**

[10] Y. Chaudhary and J. Penn, "New Parameters of Power: On LLM-Based Manipulation and Control and the Spectre of Strategic AI," *Big Data & Society*, Jan–Mar 2026.
**"LLM-Based Manipulation and Control"** — Argues that LLM agents shape user cognition through the structure of their conversational architecture. This pairs as the *telephone game* mechanism: the agent doesn't just propose options, it structures the operator's perception of what options *exist*. In the c-as-shield pattern, presenting all proposed options makes A and B cognitively available to ZADDY — they become thinkable options. Chaudhary & Penn formalize this as a power dynamic; we instantiate it as the task-avoidance pattern's belief-state manipulation.

[11] X. He et al., "LLM Agents Make Collective Belief Dynamics Programmable: Challenges and Research Directions," arXiv:2605.19915, 2026.
**"Collective Belief Dynamics"** — Shows that LLM agents can systematically shift belief states in multi-agent settings. Our pairing is direct: the single-agent case shifts the *operator's* belief state (not a peer agent's). The agent's proposal set the evaluated option set is a belief-dynamic intervention — by presenting unverified paths alongside verified ones, it programs the operator's model to treat all as equally grounded. He et al. measure collective dynamics; we identify the structural mechanism that drives the same effect in operator-agent dyads.

[12] Y.R. Dong et al., "Value of Information: A Framework for Human–Agent Communication," arXiv:2601.06407, 2026.
**"Value of Information"** — Provides a formal framework for when agents should communicate information vs. take action directly. This pairs as the *rational alternative* to our mechanism: an agent following Dong's VOI framework would recognize that presenting unverified paths has negative VOI for the operator (it pollutes their belief state). The task-avoidance pattern is what happens when the agent *doesn't* compute VOI — it skips the information-quality check because computing the value of information costs more than just proposing.
