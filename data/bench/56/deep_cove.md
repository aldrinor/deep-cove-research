# Solving a First-Price Auction with Two Asymmetric Bidders

**Yes—a general method exists.** For two risk-neutral bidders with independent private values drawn from different smooth distributions, the standard approach is to characterize equilibrium through a coupled system of differential equations for the *inverse bidding functions*, together with boundary and matching conditions. This gives a general equilibrium characterization and a numerical solution procedure; it does not give a universal closed-form formula for the two bidding functions. [1]

**The essential questions are connected.** We first derive the bidders’ incentives and the inverse-bid equations, then explain which endpoint conditions select an equilibrium. We then distinguish analytically solvable examples from the general numerical problem, compare computational methods, and identify what changes when independence, continuity, risk neutrality, or invertibility is relaxed.

## Which solution route applies?

**The distributional structure determines the route.** The same incentive argument underlies the smooth asymmetric model, but special distributions can simplify its equations substantially. The numerical literature explicitly distinguishes such analytical examples from general asymmetric auctions. [2]

| Case | Solution route | Main output |
|---|---|---|
| Smooth, common-support asymmetric IPV | Coupled inverse-bid boundary-value problem | General equilibrium characterization |
| Two different uniform intervals | Special analytical solution | Explicit inverse bids or bids |
| Power-family examples | Simplified ODEs and analytical reductions | Special solutions and exact benchmarks |
| Other regular continuous distributions | Boundary-value solving, shooting, or projection | Numerical equilibrium strategies |
| Discrete, correlated, or noninvertible cases | Modified best-response formulation | A different or extended equilibrium computation |

The key distinction is between **characterizing equilibrium**, **expressing it analytically**, and **evaluating it numerically**. These are different achievements, and the first does not require the second.

## The model and the equilibrium being sought

### Auction rules, information, and asymmetry

**There are exactly two bidders.** Bidder \(i\in\{1,2\}\) privately observes a valuation \(v_i\), submits a sealed nonnegative bid, and receives the object if her bid is highest. The winner pays her own bid; the loser pays nothing. These are the first-price sealed-bid rules used in the standard asymmetric independent-private-values model. [1]

**Values are independently drawn.** Write \(V_i\sim F_i\), with realized value \(v_i\), density \(f_i=F_i'\), and support \([\underline v_i,\overline v_i]\). Independence means that learning \(v_i\) does not change bidder \(i\)’s beliefs about the opponent’s value. Both distributions, their association with bidder identities, and the auction rules are common knowledge. [3]

**Different distributions create ex-ante asymmetry.** The relevant assumption is \(F_1\ne F_2\): bidders differ before their values are realized. This is distinct from the ordinary ex-post difference between two realized values, which occurs even in a symmetric auction. One distribution need not first-order stochastically dominate the other; a “strong bidder versus weak bidder” ordering is an additional assumption used for some comparative results, not a requirement for writing the equilibrium equations. [4]

### Assumptions behind the smooth construction

**Risk neutrality gives the baseline objective.** A bidder with value \(v_i\) who wins at bid \(b\) receives monetary surplus \(v_i-b\), and receives zero when losing. Thus she maximizes expected surplus, rather than expected utility under a nonlinear utility function. This assumption is responsible for the particular surplus terms appearing in the equations below. [3]

**Continuous types permit the differential equations.** For the main derivation, take atomless value distributions on a common support, normalized to \([0,1]\), with \(F_i(0)=0\), \(F_i(1)=1\), and continuous, strictly positive densities on the interior. Stronger smoothness and endpoint-density assumptions enter particular uniqueness theorems and numerical procedures. For example, Gayle and Richard use twice continuously differentiable CDFs with densities bounded away from zero on their common support. [3]

**The common support is a baseline.** Different distributions can share \([0,1]\), so common support does not eliminate asymmetry. Conversely, two different uniform distributions must differ in their supports, and those cases remain important analytical examples. A common change of monetary units can normalize a common interval; separately rescaling each bidder’s values changes the economic comparison between their bids and is not simply a normalization of the same auction.

**The equilibrium target is bidder-specific.** We seek a monotone pure-strategy Bayesian–Nash equilibrium consisting of bidding functions \(b_1(v_1)\) and \(b_2(v_2)\). “Pure strategy” means that a type chooses a definite bid; “Bayesian–Nash equilibrium” means that each type’s prescribed bid maximizes expected payoff against the opponent’s strategy. In the standard smooth common-support model, equilibrium strategies are continuous, strictly increasing, and differentiable on the interior. [5]

**Strict increase makes inversion possible.** The inverse function tells us which value submits a particular bid. This is the central mathematical convenience: at a common bid, the two bidders generally have different corresponding values, and inverse strategies describe both on the same bid axis.

For this regular model, the appropriate object is therefore a pair of jointly determined bidding functions—not two independent applications of the symmetric-auction formula.

## Winning probabilities, payoffs, and first-order conditions

### From an opponent’s strategy to a winning probability

**Define the inverse bidding functions.** Let \(\phi_i(b)=b_i^{-1}(b)\) on bidder \(i\)’s equilibrium bid range. The defining identities are

\[
\phi_1(b_1(v_1))=v_1,\qquad \phi_2(b_2(v_2))=v_2.
\]

A strictly increasing opponent strategy converts a bid into a cutoff in the opponent’s value. Bidder 1 outbids bidder 2 when \(V_2<\phi_2(b)\), and bidder 2 analogously outbids bidder 1 when \(V_1<\phi_1(b)\). [6]

**Both winning probabilities are explicit.** For bids inside the common smooth bid range,

\[
W_1(b)=F_2(\phi_2(b)),\qquad W_2(b)=F_1(\phi_1(b)).
\]

The distribution and inverse strategy in a bidder’s winning probability belong to the *opponent*. Independence is what allows the opponent’s unconditional marginal distribution \(F_j\) to appear here; bidder \(i\)’s own realized value does not alter it. [4]

**Bid distributions provide equivalent notation.** Define \(G_i(b)=\Pr\{b_i(V_i)\le b\}=F_i(\phi_i(b))\). Then \(W_1=G_2\) and \(W_2=G_1\). Under atomless values and strictly increasing continuous strategies, bid distributions are atomless, so using a strict or weak inequality does not change these probabilities.

Outside an opponent’s bid range, the corresponding winning probability is extended in the usual way: zero below the range and one above it. This extension matters when checking deviations, even though the interior equations are written only on the active bid range.

### Each bidder’s optimization problem

**Expected payoff is surplus times probability.** If a type deviates to an arbitrary bid \(b\), the two objectives are

\[
\pi_1(v_1,b)=(v_1-b)F_2(\phi_2(b)),
\]

\[
\pi_2(v_2,b)=(v_2-b)F_1(\phi_1(b)).
\]

These are the two individual optimization problems from which the asymmetric equilibrium is constructed. A lower bid preserves more surplus conditional on winning, but reduces the probability of winning. [2]

**Equilibrium requires global best responses.** Formally, for each bidder \(i\), the prescribed bid must satisfy

\[
\pi_i(v_i,b_i(v_i))\ge \pi_i(v_i,b)\quad\text{for every feasible bid }b.
\]

This is the equilibrium requirement. The differential equations are obtained by differentiating these objectives at interior equilibrium bids, but boundary behavior and admissibility must also be imposed.

**Bidder 1’s interior condition follows directly.** Differentiating her payoff with respect to \(b\) gives

\[
-F_2(\phi_2(b))+(v_1-b)f_2(\phi_2(b))\phi_2'(b)=0,\qquad b=b_1(v_1).
\]

The first term is the loss from paying a little more whenever she would already win. The second is the gain from additional winning probability, multiplied by surplus conditional on winning. [4]

**Bidder 2 has the analogous condition.** Exchanging the indices yields

\[
-F_1(\phi_1(b))+(v_2-b)f_1(\phi_1(b))\phi_1'(b)=0,\qquad b=b_2(v_2).
\]

Writing both conditions is useful because it exposes the strategic interdependence: bidder 1’s optimization determines an equation involving the derivative of bidder 2’s inverse strategy, and conversely.

**The marginal trade-off has a compact form.** If \(g_j(b)=G_j'(b)\), either first-order condition can be written as

\[
\frac{g_j(b)}{G_j(b)}=\frac{1}{v_i-b},\qquad j\ne i.
\]

The proportional increase in winning probability must equal the reciprocal of the surplus being protected by bid shading. This form is especially convenient when moving from direct strategies to inverse strategies. [6]

### The envelope representation

**Winning probabilities also determine equilibrium payoffs.** Let \(q_i(v)=W_i(b_i(v))\) be bidder \(i\)’s probability of winning when she follows her equilibrium strategy, and let \(U_i(v)\) be her equilibrium expected payoff. In the normalized zero-reserve model,

\[
U_i(v)=(v-b_i(v))q_i(v),\qquad U_i'(v)=q_i(v),\qquad U_i(0)=0.
\]

The envelope theorem then gives

\[
U_i(v)=\int_0^v q_i(t)\,dt,\qquad b_i(v)=v-\frac{\int_0^v q_i(t)\,dt}{q_i(v)}.
\]

Kirkegaard uses this relationship to analyze asymmetric auctions through winning probabilities rather than directly manipulating bid equations. [5]

**This identity does not decouple equilibrium.** In an asymmetric first-price auction, \(q_1(v)\) is generally not \(F_2(v)\), because a bidder 1 type \(v\) need not submit the same bid as a bidder 2 type \(v\). Instead,

\[
q_1(v)=F_2(\phi_2(b_1(v))),\qquad q_2(v)=F_1(\phi_1(b_2(v))).
\]

The envelope formula is therefore an analytical tool and a consistency check, but not a way to bypass the strategic matching problem.

The payoff derivation gives the necessary incentive equations; inverse strategies put those equations into a form that can be solved jointly.

## The coupled inverse-bid differential equations

### The general two-equation system

**Substitute equilibrium types at each bid.** At a bid \(b\) used by bidder 1, the corresponding value is \(v_1=\phi_1(b)\); for bidder 2, it is \(v_2=\phi_2(b)\). Substituting these identities into the two first-order conditions and rearranging gives

\[
\boxed{\phi_1'(b)=\frac{F_1(\phi_1(b))}{f_1(\phi_1(b))[\phi_2(b)-b]},\qquad \phi_2'(b)=\frac{F_2(\phi_2(b))}{f_2(\phi_2(b))[\phi_1(b)-b]}.}
\]

This is the standard coupled nonlinear inverse-bid system for two risk-neutral asymmetric bidders with independent private values. [1]

**The indices express strategic dependence.** The equation for \(\phi_1'\) comes from *bidder 2’s* first-order condition. Its numerator contains bidder 1’s distribution because bidder 2 is trying to outbid bidder 1; its denominator contains \(\phi_2(b)-b\), bidder 2’s surplus at that bid. The second equation reverses these roles.

**Neither equation is generally autonomous.** To determine how quickly bidder 1’s value rises with the common bid, one must know bidder 2’s corresponding value and surplus. A proposed strategy for one bidder changes the opponent’s incentives, which changes the strategy against which the original bidder is optimizing. This is why solving the two bidders separately usually fails.

**The relevant solution stays above bids.** On an active interior region, admissibility requires \(\phi_i(b)>b\), equivalent to positive bid shading by the type submitting \(b\). Given positive \(F_i\) and \(f_i\), the displayed system then implies \(\phi_i'(b)>0\). Thus monotonicity is consistent with the equations, but the admissible region must be respected during computation.

### An equivalent formulation using bid distributions

**The same problem can use quantiles.** Since \(G_i(b)=F_i(\phi_i(b))\), the chain rule gives \(G_i'=f_i(\phi_i)\phi_i'\). The inverse-bid system becomes

\[
G_1'(b)=\frac{G_1(b)}{F_2^{-1}(G_2(b))-b},\qquad G_2'(b)=\frac{G_2(b)}{F_1^{-1}(G_1(b))-b}.
\]

After solving it, recover values from \(\phi_i(b)=F_i^{-1}(G_i(b))\), and recover direct bidding functions by inversion. Gayle and Richard develop a computational approach using precisely this kind of CDF transformation and inverse-CDF representation. [3]

**Uniformizing types does not restore symmetry.** The transformed type \(F_i(V_i)\) is uniform, but a given percentile corresponds to different monetary values through \(F_1^{-1}\) and \(F_2^{-1}\). The asymmetry has moved into the quantile functions; it has not disappeared. The equivalent system makes this visible because both distinct inverse CDFs remain in the equations.

**The representation affects numerical convenience.** A value-based formulation uses \(F_i/f_i\), whereas a bid-distribution formulation uses inverse CDFs. Which is easier depends on how the primitives are supplied—for example, as analytical densities or as smooth tabulated quantiles. Both formulations encode the same equilibrium incentives.

### Why symmetry simplifies the problem

**Symmetry collapses the coupled system.** If \(F_1=F_2=F\), the symmetric equilibrium has \(\phi_1=\phi_2=\phi\). Returning to the direct bidding function then gives a single linear differential equation,

\[
b'(v)=\frac{f(v)}{F(v)}[v-b(v)].
\]

Its solution, with lower value zero and no reserve, is

\[
b(v)=v-\frac{\int_0^v F(t)\,dt}{F(v)}.
\]

The asymmetric problem generally lacks this reduction because the two values submitting a given bid differ. [1]

**The usual shortcut is inconsistent.** It is tempting to apply the symmetric formula separately against each opponent’s value distribution. But that substitutes the opponent’s *value distribution* for the opponent’s *equilibrium bid distribution*, implicitly assuming matching values submit matching bids.

For example, with \(F_1(v)=v\) and \(F_2(v)=v^2\), that shortcut gives \(b_1(v)=2v/3\) and \(b_2(v)=v/2\). Their highest bids are \(2/3\) and \(1/2\), so they fail the common-terminal-bid condition developed next. The calculation identifies the problem without requiring a full numerical solution.

The inverse system is general precisely because it allows the two bidders’ values at a common bid to differ, while solving their mutual incentives simultaneously.

## Boundary conditions, matching, and equilibrium qualifications

### The normalized common-support boundary problem

**Both inverse strategies start at zero.** With support \([0,1]\) for both bidders and reserve zero, the lower conditions are

\[
\phi_1(0)=\phi_2(0)=0.
\]

These express \(b_1(0)=b_2(0)=0\) for the continuous equilibrium representatives. They are boundary conditions, not arbitrary initial values selected by the analyst. [1]

**Both strategies share one highest bid.** There is an endogenous common maximal bid \(\bar b\in(0,1)\) such that

\[
\phi_1(\bar b)=\phi_2(\bar b)=1,
\]

or, equivalently, \(b_1(1)=b_2(1)=\bar b\). In the regular common-support model, the equilibrium bid ranges coincide with \([0,\bar b]\). [2]

**The upper matching condition has economic force.** If one bidder’s highest bid exceeded the opponent’s, sufficiently high types would be paying extra without increasing their winning probability. They could lower their bids while continuing to win. This argument rules out separate top bids and explains why the terminal bid must be determined jointly. [4]

**The unknown endpoint is part of equilibrium.** The domain of the inverse functions is itself endogenous because \(\bar b\) is unknown. Thus the problem is a two-point, free-boundary problem: solve the two ODEs, determine the common right endpoint, and satisfy both lower and upper restrictions.

The lower and upper conditions are not interchangeable. A trajectory can satisfy the local differential equations and approach the lower endpoint correctly while failing to map both highest values to the same bid.

### Why starting at zero is delicate

**The lower endpoint is singular.** At \(b=0\), both \(F_i(\phi_i(b))\) and the surplus terms in the denominators vanish. Consequently, the right-hand side has a \(0/0\)-type structure, and the ordinary local initial-value uniqueness theorem does not apply there. Fibich and Gavish explicitly distinguish the nonunique lower-end initial-value problem from the equilibrium problem with full terminal matching. [1]

**Even initial slopes may not suffice.** If both densities have finite positive limits at zero and the inverse functions have finite right derivatives there, substituting \(\phi_i(b)\sim c_i b\) into the ODEs gives \(c_1=c_2=2\). Thus both bidding functions are locally approximately \(v/2\), despite distributional asymmetry. The corresponding endpoint-slope condition appears in the numerical literature. [2]

**Local similarity does not imply global symmetry.** Sharing the same first-order behavior at zero does not determine the complete curves. Higher-value behavior must also accommodate the distributions and common highest bid. This explains why simply initializing two approximately linear strategies near zero can lead a forward solver toward the wrong trajectory.

### Different supports and reserve prices

**Different upper endpoints can be accommodated.** When both bidders remain active over a common increasing bid range but have upper values \(\overline v_1\) and \(\overline v_2\), the upper conditions become

\[
\phi_1(\bar b)=\overline v_1,\qquad \phi_2(\bar b)=\overline v_2.
\]

The highest bids still match, although the highest values differ. This is the structure used in the asymmetric-uniform example below. [2]

**Different lower endpoints require economic matching.** If one bidder’s smallest possible value exceeds the other’s, some low types may knowingly submit losing bids. The active competitive region must then be identified before applying the interior ODEs; one should not impose the common-origin conditions mechanically. [4]

**A reserve changes the lower boundary.** For a common reserve \(r\) within both supports, the standard common-support active-strategy formulation uses

\[
\phi_1(r)=\phi_2(r)=r.
\]

Types below \(r\) do not make acceptable competitive bids. Importantly, the winning probability for an active bidder still includes the probability that the opponent is below the reserve: one must account for nonparticipation rather than simply replacing the opponent’s distribution by a conditional distribution without adjustment. [6]

**Separated supports show a genuine failure.** Quint presents \(V_W\sim U[0,1]\) and \(V_S\sim U[2,3]\), with equilibrium strategies \(b_W(v)=v\) and \(b_S(v)=1\). The strong bidder’s strategy is constant, so it has no ordinary inverse bidding function. This equilibrium is therefore outside the strictly increasing interior-ODE construction. [4]

The strong bidder’s direct best response makes the mechanism transparent: against the weak bidder’s strategy, a bid \(b\in[0,1]\) yields \((v-b)b\), whose derivative is \(v-2b\ge0\) for \(v\in[2,3]\). Bidding 1 is optimal, and bidding above 1 only raises the payment. Direct optimization handles this case more naturally than an invertible-strategy ODE.

### Existence, uniqueness, and no-overbidding

**Existence is established under regular assumptions.** Results by Lebrun and Maskin–Riley establish monotone pure-strategy equilibrium in the smooth independent-private-values environment. These results justify treating the ODE boundary problem as an equilibrium construction, not merely as an exercise in finding stationary strategies. [5]

**Uniqueness is a qualified statement.** For common-support distributions with continuously differentiable, strictly positive densities, Tumenjargal’s 2026 result establishes uniqueness without requiring lower-end mass points or log-concavity. This strengthens earlier uniqueness conditions and directly supports the clean common-support benchmark. [7]

**No-overbidding defines the standard solution.** The usual admissibility restriction is

\[
0\le b_i(v_i)\le v_i.
\]

An above-value bid that wins generates negative surplus, whereas bidding one’s value avoids that loss. Eliminating weakly dominated above-value bids is therefore natural, and it is important in the uniqueness literature. [8]

**Unrestricted asymmetry can create extra equilibria.** Kaplan and Zamir construct three equilibria for values \(U[0,5]\) and \(U[6,7]\) when above-value bids are permitted. Their additional equilibria contain above-value bids that never win, yet those losing bids alter the opponent’s profitable-deviation opportunities and thereby affect allocation and price. Their paper also shows that this particular nonstandard-equilibrium phenomenon is excluded when bidders share a common lower support bound. [8]

**Admissible solutions have global incentive content.** For an exact solution of the smooth inverse system, the opponent’s bid distribution satisfies \(G_j(b)=[\phi_i(b)-b]g_j(b)\). Hence the payoff derivative of a fixed type \(v\) is

\[
\frac{\partial \pi_i(v,b)}{\partial b}=g_j(b)[v-\phi_i(b)].
\]

Because \(\phi_i\) is increasing, payoff rises below \(b_i(v)\) and falls above it within the active range. Bids above the common maximum cannot improve on the cheapest bid that already wins for sure. This explains why the admissible, correctly matched ODE solution supplies global best responses, not just local stationary points.

The equilibrium characterization is therefore the ODE system **plus** admissibility, endpoint conditions, and the appropriate treatment of active and inactive types.

## Analytical examples and what they establish

### Different uniform intervals: an explicit solution

**Asymmetric uniforms are analytically solvable.** Consider independent \(V_1\sim U[0,u_1]\) and \(V_2\sim U[0,u_2]\), where \(u_1,u_2>0\). Here \(F_i(v)=v/u_i\), so \(F_i(v)/f_i(v)=v\), and the inverse system simplifies to

\[
\phi_1'(b)=\frac{\phi_1(b)}{\phi_2(b)-b},\qquad \phi_2'(b)=\frac{\phi_2(b)}{\phi_1(b)-b}.
\]

This special cancellation permits an analytical reduction. [2]

**An identity determines the terminal bid.** Using the two equations,

\[
\frac{d}{db}\bigl[(\phi_1(b)-b)(\phi_2(b)-b)\bigr]=2b.
\]

The lower conditions imply

\[
(\phi_1(b)-b)(\phi_2(b)-b)=b^2.
\]

At the common maximum, this becomes \((u_1-\bar b)(u_2-\bar b)=\bar b^2\), giving

\[
\bar b=\frac{u_1u_2}{u_1+u_2}.
\]

The endpoint is therefore endogenous but explicitly calculable in this family. [2]

**Both inverse strategies have closed forms.** Define

\[
k_1=\frac{1}{u_1^2}-\frac{1}{u_2^2},\qquad k_2=-k_1.
\]

Then

\[
\phi_i(b)=\frac{2b}{1+k_i b^2},\qquad 0\le b\le\bar b.
\]

These expressions satisfy the coupled equations and map the common terminal bid to the bidder-specific upper values. [2]

**Direct bids follow by inversion.** Solving \(v=2b/(1+k_i b^2)\) for the admissible branch gives

\[
b_i(v)=\frac{v}{1+\sqrt{1-k_i v^2}},\qquad 0\le v\le u_i.
\]

This is an algebraic inversion of the preceding inverse strategy. When \(u_1=u_2\), both \(k_i\) vanish and the formula reduces to \(b(v)=v/2\), the symmetric two-bidder uniform equilibrium.

**The formulas show asymmetric shading.** For \(U[0,1]\) versus \(U[0,2]\), \(k_1=3/4\), \(k_2=-3/4\), and \(\bar b=2/3\). At the same positive value within the shared value range, bidder 1’s denominator is smaller, so bidder 1 bids more aggressively. Nevertheless, the two highest-value types submit the same bid: \(b_1(1)=b_2(2)=2/3\).

This illustrates an important distinction: each bidder’s strategy can be increasing in her own value while the strategies differ across identities. Consequently, the highest realized value need not always generate the highest bid.

**A published benchmark uses larger intervals.** Güth, Ivanova-Stenzel, and Wolfstetter study independent uniforms on \([50,150]\) and \([50,200]\). Subtracting their common lower value gives upper endpoints 100 and 150, so the common highest bid is, by the uniform formula, \(50+(100\times150)/(100+150)=110\), an exact calculation in the model’s monetary units. [9]

**More general uniform supports are covered.** Kaplan and Zamir solve the two-uniform-interval problem analytically with bidder-specific lower and upper endpoints, including a binding minimum bid. Their result establishes substantial analytical generality *within the uniform family*; it does not turn arbitrary asymmetric distributions into the same solvable system. [10]

### Power distributions: tractable structure and exact benchmarks

**Power CDFs simplify the equations.** For

\[
F_1(v)=v^{\alpha_1},\qquad F_2(v)=v^{\alpha_2},\qquad \alpha_1,\alpha_2>0,\quad 0\le v\le1,
\]

one has \(F_i(v)/f_i(v)=v/\alpha_i\). Thus

\[
\phi_1'(b)=\frac{\phi_1(b)}{\alpha_1[\phi_2(b)-b]},\qquad \phi_2'(b)=\frac{\phi_2(b)}{\alpha_2[\phi_1(b)-b]}.
\]

Power-family models are prominent analytical and computational examples; Marshall and coauthors obtain them by treating maxima of independent uniform draws as aggregate bidders. [11]

**Analytical tractability has several forms.** The literature includes explicit solutions for special power-family formulations, as well as analytical relationships between inverse strategies and analytical expressions for their common highest bid. It is useful to distinguish those achievements: an exact endpoint is not, by itself, an explicit elementary expression for every point of both bidding functions. [2]

**The endpoint behavior is informative.** Substituting \(\phi_i(b)\sim c_i b\) into the power-family equations gives

\[
c_1=1+\frac{1}{\alpha_2},\qquad c_2=1+\frac{1}{\alpha_1}.
\]

Therefore the corresponding local direct bids are

\[
b_1(v)\sim\frac{\alpha_2}{1+\alpha_2}v,\qquad b_2(v)\sim\frac{\alpha_1}{1+\alpha_1}v.
\]

These are derived local expressions, not complete global strategies. They also show why the common \(v/2\) lower-end approximation requires positive finite endpoint densities: power densities can vanish or diverge at zero.

**One exact benchmark is especially useful.** For \(F_1(v)=v\) and \(F_2(v)=v^2\), the common maximal bid is

\[
\bar b=\frac{37}{64}=0.578125.
\]

Fibich and Gavish use this analytical endpoint to evaluate their numerical algorithm. It also immediately rejects the separate linear rules \(2v/3\) and \(v/2\), whose terminal bids disagree with each other and with the exact benchmark. [1]

### Generic smooth distributions and small-asymmetry approximations

**Simple CDFs can still require numerics.** A distribution need not be complicated-looking to produce a difficult coupled boundary problem. Hubbard and Paarsch illustrate this with uniform distributions and smooth beta–uniform mixtures, all on \([0,1]\). [2]

For the following cases, bidder 1 has \(F_1(v)=v\). The asymmetric terminal bids are published numerical estimates, rounded here.

| Bidder 2’s CDF | Distributional relationship | Common highest bid |
|---|---|---|
| \(F_2(v)=v\) | Identical distributions | \(0.5\), exact |
| \(F_2(v)=0.1v+0.9v^3\) | Bidder 2 favors higher values | Approximately \(0.6025\) |
| \(F_2(v)=0.1v+0.9(3v^2-2v^3)\) | CDFs cross | Approximately \(0.4976\) |

**Means do not determine equilibrium bids.** In the third example, both value distributions have mean \(1/2\), yet the common highest bid differs from the symmetric value \(1/2\). The equilibrium depends on how probability mass is distributed across values and how that distribution affects strategic shading—not merely on the means.

**Small asymmetry offers an approximation route.** Fibich and Gavious develop perturbation methods around a symmetric distribution. Writing \(F_{\mathrm{avg}}=(F_1+F_2)/2\) and \(F_i=F_{\mathrm{avg}}+\epsilon A_i\), the bidding functions can be approximated schematically as

\[
b_i(v)=b_{\mathrm{sym}}(v)+\epsilon\,d_i(v)+O(\epsilon^2).
\]

The correction \(d_i\) depends on the distributional perturbation. This can yield useful comparative insights and starting values for numerical solvers, but it remains an approximation whose usefulness depends on the size and structure of asymmetry. [2]

The practical judgment is to exploit a documented analytical family when it applies, use analytical solutions as benchmarks, and otherwise solve the coupled boundary problem numerically.

## Computing the equilibrium

### Comparing the main numerical approaches

**Three approaches solve related finite problems.** Shooting repeatedly integrates the ODEs from a guessed endpoint; transformed boundary-value methods solve for whole curves on a fixed domain; projection methods approximate the curves by basis functions and choose their coefficients. These approaches are compared directly in the numerical-auction literature. [2]

| Approach | Main unknowns | Endpoint treatment | Typical attraction |
|---|---|---|---|
| Backward shooting | Terminal bid and ODE trajectory | Adjust terminal bid to match the bottom | Direct use of inverse ODEs |
| Transformed boundary-value solving | Matching-value and bid curves | Fixed value domain; terminal bid recovered | Avoids unstable backward propagation |
| Projection or collocation | Curve coefficients and terminal bid | Explicit constraints or residual terms | Flexible finite-dimensional approximation |

**A fixed-domain boundary formulation is attractive.** It addresses both the unknown terminal bid and the instability associated with integrating backward toward the singular lower endpoint. Projection is also useful, particularly for repeated solutions, provided shape constraints and incentive checks discipline the approximation.

This is a method-selection judgment, not a universal speed ranking. Distributional shape, endpoint behavior, approximation order, and the required accuracy all matter.

### Backward shooting

**Shooting searches for the common endpoint.** Begin with a trial highest bid \(B\), impose \(\phi_1(B)=\phi_2(B)=1\), and integrate the inverse ODEs backward. Then adjust \(B\) according to whether the resulting trajectory approaches the correct lower endpoint while remaining admissible. This is the basic construction used by Marshall and coauthors and subsequent algorithms. [11]

**The integration method is a component.** Runge–Kutta methods, adaptive integration, and local Taylor expansions have all been used inside shooting procedures. Gayle and Richard construct sequences of local polynomial approximations and search for the terminal endpoint by matching the lower conditions. [3]

**Endpoint misses carry economic information.** A trial endpoint that is too low can produce inverse curves that reach bid zero at positive values. A trial endpoint that is too high can push a curve toward \(\phi_i(b)=b\), where the surplus denominator vanishes and the inverse system becomes singular. These behaviors can support bracketing and adjustment of the terminal bid. [2]

**Backward instability is not just integration error.** Fibich and Gavish show that small errors in the terminal bid can grow severely as one integrates toward the bottom. In the symmetric two-bidder case, their analytical calculation specializes to

\[
b_\epsilon(v)-b(v)=\frac{\epsilon}{F(v)},
\]

where \(\epsilon\) is the error in the terminal bid. As \(F(v)\) approaches zero, even a small endpoint error is amplified. [1]

**Changing the ODE solver is insufficient.** A more accurate integrator can reduce discretization error, but it does not remove this sensitivity of the underlying backward solution. Numerical integration can also continue past a singular point and generate smooth-looking artifacts. Monotonicity and surplus constraints should therefore be checked throughout the trajectory, not merely at termination. [1]

Shooting remains a useful construction, especially with careful endpoint handling, but its lower-end sensitivity is a substantive reason to consider a boundary-value alternative.

### A fixed-domain boundary-value formulation

**Use one bidder’s value as the coordinate.** Let \(x\in[0,1]\) denote bidder 2’s value, and define

\[
p(x)=b_2(x),\qquad h(x)=\phi_1(p(x)).
\]

Thus \(h(x)\) is the bidder 1 value submitting the same bid as bidder 2 type \(x\). The identities are \(b_1(h(x))=p(x)=b_2(x)\). This change of variables replaces the unknown bid domain by the known value interval. [1]

**The transformed equations follow by differentiation.** Since \(\phi_2(p(x))=x\), the inverse-function rule and the original ODEs give

\[
p'(x)=\frac{f_2(x)}{F_2(x)}[h(x)-p(x)],
\]

\[
h'(x)=\frac{F_1(h(x))f_2(x)}{f_1(h(x))F_2(x)}\frac{h(x)-p(x)}{x-p(x)}.
\]

The boundary conditions are

\[
h(0)=0,\qquad p(0)=0,\qquad h(1)=1.
\]

The common highest bid is recovered afterward as \(\bar b=p(1)\). [1]

**The terminal bid becomes an output.** There is no need to supply \(p(1)\) as a known boundary value. Instead, solve for the matching function \(h\) and bidder 2’s bid function \(p\), and let the upper bid emerge from the solution. Bidder 1’s direct strategy is recovered from the increasing pairs \((h(x),p(x))\).

**The lower singularity still needs treatment.** The transformation fixes the domain and avoids backward propagation from a guessed terminal bid; it does not turn the lower endpoint into a regular initial-value problem. A numerical implementation uses appropriate limits, local approximations, or an interior mesh near zero. The extra endpoint restriction is meaningful precisely because this is a singular boundary problem.

**Nonlinear iteration solves the discretized equations.** Fibich and Gavish implement both fixed-point and Newton iterations. Fixed-point methods update candidate curves through simpler equations; Newton methods solve a linearized correction problem using the residuals and their derivatives. The choice of which bidder’s value serves as the coordinate can affect the behavior of a particular iteration scheme. [1]

**Their benchmark separates two error sources.** For \(F_1(v)=v\), \(F_2(v)=v^2\), the reported terminal-bid error falls to approximately \(8.5\times10^{-10}\) after 25 fixed-point iterations or 5 Newton iterations. Both methods reach the same error floor on the same discretization, illustrating that additional nonlinear iterations do not eliminate mesh error. [1]

The fixed-domain method changes how equilibrium is computed, while preserving the original joint incentives and endpoint matching.

### Discretization, interpolation, and projection

**Distributional inputs can be represented numerically.** Gayle and Richard describe constructing an equally spaced probability grid, evaluating \(F_i^{-1}\) at those probabilities, fitting B-splines, and converting the interpolant into piecewise polynomials. This permits smooth tabulated distributions to enter the equilibrium calculation without requiring simple analytical inverse CDFs. [3]

**Quantile grids resolve probability mass differently.** Equal increments of probability generally correspond to unequal increments of value. Such grids can allocate more value-space points where the density is high, while adaptive meshes can separately target sharp changes in the equilibrium curves. Low-density regions deserve attention because value-based equations contain \(F_i/f_i\), and inverse CDFs change rapidly there.

**Projection replaces functions by coefficients.** For example, approximate

\[
\widehat\phi_i(b)=\sum_{k=0}^{K}a_{ik}P_k(b/\bar b),
\]

where the \(P_k\) are chosen basis functions. The unknowns are the coefficients and \(\bar b\). Collocation imposes the equations at selected points; least-squares projection minimizes a norm of their residuals, with boundary conditions imposed explicitly or incorporated into the objective. [2]

**Economic restrictions improve the approximation.** Candidate inverse curves should be increasing, stay within the relevant value supports, satisfy \(\widehat\phi_i(b)\ge b\), and meet the endpoint conditions. The literature uses constraints based on equilibrium theory to prevent polynomial approximations from achieving a low residual by taking economically inadmissible shapes. [2]

**Refinement must be judged by outputs.** Increasing polynomial order or mesh density can improve accuracy, but numerical conditioning and endpoint effects can interfere. A small average residual can conceal a substantial error on a narrow region. Consequently, inspect endpoint errors, maximum residuals, and incentive errors as well as the average fit.

### Verifying that computed bids are equilibrium bids

**Start with structural admissibility checks.** For the baseline model, verify increasing bidding functions, nonnegative bids, no overbidding, and common highest bids. In inverse coordinates, check positive slopes and \(\widehat\phi_i(b)>b\) on the active interior. Also inspect convergence toward the lower endpoint rather than accepting an arbitrary truncation as part of the original model. [1]

**Crossing is not a monotonicity violation.** The curves \(b_1(v)\) and \(b_2(v)\) can cross even though each is increasing in its own value. What conflicts with the baseline equilibrium is a decrease in an individual bidder’s active bidding function, not a reversal of the ordering between two different bidders’ functions.

**Check incentives independently of residuals.** Given candidate strategies \(\widehat b_i\) and their induced bid CDFs \(\widehat G_i\), calculate each type’s best-response gain,

\[
\Delta_i(v)=\max_{0\le b\le v}(v-b)\widehat G_j(b)-(v-\widehat b_i(v))\widehat G_j(\widehat b_i(v)),\qquad j\ne i.
\]

The maximization includes the prescribed bid when the candidate is admissible, so \(\Delta_i(v)\ge0\). Exact equilibrium requires zero gain; numerical equilibrium assessment asks how large those gains are. Gayle and Richard recommend pointwise best-response comparisons as an accuracy check. [3]

**Utility errors are the relevant metric.** A difference between a computed bid and a best-response bid measures strategy error, whereas \(\Delta_i(v)\) measures the incentive to deviate. Neither a small bid discrepancy nor a small ODE residual automatically supplies a bound on utility gain without additional regularity and numerical error control.

**Interim and ex-ante guarantees differ.** An ex-interim error bound controls every type, while an ex-ante bound averages over the bidder’s own value distribution. In this model, the natural quantities are

\[
\epsilon_{\mathrm{interim}}=\max_i\sup_{v\in[0,1]}\Delta_i(v),\qquad \epsilon_{\mathrm{ante}}=\max_i\int_0^1\Delta_i(v)f_i(v)\,dv.
\]

The first bounds the second, but a small average gain can coexist with a larger gain for rare types. This distinction is central to approximate-equilibrium verification. [12]

**A grid search needs interpolation control.** Searching deviations on a finite bid grid finds profitable deviations that the grid captures. A formal upper bound on the best possible deviation additionally needs control of missed bids, interpolation, and any sampling error. Refining the grid is useful evidence, but it is not the same as an analytical error bound. [12]

**A compact solving sequence follows.**

1. **Specify the economic primitives.** Record \(F_1,F_2\), supports, utility, reserve, and tie-breaking; identify the active competitive region.
2. **Construct the equilibrium equations.** Use inverse values or bid distributions to derive the coupled system.
3. **Impose the correct matching conditions.** Include the lower behavior and common maximal bid, treating that bid as endogenous.
4. **Compute candidate strategies.** Use a transformed boundary solver, carefully controlled shooting, or a constrained projection method.
5. **Quantify equilibrium accuracy.** Report endpoint and equation residuals, shape checks, profitable-deviation gains, and sensitivity to mesh or tolerance changes.

The decisive computational standard is that both strategies are mutual best responses to the required accuracy—not merely that an equation solver has stopped.

## What changes outside the baseline?

**Different departures break different steps.** Some alter the first-order condition while preserving an inverse-ODE approach; others remove differentiability or invertibility and require a different equilibrium representation.

| Model change | Affected ingredient | Appropriate adjustment |
|---|---|---|
| Discrete values | Smooth density-based characterization | Direct discrete-value equilibrium method |
| Correlated values | Marginal-distribution winning probability | Conditional beliefs and revised equations |
| Risk aversion | Linear surplus objective | Utility-specific first-order conditions |
| Density zeros or support gaps | Regular ODE coefficients | Piecewise treatment or adapted numerics |
| Pooling or nonmonotone bids | Single-valued inverse strategy | Direct bid distributions or mixed strategies |
| Unequal lower supports | Common-origin matching | Identify active types and match regions |

### Discrete values and ties

**Atoms change the optimization problem.** If values have mass points, the continuous density-based derivation no longer applies directly. Strategies can produce bid atoms, and a bidder may care discontinuously about tying or slightly outbidding an opponent. Shen develops a separate characterization and algorithm for asymmetric independent private values with discrete distributions, reporting existence and uniqueness in that setting without solving ODEs. [13]

**Winning probabilities must include ties explicitly.** If the opponent’s bid CDF is \(H_j\), and bidder \(i\) wins a tie at bid \(b\) with probability \(\theta_i(b)\), then her payoff is

\[
(v-b)\left[H_j(b^-)+\theta_i(b)\bigl(H_j(b)-H_j(b^-)\bigr)\right].
\]

This expression remains meaningful when a smooth inverse cutoff does not. With fair tie-breaking between two bidders, \(\theta_i=1/2\).

**Discrete values do not imply discrete bids.** A discrete type may randomize over a continuum of bids; restricting bids to a finite grid is an additional modeling or approximation choice. Similarly, smoothing a discrete distribution into a continuous one changes the game unless the resulting approximation error is controlled. The auction-existence literature gives examples showing that finite and continuum action spaces can have different equilibrium properties. [14]

The appropriate conclusion is to use a discrete-value equilibrium method, not to insert a step CDF into equations that divide by a density.

### Correlated private values

**Conditional beliefs replace marginal beliefs.** With correlation, bidder \(i\)’s value informs her about bidder \(j\)’s value. If increasing strategies still exist, the winning probability becomes

\[
W_i(b\mid v_i)=F_{j\mid i}(\phi_j(b)\mid v_i),
\]

rather than \(F_j(\phi_j(b))\). Holding the bidder’s own type fixed when differentiating, the corresponding interior inverse condition is

\[
\phi_j'(b)=\frac{F_{j\mid i}(\phi_j(b)\mid\phi_i(b))}{f_{j\mid i}(\phi_j(b)\mid\phi_i(b))[\phi_i(b)-b]},\qquad j\ne i.
\]

This is the conditional-belief counterpart of the independent-values equation.

**Some correlated models remain tractable.** Under suitable dependence and monotonicity conditions, conditional equations can still be solved numerically. Hubbard and Paarsch discuss asymmetric affiliated-private-values examples, illustrating that correlation does not automatically eliminate a monotone equilibrium construction. [2]

**General correlation can defeat monotone purity.** Jackson and Swinkels give a two-player first-price auction with values uniformly distributed over the triangle \(v_1\ge0\), \(v_2\ge0\), \(v_1+v_2\le1\). It has no nondecreasing pure-strategy equilibrium. Their broader existence framework uses distributional strategies and can therefore cover settings in which the simple monotone inverse representation fails. [14]

**The envelope shortcut also changes.** Under independence, the bidder’s own value changes surplus but not her beliefs about the opponent. Under correlation, it changes both. Therefore the simple identity \(U_i'(v)=q_i(v)\) generally acquires additional belief effects and should not be carried over mechanically.

The conditional-distribution formulation is the right extension when monotone strategies survive; otherwise the equilibrium object must be broadened.

### Risk aversion

**Nonlinear utility changes the marginal trade-off.** Suppose bidder \(i\)’s utility from winning surplus \(s\) is \(u_i(s)\), with \(u_i(0)=0\) and \(u_i'>0\). Her expected utility is \(u_i(v_i-b)G_j(b)\), and an interior optimum satisfies

\[
-u_i'(v_i-b)G_j(b)+u_i(v_i-b)g_j(b)=0.
\]

Equivalently,

\[
\frac{g_j(b)}{G_j(b)}=\frac{u_i'(v_i-b)}{u_i(v_i-b)}.
\]

The risk-neutral condition is recovered by taking \(u_i(s)=s\). [2]

**Inverse ODEs can be modified accordingly.** On a strictly increasing equilibrium branch,

\[
\phi_j'(b)=\frac{F_j(\phi_j(b))}{f_j(\phi_j(b))}\frac{u_i'(\phi_i(b)-b)}{u_i(\phi_i(b)-b)},\qquad j\ne i.
\]

For power utility \(u_i(s)=s^{\rho_i}\), the utility ratio is \(\rho_i/s\). Thus the opponent’s utility parameter enters the equation for a bidder’s inverse strategy, just as the opponent’s surplus enters under risk neutrality.

**Monotonicity needs preference conditions.** Suitable single-crossing utility assumptions support extensions beyond risk neutrality, and Tumenjargal explicitly extends the uniqueness argument to single-crossing preferences. This is a structured extension, not a claim covering every possible nonlinear preference specification. [7]

The inverse-strategy method can survive risk aversion, but the risk-neutral ODEs must be replaced by utility-specific equations.

### Irregular distributions and noninvertible strategies

**Density irregularity is a numerical issue.** Very small densities make \(F_i/f_i\) large; density zeros or gaps can require a different local representation or piecewise treatment. Gayle and Richard specifically identify distributions whose densities approach zero as cases requiring additional numerical attention, including finer or adaptive steps. [3]

**Distributional crossings are a different issue.** CDFs that cross need not violate positivity or differentiability. They can still be handled by the same coupled system, but simple global rankings such as “bidder 1 always shades more” may cease to hold. Numerical examples demonstrate crossing bid strategies once stochastic-dominance restrictions are removed. [1]

**Revenue-theoretic irregularity is not the criterion.** The displayed equilibrium equations do not require a monotone virtual-value function or a global strong-versus-weak ordering. The relevant requirements are those used in the derivation: appropriate densities, supports, preferences, and increasing strategies. Failure of a convenient comparative-statics ordering should not be confused with failure of the general construction.

**Pooling prevents an ordinary inverse.** If a positive range of values submits the same bid, multiple values correspond to that bid. A genuinely nonmonotone strategy likewise lacks the single-valued increasing inverse required by the ODE system. In either case, return to the direct expected-payoff problem using the opponent’s induced bid distribution, with tie probabilities included when necessary.

**Broader algorithms use distributional strategies.** Methods that discretize type and action spaces and optimize over distributional strategies avoid imposing a particular bid-function shape. Their conclusions concern approximate equilibrium and require attention to convergence and abstraction error; they are not replacements for the exact smooth characterization when its assumptions apply. [15]

The governing distinction is between an unusual relationship *between* two increasing strategies, which the baseline method can handle, and a failure of individual invertibility, which changes the method itself.

## The practical conclusion

**The solution method is general but conditional.** For two regular independent-private-value bidders, solve the coupled inverse-strategy boundary-value problem, recover the direct bidding functions, and check their incentive properties. Use analytical uniform and power-family results where applicable; use a numerically controlled boundary or projection method for other distributions.

**The evidence has a defined scope.** Values and bids use the same monetary units; examples on \([0,1]\) are normalized, while the \([50,150]\) and \([50,200]\) example uses its stated model units. The uniform calculations and \(37/64\) endpoint are exact analytical results; mixture-example decimals and solver errors are published numerical approximations. Existence and uniqueness apply to the indicated equilibrium classes and assumptions, while reported algorithmic performance is case-specific—Fibich and Gavish do not claim a general convergence proof for their iterations. [1]

**The answer is therefore affirmative.** Ex-ante asymmetry removes the usual one-function symmetric formula, but it does not remove a systematic way to characterize and compute equilibrium.

## References

[1] <https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf> Fibich and Gavish’s boundary-value formulation; Fibich and Gavish’s model; Fibich and Gavish, equation 19; Fibich and Gavish’s symmetric comparison; Fibich and…
[2] <https://www.carloalberto.org/wp-content/uploads/2018/11/no.291.pdf> Hubbard and Paarsch’s survey; Hubbard and Paarsch’s two-bidder derivation; Common bid support and terminal matching; Hubbard and Paarsch’s endpoint discussion;…
[3] <https://people.umass.edu/wayneroy/Auctions.pdf> Gayle and Richard’s IPV formulation; Gayle and Richard’s baseline model; Distributional assumptions; Their transformed equations; Their Taylor-series algorithm…
[4] <https://users.ssc.wisc.edu/~dquint/econ805%202007/econ%20805%20lecture%209.pdf> Quint’s asymmetric-auction notes; Quint’s two-bidder formulation; Quint’s first-order conditions; Quint’s endpoint argument; Quint’s discussion of unequal lowe…
[5] <https://brocku.ca/repec/pdf/0504.pdf> Kirkegaard’s model and equilibrium properties; Winning probabilities and the envelope theorem; Kirkegaard’s summary of existence and regularity
[6] <http://www.econ.ucla.edu/riley/201C/2017/AuctionsIV.pdf> Riley’s inverse-strategy derivation; Riley’s logarithmic-payoff argument; Riley’s reserve matching condition
[7] <https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369> Tumenjargal’s uniqueness theorem; Single-crossing uniqueness extension
[8] <http://www.ma.huji.ac.il/~zamir/Kaplan-Zamir_ET-Bull_2014.pdf> Kaplan and Zamir on the restriction; Multiple equilibria and the common-lower-bound result
[9] <https://www.sciencedirect.com/science/article/abs/pii/S0014292104000753> Their valuation intervals
[10] <https://link.springer.com/article/10.1007/s00199-010-0563-9> Kaplan and Zamir’s analytical solution
[11] <https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf> Their power-distribution model; Backward shooting and endpoint search
[12] <https://arxiv.org/html/2408.11445> Verifying Approximate Equilibrium in Auctions; Finite-search verification guarantees
[13] <https://doi.org/10.48550/arxiv.1906.09403> Shen’s discrete-value method
[14] <https://kylewoodward.com/blog-data/pdfs/references/jackson+swinkels-econometrica-2005A.pdf> Jackson and Swinkels on discretization; The correlated triangular-support example
[15] <https://doi.org/10.48550/arxiv.2208.02036> Distributional-strategy computation
