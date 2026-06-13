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

## Remaining Rigor Debts

As of this record, the active proof debts are:

- in-house closure-uniqueness proof replacing the Deser citation;
- covariant lift of the C2/C3 static bookkeeping sector;
- nonlinear stability.

These are rigor debts only. None carries a coefficient or reopens the
closed field equations.

