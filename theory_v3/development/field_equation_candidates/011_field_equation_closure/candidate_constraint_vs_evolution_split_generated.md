# Candidate Constraint Versus Evolution Split

## Canonical Filename

```text
candidate_constraint_vs_evolution_split.md
```

This generated copy may be saved under a suffix if the sandbox locks the canonical filename.

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a final Hamiltonian split, not a covariant constraint-propagation proof, and not a completed parent conservation identity. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_constraint_vs_evolution_split.py
```

The guiding question was:

```text
Which fields are constraints, which relax, and which propagate?
```

The answer is:

```text
A:
  constraint

B:
  reduced gauge-conditioned companion

W_i:
  transverse vector response, not free radiation

h_ij^TT:
  true propagating radiation

kappa:
  non-inertial trace relaxation, not breathing radiation

A_rad:
  rejected ordinary scalar radiation
```

The next gap is:

```text
the parent identity that enforces this split.
```

---

## Why This Study Matters

The no-double-counting constraints say which sources must not feed multiple independent gravity sectors.

This study asks the companion question:

```text
Which field sectors are allowed to propagate?
```

Without this split, a constrained variable can accidentally become a new radiation channel.

The two most dangerous cases are:

```text
A becoming scalar radiation,
kappa becoming breathing radiation.
```

Both remain forbidden.

---

## Dynamics Inventory

| Field | Classification | Propagates? | Status |
|---|---|---|---|
| \(A\) | constraint / elliptic-like scalar sector | No ordinary long-range scalar radiation; static / constraint field | DERIVED_REDUCED |
| \(B\) | gauge-conditioned companion to \(A\) in exterior | No independent propagation in current reduced exterior | DERIVED_REDUCED |
| \(W_i\) | transverse vector constraint in stationary limit; possible retarded response dynamically | Not currently a free radiation sector; source-tied vector response | STRUCTURAL |
| \(h_{ij}^{TT}\) | true propagating radiative degree of freedom | Yes: ordinary long-range gravitational radiation | STRUCTURAL |
| \(\kappa\) | non-inertial relaxation / constrained trace response | No: no independent momentum channel; no ordinary breathing wave | STRUCTURAL |
| \(A_{\rm rad}\) | rejected ordinary massless scalar radiation sector | No; rejected unless separately derived and controlled | REJECTED |
| \(\Sigma_{\rm creation}\) | excluded from ordinary closed-gravity evolution | Not a field; source / regime switch | CONSTRAINED |
| \(\Gamma_{\rm relax}\) | energy-transfer / restoration term, not propagating mode | No; local restoration / accounting term | STRUCTURAL |

---

## A Sector

The \(A\)-sector is classified as:

```text
constraint / elliptic-like scalar sector
```

Schematic equation:

\[
\Delta_{\rm areal}A
=
\frac{8\pi G}{c^2}\rho.
\]

It does not propagate as ordinary scalar radiation.

Status:

```text
DERIVED_REDUCED
```

Risk:

```text
turning the static scalar constraint into a propagating scalar wave.
```

Missing:

```text
full nonlinear nonspherical constraint propagation.
```

---

## B Sector

The \(B\)-sector is classified as:

```text
gauge-conditioned companion to A in exterior.
```

Schematic relation:

\[
AB=e^{2\kappa}.
\]

For exterior:

\[
\kappa=0,
\]

so:

\[
B=\frac{1}{A}.
\]

Status:

```text
DERIVED_REDUCED
```

Risk:

```text
treating a reduced gauge relation as independent dynamics.
```

Missing:

```text
covariant gauge / physical split.
```

---

## W_i Sector

The \(W_i\)-sector is classified as:

```text
transverse vector constraint in stationary limit;
possible retarded response dynamically.
```

Schematic equation:

\[
\nabla\times\nabla\times W
=
-\frac{\alpha_W}{2K_c}j_T.
\]

It is not currently a free radiation sector.

Status:

```text
STRUCTURAL
```

Risk:

```text
importing electromagnetic-like vector waves or GR shift dynamics by hand.
```

Missing:

```text
dynamic propagation / retardation law and normalization.
```

---

## h_ij^TT Sector

The \(h_{ij}^{TT}\)-sector is classified as:

```text
true propagating radiative degree of freedom.
```

Schematic equation:

\[
\Box h_{ij}^{TT}
=
-C_TS_{ij}^{TT}.
\]

This is the ordinary long-range gravitational radiation sector.

Status:

```text
STRUCTURAL
```

Risk:

```text
correct form but coefficient / source identity matched to GR.
```

Missing:

```text
C_T and action stiffness derivation.
```

---

## Kappa Sector

The \(\kappa\)-sector is classified as:

```text
non-inertial relaxation / constrained trace response.
```

Schematic equation:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

It does not propagate.

It has:

```text
no independent momentum channel,
no ordinary breathing wave.
```

Status:

```text
STRUCTURAL
```

Risk:

```text
becoming a hidden scalar wave or repair knob.
```

Missing:

```text
K_kappa,
mu_kappa,
chi_kappa,
S_trace_effective,
covariant origin.
```

---

## A_rad Sector

The \(A_{\rm rad}\)-sector is classified as:

```text
rejected ordinary massless scalar radiation sector.
```

Schematic rule:

\[
{\rm source}(A_{\rm rad}\ {\rm ordinary\ massless})=0.
\]

Status:

```text
REJECTED
```

Risk:

```text
breathing / scalar radiation contradicts safety constraints.
```

Missing:

```text
parent identity proving absence / suppression.
```

---

## Sigma_creation

The \(\Sigma_{\rm creation}\) term is classified as:

```text
excluded from ordinary closed-gravity evolution.
```

Schematic rule:

\[
\Sigma_{\rm creation}=0
\]

in the ordinary closed regime.

Status:

```text
CONSTRAINED
```

Risk:

```text
nonconservative source contaminates ordinary closure.
```

Missing:

```text
active-regime trigger and accounting.
```

---

## Gamma_relax

The \(\Gamma_{\rm relax}\) term is classified as:

```text
energy-transfer / restoration term, not propagating mode.
```

Schematic rule:

```text
Gamma_relax acts on trace imbalance, not A_mass_flux.
```

Status:

```text
STRUCTURAL
```

Risk:

```text
cosmetic damping or energy disappearance.
```

Missing:

```text
vacuum energy destination / parent balance.
```

---

## True Radiation Rule

Current radiation rule:

```text
ordinary long-range gravitational radiation is TT-only.
```

Allowed:

```text
h_ij^TT propagates.
```

Constrained or rejected:

```text
A_rad ordinary scalar radiation is rejected.
kappa breathing radiation is rejected.
W_i free vector radiation is not currently derived.
```

This rule can be changed only by a separate derivation and observational control.

Status:

```text
CONSTRAINED
```

---

## Constraint-Like Fields

Constraint-like fields:

```text
A:
  scalar mass / monopole constraint

B:
  reduced gauge-conditioned reciprocal companion to A

W_i:
  transverse vector response in stationary/current sector

kappa:
  non-inertial trace / volume relaxation constraint
```

These may have time-dependent source response.

They are not currently ordinary free radiative degrees of freedom.

---

## Evolving / Radiating Fields

Evolving / radiating fields:

```text
h_ij^TT:
  propagating tensor radiation
```

Possibly dynamic but not yet radiative:

```text
W_i:
  may require retardation / dynamic source response

kappa:
  first-order relaxation toward local minimum
```

Rejected as ordinary radiative fields:

```text
A_rad,
kappa breathing wave.
```

---

## Failure Controls

The constraint/evolution split fails if:

1. \(A\) is promoted to a free scalar radiation field.
2. \(\kappa\) gains a second-order \(\Box\) equation and momentum channel.
3. \(W_i\) is treated as a free vector radiation field without derivation.
4. \(h_{ij}^{TT}\) coupling is copied from GR while claimed derived.
5. \(\Gamma_{\rm relax}\) hides energy loss rather than vacuum exchange.
6. \(\Sigma_{\rm creation}\) appears in ordinary closed gravity.
7. Constraint propagation is not compatible with source conservation.

---

## Parent Identity Requirements

The parent identity must explain:

```text
how constraints propagate consistently,
why TT modes alone carry ordinary radiation,
why scalar trace relaxes but does not radiate,
why vector current response is transverse,
how energy/source conservation is maintained.
```

Without this, the split is disciplined but not derived.

Status:

```text
UNFINISHED
```

---

## What This Study Established

This study established:

1. \(A\) is a scalar constraint, not scalar radiation.
2. \(B\) is a reduced companion relation, not independent propagation.
3. \(W_i\) is a transverse vector response, not currently free radiation.
4. \(h_{ij}^{TT}\) is the true propagating radiation sector.
5. \(\kappa\) is non-inertial trace relaxation, not breathing radiation.
6. \(A_{\rm rad}\) remains rejected.
7. \(\Sigma_{\rm creation}\) is excluded from ordinary closed gravity.
8. \(\Gamma_{\rm relax}\) is a restoration/accounting term, not a propagating mode.
9. The split is disciplined but not parent-derived.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not prove constraint propagation.

It did not derive \(W_i\)'s dynamic retardation law.

It did not derive \(h_{ij}^{TT}\)'s coupling.

It did not derive \(\kappa\)'s covariant origin.

It did not derive \(\Gamma_{\rm relax}\)'s energy destination.

It only classified the current constraint/evolution split.

---

## Current Best Interpretation

Current split:

```text
A:
  constraint

B:
  reduced gauge-conditioned companion

W_i:
  transverse vector response, not free radiation

h_ij^TT:
  true propagating radiation

kappa:
  non-inertial trace relaxation, not breathing radiation

A_rad:
  rejected ordinary scalar radiation
```

---

## Next Development Target

The next script should be:

```text
candidate_conservation_identity_requirements.py
```

Purpose:

```text
List the parent identities needed to justify the constraints.
```

Reason:

```text
The split is now clear; the next gap is the identity that enforces it.
```

Expected result:

```text
A requirements ledger for conservation / Bianchi-like closure:
  scalar constraint propagation,
  current decomposition,
  TT source conservation,
  kappa non-radiative trace relaxation,
  boundary mass preservation,
  exclusion of Sigma_creation in ordinary closure.
```

---

## Summary

The constraint/evolution split is now explicit:

```text
only h_ij^TT is ordinary long-range radiation.
```

Everything else is constrained, source-tied, relaxing, gauge-conditioned, or rejected.

The next goblin door is conservation identity.
