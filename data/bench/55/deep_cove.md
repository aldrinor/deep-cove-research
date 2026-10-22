# A Rigorous Benchmark for Comparing Advanced Quantitative Strategies

**A common evaluation protocol is feasible:** Multi-factor portfolios, high-frequency trading, and other advanced quantitative strategies can be compared rigorously through a standardized, multidimensional evaluation process. The appropriate benchmark is a common set of economic definitions, executable reference strategies, risk measures, regime tests, and reporting rules—not one universal market index or an unconditional league table.

**The central design choice:** Make returns, risk, and adaptability separate evaluation dimensions; require comparable capital, information timing, horizons, and cost accounting; and preserve strategy-specific diagnostics. Existing standards provide substantial building blocks, but the evidence supports mandate-dependent comparisons rather than universal scoring weights or a general multi-factor-versus-HFT winner.

| Evaluation question | Decisive specification or finding | Resulting judgment |
|---|---|---|
| What should be standardized? | Three dimensions: returns, risk, adaptability | Standardize the evaluation contract |
| Which benchmark should apply? | Four layers: mandate, peers, controls, objectives | Use complementary references |
| Which strategies belong together? | Match economic purpose, capital, risk, and horizon | Compare within declared decision tracks |
| How should returns be measured? | Compounded wealth, excess return, alpha, risk-adjusted and cost-adjusted results | Separate profitability from attribution |
| How should risk be measured? | Volatility, drawdown, downside, tails, liquidity, leverage, capacity, diversification | Use a risk panel and binding limits |
| How should adaptability be measured? | Direction–volatility states, transition losses, response times, stability | Test resilience and adjustment separately |
| What makes evidence credible? | Point-in-time data, executable orders, chronological validation, search disclosure | Apply an evidence gate before ranking |
| How should results be scored? | Raw panel first; explicit dimension scores and preference weights second | Publish conditional, sensitivity-tested rankings |

**The report’s roadmap:** The analysis first establishes the benchmark gap and comparison rules, then defines the return, risk, adaptability, and implementation layers. It subsequently specifies reproducible scoring, applies the framework to sourced multi-factor and HFT examples, and sets reporting and governance responsibilities.

## 1. What a standardized benchmark should mean

### The gap concerns joint evaluation

**Existing standards solve important pieces:** The Global Investment Performance Standards, or GIPS, standardize performance calculation and presentation. CFA Institute’s alternative-investment guidance nevertheless describes appropriate alternative-strategy benchmarks as a well-known problem and discusses market indices, peer groups, absolute-return targets, and liability-related references as different solutions. Calculation standards and benchmark suitability are therefore separate questions. [1]

**Institutional practice reaches similar conclusions:** Oregon State University’s 2026 investment materials explicitly recommend combinations of benchmarks because one benchmark does not answer every question across every horizon. They distinguish performance measurement—what happened—from attribution—why it happened—and appraisal—whether the outcome reflects desirable investment decisions. That distinction is particularly useful when comparing strategies whose return mechanisms differ fundamentally. [2]

**The documented gap is specific:** Existing approaches do not jointly settle executable net profitability, multidimensional risk, adaptation, capacity, and statistical credibility across both low-frequency portfolios and latency-sensitive trading. This supports developing a common protocol without making an exhaustive claim about every benchmark product in the market.

| Existing approach | What it answers well | Material weakness | Requirement for the common protocol |
|---|---|---|---|
| Broad-market index | Opportunity cost of market exposure | Mandate or leverage mismatch | Match exposures and financing |
| Factor-parent index | Value added within a selection universe | May omit execution and capacity | Add implementation-aware attribution |
| Manager or peer index | Relative performance among similar products | Reporting and selection biases | Preserve historical membership |
| Absolute-return target | Whether a return hurdle was met | Weak description of underlying risk | Pair hurdle with loss budgets |
| Static policy portfolio | Value added versus strategic allocation | Can become inappropriate as policy changes | Govern prospective revisions |
| Dynamic policy portfolio | Performance against changing allocation policy | Complexity reduces interpretability | Preserve rules and version history |
| Liability or inflation objective | Whether investor obligations were supported | Can conceal short-term risk exposures | Report objectives and market risk |
| Leave-one-out peer bucket | Relative results among heterogeneous products | Depends on bucket construction | Freeze eligibility and exclude self |

**Benchmark weaknesses imply concrete controls:** GIPS identifies five problems with hedge-fund peer indices: self-reporting, delayed reporting, restricted investability, survivorship, and opaque classification. These imply historical membership records, synchronized reporting, explicit access restrictions, terminal treatment of failed products, and transparent classification rules. A peer average can remain useful even when it is not an investable alternative, provided its role is clearly distinguished from an executable benchmark. [1]

**Broader coverage is not sufficient:** Gadzinski and Vacchino’s global-capital-stock approach covers 11 asset classes over 2005–2015, providing a broad reference for multi-asset allocation and exposure drift. But a global asset-value portfolio answers a different question from whether an intraday market-making system earns adequate returns on committed capital. Breadth cannot substitute for matching the investment decision. [3]

Section references:
[1] GIPS alternative-investment guidance <https://www.gipsstandards.org/wp-content/uploads/2021/03/alternative_investment_strategies_and_structures_gs_2012.pdf> Excerpt: "CFA Institute GIPS Guidance Statement on Alternative Strategies and Structures 1 Guidance Statement on Alternative Investment Strategies and Structures It is not possible to include a definitive list of every specific asset class, product, or strategy that…"
[2] OSU benchmarking framework <https://leadership.oregonstate.edu/sites/leadership.oregonstate.edu/files/2026-02/fac-4b-investment-performance-benchmarking.pdf> Excerpt: "Oregon State University’s investment program has grown in scale and sophistication since 2014, when independent governing boards were established and public universities in Oregon were empowered to manage their own investments. Distinct long term, bond rep…"
[3] Global capital-stock benchmark <https://rpc.cfainstitute.org/blogs/enterprising-investor/2017/benchmarking-multi-asset-portfolios-the-global-capital-stock> Excerpt: "More precisely, we calculated the global market value of the following 11 asset classes from 2005 to 2015 as our proxy for the global market portfolio: - Public equities - Private businesses - Government securities - Financial institution bonds - Non-finan…"

### Define the benchmark as an evaluation contract

**The proposed benchmark object:** A standardized benchmark is a versioned evaluation contract that transforms timestamped strategy decisions and executable positions into comparable economic outcomes. Its inputs are the mandate, eligible universe, information set, committed capital, risk limits, evaluation calendar, reference portfolios, execution assumptions, costs, regime definitions, and validation rules. Its outputs are a return panel, risk panel, adaptability panel, implementation diagnostics, uncertainty estimates, eligibility classification, and—when appropriate—a conditional score.

**The evaluated unit matters:** The primary unit is a deployable strategy variant at a specified capital scale, not an algorithm name. “Momentum,” “multi-factor,” or “HFT” identifies a family; a benchmarkable entry also specifies construction, financing, order handling, risk controls, and parameter-update rules. Two implementations of the same signal can consequently be separate entries.

**The economic chain governs evaluation:** Information must become a stable signal, feasible positions, executable orders, and returns after costs. A September 2026 review organizes public equity and crypto evidence around this “alpha-translation chain,” emphasizing that progress in prediction does not itself establish investment profitability. The framework should evaluate the whole chain rather than reward an upstream forecasting result as though it were realized alpha. [4]

The benchmark layers should answer distinct questions:

| Layer or gate | Decision question | Required inputs | Interpretation rule |
|---|---|---|---|
| Mandate-matched reference | Is active implementation worthwhile? | Executable reference, capital, exposures, costs | Primary opportunity-cost comparison |
| Peer or leave-one-out reference | Is it competitive within its category? | Historical membership, bucket rules, synchronized returns | Relative appraisal |
| Passive or no-signal control | Does complexity add economic value? | Same assets, constraints, accounting, evaluation dates | Incremental-value test |
| Investor-objective reference | Does it serve the intended outcome? | Return hurdle, liabilities, loss tolerance | Suitability assessment |
| Implementation and evidence gate | Are the results economically interpretable? | Timing, execution, data, validation, audit records | Determines ranking eligibility |

Section references:
[4] Alpha-translation review <https://doi.org/10.48550/arXiv.2609.04917> Excerpt: "We organize evidence with an alpha-translation chain: point-in-time information must yield a stable signal, feasible positions, executable orders, and risk-adjusted returns after costs. Across machine learning, time-series foundation models, financial language models, reinforcement learning, and agents, the examined record shows real but mainly upstream progress in prediction, text processing, portfolio design, and workflow integration. Evidence is thinner for durable net performance. Temporal contamination, repeated selec…"

### Principles that constrain the design

**Generality requires a common core:** Every strategy supplies the same economic outputs, while modular diagnostics describe its distinctive mechanisms. A factor portfolio needs exposure attribution; a market maker needs inventory and queue diagnostics. Neither should be forced into the other’s operational vocabulary.

**Rigor requires causal information timing:** Every decision must use information that existed when it was made. Training, normalization, regime estimation, and execution must obey the same rule. Statistical significance then needs adjustment for the search that produced the selected strategy.

**Comparability requires economic alignment:** Capital, risk appetite, financing, time horizon, and accounting must describe the same allocation decision. Matching annualized volatility alone does not accomplish this because liquidity, tail exposure, and capital requirements may still differ.

**Transparency includes unfavorable outcomes:** Failed variants, terminated strategies, adverse regimes, cost sensitivities, and changes to the benchmark belong in the record. This extends the GIPS emphasis on accurate inputs and consistent methodologies into research and execution reporting. [5]

**Implementation determines economic meaning:** A strategy is evaluated at an executable scale under a documented trading policy. CFA UK’s benchmark criteria—unambiguous, investable, measurable, appropriate, specified in advance, and adopted by the manager—provide the foundation. Independent benchmark oversight should coexist with the manager’s explicit acceptance of the reference, rather than permit retrospective benchmark substitution. [6]

**The practical judgment:** Standardize the evaluation contract and its outputs; retain multiple references because opportunity cost, implementation quality, competitive position, and investor suitability are different questions.

Section references:
[5] 2020 GIPS Standards <https://www.gipsstandards.org/wp-content/uploads/2021/03/2020_gips_standards_firms.pdf> Excerpt: "5.A.6 If the firm includes more than one benchmark in the gips composite report, the firm must present and disclose all required information for all benchmarks presented. 5.A.7 If the composite inclu…"
[6] CFA UK benchmark principles <https://www.cfauk.org/-/media/files/pdf/pdf/5-professionalism/3-research-and-position-papers/benchmarks-and-indices.pdf> Excerpt: "and appropriate regulatory oversight.’ 6 www.cfauk.org TABLE 1 –EXAMPLES OF INVESTMENT OBJECTIVES Investment objective Comment Assessment Achieve an investment return in excess of the policy asset mi…"

## 2. Comparing unlike strategies without erasing their differences

### A multidimensional strategy taxonomy

**Strategy labels are not exclusive:** Multi-factor describes how exposures are combined; high-frequency describes important aspects of trading technology and timing. A statistical-arbitrage strategy can also be multi-factor and high-frequency. A useful taxonomy therefore records economic exposure, execution role, asset class, holding period, rebalance interval, liquidity role, and leverage separately.

**Factor styles provide one classification:** Kolanovic and Wei group systematic styles into traditional beta, carry, momentum, value, and volatility, while also classifying asset classes and regions. They explicitly recognize that there is no unique taxonomy and that strategies can have multiple style designations. The proposed benchmark adopts this multi-label approach. [7]

| Strategy family | Main economic mechanism | Evaluation-relevant timing | Essential additional diagnostics |
|---|---|---|---|
| Multi-factor mixing | Combines separate factor sleeves | Declared portfolio rebalance schedule | Sleeve exposures and trade netting |
| Multi-factor integration | Selects joint factor characteristics | Declared signal and rebalance schedule | Factor purity and attribution |
| Trend or momentum | Exploits persistence | Signal horizon and reversal exposure | Turnover and trend dependence |
| Carry and volatility premia | Earns yield or insurance-related compensation | Funding and option horizons | Crash exposure and financing |
| Relative-value arbitrage | Trades departures from relationships | Convergence and financing horizon | Hedge error and liquidation risk |
| HFT market making | Supplies liquidity and manages inventory | Message-to-fill and inventory horizons | Queue, adverse selection, inventory |
| Aggressive HFT arbitrage | Captures short-lived price discrepancies | Feed, decision, and order latency | Opportunity decay and fill competition |
| Adaptive ML or ensembles | Changes forecasts or allocations with information | Training, update, and execution cycles | Retraining cost and adaptation attribution |

Section references:
[7] Systematic strategies across asset classes <https://www.cmegroup.com/content/dam/cmegroup/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf> Excerpt: "While there is no unique taxonomy, we classify the main factor styles as: Traditional Beta, Carry, Momentum, Value and Volatility . Additionally, many investors designate factors across traditional asset classes (equities, credit, currency, commodity, volatility) and geographic regions (Americas, Europe, Developed Asia, Emerging Markets and Frontier Markets) - e.g. US Equity Value, DM Bond Carry, etc. Notice that we have classified Volatility b…"

### Multi-factor construction changes the comparison

**Mixing and integration trade off:** Morningstar distinguishes mixing, which combines factor sleeves, from integration, which selects securities using combined characteristics. Mixing supports transparent attribution and can lower turnover, but may dilute overall exposures. Integration can produce stronger exposures while increasing active risk and making attribution more difficult. [8]

**Factor definitions create additional differences:** Sector-relative scoring can reduce sector bias but also reduce factor purity; universe-relative scoring may preserve stronger characteristics while introducing sector bets. Accordingly, a multi-factor entry must identify its parent universe, targeted factors, measurement definitions, combination method, aggressiveness, weighting, and rebalancing. A higher return produced by a sector concentration should be visible as such, rather than automatically attributed to superior factor selection.

**Risk allocation is another design choice:** Fixed factor weights, inverse-volatility weights, risk parity, and portfolio-level volatility targeting are different strategies, not reporting variations. Kolanovic and Wei distinguish cross-sectional allocation among factors from time-series allocation between a factor portfolio and cash. Both rules must be preserved in the strategy record. [7]

Section references:
[8] Morningstar multi-factor framework <https://www.morningstar.com/content/dam/marketing/shared/research/methodology/869053-FrameworkAnalyzingMultifactorFunds.pdf> Excerpt: "The conduct of Morningstar’s analysts is governed by Code influence on their factor exposures and ultimately their return and risk profiles.…"
[7] Systematic strategies across asset classes <https://www.cmegroup.com/content/dam/cmegroup/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf> Excerpt: "The process starts with an investor defining a strategy goal (alternative beta, enhanced beta, alpha, hedging), designing and selecting risk…"

### HFT is an execution umbrella

**HFT needs operationally explicit eligibility:** The MiFID II definition discussed in the 2022 Xetra study emphasizes latency-minimizing infrastructure, automated order initiation and routing, and high intraday message volumes. Short holding periods and low overnight inventory are also common empirical classification features. These characteristics distinguish HFT from algorithmic trading generally. [9]

**Liquidity provision and taking differ:** A passive market maker earns spread-related revenues while bearing inventory and adverse-selection exposure. An aggressive strategy crosses the spread and must earn enough subsequent price movement to cover that initial disadvantage. Baron, Brogaard, and Kirilenko find these different temporal profit patterns within the same E-mini futures market, illustrating why “HFT performance” is not a homogeneous category. [10]

**Reported frequency needs inspection:** Endres and Stübinger’s high-frequency pairs study uses minute observations and rolling formation/trading windows. The London Stock Exchange race study instead measures competition at microsecond resolution. Both inform fast-trading evaluation, but their data requirements, execution assumptions, and operational bottlenecks differ substantially. [11][12]

Section references:
[9] HFT definition and market study <https://doi.org/10.1007/s12599-022-00768-6> Excerpt: "Further, HFT is defined as a particular kind of algorithmi…"
[10] HFT risk and return <http://www.cftc.gov/sites/default/files/idc/groups/public/%40economicanalysis/documents/file/oce_riskandreturn0414.pdf> Excerpt: "8.42% (Row 4) of trade quantity, while taking liquidity ab…"
[11] Regime-switching pairs trading <https://www.econstor.eu/bitstream/10419/178766/1/1022453769.pdf> Excerpt: "with pairs trading application to the S&P 500 high-frequen…"
[12] Latency-arbitrage message study <https://www.nber.org/system/files/working_papers/w29011/w29011.pdf> Excerpt: "For example, if the market is at bid 10 – ask 12, so the m…"

### Apply comparability gates before calculating ranks

**Capital means committed economic capital:** Use the capital committed to support the strategy, including collateral and required liquidity reserves. Report returns on that denominator alongside notional exposure, margin, and return on deployed capital. Reusing capital repeatedly during a trading day does not justify treating each trade as a separately compounded investment.

**Risk matching has practical boundaries:** Strategies can share a target volatility or loss budget only when the corresponding positions are financeable and executable. Rescaling an HFT system can change queue competition and fill probabilities; rescaling a factor portfolio can change market impact and borrow requirements. Such strategies require re-execution of the simulation at the new scale, not just multiplication of historical returns.

| Comparison control | Common rule | Multi-factor application | HFT application |
|---|---|---|---|
| Economic purpose | Declare the allocation decision | Equity enhancement or premia allocation | Trading-business or diversifying allocation |
| Capital | Common committed-capital convention | Cash, shorts, collateral, reserves | Margin, inventory, clearing reserves |
| Risk | Shared budgets and financing limits | Factor and market exposures | Inventory and intraday exposure |
| Information cutoff | Use historically observable information | Fundamentals and constituent vintages | Feed receipt and message ordering |
| Evaluation horizon | Synchronized wealth observations | Daily valuation despite slower rebalancing | Aggregate executed intraday P&L |
| Costs | Common economic scope | Trading, borrow, funding, fees | Trading, technology, feeds, venues |
| Native diagnostics | Preserve mechanism-specific fields | Factor purity and sector attribution | Queue, latency, cancellation, fills |

**Two comparison tracks are useful:** A research track can hold the opportunity set and resource assumptions closely aligned to compare methods. An allocation track can compare different markets and instruments under a common investor objective, capital convention, and risk budget. The allocation track should not claim that residual performance differences isolate algorithmic skill, because market structure and opportunity sets remain part of the result.

**Cross-strategy reporting is not pooling:** Publishing several strategies in one scorecard does not mean combining them into a GIPS composite. GIPS requires composites to respect mandates, objectives, and strategies. The proposed scorecard compares separately defined entries while preserving those distinctions. [1]

**The practical judgment:** Compare the same economic decision on common axes, while retaining the exposures and execution conditions that explain why each strategy behaves differently.

Section references:
[1] GIPS alternative-investment guidance <https://www.gipsstandards.org/wp-content/uploads/2021/03/alternative_investment_strategies_and_structures_gs_2012.pdf> Excerpt: "CFA Institute GIPS Guidance Statement on Alternative Strategies and Structures 1 Guidance Statement on Alternative Investment Strategies and Structures It is not possible to include a definitive list of every specific asset class, product, or strategy that may be described as alternative . Investment types and portfolio structures that are within the scope of this guidance include, but are not limited to, the following: • Hedge funds and hedge-fund-like strategies • Funds of funds, where the underlying funds are invested in either traditional or alternative • Structured products requiring ongoing management…"

## 3. Return measurement: profitability, attribution, and cost

### Define the economic return first

**Unitized wealth is the foundation:** Construct a marked-to-market, cash-flow-adjusted wealth series that includes cash, collateral remuneration, derivatives settlements, distributions, and liabilities. External subscriptions and withdrawals should not become trading profits. Time-weighted returns are the default for strategy comparison; money-weighted returns can additionally describe an investor’s experience when external cash-flow timing matters.

For unitized wealth \(V_t\), cumulative return and annualized compounded return are:

$$r_t=V_t/V_{t-1}-1,\qquad R_{\mathrm{cum}}=\prod_{t=1}^{T}(1+r_t)-1,\qquad R_{\mathrm{CAGR}}=(1+R_{\mathrm{cum}})^{1/Y}-1.$$

Here \(Y\) is elapsed years under the declared calendar convention. A strategy that exhausts its capital follows the benchmark’s insolvency and termination rules; its wealth history should not restart silently.

**Arithmetic means answer another question:** An annual arithmetic mean describes expected one-period P&L under a specified capital convention; CAGR describes realized compounded wealth. Beketov, Prokopenko, and Järvis explicitly distinguish their arithmetic aggregate returns from compounded wealth performance. The common report should preserve that distinction in every table and calculation. [13]

| Return measure | Calculation basis | Interpretation | Required reporting |
|---|---|---|---|
| Absolute return | Unitized wealth and CAGR | Capital growth | Cumulative %, annualized %, dates |
| Benchmark-relative return | Strategy and reference wealth | Opportunity-cost performance | Annualized gap in percentage points |
| Alpha | Regression intercept on declared factors | Residual return after exposures | Annualized percentage points and interval |
| Risk-adjusted return | Excess return versus relevant risk | Compensation per risk unit | Sharpe, Sortino, Omega, conventions |
| Cost-adjusted return | Reconciled P&L and cost ledger | Executable economic profitability | Cost scope and return basis |
| Horizon-consistent return | Common valuation clock and window | Comparable investment experience | Sampling, calendar, annualization |

Section references:
[13] Return-aggregation distinction <https://doi.org/10.61093/fmir.10(3).1-27.2026> Excerpt: "Over the full sample, Sortino optimization produced the highest cycle-agnostic return of 0.88% per month, while the phase-conditioned highest-return strategy yielded an arithmetic aggregate of 289.44% compared with 212.96%, a difference of 76.48 percentage points that should not be interpreted as compounded wealth performance. The findings indicate the potential relevance of business-cycle information for strategic asset allocation and portfolio risk management…"

### Separate excess return from alpha

**Excess return is benchmark dependent:** Report the difference between strategy and benchmark CAGR in percentage points, and separately the relative-wealth return if required. These are different measures. For example, the published RAFI U.S. comparison is 13.9% annualized over ten years versus 12.9% for median multi-factor peers and 15.3% for the Russell 1000: calculated gaps of **+1.0 percentage point** and **−1.4 percentage points** per year, respectively. [14]

**Alpha is a model-dependent residual:** Estimate alpha on synchronized excess-return observations using a model specified before final evaluation:

$$r_{i,t}-r_{f,t}=\alpha_i+\beta_i^{\mathsf T}f_t+\varepsilon_{i,t}.$$

Report annualized arithmetic alpha as \(n\hat{\alpha}_i\), where \(n\) is the declared observations per year, with dependence-aware confidence intervals. This annualization is not a compounded investable return.

**Use nested attribution models:** A common market-and-cash model supports broad comparison; a strategy-appropriate factor model explains additional exposures. A value strategy may intentionally earn value-related returns, so removing that exposure answers a manager-skill question rather than whether the allocation itself was useful. Similarly, an equity factor model applied to futures HFT need not explain inventory, execution, or operational risks.

**Factor evidence illustrates attribution sensitivity:** Fain and Naffa’s ten-style study found significant positive value excess returns, insignificant size and momentum results, and significant negative results for earnings variability, volatility, and leverage. These findings reinforce the need to report which exposures are being rewarded rather than treat “multi-factor alpha” as one universal quantity. [15]

Section references:
[14] RAFI index comparison <https://etfdb.com/smart-beta-content-hub/multi-factor-strategies-guide-rafi-approach/> Excerpt: "12.9% for median multi-factor peers and 15.3% for the Russell 1000. - Developed Index: Returned a 12.3% 10-year annualized return vs. 12.0% for median multi-factor peers. - Emerging Marke…"
[15] Pure-factor comparison <https://doi.org/10.33893/fer.18.2.5286> Excerpt: "Excess return of the factors capturing riskiness (earnings variability, volatility, leverage) is significant and negative, which corroborates with our expectations, rendering a consensus…"

### Risk-adjusted measures need explicit conventions

**Sharpe is useful but incomplete:** Calculate the ratio from common-frequency net excess returns. Normality is not required merely to calculate Sharpe; the important problems are its reliance on two moments, unstable estimation, dependence-sensitive annualization, and limited description of asymmetric losses. Evidence from international long/short hedge funds shows that serial-correlation-aware evaluation can differ from standard monthly-to-annual Sharpe calculations. [16]

**Dependence changes annual risk:** Under independence, volatility scales by the square root of time. With autocovariances \(\gamma_k\), the variance of an \(H\)-period sum is instead:

$$\operatorname{Var}\!\left(\sum_{t=1}^{H}e_t\right)=H\gamma_0+2\sum_{k=1}^{H-1}(H-k)\gamma_k.$$

Use the same estimator and lag-selection rule across entries, and accompany it with block-bootstrap uncertainty. This prevents high-frequency observation counts or smoothed marks from creating artificial precision.

**Sortino isolates target shortfalls:** For a minimum acceptable periodic return \(m_t\), define target downside deviation using all observations in the denominator:

$$D_m=\sqrt{\frac{1}{T}\sum_{t=1}^{T}\min(r_t-m_t,0)^2}.$$

The periodic Sortino ratio is the mean return above the target divided by \(D_m\). State the target, sampling frequency, and annualization convention; conditioning the denominator only on negative observations produces a different measure.

**Omega adds threshold information:** At a declared threshold \(m\), Omega is total gains above \(m\) divided by total shortfalls below \(m\):

$$\Omega(m)=\frac{\sum_t\max(r_t-m,0)}{\sum_t\max(m-r_t,0)}.$$

Omega should be reported at its native horizon, not mechanically annualized. Calmar—the CAGR divided by positive maximum-drawdown magnitude—provides another useful diagnostic, but its path dependence makes synchronized windows essential.

Section references:
[16] Sharpe and Omega comparison <https://doi.org/10.19030/iber.v13i3.8588> Excerpt: "Based on mean-variance theory, the Sharpe ratio only considers the first two moments of return distributions, so hedge funds characterised by asymmetric, highly-skewed returns with non-negligible higher moments may be misdiagnosed in terms of performance. The Sharpe ratio is also susceptible to manipulation and estimation error. These drawbacks have demonstrated the need for augmented measures, or, in some cases,…"

### Use a reconciled cost hierarchy

**“Net” must identify its scope:** Trading-net, investor-net, and business-economic returns answer different questions. A fund investor may pay management fees that finance the manager’s staff and systems; subtracting both that fee and the same overhead from the investor’s return would double count. Conversely, comparing an HFT trading desk’s gross revenue with a fund investor’s after-fee return would mix accounting levels.

| Return layer | Costs included | Primary use |
|---|---|---|
| Paper or decision-price return | Declared hypothetical decision-price portfolio | Signal and implementation attribution |
| Trading-net return | Execution, commissions, financing, borrow | Trading-process evaluation |
| Investor-net return | Trading costs and investor-borne fund charges | Allocation comparison |
| Business-economic return | Trading costs and attributable operating expenses | Trading-business profitability |

**Actual fills already embed costs:** When P&L uses executed prices, spread crossing and realized slippage are already reflected. Implementation-shortfall attribution explains the gap from the paper portfolio; it should not be deducted a second time. CFA Institute defines implementation shortfall through actual versus decision-price paper performance and separates delay, execution, and opportunity costs. [17]

**Execution references are not return indices:** Arrival price suits urgent short-term alpha; VWAP or TWAP suits participation over an execution horizon; closing price suits close-valued index exposure. These assess trading quality, not whether the investment strategy itself is attractive. The report should therefore retain execution and investment benchmarks as separate fields. [17]

Section references:
[17] Implementation-shortfall guidance <https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/trade-strategy-execution> Excerpt: "Trade execution should be well integrated with the portfolio management process, and although trading strategies will vary on the basis of market and security type, all trade activity should be evaluated for execution quality and to assess broker and trade venue performance consistent with the fund’s objectives. Additionally, firms should have proper documentation of trade…"

### Synchronize horizons without hiding native risk

**Use common wealth observations:** Aggregate HFT P&L into the same daily valuation clock used for the allocation comparison, while retaining intraday marks for operational and risk analysis. Slower rebalancing does not imply monthly-only valuation. Bailey and colleagues require synchronous observations and common-index aggregation when comparing configurations with different trading frequencies. [18]

**Preserve calendars and cash accrual:** Cross-market reports must declare time zones, holidays, currency conversion, overnight valuation, and cash interest. Artificially adding unchanged observations or carrying stale prices can alter volatility and correlation. Annualization should follow the declared observation calendar, not whichever multiplier produces the most attractive ratio.

**The practical judgment:** Returns become comparable only after wealth accounting, benchmarks, factor models, costs, and calendars are explicit; a headline annualized percentage is not enough.

Section references:
[18] Synchronous performance-matrix rule <https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf> Excerpt: "should not be applied to an analysis with less than 1, 000 observations. example, if a strategy trades on a weekly basis, hold-out should not be used on backtests of less than 20 years. Along the same lines, Van Bell…"

## 4. Risk measurement: loss, liquidity, and scale

### Use distinct measures for distinct risks

**Risk requires a panel:** Volatility, drawdown, downside deviation, and expected shortfall describe different properties. IMAS warns that reliance on one or a few statistics prevents a holistic risk profile and recommends combining generic and strategy-specific analytics. The benchmark should make this panel mandatory even when only selected metrics enter a composite score. [19]

| Risk field | Common indicator and unit | Multi-factor emphasis | HFT emphasis |
|---|---|---|---|
| Volatility | Annualized return standard deviation, % | Market and factor contributions | Daily P&L plus intraday marks |
| Maximum drawdown | Peak-to-trough loss, %; recovery time | Factor-cycle duration | Inventory and liquidation path |
| Downside risk | Target downside deviation, % | Sustained factor shortfalls | Adverse-selection losses |
| Tail risk | VaR and ES, % at stated horizon | Crowding and correlated exits | Latency, inventory, interruption |
| Liquidity risk | Shortfall, spreads, fill rates, liquidation time | Rebalance participation | Queue and accessible depth |
| Leverage | Gross/net exposure, margin, funding | Long/short and derivative exposure | Notional and committed reserves |
| Capacity | Capital supported at target economics | Impact and borrow constraints | Opportunity and message constraints |
| Diversification | Correlation, beta, concentration, tail contribution | Factor and sector overlap | Venue and inventory concentration |

**Volatility needs two clocks:** The common portfolio panel uses synchronized daily and monthly returns; HFT additionally reports intraday inventory and equity fluctuations. GIPS guidance documents three-year annualized ex-post standard deviation based on monthly returns, together with additional measures where appropriate. The allocation panel can retain this convention without allowing it to substitute for intraday controls. [1]

**Drawdown includes time underwater:** Define drawdown as a positive loss from the previous high-water mark:

$$D_t=1-\frac{V_t}{\max_{u\le t}V_u},\qquad \mathrm{MDD}=\max_tD_t.$$

Report the peak date, trough date, recovery date, and longest underwater period. If a drawdown continues at the evaluation endpoint, report its elapsed duration through that endpoint as an ongoing episode.

**Equal windows prevent unfair penalties:** A strategy observed for decades has more opportunity to encounter a large drawdown than a recently launched strategy. Report both the full history and synchronized comparison windows. Kolanovic and Wei explicitly discuss reasonable fixed drawdown windows to avoid disadvantaging longer records. [7]

Section references:
[19] IMAS risk and performance guidance <http://www.imas.org.sg/uploads/media/2015/11/17/1011_IMAS_Guiding_Principles_for_Investment_Risk_Performance_Analysis_Functions_20151116_-_Final.pdf> Excerpt: "that the most relevant set of risk statistics will differ by portfolio, and these should be discussed and agreed by both the investment and the risk management teams. There is a need…"
[1] GIPS alternative-investment guidance <https://www.gipsstandards.org/wp-content/uploads/2021/03/alternative_investment_strategies_and_structures_gs_2012.pdf> Excerpt: "the three-year annualized ex-post standard deviation (using monthly returns) of the composite and the benchmark. If a firm determines that the three-year annualized ex-post standard d…"
[7] Systematic strategies across asset classes <https://www.cmegroup.com/content/dam/cmegroup/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf> Excerpt: "7Global Quantitative and Derivatives Strategy 11 December 2013 Marko Kolanovic (1-212) 272-1438 marko.kolanovic@jpmorgan.com To be a viable investment, Risk Factors must be expected t…"

### Tail risk must retain confidence and horizon

**VaR is a threshold:** For loss \(L_h\) over horizon \(h\), value-at-risk at confidence \(c\) is its \(c\)-quantile. Expected shortfall averages the worst \(1-c\) fraction of outcomes. A precise definition that handles probability mass at the threshold is:

$$\mathrm{VaR}_{c,h}=q_c(L_h),\qquad \mathrm{ES}_{c,h}=\frac{1}{1-c}\int_c^1q_u(L_h)\,du.$$

The proposed core report uses 95% confidence at one-day and 20-trading-day horizons, with additional native-horizon measures. These are reporting conventions, not assertions that 95% captures every important failure.

**Measure multi-period losses directly:** Construct compounded horizon returns from the wealth series rather than automatically scaling one-day VaR. OLTA’s downside framework similarly uses actual overlapping horizon returns and distinguishes VaR, expected shortfall, and drawdown recovery. Overlapping observations must remain dependent observations in uncertainty estimation. [20]

**Historical tails need scenario companions:** Historical simulation describes experienced outcomes; it does not generate a shock absent from the history. Conditional risk models can supplement it, but they require their own forecast and exceedance validation. Rickenberg’s comparison of volatility, VaR, and CVaR targeting illustrates how risk-management conclusions depend on both the selected risk measure and forecast quality. [21]

Section references:
[20] Downside-risk measurement <https://app.olta.finance/research/11-downside-risk-framework> Excerpt: "For a holding horizon of h days, the engine forms the distribution of overlapping h-day returns from the basket NAV series: each observation is t…"
[21] Downside-risk targeting study <http://garpsalesforcepublic.s3.amazonaws.com/Content__c/a1Z1W000003mRmtUAE/a2r1W0000015Rx0QAE_Whitepaper.TailRisk.Oct19.pdf> Excerpt: "273-274) propose to reflect the current volatility background, estimated by a dynamic volatility model, and account for heavy tails in the condit…"

### Liquidity and leverage alter apparent performance

**Displayed liquidity is not executable liquidity:** A factor portfolio needs participation rates, liquidation time, spreads, and impact. HFT also needs execution probability, queue position, failed cancellations, non-execution cost, and depth accessible before the opportunity disappears. Kwan and Philip show why market-wide depth can overstate liquidity available to a particular limit-order strategy. [22]

**Low overnight exposure is incomplete:** An HFT firm can end the day nearly flat while carrying substantial intraday inventory or operational exposure. Likewise, a market-neutral factor portfolio can have low net exposure but high gross leverage and borrow dependence. Report average and peak exposures, margin requirements, funding terms, collateral concentration, and stressed reserve needs.

**Leverage can reverse the conclusion:** CFA UK’s illustrative active-fund comparison changes materially after applying the same 30% gearing to the benchmark: the active fund’s reported net alpha moves from +0.58% to −2.42%. This is an illustration of denominator and exposure matching, not a general forecast of leverage effects. [6]

Section references:
[22] Limit-order execution costs <https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/29727/581062-A-Kwan-HFTExecutionCosts.pdf> Excerpt: "4 Additionally, market-wide measures of depth may overstate the actual liquidity available to investors. Van Kervel (20…"
[6] CFA UK benchmark principles <https://www.cfauk.org/-/media/files/pdf/pdf/5-professionalism/3-research-and-position-papers/benchmarks-and-indices.pdf> Excerpt: "^Net alpha is the excess return remaining after the costs for both funds have been deducted from the headline performan…"

### Capacity is a curve, not a label

**Report economics across capital scales:** Define capacity as the largest committed capital \(A\) at which the strategy meets its predeclared return hurdle and risk, liquidity, financing, and execution constraints:

$$A_{\mathrm{cap}}=\sup\{A:\text{return hurdle and all declared operating constraints hold at }A\}.$$

Report the underlying capital–return curve, not just the endpoint. A strategy may earn an attractive ratio at small scale yet contribute little deployable profit to a large portfolio.

**Market volume is only one constraint:** Percentage of average daily volume is useful for portfolio orders, but HFT capacity may instead bind through contested opportunities, queue priority, inventory, venue access, or message limits. CFA Institute identifies percentage of average daily volume as a standardized order-size measure and emphasizes that liquidity changes during crises. [17]

**The HFT bound illustrates denominator discipline:** Kearns, Nevmyvaka, and Kulesza estimate an aggressive-HFT upper-bound exercise of US$21 billion against approximately US$52 trillion of 2008 annual trading volume. The calculated ratio is about **0.0404%**, or **4.04 basis points of traded volume**—not a return on investment capital. Their exercise assumes omniscience, zero latency, no fees, and no market impact, and excludes passive HFT. [23]

Section references:
[17] Implementation-shortfall guidance <https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/trade-strategy-execution> Excerpt: "Percentage of average daily volume is a standardized measure used in trading that indicates what order size can realistically be traded. La…"
[23] Aggressive-HFT capacity exercise <https://www.cis.upenn.edu/~mkearns/talks/ParisMicrostructure.pdf> Excerpt: "• $21B vs ~ $52 trillion (TAQ) trading volume in same universe annually ( 0.05%) • 10% omniscience & no losses  $2.1B (consistent with Bro…"

### Evaluate diversification in the investor’s portfolio

**Standalone correlation is insufficient:** Report correlations, market and factor betas, concentration, and tail co-movement. Then assess the strategy’s marginal effect on the actual portfolio under normal and stressed conditions. A low unconditional correlation can conceal joint losses during the states in which diversification is most valuable.

**Neither family guarantees diversification:** Multi-factor portfolios can retain common sector or market exposure despite multiple factor labels. HFT strategies can concentrate in the same venues, instruments, counterparties, or latency-dependent opportunities. Cross-impact research also shows that correlated instruments cannot always be treated as independent execution problems. [24]

**The practical judgment:** Risk-adjusted performance must be judged together with loss persistence, executable liquidity, leverage, capital scale, and contribution to the investor’s existing risks.

Section references:
[24] Cross-impact and portfolio execution <https://ar5iv.labs.arxiv.org/html/1702.03838> Excerpt: "The main difference of our ELM and a model without cross-impact is that the impact costs of a large buy program can no longer be reduced as effectively by spreading the orders across multiple correlated inst…"

## 5. Adaptability across changing market conditions

### Separate direction, volatility, and crisis events

**Adaptability is an observed property:** A strategy is adaptable when it preserves useful economics or adjusts successfully as conditions change. It need not contain an explicit regime classifier. A simple fixed policy can be robust, while a complex adaptive model can react quickly but incorrectly.

**Direction and volatility are different:** A bull market can be volatile, and a bear market can decline gradually. Zegadło documents sensitivity in bull/bear classifications to amplitude and duration choices. Therefore, direction and volatility should be separate labels, while crisis events form an additional overlay. [25]

**A reproducible default is possible:** As a proposed baseline, label direction using the sign of the parent market’s trailing 126-trading-day return, observed through the preceding valuation time. Label volatility low, medium, or high using lagged volatility and rolling terciles, with the exact estimation window frozen in advance. Crossing two direction states with three volatility states creates six mutually exclusive evaluation cells; event windows are reported separately.

**Use locally relevant state variables:** RegimeFolio uses rolling 252-day VIX terciles at the 33rd and 67th percentiles, with approximate average thresholds of 17.8 and 23.1 in its U.S. equity application. Those numbers are sample descriptions, not universal thresholds for currencies, commodities, or crypto. Other markets should use their declared parent-market volatility or another economically justified state variable. [26]

| Regime procedure | Information basis | Strength | Required diagnostic |
|---|---|---|---|
| Lagged direction and volatility rules | Previously observed returns | Transparent and reproducible | Window and threshold sensitivity |
| Rolling volatility terciles | Historical state distribution | Adapts thresholds to local conditions | State persistence and turnover |
| Online hidden Markov model | Filtered state probabilities | Allows probabilistic transitions | Filtering lag and refit stability |
| Retrospective turning points | Completed price path | Useful descriptive stress segmentation | Separation from tradable labels |
| External event windows | Declared historical events | Captures operational and structural shocks | Event selection and overlap |

**Hindsight labels have a legitimate role:** Gupta and colleagues use a 15% turning-point threshold and a seven-trading-day neutral buffer for regime evaluation. Such labels can describe historical states or define a prediction target, but a forward shift alone does not make future-confirmed turning points observable in real time. Training labels must be complete before the training cutoff, and trading decisions must use filtered or otherwise historically observable information. [27]

Section references:
[25] Market-regime classification study <https://www.sciencedirect.com/science/article/abs/pii/S0275531921002245> Excerpt: "Title: Identifying bull and bear market regimes with a robust rule-based method Markdown Content: Skip to main content ( to article ( Image 2: Elsevier logo ( DGCID=rai_sd_header_ls_link) Journals…"
[26] RegimeFolio classification <https://arxiv.org/html/2510.14986v1> Excerpt: "Based on empirical analysis of the 2020–2024 sample, the rolling 252-day terciles correspond on average to thresholds of 17.8 (33rd percentile) and 23.1 (67th percentile). Notably, we report these…"
[27] Turning-point and oracle comparison <https://www.aimspress.com/aimspress-data/dsfe/2025/4/PDF/DSFE-05-04-019.pdf> Excerpt: "threshold of 15%, a convention consistent with prior studies in financial literature (Nystrup et al., 2017; Rapach et al., 2010). To mitigate the impact of short-term volatility and avoid abrupt t…"

### Define outputs for every state

**Each state gets the same panel:** Report net return, benchmark excess return, volatility, drawdown, expected shortfall, trading costs, liquidity, capacity, and exposure. Add observation count, elapsed duration, turnover, and the number of distinct episodes. Ten adjacent crisis observations are not equivalent to ten independent crises.

**Weighting changes the question:** Calendar-weighted aggregation describes the observed investment experience. Equal weighting across the six direction–volatility cells describes balanced state coverage. Both should be shown; a strategy that performs well because one favorable state dominates the sample should not be described as uniformly robust.

| Historical case | Scope or period | Main comparison purpose | Required outputs |
|---|---|---|---|
| Dot-com reversal | 2000–2002 equity drawdown | Factor and concentration resilience | Return, attribution, recovery |
| Global financial crisis | August 2007–March 2009 example | Correlation and funding stress | Tail loss, liquidity, leverage |
| Study-designated calm window | 2018 example | Low-turbulence behavior | Net edge and turnover |
| COVID-19 disruption | 2020 | Rapid volatility and liquidity change | Transition loss and execution |
| Geopolitical shock | 2022 example | Cross-asset structural change | Exposure and capacity |
| Xetra connectivity failure | 2 October 2017 | Operational interruption | Inventory, fills, liquidation |

**Historical windows require precise scope:** The FinTech cross-market study evaluates 12 instruments across three designated regime settings, producing 36 asset-period combinations. Its underlying subperiods overlap, so these combinations should not be treated as 36 independent macroeconomic experiments. They nevertheless demonstrate the value of retaining market-specific outcomes, including crude oil’s persistent active-strategy underperformance and negative futures-price episode. [28]

Section references:
[28] Cross-market regime tests <https://doi.org/10.3390/fintech5030082> Excerpt: "For this purpose, the period-level key performance indicators (cumulative return and Sharpe ratio) for all four strategies—buy-and-hold, the Base Strategy, the MAPE-filter, and the MAPE-position variant—are pooled across the 12 instruments and the three regimes into 36 asset-period cells ( Appendix B ( and four complementary, non-parametric tests are applied, each of which is designed to probe a different aspect of ro…"

### Measure response speed and recovery separately

**A response has several timestamps:** Record the externally defined event or reference break \(\tau_0\), detector decision \(\tau_d\), policy decision \(\tau_p\), executed adjustment \(\tau_x\), and stabilization or recovery time \(\tau_s\). For an online regime label, the benchmark must distinguish the state-assignment timestamp from an independently identified event timestamp.

The corresponding intervals are:

$$L_{\mathrm{detect}}=\tau_d-\tau_0,\qquad L_{\mathrm{decision}}=\tau_p-\tau_d,\qquad L_{\mathrm{execution}}=\tau_x-\tau_p,\qquad L_{\mathrm{stabilize}}=\tau_s-\tau_x.$$

Report raw clock time and economically relevant observations, such as rebalance opportunities or exchange messages. A microsecond quote response and a monthly factor reallocation serve different purposes.

**Response completion needs a rule:** A proposed operational convention is the time until at least 90% of the intended adjustment is executed and remains within the new risk limits for three scheduled monitoring observations. The intended adjustment, monitoring interval, and exceptions must be specified before evaluation. Performance recovery is a separate measure: for example, time to recover the pre-event high-water mark or regain a declared tracking band.

**Native measures remain essential:** Multi-factor response records factor-weight changes, publication availability, rebalance decisions, fills, and exposure restoration. HFT response records feed receipt, quote changes, acknowledgments, cancellations, inventory reduction, and liquidation. A detector refitted every 63 trading days does not necessarily have a 63-day detection lag; likewise, a 5–10-microsecond race gap does not measure economic recovery.

**Fast adjustment can be costly:** Frequent adaptation may reduce exposure to deteriorating conditions but increase turnover, false alarms, and adverse execution. Kolanovic and Wei explicitly describe the responsiveness–transaction-cost trade-off in volatility targeting and its tendency to surrender some protection during rapid market reversals. Response speed should therefore be paired with transition P&L and costs, not rewarded by itself. [7]

Section references:
[7] Systematic strategies across asset classes <https://www.cmegroup.com/content/dam/cmegroup/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf> Excerpt: "Figure 7: Growth, Inflation, Volatility and Liquidity during the past four decades Source: J.P. Morgan Quantitative and Derivatives Strategy. Regime factors are standardized to unit variance and zeros median. The five macro and market technical regime indicators discussed are not independent of one another. Table 2 below shows the correlation of these regime indicators over the past 40 years, as well as during five crisis periods. For instance, Volatility was negatively c…"

### Test whether adaptation adds value

**Controlled comparisons identify the mechanism:** Compare an adaptive strategy with the same underlying components held at fixed weights, the same policy with adaptation disabled, and a timing placebo. This separates the value of the assets or signals from the value of changing their weights. An oracle can provide an idealized upper reference, but not an executable investment benchmark.

**Positive results have counterexamples:** RegimeFolio reports 137% cumulative return and Sharpe 1.17 for 34 U.S. equities over 2020–2024. In contrast, Peisz, Saugy, and Turin-Plessia’s 2017–2025 holdout finds that neither tested regime-conditioned architecture separates from its controls or beats passive equal weighting of the same universe. [26][29]

**Architecture can dominate signal timing:** In the Peisz study, the continuous architecture returns 16.74% annualized versus −15.33% for the discrete architecture and turns over roughly one-third as much. Yet the two underlying sleeves finish only 26 basis points apart over the holdout, leaving little return difference for regime rotation to exploit. Better portfolio netting and lower turnover explain a large architecture contrast without establishing successful regime prediction.

**Stability needs repeated evaluation:** Report fold-level medians, interquartile ranges, lower-quartile returns, worst-fold losses, positive-excess-return frequencies, and sensitivity to small parameter changes. Measure post-launch retention separately from adaptation. Liu’s 1,726-strategy study reports a 2.1–3.1-percentage-point decline in volatility-adjusted returns from pro-forma to live periods, illustrating why historical stability and launch-period persistence belong in different fields. [30]

Section references:
[26] RegimeFolio classification <https://arxiv.org/html/2510.14986v1> Excerpt: "The framework achieves a cumulative return of 137%, a Sharpe ratio of 1.17, a 12% lower maximum drawdown, and a 15–20…"
[29] Controlled regime-allocation holdout <https://tfa-epfl.ch/research/papers/regime_based_strategy_final.pdf> Excerpt: "Both are evaluated on a 2017–2025 holdout set aside before any tuning, against three controls: the same two sleeves b…"
[30] Structured-strategy decay evidence <https://arxiv.org/html/2604.18821v1?ref=aligrithm.com> Excerpt: "Volatility-adjusted returns decline by 2.1--3.1 percentage points from the pro-forma to the live period, and a moving…"

### Stress the mechanism as well as prices

**Historical replay preserves joint conditions:** Replay crises with their observed prices, spreads, volumes, financing conditions, and interruptions. For multi-factor portfolios, examine factor crowding, correlated exits, borrow constraints, and rebalance concentration. For HFT, examine stale quotes, canceled connections, failed orders, inventory accumulation, and emergency liquidation.

**Hypothetical stresses test explicit dependencies:** A proposed sensitivity set halves available volume, doubles spreads, doubles volatility, moves correlations toward one, and evaluates capital at \(0.5A\), \(A\), and \(2A\). These are hypothetical perturbations, not forecasts. HFT additionally replays measured latency distributions with adverse shifts and venue outages; the engine must recalculate executions rather than subtract an arbitrary return penalty.

**The practical judgment:** Adaptability should mean useful, cost-aware behavior across states and transitions; the conclusion changes when controlled, locked evaluations show that adjustment adds repeatable value over simpler policies.

## 6. Implementation realism and evidence validity

### Make implementation change the result

**Costs are part of strategy design:** Bašić and colleagues calibrate a transaction-cost model using 269,836 institutional factor trades from July 2017 to March 2023 across the United States, Europe, and emerging markets. The regional trade counts sum exactly to that total: 99,420 + 46,905 + 123,511. Their historical factor-portfolio performance calculations cover longer periods and should be distinguished from this cost-calibration sample. [31]

| Region | Institutional trades | Median size, % of MDV | Median execution shortfall |
|---|---:|---:|---:|
| United States | 99,420 | 0.17% | 4 basis points |
| Europe | 46,905 | 0.37% | 3 basis points |
| Emerging markets | 123,511 | 1.24% | 9 basis points |

MDV is median daily volume, calculated over the preceding 25 trading days in this study; it is not identical to average daily volume.

**Median costs are calibration anchors:** They are not annual portfolio expenses or universal per-trade charges. Annual cost depends on trade-size distributions, turnover, liquidity, timing, and implementation policy. Multiplying a median cost by an unrelated turnover figure would discard precisely the size and liquidity dependence that the benchmark needs to preserve.

**Cost optimization changes factor economics:** Bašić and colleagues report momentum net returns rising from −1.52% to 2.18% per year and low-volatility net returns rising from 4.48% to 6.31% under their optimization. Their broader result is a trade-off: reducing expensive turnover can improve net performance while excessive cost penalties can remove the intended factor exposure. [31]

**Lower cost does not prove equivalence:** The same study reports roughly 80% exposure retention overall, portfolio-weight correlations above 90% in most cases, and tracking errors typically below 2%. These are separate diagnostics. A portfolio can remain close in tracking error while materially changing momentum exposure, so factor integrity cannot be represented by one similarity statistic.

Section references:
[31] Institutional factor-trading study <https://eprints.lancs.ac.uk/id/eprint/210994/3/BasicLohreMartinUtreraNolteNolte2023.pdf> Excerpt: "distributed across regions, with 99,420 trades for the US, 46,905 trades for Europe and 123,511 for EM. the trade size as a percentage of median daily volume (MDV), volatility and implementation shortfall. Median daily volume is calculated as the last 25 trading days median of daily volume. Range volatility is calculated using the past 15 days, and we only consider observations with range volatility between 5 and 100%. Implementation s…"

### Nonlinear impact determines scale economics

**Per-unit impact is often concave:** The 2011 Physical Review X study explains and supports approximately square-root price impact, contrasting it with a universally linear-impact assumption. Bašić and colleagues estimate a traded-size exponent of 0.67, with a reported 95% interval of 0.63–0.72 in their institutional sample. These findings support testing nonlinear shapes rather than imposing one exponent across all markets. [32][31]

**Concave impact still raises total costs:** As a proposed generic sensitivity form, let per-dollar impact be proportional to \((Q/V)^\delta\), where \(Q\) is order size and \(V\) is relevant market volume. Total currency impact cost is then proportional to \(Q^{1+\delta}\) when other inputs are held fixed. With square-root per-unit impact, doubling size multiplies total impact cost by approximately \(2^{1.5}=2.83\), a calculated scaling illustration—not a market-specific cost forecast.

**Cross-impact adds portfolio dependence:** Buying several correlated instruments can consume related liquidity rather than independent pools. The Trading Lightly study finds that ignoring cross-impact misestimates liquidity and leads to suboptimal execution. Its simplified model omits several other costs, so cross-impact should supplement, not replace, spread, fee, and nonlinear-size modeling. [24]

**Scale-aware utility can change rankings:** Li, DeMiguel, and Martín-Utrera show that squared Sharpe is insufficient when impact makes the factor efficient frontier nonlinear. Their comparison favors different factor models for high, medium, and low absolute risk aversion. The mechanism is economically important: turnover, liquidity, scale, and preferences change the value of a return distribution. [33]

Section references:
[32] Square-root impact mechanism <https://doi.org/10.1103/physrevx.1.021006> Excerpt: "X 1, 021006 – Published 31 October, 2011 We propose a dynamical theory of market liqu…"
[31] Institutional factor-trading study <https://eprints.lancs.ac.uk/id/eprint/210994/3/BasicLohreMartinUtreraNolteNolte2023.pdf> Excerpt: "a2 0.67 0.02 32.73 0.00 0.63 0.72 R2(%) χ2 Red. 4.5 38.57 0.00 Panel B: Simplified tr…"
[24] Cross-impact and portfolio execution <https://ar5iv.labs.arxiv.org/html/1702.03838> Excerpt: "We illustrate our results using a pool of US stocks and show that neglecting cross-im…"
[33] Factor models net of impact <https://wp.lancs.ac.uk/finec2023/files/2023/01/FEC-2023-068-Victor-DeMiguel.pdf> Excerpt: "We show that comparing factor models in terms of their squared Sharpe ratio is no lon…"

### HFT requires execution-aware replay

**A passive quote is not a fill:** An executable HFT test needs message sequencing, order acknowledgments, queue position, partial fills, cancellations, latency, venue rules, and inventory controls. A touched limit price cannot automatically be treated as an executed order. Aggressive trades must consume actual accessible depth and incur the relevant spread and fees.

**Failed messages contain information:** Aquilina, Budish, and O’Neill use complete London Stock Exchange messages, including failed trading and cancellation attempts. Their 43-day usable sample contains approximately 2.2 billion messages, and the modal winner–first-loser gap is 5–10 microseconds. A conventional order-book reconstruction that omits failed attempts cannot reproduce all the competitive information used in that analysis. [12]

**Latency changes others’ execution costs:** In the ASX ITCH experiment, Kwan and Philip estimate increases in non-HFT limit-order transaction costs relative to HFT of 1.73 basis points for institutional orders and 58.6 basis points for retail orders. Their proposed mechanism is faster access to favorable depth imbalances and cancellation of unfavorable quotes, which lowers slower traders’ execution probability and raises non-execution costs. [22]

**Market quality is a separate outcome:** The Xetra interruption study finds lower liquidity and higher volatility when low-latency connectivity is disrupted. Other studies discussed there find different effects in different settings, including reductions in adverse selection when the fastest traders lose their speed advantage. These findings concern market outcomes, not necessarily a particular HFT firm’s investment return. The benchmark should record external execution effects separately from investor profitability. [9]

Section references:
[12] Latency-arbitrage message study <https://www.nber.org/system/files/working_papers/w29011/w29011.pdf> Excerpt: "20 Figure 4.2: Percentage of 1st Successful and 1st Failed Messages by Firm (FTSE 100 Races) 010 20 1 2 3 4 5 6 7 8 9 10 1…"
[22] Limit-order execution costs <https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/29727/581062-A-Kwan-HFTExecutionCosts.pdf> Excerpt: "Using a differences-in-differences framework around the introduction of ITCH and a direct measure of limit order transacti…"
[9] HFT definition and market study <https://doi.org/10.1007/s12599-022-00768-6> Excerpt: "Since HFT provides additional order flow to securities markets, which is generally beneficial because more orders increase…"

### Protect the data and information set

**Point-in-time data prevents temporal contamination:** Preserve historical constituents, delistings, accounting-publication dates, corporate actions, identifier changes, and model versions. At high frequency, preserve exchange sequence numbers, feed provenance, timestamp resolution, clock alignment, and outage records. A strategy must not exploit a corrected price or revised fundamental before that revision existed.

**Cleaning rules need economic discipline:** Predeclare outlier treatment and inspect genuine extreme events rather than deleting them because they harm model performance. Negative futures prices, corporate restructurings, and exchange interruptions may be economically meaningful. Feature scaling and imputation must be fitted on training data; interpolation using later observations must not enter a trading-time feature.

**A participation estimate exposes selection:** Baron’s August 2010 table includes 14 aggressive, 30 mixed, and 21 passive HFT firms, totaling 65. A simple coverage estimate is \(65/85=76.5\%\) of the 85 distinct HFT firms identified across the broader study sample. This is a participation proxy, not an estimate of profitability bias; it shows why a balanced panel of survivors would change the population being evaluated. [10]

| Evidence threat | Concrete control | Diagnostic or retained artifact |
|---|---|---|
| Data errors | Versioned cleaning and reconciliation | Corrections and exclusion log |
| Look-ahead | Decision-time availability checks | Feature and order timestamps |
| Survivorship | Historical universe and terminal outcomes | Entry, exit, delisting records |
| Scaling leakage | Training-only transformations | Fitted preprocessing objects |
| Overlapping labels | Purging by information overlap | Removed training intervals |
| Data snooping | Full trial registry and adjusted inference | Search count and selection rule |
| Execution optimism | Event-aware simulation and live reconciliation | Orders, fills, rejected messages |
| Holdout reuse | Parameter lock and access log | Evaluation release history |

Section references:
[10] HFT risk and return <http://www.cftc.gov/sites/default/files/idc/groups/public/%40economicanalysis/documents/file/oce_riskandreturn0414.pdf> Excerpt: "Zhu, 2010, Individual investors and local bias, Journal of Finance, 65 (5), 1966, Mutual fund performance, Journal of Business, 39 (1), 119-138. Van Ness, B., R. Van Ness, and R. Warr, 2005, The impact of market-maker concentration on adverse selection costs for NASDAQ stocks. Journal of Financial Research, 28 (3), 461- Weller, B., 2013, Intermediation chains and specialization by speed: evidence from commodity futures markets, Working Paper. Figure 1…"

### Validate the entire research process

**Search disclosure is essential:** Bailey and colleagues show why nominal single-test significance fails after repeated strategy searches and propose probability-of-backtest-overfitting analysis using combinatorially symmetric cross-validation. Their method is useful for selection diagnostics, but chronology-preserving walk-forward tests remain necessary for a deployable adaptive system. Path-dependent statistics also require attention to observation order. [18]

**A strong historical record can mislead:** Arnott, Harvey, and Markowitz present a market-neutral ticker-letter strategy with nearly 6% annual alpha over a long historical span as a deliberately data-mined counterexample. They also report eight popular factors averaging 5.8% per year before publication versus 2.4% afterward, before fees and trading costs. Economic rationale, search disclosure, and prospective evidence therefore supplement conventional backtest statistics. [34]

**Use staged, chronological validation:** Development establishes economically plausible hypotheses and stable parameter regions. Walk-forward evaluation then trains and tunes only on earlier information, with purges covering overlapping labels and any embargo justified by the data dependency. Finally, a locked holdout tests the chosen policy, followed by prospective or live reconciliation.

**Concrete studies show different strengths:** A regime-aware LightGBM study reports Sharpe 1.18 with a 95% interval of 0.53–1.84, yet its Deflated Sharpe statistic of 0.69 does not meet the study’s corrected significance criterion. Separately, the GT-Score study reports better out-of-sample retention but lower raw test returns, 43.6% versus 46–50% for baselines. These are examples of why raw performance, uncertainty, and research-selection robustness must remain distinct outputs. [35][36]

**Prospective evidence has a distinct role:** A historical holdout can protect against direct tuning, but researchers may already know its broad market history. Arnott, Harvey, and Markowitz consequently regard live trading as the true out-of-sample experience. The report should distinguish historical holdout, prospective paper execution, and live-capital evidence rather than treat them as interchangeable.

**The practical judgment:** Implementation and evidence controls must affect eligibility and economic results directly; they should not be decorative disclosures attached to an otherwise frictionless ranking.

Section references:
[18] Synchronous performance-matrix rule <https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf> Excerpt: "The combinatorially symmetric cross-validation (CSCV) method we have proposed in Section 2.2 diﬀers from both K-FCV and LOOCV."
[34] Empirical-finance research protocol <https://people.duke.edu/~charvey/Research/Published_Papers/P138_A_backtesting_protocol.pdf> Excerpt: "average return of 5.8% a year in the span before the factors’ publica- tion and a return of only 2.4% after publication. This…"
[35] LightGBM validation <https://doi.org/10.3390/electronics15061334> Excerpt: "Backtested on 51 NASDAQ-100 constituents (2015–2026), the strategy achieved a portfolio Sharpe ratio of 1.18 (95% CI: 0.53, 1…"
[36] GT-Score comparison <https://doi.org/10.3390/jrfm19010060> Excerpt: "Key Finding: While GT-Score achieves slightly lower raw test returns (43.6% vs. 46–50%), it demonstrates a 56% higher general…"

## 7. Normalization, scoring, and uncertainty

### Normalize economic units before scores

**Raw results remain primary:** Publish committed-capital returns, actual leverage, costs, capacity curves, and native risk measures before normalization. Then align currencies, cash hurdles, valuation clocks, and comparison windows. Six- and twelve-month windows are useful short-horizon precedents, while longer synchronized windows remain necessary for persistent factor cycles and rare stresses.

**Volatility scaling has two meanings:** Liu rescales returns to a common 10% annualized-volatility level for descriptive cross-strategy analysis. Such ex-post scaling is a statistical normalization, not an implementable allocation policy. A tradable volatility-target strategy must instead use lagged risk forecasts, financing limits, and execution at the resulting position sizes. [30]

**The distinction prevents hidden foresight:** Multiplying a completed return series by \(10\%/\hat{\sigma}\) can help compare historical moments. It does not show that an investor could have selected that exposure before observing the window’s volatility. Both outputs can be useful, but they must have different labels.

Section references:
[30] Structured-strategy decay evidence <https://arxiv.org/html/2604.18821v1?ref=aligrithm.com> Excerpt: "To ensure cross-strategy comparability, returns are rescaled to a common 10% annua…"

### A complete proposed scoring rule

**Scores express declared preferences:** The following specification is a reproducible proposal, not an empirically established universal utility function. It uses three dimension scores—returns \(R\), risk \(K\), and adaptability \(A\)—on a 0–100 scale. All underlying measurements and denominators remain visible.

Define a monotonic benefit transformation \(F\) and a loss-to-budget transformation \(G\):

$$F(z)=50\left(1+\frac{z}{1+|z|}\right),\qquad G(q)=\frac{100}{1+q}\quad(q\ge0).$$

Thus \(F(0)=50\), \(F(1)=75\), and \(F(-1)=25\). For a loss equal to its budget, \(G(1)=50\); smaller loss-to-budget ratios receive higher scores.

**Freeze the economic denominators:** Let \(\sigma^*\) be the common annual risk reference, \(A^*\) the proposed allocation, and \(B_D\), \(B_E\), \(B_L\), and \(B_T\) the approved drawdown, expected-shortfall, stressed-liquidity-loss, and transition-loss budgets. These are mandate inputs fixed before evaluation. They are not estimated from whichever strategy performs best.

| Dimension | Component | Normalized input | Component weight |
|---|---|---|---:|
| Returns | Net excess profitability | Annual mean net excess return / \(\sigma^*\) | 100% of \(R\) |
| Risk | Drawdown | MDD / \(B_D\) | 25% of \(K\) |
| Risk | Tail loss | One-day ES95 / \(B_E\) | 25% of \(K\) |
| Risk | Stressed liquidity loss | Liquidation loss / \(B_L\) | 25% of \(K\) |
| Risk | Capacity coverage | \(A_{\mathrm{cap}}/A^*\) | 25% of \(K\) |
| Adaptability | Weakest-state profitability | Lowest six-state annual mean excess / \(\sigma^*\) | 40% of \(A\) |
| Adaptability | Lower-quartile stability | Lower quartile of annual-window excess / \(\sigma^*\) | 30% of \(A\) |
| Adaptability | Transition protection | Worst transition-window drawdown / \(B_T\) | 30% of \(A\) |

**Apply the transformations consistently:** The return score is \(F\) of its normalized input. Risk-loss components use \(G\); capacity uses \(100c/(1+c)\), where \(c=A_{\mathrm{cap}}/A^*\). Adaptability profitability and stability use \(F\), while transition protection uses \(G\).

**Fix measurement details in advance:** Use net excess returns over the same cash or investor hurdle, non-overlapping twelve-month windows for the stability component, and the six direction–volatility cells defined earlier. The proposed transition component uses the worst 20-trading-day drawdown following a declared state transition. Intraday responses and crisis-event losses remain additional mandatory diagnostics rather than being forced into that one horizon.

**Keep unscored diagnostics mandatory:** Alpha, Sharpe, Sortino, Omega, leverage, correlations, recovery time, and adaptation lags remain part of the decision. They are not all added to the composite because doing so would repeatedly reward closely related return or risk characteristics. The score’s narrower scope makes its meaning auditable.

**Hard constraints are non-compensating:** A high return score cannot offset a breached leverage limit, insufficient capital reserves, prohibited trading behavior, or an invalid information set. Similarly, cost-basis or valuation incompatibility determines comparison eligibility rather than receiving a favorable imputed score. Only complete eligible entries receive decision-grade composite ranks.

### Make weighting sensitivity part of the answer

**Three preference profiles are explicit:** Equal dimension weights provide a neutral reporting baseline, not a claim that investors universally value the dimensions equally. Capital preservation and return-oriented profiles expose how priorities change the result.

| Proposed profile | Returns | Risk | Adaptability | Composite |
|---|---:|---:|---:|---|
| Balanced reporting | 33⅓% | 33⅓% | 33⅓% | \((R+K+A)/3\) |
| Capital preservation | 25% | 50% | 25% | \(0.25R+0.50K+0.25A\) |
| Return oriented | 50% | 30% | 20% | \(0.50R+0.30K+0.20A\) |

**Rankings should reveal trade-offs:** First identify strategies that are dominated—worse on every relevant dimension under the same decision conditions. For the remaining strategies, report how ranks change across the declared weights, capital scales, costs, regimes, and parameter variants. This is more informative than presenting a preference-dependent ordering as a scientific constant.

**Do not confuse score and probability:** A score of 75 is neither a 75% probability of success nor an expected return. Likewise, a frequently top-ranked strategy in resampling is not guaranteed to remain top-ranked in a structural break. Statistical confidence, scenario robustness, and preference sensitivity describe different uncertainties.

### Reproduce uncertainty and rank stability

**Resample strategies jointly:** Use synchronized block resampling of strategy, benchmark, factor, and cost observations so common shocks and cross-strategy dependence are retained. Report paired differences rather than infer a difference merely because two separate confidence intervals look different. For drawdown, preserve chronological paths and check sensitivity to resampling design.

**Separate statistical and structural variation:** Bootstrap uncertainty describes sampling variation conditional on the observed process. Cost, latency, market-impact, regime-label, and capital-scale scenarios describe model or implementation variation. A useful report presents these separately before combining them into a decision envelope.

**Rank stability has a denominator:** For \(B\) declared resampling/scenario evaluations, report each strategy’s frequency at rank \(k\):

$$p_{i,k}=\frac{1}{B}\sum_{b=1}^{B}\mathbf{1}\{\operatorname{rank}^{(b)}_i=k\}.$$

Publish \(B\), the scenario weights or enumeration rule, tie treatment, and all eligibility changes. With \(N\) eligible strategies, an average top-rank frequency across them cannot exceed 100% unless ties are deliberately counted more than once and separately explained.

**The practical judgment:** A standardized metric panel can be general; a composite score is a reproducible, preference-dependent summary whose credibility depends on constraint compliance and rank sensitivity.

## 8. Worked comparison: multi-factor portfolios versus HFT

### Start with the strongest sourced comparisons

**Published factor results are heterogeneous:** Morningstar compares five long-only MSCI World factor variants over the fifteen years through 30 April 2018. All outperform their parent in absolute terms, and all but one have higher Sharpe ratios, despite substantial cyclicality and a prolonged value dry spell. This is evidence about named factor implementations and a period, not a permanent factor premium. [8]

**The cross-market RAFI comparison differs:** Its ten-year annualized results show that a strategy can outperform peers while underperforming its broad market, and that the answer changes by region.

| Published index comparison | Strategy return | Median peer return | Named market return | Calculated excess |
|---|---:|---:|---:|---|
| RAFI U.S., ten years | 13.9%/year | 12.9%/year | Russell 1000: 15.3%/year | +1.0 pp peers; −1.4 pp market |
| RAFI Developed, ten years | 12.3%/year | 12.0%/year | Peer comparison supplied | +0.3 pp versus peers |
| RAFI Emerging Markets, ten years | 10.3%/year | 9.1%/year | MSCI EM: 9.6%/year | +1.2 pp peers; +0.7 pp market |

These are the published comparison’s ten-year windows; the table does not assign them a newly inferred endpoint. [14]

**HFT subtype choice changes the headline:** Baron and colleagues identify 85 HFT firms in E-mini futures over August 2010–August 2012. The sample median firm has annualized Sharpe 4.30 and four-factor alpha 22.02%, while subtype averages differ materially.

| HFT subtype | Firms | Mean annualized four-factor alpha | Mean annualized Sharpe |
|---|---:|---:|---:|
| Aggressive | 18 | 90.67% | 4.29 |
| Mixed | 39 | 28.18% | 5.26 |
| Passive | 28 | 23.22% | 5.85 |

**Alpha and Sharpe select differently:** Aggressive firms have the highest mean alpha; passive firms have the highest mean Sharpe. The study links high risk-adjusted performance partly to inventory control and finds speed particularly important for liquidity-taking firms. Its revenues are reported gross of several operating expenses, so these results describe trading performance at the paper’s capitalization convention. [10]

**One pairs strategy supplies another anchor:** Endres and Stübinger report 93.73% annualized return and Sharpe 3.92 after stated transaction costs over 1998–2015. Their design uses 4,494 overlapping 35-day windows, comprising 30 formation days and five trading days, on minute-level S&P 500 constituent data. It should be evaluated as that particular historical implementation, not substituted for a generic microsecond-HFT return. [11]

Section references:
[8] Morningstar multi-factor framework <https://www.morningstar.com/content/dam/marketing/shared/research/methodology/869053-FrameworkAnalyzingMultifactorFunds.pdf> Excerpt: "As of April 30, 2018, there were 440 ind…"
[14] RAFI index comparison <https://etfdb.com/smart-beta-content-hub/multi-factor-strategies-guide-rafi-approach/> Excerpt: "It selects the top 25% of securities per…"
[10] HFT risk and return <http://www.cftc.gov/sites/default/files/idc/groups/public/%40economicanalysis/documents/file/oce_riskandreturn0414.pdf> Excerpt: "Table 3 reports the mean and standard de…"
[11] Regime-switching pairs trading <https://www.econstor.eu/bitstream/10419/178766/1/1022453769.pdf> Excerpt: "There are 4494 overlapping intervals of…"

### Apply one comparison matrix

**The same fields expose different mechanisms:** The following matrix applies the common framework to multi-factor construction variants and HFT execution roles. It identifies what drives the interpretation before any aggregate ranking is considered.

| Strategy variant | Return and alpha references | Principal risk mechanism | Adaptability test | Implementation requirement |
|---|---|---|---|---|
| Multi-factor mixing | Parent universe and sleeve attribution | Factor cycles and sleeve overlap | Fixed versus adaptive weights | Net external trades across sleeves |
| Multi-factor integration | Parent and joint factor exposures | Active risk and sector concentration | Exposure stability across states | Factor integrity after cost control |
| Passive HFT | Cash, executable quoting control, factor diagnostics | Inventory and adverse selection | Quote and inventory response | Queue-aware partial fills |
| Aggressive HFT | Cash and executable signal-disabled control | Spread crossing and opportunity decay | Latency and liquidity sensitivity | Accessible depth and true timing |
| Passive/control allocation | Same universe and capital convention | Declared market exposures | Identical regime slices | Equivalent financing and accounting |

**The allocation mechanism differs:** Multi-factor strategies usually depend on persistent exposures and the net economics of rebalancing. HFT depends more directly on executing small opportunities before competitors or adverse prices remove them. Factor optimization therefore risks diluting intended exposures; HFT execution optimization risks concentrating dependence on particular speed advantages, venues, or inventory limits.

**A decision-grade comparison has one gate:** Return and alpha leadership, drawdown and tail-risk leadership, adaptation speed, implementation and capacity leadership, the overall rank, and rank stability are decided by synchronized capital-defined wealth paths, common evaluation dates and regime labels, compatible risk budgets and benchmarks, fully reconciled costs, timestamped responses, and joint uncertainty analysis. The worked calculations below are source-moment diagnostics governed by that same gate.

### Work through sourced return and cost inputs

**A factor example has reconciled costs:** Bašić and colleagues’ optimized U.S. VMQL portfolio—value, momentum, quality, and low volatility—reports 12.27% annualized gross return, 10.73% net return, 12.24% volatility, and net Sharpe 0.88 over January 1985–March 2023 under the authors’ US$1 billion scale convention. Its cost components reconcile exactly at the displayed precision:

$$12.27\%-1.01\%-0.48\%-0.05\%=10.73\%.$$

The deductions are transaction costs, shorting costs, and fixed fees, respectively. [31]

**The HFT diagnostic uses pooled moments:** Baron’s passive-HFT firm-day distribution reports annualized mean return 25.69% and standard deviation 8.89%. Their ratio is a calculated **2.89**. This is a pooled population-moment ratio, distinct from the 5.85 average of firm-level Sharpe ratios; averaging ratios and taking a ratio of pooled moments are different operations. [10]

**Normalize both with identical arithmetic:** For a transparent diagnostic, treat the published annualized return inputs as annual mean moments, use a zero cash hurdle, and scale them to a 10% volatility reference. The zero-hurdle convention follows the HFT study and the return-to-volatility presentation of the factor table. These calculations estimate standardized moments; they do not reconstruct either strategy’s daily wealth path.

| Diagnostic field | U.S. VMQL portfolio | Passive-HFT pooled observations |
|---|---:|---:|
| Published annualized return input | 10.73% net | 25.69% gross |
| Published annualized volatility | 12.24% | 8.89% |
| Calculated return/volatility | 0.877 | 2.890 |
| Scaling factor to 10% volatility | 0.817 | 1.125 |
| Estimated standardized return | 8.77%/year | 28.90%/year |
| Return score at published cost basis | 73.36 | 87.15 |

The standardized estimates are \(10.73\%\times10/12.24=8.77\%\) and \(25.69\%\times10/8.89=28.90\%\). Applying the previously specified \(F\) transformation gives the displayed return scores.

**The comparison produces a useful threshold:** Let \(C_M\) and \(C_H\) be additional annual return drag, in percentage points on the original published capital bases, beyond each source’s reported cost scope. Under a constant-drag approximation that leaves the reported volatility inputs unchanged, the HFT moment proxy exceeds the factor proxy when:

$$\frac{25.69-C_H}{8.89}>\frac{10.73-C_M}{12.24},\qquad C_H<17.90+0.7263C_M.$$

The 17.90-percentage-point threshold is calculated as \(25.69-8.89(10.73/12.24)\). It is cost headroom within this source-moment comparison, not an estimate of HFT operating expenses or a forecast of investable superiority.

**Small fees need the correct denominator:** Baron reports a known US$0.15 trading fee per E-mini contract and approximately US$50,000 contract notional in the sample. The calculated fee is \(0.15/50{,}000\times10{,}000=0.03\) basis point per executed contract-side, or 0.06 basis point for two sides at that notional. Annual capital drag still depends on the number of executed sides, committed capital, and other costs.

Section references:
[31] Institutional factor-trading study <https://eprints.lancs.ac.uk/id/eprint/210994/3/BasicLohreMartinUtreraNolteNolte2023.pdf> Excerpt: "Sharpe ratio, volatility, turnover, shorting costs, fixed fees and transaction costs decomposed into two component…"
[10] HFT risk and return <http://www.cftc.gov/sites/default/files/idc/groups/public/%40economicanalysis/documents/file/oce_riskandreturn0414.pdf> Excerpt: "Table 3 reports the mean and standard deviation across firms, in addition to the 10th, 25th, 50th, 75th and 90th p…"

### Apply the remaining dimensions honestly

**Score bounds show decision sensitivity:** With the balanced composite, holding each published-cost-basis return score fixed while allowing risk and adaptability scores to span their defined 0–100 ranges produces algebraic envelopes:

| Score component | VMQL diagnostic | Passive-HFT diagnostic |
|---|---:|---:|
| Return score \(R\) | 73.36 | 87.15 |
| Risk score \(K\) | 0–100 by score definition | 0–100 by score definition |
| Adaptability score \(A\) | 0–100 by score definition | 0–100 by score definition |
| Balanced-score envelope | 24.45–91.12 | 29.05–95.72 |

These are mathematical bounds, not confidence intervals or simulated performance. Their overlap demonstrates how much information a return-only comparison leaves out.

**A ranking requires more than return:** At the displayed cost bases, the HFT return-score advantage is 13.79 points. Under equal dimension weights, it would be offset by a combined risk-and-adaptability disadvantage greater than 13.79 points. Additional costs change the return-score difference through the same monotonic formula.

**Capacity can alter the allocation choice:** The VMQL study reports net returns of 11.15%, 10.73%, and 10.21% per year at US$500 million, US$1 billion, and US$2 billion, respectively, for its U.S. implementation. The endpoint change is a calculated 0.94-percentage-point decline as scale quadruples. This is an informative capacity sensitivity, not a transferable HFT scaling rule. [31]

**Identical regime tests preserve fairness:** Both candidates would use the same daily direction–volatility labels, historical event windows, transition-loss horizon, and confidence procedures. Their native response logs would differ: factor weights and rebalance fills for VMQL, and quote, order, queue, and inventory responses for HFT. Neither a monthly rebalance interval nor a microsecond message gap substitutes for the common economic transition outcome.

**The practical judgment:** The sourced HFT observations have a stronger published return-per-volatility proxy, while the factor evidence gives directly interpretable cost and capital-scale comparisons; the framework turns that contrast into explicit decision conditions without converting heterogeneous studies into an investment winner.

Section references:
[31] Institutional factor-trading study <https://eprints.lancs.ac.uk/id/eprint/210994/3/BasicLohreMartinUtreraNolteNolte2023.pdf> Excerpt: "value assumptions: $500 million USD, $1 billion USD and $2 billion USD. The table is split into three regions: US, Europe and Emerging markets. The underlying sample period is J…"

## 9. Reproducible reporting, governance, and practical use

### Publish an auditable evaluation record

**Reproducibility starts before the backtest:** A report should connect each final metric to raw observations, transformations, model versions, decisions, orders, fills, costs, and valuation. Arbi’s reference implementation scripts the process from data acquisition through reporting, illustrating the right scope for an audit trail. [37]

| Reporting package | Required contents | Reproduction purpose |
|---|---|---|
| Strategy identity | Version, mandate, universe, parameters, update policy | Defines the evaluated entry |
| Data manifest | Providers, vintages, timestamps, identifiers, corrections | Reconstructs the information set |
| Capital and accounting | Cash flows, reserves, collateral, currency, valuation | Reproduces wealth and denominators |
| Execution and costs | Orders, fills, timing, fees, impact, financing | Reconciles paper and economic returns |
| Evaluation specification | Dates, references, regimes, folds, purges, trials | Recreates comparisons and selection |
| Results and governance | Raw panels, scores, intervals, ranks, approvals | Supports appraisal and accountability |

**Preserve intermediate artifacts:** Store point-in-time features, preprocessing fits, trained models, regime probabilities, portfolio targets, drifted holdings, order intentions, simulated or actual fills, and reconciled P&L. Record random seeds where relevant, software dependencies, dataset hashes, and calculation-code versions. Numerical outputs should be reproducible from an immutable release rather than the current state of a research notebook.

**Restricted data still need independent access:** Proprietary tick data or trading records can be reviewed within a controlled environment. Public reporting should expose schemas, calculation rules, aggregate reconciliations, and the scope of independent review. Synthetic examples can test software behavior, but they should remain labeled synthetic and should not replace empirical performance evidence.

Section references:
[37] Scripted backtesting and auditability <https://open.uct.ac.za/bitstream/11427/31158/1/thesis_sci_2019_arbi_riaz.pdf> Excerpt: "In order to be fully auditable the entire backtest process from data acquisition to report generation is scripted using the R programming language. These…"

### Assign responsibilities and update triggers

**Ownership should be independent:** A benchmark owner maintains definitions and versioning; data stewards maintain provenance; performance specialists reconcile returns; risk professionals approve budgets and scenarios; and an independent reviewer assesses methods and execution assumptions. Portfolio managers adopt the relevant mandate and reference before evaluation. IMAS supports independent risk measurement, model review, authorization, and regular backtesting. [19]

**Method changes create new versions:** Trigger review when venue rules, fees, financing, data feeds, execution calibration, strategy behavior, or market structure materially change. Repeated tail exceedances, persistent cost-model errors, rank reversals under modest assumptions, or evidence of information leakage also warrant review. Preserve the old specification and provide a bridge comparison rather than silently rewriting history.

**Eligibility should precede public ranking:** QFRS proposes seven reporting standards covering data construction, labels, point-in-time features, causal scaling, temporal splits, evaluation, and cost-aware backtesting. Its audit of 2025 Scopus-indexed forex forecasting papers finds no full compliance, with pass rates of 12.2% for economic backtesting and 31.7% for causal scaling. The relevant lesson is to gate comparisons on disclosed economic and temporal validity, not merely rank attractive reported metrics. [38]

**GIPS remains a complementary foundation:** Applicable GIPS presentations normally begin with five years of compliant performance, or the shorter history since inception, and build toward ten years. Those reporting requirements do not establish that five years suffice to validate rare-tail behavior, nor that a newer strategy lacks all evidential value. Verification, statistical validation, and economic implementation answer different questions. [5]

Section references:
[19] IMAS risk and performance guidance <http://www.imas.org.sg/uploads/media/2015/11/17/1011_IMAS_Guiding_Principles_for_Investment_Risk_Performance_Analysis_Functions_20151116_-_Final.pdf> Excerpt: "� Performance measurement, to accurately…"
[38] QFRS standards and audit <https://link.springer.com/article/10.1007/s10462-026-11664-w> Excerpt: "None of these papers achieved full compl…"
[5] 2020 GIPS Standards <https://www.gipsstandards.org/wp-content/uploads/2021/03/2020_gips_standards_firms.pdf> Excerpt: "5.C.1 Once the firm has met all the appl…"

### Use the framework for the intended decision

**Researchers can diagnose the bottleneck:** The common chain reveals whether apparent improvement comes from a better signal, different exposure, cost reduction, more leverage, favorable state coverage, or permissive execution. Ablations and locked comparisons can then isolate the mechanism without relying on one headline score.

**Portfolio managers can compare allocations:** Use the panel to select strategies that fit the capital scale, loss tolerance, liquidity needs, and existing portfolio. A high-Sharpe, low-capacity HFT strategy may be valuable as a small allocation; a lower-ratio, more scalable factor strategy may contribute more total economic profit. The relevant choice depends on marginal portfolio benefit and operational access.

**Risk and performance teams can reconcile:** Use common accounting and reference rules to explain differences between manager reports, research backtests, and realized results. Require additional review when low volatility coexists with large stress losses, slow recovery, financing concentration, or execution-model divergence.

**Academic comparisons can become cumulative:** Common schemas, trial registries, chronological splits, and executable controls make studies easier to compare without requiring identical models or markets. Negative and null results remain useful when they reveal a failure mechanism or distinguish adaptation from asset selection.

**Evidence boundaries define interpretation:** The cited results span different markets, periods, populations, capital bases, and cost scopes; index returns, modeled portfolios, firm-level statistics, and market-quality outcomes are distinct measurement objects. The 10%-volatility examples, participation ratio, cost thresholds, score envelopes, and scale differences are explicitly labeled calculations or estimates, while scoring weights, budgets, regime defaults, and hypothetical shocks are proposed conventions. Historical tests, proprietary inputs, selected universes, rounded source tables, and gross-versus-net differences limit how far individual findings extend.

**The closing judgment:** Develop a shared evaluation standard, not a universal investment winner: common economic accounting, layered references, separate return–risk–adaptability panels, executable validation, and transparent preference-dependent scoring. That architecture enables accurate comparison precisely because it standardizes the questions while preserving the mechanisms that make advanced quantitative strategies different.

## References

[1] <https://www.gipsstandards.org/wp-content/uploads/2021/03/alternative_investment_strategies_and_structures_gs_2012.pdf> GIPS alternative-investment guidance; GIPS peer-benchmark discussion; GIPS composite guidance; GIPS risk reporting
[2] <https://leadership.oregonstate.edu/sites/leadership.oregonstate.edu/files/2026-02/fac-4b-investment-performance-benchmarking.pdf> OSU benchmarking framework
[3] <https://rpc.cfainstitute.org/blogs/enterprising-investor/2017/benchmarking-multi-asset-portfolios-the-global-capital-stock> Global capital-stock benchmark
[4] <https://doi.org/10.48550/arXiv.2609.04917> Alpha-translation review
[5] <https://www.gipsstandards.org/wp-content/uploads/2021/03/2020_gips_standards_firms.pdf> 2020 GIPS Standards; 2020 GIPS reporting standards
[6] <https://www.cfauk.org/-/media/files/pdf/pdf/5-professionalism/3-research-and-position-papers/benchmarks-and-indices.pdf> CFA UK benchmark principles; Matched-leverage example
[7] <https://www.cmegroup.com/content/dam/cmegroup/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf> Systematic strategies across asset classes; Factor portfolio construction; Drawdown measurement conventions; Volatility-targeting trade-offs
[8] <https://www.morningstar.com/content/dam/marketing/shared/research/methodology/869053-FrameworkAnalyzingMultifactorFunds.pdf> Morningstar multi-factor framework; Morningstar factor comparison
[9] <https://doi.org/10.1007/s12599-022-00768-6> HFT definition and market study; Xetra evidence and contrasting studies
[10] <http://www.cftc.gov/sites/default/files/idc/groups/public/%40economicanalysis/documents/file/oce_riskandreturn0414.pdf> HFT risk and return; HFT participation and entry/exit data; HFT subtype results and accounting; HFT pooled and firm-level tables
[11] <https://www.econstor.eu/bitstream/10419/178766/1/1022453769.pdf> Regime-switching pairs trading; Regime-switching pairs result
[12] <https://www.nber.org/system/files/working_papers/w29011/w29011.pdf> Latency-arbitrage message study; HFT message-data methodology
[13] <https://doi.org/10.61093/fmir.10(3).1-27.2026> Return-aggregation distinction
[14] <https://etfdb.com/smart-beta-content-hub/multi-factor-strategies-guide-rafi-approach/> RAFI index comparison; RAFI regional results
[15] <https://doi.org/10.33893/fer.18.2.5286> Pure-factor comparison
[16] <https://doi.org/10.19030/iber.v13i3.8588> Sharpe and Omega comparison
[17] <https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/trade-strategy-execution> Implementation-shortfall guidance; Purpose-dependent execution benchmarks; Order-size and liquidity guidance
[18] <https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf> Synchronous performance-matrix rule; Probability of backtest overfitting
[19] <http://www.imas.org.sg/uploads/media/2015/11/17/1011_IMAS_Guiding_Principles_for_Investment_Risk_Performance_Analysis_Functions_20151116_-_Final.pdf> IMAS risk and performance guidance; IMAS governance guidance
[20] <https://app.olta.finance/research/11-downside-risk-framework> Downside-risk measurement
[21] <http://garpsalesforcepublic.s3.amazonaws.com/Content__c/a1Z1W000003mRmtUAE/a2r1W0000015Rx0QAE_Whitepaper.TailRisk.Oct19.pdf> Downside-risk targeting study
[22] <https://acfr.aut.ac.nz/__data/assets/pdf_file/0009/29727/581062-A-Kwan-HFTExecutionCosts.pdf> Limit-order execution costs; ASX latency and execution study
[23] <https://www.cis.upenn.edu/~mkearns/talks/ParisMicrostructure.pdf> Aggressive-HFT capacity exercise
[24] <https://ar5iv.labs.arxiv.org/html/1702.03838> Cross-impact and portfolio execution; Cross-impact evidence
[25] <https://www.sciencedirect.com/science/article/abs/pii/S0275531921002245> Market-regime classification study
[26] <https://arxiv.org/html/2510.14986v1> RegimeFolio classification; RegimeFolio results
[27] <https://www.aimspress.com/aimspress-data/dsfe/2025/4/PDF/DSFE-05-04-019.pdf> Turning-point and oracle comparison
[28] <https://doi.org/10.3390/fintech5030082> Cross-market regime tests
[29] <https://tfa-epfl.ch/research/papers/regime_based_strategy_final.pdf> Controlled regime-allocation holdout
[30] <https://arxiv.org/html/2604.18821v1?ref=aligrithm.com> Structured-strategy decay evidence; Common-volatility precedent
[31] <https://eprints.lancs.ac.uk/id/eprint/210994/3/BasicLohreMartinUtreraNolteNolte2023.pdf> Institutional factor-trading study; Cost optimization and factor integrity; Institutional impact estimate; VMQL portfolio results; VMQL capital-scale sensitivi…
[32] <https://doi.org/10.1103/physrevx.1.021006> Square-root impact mechanism
[33] <https://wp.lancs.ac.uk/finec2023/files/2023/01/FEC-2023-068-Victor-DeMiguel.pdf> Factor models net of impact
[34] <https://people.duke.edu/~charvey/Research/Published_Papers/P138_A_backtesting_protocol.pdf> Empirical-finance research protocol
[35] <https://doi.org/10.3390/electronics15061334> LightGBM validation
[36] <https://doi.org/10.3390/jrfm19010060> GT-Score comparison
[37] <https://open.uct.ac.za/bitstream/11427/31158/1/thesis_sci_2019_arbi_riaz.pdf> Scripted backtesting and auditability
[38] <https://link.springer.com/article/10.1007/s10462-026-11664-w> QFRS standards and audit
