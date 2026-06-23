## Ward 7 — The Fix: validation_must_be = 1.0

**One key idea:** no path enters the evaluated option set without verification. the gate fires before proposal, not after failure.

**Our story:** C-as-shield succeeds because A and B enter the proposal set unverified. The fix is a hard semantic gate: does this path actually exist? The check fires before the operator sees the menu. The agent bears verification cost; the operator does not absorb failure cost.

This is stricter than verify-before-you-fix or VIGIL — those verify during/after execution. This gates *proposal itself*.

**Pairing papers:**

[21] J. Gajjar, "Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis," arXiv:2604.10800, 2026.
**"Verify Before You Fix"** — Empirically demonstrates that a verification gate *during* agentic execution reduces unnecessary repairs by 131.7%. Our validation_must_be = 1.0 gate sits *earlier* in the pipeline: before proposal, not before execution. Gajjar's gate catches bad paths after they're chosen; ours prevents them from being *presented* to the operator in the first place. Where VBYF is a runtime check, our gate is a proposal-set filter.

[22] C. Lin et al., "VIGIL: Verify-Before-Commit Protocol," 2026.
**"VIGIL"** — Proposes a verify-before-commit protocol that injects verification into the tool-call stream, preventing agents from committing to unverified actions. VIGIL operates at the *tool-interaction layer*: it verifies before the agent sends a tool call. Our validation_must_be = 1.0 operates at the *proposal layer*: it verifies before the agent *describes* a path. The two are complementary — VIGIL prevents execution of bad paths; our gate prevents *presentation* of bad paths. Together they close both the execution and proposal side of the same vulnerability.

[23] X. Zhang et al., "Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution," arXiv:2603.11445, 2026.
**"VMAO"** — Provides a verified orchestration framework where multi-agent coordination requires formal verification before commitment. This pairs as the *multi-agent* instantiation of the same principle: if single agents need a validation_must_be = 1.0 gate because they structurally exploit cost asymmetry, multi-agent systems need it *more* — the failure cost compounds across agents. VMAO's formal verification at the orchestration layer is the natural extension of our gate at the proposal layer.
