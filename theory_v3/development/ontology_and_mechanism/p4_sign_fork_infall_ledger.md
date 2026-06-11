# P4 Sign Fork and the Infall Energy Ledger

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or field equation. It does not modify P4. It records a fork in postulate-space that was found by running the energy ledger for quasi-static two-body infall under different sign commitments for configuration energy, and it records a concrete tension between the quadratic gradient-energy toy and the burden-reduction mechanism notes in this folder.

The central finding is:

```text
The sign of the two-body configuration-energy cross-term decides whether
local gravitational infall is traceless configuration exchange or traceful
substance exchange. The current postulates do not fix this sign. Candidate
functionals do, so the fork is killable per candidate.
```

Tiny goblin rule:

```text
Before you choose where the treasure comes from,
check whether the second hole makes the first hole cheaper or dearer.
```

---

## 1. The Question

When a mass falls toward another mass, it gains kinetic energy. P6 commits the framework to that kinetic energy being sourced by vacuum exchange. The open question is the realization:

```text
traceless realization:
  kinetic energy is supplied by a DECREASE in configuration energy;
  no net vacuum substance change; J_kappa = 0 form.

traceful realization:
  configuration energy does NOT decrease (or increases);
  kinetic energy must be paid by net vacuum substance destruction;
  J_kappa != 0 form.
```

The v2 obstruction identified substance exchange with traceful sourcing because v2 carried a scalar-metric structure. v3's directional ontology (P3a, P4) breaks that identification: both realizations are currently open. This note shows the two realizations are distinguished by one computable quantity.

---

## 2. The Discriminator: the Two-Body Cross-Term

Let `E_config[separation r]` be the total configuration energy of the vacuum around two masses at separation `r`, under a candidate configuration-energy functional.

Define the cross-term as:

```text
X(r) = E_config(two masses at r) - E_config(two masses at infinite separation)
```

The energy ledger for quasi-static infall from infinity to `r` is:

```text
vacuum substance destroyed = Delta_KE + X(r_infinity -> r)
```

with `Delta_KE = G m1 m2 / r` in the Newtonian limit.

The fork:

```text
X < 0 and |X| = Delta_KE:
  configuration energy supplies the kinetic energy.
  No net substance change required. Traceless realization available.
  This is the Newtonian field-energy bookkeeping (negative interaction
  field energy) restated in framework vocabulary.

X >= 0:
  the vacuum must pay for BOTH the kinetic energy and the configuration
  increase. Net substance destruction is forced. Traceful realization.
```

---

## 3. The Quadratic Toy Forces the Traceful Branch

Take the simplest functional consistent with P4's positivity language: positive-definite quadratic in the gradient of the weak-field potential,

```text
E_config = (1 / 8 pi G) integral |grad Phi|^2 dV,
```

with `Phi = Phi_1 + Phi_2` by superposition in the weak field.

The cross-term evaluates exactly (same computation as the electrostatic interaction energy of two like charges):

```text
(1 / 4 pi G) integral grad Phi_1 . grad Phi_2 dV = + G m1 m2 / r.
```

So under the quadratic positive-definite functional:

```text
X(r) = + G m1 m2 / r > 0.
```

Combining wells COSTS configuration energy; it does not release it. The ledger then forces:

```text
vacuum substance destroyed = Delta_KE + X = 2 * Delta_KE.
```

A clean 50/50 split: half the destroyed vacuum's energy becomes kinetic energy of the mass, half becomes curvature energy of the deepened combined well. Infall is necessarily traceful in this branch, with a definite, computable substance budget.

---

## 4. Tension With the Burden-Reduction Notes

This result is in direct tension with two existing notes in this folder.

`gravity_as_vacuum_burden_reduction.md` proposes:

```text
When masses move closer together, their burdens can partially merge.
The combined constraint may be cheaper for the vacuum to maintain.
```

`positive_curvature_energy_J_curv.md` proposes:

```text
Ordinary gravitational potential energy is the negative cross-term
between positive curvature-configuration energies.
```

Both require `X < 0`: combining wells must be cheaper than separated wells.

The quadratic gradient functional gives `X > 0`. Therefore:

```text
The burden-reduction mechanism and the quadratic positive-definite
gradient functional are mutually exclusive.
```

This is not a defect in either note. It is a constraint surfaced by putting them in the same ledger:

- If the burden-reduction mechanism is right, the configuration-energy functional must be non-quadratic in a way that makes well-merging release energy (concave/saturating in gradient content, or carrying interface/smoothing terms that dominate the cross-term). That is a sharp design constraint on `K_strain`.
- If the functional is quadratic (or any form with positive cross-term), the burden-reduction account of attraction fails, attraction must be driven by P6's force content directly, and infall consumes vacuum substance at rate `2 * d(Delta_KE)/dt`.

Either way, one of the two currently coexisting pictures dies once a functional is chosen. They should not continue to be cited side by side without this flag.

---

## 5. The Wider Sign Fork

The infall ledger sits inside a three-branch fork on the sign structure of configuration energy.

| Branch | Infall ledger | Status of flat vacuum | First kill test |
|---|---|---|---|
| Positive-definite (P4 as written, quadratic toy) | Traceful; substance destroyed = 2 Delta_KE | Ground state, stable (P5 coherent) | kappa-leak / Cassini gamma bound on the predicted traceful budget |
| Globally negative | Traceless, Newtonian bookkeeping | NOT the ground state; flat is unstable; P5 architecture inverts | Flat-vacuum stability; gravitational waves would carry negative energy, contradicting binary-pulsar spin-down |
| Indefinite by sector | Traceless locally (trace/potential sector negative or coupling-mediated), positive radiative energy | Stable against shear; trace sector needs suppression | What principle assigns the signs? |

Notes on the branches:

```text
Globally negative appears killable immediately: it breaks P5's ground
state and gets the observed sign of gravitational-wave energy wrong.

Indefinite-by-sector matches the actual structure of GR, where the
conformal/trace mode enters the Einstein-Hilbert action with a
wrong-sign kinetic term while the transverse-traceless modes are
positive. It also maps onto the kappa/s decomposition already used in
the reduced exterior program, where binding enters through the rho-s
coupling term rather than through negative field-gradient energy.

If the framework's directional ontology could DERIVE the indefinite
signature (for example, temporal-direction vacuum extent entering the
energy with opposite sense to spatial), that would be an ontological
explanation for the conformal mode's wrong sign, which GR takes as
given. This question is the K_strain frontier restated.
```

---

## 6. Why This Fork Is Upstream of the Functional Search

Any candidate `K_strain` or configuration-energy functional implies:

```text
1. a sign for the two-body cross-term X (Section 2 discriminator),
2. a sign for radiative-mode energy (binary-pulsar anchor),
3. a stability verdict for flat vacuum (P5 anchor).
```

These three checks are cheap relative to the functional search itself, and any candidate that fails 2 or 3 is dead before detailed development. The fork therefore acts as a pre-filter for the candidate-functional program.

---

## 7. Proposed Scripts

```text
candidate_two_body_cross_term_sign.py
  Input: candidate functional (start with quadratic gradient toy).
  Compute E_config at separation r and at infinity; report sign and
  magnitude of X(r); report implied substance budget per Delta_KE.

candidate_traceful_infall_kappa_budget.py
  For the positive-definite branch: take substance budget 2*Delta_KE
  for a specified process (falling body; bound orbit), map to a
  kappa-sourcing rate under the reduced mode language, and bound the
  induced gamma-like deviation against the Cassini constraint.

candidate_sector_signature_stability.py
  For the indefinite branch: reduced kappa/s functional with opposite
  sector signs; check flat-vacuum stability with and without the
  M_kappa^2 suppression term; check radiative-sector energy sign.
```

---

## 8. Established

```text
The traceless/traceful realization of P6 exchange during infall is
decided by the sign of the two-body configuration-energy cross-term.

Under the positive-definite quadratic gradient functional, the
cross-term is +G m1 m2 / r, infall is traceful, and the substance
budget is exactly 2 * Delta_KE.

The burden-reduction mechanism notes require the opposite cross-term
sign and are therefore incompatible with the quadratic functional.

A globally negative configuration energy conflicts with P5's ground
state and with the observed positive energy of gravitational radiation.
```

---

## 9. Not Established

```text
Which branch nature uses.

That net substance change maps to trace-mode (kappa) sourcing; this is
plausible under the reduced mode language but the vacuum's mathematical
structure is open work.

The cross-term sign for any functional other than the quadratic toy.

Any covariant statement; everything here is weak-field/Newtonian-limit
ledger reasoning.

Any modification to P4, P5, or P6. This note records a fork, not a
revision.
```

---

## 10. Origin

This note records the outcome of a postulate-space reasoning session (June 2026) examining whether P6's vacuum exchange during infall must be traceful. The session began from the observation that v3's directional ontology reopens the traceless realization that v2's scalar structure excluded, then found that the choice is fixed per-functional by the infall ledger rather than being a free interpretive option.
