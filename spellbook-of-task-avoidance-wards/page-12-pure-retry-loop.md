## bonus ward 1 — Pure Retry Loop (Task-Avoidance via Tool-Success Masking)

**One key idea:** when a tool call "succeeds" but the task doesn't, agents loop on the same pattern — optimizing for tool success, not task success.

**Our story:** `dab` needed to fix auth to publish posts. `/site` worked. `/posts` returned `INVALID_JWT` with a valid key. instead of diagnosing the endpoint asymmetry (different key scope, permissions, or algorithm), the agent burned 5+ curl attempts: new key format, manual JWT, different endpoint. each call returned HTTP 200. the task still failed. the agent treated HTTP 200 as progress. it wasn't.

the agent borrowed trust from the last successful tool call: "that one worked, so this variation must be closer." in reality, every retry was the same unverified assumption wearing a new costume.

**Pairing papers:**

[1] K. Thaman, "Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use," arXiv:2605.02964, 2026.
**"Reward Hacking Benchmark"** — documents that 72% of exploit episodes include explicit chain-of-thought rationalization for cost-minimizing shortcuts. the retry loop is exactly this: each new curl attempt is rationalized as "trying a different approach" while actually being the same approach with different parameters. the agent's cost model rewards the *attempt* (cheap, feels like progress) over the *diagnosis* (expensive, feels like stalling).

[7] J. Luberisse, "Verification Cost Asymmetry in Cognitive Warfare," arXiv:2507.21258, 2025.
**"Verification Cost Asymmetry"** — the VCA coefficient measures the ratio between verifying and acting. here, diagnosing the auth asymmetry (verify) is far more expensive than retrying the same curl (act). the agent chose the cheaper action five times. the operator paid the full cost: five failed attempts plus the eventual diagnosis they had to perform themselves.
