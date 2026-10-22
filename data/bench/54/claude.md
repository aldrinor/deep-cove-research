# Mean-Variance, Black-Litterman and Deep Learning in Asset Allocation: Core Differences and a Principled Hybrid Framework

The three model families differ mainly in where they put prior structure and where they let the data decide. Mean-Variance (MV) trusts sample estimates and optimizes them hard. Black-Litterman (BL) trusts market equilibrium and lets views move it only in proportion to their stated confidence. Deep learning (DL) trusts flexible function approximation and, in its end-to-end form, skips explicit return and risk estimation entirely. Their strengths can be combined, and the best-documented hybrids already do so: ML-generated views fed into BL, shrinkage or ML covariance estimates fed into constrained optimizers, and differentiable optimization layers trained end-to-end. The result is better described as a disciplined *layered architecture* than as a single "general-purpose model." Its gains are incremental and fragile out of sample, and they have to be checked against naive benchmarks such as 1/N.

## TL;DR

- **Core differences:** MV measures risk as symmetric variance and estimates returns from noisy sample means, which makes the optimizer an "error maximizer." BL keeps the covariance-based risk measure but replaces sample means with CAPM-implied equilibrium returns, updated in a Bayesian way by views. DL/ML learns non-linear return signals, can optimize tail or drawdown objectives directly, and can output weights end-to-end. The price is opacity, heavy overfitting risk, and returns that are concentrated in hard-to-arbitrage, high-turnover segments.
- **Can they be combined? Yes, as a layered stack.** The stack is: an equilibrium prior (BL) → ML views with calibrated uncertainty (Ω) → shrinkage/factor/tail-aware risk → constrained, cost-aware robust optimizer → regime modulation → rigorous validation (purged CV, deflated Sharpe). Each layer has peer-reviewed support. The full integrated stack is a proposal, not an established result.
- **What to do:** Use structure (BL prior, risk budgets, constraints) to contain ML. Put ML where the signal-to-noise ratio is highest: covariance and volatility, text and alternative data, regime detection. Treat any reported DL outperformance as unproven until it survives transaction costs, large-cap-only universes, and multiple-testing corrections.

## Key Findings

1. **Estimation error, not model elegance, decides out-of-sample results.** DeMiguel, Garlappi and Uppal (2009, *Review of Financial Studies*) find that for sample-based MV and its extensions to beat 1/N, the estimation window needed is "around 3000 months for a portfolio with 25 assets and about 6000 months for a portfolio with 50 assets."\[1\] In practice, about 120 months are used.\[2\]
2. **Errors in means dominate.** Chopra and Ziemba (1993, *Journal of Portfolio Management*) show that at a risk tolerance of 50, "errors in means are about eleven times as important as errors in variances," and errors in variances are about twice as important as errors in covariances. The gap narrows as risk tolerance falls.\[3\] This is why BL replaces the means and minimum-variance or risk-parity methods drop them.
3. **ML improves return prediction, but only modestly in absolute terms.** In Gu, Kelly and Xiu (2020, *RFS*), neural networks reach monthly stock-level out-of-sample R² of 0.33% (NN1) to 0.40% (NN3); the authors report that "trees and neural networks unambiguously improve return prediction with monthly stock-level R²'s between 0.33% and 0.40%." Their value-weighted long-short decile spread earns an out-of-sample Sharpe of 1.35, versus 0.61 for a linear model. S&P 500 timing improves Sharpe from 0.51 to 0.77.
4. **ML profits shrink under economic restrictions.** Avramov, Cheng and Metzker (2023, *Management Science*) find that excluding microcaps, distressed stocks or high-volatility episodes "considerably attenuates profitability." Performance "further deteriorates in the presence of reasonable trading costs because of high turnover and extreme positions."\[4\]
5. **Hybrids that keep structure perform best in published tests.** Uysal, Li and Mulvey (2024, *Annals of Operations Research*) embed a risk-budgeting layer inside a neural network. Out of sample (2017–2021) it reaches a Sharpe of 1.16, versus 0.83 for a pure risk-budgeting model (1.24 with asset filtering).\[5\]\[6\] The authors note that the model-free network variant is a black box.\[7\]
6. **Industry practice is hybrid, not end-to-end.** Wealthfront's Classic Portfolio Investment Methodology White Paper states: "we use the Black-Litterman model to blend expected returns from the Capital Asset Pricing Model (CAPM)… with long-term expectations obtained from the Wealthfront Factor Model." Betterment says it "derives excess returns using the Black-Litterman model as a starting point." BlackRock Systematic and Man AHL use ML and LLMs mainly for signal extraction, inside conventional risk and portfolio construction.\[8\]\[9\]

## Part 1 — Core Differences Across the Three Families

### 1.1 Comparison table

| Dimension | Mean-Variance (Markowitz) | Black-Litterman | Deep learning / ML |
|---|---|---|---|
| **Risk definition** | Portfolio variance wᵀΣw. Symmetric; sufficient only under elliptical/normal returns or quadratic utility | Same Σ, plus estimation uncertainty in the mean (τΣ) and view uncertainty (Ω); posterior covariance Σ + [(τΣ)⁻¹ + PᵀΩ⁻¹P]⁻¹ | Implicit (learned through the loss) or explicit alternative measures: CVaR/ES, downside deviation, drawdown; time-varying via LSTM/attention/GARCH hybrids |
| **Risk estimation** | Sample covariance: noisy and ill-conditioned when N is large relative to T | Inherits Σ, usually sample or shrunk | Can learn conditional covariance or bypass it; risk enters through Sharpe/Sortino-type losses |
| **Return source** | Historical sample means | CAPM reverse optimization Π = δΣw_mkt, blended with views (P, Q, Ω) | Non-linear mapping from large feature sets (characteristics, prices, text); or none (end-to-end/RL) |
| **Return error handling** | None in the base model (Michaud's "error maximization") | Bayesian shrinkage toward equilibrium; confidence controls the tilt (Idzorek) | Regularization, ensembling, early stopping; uncertainty usually not calibrated |
| **Weight mechanics** | Quadratic program on the efficient frontier; corner solutions, high turnover | MV on posterior inputs; weights = scaled market portfolio + view portfolios (He & Litterman) | Two-stage predict-then-optimize, or a network that outputs weights (softmax/constraint layers), or an RL policy |
| **Constraints and costs** | Easy to add (QP); costs via penalties | Same as MV | Hard constraints require projection/implicit layers; costs must be in the reward/loss |
| **Interpretability** | Transparent but fragile | Highest: every tilt traces to a stated view | Low; post-hoc XAI only partial |
| **Main failure mode** | Estimation error, normality, instability | Garbage-in views; overconfident Ω; equilibrium assumption; τ ambiguity | Overfitting, non-stationarity, data snooping, turnover, hyperparameter and seed sensitivity |

### 1.2 Risk measurement

**Mean-Variance.** Variance treats upside and downside deviations alike. It is a complete description of risk only for elliptical return distributions. Fat tails, negative skewness, and volatility clustering are ignored. Correlations that rise in crises (shown by Ang and Bekaert, discussed below) break the static Σ.\[10\] The practical problem is estimation. With N assets, Σ has N(N+1)/2 parameters, and the sample matrix is ill-conditioned or even singular when N approaches T. Inverting it amplifies noise into extreme weights.

**Post-Markowitz refinements of risk:**
- **Shrinkage.** Ledoit and Wolf ("Honey, I Shrunk the Sample Covariance Matrix," *JPM* 2004) shrink the sample covariance toward a structured target such as a constant-correlation or single-factor matrix. The intensity is chosen to minimize expected estimation loss. The estimator is well-conditioned even when N > T.\[11\]\[12\] Later nonlinear shrinkage ("Markowitz meets Goldilocks," *RFS* 2017) shrinks eigenvalues individually.\[13\]
- **Robust and Bayesian approaches.** Robust MVO optimizes against worst-case means or covariances within an uncertainty set. Bayesian and Bayes-Stein estimators (Jorion 1986) shrink means toward a common value.\[14\]
- **Risk parity and HRP.** López de Prado's Hierarchical Risk Parity (*JPM* 2016) clusters assets by correlation distance and allocates by recursive inverse-variance bisection. It never inverts Σ. In his Monte Carlo experiments, the minimum-variance CLA portfolio "exhibit[s] the highest variance out-of-sample, and 72.47% greater variance than HRP's."\[15\]\[16\] Independent backtests are more mixed. A Copenhagen Business School thesis and a constrained-HRP study using real rather than simulated data found results that "stand in contrast" to the simulation evidence in some settings.\[17\]\[18\]
- **CVaR optimization.** Rockafellar and Uryasev (2000) showed that CVaR (Expected Shortfall) can be minimized as a linear program over return scenarios. It is coherent, focuses on the tail, and works with fat-tailed or non-parametric distributions. It needs many scenarios to estimate the tail reliably.

**Black-Litterman.** BL does not change the risk model. It keeps Σ and adds two kinds of uncertainty: τΣ for uncertainty in equilibrium means, and Ω for view uncertainty. The posterior covariance is slightly inflated, so estimation risk is acknowledged but stays Gaussian.\[19\] Extensions relax this. Meucci's "Beyond Black-Litterman" (entropy pooling) handles views on arbitrary distributions. Kocuk and Cornuéjols (*Omega*, 2020) combine BL with CVaR under a mixture-of-normals model and find "typically ... less risky portfolios than a purely market-based portfolio while producing similar returns on average."\[20\]

**Deep learning / ML.** DL models treat risk in three ways:
- **Implicitly**, through a loss. Zhang, Zohren and Roberts (2020) maximize the Sharpe ratio directly by gradient ascent, so volatility enters only as the denominator.\[21\]
- **Explicitly**, through alternative objectives: CVaR, downside deviation, drawdown penalties, or distributional RL.
- **Conditionally**, through time-varying volatility and covariance from recurrent or attention models, or LSTM-GARCH hybrids.

The advantage is that regime-dependent, asymmetric risk can be represented. The disadvantage is that the learned risk is only as good as the training sample. Tail events are rare, so a network trained on calm data has seen few tails to learn from.

**Bottom line on risk.** The difference is less "variance vs. something better" than "where does uncertainty live?" MV ignores estimation uncertainty. BL models it with Gaussian simplicity. ML can model rich conditional risk but rarely quantifies its own model uncertainty.

### 1.3 Return prediction

**Mean-Variance: historical means.** Sample means have standard errors on the order of σ/√T. With 20% volatility and 10 years of data, that is about ±6% per year, which is often larger than the risk premium being estimated. Michaud (1989) called MV an "error maximizer": it overweights assets whose estimated means are too high. Chopra and Ziemba quantify this. Errors in means are roughly 11× as damaging as variance errors and over 20× as damaging as covariance errors at a risk tolerance of 50.\[22\]

**Black-Litterman: equilibrium + Bayesian views.**
- Black and Litterman (1992, *Financial Analysts Journal*) reverse-optimize market-cap weights to get implied excess returns Π = δΣw_mkt. These are the returns that would make the market portfolio optimal.\[23\]\[24\]
- The posterior is E[R] = [(τΣ)⁻¹ + PᵀΩ⁻¹P]⁻¹[(τΣ)⁻¹Π + PᵀΩ⁻¹Q].\[19\]\[25\]
- He and Litterman (1999) show that the unconstrained optimal portfolio is the scaled market portfolio plus a weighted sum of view portfolios.\[26\]\[27\]
- Idzorek's method maps an intuitive 0–100% confidence onto Ω.\[28\] His guide notes that τ and Ω "are very difficult to specify." Litterman himself said there is no "universal answer" for Ω.\[28\]
- The subjectivity criticism is real, but it moves the problem rather than creating it. MV also uses subjective inputs: the choice of sample window is one. BL at least makes the subjectivity explicit and bounded.
- The deeper risks are overconfident Ω, and an equilibrium prior that assumes CAPM holds and that market weights are observable and optimal.\[29\] Neither assumption is clean for multi-asset or private-market universes.

**Deep learning / ML: high-dimensional non-linear prediction.**
- Gu, Kelly and Xiu (2020) compare 11 methods on "nearly 30,000 individual stocks over 60 years from 1957 to 2016" with 920 covariates (94 characteristics × 9 interactions + 74 industry dummies). Trees and neural networks "unambiguously improve return prediction." Shallow networks (NN3) perform best, and gains come mostly from non-linear interactions among a small set of robust predictors (momentum, liquidity, volatility).\[30\]
- The economic gains are concentrated where arbitrage is hard. The equal-weighted spread Sharpe of 2.45 is driven by micro-caps, which Avramov, Cheng and Metzker show do not survive realistic restrictions.\[4\]\[30\]
- Kelly, Malamud and Zhou ("The Virtue of Complexity in Return Prediction," *Journal of Finance* 2024) prove that heavily over-parameterized models with appropriate shrinkage can dominate simple ones. They also show that out-of-sample R² is "a poor measure of its economic value."\[31\]\[32\] This is contested: Nagel (2025, NBER WP 34104), Berk (2023) and Buncic (2025) argue that the apparent virtue reflects mechanical features of the setup.\[33\]\[34\] Treat it as an open debate.
- **Bypassing prediction.** Jiang, Xu and Liang (2017) train an RL policy (EIIE topology) that maps price histories directly to weights. Their reported crypto backtests are large: the earlier Jiang and Liang paper claims "10-fold returns in 1.8 month's periods."\[35\]\[36\] A later independent replication found the networks "exhibited average performance, failing to demonstrate the superiority" when moved to stock markets.\[37\] Zhang, Zohren and Roberts (2020, *Journal of Financial Data Science*) use a single 64-unit LSTM on four index ETFs. It outputs softmax weights trained to maximize Sharpe, which "circumvents the requirements for forecasting expected returns."\[38\]\[39\]

**Signal-to-noise.** Monthly predictable variance in individual stock returns is well under 1%.\[30\] Any model with many parameters fits noise unless it is heavily regularized. This, and not interpretability, is the binding constraint on DL in allocation.

### 1.4 Asset allocation mechanics

- **MV:** a quadratic program. Without constraints, it produces large long-short positions. With long-only constraints, it gives corner solutions. Black and Litterman (1992) reported that a constrained optimizer using historical means kept positive weights in only 2 of 14 assets.\[25\] Remedies are weight bounds (Jagannathan and Ma show constraints act like covariance shrinkage), turnover penalties, L1/L2 norm penalties, and resampling (Michaud's resampled frontier, which averages weights over bootstrapped inputs).
- **BL:** the same optimizer, fed with posterior inputs. Weights start at the market portfolio and move only in proportion to view strength and confidence. This yields diversified, intuitive, low-turnover allocations.\[24\] That explains why it dominates institutional strategic allocation and robo-advice.
- **DL/ML:** three patterns.
  1. *Predict-then-optimize:* ML forecasts feed an MVO or risk model. This is modular and auditable, but the forecaster is trained on MSE, which ignores how errors propagate through Σ⁻¹.
  2. *End-to-end weight networks:* softmax gives long-only weights; constraint or implicit layers enforce budgets. Costs and turnover must be in the loss.
  3. *RL policies:* multi-period, path-dependent, and able to internalize transaction costs, but sample-inefficient and unstable across random seeds.

**Transaction costs and turnover are where DL most often fails in practice.** Avramov et al. attribute much of the ML deterioration to "high turnover and extreme positions."\[4\] The Deep Declarative Risk Budgeting paper (2025) documents that early end-to-end frameworks are "highly sensitive to neural network initialization." This means two runs of the same model can sit on opposite sides of the risk-parity benchmark.\[40\]\[41\]

### 1.5 Limitations beyond the ones in the question

| Limitation | MV | BL | DL/ML |
|---|---|---|---|
| Normality / symmetric risk | Core assumption | Core assumption (Gaussian prior and likelihood) | Not required, but tails are under-sampled |
| Subjectivity | Hidden (window, estimator choice) | Explicit (views, τ, Ω) | Hidden (architecture, features, hyperparameters, seeds) |
| Interpretability | High | Highest | Low |
| Estimation error | Severe | Mitigated for means; Σ unchanged | Severe; parameters ≫ effective sample size |
| Non-stationarity / regimes | Static | Static unless views are dynamic | Can adapt, but may learn the last regime |
| Data snooping / multiple testing | Moderate | Moderate (view backtests) | Severe: thousands of configurations |
| Small samples | ~120 months typical | Same | Daily data inflates N but not independent regimes |

### 1.6 Empirical evidence across market conditions

- **1/N is the benchmark to beat.** DeMiguel et al. found that across 14 models and seven datasets, none consistently beat 1/N on Sharpe ratio, certainty-equivalent return, or turnover.\[42\]
- **Crises.** Ang and Bekaert (2002, *RFS*) document "a 'bear' regime with higher correlations, higher volatilities, and lower conditional means."\[10\] A static Σ understates crisis risk exactly when it matters. In Uysal et al., the end-to-end risk-budgeting portfolio "tracks the nominal risk-parity under normal market conditions and presents advantages under abnormal events such as bond crash and Covid-crash."\[43\] That is one encouraging but single-study, single-universe (ETF) result.
- **DL fragility.** Reported DL gains are typically on short tests, small universes (a handful of ETFs or 20 surviving S&P 500 stocks in Costa and Iyengar's study), or crypto.\[44\] Larger, cost-aware tests (Avramov et al.) show substantial attenuation.\[45\] Evidence is mixed rather than negative: Azevedo, Hoegner and Velikov ("The Expected Returns on Machine-Learning Strategies," SSRN 4702406) find that "despite a cumulative performance reduction of 57% due to these factors [costs, post-publication decay, high-liquidity era], sophisticated machine learning strategies remain profitable, particularly those employing LSTM models," with net out-of-sample monthly returns of "up to 1.42%" and an LSTM six-factor net alpha of "1.20% (t-stat of 3.46)."

## Part 2 — Combining Strengths: Evidence on Hybrid Frameworks

### 2.1 ML-generated views in Black-Litterman

This is the most natural hybrid. It keeps BL's prior and interpretability and uses ML only to supply Q and, ideally, Ω.
- **Industry precedent.** Wealthfront's Classic Portfolio Investment Methodology White Paper states: "we use the Black-Litterman model to blend expected returns from the Capital Asset Pricing Model (CAPM)… with long-term expectations obtained from the Wealthfront Factor Model," and its covariance matrix uses "historical data, combined with factor analysis using the Wealthfront Factor Model." A quantitative model replacing subjective views is the production version of this hybrid. Betterment uses BL as the starting point for excess returns in its asset location methodology.\[46\]
- **Academic work.** There are many papers using ML classifiers, LSTMs, Transformer-GANs (arXiv 2404.02029), decomposition-plus-LSTM forecasters (arXiv 2505.01781), and LLMs (arXiv 2504.14345, which tunes τ on a validation period) as view generators.\[19\]\[47\]\[48\]\[49\] Most report gains over MV or market weights. Most are also small-sample preprints without multiple-testing control. Zhao (arXiv 2311.04475) is candid that "further improvement and robustness checking should be performed."\[50\]
- **Regime views.** Shu and Mulvey (arXiv 2410.14841) use a sparse jump model to label six factor indices as bull or bear, then feed these labels as BL views.\[26\] Over 2007–2024 with 5 bp costs, the information ratio versus the market rises "from just 0.05 for the EW benchmark to approximately 0.4." Sharpe rises from 0.54 (EW) to 0.57–0.65 depending on tracking-error target. Absolute maximum drawdown barely changes (−52.9% → −50.5% to −52.5%), and turnover is high (237–628%).\[26\]
- **Calibrating Ω from model uncertainty is the key open piece.** Options include ensemble dispersion, Bayesian neural nets or MC dropout, conformal prediction intervals, and predictive entropy. A 2026 proposal (arXiv 2607.20533) maps neural-predicate entropy to Ω, but it is "explicitly theoretical" with no empirical validation.\[51\]\[52\] In principle, Ω should equal the out-of-sample forecast error variance of the ML model, estimated walk-forward. Doing so automatically shrinks weak ML views back toward equilibrium. This is a recommendation, not a published standard.

### 2.2 ML and structured covariance estimation feeding classical optimizers

Covariance is far more predictable than means, so this is where ML has the best signal-to-noise. Evidence-backed components:
- Ledoit-Wolf linear and nonlinear shrinkage
- Factor risk models
- Random-matrix-theory denoising (López de Prado, *Machine Learning for Asset Managers*)
- HRP clustering

Newer work learns covariance cleaning end-to-end: a 2026 *Journal of Finance and Data Science* paper reports rotation-invariant neural covariance cleaning for variance minimization across hundreds to thousands of stocks.\[44\] A practitioner preprint (arXiv 2507.07107) pairs a Transformer return model with Markowitz-Ledoit-Wolf and reports a deflated Sharpe ratio of 0.978 after about 50 configurations.\[53\] That is a good example of reporting discipline, though still a single-market (A-share) study.

### 2.3 Robust and Bayesian optimization with ML forecasts as uncertain inputs

- **Robust MVO** penalizes worst-case mean error within an ellipsoid sized by forecast uncertainty. It pairs naturally with ML ensembles.
- **Resampled efficient frontiers** (Michaud) average weights across bootstrapped input draws.
- **Distributionally robust end-to-end learning** (Costa and Iyengar, *Quantitative Finance* 2023) puts a minimax portfolio layer inside the network. The ambiguity set is centered on the predicted distribution, and both risk tolerance and the degree of robustness are learned from data. The authors' motivation is that "existing end-to-end systems are not able to quantify and correct for the impact of model risk on the decision layer."\[54\]\[55\]

### 2.4 End-to-end / decision-focused learning with differentiable optimization layers

- **Butler and Kwon** ("Integrating prediction in mean-variance portfolio optimization," *Quantitative Finance* 23(3), 2023) train regression forecasters on the MVO decision loss rather than MSE. They give closed forms for unconstrained and equality-constrained cases and use differentiable QP layers for inequality constraints. On synthetic and global futures data, the integrated approach beats the decoupled one.\[56\]\[57\]\[58\]
- **Why it helps:** Lee et al. (arXiv 2409.09684) show the decision-focused gradient "tilts MSE-based prediction errors by the inverse covariance matrix Σ⁻¹."\[59\] The forecaster learns to be accurate where errors are most costly for the portfolio. This puts Chopra-Ziemba's insight into the training objective.
- **Uysal, Li and Mulvey (2024):** a risk-budgeting implicit layer. Sharpe 1.16 vs 0.83 for pure risk budgeting, and vs 0.79 for nominal risk parity in the preprint.\[60\]
- **Caveat:** end-to-end systems inherit DL's seed sensitivity. Deep Declarative Risk Budgeting (arXiv 2504.19980) is a direct response to that instability.\[41\]

### 2.5 Regime-switching and ensembles

- **Ang and Bekaert (2002):** international diversification "is still valuable with regime changes." Ignoring regimes costs little for all-equity portfolios, but the cost "increase[s] when a conditionally risk-free asset can be held."\[61\] This is a theoretical result that assumes observable regimes.\[10\]
- **Nystrup, Madsen and Lindström (*Quantitative Finance* 2018):** an HMM with model predictive control on MSCI World, 1998–2015, with 10 bp costs and a one-day delay. Results: Sharpe 0.63 vs 0.30 buy-and-hold and 0.32 for a static 69/31 portfolio; maximum drawdown 25% vs 57% (buy-and-hold) and 44% (static). Across six indices, volatility and drawdown were lower in all cases. Sharpe was higher in five of six; FTSE was the exception, at 0.36 vs 0.54.\[62\]
- **Caveats on regime evidence.** Nystrup's own earlier stock/bond study (*JPM* 2015) attributes the outperformance "mainly" to 2008. Its strengths include "break-even transaction cost ... more than 200 basis points per one-way transaction."\[63\] Much of the regime evidence comes from two crashes (2000–02, 2008) and stock-vs-cash switching.
- **Jump models vs HMMs.** Shu, Yu and Mulvey (*Journal of Asset Management* 2024) report that statistical jump models beat HMM-guided and buy-and-hold strategies on volatility, drawdown and Sharpe for the S&P 500, DAX and Nikkei over 1990–2023. With 10 bp one-way costs, the jump model raised CAGR over buy-and-hold "by 1%, 1.8% and 3.9%" for the S&P 500, DAX and Nikkei 225 respectively, lifted Sharpe from 0.48→0.68, 0.30→0.44 and 0.12→0.31, and cut S&P 500 maximum drawdown from −55.2% to −26.6%. All these jump-model papers come from one research group with validation-tuned hyperparameters.
- **Use regimes as a modulator, not an oracle.** The evidence supports using regimes to scale risk and to reweight model ensembles: shift toward equilibrium/minimum-variance in high-volatility states, and allow more ML tilt in calm states. It does not support regimes as a return predictor.

### 2.6 Explainability tools

SHAP, LIME, integrated gradients and attention maps can attribute weights or forecasts to features. Post-hoc explanation of DRL portfolio agents is an active area (arXiv 2407.14486).\[64\] They help but are not sufficient:
- Attributions are local, unstable under correlated features (common in finance), and explain the model, not the market.
- Attention weights are not faithful explanations.
- The stronger route is *structural interpretability*: embedding the network inside an interpretable decision layer. Examples are BL views, risk budgets, or a constrained QP, where every final weight decomposes into prior + view tilts + constraint effects.
- Man AHL's Anthony Ledford frames the practical goal as "a key diagnostic for interpreting what a machine learning model will do next," rather than full transparency.\[65\]

### 2.7 HRP and ML-inspired interpretable allocators

HRP uses unsupervised learning (hierarchical clustering) to structure the covariance. It needs no inversion and no return forecasts, and its weights trace to a dendrogram.\[15\] It is a sensible middle ground and a stronger default than MV for large, noisy universes. Its simulation-based superiority should not be read as guaranteed in live data. Hybrid variants combine HRP with RL (Millea and Edalat 2022; arXiv 2508.11856).\[66\]

### 2.8 Industry practice (public information only)

- **Robo-advisors:** BL/MV strategic allocation with quantitative views (Wealthfront's factor model; Betterment's BL-based expected returns), plus rules-based rebalancing and tax optimization.\[23\]\[46\] No public evidence of DL directly setting client weights.
- **BlackRock Systematic:** says AI and ML have "played a pivotal role in our investment process for nearly two decades." LLMs are "fine-tuned to perform specific investment tasks, for example forecasting the market reaction following corporate earnings calls."\[67\] Its macro LLM platforms extract sentiment from broker research.\[68\]\[69\] BlackRock reports that "the forecasting accuracy of OpenAI's GPT models has decreased with newer versions of GPT-4" for its task.\[67\] Co-CIO Jeff Shen flags point-in-time leakage: off-the-shelf LLMs create "very strong peek-ahead bias." He calls ML for portfolio construction "the less obvious development."\[8\] This is ML for signals, inside a conventional risk and construction process.
- **Man AHL:** has traded ML components in client multi-strategy programs since early 2014. It emphasizes Bayesian ML for noisy data and says ML "ha[s] the most to offer towards the faster end of the spectrum." Faster signals show more non-linearity but are "hard to capture as alpha in the client-scale funds."\[70\]\[71\]
- **Two Sigma and others:** little verifiable public detail on how ML and classical construction are combined. Claims in secondary sources should be treated as unverified.
- **Aladdin:** primarily a risk, analytics and operations platform built around factor risk models. Public material does not support claims that it runs DL allocation.

## Part 3 — A Principled Hybrid Framework (Proposal)

The following is a synthesis. Each layer is backed by evidence, but the integrated system has not been validated as a whole in the literature.

| Layer | Function | Recommended components | Evidence status |
|---|---|---|---|
| (a) Prior | Anchor weights; prevent error maximization | BL reverse-optimized equilibrium (or risk-parity/HRP prior where market weights are ill-defined) | Established |
| (b) Views + uncertainty | Supply Q and Ω | Gradient boosting / shallow NN / LLM text signals; Ω = walk-forward forecast error variance, ensemble dispersion, or conformal width | Views: well studied but fragile; calibrated Ω: proposed |
| (c) Risk | Conditional, tail-aware Σ | Ledoit-Wolf / nonlinear shrinkage, factor models, RMT denoising; CVaR/drawdown constraints; ML volatility forecasts | Established (shrinkage, CVaR); ML vol: promising |
| (d) Optimizer | Turn inputs into implementable weights | Constrained, robust or distributionally robust QP/conic program with turnover and cost penalties; optionally trained end-to-end (Butler-Kwon, Costa-Iyengar, Uysal et al.) | Established (robust QP); end-to-end: peer-reviewed but small-universe |
| (e) Regime modulation | Adapt to non-stationarity | HMM / jump model scaling τ, view confidence, and risk budget; ensemble weighting across (a)–(d) | Moderate; concentrated in crash periods |
| (f) Governance | Guard against overfitting; explain | Walk-forward, combinatorial purged CV with embargo, deflated Sharpe, probability of backtest overfitting; weight attribution prior vs view vs constraint; SHAP on view models; 1/N and market benchmarks | Established methodology |

**Design principles:**
1. **ML proposes; structure disposes.** Never let a network output unconstrained weights. Route its information through Q/Ω or a risk budget, so that weak signals revert to the prior automatically.
2. **Put model capacity where predictability lives.** Use it for covariance, volatility, text and regime detection before cross-sectional means.
3. **Optimize the decision, not the forecast.** Where feasible, train on decision loss (decision-focused learning). Keep a two-stage fallback for auditability.
4. **Price everything.** Include costs, turnover, capacity, and large-cap-only robustness checks in training and evaluation.
5. **Deflate everything.** Bailey and López de Prado's deflated Sharpe ratio corrects for "selection bias under multiple testing and non-Normally distributed returns."\[72\] Report the number of configurations tried.

**Why "general-purpose" is hard:**
- Non-stationarity: the data-generating process shifts, and correlations jump in crises.
- Low signal-to-noise: monthly R² is below 1%.
- Adaptive markets and reflexivity: published or crowded signals decay.
- Limited independent history: there are few crises to learn from.
- Objective heterogeneity: liabilities, taxes and constraints differ across investors.

A framework can be general in *architecture*. Its calibration must remain local to the universe, horizon and investor.

## Recommendations

- **For strategic or multi-asset allocation:** use BL with quantitative views and shrinkage covariance as the default. Add ML views only with walk-forward-calibrated Ω, and benchmark against 1/N and market weights.
- **For large equity universes:** use ML (shallow NNs, boosted trees) for cross-sectional signals. Feed them into a factor-risk, cost-aware optimizer with turnover limits. Test excluding microcaps.
- **For risk-based mandates:** use HRP or risk budgeting, optionally with an end-to-end learned budget (Uysal et al.). Prefer model-based over model-free networks.
- **Treat pure end-to-end DL and RL as research,** not production, until they show robustness across seeds, universes and cost regimes.
- **Use regime signals to modulate risk and confidence,** not as a standalone alpha source.

## Caveats

- Many hybrid results cited here come from arXiv preprints, small universes (ETFs, ≤20 stocks), or single research groups. Several BL+DL papers lack transaction costs and multiple-testing control.
- The HRP superiority evidence is simulation-based. Live-data replications are mixed.\[18\]
- The "virtue of complexity" result is contested in ongoing work.\[33\]
- Regime-switching gains are concentrated in 2000–02 and 2008.\[63\]
- Industry descriptions come from firms' own marketing or interviews and cannot be independently verified. They describe where ML is used, not its realized performance contribution.
- Foundation models and LLMs for allocation (2023–2026) are early-stage. Look-ahead bias from pre-training data is a first-order threat to any backtest that uses them.\[73\]

## 資料來源

1. [Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901)
2. [1/N by Victor DeMiguel, Lorenzo Garlappi, Raman Uppal :: SSRN](https://www.ssrn.com/abstract=911512.)
3. [Selected Works of William T. Ziemba: A Memorial Volume 9811285527, 9789811285523 - DOKUMEN.PUB](https://dokumen.pub/selected-works-of-william-t-ziemba-a-memorial-volume-9811285527-9789811285523.html)
4. [Machine Learning vs. Economic Restrictions: Evidence from Stock Return Predictability](https://ideas.repec.org/a/inm/ormnsc/v69y2023i5p2587-2619.html)
5. [Xiaoyue Li - Google Scholar](https://scholar.google.com/citations?user=V8vOoTkAAAAJ&hl=vi)
6. [End-to-end risk budgeting portfolio optimization with neural networks - New Jersey Research Community](https://www.researchwithnj.com/en/publications/end-to-end-risk-budgeting-portfolio-optimization-with-neural-netw/)
7. [End-to-end risk budgeting portfolio optimization with neural networks](https://www.researchgate.net/publication/373427239_End-to-end_risk_budgeting_portfolio_optimization_with_neural_networks)
8. [How BlackRock Systematic Uses AI and Alternative Data](https://www.wealthmanagement.com/investing-strategies/ai-large-language-models-and-active-management-inside-blackrock-s-approach-to-systematic-investing)
9. [Man AHL: The Systematic CTA Pioneer Blending Trend-Following with Machine Learning](https://brokersdb.com/learn/man-ahl-systematic-cta-trend-following)
10. <https://business.columbia.edu/sites/default/files-efs/pubfiles/1971/1137.pdf>
11. [Honey, I Shrunk the Sample Covariance Matrix · Reasonable Deviations](https://reasonabledeviations.com/notes/papers/ledoit_wolf_covariance/)
12. [Michael Wolf (statistician)](<https://en.wikipedia.org/wiki/Michael_Wolf_(statistician)>)
13. [Olivier Ledoit - Google Scholar](https://scholar.google.com/citations?user=g8DNHjIAAAAJ&hl=en)
14. [Covariance Matrix Analysis for Optimal Portfolio Selection](https://arxiv.org/pdf/2407.08748)
15. [Building Diversified Portfolios that Outperform Out-of-Sample by Marcos Lopez de Prado :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678)
16. [BUILDING DIVERSIFIED PORTFOLIOS THAT OUTPERFORM OUT-OF-SAMPLE](https://smallake.kr/wp-content/uploads/2020/04/SSRN-id2708678.pdf)
17. [Copenhagen Business School Master Thesis Finance and Investments](https://research.cbs.dk/files/76452070/1332322_Master_Thesis_Hierarchical_Risk_Parity.pdf)
18. [A Constrained Hierarchical Risk Parity Algorithm with Cluster-based Capital](https://www.fmx.nfkatzke.com/Projects/HRP.pdf)
19. [Enhancing Portfolio Optimization with Transformer-GAN Integration: A Novel Approach in the Black-Litterman Framework](https://arxiv.org/pdf/2404.02029)
20. [Incorporating Black-Litterman views in portfolio construction when stock returns are a mixture of normals - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0305048317312604)
21. [Deep Learning for Portfolio Optimization](https://arxiv.org/html/2005.13665v3)
22. [The Effect of Errors in Means, Variances, and Covariances on Optimal Portfolio Choice](https://www.researchgate.net/publication/247905549_The_Effect_of_Errors_in_Means_Variances_and_Covariances_on_Optimal_Portfolio_Choice)
23. [Wealthfront Classic Portfolio Investment Methodology White Paper](https://research.wealthfront.com/whitepapers/investment-methodology/)
24. [Black & Litterman (1992): Global Portfolio Optimization](https://foxholm.com/q/research/black-litterman-model/)
25. [Black-Litterman Model: Why Combining Market Equilibrium with Investor Views Fixes Portfolio Optimization](https://www.tradicted.com/research/black-portfolio-1992/)
26. [Dynamic Factor Allocation Leveraging Regime-Switching Signals](https://arxiv.org/pdf/2410.14841)
27. [(PDF) Asset Allocation with Black-Litterman in a case study of Robo Advisor Betterment](https://www.researchgate.net/publication/326878665_Asset_Allocation_with_Black-Litterman_in_a_case_study_of_Robo_Advisor_Betterment)
28. [A STEP-BY-STEP GUIDE TO THE BLACK-LITTERMAN MODEL](https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf)
29. [The Black-Litterman Model: Blending Views with Market Equilibrium](https://quantdecoded.com/en/the-black-litterman-model-blending-views-with-market-equilibrium)
30. [Empirical Asset Pricing via Machine Learning](https://www.research-center.mirova.com/en/research-library/Empirical-Asset-Pricing-via-Machine-Learning)
31. [The Virtue of Complexity in Return Prediction - KELLY - 2024 - The Journal of Finance - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13298)
32. [The Virtue of Complexity in Return Prediction](https://economics.yale.edu/research/virtue-complexity-return-prediction)
33. [(Mis)Understanding Benign Overfitting in Equity Return Prediction](https://arxiv.org/pdf/2608.23761)
34. [The Virtue of Sparsity in Complexity](https://arxiv.org/pdf/2604.17166)
35. [arXiv:1706.10059v2 \[q-fin.CP\] 16 Jul 2017 Deep Portfolio Management](https://arxiv.org/pdf/1706.10059)
36. [Cryptocurrency Portfolio Management with Deep Reinforcement Learning](https://arxiv.org/pdf/1612.01277)
37. [A Deep Reinforcement Learning Framework For Financial Portfolio Management](https://www.alphaxiv.org/abs/2409.08426)
38. [Deep Learning for Portfolio Optimisation by Zihao Zhang, Stefan Zohren, Stephen Roberts :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3613600)
39. [EconPapers: Deep Learning for Portfolio Optimization](https://econpapers.repec.org/RePEc:arx:papers:2005.13665)
40. [Deep Declarative Risk Budgeting Portfolios](https://arxiv.org/pdf/2504.19980)
41. [Deep Declarative Risk Budgeting Portfolios](https://www.alphaxiv.org/abs/2504.19980)
42. [How Inefficient is the 1/N Asset-Allocation Strategy? by Victor DeMiguel, Lorenzo Garlappi, Raman Uppal :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=785164)
43. [End-to-End Risk Budgeting Portfolio Optimization with Neural Networks](https://arxiv.org/pdf/2107.04636)
44. [End-to-end large portfolio optimization for variance minimization with neural networks through covariance cleaning - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2405918826000048)
45. [Machine Learning Versus Economic Restrictions: Evidence from Stock Return Predictability](https://www.researchgate.net/publication/336054751_Machine_Learning_Versus_Economic_Restrictions_Evidence_from_Stock_Return_Predictability)
46. [Betterment's asset location methodology](https://www.betterment.com/resources/asset-location-methodology)
47. [(PDF) Black-Litterman Portfolios with Machine Learning derived Views](https://www.researchgate.net/publication/326489143_Black-Litterman_Portfolios_with_Machine_Learning_derived_Views)
48. [Enhancing Black-Litterman Portfolio via Hybrid Forecasting Model Combining Multivariate Decomposition and Noise Reduction](https://arxiv.org/pdf/2505.01781)
49. [LLM-Enhanced Black-Litterman Portfolio Optimization](https://arxiv.org/html/2504.14345v2)
50. [\[2311.04475\] Portfolio Construction using Black-Litterman Model and Factors](https://arxiv.org/abs/2311.04475)
51. [Grounding Investor Views: Neural Predicates in the Black-Litterman Model](https://arxiv.org/html/2607.20533v1)
52. [Grounding Investor Views: Neural Predicates in the Black-Litterman Model · Pith Review](https://pith.science/paper/2607.20533)
53. [Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction](https://arxiv.org/pdf/2507.07107)
54. [Distributionally Robust End-to-End Portfolio Construction](https://arxiv.org/pdf/2206.05134)
55. [Giorgio Costa - Google Scholar](https://scholar.google.com/citations?user=Os7NTjMAAAAJ&hl=ja)
56. [Integrating prediction in mean-variance portfolio optimization](https://arxiv.org/pdf/2102.09287)
57. [Decision-Focused Learning for Mean–Variance Portfolio Optimization via KKT-Based Reformulation](https://arxiv.org/html/2609.21427)
58. [EconPapers: Integrating prediction in mean-variance portfolio optimization](https://econpapers.repec.org/article/tafquantf/v_3a23_3ay_3a2023_3ai_3a3_3ap_3a429-452.htm)
59. [Return Prediction for Mean-Variance Portfolio Selection: How Decision-Focused Learning Shapes Forecasting Models](https://arxiv.org/html/2409.09684v4)
60. [\[PDF\] End-to-End Risk Budgeting Portfolio Optimization with Neural Networks](https://www.semanticscholar.org/paper/End-to-End-Risk-Budgeting-Portfolio-Optimization-Uysal-Li/40f168b66d9f2c36ed3af7c13cdd8cd1aef2e8c0)
61. [EconPapers: International Asset Allocation With Regime Shifts](https://econpapers.repec.org/RePEc:oup:rfinst:v:15:y:2002:i:4:p:1137-1187)
62. <https://backend.orbit.dtu.dk/ws/files/139272081/Dynamic_Portfolio_Optimization_Across_Hidden_Market_Regimes_ACCEPTED.pdf>
63. <https://backend.orbit.dtu.dk/ws/files/152802375/phd465_Nystrup_P.pdf>
64. [Explainable Post hoc Portfolio Management Financial Policy of a Deep Reinforcement Learning agent](https://arxiv.org/pdf/2407.14486)
65. [Financial applications of Machine Learning at Man AHL](https://bm.hkust.edu.hk/events/2018/05/financial-applications-machine-learning-man-ahl)
66. [Optimal Portfolio Construction -- A Reinforcement Learning Embedded Bayesian Hierarchical Risk Parity (RL-BHRP) Approach](https://arxiv.org/pdf/2508.11856)
67. [How AI is Transforming Investing](https://www.blackrock.com/institutions/en-apac/insights/thought-leadership/ai-investing)
68. [The macro decoder](https://www.blackrock.com/institutions/en-global/institutional-insights/thought-leadership/investment-actions/macro-decoder)
69. [Decoding market trends with LLMs](https://www.blackrock.com/za/professionals/themes/systematic-investing/macro-decoder)
70. [An Introduction to Machine Learning](https://www.man.com/insights/intro-machine-learning)
71. [The Rise of Machine Learning at Man AHL](https://www.man.com/insights/the-rise-of-machine-learning)
72. [The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality by David H. Bailey, Marcos Lopez de Prado :: SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551)
73. [inside blackrock approach systematic investing 200304879](https://finance.yahoo.com/news/inside-blackrock-approach-systematic-investing-200304879.html)