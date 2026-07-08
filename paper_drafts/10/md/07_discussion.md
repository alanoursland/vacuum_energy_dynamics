# 7. Discussion

The question in the title has a clean answer. Energy bookkeeping —
the Newtonian anchor, exact flux accounting, time–radial compensation,
and a constant counting weight — buys the one-parameter family
$A_\lambda$, the scale $r_s = 2GM/c^2$ inside every member, and the
entirety of first post-Newtonian phenomenology. It provably does not
buy the member: the strongest invariant accounting argument lands at
$|\lambda| = 1/4$ with a convention-dependent sign, and the
Schwarzschild self-sourcing term exceeds the Newtonian field energy
density by a factor of four that no convention absorbs. The member is
bought elsewhere — by the self-coupling consistency of the field
equations on the theory side, or by $\beta$ on the experimental side,
where $\beta - 1 = \lambda + 1$ makes the purchase explicit. The
horizon, in turn, belongs entirely to the member: its existence is
equivalent, across the family, to $\beta < 2$.

The analysis suggests a discipline for the derivation genre,
which shows no sign of retiring. Any proposed simple derivation of the
Schwarzschild metric must import at least one ingredient beyond
(I1)–(I4), and the import is where the second-order physics enters;
it deserves to be named as such rather than folded into the scenery.
The published derivations, read this way, form a table rather than a
quarrel:

| route | extra ingredient | what it is |
|---|---|---|
| Michell/Laplace escape velocity | none | no selection; scale only |
| Visser (2004); Czerniawski (2006) | Newtonian river in flat slices | chart-level statement of $\lambda = -1$ |
| Kassner (2015) | exact $1/r^2$ force law ($R^t{}_t = 0$) | dynamics-grade postulate |
| Kassner (2015), variant | coefficient from Mercury | measurement of $\beta$ |
| Kassner (2019) on Shuler (2018) | relativistic force-law criterion | dynamics-grade postulate |
| bootstrapped gravity (Casadio et al. 2018) | $q_\Phi = 1$ by 1PN matching | recovery-shaped calibration |
| field-theoretic bootstrap (Deser 1970; Duff 1973) | self-coupling consistency to all orders | the actual selector |

The last row is the honest endpoint: iterated self-coupling
consistency, carried to all orders, is a derivation of the Einstein
equations, at which point one is no longer doing simple derivations.
Between the first row and the last, every route pays for the member
with one dynamics-grade coin, and the family prices the coin.

Two limitations bound the claims. The family is a statement about
static, spherically symmetric exteriors on the compensated branch
$AB = 1$; relaxing (I3) enlarges the candidate space, and the
accounting analysis of Sec. 4 would need to be redone there (the
first-order degeneracy, however, only deepens: relaxed spatial sectors
generically spoil $\gamma = 1$ and die faster, not slower). And the
no-go is a statement about *static* accounting with gradient-local
densities; it does not exclude that some genuinely dynamical
bookkeeping — a work budget for time-dependent processes, with
radiation accounted — could select the member. We know of no such
argument, and the tree-level resummation suggests that any successful
one would be the field equations wearing a disguise; but the theorem
proved here is the static one.

For teaching, the upshot is a replacement for the usual mumble. The
honest answer to "why does the escape-velocity argument give exactly
$r_s$?" is in three parts: because the scale $2GM/c^2$ is first-order
information that every candidate exterior shares; because the exact
theory happens to admit a chart in which infall is Newtonian at all
radii, so the old calculation is secretly a correct one about the true
metric; and because the part of the answer that sounds like it should
be creditable to energy accounting — that something special happens
*at* that radius — is precisely the part accounting cannot certify. A
student who absorbs the three parts has learned, in miniature, what
the field equations are for.

## Suggested problems

1. Verify the identity
   $\Delta(e^{\mu s}) = \mu e^{\mu s}[\Delta s + \mu (s')^2]$ and use
   it to show that an exact Gauss law in the variable $f(A)$ has a
   field-independent self-sourcing weight only when $f$ is a power of
   $A$ (or $\ln A$).
2. Solve $\Delta s = \lambda (s')^2$ by the Bernoulli substitution and
   confirm the family, including the $\lambda \to 0$ limit.
3. Compute the two-shell field cross term for the density
   $\lambda c^4|\nabla s|^2/8\pi G$ and reproduce
   $\lambda = -1/4$ and $\lambda = +1/4$ for the two matter
   conventions.
4. Carry the family to isotropic coordinates and derive
   $\gamma = 1$, $\beta = \lambda + 2$.
5. Show that $A_\lambda$ has a zero at positive radius if and only if
   $\lambda < 0$, and locate it.
6. Bring a general $AB = 1$ metric to Painlevé–Gullstrand form and
   show that the river obeys $\tfrac12 v^2 = GM/r$ at all radii only
   for the Schwarzschild member.
