# Tensor-Virial Identity in Generality

## Statement

Let \(T^{\mu\nu}\) be a symmetric stress tensor on a flat background,
using \(x^0=ct\), and assume

$$
\partial_\mu T^{\mu\nu}=0.
$$

For an isolated source with compact support, or with falloff sufficient
to discard the surface terms below,

$$
\boxed{
\int T^{ij}\,d^3x
=
{1\over 2c^2}{d^2\over dt^2}
\int T^{00}x^i x^j\,d^3x
}.
$$

Equivalently, if

$$
I^{ij}(t)=\int T^{00}x^i x^j\,d^3x,
$$

then

$$
\ddot I^{ij}=2c^2\int T^{ij}\,d^3x .
$$

This is the tensor-virial step needed in the quadrupole chain of the
008 radiative bootstrap.

## Proof

Stress conservation with \(x^0=ct\) gives

$$
\dot T^{00}=-c\,\partial_k T^{k0},
\qquad
\dot T^{0i}=-c\,\partial_k T^{ki}.
$$

Using symmetry \(T^{k0}=T^{0k}\),

$$
\dot I^{ij}
=
\int \dot T^{00}x^i x^j\,d^3x
=
-c\int \partial_kT^{0k}x^i x^j\,d^3x .
$$

The product rule gives

$$
\partial_k(T^{0k}x^i x^j)
=
(\partial_kT^{0k})x^i x^j
+T^{0i}x^j+T^{0j}x^i .
$$

The surface integral of \(T^{0k}x^i x^j\) vanishes by the support/falloff
assumption, so

$$
\dot I^{ij}
=
c\int (T^{0i}x^j+T^{0j}x^i)\,d^3x .
$$

Differentiate again and use momentum conservation:

$$
\ddot I^{ij}
=
-c^2\int
\left[
(\partial_kT^{ki})x^j+(\partial_kT^{kj})x^i
\right]d^3x .
$$

For the first term,

$$
\partial_k(T^{ki}x^j)=(\partial_kT^{ki})x^j+T^{ji}.
$$

For the second,

$$
\partial_k(T^{kj}x^i)=(\partial_kT^{kj})x^i+T^{ij}.
$$

The two surface terms vanish by the same isolation assumption. Therefore

$$
\ddot I^{ij}
=
c^2\int(T^{ji}+T^{ij})\,d^3x .
$$

Since \(T^{ij}=T^{ji}\),

$$
\ddot I^{ij}=2c^2\int T^{ij}\,d^3x,
$$

which proves the identity.

## Fit In The Admitted Presentation

This closes a rigor debt inside the already-admitted field-equation
presentation. It does not change the equations, the radiative
normalization, or any observational coefficient. It upgrades one line in
the quadrupole derivation from "verified on a compact witness" to
"proved under stated conservation and boundary assumptions."

The result belongs with the radiative-sector rigor notes, not the open
physics program. It is a bookkeeping theorem for the existing
quadrupole chain.

