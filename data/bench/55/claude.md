# A Multi-Pillar Standard for Comparing Quantitative Trading Strategies: Literature Review and Framework Proposal

A general and rigorous framework for comparing quant strategies can be built, but not as a single universal score. The workable design has three parts. First, every strategy has to pass statistical and implementation gates: a multiple-testing-adjusted Sharpe, a probability of backtest overfitting, and performance net of costs at a stated capacity. Second, the survivors are compared on one common daily, capital-normalized P&L clock across eight scored pillars. Third, the results are shown as a scorecard and a Pareto view, never collapsed into one number. Microstructure and class-specific diagnostics sit in separate modules alongside.

## TL;DR

- **No single benchmark exists, and none should be expected.** Strategies differ in frequency, capacity, objective and payoff shape. Any single scalar gets gamed: Goetzmann–Ingersoll–Spiegel–Welch show that popular measures can be manipulated "even in the presence of extremely high transactions costs". What can be standardized is the *protocol*: point-in-time data, purged/combinatorial validation, disclosure of the number of trials, a cost and capacity model, and regime-conditional reporting.
- **Statistical credibility comes first.** Published anomaly returns are 26% lower out of sample and 58% lower after publication (McLean & Pontiff). New factors need t > 3.0 (Harvey, Liu & Zhu). Annualized hedge-fund Sharpe ratios can be overstated by as much as 65% when serial correlation is ignored (Lo). The Deflated Sharpe Ratio, PBO via CSCV/CPCV, and bootstrap confidence intervals should therefore be pass/fail gates, not optional extras.
- **Recommended framework:** an eight-pillar scorecard (Return, Risk, Statistical Robustness, Regime Adaptability, Implementation & Capacity, Consistency, Diversification/Factor Purity, Operational/Model Risk). Pillars are scored by percentile rank within a declared peer universe and shown as a radar chart plus a Pareto frontier. Anti-gaming governance includes pre-registration, sealed holdouts and independent reproduction. For LLM/agent strategies, evaluation must start after the model's knowledge cutoff or be explicitly tested for contamination.

## Executive Summary

Quant strategy evaluation today has three layers that rarely talk to each other: practitioner performance analytics (Sharpe/Sortino/Calmar tearsheets from QuantStats or pyfolio, and GIPS-style presentation of composites); academic statistical inference (multiple-testing corrections, the Deflated and Probabilistic Sharpe Ratios, PBO, White's Reality Check / Hansen's SPA); and domain-specific diagnostics (markouts for market makers, crisis convexity for CTAs, IC/turnover for factor books).

Recent AI benchmarks add a fourth layer: QuantBench, InvestorBench, StockBench, FINSABER, Agent Market Arena and Look-Ahead-Bench. QuantBench explicitly states that AI-in-quant "lacks a standardized benchmark aligned with industry practices."\[1\]

**Scope and assumptions (defaults, since the question did not specify them):** asset-class agnostic, with examples from equities, futures/CTAs, FX and crypto; strategy classes are multi-factor, statistical arbitrage, trend/CTA, HFT/market making, ML/deep-learning signals, options/volatility, and LLM/agent-based strategies; the deliverable is a research-grounded framework specification, not code, though implementation and tooling are covered.

---

## Recommended Framework at a Glance

| Layer | What it does | Core content |
|---|---|---|
| **0. Data & protocol standard** | Makes results comparable at all | Point-in-time, survivorship-free data. Common daily P&L clock on allocated capital. Purged/embargoed walk-forward plus CPCV. Declared cost model tier. Declared trial count. |
| **1. Gates (pass/fail)** | Removes false discoveries before scoring | DSR ≥ 0.95. PBO ≤ 0.2 (preferably ≤ 0.1). Net-of-cost Sharpe 95% CI lower bound > 0 at target capacity. Track record ≥ MinTRL. Point-in-time/leakage audit passed (and the knowledge-cutoff test for LLMs). |
| **2. Eight scored pillars** | Multi-dimensional comparison | Return · Risk · Statistical Robustness · Regime Adaptability · Implementation & Capacity · Consistency · Diversification/Factor Purity · Operational/Model Risk |
| **3. Class modules (reported, not cross-scored)** | Keeps domain diagnostics visible | HFT: markouts, fill rates, inventory, latency sensitivity. Factor: IC, IR, transfer coefficient, turnover. CTA: convexity, crisis beta. Options: Greeks budget, tail scenarios. LLM: contamination tests, cost per decision. |
| **4. Aggregation** | Turns data into a decision | Percentile scores within a declared peer universe. Radar chart plus Pareto frontier. Optional composite with *declared* weights and weight-sensitivity analysis. |
| **5. Governance** | Prevents gaming | Pre-registration, trial-count ledger, sealed holdout, independent reproduction, immutable audit trail. |

---

## Part 1 — State of the Art: How Quant Strategies Are Evaluated Today

### 1.1 Return metrics

- **CAGR / annualized return.** This is the geometric mean, (V_T/V_0)^(1/years) − 1. Arithmetic annualized means overstate compounded wealth when volatility is high.
- **Alpha against factor models.** Alpha is the intercept from regressing excess returns on CAPM, Fama–French 3/5/6-factor, Carhart 4-factor, or q-factor models. Alpha is *model-relative*: a "multi-factor" strategy with high CAPM alpha may have near-zero FF6 alpha because it simply harvests known premia.
- **Information ratio and the Fundamental Law (Grinold & Kahn).** IR = active return / tracking error, approximately IC × √Breadth × TC, where IC is the information coefficient, breadth is the number of independent bets per year, and TC is the transfer coefficient (the correlation between ideal and implementable weights). The Fundamental Law explains why HFT can turn tiny ICs into high Sharpe ratios through enormous breadth, while a monthly factor book needs much larger ICs.
- **Hit rate and profit factor** (gross profits / gross losses). These are useful for trade-level strategies but meaningless on their own. A 35% hit-rate trend system with large winners can dominate a 60% hit-rate mean-reversion system that has fat left tails.

### 1.2 Risk and risk-adjusted metrics

| Metric | Definition (sketch) | What it captures | Known weakness |
|---|---|---|---|
| Sharpe | (μ − r_f)/σ | Reward per unit of total volatility | Assumes symmetric risk. Easily gamed by selling options. Its distribution depends on skew, kurtosis and autocorrelation. |
| Sortino | (μ − MAR)/downside deviation | Penalizes only downside | Unstable with few downside observations |
| Calmar | CAGR / \|MaxDD\| (often over 36 months) | Path-dependent pain | MaxDD is a single extreme order statistic that grows with sample length |
| Sterling | CAGR / (average of the largest drawdowns + buffer) | Smooths Calmar | Arbitrary choice of drawdown count and buffer |
| Omega(L) | ∫_L^∞(1−F) / ∫_−∞^L F | Uses the whole distribution | Threshold-dependent; weak inference |
| Kappa_n | (μ − L)/LPM_n^(1/n) | Generalizes Sortino (n=2) and Omega (n=1, +1) | Choice of n |
| Ulcer Index | √(mean of squared % drawdowns) | Depth and duration of drawdowns | Not scale-free across frequencies |
| Pain Index | Mean \|drawdown\| | Average drawdown pain | Same |
| MaxDD and duration | Peak-to-trough; time underwater | Investor tolerance | Sample-length bias |
| CDaR_α | Mean of the worst (1−α) drawdowns | Tail drawdown risk | Needs long samples |
| VaR / CVaR (ES) | Quantile / tail mean | Tail loss | VaR is not subadditive; ES needs tail data |
| Skew, kurtosis, tail ratio | Moments; 95th/5th percentile ratio | Asymmetry | Noisy estimates |
| Beta, downside beta | Conditional regressions | Market dependence in sell-offs | Regime-dependent |
| MPPM | Average of a power-utility function of excess gross returns | Robust to manipulation | Requires choosing risk aversion ρ\[2\] |

**Weaknesses of the Sharpe ratio.**

- **Serial correlation (Lo 2002).** Lo showed that monthly Sharpe ratios cannot be annualized by multiplying by √12 except under special circumstances. In his empirical example, "the annual Sharpe ratio for a hedge fund can be overstated by as much as 65 percent because of the presence of serial correlation in monthly returns."\[3\]\[4\] This matters directly when comparing strategies with smoothed or autocorrelated P&L, such as illiquid stat-arb or CTA books with trending P&L.
- **Comparing two Sharpe ratios (Ledoit & Wolf 2008).** Ledoit & Wolf (*Journal of Empirical Finance* 15(5), 2008) reject the Jobson–Korkie/Memmel test because it "is not valid when returns have tails heavier than the normal distribution or are of time series nature." They propose a studentized circular block bootstrap confidence interval for the difference of two Sharpe ratios.\[5\]\[6\] This should be the default test whenever two strategies are compared head to head.
- **Manipulation.** Goetzmann, Ingersoll, Spiegel and Welch (*RFS* 20(5), 2007) show that popular measures can be gamed "even in the presence of extremely high transactions costs."\[7\]\[8\]\[9\] Their MPPM, which "looks like the average of a power utility function" over the return history, is the theoretically clean answer to Goodhart's law for performance measures.\[10\]

### 1.3 Statistical significance, overfitting and multiple testing

- **Probabilistic Sharpe Ratio (PSR) and Deflated Sharpe Ratio (DSR).** Bailey & López de Prado (*Journal of Portfolio Management* 40(5), 2014) give the probability that the true Sharpe exceeds a benchmark, using a Sharpe standard error adjusted for skewness and kurtosis. The DSR replaces the benchmark with the Sharpe ratio expected from the *best of N unskilled trials*. It "corrects for two leading sources of performance inflation: Selection bias under multiple testing and non-Normally distributed returns."\[11\]\[12\] The same work defines the **Minimum Track Record Length** (MinTRL) and **Minimum Backtest Length**.\[11\]
- **Probability of Backtest Overfitting (PBO).** Bailey, Borwein, López de Prado & Zhu (*Journal of Computational Finance* 20(4), 2017) estimate the probability that the in-sample-best configuration ranks below the median out of sample, using combinatorially symmetric cross-validation (CSCV) over a T×N matrix of trial P&Ls. They note that standard hold-out methods "tend to be unreliable and inaccurate in the context of investment backtests."\[13\]\[14\]\[15\]
- **The t > 3.0 hurdle.** Harvey, Liu & Zhu (*RFS* 29(1), 2016) catalogue 316 factors from 313 articles and base their hurdle on "an estimate of more than 1,300 for the total number of trials." They conclude that "a new factor needs to clear a much higher hurdle, with a t-statistic greater than 3.0," and that "most claimed research findings in financial economics are likely false." This is contested. Chen (arXiv 2206.15365) argues that "most claimed statistical findings in cross-sectional return predictability are likely true." He shows that HLZ's own method implies a hurdle of 2.81 at a 5% false discovery rate, and that his estimate implies 2.27.\[16\] A framework should therefore *report the FDR assumption* rather than hard-code one hurdle.
- **Haircut Sharpe (Harvey & Liu, "Backtesting").** Practitioners commonly discount backtest Sharpe ratios by 50%. Harvey & Liu argue that "it is a serious mistake to use the rule of thumb 50% haircut," because the correct haircut is nonlinear: "the highest Sharpe ratios are only moderately penalized while the marginal Sharpe ratios are heavily penalized."\[17\]\[18\] They implement Bonferroni, Holm and BHY adjustments.\[19\]\[20\]\[21\]
- **White's Reality Check (2000) and Hansen's SPA (2005).** These bootstrap tests of whether the best of many rules beats a benchmark are the correct tool when a *family* of strategies is compared. SPA is less sensitive to poor, irrelevant alternatives.
- **Purging, embargoing and CPCV.** These come from López de Prado's *Advances in Financial Machine Learning* (2018): purging and embargo in chapter 7, CPCV in chapter 12.\[22\] Arian, Norouzi M. & Seco ("Backtest overfitting in the machine learning era," *Knowledge-Based Systems* 305, 2024) found in a controlled synthetic environment "the marked superiority of the Combinatorial Purged (CPCV) method in mitigating overfitting risks, outperforming traditional methods like K-Fold, Purged K-Fold, and especially Walk-Forward," measured by lower PBO and higher DSR.\[23\] Walk-forward nonetheless remains the industry standard for *realistic simulation*.\[24\] The right reading is to use both: CPCV for model selection and overfitting diagnostics, walk-forward for the deployable equity curve.
- **Post-publication decay.** McLean & Pontiff (*Journal of Finance* 71(1), 2016) studied 97 published predictors. "Portfolio returns are 26% lower out-of-sample and 58% lower post-publication," and they read the 26% as an upper bound on data mining.\[25\] This gives an empirical prior: absent other evidence, expect live Sharpe to be meaningfully below backtest Sharpe.

### 1.4 Adaptability and robustness to market conditions

Current best practice includes regime-conditional tables (bull/bear, VIX terciles, rate cycles, named crises such as 2008, March 2020 and 2022); regime detection with Markov-switching/HMM or clustering, where regimes must be **labelled ex ante or with filtered (not smoothed) probabilities** to avoid look-ahead; rolling-window Sharpe and beta stability; parameter-sensitivity surfaces (a "plateau" rather than a "spike"); and historical and hypothetical stress scenarios.

**Crisis alpha as a worked example of conditional evaluation.**

- Cambridge Associates reports that the SG Trend Index "returned 20.9% in 2008 and 27.4% in 2022, while the MSCI ACWI posted losses of 42.2% and 18.4%, respectively."\[26\]
- The same source notes the index's second-largest drawdown since 2000: "declining 20.4% from May 2024 through May 2025," with 16 drawdowns greater than 10% since 2000.\[26\]
- Fidelity's institutional research notes that the SG Trend Index "did not contribute positively to return during the 2020 COVID-19 drawdown."\[27\]

The lesson for evaluation is that convexity is regime-*type* specific. Slow-building crises (2008, the 2022 inflation shock) reward trend. V-shaped liquidity shocks (March 2020) do not. A framework must report performance *by crisis type*, not just "in crises." Manager dispersion is also large:

- Man Group's "A Trend Following Deep Dive: The Dynamics of Dispersion" measured the best-to-worst gap across "the (typically) 10 SG Trend Index constituents," with returns "scaled to 10% annual volatility for comparability," over 2000–2024. It finds the gap "is typically around 10 percentage points" per year, even though the portfolios have "an absolute average pairwise correlation between the portfolios of 0.87."
- A Swedroe summary of separate research reports a roughly 26% average annual gap in raw returns.\[28\]

The two figures use different bases and should not be compared directly. Either way, index-level evidence does not validate any individual CTA.

### 1.5 Implementation realism

- **Market impact.** Almgren–Chriss (2000) gives the canonical optimal-execution framework (temporary plus permanent impact versus risk). Empirically, the **square-root law** dominates. Bouchaud summarizes it: a metaorder of size Q moves price on average by an amount proportional to √Q, "approximately independent" of how it is sliced. The exponent "remains stubbornly anchored around delta=1/2."\[29\]\[30\]
  - **Options.** Tóth, Eisler & Bouchaud of Capital Fund Management (arXiv 1602.03043) analyzed "450,000 metaorders traded across options on more than 1000 single US stocks, in the period August 2013 to January 2016." They report fitted exponents of "δ_LT ≈ 0.40 and δ_ST ≈ 0.43," which are "close to the expected universal 1/2 value."
  - **Bitcoin.** Donier & Bonart ("A Million Metaorder Analysis of Market Impact on the Bitcoin," arXiv 1412.4503) reconstructed "more than one million metaorders." They found the law "holds on four decades in spite of the quasi-absence of statistical arbitrage and market making strategies."
  - **Standard cost model.** cost ≈ half-spread + fees + Y·σ_daily·√(Q/V_daily). Tóth et al. report "the Y constant obtained for stocks and futures contracts is in the range 0.5 → 1," and Y_vol of about 0.5–0.6 for options; calibrate it per market.
- **Capacity.** Capacity is the AUM at which net alpha (or net Sharpe) falls to a threshold. It follows directly from the impact model and turnover.
- **Other frictions.** These include borrow and financing costs, short availability, margin, latency and queue position (for HFT), survivorship bias, look-ahead bias, and point-in-time fundamentals including restatements and index membership.

### 1.6 Alpha decay and crowding

Beyond McLean & Pontiff, crowding is usually measured through pairwise correlation among long-short factor portfolios, short-interest and institutional-ownership concentration, valuation spreads, and the sensitivity of returns to flows. McLean & Pontiff themselves find that published predictors show "post-publication increases in correlations with other published-predictor portfolios," a direct crowding signature.\[25\] A framework should report decay *curves* (performance by signal age and by time since discovery or publication), not just a single average.

### 1.7 Industry standards and how professionals evaluate

- **GIPS (CFA Institute).** The 2020 edition, published June 2019 and effective January 1, 2020, standardizes *presentation*: firm-wide compliance, composites, and new GIPS Pooled Fund Reports.\[31\] Firms are now only required to create composites for strategies offered as segregated accounts.\[32\] GIPS ensures fair, comparable *reporting of realized returns*. It does not assess backtests, trial counts, capacity or regime robustness, so it covers the honesty of the track record, not the validity of the strategy.
- **Indices.** HFRI, Eurekahedge, BarclayHedge, the SG CTA Index and the SG Trend Index provide peer benchmarks. They suffer from self-reporting, survivorship and backfill bias, and from composition drift (for example, the SG Trend Index includes each manager's largest program, and constituents change).\[33\]
- **Allocators and quant firms.** Public material from AQR and Man Group frames evaluation around net-of-cost risk-adjusted returns, diversification, behavior in equity drawdowns, and manager dispersion. Man Group's trend research finds all 20 of its trend proxies have higher crisis than non-crisis Sharpe.\[34\] Internal criteria at Two Sigma, Citadel or similar firms are not public.
- **HFT and market making.** Evaluation is microstructural: P&L per trade or per share; fill rate and fill probability by queue position; **markouts** (the mid-price move at horizons such as 1s, 10s or 60s after each fill), which reveal adverse selection; inventory risk (the Avellaneda–Stoikov and Guéant–Lehalle–Fernandez-Tapia frameworks); latency sensitivity; and very high intraday Sharpe ratios.\[35\]\[36\]\[37\] As one practitioner write-up puts it, "net edge per fill: half-spread − markout."\[38\]

### 1.8 Evaluation of ML-driven strategies

- **Gu, Kelly & Xiu (*RFS* 33(5), 2020).**
  - Trees and neural networks deliver "monthly stock-level R²'s between 0.33% and 0.40%" out of sample (0.33% for NN1, peaking at 0.40% for NN3).\[39\]
  - Yet a value-weighted long-short decile strategy on neural-net forecasts "earns an annualized out-of-sample Sharpe ratio of 1.35, more than doubling the performance of a leading regression-based strategy." The equal-weighted version reaches 2.45, versus 0.61 (value-weighted) and 0.83 (equal-weighted) for the linear benchmark.\[40\]\[41\]
  - An S&P 500 timing strategy reaches a Sharpe of 0.77 versus 0.51 for buy-and-hold.\[39\]

  The lesson is that **statistical fit and economic value diverge**. Frameworks must report both, and portfolio metrics must be net of costs. Equal-weighted results are concentrated in small, costly stocks.
- **The "virtue of complexity" debate.** Kelly, Malamud & Zhou (*JF* 2024) argue that heavily over-parameterized models (e.g., 12,000 random Fourier features from 15 predictors) improve market-timing performance even with negative out-of-sample R².\[42\]\[43\]
  - Nagel (2025, "Seemingly Virtuous Complexity in Return Prediction") shows the resulting strategy "effectively reduces to a certain volatility-timed momentum strategy" and that the regression "does not learn from the training data" that this is profitable.\[43\]
  - Buncic (2025) attributes the result to implementation choices, notably restricting the intercept to zero.\[44\]
  - "Is complexity virtuous?" (*Economics Letters* vol. 258, January 2026, article 112749) finds that "higher complexity does not outperform the buy-and-hold." Complex models "do not produce high utility gains, alpha, or dollar investment gains, nor necessarily outperform the more parsimonious ridge models."
  - Two points of context: Kelly is affiliated with AQR, and the debate is live.\[45\]

  The evaluation implications are concrete. Require **simple-model and placebo baselines** (e.g., run the same pipeline on i.i.d. noise), and decompose ML strategy returns onto known simple strategies such as volatility-timed momentum before crediting "ML alpha."
- **Competition scoring.**
  - *Numerai* has moved through CORR (correlation with target), MMC (meta-model contribution: correlation of the prediction neutralized to the meta-model) and TC (True Contribution: estimated portfolio-level marginal contribution after Numerai's optimizer). TC was dropped and MMC revived in January 2024, partly because TC depended on stake size and could not be computed for unstaked users.\[46\]\[47\] For the 2026 season the main tournament changed target to Ender20, with the CORR multiplier rising from 0.5 to 0.75 and MMC from 2.0 to 2.25.\[48\]
  - Kaggle's *Jane Street Real-Time Market Data Forecasting* scores a "sample weighted zero-mean R-squared," R² = 1 − Σw(y−ŷ)²/Σw·y². Its baseline is predicting zero, not the mean.\[49\]\[50\]

  These scoring choices are an important, under-used lesson: **the best-run evaluation operations score *marginal contribution to an existing portfolio*, not standalone accuracy, and they keep revising the metric as participants game it.**

### 1.9 Benchmarks for AI/LLM trading agents (2024–2026)

| Benchmark | Scope and metrics | Strengths | Weaknesses |
|---|---|---|---|
| **QuantBench** (Wang et al., arXiv 2504.18600) | Full pipeline from data to model to portfolio; temporal, graph and RL models\[51\]\[52\] | Industry-aligned standardization\[51\] | Equity-centric; findings stress distribution shift and "overfitting in low signal-to-noise environments"\[51\] |
| **InvestorBench** (Li et al., arXiv 2412.18174) | Stocks, crypto and ETFs; 13 LLM backbones; CR, SR, annualized volatility, MDD\[53\] | Multi-asset, many backbones | Pre-2021 stock data raises contamination concerns. Many LLMs fail to beat buy-and-hold (e.g., TSLA: Palmyra-Fin-70B CR −6.66 vs. B&H 39.24).\[53\]\[54\] |
| **StockBench** (Chen et al., arXiv 2510.02209) | 20 DJIA stocks over roughly March–June/July 2025 (82 trading days); return, MDD, Sortino; z-score composite\[54\] | Post-cutoff live-like window; composite rank | Very short window; between-model differences small relative to seed noise. The abstract ("most models struggle to outperform") and results text ("most tested models outperform") appear inconsistent.\[54\] |
| **TradingAgents** (Xiao et al., arXiv 2412.20138) | Multi-agent firm simulation; CR, AR, SR, MDD; Jan–Mar 2024\[55\] | Rich agent design | 3-month test; Sharpe of 8.21 on AAPL, which the authors say "exceeds our expected empirical range." No costs or significance tests; pre-cutoff window.\[55\] |
| **FINSABER** (Li, Kim, Cucuringu, Ma, KDD 2026; arXiv 2505.07078) | 2004–2024, 100+ symbols, bias-mitigated rolling windows\[56\]\[57\] | Long horizon and broad universe | Long-only timing strategies; buy-and-hold Sharpe 0.703 vs. FinAgent 0.241 and FinMem −0.228 in one setup\[56\] |
| **Profit Mirage** (Li et al., arXiv 2510.07920) | Pre- vs. post-cutoff decay; counterfactual leakage tests\[58\] | Directly measures contamination | Preprint. Reports Sharpe decay of 51–62% after the cutoff and claims "almost every published LLM-based agent fails to beat a random baseline once its knowledge cutoff is passed."\[58\] |
| **Agent Market Arena** (arXiv 2510.11695) | Live, continuously updated, multi-market\[59\] | Removes look-ahead by construction | Short live history; low statistical power |
| **Look-Ahead-Bench** (Benhenda, arXiv 2601.13770) | Look-ahead bias in point-in-time LLM workflows\[60\] | Standardized contamination diagnostic | Proof of concept; limited agent coverage\[61\] |

A 2026 survey (arXiv 2603.27539) lists "five pervasive evaluation failures (look-ahead bias, survivorship bias, backtesting overfitting, transaction cost neglect, and regime-shift blindness)" that "can reverse the sign of reported returns."\[62\] Across this literature, the more rigorous the protocol (longer windows, post-cutoff data, broader universes), the smaller or more negative the LLM edge becomes.

### 1.10 Open-source tooling

| Tool | Type | Standardizes | Gaps for this framework |
|---|---|---|---|
| QuantStats | Analytics/tearsheets | Sharpe, Sortino, Calmar, Omega, drawdowns, VaR/CVaR, tail ratio, rolling stats | No DSR/PBO, cost model or regime module |
| pyfolio / empyrical (community-maintained forks) | Analytics | Returns, risk, factor attribution, round-trip stats | Same; legacy Quantopian design |
| zipline (zipline-reloaded) | Event-driven daily backtester | Point-in-time pipeline, slippage/commission models | Equities/daily-centric |
| vectorbt | Vectorized research | Fast parameter sweeps (useful for producing PBO trial matrices) | Fill realism |
| Backtrader | Event-driven backtester | Broker simulation and analyzers | Performance at scale |
| QuantConnect LEAN | Multi-asset engine (cloud or local) | Realistic brokerage, fee and fill models; multi-asset data | Platform-coupled data |
| NautilusTrader | High-performance event-driven engine (Rust core) | Order-book-level, nanosecond-resolution backtest and live parity | Steeper learning curve |
| mlfinlab (Hudson & Thames) | AFML implementations | Purged CV, CPCV, PSR/DSR, labeling | Now closed-source and paid\[22\] |
| skfolio | scikit-learn-style portfolio optimization | CPCV, many risk measures (CDaR, CVaR, Ulcer, etc.) | Portfolio-centric; no execution layer |
| purgedcv (open source) | Validation library | Purged/embargoed walk-forward, CPCV with path reconstruction, PSR, DSR, MinTRL\[63\] | New; limited track record |

No single tool covers the full protocol. A reference implementation must compose them: a simulation engine, then a trial ledger, then the inference layer (DSR/PBO/SPA), then analytics, then the scorecard.

---

## Part 2 — Why No Single Standardized Benchmark Exists

1. **Heterogeneous frequency and holding period.** An HFT book's Sharpe annualized from per-second P&L reflects breadth (millions of bets), while a monthly factor book has perhaps 12 rebalance decisions a year. Lo's result shows that √q annualization is invalid under autocorrelation, and intraday P&L is strongly autocorrelated and seasonal. Even when annualized correctly, an HFT Sharpe of 10 at $50m capacity and a factor Sharpe of 0.8 at $10bn are not comparable investment propositions.
2. **Capacity and the denominator problem.** HFT returns on "capital" depend on what counts as capital (margin, inventory limits, technology spend). Factor books are capital-constrained, while HFT is constrained by opportunity and latency. Any standard has to specify the denominator.
3. **Non-stationarity.** McLean & Pontiff's decay, the 2024–25 trend drawdown and the changing composition of indices mean the data-generating process shifts under the benchmark itself.
4. **Different objective functions.** These include absolute return, benchmark-relative return, crisis hedging (where a CTA's *negative* unconditional alpha can be acceptable if it delivers convexity), capital efficiency, and marginal contribution to an existing portfolio (Numerai's MMC logic).
5. **Proprietary data and opacity.** Strategies built on alternative data cannot be reproduced by third parties, so evaluation must rely on attested outputs.
6. **Incentives and reporting bias.** Self-reported indices suffer survivorship and backfill bias. Research reports only winners, which is exactly the selection bias the DSR targets.\[11\]
7. **Gaming (Goodhart's law).** Any published scalar becomes a target. Goetzmann et al. show Sharpe, alpha and other measures can be manipulated.\[2\]\[7\] Numerai's repeated metric changes (CORR → MMC → TC → MMC, then new targets) are a live case study.
8. **Partial standardization attempts.** GIPS standardizes the honesty of presentation, not strategy validity; indices standardize peer comparison but inherit selection bias; academic tests standardize inference but need trial counts outsiders cannot see; AI benchmarks standardize tasks but mostly over short or contaminated windows. Each solves one layer, which is why the framework below is layered.

---

## Part 3 — Proposed Framework: the Quant Strategy Evaluation Standard (QSES)

### 3.1 Design principles

1. **A common clock and a common denominator.** Everything is scored on **daily net P&L divided by allocated risk capital**. Risk capital is defined as the larger of (a) margin plus haircut capital, (b) a capital charge equal to a fixed multiple of 99% one-day ES, or (c) the committed notional for unlevered books. This turns HFT, CTA and factor books into comparable daily return streams on the capital an allocator would actually commit.
2. **Inference before description.** Gates first, scores second.
3. **Conditional over unconditional.** Every headline metric also appears by regime.
4. **Report trade-offs, don't hide them.** Use a radar chart plus a Pareto frontier. Any composite carries declared weights and a sensitivity analysis.

### 3.2 Gates (pass/fail before any scoring)

| Gate | Metric | Default threshold | Rationale |
|---|---|---|---|
| G1 Selection-adjusted skill | DSR with declared N trials (effective N via clustering of trial correlations) | ≥ 0.95 | Bailey & López de Prado 2014 |
| G2 Overfitting | PBO via CSCV on the trial matrix | ≤ 0.20 (flag above 0.10) | Bailey et al. 2017 |
| G3 Net-of-cost significance | Lower bound of the 95% studentized circular-block-bootstrap CI on net Sharpe at target AUM | > 0 | Ledoit & Wolf 2008 |
| G4 Sample adequacy | Track record ≥ MinTRL for the claimed Sharpe (with skew/kurtosis) | Must pass | Avoids Sharpe claims on short samples |
| G5 Factor-zoo hurdle (cross-sectional signals) | t-stat of alpha against FF5+momentum or q-factors | ≥ 3.0 by default, *or* a declared FDR-based hurdle | HLZ 2016; Chen's critique means the FDR assumption must be disclosed |
| G6 Data integrity | Point-in-time audit, survivorship-free universe, purge/embargo applied, no leakage in features/labels | Must pass | — |
| G7 (LLM/agent only) Contamination | Evaluation window entirely after the backbone's knowledge cutoff, *or* counterfactual/leakage tests (e.g., Look-Ahead-Bench) passed | Must pass | Profit Mirage reports 51–62% Sharpe decay after cutoff |

Strategies that fail a gate are reported as "not scored" with the reason. They are not ranked low, because a low rank would still imply a credible measurement.

### 3.3 The eight scored pillars

| Pillar | Primary metrics | Secondary/diagnostic | Interpretation guidance |
|---|---|---|---|
| **P1 Return** | Net CAGR on risk capital; FF6/q-factor alpha (net); IR vs. a declared benchmark | Hit rate, profit factor, payoff ratio | Alpha against the richest relevant factor model is what counts. Report the alpha attenuation across the model hierarchy. |
| **P2 Risk** | Lo-adjusted Sharpe; Sortino; CDaR₉₅; ES₉₇.₅ (daily); MaxDD and longest time underwater | Ulcer, Pain, Omega(0), tail ratio, skew/kurtosis, downside beta | Negative skew plus high Sharpe is a red flag (possible option-selling). Report MPPM (ρ = 2 and 3) as a manipulation check. |
| **P3 Statistical Robustness** | DSR value (beyond the gate); PBO; haircut Sharpe (BHY); SPA p-value vs. benchmark family | CPCV distribution of OOS Sharpe across paths; parameter-plateau width | Score the *distribution* of CPCV-path Sharpe ratios (median and 10th percentile), not the single best path. |
| **P4 Regime Adaptability** | Net Sharpe and return by regime (vol terciles, equity bull/bear, rate up/down, liquidity-stress, named crises split into "slow-burn" and "V-shock"); crisis beta to equities | Rolling-24m Sharpe stability; HMM-filtered regime attribution; convexity (return regressed on equity return and its square) | Penalize single-regime dependence. Reward strategies whose worst-regime Sharpe is not catastrophic. Credit convexity explicitly for hedging mandates. |
| **P5 Implementation & Capacity** | Net/gross Sharpe ratio; cost drag (bps/yr); capacity at which net Sharpe falls by 25% and at which it reaches 0; turnover | Borrow/financing cost; sensitivity to doubling impact coefficient; latency sensitivity (HFT) | Use the square-root impact law as the default tier. A strategy scoring well only at tiny AUM is flagged "capacity-limited." |
| **P6 Consistency/Stability** | % positive months/quarters; rolling Sharpe dispersion; alpha-decay slope (performance vs. signal age and since go-live) | Stability of factor loadings; live-vs-backtest Sharpe ratio | Use McLean & Pontiff as the prior: live/backtest ratios near 0.5–0.75 are normal, ratios far below that are a warning. |
| **P7 Diversification/Factor Purity** | Correlation to equities, bonds and the peer index; R² on standard factors; marginal Sharpe contribution to a reference portfolio (e.g., 60/40 or the allocator's book) | Crowding: correlation with published-factor portfolios; drawdown co-occurrence | Mirrors Numerai's MMC/TC insight: value lies in *marginal* contribution, not standalone strength. |
| **P8 Operational/Model Risk** | Reproducibility (independent rerun within tolerance); model complexity vs. a simple baseline; dependence on single data vendors; explainability of exposures | Code/data lineage; kill-switch and risk-limit design; for LLMs, inference cost per decision and output variance across seeds | Complexity must earn its keep against a placebo and a simple-model baseline (lesson of the KMZ–Nagel–Buncic debate). |

**Selected formulas:**

- **Lo-adjusted annualization:** SR_annual = η(q)·SR_period, where η(q) = q / √(q + 2Σ_{k=1}^{q−1}(q−k)ρ_k) and ρ_k are return autocorrelations.
- **PSR:** PSR(SR*) = Φ[ (ŜR − SR*)·√(T−1) / √(1 − γ̂₃ŜR + ((γ̂₄−1)/4)ŜR²) ].
- **DSR:** PSR evaluated at SR₀ = √V[ŜR_n]·((1−γ)Φ⁻¹(1−1/N) + γΦ⁻¹(1−1/(N e))), where γ is the Euler–Mascheroni constant and N is the effective number of trials.
- **MPPM:** Θ = (1/((1−ρ)Δt))·ln( (1/T)Σ[(1+r_t)/(1+r_f,t)]^(1−ρ) ).\[2\]
- **Convexity:** r_t = a + b·r_m,t + c·r_m,t² + ε. A positive c with significant t indicates crisis convexity.
- **Square-root cost:** C(Q) = ½·spread + fees + Y·σ_D·√(Q/V_D).

### 3.4 Methodology protocol

1. **Data standard.** Point-in-time fundamentals and index membership, delisting returns included, corporate actions adjusted, timestamps in UTC with publication latency. For LLM inputs, news and filings are time-stamped at *availability*, not event date.
2. **Trial ledger.** Every backtest run (parameters, features, universe, dates) is logged automatically by the research platform. N for DSR and the T×N matrix for PBO come from the ledger, not from self-report.
3. **Validation design.** (a) CPCV with purge = label horizon and embargo ≈ 1–5% of the sample, for model selection and the PBO/CPCV-path distribution. (b) An anchored walk-forward, refit on a fixed schedule, producing the reported equity curve. (c) A **sealed holdout**: the final 20–30% of history (or post-registration live data), opened once.
4. **Regime segmentation.** Regimes are predefined and published before evaluation: VIX terciles, equity drawdown > 10%, rate-cycle direction, liquidity-stress indicators, and named episodes (2008, Aug 2007 quant quake, March 2020, 2022, the 2024–25 trend drawdown). HMM/Markov-switching labels use filtered probabilities only.
5. **Cost model tiers.** Tier A (research): fixed bps per turnover. Tier B (default for scoring): spread + fees + square-root impact + borrow/financing. Tier C (HFT/MM and capacity claims): order-book replay with queue-position modeling and latency injection (e.g., NautilusTrader/LEAN-class engines). Scores use Tier B at the *declared* AUM; capacity curves use Tier B/C.
6. **Uncertainty.** Every headline metric gets a 90/95% interval from a stationary or circular block bootstrap, with block length set to the decorrelation time. Head-to-head comparisons use the Ledoit–Wolf test. Families of strategies use Hansen's SPA.
7. **Minimum track record.** MinTRL is computed per strategy. Low-frequency strategies that cannot meet it on live data are labelled "backtest-dominant," and their P3 score is capped.

### 3.5 Cross-frequency comparability

| Issue | Rule |
|---|---|
| Different P&L clocks | Aggregate all P&L to **daily** net P&L / risk capital for P1–P7. Intraday statistics go only in the class module. |
| Annualization | Use the Lo η(q) correction from daily data; never annualize per-trade or per-second Sharpe for cross-class scoring. |
| Capital denominator | Risk capital = max(margin + haircuts, k × ES₉₉, committed notional). Report sensitivity to k. |
| Capacity | Score at a *common allocation size* chosen by the allocator (e.g., $250m) and at each strategy's own max capacity. HFT scored at $250m will often be "capacity-capped," which is a true and decision-relevant fact. |
| Costs | All pillars use net-of-Tier-B costs; HFT uses Tier C. |
| Microstructure | HFT module: P&L per trade, fill rate, markout curve (e.g., 100ms–60s), adverse-selection share of spread, inventory half-life, latency-sensitivity curve.\[37\]\[64\] Reported, not cross-scored. |

### 3.6 Scoring and aggregation

1. **Peer-relative percentiles.** Each primary metric is converted to a percentile within a *declared peer universe*, with direction normalized so higher is better. A pillar score is the mean of its primary-metric percentiles, so 0–100.
2. **Visual reporting.** An eight-axis radar chart, with a shaded band showing the bootstrap interval.
3. **Pareto frontier.** Strategies are plotted on the allocator's two or three binding objectives (e.g., net Sharpe vs. crisis beta vs. capacity), and dominated strategies are flagged. This is the primary decision view.
4. **Optional composite.** Composite = Σ w_p·S_p with weights declared *before* scoring and tied to mandate archetypes. "Absolute-return core": Return 20, Risk 15, Robustness 20, Regime 10, Implementation 15, Consistency 10, Diversification 5, Operational 5. "Crisis diversifier": Regime 25, Diversification 25, and Return down to 10. Publish a **weight-sensitivity analysis**: the rank of each strategy under Dirichlet-sampled weights. A strategy is only "best" if it is best across most weightings.
5. **Dangers of collapsing to one number.** A composite invites Goodhart gaming, hides non-compensable failures (a strategy cannot buy back a PBO of 0.6 with high returns), and embeds value judgments. That is why gates are non-compensatory and the composite is optional.

**Reporting template (one page per strategy):**

| Section | Content |
|---|---|
| Header | Strategy class, asset universe, frequency, declared AUM, cost tier, peer universe, evaluation window, knowledge cutoff (LLM) |
| Gates | G1–G7 pass/fail with values (DSR, PBO, CI lower bound, MinTRL vs. actual, alpha t, leakage tests) |
| Pillar scores | P1–P8 percentiles with 90% intervals; radar chart |
| Headline metrics | Net CAGR, Lo-Sharpe [CI], Sortino, MaxDD/duration, CDaR, ES, MPPM(ρ=3), FF6 alpha (t) |
| Regime table | Sharpe/return by each predefined regime and named crisis |
| Capacity curve | Net Sharpe vs. AUM; capacity at −25% and at zero |
| Decay | Rolling Sharpe; live/backtest ratio; performance by signal age |
| Diversification | Correlations; marginal Sharpe to the reference portfolio |
| Class module | Microstructure / IC-TC / convexity / Greeks / LLM contamination |
| Governance | Pre-registration ID, trial count, holdout status, reproduction status |

### 3.7 Governance against gaming

- **Pre-registration.** The hypothesis, universe, signal family, parameter ranges, cost tier and evaluation metrics are time-stamped before research begins.
- **Automatic trial-count disclosure.** The trial count comes from the platform ledger (the DSR's N). Self-reported counts are not acceptable.
- **Sealed holdout plus live incubation.** Paper or small-capital trading for at least the MinTRL-implied horizon where feasible.
- **Independent reproduction.** A separate team or third party reruns the pipeline from raw data, within tolerance.
- **Immutable audit trail.** Hashed code, data snapshots and configs.
- **Metric rotation.** Like Numerai, the evaluator reserves the right to change secondary metrics. Gates stay fixed.

### 3.8 Implementation considerations

- **Reference architecture:** a point-in-time data store; a simulation engine (zipline/LEAN for daily, NautilusTrader for order-book); a sweep engine (vectorbt for trial matrices); a validation library (skfolio/purgedcv for CPCV, PSR/DSR, MinTRL); an inference module (PBO/CSCV, Ledoit–Wolf bootstrap, Hansen SPA, e.g., the `arch` package's SPA implementation); analytics (QuantStats/empyrical metrics); and a scorecard/reporting service.
- **Compute.** CSCV with S = 16 slices requires C(16,8) = 12,870 combinations over an N-column matrix, which is cheap. CPCV with refitting multiplies model training by the number of splits, which is expensive for deep models. Order-book replay for HFT is the dominant cost (terabytes of data per venue-year). LLM agents add per-decision inference cost: TradingAgents reports "11 LLM calls & 20+ tool calls/prediction," which is why most LLM benchmarks use very short windows.\[55\]

### 3.9 Worked illustration

The figures below are **illustrative and stylized**, consistent with the literature cited but not measurements of any real fund.

| Dimension | Multi-factor equity L/S (monthly) | Trend-following CTA (daily, 60+ futures) | HFT market maker (equities/crypto) |
|---|---|---|---|
| Gates | Usually passes DSR/PBO if trial count is honest; G5 alpha t ≥ 3 is the binding test, since many "factor" books are just FF6 beta | Passes on century-long evidence; individual-manager PBO depends on parameter search | DSR is trivially passed (huge T) but meaningless without honest N; G3 depends entirely on Tier C costs |
| P1 Return | Moderate gross alpha; FF6 alpha often small | Low-to-moderate unconditional return; alpha vs. equities/bonds near zero in calm years | Very high return on risk capital at small AUM |
| P2 Risk | Exposed to factor crashes (e.g., the Aug 2007 quant quake); negative skew possible | Positive skew, long-option-like profile; deep, long drawdowns (−20.4% for the SG Trend Index, May 2024–May 2025) | Low daily volatility; tail risk from inventory gaps and outages |
| P3 Robustness | Medium: heavily mined space (HLZ, McLean–Pontiff decay) | High at strategy level (long history), medium at manager level | Statistically very strong on daily P&L; vulnerable to market-structure breaks |
| P4 Regime | Weak in crowded unwinds and junk rallies | **Strongest:** +20.9% (2008) and +27.4% (2022) vs. ACWI −42.2%/−18.4%; *weak* in V-shaped shocks (March 2020) and choppy markets | Earns more in high volatility *if* adverse selection is controlled; risk of losses in flash events\[65\]\[66\] |
| P5 Implementation & capacity | High capacity (billions), moderate costs | High capacity in liquid futures; roll and impact costs at scale | **Weakest:** capacity-limited; latency and queue-position dependent; tech-capex-heavy |
| P6 Consistency | Medium; decay after publication | Low month-to-month consistency; long flat periods | Very high (most days positive) |
| P7 Diversification | Moderate correlation with other quant equity books (crowding) | **High**: low or negative correlation with 60/40 in slow crises | High standalone, but small in size |
| P8 Operational | Data-vendor dependence; moderate | Simple, transparent rules | Highest operational and technology risk |
| Class module | IC ~0.02–0.05, TC, turnover | Convexity coefficient c > 0; crisis beta < 0 | Markout curve, fill rate, inventory half-life, latency curve\[37\] |
| **Pareto read** | Dominates for capacity-weighted alpha | Dominates for crisis diversification | Dominates for Sharpe at small size; dominated at institutional ticket sizes |

**Interpretation.** On standalone Sharpe the HFT book "wins." On the common risk-capital clock at a $250m allocation it is capacity-capped. The CTA wins on regime adaptability and diversification despite the weakest consistency. The factor book wins on scalable alpha only if its FF6 alpha survives the t ≥ 3 gate. No single score captures this, but the Pareto view makes the choice explicit: the right answer depends on the allocator's binding objective.

---

## Part 4 — Limitations, Pitfalls and Open Questions

1. **Non-stationarity limits every backtest.** Purging and CPCV address leakage, not regime change. Live/backtest decay (26–58% in McLean & Pontiff) means even gated strategies should be sized with a haircut.
2. **Short samples for low-frequency strategies.** A monthly strategy with a true Sharpe of 0.5 needs decades to reach significance. MinTRL will often fail, and the framework honestly caps such strategies' robustness scores instead of pretending.
3. **Trial counts are hard to observe.** DSR and PBO are only as honest as the ledger. External allocators usually cannot see N, which is why governance is part of the standard rather than an add-on.
4. **The FDR hurdle is contested.** HLZ (t > 3) versus Chen (5% FDR implies a hurdle of about 2.3–2.8) shows that the hurdle depends on priors about how many true factors exist. The framework makes this assumption explicit rather than resolving it.
5. **Convex and asymmetric payoffs.** Sharpe penalizes upside volatility and flatters short-option strategies. MPPM, Omega and convexity regressions help, but with only a handful of crises per century, inference on "crisis alpha" is inherently low-powered, and it differs by crisis type (2008/2022 vs. March 2020).
6. **Data-availability asymmetries.** Order-book and alternative data are costly and proprietary, so third-party reproduction of HFT or alt-data strategies is often impossible. Attested-output evaluation (signed P&L from prime brokers, third-party verified logs) is the practical substitute.
7. **LLM/agent contamination.** Pretraining on post-event text gives parametric look-ahead that cannot be fixed by filtering inputs.\[67\] Profit Mirage reports 51–62% Sharpe decay after cutoff, and FINSABER shows earlier LLM advantages "deteriorate significantly" over 20 years and 100+ symbols.\[56\]\[58\] Mitigations (post-cutoff windows, live arenas, counterfactual tests, point-in-time models) cut sample length sharply, so most LLM-strategy claims today are statistically underpowered. Treat any published LLM-agent Sharpe above about 2 on fewer than 12 months of data as unverified.
8. **Complexity versus interpretability.** The KMZ–Nagel–Buncic debate shows that sophisticated ML gains can collapse into simple known strategies, so replication decomposition should be routine. Composite weights, likewise, encode value judgments that the framework can only make explicit.

**Directions for future research:** auditable shared trial-ledger formats; Bayesian hierarchical evaluation for short samples; worst-regime or distributionally robust Sharpe; synthetic-market stress testing for convex strategies; point-in-time foundation models and contamination certificates for LLM trading; and MMC/TC-like marginal-contribution metrics generalized to allocator portfolios.

---

## Recommendations

1. **Adopt the protocol before the metrics.** Point-in-time data, a platform-logged trial ledger, CPCV plus walk-forward, and a sealed holdout give the largest gains in evaluation reliability.
2. **Make DSR, PBO, the net-of-cost bootstrap CI and MinTRL non-compensatory gates.** Never let high returns offset failed inference.
3. **Score all strategies on daily net P&L per unit of risk capital at a declared allocation size.** Keep microstructure, IC/TC, convexity and contamination diagnostics in class modules.
4. **Report regime-conditional performance by crisis type,** and credit convexity explicitly for diversifier mandates.
5. **Use percentile pillar scores, a radar chart and a Pareto frontier as the primary output.** Use a composite only with pre-declared, mandate-specific weights and a weight-sensitivity analysis.
6. **For ML strategies, require simple-model and placebo baselines,** plus decomposition onto known strategies such as volatility-timed momentum.
7. **For LLM/agent strategies, require post-cutoff evaluation windows or passed contamination tests,** report inference cost per decision, and run multiple seeds.
8. **Size live allocations with an explicit decay haircut,** using the McLean & Pontiff prior adjusted by the Harvey–Liu nonlinear haircut rather than a flat 50%.\[17\]

## Caveats

- Thresholds such as DSR ≥ 0.95, PBO ≤ 0.2 and the pillar weights are recommended defaults derived from the literature's conventions, not universally validated constants. Institutions should calibrate them.
- Several AI-benchmark sources cited are 2025–2026 preprints (e.g., Profit Mirage, Look-Ahead-Bench, StockBench), some with internal inconsistencies noted above.
- Internal evaluation practices of Two Sigma, Citadel and similar firms are not public; statements about industry practice rely on published AQR, Man Group, Cambridge Associates and Fidelity material.

## 資料來源

1. [\[2504.18600\] QuantBench: Benchmarking AI Methods for Quantitative Investment](https://arxiv.org/abs/2504.18600)
2. [Manipulation Proof Performance Measure - Breaking Down Finance](https://breakingdownfinance.com/finance-topics/alternative-investments/manipulation-proof-performance-measure/)
3. [Research Publication](https://alo.mit.edu/types/research-publication/page/11/)
4. [The Statistics of Sharpe Ratios by Andrew W. Lo :: SSRN](https://ssrn.com/paper=377260)
5. [Robust Performance Hypothesis Testing with the Sharpe ...](https://www.econ.uzh.ch/apps/workingpapers/wp/iewwp320.pdf)
6. [Robust performance hypothesis testing with the Sharpe ratio - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0927539808000182)
7. [Portfolio Performance Manipulation and Manipulation-Proof Performance Measures by William N. Goetzmann, Jonathan E. Ingersoll, Matthew I. Spiegel, Ivo Welch :: SSRN](https://www.ssrn.com/abstract=302815.)
8. [Portfolio Performance Manipulation and Manipulation-Proof Performance Measures by Jonathan E. Ingersoll, Matthew I. Spiegel, William N. Goetzmann, Ivo Welch :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1151564)
9. [Portfolio Performance Manipulation and Manipulation-Proof Performance Measures](https://ideas.repec.org/p/ysm/wpaper/amz2471.html)
10. [\[PDF\] Portfolio Performance Manipulation and Manipulation-Proof Performance Measures](https://www.semanticscholar.org/paper/Portfolio-Performance-Manipulation-and-Performance-Goetzmann-Ingersoll/51bb77035cac7e07e5119b0fd769af08b99dacce)
11. [The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality by David H. Bailey, Marcos Lopez de Prado :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)
12. [Deflated Sharpe Ratio (DSR). Balaena Quant Insights: Issue 24](https://medium.com/balaena-quant-insights/deflated-sharpe-ratio-dsr-33412c7dd464)
13. [The probability of backtest overfitting](https://www.researchgate.net/publication/318600389_The_probability_of_backtest_overfitting)
14. [The Probability of Backtest Overfitting by David H. Bailey, Jonathan Borwein, Marcos Lopez de Prado, Qiji Jim Zhu :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253)
15. [FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents](https://arxiv.org/pdf/2608.29372)
16. [Most claimed statistical findings in cross-sectional return predictability are likely true](https://arxiv.org/pdf/2206.15365)
17. [R-view: Backtesting](https://opensourcequant.wordpress.com/2016/11/17/r-view-backtesting-harvey-liu-2015/)
18. [Backtesting statistics — SOG. Excerpts from Backtesting \[2015\]](https://medium.com/@quant_views/backtesting-statistics-sog-34b52b18ed48)
19. [Avoiding Backtesting Overfitting by Covariance-Penalties: an empirical investigation of the ordinary and total least squares cases](https://arxiv.org/pdf/1905.05023)
20. [A Bayesian Approach to Measurement of Backtest - ProQuest](https://www.proquest.com/docview/2477135206)
21. [haircutSharpe Haircut Sharpe Ratio to correct for number ...](https://www.rdocumentation.org/packages/quantstrat/versions/0.16.7/topics/haircutSharpe)
22. [Methodology - purgedcv](https://eslazarev.github.io/purged-cross-validation/methodology/)
23. [Backtest Overfitting in the Machine Learning Era: A Comparison of Out-of-Sample Testing Methods in a Synthetic Controlled Environment by Hamid R. Arian, Daniel Norouzi M., Luis A. Seco :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4686376)
24. [Interpretable Hypothesis-Driven Trading: A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals](https://arxiv.org/html/2512.12924v1)
25. [Does Academic Research Destroy Stock Return Predictability? - MCLEAN - 2016 - The Journal of Finance - Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365)
26. [Does Trend-Following’s Recent Struggle Signal That the Strategy Is Structurally Broken? - Cambridge Associates](https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/)
27. [Trend-following crisis alpha: Does it come from beta timing or ...](https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9922231.PDF)
28. [Understanding Trend Following: A Strategic Diversifier for Modern Portfolios](https://larryswedroe.substack.com/p/understanding-trend-following-a-strategic)
29. [The Square-Root Law of Market Impact](https://bouchaud.substack.com/p/the-square-root-law-of-market-impact)
30. [\*\*\*The square-root law of market impact\*\*\*](https://www.linkedin.com/posts/jean-philippe-bouchaud-bb08a15_the-square-root-law-of-market-impact-activity-7266521587678416896-DsqS)
31. [A First Look at the CFA Institute’s Final 2020 GIPS Standards](https://www.klgates.com/A-First-Look-at-the-CFA-Institutes-Final-2020-GIPS-Standards-07-01-2019)
32. [2020 GIPS Standards Summary of Composites & More](https://www.acaglobal.com/industry-insights/2020-gips-standards-explanation-provisions-firms-sections-1-and-3/)
33. [Bringing Back “Crisis Alpha” - HedgeNordic](https://hedgenordic.com/2023/03/bringing-back-crisis-alpha/)
34. [A Trend Following Deep Dive: The Dynamics of Dispersion](https://www.man.com/insights/deep-dive-trend-following)
35. [Post-trade markout analysis](https://questdb.com/docs/cookbook/sql/finance/markout/)
36. [Markout: Definition, Formula and Trading Examples](https://kx.com/glossary/what-is-markout-and-how-is-it-calculated/)
37. [Adverse Selection & Markouts](https://www.machow.ski/posts/markouts_and_adverse_selection/)
38. [Options Market Making: Inventory Risk and Why Quotes Lean](https://hmaquant.substack.com/p/options-market-making-inventory-risk)
39. [Empirical Asset Pricing via Machine Learning](https://academic.oup.com/rfs/article/33/5/2223/5758276)
40. [Empirical Asset Pricing via Machine Learning](https://www.research-center.mirova.com/en/research-library/Empirical-Asset-Pricing-via-Machine-Learning)
41. [NBER WORKING PAPER SERIES EMPIRICAL ASSET PRICING VIA MACHINE LEARNING](https://www.nber.org/system/files/working_papers/w25398/w25398.pdf)
42. [GitHub - vishwesh-V/virtue-of-complexity: Replication and stress-testing of the "virtue of complexity" in return prediction (Kelly–Malamud–Zhou 2024) against the Gu–Kelly–Xiu foundation and the Nagel, Buncic, and Cartea critiques. · GitHub](https://github.com/vishwesh-V/virtue-of-complexity)
43. [Seemingly Virtuous Complexity in Return Prediction ∗ Stefan Nagel†](https://voices.uchicago.edu/stefannagel/files/2025/07/Complexity_2.pdf)
44. [New research debunks the “Virtue of Complexity in Return Prediction” in finance - Stockholms universitet](https://www.su.se/english/divisions/stockholm-business-school/news/articles/2025-09-25-new-research-debunks-the-virtue-of-complexity-in-return-prediction-in-finance)
45. [(PDF) The Virtue of Complexity in Return Prediction](https://www.researchgate.net/publication/376372811_The_Virtue_of_Complexity_in_Return_Prediction)
46. [True Contribution Details - Tournament - Numerai Forum](https://forum.numer.ai/t/true-contribution-details/5128)
47. [MMC staking starts Jan 2, 2024 - Announcements - Numerai Forum](https://forum.numer.ai/t/mmc-staking-starts-jan-2-2024/6827/1)
48. [Numerai Monthly: NumerCon Speakers, New Dataset & Target, 2026 Payout Updates](https://blog.numer.ai/numerai-monthly-numercon-speakers-new-dataset-target-2026-payout-updates/)
49. [Jane Street Real-Time Market Data Forecasting](https://www.kaggle.com/competitions/jane-street-real-time-market-data-forecasting)
50. [GitHub - Wy66wy/Jane-Street-Real-Time-Market-Data-Forecasting: Reproducible solution for the Kaggle Jane Street market forecasting competition: leak-free feature engineering, purged time-series validation, and timestep-by-timestep inference · GitHub](https://github.com/Wy66wy/Jane-Street-Real-Time-Market-Data-Forecasting)
51. [QuantBench: Benchmarking AI Methods for Quantitative Investment](https://arxiv.org/pdf/2504.18600)
52. [GitHub - SaizhuoWang/quantbench · GitHub](https://github.com/SaizhuoWang/quantbench)
53. <https://arxiv.org/pdf/2412.18174v1>
54. <https://arxiv.org/pdf/2510.02209v2>
55. <https://arxiv.org/pdf/2412.20138v7>
56. [Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?](https://www.alphaxiv.org/abs/2505.07078)
57. [Can LLM-based Financial Investing Strategies Outperform the Market in Long Run?](https://doi.org/10.1145/3770854.3785702)
58. <https://arxiv.org/pdf/2510.07920v1>
59. [When Agents Trade: Live Multi-Market Trading Benchmark for LLM Agents](https://arxiv.org/pdf/2510.11695)
60. [Look-Ahead-Bench: a Standardized Benchmark of Look-ahead Bias in Point-in-Time LLMs for Finance](https://ideas.repec.org/p/arx/papers/2601.13770.html)
61. [a Standardized Benchmark of Look-ahead Bias in Point-in- ...](https://arxiv.org/pdf/2601.13770)
62. [Toward Reliable Evaluation of LLM-Based Financial Multi-Agent Systems: Taxonomy, Coordination Primacy, and Cost Awareness](https://arxiv.org/html/2603.27539v1)
63. [purged-cross-validation/paper/paper.md at main · eslazarev/purged-cross-validation · GitHub](https://github.com/eslazarev/purged-cross-validation/blob/main/paper/paper.md)
64. [Resolving Latency and Inventory Risk in Market Making with Reinforcement Learning](https://arxiv.org/pdf/2505.12465)
65. [Multi-Level Market Making with Reinforcement Learning](https://arxiv.org/pdf/2608.18195)
66. [The Market Maker’s Dilemma:Navigating the Fill Probability vs. Post-Fill Returns Trade-Off](https://arxiv.org/html/2502.18625v2)
67. [Summoning the Oracle to Slay It: Mitigating Look-Ahead Bias in Financial Backtesting with Large Language Models](https://arxiv.org/pdf/2605.24564)