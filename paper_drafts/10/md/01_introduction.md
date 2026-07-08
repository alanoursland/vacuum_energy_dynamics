# 1. Introduction

In 1784 John Michell computed the radius at which escape velocity
reaches the speed of light and found $r = 2GM/c^2$ — the Schwarzschild
radius, to the coefficient, a hundred and thirty-one years before the
Schwarzschild solution. The calculation uses nonrelativistic kinetic
energy and the Newtonian potential, both inapplicable, and lands on
the exact general-relativistic answer. Every instructor of general
relativity eventually faces a student who has noticed this, and the
available answers — "the errors cancel," "it is a coincidence," "do
not read anything into it" — are true without being satisfying. They
explain nothing about *why* the cancellation is exact rather than
approximate, and they sit awkwardly beside a fact of classroom life:
energy arguments of exactly this flavor keep being proposed, in print,
as derivations of the Schwarzschild metric.

The proposals have a history of their own. Simple derivations
combining special relativity, the equivalence principle, and Newtonian
gravity go back at least to Lenz and Schiff (1960) and Sacks and Ball
(1968); skeptical analyses began at once (Schild 1960) and culminated
in the theorem-grade objection of Gruber, Price, Matthews, Cordwell,
and Wagner (1988), whose title — "The impossibility of a simple
derivation of the Schwarzschild metric" — was intended to close the
genre. It did not close. Visser (2004) exhibited a Newtonian heuristic
that lands on the exact geometry in Painlevé–Gullstrand form, flagging
the exactness as an unexplained accident; Czerniawski (2006) advanced
the same route explicitly against the impossibility claim; Kassner
(2015, 2017) constructed reconstructions from augmented postulate
sets, with a residual coefficient fixed by Mercury's perihelion; and
Shuler (2018) proposed, with Kassner (2019) then paring back, a family
of exteriors indistinguishable in the weak field. The genre thus holds
three positions — impossibility, possibility, and family — and the
disagreement has persisted, we suggest, for a structural reason: the
positions have lacked a common object to be claims *about*. What has
been missing is a statement of precisely what the shared ingredients
determine.

This paper supplies that statement, and with it the dispute largely
resolves itself. Fix the ingredients every energy-accounting route
uses: the
Newtonian limit; an exact Gauss-type flux law in some static potential
variable; the time–radial compensation $g_{tt}g_{rr} = -1$; and the
requirement that the weight with which field energy enters its own
source be a constant of the theory. We show (Sec. 2) that these
determine the exterior exactly up to one parameter — a one-parameter
family of static metrics

$$A_\lambda = \big(1 + \lambda\,r_s/r\big)^{-1/\lambda},
\qquad B = 1/A_\lambda,$$

in which $\lambda$ is the self-energy counting weight, Schwarzschild
is the member $\lambda = -1$, and all members agree through first
post-Newtonian order. Three theorems about this family then do the
work of the paper.

First, a dichotomy (Sec. 3), which sets the stakes: members with
$\lambda \geq 0$ have no horizon at any radius. Miscounting the
field's energy does not move the surface $A = 0$; it deletes it. The
parameter the ingredients leave free is not a second-order refinement
— the existence of black-hole horizons rides on it, and with it the
part of Michell's conclusion that feels most like a triumph of energy
reasoning: that something drastic happens at $r_s$ at all.

Second, a no-go (Sec. 4): no static energy-accounting argument selects
the Schwarzschild member. The one convention-independent handle on
gravitational energy in the weak field — the work budget of
quasi-static assembly, evaluated on interaction terms where
localization ambiguities cancel — forces $|\lambda| = 1/4$, with even
the sign contingent on how matter is carried in the books. Honest
accounting does not merely fall short of Schwarzschild; it selects
against it. A corollary: the nonlinear term that resums the
Schwarzschild exterior is four times the Newtonian field energy
density, so the familiar identification of the two is not loose
language but an error of definite size.

Third, a dictionary (Sec. 5), which supplies what accounting cannot:
transforming the family to isotropic coordinates gives $\gamma = 1$
identically and $\beta - 1 = \lambda + 1$ exactly. The parametrized
post-Newtonian parameter $\beta$, long glossed as "nonlinearity in the
superposition law," is within this family a direct measurement of the
self-energy counting weight. Three of the four classical tests are
blind to $\lambda$; the perihelion precession alone discriminates, and
the modern bound $|\beta - 1| \lesssim 10^{-4}$ fixes $\lambda = -1$
to four decimal places. The dichotomy then closes: within the family,
whether horizons exist is the weak-field question $\beta < 2$, and
Mercury answered it.

Energy reasoning does deliver the scale, and one more thing, which
resolves the original puzzle (Sec. 6): the Schwarzschild member —
uniquely in
the family — admits a slicing in which infall from rest at infinity
follows the Newtonian velocity profile $\tfrac12 v^2 = GM/r$ exactly,
at every radius, with the horizon at $v = c$. Michell's computation
was, unknowably, a correct computation in that chart. The cancellation
of errors is the signature of the dynamically selected member, and its
exactness is exactly as deep as the selection problem the rest of the
paper quantifies.

The arbitration of the three positions then reads off (Secs. 6.2, 7):
the impossibility theorem is correct for accounting ingredients, with
the family as its precise residue; the possibility derivations are
correct because each imports one dynamics-grade selector — a chart
ansatz, a force law, or a measurement — and the import is mandatory.
All results are verified symbolically; the scripts accompany the paper
as supplementary material (Sec. 8).
