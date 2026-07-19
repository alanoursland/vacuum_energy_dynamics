# 1. Introduction

In 1784, John Michell used Newtonian mechanics to determine the radius at which the escape velocity from a spherical body equals the speed of light. His result,

[
r=\frac{2GM}{c^2},
]

is numerically identical to the Schwarzschild radius, obtained from general relativity 131 years later. The agreement is puzzling because Michell’s calculation uses both the Newtonian gravitational potential and the nonrelativistic kinetic-energy formula in a regime where neither is generally valid. Standard explanations—such as “the errors cancel” or “the result is a coincidence”—correctly deny that Michell derived a relativistic horizon, but they do not explain why the cancellation is exact.

The same puzzle appears in a broader literature on simple derivations of the Schwarzschild metric. Arguments combining Newtonian gravity, special relativity, the equivalence principle, and energy conservation date at least to Lenz’s unpublished construction, reported by Sommerfeld (1952), and were developed further by Schiff (1960), Tangherlini (1962), and Sacks and Ball (1968). Counterexamples followed closely (Rindler 1968, 1969), culminating in the systematic objection of Gruber, Price, Matthews, Cordwell, and Wagner (1988), whose title—“The impossibility of a simple derivation of the Schwarzschild metric”—summarized the resulting position.

The issue nevertheless remained open. Visser (2005) showed that a Newtonian heuristic reproduces the Schwarzschild geometry in Painlevé–Gullstrand coordinates, while emphasizing that the exact agreement remained unexplained. Czerniawski (2006) defended a similar construction against the impossibility claim. Kassner (2015, 2017) reconstructed the metric from enlarged sets of postulates, with one remaining coefficient fixed by Mercury’s perihelion precession. Shuler (2018) proposed a family of static spherical exteriors, and Kassner (2019) subsequently examined which additional assumptions select the Schwarzschild member.

These works represent three broad positions. The first holds that simple energy-based assumptions cannot determine the Schwarzschild metric. The second holds that an appropriate combination of such assumptions can determine it. The third holds that the assumptions determine a family of metrics rather than a unique exterior. We argue that these positions have persisted because they have not been formulated as claims about the same set of assumptions. The relevant question is not simply whether a “simple derivation” is possible, but precisely what the assumptions shared by such derivations determine.

We therefore fix four ingredients that recur in energy-accounting approaches:

1. the Newtonian weak-field limit;
2. an exact Gauss-type flux law written in a static potential variable;
3. the time–radial compensation condition
   [
   g_{tt}g_{rr}=-1;
   ]
4. a constant weight governing the contribution of gravitational field energy to its own source.

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

The parameter (\lambda) is the constant self-energy counting weight. The Schwarzschild exterior is recovered for

[
\lambda=-1,
]

for which

[
A_{-1}(r)=1-\frac{r_s}{r}.
]

The family is complete relative to the four assumptions above: any static spherical exterior satisfying them belongs to this one-parameter class. All members have the same Newtonian limit and the same first post-Newtonian spatial-curvature parameter,

[
\gamma=1.
]

The parameter left undetermined by the assumptions appears instead in the nonlinear post-Newtonian coefficient (\beta).

The remainder of the paper establishes three principal results.

First, the family exhibits a sharp horizon dichotomy. A horizon can occur only when

[
\lambda<0.
]

For (\lambda\geq0), the metric function (A_\lambda(r)) remains nonzero at every positive radius, and no horizon exists. The undetermined parameter therefore does not merely control a small higher-order correction. Its sign determines whether the exterior contains a horizon at all.

Second, static energy accounting cannot select the Schwarzschild value (\lambda=-1). We examine the quasi-static assembly of two spherical shells and isolate the interaction terms for which ambiguities in the localization of gravitational energy cancel. As the convention for matter energy is varied between local and asymptotic accounting, the resulting self-energy weight is restricted to

[
-\frac14\leq\lambda\leq\frac14.
]

The entire interval excludes the Schwarzschild value. Thus static accounting does not merely leave (\lambda) undetermined; under the assumptions considered here, it cannot reproduce the self-sourcing strength required by the Schwarzschild exterior. Equivalently, the nonlinear source term associated with Schwarzschild is four times the standard Newtonian gravitational field-energy density.

Third, the family admits a direct parametrized post-Newtonian interpretation. After transformation to isotropic coordinates, we find

[
\gamma=1
]

for every member and

[
\beta-1=\lambda+1.
]

Within this family, the PPN parameter (\beta) therefore directly determines the self-energy weight:

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

This relation also connects weak-field observations to the horizon dichotomy. Since a horizon exists precisely when (\lambda<0), the equivalent condition within the family is

[
\beta<2.
]

This does not mean that Mercury directly probes a black-hole horizon. Rather, once the one-parameter family is assumed, a weak-field measurement of (\beta) determines the same parameter that controls the strong-field horizon structure. The family members previously proposed by Shuler correspond to values of (\beta) already excluded by perihelion data, so they do not require strong-field observations to be distinguished from Schwarzschild.

The family also clarifies Michell’s coincidence. The Schwarzschild member is unique within the class in admitting a Painlevé–Gullstrand slicing for which particles falling from rest at infinity obey the exact Newtonian-looking velocity relation

[
\frac12v^2=\frac{GM}{r}
]

at every radius. In that slicing, the condition (v=c) occurs at

[
r=\frac{2GM}{c^2}.
]

Michell’s calculation was therefore not a derivation of the Schwarzschild metric: Newtonian mechanics alone does not determine the relativistic geometry or establish the existence of a horizon. Conversely, the numerical agreement is not devoid of explanation. Once the Schwarzschild member has been selected by dynamics or observation, its Painlevé–Gullstrand description explains why Michell’s Newtonian calculation gives the exact horizon radius.

The three historical positions can then be reconciled. The impossibility result is correct for the stated accounting assumptions: they do not uniquely determine Schwarzschild. The family position identifies the precise residual freedom left by those assumptions. Successful possibility derivations reach Schwarzschild only by introducing an additional selector, such as a dynamical law, a coordinate-slicing condition with physical content, or an observational constraint. Such an additional input is not optional; it is exactly what fixes (\lambda=-1).

Section 2 derives the complete one-parameter family. Section 3 establishes the horizon dichotomy. Section 4 develops the static-accounting no-go result. Section 5 derives the PPN dictionary and observational constraints. Section 6 analyzes the Painlevé–Gullstrand infall profile and Michell’s coincidence. Section 7 discusses the implications for simple derivations of the Schwarzschild exterior, and Section 8 describes the accompanying symbolic verification scripts.
