# 1. Introduction

In 1784, John Michell used Newtonian mechanics to determine the radius at which the escape velocity from a spherical body equals the speed of light. His result,

[
r=\frac{2GM}{c^2},
]

is numerically identical to the Schwarzschild radius, obtained from general relativity more than a century later. Michell’s calculation uses both the Newtonian gravitational potential and the nonrelativistic kinetic-energy formula in a regime where neither is generally valid. Describing the agreement as a cancellation of errors or a coincidence establishes that Michell did not derive a relativistic horizon, but does not account for the exact numerical coefficient.

The same question appears in a broader literature on simple derivations of the Schwarzschild metric. Arguments combining Newtonian gravity, special relativity, the equivalence principle, and energy conservation date at least to Lenz’s unpublished construction, reported by Sommerfeld (1952), and were developed further by Schiff (1960), Tangherlini (1962), and Sacks and Ball (1968), with the Lenz–Sommerfeld argument later revisited by Cuzinatto, Pimentel, and Pompeia (2011). Rindler (1968, 1969) supplied counterexamples, and Gruber, Price, Matthews, Cordwell, and Wagner (1988) gave a systematic analysis of why the usual ingredients do not uniquely determine the metric.

Later work revisited the question. Visser (2005) showed that a Newtonian heuristic reproduces the Schwarzschild geometry in Painlevé–Gullstrand coordinates, while emphasizing that the exact agreement remained unexplained. Czerniawski (2006) developed a related construction. Kassner (2015) reconstructed the weak-field metric from an enlarged set of physical assumptions, with one remaining coefficient fixed by Mercury’s perihelion precession; later reconstructions supplied additional physics through postulates or a dust-ball condition (Kassner 2017).

Shuler (2018) exhibited the Schwarzschild metric and two alternatives in a common parameterized form. Kassner (2019) reviewed those metrics and showed that only Schwarzschild satisfies a standard relativistic generalization of Newton’s law. Related heuristic derivations likewise reach Schwarzschild by supplementing Newtonian or kinematic input with further assumptions. The present work does not claim the closed metric form as new. Its contribution is to derive the continuous family as the complete result of the assumptions below and to identify separately what the specified static accounting class, post-Newtonian measurements, and an exact Painlevé–Gullstrand infall condition imply for its free parameter.

These conclusions differ because the derivations do not use identical assumptions. We therefore ask what a specified common construction determines before any additional condition is used to select Schwarzschild.

We abstract three recurring ingredients from energy-accounting approaches:

1. the Newtonian weak-field limit;
2. the requirement that a monotonic static potential variable obey an exact vacuum Gauss law;
3. the reciprocal condition
   [
   g_{tt}g_{rr}=-1;
   ]

These ingredients still leave unrestricted functional freedom in the choice of potential variable. To obtain a definite class, we impose one additional closure condition:

4. the nonlinear squared-gradient coefficient obtained when the flux law is written in (s=\ln A) is constant.

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

Any static spherical exterior satisfying these four assumptions belongs to this one-parameter class. Assumptions (I1)–(I4) construct the family but do not select (\lambda=-1). Selection requires an additional physical, kinematic, or observational condition.

All members have the same Newtonian limit and the same leading spatial PPN coefficient,

[
\gamma=1.
]

The parameter left undetermined by the assumptions appears instead in the nonlinear post-Newtonian coefficient (\beta).

The results are confined to assumptions (I1)–(I4), the static asymptotically flat branch with (A>0), and the resulting family (A_\lambda). “Unique” means unique within that family. For general (\lambda<0), only a finite positive-radius zero of (A_\lambda) is established; the zero is identified as a horizon only for Schwarzschild. The accounting bound uses the gradient-local matter–field conventions of Sec. 4, and observational inferences use the test-specific PPN assumptions stated in Sec. 5.

The sign of (\lambda) determines whether the static time coefficient has a finite positive-radius zero. Within the matter–field split of Sec. 4, a two-shell calculation confines (\lambda) to ([-1/4,1/4]). The PPN transformation gives (\gamma=1) and (\beta=\lambda+2), so observations determine the member independently of that convention. Every member also admits a Painlevé–Gullstrand-type form, but the exact Newtonian infall profile selects (\lambda=-1) and accounts for Michell’s numerical result.
