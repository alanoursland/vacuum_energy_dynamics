# 1. Introduction

In 1784, John Michell used Newtonian mechanics to determine the radius at which the escape velocity from a spherical body equals the speed of light. His result,

[
r=\frac{2GM}{c^2},
]

is numerically identical to the Schwarzschild radius, obtained from general relativity 131 years later. The agreement is puzzling because Michell’s calculation uses both the Newtonian gravitational potential and the nonrelativistic kinetic-energy formula in a regime where neither is generally valid. Standard explanations—such as “the errors cancel” or “the result is a coincidence”—correctly deny that Michell derived a relativistic horizon, but they do not explain why the cancellation is exact.

The same puzzle appears in a broader literature on simple derivations of the Schwarzschild metric. Arguments combining Newtonian gravity, special relativity, the equivalence principle, and energy conservation date at least to Lenz’s unpublished construction, reported by Sommerfeld (1952), and were developed further by Schiff (1960), Tangherlini (1962), and Sacks and Ball (1968), with the Lenz–Sommerfeld argument later revisited by Cuzinatto, Pimentel, and Pompeia (2011). Counterexamples followed closely (Rindler 1968, 1969), culminating in the systematic objection of Gruber, Price, Matthews, Cordwell, and Wagner (1988), whose title—“The impossibility of a simple derivation of the Schwarzschild metric”—summarized the resulting position.

The issue nevertheless remained open. Visser (2005) showed that a Newtonian heuristic reproduces the Schwarzschild geometry in Painlevé–Gullstrand coordinates, while emphasizing that the exact agreement remained unexplained. Czerniawski (2006) defended a similar construction against the impossibility claim. Kassner (2015) reconstructed the weak-field metric from an enlarged set of physical assumptions, with one remaining coefficient fixed by Mercury’s perihelion precession; later reconstructions supplied additional physics through postulates or a dust-ball condition (Kassner 2017).

Shuler (2018) exhibited the Schwarzschild metric and two alternatives in a common parameterized form. Kassner (2019) reviewed those metrics and showed that only Schwarzschild satisfies a standard relativistic generalization of Newton’s law. Related heuristic derivations likewise reach Schwarzschild by supplementing Newtonian or kinematic input with further assumptions. The present work does not claim the closed metric form as new. Its contribution is to derive the continuous family as the complete result of the assumptions below and to identify separately what the specified static accounting class, post-Newtonian measurements, and an exact Painlevé–Gullstrand infall condition imply for its free parameter.

These works represent three broad positions. The first holds that simple energy-based assumptions cannot determine the Schwarzschild metric. The second holds that an appropriate combination of such assumptions can determine it. The third holds that the assumptions determine a family of metrics rather than a unique exterior. We argue that these positions have persisted because they have not been formulated as claims about the same set of assumptions. The relevant question is not simply whether a “simple derivation” is possible, but precisely what the assumptions shared by such derivations determine.

We therefore fix four ingredients that recur in energy-accounting approaches:

1. the Newtonian weak-field limit;
2. the requirement that a monotonic static potential variable obey an exact vacuum Gauss law;
3. the time–radial compensation condition
   [
   g_{tt}g_{rr}=-1;
   ]
4. a constant coefficient for the nonlinear squared-gradient term obtained when the flux law is written in (s=\ln A).

For a static, spherically symmetric exterior, these assumptions determine the metric up to one dimensionless parameter. Writing

[
ds^2=-A_\lambda(r)c^2dt^2+B(r)dr^2+r^2d\Omega^2,
]

we obtain

[
A_\lambda(r)
============

\left(1+\lambda\frac{r_s}{r}\right)^{-1/\lambda},
\qquad
B(r)=\frac{1}{A_\lambda(r)}.
]

Mathematically, (\lambda) is the constant coefficient of the squared-gradient term. Section 4 examines the additional assumptions under which it may be interpreted as a self-energy counting weight. The Schwarzschild exterior is recovered for

[
\lambda=-1,
]

for which

[
A_{-1}(r)=1-\frac{r_s}{r}.
]

The primary result is the completeness statement: any static spherical exterior satisfying the four assumptions above belongs to this one-parameter class. This separates construction from selection. Assumptions (I1)–(I4) construct the candidate class but do not select (\lambda=-1); any derivation that reaches Schwarzschild must supply an additional physical, kinematic, or observational condition, whether or not that condition is presented as a separate step.

All members have the same Newtonian limit and the same first post-Newtonian spatial-curvature parameter,

[
\gamma=1.
]

The parameter left undetermined by the assumptions appears instead in the nonlinear post-Newtonian coefficient (\beta).

All claims below are made within this stated framework: assumptions (I1)–(I4), the static asymptotically flat exterior branch on which (A>0), and the resulting family (A_\lambda). Accordingly, “unique” means unique within that family. For general (\lambda<0), we establish only that (A_\lambda) has a finite positive-radius zero; this paper identifies such a zero as a horizon only for the Schwarzschild member. The accounting exclusion applies to the gradient-local static ledger and matter conventions defined in Sec. 4. PPN inferences use the family relation derived in Sec. 5 together with any experiment-specific PPN assumptions stated there.

Beyond the classification theorem, the paper develops four consequences with different logical status.

First, as an immediate structural corollary, the family exhibits a sharp zero-set dichotomy. The static time coefficient has a finite positive-radius zero precisely when

[
\lambda<0.
]

For (\lambda\geq0), the metric function (A_\lambda(r)) remains nonzero at every positive radius. The undetermined parameter therefore does not merely control a small higher-order correction. Its sign also determines whether the static time coefficient vanishes at finite radius.

Second, as a conditional result within the static bookkeeping class defined in Sec. 4, a two-shell assembly ledger excludes the Schwarzschild value (\lambda=-1). As the convention for matter energy is varied between the local and asymptotic audits, the resulting self-energy weight is restricted to

[
-\frac14\leq\lambda\leq\frac14.
]

The entire interval excludes the Schwarzschild value. In the same gradient-local convention, the nonlinear source term associated with Schwarzschild is four times the standard Newtonian gravitational field-energy density.

Third, as an operational result, the family admits a direct parametrized post-Newtonian interpretation. After transformation to isotropic coordinates, we find

[
\gamma=1
]

for every member and

[
\beta-1=\lambda+1.
]

The PPN parameter (\beta) therefore directly determines the family parameter:

[
\lambda=\beta-2.
]

The classical light-bending and time-delay tests are insensitive to (\lambda) because they depend primarily on (\gamma), which is common to the entire family. Perihelion precession, however, depends on (\beta) and therefore distinguishes the members. The observational bound

[
|\beta-1|\lesssim10^{-4}
]

selects

[
\lambda=-1
]

to the same accuracy.

This relation also connects weak-field observations to the zero-set dichotomy. A finite positive-radius zero exists precisely when

[
\beta<2.
]

A weak-field measurement of (\beta) thus determines the same parameter that controls the finite-radius zero structure. The family members previously proposed by Shuler correspond to values of (\beta) already excluded by perihelion data, so they do not require strong-field observations to be distinguished from Schwarzschild.

Fourth, the family gives a conceptual explanation of Michell’s coincidence. The Schwarzschild member is unique within the class in admitting a Painlevé–Gullstrand slicing for which particles falling from rest at infinity obey the exact Newtonian-looking velocity relation

[
\frac12v^2=\frac{GM}{r}
]

at every radius. In that slicing, the condition (v=c) occurs at

[
r=\frac{2GM}{c^2}.
]

Michell’s calculation was therefore not a derivation of the Schwarzschild metric: Newtonian mechanics alone does not determine the relativistic geometry or establish the existence of a horizon. Conversely, the numerical agreement is not devoid of explanation. Once the Schwarzschild member has been selected by dynamics or observation, its Painlevé–Gullstrand description explains why Michell’s Newtonian calculation gives the exact horizon radius.

The three historical positions can then be reconciled. The base assumptions do not uniquely determine Schwarzschild; they leave the residual freedom parameterized by (\lambda). Successful possibility derivations reach Schwarzschild by introducing an additional selector, such as a dynamical law, a coordinate-slicing condition with physical content, or an observational constraint.

Section 2 derives the complete one-parameter family. Section 3 establishes the finite-radius zero dichotomy. Section 4 develops the conditional static-accounting no-go result. Section 5 derives the PPN dictionary and observational constraints. Section 6 analyzes the Painlevé–Gullstrand infall profile and Michell’s coincidence. Section 7 discusses the implications for simple derivations of the Schwarzschild exterior, and Section 8 summarizes the conclusions.
