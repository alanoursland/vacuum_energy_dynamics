# Candidate Parent Identity Exclusion Constraints

## Canonical Filename

```text
candidate_parent_identity_exclusion_constraints.md
```

This document summarizes the output of:

```text
candidate_parent_identity_exclusion_constraints.py
```

---

## What This Document Is

This document is a development note for the `12_parent_identity_and_recombination/` group.

It is not a parent identity, not a derivation of closure, and not a covariant recombination map. It does not add a formal commitment to the theory.

Its purpose is to rule out false parent identities before attempting to write a positive one.

The guiding question was:

```text
What can the parent identity not be?
```

The answer is:

```text
The parent identity cannot be:
  a decorative Bianchi restatement,
  an ordinary scalar A wave,
  Box kappa,
  rho double-sourced into kappa,
  nonzero exterior kappa charge,
  trace contamination of TT,
  longitudinal current sourcing W_i,
  boundary smoothing changing exterior mass,
  Sigma_creation in ordinary closure,
  GR coefficients inserted as derivation,
  metric recombination copied from GR.
```

The remaining parent-identity space is already strongly constrained.

---

## Why This Study Matters

Group 11 ended with a coherent reduced equation ledger but no closure.

The missing object was:

```text
parent conservation / recombination identity.
```

The dangerous move would be to immediately write a formal-looking parent identity and mistake it for a derivation.

This study prevents that by asking first:

```text
What parent identity forms are already forbidden?
```

The answer cuts away false parents before naming the real one.

---

## Compact Exclusion Ledger

| Exclusion | Forbidden Form | Status | Surviving Requirement |
|---|---|---|---|
| X1: Decorative Bianchi restatement | \({\rm Div}\,E_{\rm parent}=0\) because GR has \(\nabla_\mu G^{\mu\nu}=0\) | EXCLUDED | Define \(E_{\rm parent}\) and show its reduced projections force the known sectors |
| X2: Ordinary scalar \(A\) wave | \(\Box A=\) scalar source as ordinary long-range gravitational radiation | FORBIDDEN | Parent identity must propagate the \(A\) constraint through source continuity, not \(\Box A\) radiation |
| X3: Ordinary \(\Box\kappa\) trace wave | \(\Box\kappa=\alpha\,{\rm trace}\) or \(\alpha p\) | FORBIDDEN | Trace / pressure may shift \(\kappa_{\min}\), followed by first-order relaxation only |
| X4: \(\rho\) double-sourced into \(\kappa\) | \(\rho\) sources both \(A\) and independent long-range \(\kappa\) | FORBIDDEN | Parent identity must route \(\rho\) to \(A\) and prevent \(\rho\)-sourced \(\kappa\) charge |
| X5: Nonzero exterior \(\kappa\) charge | \(\int S_\kappa d^3x\ne0\) for ordinary closed matter | FORBIDDEN | Parent identity must enforce \(\kappa\)-charge neutrality / projection or boundary cancellation |
| X6: Trace contamination of TT radiation | trace or pressure directly sources \(h_{ij}^{TT}\) | FORBIDDEN | Parent identity must separate \(P_{TT}\) stress from trace stress |
| X7: Longitudinal current sources \(W_i\) | \(P_Lj\) sources transverse vector \(W_i\) / frame dragging | FORBIDDEN | Parent identity must preserve \(j=P_Tj+P_Lj\) |
| X8: Free vector radiation imported by analogy | \(W_i\) becomes a free propagating vector wave without derivation | EXCLUDED | Any retarded \(W_i\) dynamics must be derived and must not add forbidden radiation modes |
| X9: Boundary relaxation changes exterior mass | \(\kappa\) / joint-minimum smoothing changes \(M_{\rm ext}\) or exterior \(1/r\) coefficient | FORBIDDEN | Parent identity must preserve exterior \(A\) flux under \(\kappa\) relaxation |
| X10: \(\Sigma_{\rm creation}\) in ordinary closure | \(\Sigma_{\rm creation}\ne0\) in ordinary closed gravity | FORBIDDEN | Parent identity must separate ordinary closed regime from active creation regimes |
| X11: Relaxation as energy loss | \(\Gamma_{\rm relax}\) removes energy without a destination variable | EXCLUDED | Parent identity must include or imply vacuum configuration energy accounting |
| X12: GR coefficient insertion as derivation | insert Lense-Thirring normalization, \(C_T\), or tensor flux coefficient because GR has them | EXCLUDED | Parent identity may target GR coefficients, but must not claim them without derivation |
| X13: Metric recombination copies GR by form | \(g_{tt},g_{0i},g_{ij}\) assigned full GR weak-field form before parent recombination is derived | EXCLUDED | Parent identity must produce a recombination map preserving source splits and constraints |
| X14: Near-boundary deviation promoted before closure | claim measured / predicted near-boundary GR deviation from joint-minimum diagnostic alone | EXCLUDED | Keep diagnostic before prediction until recombination and magnitude are derived |

---

## Status Counts

The run counted:

```text
EXCLUDED: 6
FORBIDDEN: 8
```

Interpretation:

```text
The candidate parent space is already strongly constrained.
Most false parents are forbidden because they reintroduce scalar radiation,
double-count sources, tune mass, or import GR by hand.
```

---

## Surviving Parent Requirements

Any surviving parent identity must:

1. Define \(E_{\rm parent}\) and \(B_{\rm source}\) rather than restating Bianchi compatibility.
2. Keep \(A\) as a scalar constraint, not ordinary scalar radiation.
3. Keep \(\kappa\) first-order / non-inertial, not \(\Box\kappa\).
4. Route \(\rho\) to \(A\) without independent long-range \(\kappa\) charge.
5. Preserve exterior \(A\) mass flux under boundary / \(\kappa\) relaxation.
6. Split \(j\) into transverse vector source and longitudinal continuity.
7. Split TT stress from trace stress.
8. Exclude \(\Sigma_{\rm creation}\) in ordinary closed gravity.
9. Account for \(\Gamma_{\rm relax}\) as vacuum configuration exchange.
10. Derive or honestly label vector / tensor coefficients.
11. Produce recombination without scalar double-counting.
12. Keep near-boundary deviation diagnostic-only until magnitude is derived.

Status:

```text
CONSTRAINED
```

---

## Hardest Exclusions to Make Constructive

The hardest exclusions are:

### 1. Decorative Bianchi Restatement

Need:

```text
actual definitions and reduced implications.
```

The identity cannot simply be:

```text
Div E_parent = 0
```

because GR has a divergence identity.

It must show why the reduced sectors follow.

---

### 2. Scalar A Not Radiation

Need:

```text
constraint propagation from continuity.
```

The parent identity must explain why \(A\) remains a constraint / mass-flux response rather than becoming:

\[
\Box A = S.
\]

---

### 3. Kappa Not Box Kappa

Need:

```text
trace-minimum relaxation identity.
```

The parent identity must explain why trace / pressure shifts \(\kappa_{\min}\), followed by first-order relaxation, instead of producing:

\[
\Box\kappa=\alpha S.
\]

---

### 4. Boundary Relaxation Preserves Exterior Mass

Need:

```text
boundary mass theorem.
```

The parent identity must preserve:

\[
\delta M_{\rm ext}\big|_{\kappa\ {\rm boundary\ relaxation}}=0.
\]

---

### 5. Metric Recombination Not GR Import

Need:

```text
recombination map from sector identity.
```

The parent identity must not merely assign GR-shaped metric components by hand.

---

## What Remains Possible

Still possible parent identity classes:

```text
a divergence / balance identity with explicit sector projectors,
a constrained scalar sector plus TT radiative sector,
a transverse current / vector response sector that is source-tied,
a trace / minimum relaxation channel for kappa,
a boundary / interface identity preserving exterior mass,
a recombination map generated after source / projector splitting.
```

But none of these are derived yet.

Status:

```text
UNRESOLVED
```

---

## What This Study Established

This study established:

1. The parent identity cannot be a decorative Bianchi restatement.
2. \(A\) cannot become ordinary scalar radiation.
3. \(\kappa\) cannot become a \(\Box\kappa\) trace wave.
4. \(\rho\) cannot source independent long-range \(\kappa\).
5. Exterior \(\kappa\) charge must vanish.
6. Trace stress cannot feed TT radiation.
7. Longitudinal current cannot source \(W_i\).
8. \(W_i\) cannot be promoted to free vector radiation by analogy.
9. Boundary relaxation cannot change exterior mass.
10. \(\Sigma_{\rm creation}\) is excluded from ordinary closed gravity.
11. \(\Gamma_{\rm relax}\) must be energy-accounted.
12. GR coefficients cannot be inserted as derivations.
13. Metric recombination cannot copy GR by form.
14. Near-boundary deviation remains diagnostic-only.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive sector projectors.

It did not derive \(A\)-constraint propagation.

It did not derive \(\kappa\)'s trace relaxation identity.

It did not derive boundary mass preservation.

It did not derive metric recombination.

It only narrowed the parent identity candidate space.

---

## Current Best Interpretation

The parent identity cannot be:

```text
a decorative Bianchi restatement,
an ordinary scalar A wave,
Box kappa,
rho double-sourced into kappa,
nonzero exterior kappa charge,
trace contamination of TT,
longitudinal current sourcing W_i,
boundary smoothing changing exterior mass,
Sigma_creation in ordinary closure,
GR coefficients inserted as derivation,
metric recombination copied from GR.
```

This is not yet construction.

It is successful exclusion.

---

## Next Development Target

The next script should be:

```text
candidate_parent_identity_reduced_implications.py
```

Purpose:

```text
State what the parent identity must imply in each reduced sector.
```

Reason:

```text
After ruling out false parents, define the reduced-sector tests for any surviving parent.
```

Expected result:

```text
A reduced-sector implication ledger:
  static spherical A-sector,
  exterior B=1/A when kappa=0,
  weak scalar constraint,
  transverse vector W_i,
  TT tensor radiation,
  non-radiative kappa relaxation,
  boundary mass preservation,
  ordinary Sigma_creation=0.
```

---

## Summary

Group 12 begins by cutting away false parents.

The first result is:

```text
The parent identity candidate space is already narrow.
```

The next result should define what any surviving parent must imply.
