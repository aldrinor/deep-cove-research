# Solving the Asymmetric Two-Bidder First-Price Auction (Independent Private Values): Framework, Closed Forms, and Numerical Recipe

Yes, there is a general method: write each bidder’s first-order condition in terms of the opponent’s inverse bid function, which gives a coupled pair of nonlinear first-order ODEs. Then solve that pair as a free-boundary, two-point boundary-value problem: both bids are pinned at a common low bid and a common, unknown high bid b̄. Existence and uniqueness are settled under mild regularity conditions (Lebrun 1999/2006, Maskin–Riley 2000/2003). [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf) Closed forms exist only in special families, and everything else needs numerical solution. [uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)

## TL;DR

- **Method:**  with φ_i = b_i⁻¹, the equilibrium solves φ_j′(b) = F_j(φ_j(b)) / [f_j(φ_j(b))·(φ_i(b) − b)] for i ≠ j. The conditions are φ_i(b̲) = (known low-end values) and φ_1(b̄) = b̄_1-value = ω_1, φ_2(b̄) = ω_2, with b̄ found as part of the solution. Under Lebrun’s (2006) conditions, for example strict log-concavity of the CDFs just above the highest lower support endpoint, the equilibrium is unique.
- **Closed forms are rare.**  The canonical one is Griesmer–Levitan–Shubik (1967) for U[0,ω_1] vs U[0,ω_2]: φ_i(b) = 2b/(1 + k_i b²), with k_i = 1/ω_i² − 1/ω_j² and b̄ = ω_1ω_2/(ω_1+ω_2). Kaplan–Zamir (2012) solve every uniform pair, including different lower endpoints and a minimum bid. Plum (1992) covers power distributions, and Cheng (2006) gives a linear-bid power family.
- **In practice, use a stable solver.**  Backward shooting from b̄ (Marshall et al. 1994) is, in Fibich and Gavish’s (2011) words, the method that “has become the standard method,” used in numerous subsequent studies including Maskin–Riley (2000) and Li–Riley (2007), but it is analytically unstable near the low end. Fibich–Gavish’s (2011) boundary-value method is more robust: by their account it “performs well even when the number of players is large,” including for Weibull, truncated normal, beta and multiply-crossing distributions; Chebyshev/projection methods (Hubbard–Kirkegaard–Paarsch 2013) are another option. Validate any solver against the uniform closed form before using it on your own distributions.

## Key Findings

1. **The system.**  Bidder i’s FOC involves only the opponent’s distribution and inverse bid. In equilibrium the two FOCs couple: φ_1 appears in bidder 2’s equation through the denominator, and vice versa.
2. **Boundary conditions are the crux.**  The top bid is common to both bidders and endogenous. At the bottom, the system is singular (0/0) when supports share a lower endpoint without atoms. [uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf) That is why forward integration from the bottom does not pin down the solution and backward integration from the top is unstable; as Li and Riley put it, the equations “are very poorly behaved at the lower end-point.”
3. **Theory guarantees a well-posed target.**
    - Existence: Lebrun (1996, 1999); Maskin–Riley (2000b). [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - Uniqueness: Lebrun (1999) with atoms at the common lower endpoint; Maskin–Riley (2003) with positive mass at the lower endpoint; Lebrun (2006) with local strict log-concavity at the highest lower endpoint, or a strictly highest lower endpoint, or a binding reserve. [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf)[ias](https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf)
4. **Economics.**  Under conditional stochastic dominance the strong bidder shades more and the weak bidder bids more aggressively (Maskin–Riley 2000a). The auction is therefore inefficient, and revenue equivalence with the second-price/English auction fails. [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF) In the uniform [0,1] vs [0,2] example, by my calculation, first-price revenue is ≈0.459 versus 5/12 ≈ 0.417 for the second-price auction.

## Details

### 1. Model and the coupled ODE system

**Setup.**

- Bidder i ∈ {1,2} has value v_i ~ F_i on [a_i, ω_i], with density f_i > 0 on (a_i, ω_i]. Values are independent; bidders are risk neutral.
- Strategies b_i(·) are strictly increasing on the relevant range, with inverses φ_i(b) = b_i⁻¹(b).

**First-order conditions.**  Bidder i with value v who bids b wins if b_j(v_j) < b, i.e., if v_j < φ_j(b). He therefore solves

max_b (v − b)·F_j(φ_j(b)).

The FOC is −F_j(φ_j(b)) + (v − b) f_j(φ_j(b)) φ_j′(b) = 0. Impose consistency, v = φ_i(b): in equilibrium the bidder who submits b has value φ_i(b). This gives

**φ_j′(b) = F_j(φ_j(b)) / [ f_j(φ_j(b)) · (φ_i(b) − b) ], i ≠ j,**

that is,

φ_1′(b) = F_1(φ_1(b)) / [f_1(φ_1(b))·(φ_2(b) − b)], φ_2′(b) = F_2(φ_2(b)) / [f_2(φ_2(b))·(φ_1(b) − b)].

Bookkeeping trap: the equation for φ_1′ comes from bidder 2’s optimization. It contains bidder 1’s own distribution (the reverse hazard ratio F_1/f_1) and bidder 2’s markup (φ_2 − b) in the denominator. Hubbard and Paarsch’s survey writes exactly this pair, dφ_2/ds = F_2[φ_2]/([φ_1 − s] f_2[φ_2]) and symmetrically. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf) Fibich–Gavish write the same thing for n = 2 as dv_1/db = (F_1/f_1)·1/(v_2 − b). [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)

**Equivalent “Lebrun” form.**  Let G_i(b) = F_i(φ_i(b)) be the distribution of bidder i’s bid. Then bidder j’s FOC is simply

d/db ln G_i(b) = 1/(φ_j(b) − b).

For n bidders, Lebrun (1999) writes d/db ln F_i(α_i(b)) = (1/(n−1)){−(n−2)/(α_i − b) + Σ_{j≠i} 1/(α_j − b)}. He then works with ψ_i = F_i∘α_i as the unknowns, which makes the system regular away from the bottom. [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf) The general n-bidder form is

φ_i′(b) = [F_i(φ_i)/f_i(φ_i)]·[ (1/(n−1)) Σ_m 1/(φ_m − b) − 1/(φ_i − b) ]. [uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)

With n = 2 this reduces to the pair above.

### 2. Boundary conditions and why the top bid is common

**Common top bid b̄.**  Suppose b̄_i > b̄_j. Then bidder i’s highest types win with probability one at any bid in (b̄_j, b̄_i]. They could cut their bid toward b̄_j without lowering the win probability, which contradicts optimality. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf) Hence b_1(ω_1) = b_2(ω_2) = b̄, i.e., φ_1(b̄) = ω_1 and φ_2(b̄) = ω_2. As Hubbard and Paarsch put it, “No bidder will submit a bid that exceeds the highest bid chosen by all other players because the bidder could strictly decrease the bid by some small amount ε and still win the auction with certainty.” [uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)

Kaplan–Zamir prove the analogous statement for the bottom of the winning-bid interval (their Lemma 2): the interval of bids with positive win probability is the same for both buyers. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf) b̄ is unknown a priori, so this is a free-boundary problem with more boundary conditions than equations (2N conditions for N ODEs). [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)

**Low end, common lower endpoint a (no atom, no binding reserve).**  φ_1(a) = φ_2(a) = a. Every term in the system becomes 0/0 there, so the right-hand side is not Lipschitz and Picard–Lindelöf fails. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf) Fibich and Gavish note that “the initial value problem … does not have a unique solution.” The bottom condition alone admits a continuum of solutions, and the top condition selects one. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)

**Low end, different lower endpoints (a_1 < a_2, bidder 2 has the higher floor).**

- The lowest winning bid b̲ lies in [a_1, a_2].
- Types of bidder 1 below b̲ cannot win. By the standard convention they bid their value, which delivers the same allocation. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)
- Bidder 2’s lowest type best-responds to that behavior: b̲ ∈ argmax_b F_1(b)(a_2 − b). This is Maskin–Riley (2003), Lemma 3, eq. (2.2) in two-bidder form. [ias](https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf)
- The boundary conditions become φ_1(b̲) = b̲ and φ_2(b̲) = a_2. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)
- In the uniform case this gives b̲ = (a_1 + a_2)/2 (Kaplan–Zamir, eq. 2, with a minimum bid m: b̲ = max{(a_1+a_2)/2, m}). [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)
- **Extreme case (the “Getty effect”).**  If the strong bidder’s floor is high enough, she bids the weak bidder’s maximum and always wins. In the uniform case this happens when a_2 ≥ 2ω_1 − a_1. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf) Maskin–Riley’s Example 1 is U[0,1] vs U[2,3]: [isid](https://www.isid.ac.in/~dmishra/topicsdoc/maskin_riley.pdf) the strong bidder bids 1 and revenue is 1, versus E[v_w] = 1/2 in the open auction. [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF)

**Reserve price r.**  The marginal type bids r, so φ_i(r) = r for bidders whose support extends below r. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf) A binding reserve acts like an atom at the bottom. This is exactly the case in which Lebrun’s (1999) and Maskin–Riley’s (2003) mass-point uniqueness theorems apply. [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf)[ias](https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf)

### 3. Existence and uniqueness results

- **Plum (1992, IJGT 20(4):393–418).**  Two bidders, values independent on intervals. [springer](https://link.springer.com/10.1007/BF01271133) For pay-your-bid formats, equilibria are C¹ and strictly increasing and are characterized by “a boundary value problem for a system of singular differential equations.” [springer](https://link.springer.com/10.1007/BF01271133) Plum also computes closed forms for power distributions.
- **Lebrun (1996, Economic Theory 7(3):421–443; 1999, IER 40(1):125–142).**  Existence for n bidders. Characterization: there is η ∈ (c, d) such that the inverse bids solve the ODE system with α_i(c) = c “for all, except possibly one, i” and α_1(η) = … = α_n(η) = d. Uniqueness when every distribution has a mass point at the common lower endpoint, and also in the symmetric case and for a stochastically ranked pair. The key tool is strict monotonicity in η (his Lemma 2): if η < η̃, the backward solutions satisfy α̃_i(b) < α_i(b) everywhere. [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf) This monotonicity is what justifies bisection on b̄.
- **Maskin & Riley (2000b, RES 67(3):439–454).**  Existence of equilibrium in sealed high-bid auctions with asymmetric bidders. The winning-bid distribution has interval support and is continuous; best responses are monotone. [researchgate](https://www.researchgate.net/publication/4783378_Equilibrium_in_Sealed_High_Bid_Auctions)[ias](https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf)
- **Maskin & Riley (2003, GEB 45(2):395–409).**  Uniqueness when values have finite support and positive mass at the lower endpoint. For two buyers no symmetry is needed; for more than two they add mild conditions, such as a common upper endpoint. They note the mass-point assumption “is satisfied automatically if the seller sets a reserve price that is even marginally above the lowest possible buyer reservation price.” [ias](https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf)
- **Lebrun (2006, GEB 55(1):131–151), Theorem 1.**  Let supports be intervals [c_i, d_i], with F_i differentiable and density locally bounded away from zero, F_i(c_i) = 0, and order the lower endpoints c_1 ≥ c_2 ≥ c_i. The equilibrium in which bidders bid at most their values is unique under any one of three conditions:
    - (i) the reserve exceeds the highest lower endpoint, r > c_1;
    - (ii) the highest lower endpoint is strictly highest, c_1 > c_2;
    - (iii) each F_i is strictly log-concave (i.e., f_i/F_i strictly decreasing) on some interval just to the right of c_1. [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf)
  Upper endpoints may differ. Since many commonly used distributions have log-concave CDFs (Bagnoli and Bergstrom 2005, Economic Theory 26:445–469, catalogue them), (iii) is the workhorse condition.
- **Caution.**  Kaplan and Zamir later published “Multiple equilibria in asymmetric first-price auctions” (Economic Theory Bulletin 3:65–77, 2015), showing that the Maskin–Riley/Lebrun uniqueness results require the assumption that a buyer never bids above his value, and that dropping it yields additional, substantial equilibria with higher revenue. Uniqueness is a theorem under conditions like those above, not a universal fact. If you work with exotic distributions, check that the conditions hold.

### 4. Closed-form special cases

**(a) Griesmer–Levitan–Shubik (1967, Naval Research Logistics Quarterly 14(4)): U[0, ω_1] vs U[0, ω_2].**

Here F_i/f_i = v. The trick is to subtract 1 from each ODE and add the two:

d/db {[φ_1(b) − b][φ_2(b) − b]} = 2b, hence [φ_1(b) − b][φ_2(b) − b] = b² (using φ_i(0) = 0).

Evaluating at b̄ gives (ω_1 − b̄)(ω_2 − b̄) = b̄², so

**b̄ = ω_1ω_2 / (ω_1 + ω_2).**

Substituting back decouples the system. With φ_i − b = bψ_i, one gets ψ_i′ = (ψ_i² − 1)/b, and so

**φ_i(b) = 2b / (1 + k_i b²), k_1 = 1/ω_1² − 1/ω_2², k_2 = 1/ω_2² − 1/ω_1² = −k_1.**

Inverting gives the bid functions:

**b_i(v) = [1 − √(1 − k_i v²)] / (k_i v)** , which reduces to v/2 as k_i → 0.

I checked these formulas against two independent sources:

- **Hubbard–Paarsch survey.**  It gives φ_1(s) = 2s/(1+k_1s²) with k_1 = 1/v̄_1² − 1/v̄_2², and s̄ = v̄_1v̄_2/(v̄_1+v̄_2), derived “following Krishna.” [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)
- **Kaplan–Zamir eq. (1),**  normalized to U[0,1] vs U[0,β]: v_1(b) = 2bβ²/(β² − b²(1−β²)) and v_2(b) = 2bβ²/(β² + b²(1−β²)), which is algebraically identical. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)

This is the example Krishna works in *Auction Theory*  (Ch. 4, asymmetric auctions; cited elsewhere as Section 4.3 of the first edition). I could not verify the exact example number or page in the 2nd edition.

**Worked example: U[0,1] (weak, bidder 1) vs U[0,2] (strong, bidder 2).**

- Parameters: k_1 = 3/4, k_2 = −3/4, b̄ = 2/3.
- Inverse bids: φ_1(b) = 8b/(4 + 3b²) and φ_2(b) = 8b/(4 − 3b²). Check: φ_1(2/3) = 1 and φ_2(2/3) = 2.
- Bids: b_1(v) = (2/(3v))(2 − √(4 − 3v²)) and b_2(v) = (2/(3v))(√(4 + 3v²) − 2).

| value v | weak b_1(v) | strong b_2(v) | symmetric benchmark v/2 |
| --- | --- | --- | --- |
| 0.5 | 0.263 | 0.239 | 0.25 |
| 1.0 | 0.667 (= b̄) | 0.430 | 0.50 |
| 2.0 | — | 0.667 (= b̄) | 1.00 |

What the table shows:

- **Weak aggression, strong shading.**  At equal values the weak bidder bids more, and the strong bidder shades below the symmetric v/2.
- **Inefficiency.**  A weak bidder with v_1 = 0.5 bids 0.263, which beats strong types up to φ_2(0.263) ≈ 0.555. A weak bidder with v_1 = 0.95 bids ≈ 0.606, which beats strong types up to ≈ 1.67.
- **Revenue (my calculation).**  The winning bid has CDF G(b) = F_1(φ_1)F_2(φ_2) = 32b²/(16 − 9b⁴) on [0, 2/3], so E[revenue] = 2/3 − ∫₀^{2/3} G ≈ 0.459. The second-price auction yields E[min(v_1, v_2)] = 5/12 ≈ 0.417. The first-price auction earns about 10% more, consistent with Maskin–Riley’s “stretch” result.

**(b) Kaplan–Zamir (2012, Economic Theory 50(2):269–302): any pair U[a_1, ω_1], U[a_2, ω_2], with or without a minimum bid m.**  This answers a problem Vickrey posed in 1961. [springer](https://link.springer.com/article/10.1007/s00199-010-0563-9) Their method:

1. Settle trivial cases first: the Getty case, and m above the relevant support.
2. Fix b̲ = max{(a_1+a_2)/2, m}.
3. Add the two uniform FOCs, φ_1′(φ_2 − b) = φ_1 − a_1 and φ_2′(φ_1 − b) = φ_2 − a_2. The sum integrates to the identity φ_1φ_2 = b(φ_1+φ_2) − (a_1+a_2)b + c, with c = (a_1+a_2)²/4 when the minimum bid does not bind.
4. Evaluating the identity at b̄ gives b̄ = [ω_1ω_2 − c] / [(ω_1 − a_1) + (ω_2 − a_2)], which reduces to ω_1ω_2/(ω_1+ω_2) when a_i = 0.
5. Use the identity to eliminate φ_2. This leaves a single ODE, φ_1′(b)(a_1 + a_2 − 2b)² = 4(φ_1 − a_1)(φ_1 − b), which they solve explicitly. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)

With no binding minimum bid, the solution has the form

φ_1(b) = a_1 + (a_2 − a_1)² / [ (a_1 + a_2 − 2b)·C_1·exp((a_2 − a_1)/(a_1 + a_2 − 2b)) + 4(a_2 − b) ],

with C_1 pinned down by φ_1(b̄) = ω_1. Bidder 2’s inverse bid follows by swapping roles. A separate formula applies when the minimum bid binds. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)

Other results from the paper:

- The equilibrium is continuous in all five parameters. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)
- The case where one value is commonly known (a mixed strategy) is a limit of the general solution. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)
- **Crossing bids.**  With a minimum bid, bid functions can cross both at the minimum bid and at an interior point, even though one distribution stochastically dominates the other. [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)
- **A linear-bid class.**  For every m ≥ 0 there is a uniform class with b_1(v) = v/2 + m/2 and b_2(v) = v/2 + m/4. Their working paper states that within the uniform family, “outside the symmetric case, linear bid functions can occur only in the presence of a minimum bid.” [u-tokyo](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)

**(c) Plum (1992): power distributions F_1(x) = x^μ, F_2(x) = (x/β)^μ.**  [arxiv](https://arxiv.org/html/1906.09403v2) These have the same exponent, a common lower endpoint 0, and different upper bounds; Plum obtains a closed form for this family. [arxiv](https://arxiv.org/pdf/1906.09403) I could not obtain Plum’s full text, so I do not reproduce his general-μ formulas here. The μ = 1 case is the GLS solution above.

**(d) Cheng (2006, J. Math. Econ. 42(4–5):471–498): linear equilibria by “reverse engineering.”**  Cheng studies power-type families in which bids are linear. [psu](https://capcp.la.psu.edu/wp-content/uploads/sites/11/Working%20Papers/2007/AsymResale.pdf) In his words, “a buyer’s bidding strategy depends only on the total ‘strength’ of his opponents. The strength is measured by the power of the cumulative distribution function.” A power CDF also represents a merged cartel of several such buyers bidding jointly. [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0304406806000644)

My own derivation shows the mechanism; check the parameterization against Cheng’s paper.

- Take F_i(v) = (v/β_i)^{a_i} on [0, β_i].
- Against any linear opponent bid, (v − b)·b^{a_j} is maximized at b = a_j v/(1 + a_j). So b_1(v) = a_2v/(1+a_2) and b_2(v) = a_1v/(1+a_1).
- The common-top-bid condition requires β_1/β_2 = a_1(1+a_2)/[a_2(1+a_1)].

Cheng’s result for this family is that “the seller’s revenue is higher in the sealed-bid auction than in the open auction,” for any numbers of weak and strong buyers. [doi](https://doi.org/10.2139/ssrn.746786)

**(e) Maskin–Riley (2000a, RES 67(3):413–438) examples.**

- *Shift:*  weak U[0,1], strong U[2,3]. This is the Getty effect, and the first-price auction wins. [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF)
- *Stretch:*  weak U[0, 1/(1+z)], strong U[0, 1/(1−z)]. Here φ_w(b) = 2b/(1+z²... in their normalization the inverse bids are φ_w = 2b/(1 + (2zb)²)-type expressions, and the winning-bid CDF falls in z, so first-price revenue rises with asymmetry while second-price revenue falls. [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF)
- *Mass reallocated to the weak bidder’s lower endpoint:*  the open auction wins, because the strong bidder is tempted to “low-ball.” [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF)

### 5. Qualitative properties you can rely on (and check numerically)

- **Strong vs weak (Maskin–Riley 2000a).**  Under conditional stochastic dominance (F_s/F_w increasing), the strong bidder shades more: b_s(v) < b_w(v) on the interior. Moreover, “strong” buyers prefer the open auction, whereas “weak” buyers prefer the high-bid auction (their Prop. 2.5). [cdedse](http://cdedse.org/wp-content/uploads/2020/02/Working-Paper-304.pdf)[ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF)
- **Inefficiency.**  Because b_w(v) > b_s(v), the weak bidder sometimes wins with the lower value. The Myerson revenue formula then shows why rankings are ambiguous: the first-price auction misallocates relative to the efficient rule but can move allocations toward the bidder with higher marginal revenue. [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF)
- **Revenue ranking is genuinely ambiguous.**  Shifts and stretches favor the first-price auction (Maskin–Riley Props. 3.3–3.4); mass at the bottom favors the open auction (Prop. 3.5). [ucla](http://www.econ.ucla.edu/riley/research/asyRES.PDF) Kirkegaard (2012, Econometrica 80(5):2349–2364) unifies these: “the first-price auction is more profitable than the second-price auction when the strong bidder’s distribution is flatter and more disperse than the weak bidder’s distribution.” [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[wiley](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA9859) Li and Riley (2007) find numerically that asymmetry effects on revenue are “economically large.” [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0167718706001329)
- **Crossing.**  Kirkegaard (2009, JET 144:1617–1635) analyzes the ratio of equilibrium payoffs against the ratio of CDFs and proves that “first order stochastic dominance is necessary for bidding strategies *not*  to cross.” [cdedse](http://cdedse.org/wp-content/uploads/2020/02/Working-Paper-304.pdf)[repec](https://ideas.repec.org/a/eee/jetheo/v144y2009i4p1617-1635.html) Fibich–Gavish (2011) computed the first example of bid functions crossing twice. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf) These are good diagnostics: if your numerical bids cross when theory says they cannot, the solver is wrong. Hubbard–Kirkegaard–Paarsch (2013) recommend plotting relative expected payoffs for exactly this purpose. [springer](https://link.springer.com/article/10.1007/s10614-012-9333-z)

### 6. Numerical methods for the general case

- **Marshall, Meurer, Richard & Stromquist (1994, GEB 7(2):193–220).**
    - First general solver. It is motivated by collusion, where cartels induce power-type asymmetries. [psu](https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf)
    - Integrates backward from a guessed b̄ using Taylor-series expansions, because forward solutions from an approximation near the origin miss the top condition. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - They observed that “backward solutions are well behaved except in neighborhoods of the origin where they become (highly) unstable.” [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - Their F_1 = v, F_2 = v² case on [0,1] has the analytic top bid b̄ = 37/64, which makes a convenient test case. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
- **Bajari (2001, Economic Theory 18:187–205).**  Procurement framing. Proves uniqueness and gives three algorithms; the third uses a single global polynomial approximation for each inverse bid and iterates on the coefficients instead of searching for the endpoint. [psu](https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf)[springer](https://link.springer.com/article/10.1007/PL00004128)
- **Li & Riley (2007, IJIO 25(6):1269–1298), “Auction choice.”**  Their BIDCOMP2 program does backward shooting with adaptive step size. Gayle & Richard (2008, Computational Economics 32(3)) automate local Taylor expansions for arbitrary user-supplied distributions. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
- **Fibich & Gavious (2003, Math. Oper. Res. 28(4):836–852).**  Perturbation analysis gives explicit approximations of equilibrium bids for weakly asymmetric bidders, expanding around the symmetric solution. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[informs](https://pubsonline.informs.org/doi/10.1287/moor.28.4.836.20510) Fibich and Gavish later argue that for large auctions the right averaging is geometric rather than arithmetic in the CDFs. [tau](https://www.math.tau.ac.il/~fibich/Manuscripts/Asymmetric-first-price-auctions-boundary-layer.pdf)
- **Fibich & Gavish (2011, GEB 73:479–495), boundary-value method.**
    - **Why shooting fails.**  In the symmetric case, an error ε in b̄ propagates as b_ε(v) = b(v) + ε/F^{n−1}(v), which blows up as v → 0. The instability is “an inherent analytic property of backward solutions” and “cannot be eliminated by changing the numerical methodology.” [sciencedirect](https://www.sciencedirect.com/science/article/abs/pii/S0899825611000509) It worsens with n: with F = v and an error of only ε = −10⁻¹⁵ in b̄, the lowest value at which the backward solution remains valid rises from 0.033 for n = 10 to 0.17 for n = 20 and 0.70 for n = 100 (Fibich–Gavish 2011, §3.3).
    - **Two failure types.**  If b̄ is too low (type I), the solutions stay monotone but end above the low endpoint. If b̄ is too high (type II), φ_i hits the 45° line, where φ′ is infinite. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf) Some solvers, such as Matlab’s ODE45, silently integrate past that point and produce artifacts. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - **The fix.**  Change the independent variable to v_2. The system becomes dv_1/dv_2 = (F_1/f_1)(f_2/F_2)(v_1 − b)/(v_2 − b) and db/dv_2 = (f_2/F_2)(v_1 − b). It lives on the fixed domain v_2 ∈ [0,1], with conditions v_1(0) = b(0) = 0 and v_1(1) = 1, and b̄ is recovered as b(v_2 = 1). [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - **Solving it.**  Use fixed-point or Newton iterations. On the 37/64 test, Newton reached an error of 8.5×10⁻¹⁰ in 5 iterations versus 25 for fixed-point. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - **Scale.**  The method handles auctions “with as many as 450 players and with as many as nine different types of players.” It shows that the first- vs second-price revenue difference “decays as 1/n³ or even faster.”
    - **Limits.**  The authors stress that the evidence for convergence “is purely numerical.” Matlab code is in their online supplement. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
    - **Companion paper.**  Fibich & Gavish (2012, Math. Oper. Res. 37(2):219–243) recast power-law cases as a dynamical system. [researchgate](https://www.researchgate.net/publication/333993469_Bayesian_Nash_Equilibrium_in_First-Price_Auction_with_Discrete_Value_Distributions) There the bottom singularity is a saddle point, which yields a stable *forward* -shooting method. [ssrn](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1589726)
- **Hubbard & Paarsch (survey chapter; also their MIT Press book *Auctions* ) and Hubbard, Kirkegaard & Paarsch (2013, Computational Economics 42(2):241–266).**
    - Approximate each φ_i by a Chebyshev polynomial on [b̲, b̄], treat b̄ as an extra unknown, and minimize the squared FOC residuals at nodes. [uoguelph](https://www.uoguelph.ca/economics/repec/workingpapers/2015/2015-02.pdf)
    - Impose theory-derived constraints as part of the fit: the boundary conditions, monotonicity, and the bid-below-value condition. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[springer](https://link.springer.com/article/10.1007/s10614-012-9333-z)
    - Warning: “low-degree polynomial approximations perform poorly and can lead to incorrect policy recommendations concerning auction design.” [repec](https://ideas.repec.org/p/cca/wpaper/207.html)[springer](https://link.springer.com/article/10.1007/s10614-012-9333-z)
    - Their survey also gives the procurement mirror image, CRRA risk aversion, coalitions and bid preferences, with code. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)

### 7. Practical recipe for two bidders (Python/MATLAB)

**Step 0 — Classify the support configuration.**

- If the lower endpoints are equal at a, the boundary conditions are φ_i(a) = a.
- If a_1 < a_2, compute b̲ = argmax_b F_1(b)(a_2 − b) (or the reserve, if higher). The boundary conditions are then φ_1(b̲) = b̲ and φ_2(b̲) = a_2.
- Check for the Getty case: if bidder 2 prefers to bid ω_1 and win for sure, i.e., the argmax is at or above ω_1, then b_2 ≡ ω_1 and you are done.

**Step 1 — Validate first.**  Implement the solver and reproduce U[0,1] vs U[0,2] (b̄ = 2/3, φ_i = 2b/(1 ± (3/4)b²)) and the MMRS case F_1 = v, F_2 = v² (b̄ = 37/64).

**Step 2a — Backward shooting (simple, fine for n = 2 with care).**

1. Bracket b̄ in (b̲, min(ω_1, ω_2)).
2. For a trial b̄, integrate the pair φ_1′ = F_1(φ_1)/[f_1(φ_1)(φ_2 − b)] and φ_2′ = F_2(φ_2)/[f_2(φ_2)(φ_1 − b)] *backward*  from φ_1(b̄) = ω_1, φ_2(b̄) = ω_2. The top end is regular, since φ_i − b̄ > 0.
3. Use a stiff/implicit solver (e.g., `solve_ivp(method="Radau")` or ode15s) with event functions that stop when φ_i(b) − b ≤ δ for either i. That event is a type-II hit, meaning b̄ is too high.
4. Stop just above b̲, at b = b̲ + h. If an event fired, lower b̄. If the solution reaches b̲ + h with φ_i still clearly above their targets, b̄ is too low (type I), so raise it.
5. Bisect on b̄. Lebrun’s monotonicity lemma guarantees the ordering; switch to a secant method once bracketed.
6. Stop when ‖φ(b̲ + h) − target‖ < tol, using a local expansion near b̲ for the target. Never integrate into the singular point itself.

Expect to get b̄ to roughly 6–10 digits for two well-behaved bidders. Bids near the bottom are the least accurate part of the solution.

**Step 2b — Boundary-value method (preferred for robustness or when n > 2).**

1. Reparameterize by v_2 on its support, as in Fibich–Gavish.
2. Discretize d/dv_2 with high-order finite differences on a grid.
3. Start from v_1 = v_2 and b = v_2/2, then run Newton iterations on the residuals (R_{v1}, R_b).
4. Read off b̄ = b(ω_2).

Alternatively, use a Chebyshev collocation/least-squares solver with b̄ as a parameter (Hubbard–Kirkegaard–Paarsch).

**Step 3 — Post-checks.**

- Monotonicity, and b_i(v) ≤ v.
- Whether the bid functions cross, and whether that matches Kirkegaard’s (2009) predictions.
- The ordering b_s < b_w under conditional stochastic dominance.
- Payoff ratios.
- Revenue: compute it from the winning-bid CDF G(b) = F_1(φ_1(b))F_2(φ_2(b)) as E = b̄ − ∫_{b̲}^{b̄} G(b) db, plus b̲·G(b̲) if there is a mass point at the bottom.

### 8. Extensions

- **Reserve price r.**  Start the system at φ_i(r) = r. A binding reserve gives F_i(r) > 0, so the uniqueness theorems apply (Maskin–Riley 2003; Lebrun 2006, condition (i)). [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf)[ias](https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf) The bid functions start with zero slope at r, so φ′ is infinite there; handle that point with an expansion.
- **Risk aversion.**  Maskin–Riley (1984) is the symmetric benchmark. With asymmetric CRRA utilities (v − b)^{γ_i}, Hubbard–Paarsch derive φ_i′ = (F/f)[(1/(n−1))Σ_m γ_m/(φ_m − b) − γ_i/(φ_i − b)]. Heterogeneous risk attitudes alone create an asymmetric auction even with identical value distributions. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf)
- **More than two bidders.**  Use the general N-bidder system in §1, with a common top bid when upper endpoints coincide. Backward shooting deteriorates quickly with n (Fibich–Gavish); prefer boundary-value or projection methods. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf) Hubbard & Kirkegaard (2015 working paper) treat the general N-bidder model with differing supports, where bid “separation” can occur at the bottom. [uoguelph](https://www.uoguelph.ca/economics/repec/workingpapers/2015/2015-02.pdf)
- **Procurement (low-bid) auctions.**  These are the mirror image. Replace F with the survivor function 1 − F and (φ − b) with (b − φ); the cost-ceiling end is singular and the common *lowest*  bid is the free boundary. Hubbard–Paarsch give φ_n′(b) = [(1−F_n)/f_n]·[(1/(N−1))Σ 1/(b − φ_m) − 1/(b − φ_n)], solved by forward shooting from the unknown low bid. [uiowa](https://vinci.cs.uiowa.edu/~hjp/download/HoCE.pdf) Bajari (2001) works in this framing. [uiowa](https://vinci.cs.uiowa.edu/~hjp/HubbardPaarschHoCE.pdf)[springer](https://link.springer.com/article/10.1007/PL00004128)

## Recommendations

1. **Check the closed forms first.**  If your distributions are uniform (any supports, any minimum bid), use Kaplan–Zamir. If they are power-type with a common lower endpoint, use Plum or Cheng. Don’t solve numerically what has a closed form.
2. **Otherwise, make sure the problem is well posed:**
    - log-concave CDFs near the highest lower endpoint, or a binding reserve, or a strictly highest floor (Lebrun 2006);
    - densities bounded away from zero on the interior.
3. **For two bidders, backward shooting with a stiff solver, event detection and bisection on b̄ is adequate** , if you validate on the GLS and MMRS benchmarks and stop short of the singular point. For anything larger, or where you need accuracy at low values (e.g., structural estimation), switch to the Fibich–Gavish boundary-value method or a carefully constrained, sufficiently high-degree Chebyshev method.
4. **Use theory as a unit test:**
    - common b̄;
    - b_w > b_s under conditional stochastic dominance;
    - no crossing under first-order stochastic dominance in the standard cases;
    - first-price revenue above open-auction revenue for shifts and stretches.
5. **Don’t assume revenue equivalence or efficiency.**  Compute both auctions’ revenue explicitly. The sign of the difference depends on the shape of the asymmetry (Kirkegaard 2012), and it shrinks quickly as the number of bidders grows (Fibich–Gavish).

## Caveats

- **Notation varies across sources:**  lower endpoints underlined vs a_i; φ vs v_i(b) vs α_i. Some extracted texts (e.g., Kaplan–Zamir’s working-paper PDF) lose underline/overline marks. I re-derived the Kaplan–Zamir boundary formulas and the GLS solution and checked them for consistency, but **check the explicit Kaplan–Zamir solution against the published version before relying on it.**
- **Not verified from primary text:**  Plum’s general-μ formulas and Cheng’s exact parameterization. The Cheng linear family stated above is my derivation and is consistent with how the paper is described. The Krishna (2nd ed.) example number is also unverified.
- **My own calculations:**  the worked-example revenue figures (≈0.459 vs 0.417) and the specific inefficiency thresholds.
- **Unproven convergence:**  Fibich–Gavish’s boundary-value method has strong numerical evidence but no convergence proof. Shooting-method accuracy near the low end is limited by an analytic instability, not just by step size. [technion](https://ngavish.net.technion.ac.il/files/2013/01/BV_Method_GEB112.pdf)
- **Uniqueness is conditional:**  Kaplan and Zamir (Economic Theory Bulletin 3:65–77, 2015) show that the Maskin–Riley/Lebrun uniqueness results require the assumption that a buyer never bids above his value, and that dropping it yields additional, substantial equilibria with higher revenue. Ties and atoms can also require tie-breaking rules other than the fair rule for an equilibrium to exist (Lebrun 1996, 2002; Maskin–Riley 2000b). [yorku](https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf)