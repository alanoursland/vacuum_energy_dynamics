# 4. What energy accounting cannot fix

With horizons riding on the outcome, the natural hope — the one the
simple-derivation genre keeps returning to — is that $\lambda$ is not
free at all: gravitational field energy is negative, it must gravitate
like any other energy, and imposing this should select the member. The
Nordtvedt program and lunar laser ranging have, after all, confirmed
to high precision that gravitational binding energy gravitates. This
section shows why the hope fails, not for want of ingenuity but as a
matter of theorem. The argument has two steps: a lemma showing that
the most tempting formulation of the requirement is empty, and a
computation showing that the strongest invariant formulation selects
the wrong value.

## 4.1 A lemma on self-consistency

In the weak field the sourced equation reads
$\Delta s = (8\pi G/c^4)\,\rho c^2$, so the coupling per unit energy
density is $8\pi G/c^4$. It is then natural to read the vacuum
equation $\Delta s = \lambda (s')^2$ as the statement that a field
energy density

$$u_\lambda \;=\; \lambda\,\frac{c^4 (s')^2}{8\pi G}$$

sources the field at the same coupling as matter. One might hope to
fix $\lambda$ by demanding precisely this: *the field's own energy
gravitates with the universal coupling.*

The demand is empty. The quantity $u_\lambda$ was defined as whatever
multiplies the coupling in the equation; the statement holds
identically for every $\lambda$, including $\lambda = 0$ with
$u_0 = 0$. Self-consistency between an equation and a density read off
from that equation cannot select anything. To give the requirement
content, the field energy density must be determined *independently* —
from the mechanics of the theory, not from the equation under test.
The remainder of this section is the strongest such determination we
know how to make, and its verdict is unexpected.

## 4.2 The invariant ledger

Local gravitational energy density is a notoriously convention-bound
quantity — in general relativity it is the pseudotensor problem, and
already in Newtonian gravity the density $-|\nabla\Phi|^2/8\pi G$ can
be traded for $\tfrac12\rho\,\Phi$, or mixtures, by moving total
divergences. What survives every such rearrangement is an integral:
the work budget of a quasi-static assembly process, read at infinity.

Take two concentric thin shells, masses $m_1$ and $m_2$, at radii
$a < b$, in the weak-field regime where all members of the family
coincide. Lowering the outer shell in from infinity against the inner
shell's attraction delivers work $W = G m_1 m_2 / b$ to the winch.
Energy conservation then fixes the interaction part of the system's
total energy,

$$E_{\rm int} = -\,\frac{G m_1 m_2}{b},$$

independently of any convention. Shell self-energies and surface terms
play no role: they are unchanged by the assembly and drop out of the
budget. This cross term is the one handle on gravitational energy that
every bookkeeping must respect.

Now suppose, as the self-sourcing reading requires, that the field
energy resides locally in the gradient, with density
$u = \lambda\,c^4 |\nabla s|^2/8\pi G$ and $s = 2\Phi/c^2$ at this
order. The localization is not a fresh choice from the menu of the
opening paragraph: a matter-localized bookkeeping such as
$\tfrac12\rho\,\Phi$ vanishes identically in vacuum, which is exactly
where the self-source term lives, so only a gradient-local density
can be the thing the equation counts. The self-sourcing reading fixes
the localization; what it cannot fix is the matter convention below. The gradients superpose, and the cross term of the density
integrates over the region exterior to the outer shell (the only place
both gradients are nonzero) to

$$E^{\rm field}_{\rm cross}
= \frac{\lambda\,c^4}{8\pi G}\int 2\,\nabla s_1\!\cdot\!\nabla s_2
\; dV
= 4\lambda\,\frac{G m_1 m_2}{b}.$$

The books must now balance, and here the convention question that the
cross term was supposed to evade reappears in a different place: at
what energy is the *matter* carried? Two conventions are natural, and
the literature uses both without always noticing the choice.

If matter is carried at its rest energy — the deficit lives entirely
in the field — then the field cross term must supply all of
$E_{\rm int}$:

$$4\lambda\,\frac{G m_1 m_2}{b} = -\,\frac{G m_1 m_2}{b}
\quad\Longrightarrow\quad
\lambda = -\tfrac{1}{4}.$$

If instead matter is carried at its locally redshifted energy — each
shell weighed with the other's potential, so the matter books already
contain $-2\,G m_1 m_2/b$ — then the field must return half the
deficit:

$$-\,\frac{2 G m_1 m_2}{b} + 4\lambda\,\frac{G m_1 m_2}{b}
= -\,\frac{G m_1 m_2}{b}
\quad\Longrightarrow\quad
\lambda = +\tfrac{1}{4}.$$

Anything between them interpolates: carrying matter at a fraction $f$
of the redshift correction gives $\lambda = (2f-1)/4$, so the
conventions fill the interval $[-1/4, +1/4]$.

The range of $f$ deserves an argument rather than an assumption, since
the interval rests on it. The endpoints are not merely the two
conventions the literature happens to use; at this order they are the
two *operational audits* available for a static element's energy. (A
convention, at second order, is characterized by $f$ alone:
self-potential terms in the carried mass are configuration-independent
and cancel from the cross ledger, and higher potential corrections
enter at third order.) A local audit — scales at the element — reads
the rest energy: $f = 0$. An asymptotic audit — hoist the element
reversibly back to infinity and weigh what arrives — reads the
redshifted energy: $f = 1$; and since the hoist can actually be
performed, books carrying the element below that value would show a
surplus materializing at infinity on retrieval. Conversely, books
carrying the element above its local reading ($f < 0$) credit the
matter column with energy that no measurement at the matter can find —
field energy relabeled, which the gradient-local assignment already in
force forbids counting a second time. A convention, in the sense the
theorem uses the word, is a fixed bookkeeping station between the two
audits; mixtures are convex, and $f \in [0, 1]$. For a reader who
insists the books are only books and $f$ may roam: the arithmetic
prices the excursion. Reaching merely the *sign* of the Schwarzschild
weight requires $f < 0$; reaching $\lambda = -1$ itself requires
$f = -3/2$ — matter credited with one and a half times the full
redshift correction *above* its rest energy. No bookkeeping in the
literature examined here has proposed it. Every static count within
the operational range falls short of the Schwarzschild weight by at
least a factor of four in magnitude, and most miss its sign.

## 4.3 The no-go, and a factor of four

The computation proves the following.

> **No-go.** Under ingredients (I1)–(I4), with the field energy
> assigned a gradient-local density (the only localization the
> self-sourcing reading admits) and matter carried at any fixed
> convention between its two operational audits — locally measured
> rest energy and asymptotically deliverable energy,
> $0 \le f \le 1$ — the invariant assembly ledger confines $\lambda$
> to the interval $[-1/4, +1/4]$, the endpoints realized by the two
> audits. Static energy accounting is not merely insufficient to
> select the Schwarzschild member; done honestly, it selects a
> *different* member.

A corollary makes the situation vivid. The Schwarzschild member's
self-source term is $u_{-1} = -c^4 (s')^2/8\pi G$, and with
$s' = 2\Phi'/c^2$ this equals $-4\,|\nabla\Phi|^2/8\pi G$: four times
the Newtonian field energy density. The term that resums the
Schwarzschild exterior is not the Newtonian energy density in
disguise, and identifications of the two — tempting, and present in
more than one place in the literature — are wrong by a factor that no
change of convention repairs. There is no bookkeeping in which the
Schwarzschild nonlinearity is "the field's energy, counted once."

This is the quantitative content behind the impossibility result of
Gruber et al. (1988). Their argument showed that Newtonian-plus-SR
reasoning cannot reach the second-order metric; the present form
locates the obstruction precisely (a single coefficient), evaluates
what honest accounting yields instead ($\pm 1/4$), and identifies why
the gap cannot be talked away: the coefficient is a property of the
dynamics, while the accounting arguments have access only to
quantities that are either convention-relative (local densities) or
$\lambda$-blind (first-order invariants).

It also explains a choice that had to be made by hand elsewhere. In
the bootstrapped-Newtonian program of Casadio and collaborators, a
self-interaction term is added to the Poisson equation with a coupling
charge $q_\Phi$, and $q_\Phi = 1$ is adopted *because* it reproduces
the leading post-Newtonian expansion of Schwarzschild. The present
result shows this was not a shortcut that better accounting could have
avoided: within any such scheme there is no accounting principle that
lands on the general-relativistic weight. What does fix the weight is
dynamics — the self-coupling consistency arguments of Deser (1970)
and, diagrammatically, the tree-graph resummation of Duff (1973)
select the Einstein equations and with them $\lambda = -1$ — or else
measurement, to which we now turn.
