# 6. The Michell coincidence, resolved

The oldest calculation in this subject is also the one that most needs
explaining. Michell (1784) and Laplace (1799) set the escape velocity
equal to the speed of light, $\tfrac12 v^2 = GM/r$ with $v = c$, and
obtained $r = 2GM/c^2$ — the exact horizon radius, from premises that
are wrong twice over (nonrelativistic kinetic energy, Newtonian
potential). The standard verdict is a cancellation of errors, and the
standard warning is that nothing may be inferred from it. Both are
correct, and neither is the end of the story, because the coincidence
has structure that the verdict does not touch: why does the *exact*
number come out, rather than the right order of magnitude?

## 6.1 Every member has a river; one river is Newtonian

Any member of the family admits Painlevé–Gullstrand form. Setting
$t = T - \int \sqrt{1 - A}\,/(cA)\; dr$ brings the metric
$-c^2 A\,dt^2 + A^{-1} dr^2 + r^2 d\Omega^2$ to

$$ds^2 = -c^2\,dT^2 + \big(dr + v(r)\,dT\big)^2 + r^2 d\Omega^2,
\qquad
v(r) = c\,\sqrt{1 - A(r)}\,,$$

flat spatial slices threaded by a radial "river" of velocity $v(r)$ —
the picture developed pedagogically by Hamilton and Lisle (2008). The
slicing exists family-wide; it is the profile of the river that knows
the member. The Newtonian free-fall law,

$$\tfrac12\,v^2 = \frac{GM}{r}
\qquad\text{at every } r,$$

requires $1 - A = r_s/r$ exactly — and within the family that is the
statement $\lambda = -1$ and nothing else, since
$1 - A_\lambda = x - \tfrac{1+\lambda}{2}x^2 + O(x^3)$. Every other
member's river deviates from the Newtonian profile at second order.
For the Schwarzschild member, and for it alone, the correspondence is
exact at all radii, and the horizon sits precisely where the river
reaches the speed of light: $v(r_{\rm h}) = c \iff A = 0$.

This is the resolution. Michell's calculation is not a lucky
juxtaposition of two mistakes; it is a *correct calculation performed
in the Painlevé–Gullstrand slicing of the selected member*, carried
out a century before the slicing existed. The "cancelling errors"
cancel because the exact theory, in this chart, really does assign
infalling frames the Newtonian velocity profile and really does mark
the horizon by $v = c$. What is accidental is not the arithmetic but
the applicability: the calculation is only about the $\lambda = -1$
member, and nothing in Michell's premises — nothing, by Sec. 4, in
any energy-accounting premises — selects that member. The coincidence
is real, and it is exactly as large as the selection problem this
paper has been quantifying.

The limits of the shortcut confirm the reading. The Michell route
carries no spatial metric: taken as a metric ansatz it corresponds to
$B = 1$, hence $\gamma = 0$ and half the observed light deflection,
the failure that ruled out scalar-gravity reasoning in 1919. It hands
you a number, not a function; the function was always the hard part.

## 6.2 The dispute, arbitrated

The pieces are now in place to settle accounts in the
impossibility–possibility dispute, and the settlement is that everyone
was right at their declared scope.

Gruber et al. (1988) claimed that special relativity plus Newtonian
gravity plus equivalence-principle reasoning cannot reach the exact
metric. Within the ingredient class of Sec. 2 that is a theorem, now
with a precise residue: the reachable set is the family, one parameter
short.

The possibility papers each add one member-selecting ingredient, and
the addition is doing all the work. Visser (2004) reaches
Schwarzschild by embedding Newtonian free fall in flat slices with
Galilean assembly — a structural ansatz that, as just seen, is
equivalent to imposing the Newtonian river profile, i.e. to selecting
$\lambda = -1$ by hand; his own observation that the exactness "is an
accident" is, in the present language, the observation that the ansatz
happens to name the dynamically selected member. Czerniawski (2006)
runs the same route explicitly as a counter to the impossibility
claim. Kassner (2015) is the most self-aware case: his added postulate
(an exact inverse-square force law, which he connects to
$R^t{}_t = 0$) is announced as going beyond the base ingredients, and
where his postulates still leave a coefficient free he fixes it from
Mercury — the operational twin of Sec. 5. Shuler (2018) proposed, and
Kassner (2019) reduced, a family of 1PN-degenerate exteriors, with the
reduction again supplied by a force-law criterion of dynamical
character.

The arbitration, then: the impossibility theorem holds for accounting
ingredients; the possibility derivations succeed because each imports
one dynamics-grade selector, variously disguised as a chart choice, a
force law, or an experimental input. The family makes the disguises
transparent, and the no-go of Sec. 4 shows the import was mandatory:
there was nothing in the accounting to promote.

[Figure 3 near here: the river profile $v(r)/c$ for the family
members of Fig. 1; only the $\lambda = -1$ profile follows
$\sqrt{r_s/r}$ exactly, and only profiles with $\lambda < 0$ reach
$v = c$ at finite radius.]
