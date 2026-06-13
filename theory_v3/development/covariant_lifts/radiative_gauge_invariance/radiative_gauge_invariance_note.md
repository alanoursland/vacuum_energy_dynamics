# Gauge Invariance of Averaged Radiative Stress

## Statement

In the local inertial short-wave regime of the 015 averaging lift, the
averaged radiative stress is

$$
<t_{ab}> =
{c^4\over 32\pi G}
<\partial_a h^{TT}_{ij}\partial_b h^{TT}_{ij}>
$$

to leading order in \(\lambda/L\). This quantity is invariant under
admissible relabeling gauge transformations at the same leading order.

## Admissible Gauge Transformations

For a high-frequency wave with propagation direction \(n_i\), the
leading fast part of an infinitesimal relabeling is

$$
\delta h_{ij}
=
\partial_i\xi_j+\partial_j\xi_i
=
n_i v_j+n_j v_i
$$

after absorbing the fast phase derivative into \(v_i\). This is a
longitudinal tensor: every term carries at least one factor of \(n_i\).

Slow-envelope derivatives of \(\xi_i\) are not claimed to vanish
identically. They are suppressed by the same scale separation used in
015:

$$
\lambda \ll \ell_{\rm avg} \ll L.
$$

So the leading radiative gauge question is whether the longitudinal fast
piece can change \(h^{TT}_{ij}\). It cannot.

## TT Projector

Let

$$
P_{ij}=\delta_{ij}-n_i n_j
$$

and

$$
\Lambda_{ij,kl}
=
P_{ik}P_{jl}
-{1\over2}P_{ij}P_{kl}.
$$

The TT projection is

$$
h^{TT}_{ij}=\Lambda_{ij,kl}h_{kl}.
$$

For any \(v_i\),

$$
\Lambda_{ij,kl}(n_kv_l+n_lv_k)=0
$$

when \(n_i n_i=1\). Therefore the leading fast pure-gauge part has no
TT component.

## Consequence for the Averaged Stress

Because the projector is linear,

$$
(h+\delta h)^{TT}_{ij}=h^{TT}_{ij}.
$$

Therefore

$$
\partial_a(h+\delta h)^{TT}_{ij}
=
\partial_a h^{TT}_{ij}
$$

at leading short-wave order, and hence

$$
<\partial_a(h+\delta h)^{TT}_{ij}
\partial_b(h+\delta h)^{TT}_{ij}>
=
<\partial_a h^{TT}_{ij}\partial_b h^{TT}_{ij}>.
$$

Thus the averaged radiative stress used in 015 is gauge-invariant under
the admitted high-frequency relabelings.

## What This Retires

This retires the radiative gauge-invariance subpiece of the covariant
lift debt for \(<t_{ab}>\). Together, 015 and 016 close the radiative
averaging/gauge part of the open item. The remaining targeted lift from
that item is the general time-dependent vector sector from 012.

