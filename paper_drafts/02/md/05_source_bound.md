# 5. Source-Bound Constraint: Why the Negative Reservoir Cannot Be Mined

One might still worry that a non-propagating negative sector could be
mined. Even if it cannot radiate on its own, perhaps an engineered process
could create a negative static configuration and extract compensating
positive energy.

The source-free constraint equation rules this out. In the static exterior
variable $A$, the zero-source equation is

$$
\Delta_{\rm ar} A=0,
$$

or

$$
(r^2 A')'=0.
$$

Integrating once gives

$$
r^2 A'=C_1,
$$

and integrating again gives

$$
A(r)=C_0-\frac{C_1}{r}.
$$

For an asymptotically flat source-free configuration, $A\to1$ at infinity,
so $C_0=1$. Regularity at the origin requires $C_1=0$. Hence

$$
A(r)\equiv1.
$$

Flat vacuum is the unique regular, asymptotically flat, zero-source static
state.

The negative static field energy is therefore source-bound. It exists
only as the constrained response to sources. Without a source there is no
independent well, and without an independent well there is no free
negative reservoir to mine.

Changing the negative sector requires changing the sources that determine
it. Moving sources, rearranging them, or making them time dependent
returns the system to the ordinary dynamical ledger, where the propagating
sector is positive. The negative static field can participate in energy
bookkeeping, but it is not an autonomous fuel supply.

This point is easy to miss. The statement

$$
u_{\rm stat}=-\frac{c^4}{8\pi G}(s')^2
$$

does not mean that arbitrary negative-energy static configurations are
available. The constraint equation and boundary conditions determine which
static configurations exist. In the absence of sources, the only one is
flat space.

The reduced source-binding result is verified as the G02 part of
`gate_G03_radiative_positivity.py`.
