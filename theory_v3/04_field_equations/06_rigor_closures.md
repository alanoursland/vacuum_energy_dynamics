# Rigor Closures on the Field-Equation Proof

This document records proof-hardening work completed after
`proof.md` was promoted as the direct derivation of the field equations.
These closures do not change the equations, move coefficients, or add
new physics. They discharge rigor debts around steps already present in
the proof.

`proof.md` remains the complete direct proof in one place. The closures
below are supporting theorem records and verification pointers that keep
the main proof readable while making its auxiliary assumptions explicit.

## Completed Closures

### P8/T4 Formal Rewrite

Former P8 content is no longer treated as a live postulate or standalone
recovery condition. The retained P8 file is a theorem record:

```text
former P8 content = P9 + C2
```

T4 now depends directly on P9 and the C2 bootstrap, and weak-field
summaries inherit \(\beta=1\) through the P9+C2/T4 chain.

Discharge files:

- `01_postulates/demoted_p8_static_exterior_temporal_self_coupling.md`
- `02_foundations/t4_second_order_temporal_self_coupling.md`
- `03_weak_field/summary_weak_field_gr_recovery.md`

### Scalaron Screening Note

Screening changes detectability, range, or amplitude; it does not satisfy
exact P7' unless the scalar profile is identically zero. For a general
screened scalar contribution

$$
\phi=\phi_{\rm GR}-q(r),\qquad \psi=\phi_{\rm GR}+q(r),
$$

the P7' shadow is

$$
r q'(r)-q(r).
$$

Exact P7' plus asymptotic flatness forces \(q=0\). Therefore screening
cannot rescue \(a\neq0\) unless the theory owner re-scopes P7'.

Discharge files:

- `development/scalaron_screening/scalaron_screening_note.md`
- `vacuum_forge/src/field_equation_trials/013_scalaron_screening/scalaron_screening_p7prime_obstruction.py`

### Tensor-Virial Identity

The compact witness in 008 has been replaced by a general conservation
identity. For an isolated symmetric stress tensor on flat background,
with \(x^0=ct\),

$$
\int T^{ij}\,d^3x
=
{1\over 2c^2}{d^2\over dt^2}
\int T^{00}x^i x^j\,d^3x .
$$

The proof uses flat stress conservation, stress symmetry, vanishing
surface terms, and enough regularity to commute time derivatives through
the integral.

Discharge files:

- `development/tensor_virial_identity/tensor_virial_identity_note.md`
- `vacuum_forge/src/field_equation_trials/014_tensor_virial_identity/tensor_virial_identity_general.py`

### Radiative TT Averaging

The Isaacson averaging portion of the radiative covariant-lift debt is
closed at local inertial short-wave level. The averaging window is

$$
\lambda \ll \ell_{\rm avg} \ll L.
$$

Fast periodic total derivatives and cross terms average away, slow
envelope corrections are suppressed by powers of \(\lambda/L\), and the
retarded TT stress remains positive and null-transported.

Discharge files:

- `development/covariant_lifts/radiative_tt_averaging/radiative_tt_averaging_note.md`
- `vacuum_forge/src/field_equation_trials/015_isaacson_averaging/isaacson_tt_averaging.py`

### Radiative Gauge Invariance

The averaged radiative stress built from TT-projected data is invariant
under admissible high-frequency relabeling gauge transformations at
leading local inertial short-wave order. The leading fast pure-gauge
piece is longitudinal,

$$
n_i v_j+n_j v_i,
$$

and the TT projector annihilates it for unit propagation direction
\(n_i n_i=1\). Slow gauge-envelope terms remain in the
\(\lambda/L\)-suppressed class established by the averaging closure.

Discharge files:

- `development/covariant_lifts/radiative_gauge_invariance/radiative_gauge_invariance_note.md`
- `vacuum_forge/src/field_equation_trials/016_radiative_gauge_invariance/radiative_gauge_invariance.py`

### General Time-Dependent Vector Sector

The stationary 012 frame-dragging closure has been lifted to the linear
time-dependent transverse vector sector. In transverse gauge,

$$
G_{ti}^{(1)}=-{1\over2}\Delta w_i,
$$

and

$$
G_{ij}^{(1)}
=
-{1\over 2c^2}
\left(\partial_i\dot w_j+\partial_j\dot w_i\right).
$$

The stationary limit recovers 012 exactly, and source-free transverse
vector Fourier modes have zero amplitude for \(k\neq0\), not a
propagation law.

Discharge files:

- `development/covariant_lifts/vector_time_dependent/vector_time_dependent_note.md`
- `vacuum_forge/src/field_equation_trials/017_vector_time_dependent/vector_time_dependent.py`

### In-House Closure Uniqueness

The Deser self-coupled spin-2 closure citation has been retired as an
active rigor debt under the stated local, two-derivative,
no-extra-field, torsion-free first-order scope. The 018 proof program
checks:

```text
massless spin-2 + relabeling gauge symmetry + universal coupling
+ self-energy coupling + locality/two-derivative/no-extra-field
consistency => Einstein-Hilbert/Palatini closure
```

up to the admitted cosmological term, boundary terms, normalization
fixed elsewhere, inert four-dimensional Gauss-Bonnet, and field
redefinitions.

The discharge chain proves conservation-forced self-coupling, finite
Palatini closure, exhaustiveness of the local first-order
two-derivative monomial basis under the no-extra-field assumptions,
elimination of the independent connection, exclusion of all higher-H
mismatch directions, reduction of equal-coefficient higher-H terms to
nonlinear metric-density variable choice, and final term-class
accounting.

Discharge files:

- `development/closure_uniqueness/`
- `vacuum_forge/src/field_equation_trials/018_closure_uniqueness/`

### Covariant Static Lift (C2/C3)

The static bookkeeping sector's reduced theorems are the covariant
static spherical content of the closed parent:

- the areal flux law is the covariant tt-equation with the
  gauge-invariant Misner-Sharp mass
  \(m = (c^2 r/2G)(1-(\nabla r)^2)\) as the enclosed source,
  \(m' = (4\pi r^2/c^2)\rho\), identically;
- the P7' shadow \(AB=1\) is the chart-free statement
  \((\nabla r)^2 = -\xi^2/c^2\), with the C3 t-r block identity
  verified in an arbitrary radial gauge (shadow variable
  \(a b/R'^2\));
- the C2 bootstrap equation is the covariant vacuum tt-equation on the
  compensated branch, \(d/dr[r^2 G^t{}_t] = r\,\Delta_{\rm areal}A\),
  with coinciding solution families under asymptotic flatness and the
  angular equation implied (Bianchi);
- staticity is derived (Birkhoff-type): \(G_{tr} = \dot B/(rB)\) kills
  time dependence, and the residual \(h(t)\) is pure relabeling
  (Kretschmann \(= 12 r_s^2/r^6\) for arbitrary \(h\)).

Discharge files:

- `development/covariant_lifts/static_covariant_lift/static_covariant_lift_note.md`
- `vacuum_forge/src/field_equation_trials/019_static_covariant_lift/static_covariant_lift.py`

### Nonlinear Stability (scoped)

In-house at full nonlinearity in the spherical sector: vacuum plus a
regular center force flat uniquely (the Birkhoff family has
\(K = 12 C_1^2/r^6\); regularity kills \(C_1\)), and the Misner-Sharp
mass satisfies \(m' = (4\pi r^2/c^2)\rho \ge 0\) exactly, so the
negative static reservoir cannot decay, be mined, or drive a
quasilocal mass negative at any field strength. The quadratic sector
signature (TT positive; scalar/vector constraint-type) is inherited
from G03/017 and re-verified.

The global small-data statement (Minkowski-asymptotic data disperse)
is carried as an **external mathematical import** of the Fierz-Pauli
class: Christodoulou-Klainerman 1993 / Lindblad-Rodnianski 2010 are
theorems of PDE analysis about the equations the 018 closure fixed,
with no gravitational phenomenology as input and no framework
coefficient depending on them. An in-house re-derivation at that scale
is declared out of scope by decision and recorded visibly, not carried
as a hidden debt.

Discharge files:

- `development/nonlinear_stability/nonlinear_stability_note.md`
- `vacuum_forge/src/field_equation_trials/020_nonlinear_stability/nonlinear_stability_scoped.py`

## Remaining Rigor Debts

As of this record (2026-07-01), no active proof debts remain on the
field-equation derivation chain itself. The metric-branch input audit
(quadratic-vs-Finsler selector) remains open as a scope limitation on
the novelty claim, recorded in `05_open_obligations.md` — it bounds
what the proof claims to derive from P2 alone; it does not touch the
derivation's validity within the declared SR branch.

The recorded external mathematical imports (Fierz-Pauli 1939 linear
uniqueness; CK93/LR10 global small-data stability) are not debts: no
coefficient moves with them, and each is stated with its import class
in place.
