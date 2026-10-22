# Mean–Variance, Black–Litterman and Deep Learning: Their Differences and How to Combine Them

**The models solve different problems.** Mean–Variance Optimization converts expected returns and covariances into portfolio weights; Black–Litterman improves the return inputs by combining an equilibrium baseline with confidence-weighted views; deep learning can estimate nonlinear return signals, risk distributions or allocation policies. Consequently, they are often complementary layers rather than mutually exclusive alternatives. Their respective foundations are explained in the Mean–Variance literature [1], Idzorek’s Black–Litterman guide [2] and the systematic survey of financial deep learning [3].

**A hybrid framework is feasible.** A well-designed combination can use deep learning for information extraction, Black–Litterman for uncertainty-aware return blending, and a constrained optimizer for diversification, downside protection and trading costs. The strongest practical case is for a modular system whose components earn their place through out-of-sample investment results—not for a universally superior algorithm.

| Approach | Risk measurement | Return prediction | Asset allocation | Strengths | Limitations |
|---|---|---|---|---|---|
| Mean–Variance | Variance and covariance | Consumes estimated expected returns | Quadratic optimization | Transparent trade-offs and constraints | Input sensitivity; incomplete tail representation |
| Black–Litterman | Covariance plus uncertainty about mean returns | Equilibrium prior blended with views | Confidence-weighted portfolio tilts | Stabilizes forecasts and expresses convictions | Benchmark dependence; view and confidence errors |
| Deep learning | Learned volatility, densities, quantiles or reward-based risk | Nonlinear functions of financial features | Forecast-fed optimizer or direct policy | Flexible representations and adaptation | Overfitting, distribution shift and opacity |
| Proposed hybrid | Conditional covariance, tail risk and forecast uncertainty | Learned signals moderated by priors | Constrained, cost-aware optimization | Combines flexibility with explicit controls | More calibration and operational complexity |

**Four questions organize the comparison.** The report first separates risk measurement, forecasting and allocation, then examines each model’s mechanics, compares evidence across market conditions, and evaluates a concrete hybrid design. Its scope is global financial markets, with evidence covered through **2026-09-13**; individual studies retain their own countries, asset universes and evaluation periods.

Section references:
[1] Outliers and return estimation <https://doi.org/10.3390/ijfs10030064> Excerpt: "Mean square error (MSE): According to Table 2 ( and Table 3 ( the average values of MSE for each of the machine learning models are reported as follows: 2.9000 for CNN-BiLSTM, 2.5794 for BiLSTM, 2.5570 for LSTM, and 1.8081 for R-CNN-BiLSTM. The biggest MAE is 9.3412, which is found on stock MTC gen…"
[2] Black–Litterman construction <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Excerpt: "implied confidence levels of View 1, View 2, and View 3 in the example are 32.94%, 43.06%, and 33.02%, respectively. Only using the scaled variance of each individual view portfolio to determine the diagonal elements of Ω ignores the stated confidence levels of 25%, 50%, and 65%. Table 7 Implied Co…"
[3] Deep-learning application roles <https://link.springer.com/article/10.1007/s10462-022-10226-0> Excerpt: "The search query construct provided us with the starting point for answering research questions (1) and (2). Then, we evaluated the relevance to the research objective of the 185 publications and considered how each study answered question (3). We objectively reviewed all query responses without fo…"

## 1. The central distinction: forecasting, risk measurement and allocation

### Three layers, not three interchangeable algorithms

**Mean–Variance is an allocation rule.** It answers: given expected returns, covariances and investment restrictions, which weights offer the preferred risk–return trade-off? It does not inherently determine whether expected returns should come from historical averages, economic factors, analyst judgments or neural networks. Marakbi’s treatment explicitly separates parameter estimation from portfolio selection, making this distinction important for interpreting model comparisons. [4]

**Black–Litterman is primarily information blending.** Its distinctive contribution is a structured way to combine a benchmark-implied return prior with additional beliefs and their uncertainty. The resulting expected returns commonly enter a Mean–Variance optimizer, although alternative allocation objectives can be used. Thus, “Black–Litterman versus Mean–Variance” frequently means comparing different return-estimation procedures inside closely related optimization machinery. [2]

**Deep learning spans several layers.** A neural network might forecast returns, estimate conditional volatility, produce a probability distribution, generate scenarios or directly choose exposures. These applications solve different problems: better volatility forecasts do not establish better return forecasts, while profitable trading decisions do not automatically establish calibrated tail-risk estimates. The financial deep-learning survey distinguishes portfolio management, prediction, trading and risk management as separate application areas. [3]

**Classical models are not inherently ML.** Mean–Variance is mathematical optimization, while classical Black–Litterman is Bayesian portfolio construction. They become part of a machine-learning investment system when learned forecasts, risk estimates or control parameters enter their calculations. Keeping these categories separate prevents an architectural improvement from being mistaken for evidence that one entire model family has defeated another.

Section references:
[4] Mean–Variance estimation and selection <https://www.diva-portal.org/smash/get/diva2:1060405/FULLTEXT01.pdf> Excerpt: "Parameter estimation: from historical observations and beliefs, one forms estimations of future performance (in terms of return and variance) of the speciﬁed universe of securities. Portfolio selection: employing the estimated para…"
[2] Black–Litterman construction <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Excerpt: "(2003).2 The Black Litterman model combines the CAPM (see Sharpe (1964)), reverse optimization (see Sharpe (1974)), mixed estimation (see Theil (1971, 1978)), the universal hedge ratio / Black’s global CAPM (see Black (1989a, 1989b…"
[3] Deep-learning application roles <https://link.springer.com/article/10.1007/s10462-022-10226-0> Excerpt: "3 Deep learning for stock market applications 3.1 What is deep learning? Deep learning describes an ML technique based on networks of simple concepts and featuring different arrangements or architecture that allows computers to lea…"

### Market risk and forecast uncertainty differ

**Risk has two distinct meanings.** Market risk concerns the variation and losses that can occur even when a model’s parameters are correctly known. Estimation uncertainty concerns how poorly those parameters—especially expected returns—are known. A market can have high volatility but a relatively well-estimated conditional variance, or low recent volatility alongside highly uncertain forecasts.

**The distinction changes position sizing.** A conventional Mean–Variance implementation often treats estimated returns and covariances as fixed inputs. Black–Litterman explicitly models uncertainty about mean returns and views, while Bayesian neural networks can incorporate parameter uncertainty into predictive distributions. These mechanisms address related but nonidentical sources of uncertainty. [5]

**Confidence does not eliminate losses.** A narrow interval around an estimated expected return is not a narrow interval around tomorrow’s realized return. Similarly, a high-confidence Black–Litterman view can justify a larger active position while increasing portfolio exposure to market shocks. Treating confidence as if it directly reduced economic risk is a consequential modeling error.

Section references:
[5] Bayesian portfolio uncertainty <https://doi.org/10.1109/ijcnn60899.2024.10650382> Excerpt: "The proposed models estimate the density of returns and incorporate parameter uncertainty through Bayesian inference. The uncertainty and any financial risk metric of interest can directly be obtained from the estimated density. Furthermore, through the BNN input-output design, proposed BNNs incorporate potential non-linear effects of each asset in the portfolio on the obtained density estimates. The proposed method is applicable…"

### Different risk measures answer different questions

**Variance measures overall dispersion.** It penalizes unusually positive and unusually negative returns symmetrically. Downside deviation instead considers outcomes below a specified benchmark; Value-at-Risk, or VaR, identifies a loss quantile; expected shortfall, also called ES or CVaR, measures average loss in the specified worst tail. Maximum drawdown measures the largest peak-to-trough decline along an investment path. [6]

**Changing the measure changes the decision.** A portfolio can have relatively low volatility but substantial crash exposure, or a better Sharpe ratio but worse maximum drawdown. The appropriate objective therefore depends on the mandate: an absolute-return fund, a benchmark-relative equity manager and a capital-preservation portfolio need not prefer the same weights.

**The resulting judgment is architectural.** Choose the risk definition and investment constraints first, then evaluate how forecasts and uncertainty estimates improve decisions within them; the model name alone does not determine investment suitability.

Section references:
[6] Variance, downside and tail measures <https://pmc.ncbi.nlm.nih.gov/articles/PMC9362979/> Excerpt: "Maximum of the drawdown at time t is an indicator of the risk that measures the largest difference between the maximum and minimum the cumulative returns over the history preceding time t. mathematical expression unavailable in source extraction 16 The Sortino’s Ratio (Sortino and Price, 1994) is given by: mathematical expression unavailable in source extraction 17 where mathematical…"

## 2. Mean–Variance: transparent optimization with sensitive inputs

### What enters the model and how weights are chosen

**Expected returns and covariances determine weights.** For portfolio weights \(w\), expected asset returns \(\mu\) and return covariance matrix \(\Sigma\), expected portfolio return is \(w^\top\mu\), while portfolio variance is \(w^\top\Sigma w\). A standard Mean–Variance problem minimizes variance while meeting a return target \(p\) and investing the full budget. [7]

\[\min_w w^\top\Sigma w\quad\text{subject to}\quad w^\top\mu=p,\qquad \mathbf{1}^\top w=1.\]

**The objective makes preferences explicit.** An equivalent trade-off formulation maximizes expected return minus a variance penalty, with a positive risk-aversion coefficient \(\gamma\). Increasing \(\gamma\) favors lower-variance portfolios, while changing it traces different points on the efficient frontier—the portfolios offering the highest modeled return for their modeled risk. [4]

\[\max_{w\in\mathcal W}\left\{w^\top\mu-\frac{\gamma}{2}w^\top\Sigma w\right\}.\]

**Constraints define the investable solution.** The feasible set \(\mathcal W\) can include full investment, no short selling, position limits, sector exposure restrictions and trading-cost penalties. With a positive-semidefinite covariance matrix and suitable convex constraints, this remains a tractable optimization problem. The transparency is valuable: a manager can identify whether a position reflects expected return, diversification or a binding restriction.

**Forecasting remains a separate choice.** Historical sample means are common return inputs, but they are not compulsory. Marakbi’s empirical analysis, for example, uses CAPM-based return estimates while changing the covariance estimator. This matters because poor results from sample-mean inputs should not automatically be attributed to the allocation rule itself. [4]

**Covariance captures joint movement.** Its diagonal entries measure individual asset variances, while off-diagonal entries measure co-movement. Diversification depends on the latter: several individually volatile assets can form a less volatile portfolio when their returns do not move together. Conversely, apparently diversified positions can share a large common exposure.

Section references:
[7] Mean–Variance formulation <https://arxiv.org/pdf/2604.24486> Excerpt: "​ Σ = covariance matrix of asset returns, ​ µ = vector of expected returns, ​ 𝑝 = target portfolio return. The findings lead to what is known as the efficient frontier which is an array of optimal portfolios given the maximum expected return for a specified level of risk. The real-world application of MPT depends on several important assumptions that simplify the difficulties of…"
[4] Mean–Variance estimation and selection <https://www.diva-portal.org/smash/get/diva2:1060405/FULLTEXT01.pdf> Excerpt: "portfolios with the highest possible expected return for a given level of volatility (risk) (Berk and DeMarzo 2014). At its core, CAPM is a single-factor linear model (commonly referred to as the security market line) that relates the expected return of an asset and the market portfolio. The mathematical representation of the security market line is as follows: µi = E Ri = rf + β…"

### Normality is useful, but not mathematically necessary

**Normality is not an optimization requirement.** The familiar normal-return assumption justifies summarizing portfolio outcomes by their first two moments, because a normal distribution is fully described by its mean and variance. But the quadratic program itself can be solved for non-normal returns whenever the necessary moments exist. Marakbi’s literature review specifically identifies the claim that Mean–Variance necessarily requires joint normality as a common misconception. [4]

**The deeper assumption concerns preferences.** Mean–Variance analysis treats expected return and variance as sufficient for portfolio choice. Normality provides one important setting in which that simplification is attractive; certain elliptical-distribution settings also preserve useful mean–variance relationships. With general asymmetric distributions, however, portfolios sharing the same mean and variance can have very different probabilities and severities of loss. [8]

**Non-normality is empirically concrete.** In the 2022 copula–Black–Litterman study, Shapiro–Wilk tests rejected normality for all **10 selected international ETFs**, using daily logarithmic returns over 2012–early 2022. In Agouram and Lakhnati’s Moroccan sample, Jarque–Bera tests rejected normality at the 99% confidence level for all **six MADEX stocks**, each with 714 daily observations from 1 January 2011 to 10 January 2014. [6][9]

**The Moroccan sample names matter.** Those six stocks were Addoha, Atlanta, BCP, Delta Holding, Managem and Maroc Telecom: the result concerns that defined sample, not an estimated percentage of all global securities. Separately, the 2024 Dynamic Black–Litterman study rejected normality for all 10 country ETFs at the 1% level while finding their return series stationary under its Augmented Dickey–Fuller tests. Non-normality and nonstationarity are therefore distinct issues. [10]

Section references:
[4] Mean–Variance estimation and selection <https://www.diva-portal.org/smash/get/diva2:1060405/FULLTEXT01.pdf> Excerpt: "This chapter will provide an extensive review of literature associated with portfolio optimization. Essentially, this chapter…"
[8] Non-elliptical return risks <https://actuaries.org/app/uploads/2025/07/Bugar_Maurer_Vo_Rome2008.pdf> Excerpt: "The expected return8, which can be estimated as the (arithmetic) average of returns in a given time period, is a typical measu…"
[6] Variance, downside and tail measures <https://pmc.ncbi.nlm.nih.gov/articles/PMC9362979/> Excerpt: "This study examines the portfolio optimization problem by exploiting daily data of 10 international Exchange Trade Funds (ETF)…"
[9] MADEX tests <https://doi.org/10.4236/jfrm.2015.42007> Excerpt: "We propose to build a portfolio composed only of assets from the MADEX over a period of national and global financial crisis s…"
[10] Country-ETF distribution tests <https://doi.org/10.3390/fractalfract8110642> Excerpt: "Next, at the 1% significance level, the Augmented Dickey–Fuller (ADF) test indicates that the return series of all 10 ETFs are…"

### How non-normal returns affect risk, forecasts and allocations

**Variance remains a valid statistic.** For a linear portfolio with finite second moments, \(w^\top\Sigma w\) is its variance regardless of skewness or kurtosis. Heavy tails do not automatically make that identity understate variance. The problems arise when variance is treated as a complete description of loss risk, when normal quantiles are imposed on non-normal outcomes, or when historical covariance estimates fail to represent current conditions.

**Tail shape changes loss assessment.** Negative skewness concentrates risk on the downside, while heavy tails allow more extreme outcomes than a Gaussian model with comparable dispersion. A variance-efficient portfolio can consequently be unattractive under expected shortfall or drawdown criteria. Agouram and Lakhnati found very similar VaR results for Mean–Variance and mean-Gini portfolios, but lower CVaR for mean-Gini during their turbulent MADEX evaluation. The chosen risk metric changed the comparative conclusion. [9]

**Return estimation also becomes harder.** Under a stationary process with a finite mean, non-normality alone does not necessarily bias the sample mean. Nevertheless, extreme observations can increase its sampling variability, while changing regimes can make a long historical average a poor estimate of the current conditional mean. Robust location estimation, shrinkage or conditional forecasts address different parts of this problem. [1]

**Changing dependence alters diversification.** Volatility clustering means that large movements tend to be followed by further large movements. Cont’s review documents persistent dependence in absolute or squared returns even when signed returns have little autocorrelation. A covariance matrix averaged across calm and turbulent periods can therefore misstate current portfolio risk without any change to the optimizer’s mathematics. [11]

**Allocation can amplify these errors.** An overstated expected return makes an asset appear attractive; understated variance or covariance makes it appear cheap to hold. The optimizer then assigns it more weight, increasing the portfolio’s exposure to the very estimation error that produced the favorable input. This selection effect helps explain why an excellent fitted frontier can disappoint out of sample.

Section references:
[9] MADEX tests <https://doi.org/10.4236/jfrm.2015.42007> Excerpt: "Finally, we utilised CVaR to compare the two pairs of strategies because the outcomes are similar and CVaR can better capture the tail risk. This risk measure follows directly from the value-at-risk. This paper is organised as follows: Firstly, we present the framewo…"
[1] Outliers and return estimation <https://doi.org/10.3390/ijfs10030064> Excerpt: "For example, provided that historical closing prices of a certain stock are {243, 190, 150, 80, 56, 28, 142}, in this case, the sample mean is 127, which is not considered a good location estimator for these observations. Next, the median of the sample is 150, which…"
[11] Volatility clustering <http://rama.cont.perso.math.cnrs.fr/pdf/clustering.pdf> Excerpt: "Volatility Clustering in Financial Markets 11 4.1 An agent-based model for volatility clustering Our model describes a market where a single asset, whose price is denoted by St, is traded by N agents. Trading takes place at discrete periods t = 0, 1, 2, ... We will s…"

### Why inverse covariance creates instability

**The mechanism is visible algebraically.** In an unconstrained risky-asset problem with cash absorbing the remaining budget, the Mean–Variance solution is proportional to inverse covariance times expected excess returns. The DeePM paper uses this expression to explain the classic “error maximization” problem. [12]

\[w^\star=\frac{1}{\gamma}\Sigma^{-1}\mu.\]

**A first-order calculation shows amplification.** Holding risk aversion fixed, small perturbations in the inputs approximately change weights according to the following mathematical expansion of that solution. The full-investment constrained solution has additional terms, but the same inverse-covariance sensitivity remains.

\[\Delta w\approx\frac{1}{\gamma}\left[\Sigma^{-1}\Delta\mu-\Sigma^{-1}(\Delta\Sigma)\Sigma^{-1}\mu\right].\]

**Near-redundant assets are especially sensitive.** When two assets are highly similar, some covariance eigenvalues can be small. Their inverses can be large, magnifying modest estimation differences into substantial offsetting positions. Long-only restrictions prevent unlimited long–short bets, but can replace them with concentrated corner solutions and abrupt changes in which assets receive positive weights.

**Small changes can reshape holdings.** Idzorek’s guide cites Best and Grauer’s finding that a small increase in one asset’s expected return can force half the assets out of a Mean–Variance portfolio. This is a sensitivity result, not a forecast that half of every portfolio will disappear; it illustrates why input uncertainty must be considered before interpreting optimized weights literally. [2]

Section references:
[12] Inverse-covariance sensitivity <https://arxiv.org/html/2601.05975> Excerpt: "While classical mean–variance optimization (Markowitz, 1952) provides a foundational framework, its practical deployment is plagued by error maximization (Michaud, 1989), where small estimation errors in covariance matrices lead to unstable, turnover-intensive portfolios. Consequentl…"
[2] Black–Litterman construction <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Excerpt: "expected return of one of the portfolio's assets can force half of the assets from the In a search for a reasonable starting point for expected returns, Black and Litterman (1992), He and Litterman (1999), and Litterman (2003) explore several alternative forecasts: historical returns…"

### Better inputs can improve the same optimizer

**Covariance choice produces measurable differences.** Marakbi compared five estimators using nine global equity, bond, commodity and real-estate assets. In a separate risk-prediction exercise over 1994–2013, the study estimated covariance from 24 months of returns and compared predicted volatility with subsequent 12-month realized volatility for randomly weighted long-only portfolios. A ratio of one indicates agreement. [4]

| Covariance estimator | Mean realized/predicted volatility | Variance of ratios | Reading of the result |
|---|---:|---:|---|
| Historical sample | 1.1027 | 0.3760 | Average risk underprediction |
| Single-index | 1.0347 | 0.3182 | Closer average agreement |
| Shrinkage to single-index | 1.0983 | 0.3718 | Similar to sample estimate |
| Random-matrix filtering | 1.1310 | 0.4184 | Largest average underprediction |
| Gerber statistic | 1.0128 | 0.3026 | Closest average agreement |

**This proxy measures risk calibration.** It does not measure return-prediction skill or establish the best investment strategy, because the portfolios in that exercise were not optimized. Its value is that it isolates covariance forecasting from errors in expected-return estimation.

**Portfolio outcomes confirm a practical channel.** In the same thesis’s monthly, long-only allocation tests, with proportional trading costs of 10 basis points, replacing sample covariance with the Gerber-based estimator improved risk-adjusted results. For the 9% target-volatility profile, the comparison was as follows over January 1994–December 2013. [4]

| Covariance input | Net return/year | Volatility/year | Net Sharpe | Maximum drawdown | Annual turnover |
|---|---:|---:|---:|---:|---:|
| Historical sample | 9.48% | 10.81% | 0.61 | 30.60% | 317% |
| Gerber-based | 9.46% | 10.09% | 0.65 | 28.85% | 331% |

**The improvement came through risk control.** Nearly unchanged return accompanied lower volatility and drawdown, rather than a large forecasting breakthrough. The Gerber implementation also required positive-semidefinite matrix repair, and its generally greater trading burden increased sensitivity to higher costs. Those details are part of the economic mechanism, not incidental implementation choices.

**Mean–Variance remains a useful allocator.** Its main weaknesses should motivate better estimation, uncertainty treatment and risk objectives—not the assumption that nonlinear forecasting must replace explicit optimization.

Section references:
[4] Mean–Variance estimation and selection <https://www.diva-portal.org/smash/get/diva2:1060405/FULLTEXT01.pdf> Excerpt: "monthly data from the period January 1994 to December 2013. Data from the period January 1992 to January 1994 is excluded as the optimizer will require two years worth of monthly data to initialize the ﬁrst portfolio. I.e., January 1994 to December 2013 is the evaluation period. TR denotes total return data, which accommodates for dividends and splits. 5.1 Ex ante deﬁned sub-periods within the full evaluation sample ranging from 1st January 1994 to 31st December 2013. 5.2 Descriptive statistics for SI- and HC-based portfolios, at ﬁve diﬀerent risk target 5.3 Relative return performance for the full evaluation period. The returns of SI- based portfolios are converted to risk-adjusted returns by deleveraging SI portfolio volatility to HC portfolio volatility. ∆denotes the diﬀerence in return between SI-based portfolios and HC-based portfolios. 5.4 Descriptive statistics…"

## 3. Black–Litterman: a baseline, views and confidence-weighted departures

### The equilibrium prior establishes the starting position

**Black–Litterman starts from a benchmark.** It reverse-optimizes benchmark weights to obtain the expected excess returns that would make those weights optimal under the chosen covariance matrix and risk aversion. For market-capitalization weights \(w_{\mathrm{mkt}}\), the usual equilibrium prior is: Equilibrium reverse optimization [2]

\[\pi=\gamma\Sigma w_{\mathrm{mkt}}.\]

**The prior is an implied return.** It is not simply the historical average return and not a promise that equilibrium returns will materialize. Rather, it provides a coherent baseline across the asset universe. With no differing views, the original market-weight allocation is recovered when the allocation stage uses the corresponding risk matrix, risk aversion and compatible constraints.

**Benchmark choice is economically consequential.** A market-capitalization portfolio supplies a natural reference for a benchmark-oriented equity mandate. A liability-driven institution, dollar-neutral strategy or futures portfolio may need another reference. Reverse optimization can be applied to a policy benchmark, but its interpretation then becomes “returns implied by this reference allocation,” rather than automatically representing global market equilibrium.

Section references:
[2] Black–Litterman construction <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Excerpt: "(2003).2 The Black Litterman model combines the CAPM (see Sharpe (1964)), reverse optimization (see Sharpe (1974)), mixed estimation (see Theil (1971, 1978)), the universal hedge ratio / Black’s global CAPM (see Black (1989a, 1989b) and Litterman (2003)), and mean-variance optimization (see Markowitz (1952)). Section 1 illustrates the sensitivity of mean-variance optimization and how reverse optimization mitigates this problem. Section 2 presents th…"

### Views specify what should differ from the baseline

**Views enter through explicit matrices.** With \(N\) assets and \(K\) views, \(P\) is a \(K\times N\) matrix identifying the assets or spreads involved, while \(Q\) contains the \(K\) expected returns. An absolute view refers to an asset or basket’s return; a relative view refers to one asset or basket outperforming another. [13]

**Idzorek provides concrete examples.** His eight-asset illustration includes the following views and user-specified confidence levels. The figures are illustrative investment inputs, not realized returns or estimated success probabilities. [2]

| View | Expected-return input | Confidence | Interpretation |
|---|---:|---:|---|
| International developed equity | 5.25% excess return | 25% | Absolute return view |
| International versus US bonds | 25 basis points | 50% | Relative bond view |
| US growth versus value baskets | 2.00% outperformance | 65% | Relative equity-style view |

**Relative views target specific convictions.** A manager may believe growth will outperform value without forecasting the entire equity market’s direction. Black–Litterman allows that belief to enter directly as a spread, instead of requiring independent absolute forecasts for every asset. This can make the relationship between investment judgment and active allocation easier to audit.

Section references:
[13] Bayesian view specification <https://ar5iv.labs.arxiv.org/html/1811.09309> Excerpt: "The matrix of our personal views is very likely not to be invertible since, as we have seen in Section 1.2, we can have relative views (the ones for which the rows sum up to 0 ) and we can have absolute views (only one 1 in a row).…"
[2] Black–Litterman construction <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Excerpt: "implied confidence levels of View 1, View 2, and View 3 in the example are 32.94%, 43.06%, and 33.02%, respectively. Only using the scaled variance of each individual view portfolio to determine the diagonal elements of Ω ignores t…"

### Confidence, uncertainty and risk play separate roles

**Confidence is expressed through uncertainty.** In a conventional Gaussian formulation, the unknown mean return has prior distribution \(\mu\sim N(\pi,\tau\Sigma)\), while views satisfy \(Q=P\mu+\varepsilon\), with view-error covariance \(\Omega\). Smaller entries in \(\Omega\) indicate greater confidence; \(\tau\) scales uncertainty about the prior mean. [13]

**The posterior responds to disagreement.** The standard Gaussian update can be written in the following form, where \(Q-P\pi\) is the difference between the expressed views and their prior-implied values:

\[\mu_{\mathrm{BL}}=\pi+\tau\Sigma P^\top(P\tau\Sigma P^\top+\Omega)^{-1}(Q-P\pi).\]

**Three effects determine the tilt.** A larger disagreement supplies a stronger signal; greater prior uncertainty permits more movement away from equilibrium; greater view uncertainty reduces that movement. Because \(\Sigma\) links assets, one view can also change posterior expected returns for other assets that co-move with those directly named in the view.

**The scalar case clarifies confidence.** For one viewed return with prior mean uncertainty \(s^2\) and view-error variance \(v^2\), the weight on the disagreement is \(s^2/(s^2+v^2)\). As view uncertainty approaches zero, the posterior increasingly follows the view; as it becomes very large, the prior dominates. This is a mathematical weighting mechanism, not evidence that confident views are accurate.

**Posterior mean uncertainty is not volatility.** Under the stated Gaussian model and known \(\Sigma\), uncertainty about the mean has covariance:

\[M_{\mathrm{BL}}=\left[(\tau\Sigma)^{-1}+P^\top\Omega^{-1}P\right]^{-1}.\]

**Predictive covariance requires another distinction.** When conditional return noise and mean uncertainty are modeled separately, predictive return covariance can be represented as \(\Sigma+M_{\mathrm{BL}}\). Implementations differ in whether allocation uses the original covariance or such an augmented matrix. Therefore, a reported “Black–Litterman covariance” should be identified as either uncertainty about expected returns or covariance of future realized returns.

**Greater confidence can increase investment risk.** Reducing view uncertainty decreases modeled uncertainty about the mean, but may create a larger active position. If that position is concentrated or exposed to a common shock, realized portfolio volatility and drawdown can rise. The correct judgment is that confidence changes how strongly to act on information—not that confidence itself makes the resulting investment safe.

Section references:
[13] Bayesian view specification <https://ar5iv.labs.arxiv.org/html/1811.09309> Excerpt: "Since for both models we have that P\mu\sim N(q,\Omega) , the smaller the uncertainty in our views (the diagonal entries of \Omega ), the smaller the standard deviation and, hence, the more certain the investor is about that particular view. Hence, from the above remark, we will look at how P\hat{\bar{\mu}} behaves as we look at small values for the diagonal entries of \Omega . But how should one define small ? As we have seen in section 2.4, the expected returns for the views were q=\begin{bmatrix}0.02\\ 0.05\end{bmatrix} . Hence, even a value of 10^{-4} is quite large since this would be the variance of our view and, therefore, the standard deviation would become 10^{-2} . Hence, a 95\% confidence interval for the first view would be (0,0.04) . If one tries to input even smaller \omega , the Inverse Wishart random generator gives a non-singularity error. Hence, we conclude that we compare the models on val…"

### Why parameter calibration and subjectivity matter

**Tau has no universal setting.** Idzorek reports literature choices ranging from **0.01–0.05** to **1**. A 2024 Dynamic Black–Litterman implementation sets \(\tau=0.05\) and estimates covariance from the preceding 60 days. These values describe particular model conventions and estimation choices, not portable confidence percentages. [2][10]

**Relative scaling matters more than labels.** Holding \(\Omega\) fixed, increasing \(\tau\) makes the prior mean less certain and generally increases the influence of views. But if \(\Omega=\tau\Omega_0\), the common scale cancels from the posterior-mean update. Comparing numerical tau values across implementations without examining their Omega construction can therefore be misleading.

**Subjectivity extends beyond human opinions.** Human forecasts can exhibit overconfidence, herding or poorly specified horizons. Automated forecasts replace some judgment with data and algorithms, but introduce choices about training samples, features, architecture and confidence mapping. Fuhrer and Hock emphasize that Black–Litterman’s practical appeal comes with nontrivial calibration. [14]

**Repeated predictions measure only some uncertainty.** The LLM-enhanced Black–Litterman study makes 100 queries per stock, using the response mean as the view and response variance on Omega’s diagonal. This operationalizes confidence, but repeated-query dispersion measures variability in generated answers; a model can consistently repeat a biased forecast. Economic calibration must therefore also examine errors against subsequent outcomes. [15]

**Correlated views need correlated uncertainty.** Two forecasts based on the same price history or news story do not necessarily constitute two independent pieces of evidence. A diagonal Omega can overstate combined confidence when their errors are correlated. Human and neural views should consequently be reconciled through their information overlap and forecast-error dependence, not merely averaged.

Section references:
[2] Black–Litterman construction <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Excerpt: "Litterman model, typically sets the value of the scalar (τ ) between 0.01 and 0.05, and then calibrates the model based on a target level of tracking error.9 Conversely,…"
[10] Country-ETF distribution tests <https://doi.org/10.3390/fractalfract8110642> Excerpt: "As previously stated, we predict the 10-day-ahead close price of each ETF using the past 60 days of price data and technical indicators. Predictions are made over eight…"
[14] Practical uncertainty assessment <https://doi.org/10.3790/ccm.2025.1447405> Excerpt: "(2021): Black–Litterman and Beyond: The Bayesian Paradigm in Investment Management. The Journal of Portfolio Management, 47, 91–113. Google Scholar - Ledoit, O./Wolf, M.…"
[15] Repeated-query confidence mechanism <https://arxiv.org/html/2504.14345v2> Excerpt: "For each stock, the LLM is queried N=100 times, and the mean of these repeated responses constitutes the view for that stock. Picking matrix ( \mathbf{P}\in\mathbb{R}^{k…"

### What changes when tail risk replaces variance

**Black–Litterman need not remain Gaussian.** The 2022 international-ETF study generates views using ARMA–GARCH models and an R-vine copula, then allocates using CVaR. A copula models dependence separately from individual return distributions, allowing richer joint-tail behavior than a covariance matrix alone. [6]

**The shared-sample results reveal trade-offs.** In its 2012–early-2022 daily ETF backtest, the unconstrained-weight comparisons included the following annualized return, volatility and Sharpe figures. Drawdown here is the worst decline within a three-month window, not whole-period maximum drawdown. [6]

| Strategy | Return/year | Volatility/year | Sharpe | Worst three-month drawdown |
|---|---:|---:|---:|---:|
| Copula–BL, tau 0.2 | 3.965% | 9.712% | 0.202 | 17.042% |
| Copula–CVaR | 3.732% | 9.836% | 0.176 | 18.093% |
| Equal-weight benchmark | 3.147% | 7.143% | 0.161 | 22.164% |
| Mean–Variance | 3.398% | 8.743% | 0.159 | 17.229% |

**Higher Sharpe did not mean lower volatility.** Copula–BL led this comparison on Sharpe, while Mean–Variance and the equal-weight benchmark had lower standard deviations. Copula–CVaR offered stronger tail-loss control and lower turnover than the Black–Litterman extension. Moreover, applying a 50% maximum weight to Mean–Variance increased its reported Sharpe to 0.203, illustrating how constraints can materially change the comparison. [6]

**Black–Litterman is best understood as disciplined conviction management.** It can stabilize investment views, but its value depends on a suitable reference portfolio, calibrated uncertainty and an allocation objective that measures the risks the investor actually wants controlled.

Section references:
[6] Variance, downside and tail measures <https://pmc.ncbi.nlm.nih.gov/articles/PMC9362979/> Excerpt: "This study examines the portfolio optimization problem by exploiting daily data of 10 international Exchange Trade Funds (ETF) from 2012 to 2022. We extend the Black-Litterman (BL) approach using ARMA-GARCH-copula-based expected returns as a proxy for investor views and use the CVaR metric as a risk measure in the optimization procedure. The BL approach provides a Bayesian methodology for combining the equilibrium returns and the investor views to produce expected returns. We use Regular Vine (R-vine) copula since it provides a flexible multivariate dependency modeling. The suggested approach is compar…"

## 4. Deep learning: flexible information extraction with deployment costs

### Model families and their financial roles

**Deep learning has no single specification.** CNNs, recurrent networks, transformers, Bayesian networks and reinforcement-learning agents differ in the structures they learn and the decisions they support. Their common feature is flexible representation learning, not a common return assumption, risk measure or allocation objective. [3]

| Family | Typical inputs | Learned object | Portfolio role | Main trade-off |
|---|---|---|---|---|
| CNN | Charts, technical-feature arrays | Local or spatial patterns | Signals and stock selection | Representation choices can dominate |
| LSTM, BiLSTM, GRU, BiGRU | Return and indicator sequences | Temporal dependencies | Return or volatility forecasts | Memory can also preserve obsolete patterns |
| CNN–LSTM hybrids | Feature arrays and sequences | Combined spatial–temporal patterns | Forecast-fed allocation | More components to estimate |
| Transformer and graph models | Multivariate sequences, asset relationships | Long-context and cross-asset representations | Signals, views and scenarios | Data, compute and structural assumptions |
| Bayesian RNN/LSTM | Asset and portfolio histories | Predictive return densities | Distributional risk assessment | Inference and architecture sensitivity |
| Deep reinforcement learning | Market features and portfolio state | Sequential action policy | Weights, exposures or control parameters | Reward and environment dependence |

**Inputs extend beyond prices.** The surveyed literature uses market data, technical indicators, fundamentals, macroeconomic variables, news and social media. OHLCV features summarize opening, high, low and closing prices plus volume. These data sources can complement one another, but their publication times and economic meaning must remain aligned with the forecast horizon. [3]

**Architectures encode different assumptions.** CNNs favor reusable local patterns; LSTMs and GRUs use gated memory to represent temporal dependence; transformers learn relationships across sequence positions. Bidirectional networks can use an entire historical input window safely if that window ends before the decision, but must not obtain future observations through how training examples are constructed.

Section references:
[3] Deep-learning application roles <https://link.springer.com/article/10.1007/s10462-022-10226-0> Excerpt: "For non-traditional data sources, such as news or social media, it is quite common to combine and summarize multiple individual items within the same time interval. For example, (Day and Lee 2016) uses multiple daily news headlines as part of the training data. Elsewhere, using a sentence encoder (Conneau et al. 2017) generates equal length vectors from differently sized sets of words representing different sentences. The literature reviewed commonly uses a snapshot or aggregated data to summarize a data point within a time interval. This could be due to the data’s granularity being directly proportional to its volume. Consequently, more parameters will be required in neural networks comprising highly granular data. 2.1.3 Volume Although the volume of the data closely relates to the fr…"

### Return forecasting: nonlinear capacity is useful only when signal persists

**Nonlinearity can capture conditional relationships.** A predictor’s effect may depend on volatility, valuation, momentum or another state variable. Deep networks can learn such interactions without manually specifying every cross-term. The postwar US allocation study describes LSTM memory and gating as mechanisms for representing nonlinear, long-run temporal dependence. [16]

**Capacity does not create information.** Financial returns are noisy, and a model can fit historical relationships that disappear when market structure changes. The Office of Financial Research’s August 2026 fixed-data benchmark found asset returns near-unforecastable across roughly a dozen univariate method families without exogenous regressors, while hybrid and machine-learning approaches added forecasting power for basis spreads and bank indicators. [17]

**The target explains part of the contrast.** That benchmark does not imply that cross-sectional rankings, news-conditioned returns or volatility are equally difficult to predict. It does show why an investment system should identify what is being forecast and where incremental information comes from. A network that adds value through risk estimation may be useful even when its directional-return forecasts are weak.

**A concrete neural study separates outputs.** The 2026 joint return–risk paper reports daily return RMSE of **0.0264 in log-return units** and directional accuracy of approximately **51.9%** for ten large-cap US equities in its labeled 2020–2024 test. Its portfolio results were: Joint return–risk experiment [18]

| Strategy | Reported annual return | Sharpe |
|---|---:|---:|
| Neural Portfolio | 36.41% | 0.9125 |
| Equal Weight | 23.32% | 0.7756 |
| Historical Mean–Variance | 20.62% | 0.7474 |

**Forecast accuracy is not economic attribution.** Those portfolio differences reflect the combined forecasting, risk-estimation and optimization system. They do not by themselves identify how much improvement arose from directional prediction, changing exposure or covariance construction. The paper’s methods use rolling statistics for marginal volatility and covariance of predicted returns, making the treatment of residual return risk an especially important question.

**Predicted means are not total risk.** For a model \(r=m(x)+\varepsilon\) with zero conditional residual mean, the law of total covariance separates variation in conditional means from variation around those means:

\[\operatorname{Cov}(r)=\operatorname{Cov}(m(x))+\mathbb E[\operatorname{Cov}(r\mid x)].\]

**The omitted component can be substantial.** Covariance of forecasts alone can miss unpredictable return variation. A hybrid should therefore specify whether its neural risk module estimates conditional realized-return covariance, parameter uncertainty, or simply variation in forecasts. These quantities should not be substituted for one another because they share the label “risk.”

Section references:
[16] Nonlinear return forecasting <https://arxiv.org/html/2009.03394> Excerpt: "LSTM can capture a complex nonlinear time series dependence structure, including long-run dependence and nonstationarity, and it mitigates the problem of gradient vanishing and gradient exploding to some extent by adding gating units to capture the dependence. We argue that time series dependence is an important feature to explore, and we demon…"
[17] Fixed-data forecasting benchmark <https://www.financialresearch.gov/working-papers/2026/08/25/time-series-forecasting-methods-financial-markets/> Excerpt: "Holding the data fixed and evaluating roughly a dozen univariate methods without exogenous regressors, we find that asset returns remain near unforecastable across every method family and that hybrid and machine learning methods exhibit additional forecasting power on basis spreads and bank indicators. Keywords: time series forecasting; machine…"
[18] Joint Return and Risk Modeling with Deep Neural Networks for Portfolio Construction <https://arxiv.org/html/2603.19288> Excerpt: "Out-of-sample results during 2020–2024 show that the deep forecasting model achieves competitive predictive accuracy (RMSE = 0.0264) with economically meaningful directional accuracy (51.9%). More importantly, the learned representation effectively captures volatility clustering and regime shifts. When integrated into portfolio optimization, th…"

### Risk modeling: densities and quantiles require calibration

**Bayesian networks can represent distributions.** The 2024 IJCNN paper estimates time-varying portfolio return densities with Bayesian RNNs and LSTMs, incorporating parameter uncertainty through Bayesian inference. Its empirical application assesses an equally weighted portfolio of 29 ETFs plus a risk-free asset over 2005–2020. [5]

**Distributional outputs support multiple measures.** A suitably estimated density can generate volatility, loss quantiles and tail averages rather than only a point forecast. But the IJCNN study deliberately separates portfolio-weight optimization from risk assessment: its reported risk-estimation improvement should be interpreted at that layer. It also finds Bayesian RNN results relatively more stable than Bayesian LSTM results, with larger models more dependent on inference method. [5]

**Quantile networks target losses directly.** A network trained with quantile, or pinball, loss can estimate a conditional VaR threshold without fitting a normal distribution. Whether that threshold is useful depends on how often losses exceed it and whether exceedances cluster. The cross-market evidence developed below shows that flexible neural quantiles can still underreact to stress.

**Nonparametric does not mean assumption-free.** Neural models impose assumptions through architecture, training loss, feature construction, regularization and the representativeness of historical data. They relax some parametric restrictions, but remain exposed to sparse extreme observations and unfamiliar joint-loss patterns.

Section references:
[5] Bayesian portfolio uncertainty <https://doi.org/10.1109/ijcnn60899.2024.10650382> Excerpt: "We analyze the risk of a daily, equally weighted portfolio of 29 ETFs and a risk-free asset for a long time span with differing market environments between 09/06/2005 and 10/09/2020. We study the effects of different inference methods on the obtained results. The proposed models improve portfolio risk estimates compared to the benchmark. The performances of the proposed models depend on BNN design and the inference method. RNN models lead to relatively more stable results compared to LSTMs. Furthermore, the results of models with a relatively higher number of…"

### Allocation: forecast-fed optimization versus direct policies

**Forecast-fed allocation preserves financial structure.** Neural expected returns or risk estimates can enter Mean–Variance, Black–Litterman, CVaR or Sharpe-ratio optimization. This preserves explicit restrictions and allows the contribution of each input to be examined. The 2024 Dynamic Black–Litterman study, for example, uses recurrent networks to produce 10-day-ahead ETF forecasts that become portfolio views. [10]

**Direct policies learn actions instead.** A reinforcement-learning agent receives market and portfolio states and learns actions that maximize a specified reward. DeepTrader combines asset-level pattern learning with market-condition information to adjust long–short exposure, using negative maximum drawdown as a reward component. Its risk behavior follows that reward and environment—not the generic fact that it uses deep learning. [19]

**Reward design embeds investment preferences.** Maximizing log return, a Sharpe-related reward or drawdown protection can produce different policies from the same observations. The RA-DRL framework makes this explicit by training three PPO agents around distinct return and risk goals, then combining their actions through a CNN. Its out-of-sample assessment covers India, the United States, Taiwan and Spain from January 2021 to March 2024. [20]

**Intermediate control can be more governable.** Smart Tangency Portfolio assigns DRL the narrower tasks of choosing a risk–return position and rebalancing horizon, while a classical optimizer computes weights. This reduces the burden of learning every portfolio restriction through rewards. It also separates adaptive control from the investor’s ultimate risk mandate, which should remain externally governed. [21]

Section references:
[10] Country-ETF distribution tests <https://doi.org/10.3390/fractalfract8110642> Excerpt: "Using recurrent neural networks (RNNs), past price data and technical indicators are employed to forecast the prices of each exchange-traded fund (…"
[19] DeepTrader allocation mechanism <https://doi.org/10.1609/aaai.v35i1.16144> Excerpt: "In particular, to tackle the risk-return balancing problem, our model embeds macro market conditions as an indicator to dynamically adjust the prop…"
[20] Multi-objective DRL design <https://doi.org/10.1007/s44196-025-00875-8> Excerpt: "In-sample data from 01/01/2011 to 31/12/2020 is utilized for training the PPO agents, and their trading performance is assessed on out-of-sample da…"
[21] Optimizer-mediated reinforcement learning <https://doi.org/10.3390/ijfs13040227> Excerpt: "Title: Smart Tangency Portfolio: Deep Reinforcement Learning for Dynamic Rebalancing and Risk–Return Trade-Off Markdown Content: Image 1: Open Acce…"

### Overfitting, leakage, shift and interpretability

**Low signal encourages noise memorization.** A high-capacity model may fit accidental relationships, especially with many predictors and comparatively few independent market episodes. Reported controls include feature pruning, dropout, weight decay, Huber loss, temporally ordered validation and ensembling across random initializations. The postwar LSTM study averages five initialized models per estimation window. [16]

**Leakage can manufacture apparent predictability.** Examples include scaling with future observations, selecting historical securities using later index membership, using revised macroeconomic data, or allowing overlapping forward-return labels to contaminate validation. Khushi’s quantitative-finance reporting standards identify point-in-time features, leakage-free normalization and time-respecting splits as necessary parts of credible economic testing. [22]

**Distribution shift is a different failure.** A leakage-free model can still fail when the relationship between inputs and returns changes. Retraining allows adaptation but does not guarantee it: shorter windows react faster while increasing estimation noise, and longer windows provide more observations while mixing potentially incompatible regimes.

**Interpretability has several levels.** Classical optimization exposes its objective and constraints, but may still receive opaque inputs. Neural feature attribution can show which inputs influenced a forecast, while SHAP can help explain learned risk or allocation outputs. Neither feature attribution nor attention weights automatically establish economic causality. [23]

**Explanations should also be stable.** Small, economically irrelevant input changes should not produce radically different accounts of why a position exists. The financial-XAI review connects feature-contribution analysis with debugging and pruning potentially overfitted features, and stresses consistency across inputs. [23]

**Deep learning earns a portfolio role through incremental decision value.** Nonlinear capacity is an advantage when persistent information survives realistic testing; otherwise, it adds estimation and operational risk without improving the investment.

Section references:
[16] Nonlinear return forecasting <https://arxiv.org/html/2009.03394> Excerpt: "We consider NN1, NN2, and NN3 models that contain 16, 32–16, and 32–16–8 neurons in the one, two, and three hidden layer structures, respectively, and an LSTM model, which is an NN with three recurrent layers with 32-16-8 neurons in each and LSTM cells in…"
[22] Leakage and reporting standards <https://link.springer.com/article/10.1007/s10462-026-11664-w> Excerpt: "The seven standards specify an end-to-end experimental pipeline, covering (i) dataset construction, (ii) labelling, (iii) point-in-time feature engineering, (iv) leakage-free scaling or normalisation, (v) time-respecting data splits, (vi) evaluation metri…"
[23] Financial explainable-AI review <https://link.springer.com/article/10.1007/s10462-024-11077-7> Excerpt: "Stability in the prediction can be used to access a model’s confidence while explanations provided by the model should only be trusted if it produces results that are consistent across different data inputs. Causality: It is usually in the interest of dev…"

## 5. What changes across market conditions?

### The evidence favors conditional decisions

**Performance changes with the environment.** Calm markets, volatility shocks, persistent trends and abrupt structural breaks alter both the information available to models and the costs of acting on it. The relevant distinction is often not “classical versus deep,” but whether a system captures the current conditional distribution without generating excessive trading.

| Market condition | Mean–Variance | Black–Litterman | Deep learning | Practical judgment |
|---|---|---|---|---|
| Stable relationships | Tractable baseline | Stable benchmark-relative tilts | Can exploit persistent interactions | Demand incremental net value |
| Rising volatility | Needs responsive covariance | Needs updated risk and confidence | Adaptation depends on training | Compare with dynamic classical risk |
| Heavy-tailed losses | Variance omits tail severity | Classical form retains tail assumptions | Tail outputs need backtesting | Use explicit ES and stress controls |
| Abrupt regime change | Historical inputs can lag | Prior and views can become stale | Learned relationships can fail | Reduce reliance on fragile signals |
| Weak directional signal | Return estimates become noisy | Equilibrium anchor limits active bets | Capacity can fit noise | Favor shrinkage and low turnover |

**The mechanisms explain the table.** A flexible model benefits when its additional state information predicts economically relevant changes. A simpler model benefits when estimation noise dominates, because stronger structure can prevent reactions to transient patterns. The balance is observable only through the complete investment process, including execution.

### Tail-risk forecasting: the strongest controlled comparison

**Filtered classical risk beat compact LSTMs.** The 2026 study *Does Machine Learning Beat the GARCH Benchmark?* compares historical simulation, GARCH-filtered historical simulation and a walk-forward quantile LSTM across **39 equity markets**, comprising 19 developed, 18 emerging and two frontier markets. Its common out-of-sample sample spans 2005–2025 and **192,789 market-days**. [24]

**Calibration, not average level, separated them.** At a 5% target exceedance probability, filtered historical simulation achieved a 4.92% average breach rate and passed conditional coverage in 19 markets. The 16-unit LSTM passed in four; increasing it to 64 units improved the count to nine. A conditional-coverage pass means the test did not reject the combined coverage and timing requirements at the study’s threshold. [24]

| Risk estimator | Mean breach rate | Conditional-coverage passes | Mean tail-calibration \(Z_2\) |
|---|---:|---:|---:|
| Historical simulation | 5.61% | 0/39 markets | −0.205 |
| GARCH-filtered simulation | 4.92% | 19/39 markets | −0.003 |
| LSTM, 16 units | 5.12% | 4/39 markets | −0.195 |
| LSTM, 64 units | 4.99% | 9/39 markets | −0.113 |

**Breach frequency alone would mislead.** The small LSTM’s average rate was close to 5%, but its losses still clustered in ways inconsistent with conditional calibration. Historical simulation failed the independence test in every market. This shows why a risk model should be assessed on when it fails, not merely how often. [24]

**Filtering addresses a specific mechanism.** GARCH updates conditional variance as new returns arrive, while filtered historical simulation obtains tail information from standardized empirical residuals. Its use of normal quasi-likelihood for variance estimation does not mean that final tail quantiles are forced to be normal. This is a stronger benchmark than a static Gaussian risk model.

**The crisis response was economically visible.** In the study’s US example, filtered VaR reached 8.2% by 29 October 2008 using parameters estimated before 2008, whereas historical simulation reacted much more slowly as crisis observations entered its rolling window. The speed advantage came from daily variance updating, not foreknowledge of the crisis. [24]

**Neural outputs nevertheless added different information.** The study found the neural risk measures less procyclical: in its macroeconomic baseline, a one-percentage-point increase in GDP growth was associated with a 1.5% decline in neural risk, versus 4.3% for historical tail risk. However, that smoother response was not a substitute for adequate stress calibration. The implication is to evaluate neural and filtered measures as potentially complementary signals. [24]

Section references:
[24] Global tail-risk comparison <https://doi.org/10.3390/economies14090379> Excerpt: "We compare three families of Value-at-Risk and expected shortfall estimators—rolling historical simulation, GARCH(1,1) filtered historical simulation (FHS), and a walk-forward multi-quantile LSTM—on identical, strictly out-of-sample footing across thirty-nine developed, emerging, and frontier equity markets over 2005–2025 (192,789 market-days). The answer to the title question is no. Historical simulation fails the Christoffersen independence test in every market. Filtering repairs most of this: FHS passes conditional coverage in nineteen markets, attains a 4.9% breach rate against a 5% target, and prices expected shortfall essentially without bias (mean Acerbi–Székely Z 2 of −0.003). The neural measure improves on historical simulation but passes conditional coverage in only four markets and understates tail severity by roughly 20% (Z 2 = −0.195); it tracks filtered more closely than historical VaR (within-market correlation 0.53 versus 0.40, p 0.001), which indicates t…"

### Volatility and predictability regimes change rankings

**Dynamic variance protected better in stress.** Iqbal and Ramachandran compare A2C, PPO, DDPG, TD3 and SAC with the NIFTY50 index and a dynamic minimum-variance portfolio under trading costs, position limits and turbulence penalties. DRL outperformed the market benchmark in most low- and medium-volatility regimes, but no algorithm dominated consistently; variance-based portfolios offered stronger downside protection in high volatility. [25]

**Regime definitions were tested across windows.** Their high-volatility periods include 2007–2009 and March–May 2020. Re-identification using 21-, 30- and 60-day log-variance windows altered boundary timing and duration rather than the broad classification. This supports the interpretation that the performance differences related to market conditions, not simply one arbitrary volatility window. [25]

**Structured signals can favor deep policies.** Another Indian-equity study compares four DRL models with six traditional strategies across three market-efficiency groups among 45 firms. Deep models performed best in the study’s highly efficient category, while traditional methods often matched or exceeded returns in less efficient categories. The authors explain their classification in terms of stable, weak signals versus noisy, less structured processes—not as a universal proposition about informational market efficiency. [26]

**Asset class changes the adaptation problem.** In a four-cryptocurrency DRL experiment, average daily volatility ranged from **2.47%** during 25 October–10 November 2018 to **7.34%** during 25 November–10 December 2018. The experiment charged 0.2% on buys and sells, and no configuration achieved positive daily returns in every test period. Adaptation should therefore be judged jointly against volatility and implementation friction. [27]

Section references:
[25] NIFTY50 regime evidence <https://doi.org/10.1007/s10690-026-09629-8> Excerpt: "Volatility regimes are re-identified using 21-day, 30-day, and 60-day rolling windows applied to the log-variance of NIFTY50 returns, with structural breaks detected using the same methodology as in the main anal…"
[26] Efficiency-conditioned comparison <https://link.springer.com/article/10.1007/s44163-026-01869-x> Excerpt: "The results show that deep learning models perform best in highly efficient markets where signals are weak but consistent. In moderately and least efficient markets, traditional strategies often achieve similar o…"
[27] Cryptocurrency test conditions <https://doi.org/10.1007/s00521-020-05359-8> Excerpt: "On average, the period with the lowest volatility (2.47\(\%\)) goes from 25 October 2018 to 10 November 2018 (Test 7) and the highest volatility (7.34\(\%\)) is reached in the period from 25 November 2018 to 10 D…"

### Return and allocation evidence points in both directions

**Black–Litterman has contrasting historical results.** A Swedish-equity simulation favored it over Mean–Variance in four of five strategy strengths, while a two-asset equity–bond study favored Mean–Variance, especially in recessions and crises. Deep-learning studies likewise show advantages that vary with investment horizon and model complexity.

| Study setting | Evaluation context | Main finding | Investment interpretation |
|---|---|---|---|
| 23 OMXS30 stocks | 2003–2013; zero costs | BL led in 4/5 strategy strengths | Useful benchmark-relative view integration |
| SPX equities and bond index | 2000–2018 out of sample | MV led, especially in crises | BL anchoring is not automatic protection |
| US stock index and Treasury bill | Postwar sample | LSTM led CER and Sharpe in 5/7 decades | Recurrent signals helped market timing |
| Equities, ETFs and bonds | 2015–2023; seven strategies | MV led return/Sharpe; Transformer–GNN led risk control | The preferred metric changes the winner |

**The Swedish comparison is specific.** Hirani and Wallström used 23 of the 30 OMXS30 stocks, rebalancing every 20 trading days with risk aversion 2.5 and 5% stated prior uncertainty. Their sensitivity analysis found Black–Litterman materially less responsive to input changes than classical Mean–Variance. [28]

**The two-asset counterexample is substantive.** The Copenhagen Business School study uses rolling return and covariance estimates for SPX equities and the LUATTRUU bond index over 2000–2018, evaluating Sharpe, certainty-equivalent return and other measures. Its finding that Black–Litterman underperformed during recessions and crises directly challenges the idea that equilibrium shrinkage necessarily provides superior downside protection. [29]

**Recurrent gains depended on timing.** In the postwar stock-index–Treasury-bill study, the best LSTM increased annual certainty-equivalent return from approximately 4.7% to 10%, while monthly Sharpe increased from 0.049 to approximately 0.175. Certainty-equivalent return expresses utility-adjusted performance under the study’s investor preferences, rather than a guaranteed investment return. The LSTM’s incremental advantage weakened with annual rebalancing, and simpler networks sometimes matched it during expansions. [16]

**Different objectives also explain opposing winners.** Ozechi and colleagues’ 2015–2023 comparison reports the highest cumulative return and Sharpe for Mean–Variance with well-calibrated inputs, but the lowest volatility and drawdown for Transformer–GNN. That result supports comparing complete risk–return profiles rather than selecting whichever model leads one statistic. [7]

Section references:
[28] OMXS30 comparison <https://liu.diva-portal.org/smash/get/diva2:758241/FULLTEXT01.pdf> Excerpt: "rebalancing frequency of 20 trading days, an estimated risk aversion parameter of 2.5 and a five per cent uncertainty associated with the CAPM prior. Sensitivity analysis performed by examining how the results are affected by varia…"
[29] Equity–bond counterexample <https://research.cbs.dk/en/studentProjects/a-comparison-of-the-black-litterman-model-and-the-mean-variance-a/> Excerpt: "Further, it compares the performance of the allocation models over an out-of-sample period running from 01-01-2000 to 31-12-2018, reflecting a real investment scenario. The analysis applies a simple multi-asset portfolio consisting…"
[16] Nonlinear return forecasting <https://arxiv.org/html/2009.03394> Excerpt: "By departing from the expectations hypothesis and exploiting return predictability through our best-performing LSTM specification, the investor’s annual certainty-equivalent return roughly doubles (from around 4.7% to approximately…"
[7] Mean–Variance formulation <https://arxiv.org/pdf/2604.24486> Excerpt: "from 2015 to 2023 across a variety of asset classes were used, including equities, Exchange-Traded Funds (ETFs), and bonds. This research further examines the structural capabilities and predictive power of Graph Neural Networks (G…"

### Trading friction can reverse the practical conclusion

**A small forecasting gain may be expensive.** Bengoechea Pardo’s anchored walk-forward study uses monthly OHLCV-derived features for 30 large-cap US equities over 2010–2025. Its best MLP only marginally improved on a no-ML Black–Litterman baseline, at more than three times the transaction cost. [30]

| Portfolio | Reported Sharpe | Construction | Economic reading |
|---|---:|---|---|
| Best MLP pipeline | 0.96 | Promoted forecasts into BL | Small improvement with higher costs |
| No-ML Black–Litterman | 0.94 | Regularized allocation baseline | Nearly matched the learned model |
| Equal-weight 1/30 | 0.93 | Naive diversification | Competitive simple reference |

**Regularization supplied much of the value.** The study attributes its risk-adjusted performance primarily to covariance regularization and Bayesian shrinkage, expressed through drawdown control, rather than predictive model content. That is a concrete reason to test component contributions before crediting a hybrid’s results to deep learning. [30]

**Regime adaptation can generate costly discontinuities.** A European multi-asset CVaR study, evaluated over 808 weeks from 15 October 2010 to 3 April 2026, reports the following results. At each regime transition, changing the optimization scenario set caused substantial weight changes. [31]

| Strategy | Annual turnover | Gross Sharpe | Net Sharpe at 10 bps |
|---|---:|---:|---:|
| Static CVaR | 21.4% | 0.530 | 0.528 |
| Regime CVaR-A | 225.8% | 0.365 | 0.346 |
| Weighted CVaR | 232.5% | 0.368 | 0.348 |

**The cost arithmetic is economically meaningful.** Estimated linear annual cost drag for Regime CVaR-A is approximately **0.226%**, from \(2.258\times0.001\), versus **0.021%** for Static CVaR, from \(0.214\times0.001\), using the reported annual turnover and a 10-basis-point one-way rate. These are first-order cost estimates before additional market impact.

**Statistical uncertainty also matters.** The same study reports bootstrap Sharpe intervals approximately ±0.4 and no conventionally significant pairwise excess-return differences. Its economic ordering favors the static design under the stated costs, but small Sharpe differences should not be treated as precise estimates of durable superiority. [31]

**Market-condition performance is a design property.** The useful question is which combination of information, risk representation and trading discipline survives the relevant regime—not which model family deserves a permanent first-place ranking.

Section references:
[30] Cost-aware ML stress test <https://doi.org/10.5281/zenodo.20719912> Excerpt: "A rigorous, leak-free, cost-aware stress-test of whether machine-learning models trained only on monthly features derived from daily OHLCV price-volume data can produce economically meaningful, net-of-cost portfolio improvements over disciplined baselines, on 30 large-cap US equities (2010 to 2025). Models (regularized linear, tree ensembles, and deep networks) are evaluated under anchored walk-forward retraining with a pre-specified promoti…"
[31] Regime-CVaR implementation evidence <https://doi.org/10.3390/economies14070268> Excerpt: "Panel B evaluates the period from 15 October 2010 to 3 April 2026 (808 weeks) and includes all regime-conditional strategies. Performance metrics include annualized CAGR, annualized volatility, Sharpe ratio, maximum drawdown, 95% CVaR, Calmar ratio, and annualized turnover. The Sharpe ratio is computed using weekly excess returns over EURIBOR 3M and annualized by multiplying by the square root of 52. CAGR and volatility are annualized from w…"

## 6. Combining the strengths into a practical hybrid

### A completed example establishes technical feasibility

**TG–BL implements the proposed sequence.** The 2026 Transformer–GAN–Black–Litterman framework encodes market histories with a transformer, generates conditional return scenarios, converts them into views and uncertainty, and applies Black–Litterman before constrained portfolio construction. It includes turnover limits, transaction costs and next-opening execution for signals formed at the preceding close. [32]

**Its reported test shows material improvement.** Using the top 50 S&P 500 stocks selected by capitalization at each rolling-window start, the study covers January 2010–December 2024, with January 2022–December 2024 as its out-of-sample test. Against classical Black–Litterman, it reports: [32]

| System | Annual return | Sharpe | Maximum drawdown |
|---|---:|---:|---:|
| TG–BL | 16.82% | 1.16 | 12.48% |
| Classical Black–Litterman | 11.35% | 0.68 | 22.14% |
| Difference | +5.47 percentage points | +0.48 | −9.66 percentage points |

**Uncertainty supplies the stabilizing mechanism.** In volatile periods, the generated scenario distribution widens, increasing uncertainty attached to AI views. Black–Litterman then places less reliance on those views. The economic idea is sound: the system should not translate a large but unreliable forecast into an equally large active position. [32]

**The design is more important than branding.** Its feasibility does not require a transformer and GAN in every application. A recurrent forecaster, simpler probabilistic model or robust scenario estimator can occupy the same role if it provides better calibrated, economically useful information for the intended market.

Section references:
[32] TG–BL architecture <https://doi.org/10.3390/math14162939> Excerpt: "We use the top 50 constituent stocks of the S&P 500 index, selected by market capitalization as of the beginning of each rolling window, covering the period from January 2010 to December 2024. The selected period contains multiple market conditions: steady expansion before 2020; COVID-19 market crash; post-pandemic re…"

### A concrete modular architecture

**Each module should have one responsibility.** The following is a proposed synthesis of documented approaches, not a claim that one published experiment has validated every component together.

| Module | Main input | Main output | Purpose | Governing control |
|---|---|---|---|---|
| Point-in-time data | Prices, fundamentals, macro, text | Decision-time features | Preserve information timing | Publication and execution timestamps |
| Forecast model | Historical features | Returns, rankings or scenarios | Extract nonlinear signals | Temporal validation and simple baselines |
| Risk model | Returns and conditional features | Covariance and tail scenarios | Represent stochastic losses | Classical filtering and stress checks |
| Uncertainty model | Forecast errors and intervals | View-error covariance | Quantify forecast reliability | Dependence-aware calibration |
| Black–Litterman | Prior, views, uncertainty | Posterior mean returns | Moderate active convictions | Benchmark and confidence governance |
| Constrained allocator | Posterior returns and risk | Target portfolio weights | Match the mandate | Exposure, tail and turnover restrictions |
| Execution layer | Targets and current holdings | Implementable trades | Preserve gains after friction | Costs, liquidity and no-trade regions |
| Explanation layer | Forecasts, views and constraints | Decision attribution | Make positions auditable | Stability and reconciliation checks |

**Information flows through explicit interfaces.** Market data become forecasts or scenarios; calibrated uncertainty determines how strongly those forecasts influence posterior returns; the optimizer translates posterior information into feasible weights; execution determines whether the intended trade is economically worthwhile. This structure allows a failed forecast module to be replaced without discarding the entire portfolio system.

### Forecasts and priors should complement one another

**The prior supplies a reference allocation.** For a benchmark-oriented equity strategy, market-capitalization weights provide the classical Black–Litterman anchor. For other mandates, a policy portfolio may be more appropriate. The selection should reflect what the investor intends to hold when there is insufficient reason to make active departures.

**Deep models should supply identified information.** A return forecaster can produce absolute views, a ranking model can produce relative views, and a distributional model can generate scenarios. These outputs should have a common currency, horizon and return definition before entering the posterior. A 10-day expected return cannot be combined directly with an annual prior and daily view variance.

**Human views can remain valuable.** They can encode information outside the fitted dataset or impose a documented assessment of an unusual event. But disagreement between a human view and a neural forecast should be resolved through their relevance, reliability and shared information—not by assigning human judgment or automation automatic priority.

**A useful alternative learns fewer decisions.** Smart Tangency Portfolio illustrates delegating risk–return positioning and rebalance timing to DRL while retaining explicit optimization. Its evidence supports the broader principle that AI need not directly output every asset weight to add adaptive behavior. [21]

Section references:
[21] Optimizer-mediated reinforcement learning <https://doi.org/10.3390/ijfs13040227> Excerpt: "Unlike approaches that directly estimate portfolio weights, our framework retains the optimization structure while delegating the choice of risk level and rebalancing interval to the AI agent, thereby improving stability and incorporating a market-timing component. Empirical a…"

### Uncertainty should govern how strongly the system acts

**Calibrate uncertainty against the correct object.** Omega represents errors or uncertainty in views about expected returns; it is not automatically equal to the full variance of realized returns. Scenario dispersion contains market uncertainty as well as possible parameter uncertainty. A hybrid must document how those components become confidence in a mean-return view.

**Dependence must survive the calibration.** Forecast errors often co-move across assets because they share market shocks and model assumptions. Liao, Ma, Neuhierl and Schilling develop neural forecast-confidence intervals that account for cross-sectional dependence, using a closed-form approximation and a computationally lighter k-step bootstrap. Their asymptotic coverage results apply under stated complexity conditions, including a non-overparameterized model setting. [33]

**Uncertainty can justify smaller or zero bets.** Their uncertainty-averse allocation treats expected returns as lying within confidence intervals and optimizes worst-case Mean–Variance utility. The resulting non-participation region expands as uncertainty rises. If cash or a defensive alternative is feasible, this provides a coherent mechanism for declining a risky position whose apparent edge is too uncertain. [33]

**Do not count uncertainty repeatedly.** Increasing Omega, adding posterior mean uncertainty to predictive covariance, applying robust mean intervals and shrinking position limits can all reduce exposure. Using all four without separating their purposes may penalize the same uncertainty several times. A general-purpose architecture needs a coherent uncertainty accounting system, not simply more conservative components.

Section references:
[33] Forecast-confidence intervals <https://memento.epfl.ch/public/upload/files/Neuhierlpaper_5dGqnJV.pdf> Excerpt: "selection under uncertainty aversion, we show that machine learning confidence intervals lead to qualitatively different investment behavior relative to the standard mean-variance model. Another strand of literature in asset pricing studies model uncertainty (e.g., Avramov (2002), Anderson and Cheng (2016); Bianchi et al. In this…"

### Allocation should combine financial objectives with implementation

**A practical objective separates concerns.** One possible specification uses a posterior-centered uncertainty set \(\mathcal U_t\), stochastic return covariance \(\Sigma_{\mathrm{risk},t}\), trading-cost function \(C_t\), current pre-trade weights \(w_t^-\), and a turnover regularizer \(\eta\). An expected-shortfall ceiling then controls tail loss independently of the symmetric variance penalty:

\[\max_{w\in\mathcal W_t}\min_{\mu\in\mathcal U_t}\left\{w^\top\mu-\frac{\gamma}{2}w^\top\Sigma_{\mathrm{risk},t}w-C_t(w-w_t^-)-\eta\|w-w_t^-\|_1\right\}\quad\text{subject to}\quad \operatorname{ES}_{\alpha,t}(-w^\top r)\le b_t.\]

**This is a proposed allocation formulation.** The feasible set can impose budget, position, leverage, sector, factor and liquidity restrictions; \(b_t\) is the mandate’s tail-risk budget. Here, covariance represents stochastic return variation, while \(\mathcal U_t\) represents uncertainty about expected returns. A mean–CVaR formulation is another option when tail loss should be the primary objective rather than an additional constraint.

**Not every portfolio needs every term.** Robust intervals may add little when returns are already strongly shrunk and views are weak. Tail constraints may dominate variance in a capital-preservation mandate. The appropriate simplification is the one that preserves the investor’s objectives while reducing estimation burden and unnecessary trading.

**Regime information can modify constraints smoothly.** The European CVaR study retained its full 260-week scenario window and translated regime information into transparent allocation bands rather than repeatedly replacing the risk sample. Its example rules cap equities at 45% and require at least 30% defensive assets in stress, versus a 75% equity cap and 10% defensive floor in risk-on states. [31]

**The operational result favored restraint.** These regime-constrained bands achieved net Sharpe within 0.009 of the static benchmark at roughly 29% annual turnover, compared with approximately 226% for naive regime-conditional CVaR. This is evidence that the route from regime information to weights can matter more than the sophistication of the regime detector itself. [31]

**Trading should have an inaction option.** Transaction costs create a no-trade region: a small modeled improvement need not justify adjusting the portfolio. Cost-aware optimization and bands help distinguish a genuinely useful forecast change from an economically irrelevant fluctuation. [34]

Section references:
[31] Regime-CVaR implementation evidence <https://doi.org/10.3390/economies14070268> Excerpt: "Using a strictly out-of-sample walk-forward design, we show that naive regime-conditional CVaR allocation generates excessive turnover (approximately 226% per year) that erodes net performance below a simple benchmark under any realistic t…"
[34] No-trade-region analysis <https://link.springer.com/article/10.1007/s11408-022-00419-6> Excerpt: "Our method is useful for actual portfolio allocations where various transaction costs have to be taken into account and a portfolio needs to be optimized. First, our paper demonstrates that a rebalancing strategy may be advocated for risk-…"

### Several hybrid paths already have distinct evidence

**The strongest combination depends on purpose.** Published and emerging systems connect classical structure with learning in different ways; they should not be ranked by comparing their headline Sharpes across different datasets.

| Hybrid example | Universe and period | Main integration | Reported result |
|---|---|---|---|
| Dynamic Black–Litterman | 10 country ETFs; 2024 study | Recurrent views and Hurst-based confidence | Stronger negative-trend performance |
| Differentiable risk budgeting | Multi-asset; 2017–2022 out of sample | LSTM volatility and regime switching | Sharpe 1.38 |
| DeePM preprint | 50 futures; 2010–2025 | Learned structure, EVaR-related penalty and costs | Net risk-adjusted returns roughly twice classical references |
| BAVAR–BLED preprint | 29 DJIA stocks; decade-long evaluation | Bayesian VAR, Student-t BL and TD3 | Sharpe 1.72; Sortino 2.70 |

**Risk-budget learning has an interpretable channel.** The 2025 Scientific Reports framework combines LSTM volatility forecasts, differentiable risk budgeting and regime switching. It reports a 1.38 out-of-sample Sharpe for 2017–2022, 55% above traditional risk parity and 23% above its contemporary deep-learning comparisons, alongside a 41% relative reduction in stress-period maximum drawdown. SHAP-based risk attribution supplies a post-hoc explanation layer. [35]

**Structural priors can regularize deep models.** DeePM’s graph component introduces a sparse macroeconomic structure, and its ablation reports a 21% relative maximum-drawdown reduction versus a purely data-driven attention model. The paper acknowledges that the hand-specified graph is a subjective structural prior, not established causality. This is a useful example of classical economic judgment constraining statistical flexibility. [12]

**Fat-tail hybrids address another dimension.** BAVAR–BLED uses regime-aware Bayesian VAR estimates, Student-t Black–Litterman distributions, transformer-generated views and CNN-derived risk-aversion inputs within TD3. Student-t distributions address heavy tails, but do not automatically model every form of asymmetry; their parameters and dependence assumptions still determine the resulting losses. Its reported 57.26% total return is an aggregate decade-long evaluation result, not an annual return forecast. [36]

Section references:
[35] Adaptive risk budgeting <https://doi.org/10.1038/s41598-025-26337-x> Excerpt: "The framework achieves three primary research objectives: first, it demonstrates superior risk-adjusted performance with a Sharpe ratio of 1.3…"
[12] Inverse-covariance sensitivity <https://arxiv.org/html/2601.05975> Excerpt: "The inclusion of the Graph GNN reduces Maximum Drawdown by 21% relative to a purely data-driven attention model, confirming the value of domai…"
[36] BAVAR–BLED design and results <https://arxiv.org/abs/2606.09104> Excerpt: "We propose a new BAVAR-BLED algorithm that combines methods derived from Bayesian-Averaging Vector Autoregressive (BAVAR) and the Black-Litter…"

### Failure modes determine whether the combination helps

**Conflicting signals can increase instability.** If two view generators repeatedly disagree, changing their relative confidence can produce rapidly reversing posterior forecasts. The remedy is not necessarily another ensemble: the system may need correlated error modeling, slower confidence updates, smaller active-risk budgets or exclusion of unreliable views.

**A common error can defeat diversification.** Several neural models trained on the same market history may share the same regime failure. Likewise, a benchmark prior and learned views can both favor a crowded market exposure. Diversifying algorithms is not equivalent to diversifying economic risks.

**Generative scenarios can miss joint crashes.** A scenario generator can reproduce average volatility while failing to represent simultaneous losses, liquidity stress or unfamiliar tail dependence. The risk layer should therefore compare generated scenarios with historical stress episodes and transparent filtered models, rather than assuming that a realistic-looking distribution is calibrated.

**More modules create operational dependencies.** Data timing errors, stale forecasts, inconsistent units or failed retraining can propagate into weights. Modular interfaces help because each output can be checked independently, but they also create more calibration and monitoring responsibilities. Computationally integrated prediction–optimization can improve downstream decisions, while becoming demanding as the decision dimension grows. [37]

**Interpretability should follow the entire decision.** A useful explanation identifies the originating signal, its departure from the prior, the confidence applied, the binding allocation constraints and the cost justification for trading. SHAP alone explains only part of that chain; a transparent optimizer alone does not explain an opaque forecast.

**A hybrid is effective when its interfaces control error propagation.** Combining components adds value only when uncertainty moderation, financial constraints and execution discipline prevent flexibility from becoming excessive conviction.

Section references:
[37] Integrated prediction–optimization trade-off <https://utoronto.scholaris.ca/bitstreams/b05140c9-54d5-4175-82a7-cc8a8422fb3a/download> Excerpt: "By optimizing prediction models for the downstream decision cost, the IPO framework makes more efficient use of the training data and surrounding problem structure, while keeping prediction model complexity low. Further arguments against an IPO approach is that, in most cases, the optimal prediction model parameterization is not unique and, moreover, can result in predictions that are counter-intuitive in the…"

## 7. How comparative effectiveness should be judged

### Compare the allocator and the full system separately

**Two comparisons answer different questions.** To isolate allocation mechanics, hold forecasts, risk inputs, constraints, rebalancing and costs fixed while changing the allocator or posterior update. To compare complete investment systems, allow their forecasters to differ, but give them the same point-in-time information opportunity, investment mandate and execution assumptions.

**Identical forecasts are not always appropriate.** Requiring every complete system to use the same expected returns would remove much of deep learning’s potential contribution. Conversely, changing forecasts, covariance, constraints and trading frequency simultaneously prevents a clean attribution to the allocation method. Both controlled component tests and full-system comparisons are necessary.

**A shared scoreboard makes trade-offs visible.** Each model should be evaluated on the same decision dimensions, even when the machinery generating its outputs differs.

| Test dimension | Mean–Variance | Black–Litterman | Deep learning | Hybrid decision criterion |
|---|---|---|---|---|
| Risk and tails | Realized versus predicted risk | Market and mean uncertainty | Density or quantile calibration | Reliable losses under stress |
| Return information | Input-estimation quality | Improvement over prior | Incremental predictive signal | Better net investment decisions |
| Weight stability | Input perturbations | Confidence sensitivity | Seed and retraining variation | Stable economically justified positions |
| Regime behavior | Conditional covariance response | Prior and view adaptation | Distribution-shift resilience | Protection without excessive lag |
| Turnover and costs | Reoptimization burden | Cost of active tilts | Signal-driven trading | Net gains at implementable costs |
| Statistical reliability | Parameter uncertainty | Tau/Omega robustness | Selection and overfitting risk | Dependence-aware uncertainty intervals |
| Interpretability | Objective and constraints | View-to-tilt explanation | Feature and policy attribution | Auditable end-to-end decisions |

### Measure economic performance and loss behavior together

**Sharpe is necessary but insufficient.** Report excess return per unit volatility with the same risk-free rate and annualization convention across systems. Complement it with Sortino for downside variability, Calmar for return relative to drawdown, Omega for gains versus losses around a specified threshold, and certainty-equivalent return when investor preferences are explicitly modeled. These measures answer different questions and should not be treated as interchangeable rankings.

**Downside and tails need direct tests.** Report downside deviation or semivariance, VaR and ES at stated horizons and confidence levels, and stress-period losses. Kupiec tests assess breach frequency, Christoffersen tests assess timing and conditional coverage, and ES backtests examine tail severity. The 39-market study shows why acceptable average breach frequency can coexist with poor stress behavior. [24]

**Drawdown adds path-dependent information.** Report maximum drawdown, its measurement frequency and the relevant evaluation window. A relative drawdown reduction, such as 41%, is different from a reduction of 9.66 percentage points. Keeping these bases explicit prevents a lower-volatility or shorter-window result from being mistaken for a stronger capital-preservation claim.

**Turnover must use a stated convention.** Some studies report the sum of absolute purchases and sales; others use half that amount or another one-way measure. Costs should be applied consistently to actual pre-trade-to-target changes, with commissions, spreads, slippage, financing and market impact included as appropriate. Gross performance and net performance should both be shown.

**Cost-aware control can be a major contribution.** In a 2017–March-2026 cryptocurrency PPO study, the geometric-cost design reduced turnover by 56%–83% relative to signal following, while a circuit breaker reduced maximum drawdown by 28%–38%. These findings illustrate an execution-and-risk channel of value rather than proof that return forecasting improved. [38]

Section references:
[24] Global tail-risk comparison <https://doi.org/10.3390/economies14090379> Excerpt: "A direct test of this scope condition ( Section 4.6 ( (a)) shows that it is real but not decisive: a four-times-larger network roughly doubles conditional-coverage passes (nine versus four of…"
[38] Cost-aware crypto control <https://doi.org/10.3390/risks14050103> Excerpt: "The geometric PPO achieves turnover reductions of 78% (BTC) to 83% (ETH) relative to Greedy Signal, and 56% (BTC) to 62% (ETH) relative to flat-fee PPO. These reductions arise through two dist…"

### Test calibration, stability and incremental contribution

**Calibration must match the forecast object.** A 95% interval for an expected return and a 95% predictive interval for realized returns should not be evaluated as the same object. Similarly, view confidence, neural parameter uncertainty and VaR coverage require different checks. Forecast intervals should be assessed for empirical coverage and informativeness, not merely whether they are wide enough to contain outcomes.

**Stability should be economically interpreted.** Test weights and performance across training seeds, rolling windows, estimation choices, rebalancing frequencies and market regimes. Stable weights are not automatically desirable if the environment genuinely changes, but unstable weights unsupported by changing economic information are a warning sign.

**Ablations identify what actually helps.** The hybrid should be compared with simplified versions under otherwise consistent conditions:

| Comparison | Component changed | Question answered |
|---|---|---|
| Hybrid versus no-learned-view BL | Forecast information | Does the learned signal add value? |
| Learned forecasts with MV versus BL | Prior blending | Does uncertainty-weighted shrinkage help? |
| Sample versus regularized covariance | Risk estimation | Are gains primarily diversification gains? |
| Tail-aware versus variance-only allocation | Risk objective | Is downside protection worth its cost? |
| Cost-aware versus friction-blind allocation | Trading discipline | Do implementation controls preserve returns? |

**Statistical tests should preserve dependence.** Financial returns, forecast errors and portfolio decisions can be serially and cross-sectionally dependent. Confidence intervals and bootstrap procedures should respect that structure, and repeated model selection should be reflected in the strength of the final claim. Positive returns or significant individual strategy statistics do not establish a significant difference between competing systems.

**Published accuracy is not sufficient evidence.** Khushi’s audit of Scopus-indexed 2025 forex forecasting papers found no paper meeting all seven proposed reporting standards; economic backtesting passed in 12.2% and causal scaling in 31.7%. Those results concern that audit population, but reinforce the importance of decision-time data handling and friction-aware economic evaluation. [22]

**The effectiveness decision is conditional.** Prefer the hybrid over simpler alternatives when comparable walk-forward tests show durable net risk-adjusted gains, acceptable downside and tail calibration, stable allocations and credible explanations across the intended markets and regimes; isolate allocation effects with common forecasts, and assess full-system effects with common information, constraints, timing and costs.

**Measurement bases shape the evidence.** The empirical figures above are within-study historical results across different samples, with some findings from theses and preprints. Sharpe ratios retain their stated annual or monthly basis; drawdowns retain their stated windows. In the tail-risk comparison, neural NCVaR is a discrete quantile-average approximation, whereas filtered ES is an empirical tail mean, so their severity statistics assess different estimator constructions. The linear cost drags are labeled estimates; the proposed hybrid objective is a design synthesis rather than a claimed completed validation.

Section references:
[22] Leakage and reporting standards <https://link.springer.com/article/10.1007/s10462-026-11664-w> Excerpt: "None of these papers achieved full compliance across all seven standards, with economic backtesting (12.2%) and causal scaling (31.7%) recorded the lowest pass rates. QFRS underpins a public state-of-the-art leaderboard, ensuring that only studies satisfying these standards are ranked, with the goal of shifting the literature from opaque, error-metric-driven results to transparent, economically meaningful and comparable benchmarks. The accompanying leaderboard is available and updated regularly at Similar content being viewed by others Acknowledgements MK is supported by UKRI–NERC grant UKRI4338. The author thanks Profes-sor Marcos López de Prado, Professor Ge…"

## Conclusion

**The strongest combination is modular and uncertainty-aware.** Mean–Variance contributes transparent allocation, Black–Litterman contributes a coherent baseline and disciplined use of views, and deep learning contributes flexible information extraction. Combining them can produce a more general-purpose investment framework—but effectiveness comes from calibrated inputs, explicit downside controls, implementable trading and demonstrable incremental value, not from combining sophisticated model names.

## References

[1] <https://doi.org/10.3390/ijfs10030064> Outliers and return estimation
[2] <https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf> Black–Litterman construction; Reported allocation sensitivity; Original view illustration; Tau calibration discussion
[3] <https://link.springer.com/article/10.1007/s10462-022-10226-0> Deep-learning application roles; Financial deep-learning survey; Feature categories and data demands
[4] <https://www.diva-portal.org/smash/get/diva2:1060405/FULLTEXT01.pdf> Mean–Variance estimation and selection; Efficient-frontier mechanics; Return-input alternatives; Normality and Mean–Variance preferences; Covariance-estimator…
[5] <https://doi.org/10.1109/ijcnn60899.2024.10650382> Bayesian portfolio uncertainty; Bayesian neural density estimation; Architecture and inference sensitivity
[6] <https://pmc.ncbi.nlm.nih.gov/articles/PMC9362979/> Variance, downside and tail measures; International ETF tests; Copula-based Black–Litterman design; ETF portfolio results; Risk-objective and constraint effects
[7] <https://arxiv.org/pdf/2604.24486> Mean–Variance formulation; Multi-asset comparison
[8] <https://actuaries.org/app/uploads/2025/07/Bugar_Maurer_Vo_Rome2008.pdf> Non-elliptical return risks
[9] <https://doi.org/10.4236/jfrm.2015.42007> MADEX tests; VaR versus CVaR evidence
[10] <https://doi.org/10.3390/fractalfract8110642> Country-ETF distribution tests; Dynamic implementation; Recurrent forecasts as BL inputs
[11] <http://rama.cont.perso.math.cnrs.fr/pdf/clustering.pdf> Volatility clustering
[12] <https://arxiv.org/html/2601.05975> Inverse-covariance sensitivity; DeePM structural ablation
[13] <https://ar5iv.labs.arxiv.org/html/1811.09309> Bayesian view specification; Black–Litterman uncertainty formulation
[14] <https://doi.org/10.3790/ccm.2025.1447405> Practical uncertainty assessment
[15] <https://arxiv.org/html/2504.14345v2> Repeated-query confidence mechanism
[16] <https://arxiv.org/html/2009.03394> Nonlinear return forecasting; Overfitting controls; LSTM allocation and horizon effects
[17] <https://www.financialresearch.gov/working-papers/2026/08/25/time-series-forecasting-methods-financial-markets/> Fixed-data forecasting benchmark
[18] <https://arxiv.org/html/2603.19288>
[19] <https://doi.org/10.1609/aaai.v35i1.16144> DeepTrader allocation mechanism
[20] <https://doi.org/10.1007/s44196-025-00875-8> Multi-objective DRL design
[21] <https://doi.org/10.3390/ijfs13040227> Optimizer-mediated reinforcement learning; Learning control parameters
[22] <https://link.springer.com/article/10.1007/s10462-026-11664-w> Leakage and reporting standards; Reporting-standard audit
[23] <https://link.springer.com/article/10.1007/s10462-024-11077-7> Financial explainable-AI review; Explanation consistency
[24] <https://doi.org/10.3390/economies14090379> Global tail-risk comparison; Coverage and architecture results; Breach-timing evidence; 2008 filtering example; Macroeconomic risk responses; Tail-risk evaluat…
[25] <https://doi.org/10.1007/s10690-026-09629-8> NIFTY50 regime evidence; Volatility-window sensitivity
[26] <https://link.springer.com/article/10.1007/s44163-026-01869-x> Efficiency-conditioned comparison
[27] <https://doi.org/10.1007/s00521-020-05359-8> Cryptocurrency test conditions
[28] <https://liu.diva-portal.org/smash/get/diva2:758241/FULLTEXT01.pdf> OMXS30 comparison
[29] <https://research.cbs.dk/en/studentProjects/a-comparison-of-the-black-litterman-model-and-the-mean-variance-a/> Equity–bond counterexample
[30] <https://doi.org/10.5281/zenodo.20719912> Cost-aware ML stress test; Reported performance attribution
[31] <https://doi.org/10.3390/economies14070268> Regime-CVaR implementation evidence; Cost and inference results; Transparent regime constraints; Weight-band results
[32] <https://doi.org/10.3390/math14162939> TG–BL architecture; TG–BL out-of-sample results; TG–BL stress response
[33] <https://memento.epfl.ch/public/upload/files/Neuhierlpaper_5dGqnJV.pdf> Forecast-confidence intervals; Uncertainty-averse allocation
[34] <https://link.springer.com/article/10.1007/s11408-022-00419-6> No-trade-region analysis
[35] <https://doi.org/10.1038/s41598-025-26337-x> Adaptive risk budgeting
[36] <https://arxiv.org/abs/2606.09104> BAVAR–BLED design and results
[37] <https://utoronto.scholaris.ca/bitstreams/b05140c9-54d5-4175-82a7-cc8a8422fb3a/download> Integrated prediction–optimization trade-off
[38] <https://doi.org/10.3390/risks14050103> Cost-aware crypto control
