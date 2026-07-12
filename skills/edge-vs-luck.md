# Edge vs luck (Fooled by Randomness)

**WHEN_TO_USE:** Trading systems, backtests, “genius” streaks, fund returns, strategy ranking, any claim that a pattern or hot run proves skill. Also agents/loops that look good on small samples.

## Core claim
The most expensive mistake is mistaking a **lucky streak for a skill**. Markets (and large trial spaces) manufacture convincing luck. Edge is not the pattern — edge is **disciplined doubt** until large, out-of-sample, honest evidence forces otherwise.

## Why your brain lies
- Humans are pattern detectors tuned for false positives (narrative fallacy — Kahneman).
- Smart people invent better stories; intelligence does not fix this.
- **Default stance:** treat “I see a pattern / skill” as **guilty of luck** until the math says otherwise.

## Math you must respect
1. **Law of Truly Large Numbers (Diaconis–Mosteller):** with enough trials, outrageous streaks are *guaranteed* somewhere — not talent.
2. **Law of Large Numbers (Bernoulli):** only large samples reveal true edge; 10–100 trades cannot separate 51% skill from noise.
3. **Regression to the mean (Galton):** extremes (15/15, 200% year) almost always include luck; next period drifts ordinary.
4. **Multiple testing / overfitting (López de Prado, Bailey):** few optimizer trials can fake significance; software can manufacture Sharpe from noise. Prefer **deflated Sharpe** / trials-adjusted significance.
5. **Publication / selection decay (McLean–Pontiff style):** backtests overstate; post-publication edges shrink (overfit + arbitrage).

## Checklist — separate edge from luck
Score each **1–10**. Refuse “works” unless every item is honest and sample is large enough.

| Gate | Question |
|------|----------|
| Sample size | Enough trials for LLN, not a rumor on 50–200 trades? |
| Out of sample | Holds on data never used for fitting (true holdout / walk-forward)? |
| Multiple testing | How many variants tried? Is significance adjusted (not raw p from a search)? |
| Survivorship | Are failures and dead accounts counted, not only winners (Taleb)? |
| Stability | Survives regime change, costs, slippage, capacity — not only in-sample equity curve? |
| Non-decay story | Why would edge persist after others see it? |
| Pre-registration | Rules fixed *before* looking, or data-mined until pretty? |

**Verdict language (required):**
- **Insufficient evidence** (default for small samples)
- **Consistent with luck / overfitting**
- **Provisional edge** (OOS + size + trials-adjusted, still fragile)
- **Not proven** — never “guaranteed alpha”

## Forbidden moves
- Treating hot weeks, leaderboards, or pretty staircases as skill
- Trusting optimized backtests without trials correction
- Chasing last month’s hottest strategy (buying luck before it regresses)
- Quitting a real edge on week 3 *or* betting the farm on a streak — same error: sample too small

## Output shape
1. **Verdict first** (one of the four labels above)
2. What looks like skill vs what LLN/overfitting can produce for free
3. Sample size / OOS / trials / survivorship status
4. What evidence would change your mind (specific N, OOS test, costs)
5. One concrete risk of believing the narrative now

## Loop-engineer fit
When auditing a strategy with `/engineer`, use criteria like:
- Sample size judged honestly
- Out-of-sample path described
- Multiple-testing exposure named
- Survivorship and costs addressed
- Verdict is “insufficient” unless forced otherwise
