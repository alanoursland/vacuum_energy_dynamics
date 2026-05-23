# Candidate Conservation Identity Requirements

## What This Document Is

This document is a development note for the `08_covariant_parent_structure/` group.

It is not a derivation of conservation laws, not a Bianchi identity, and not a closed parent field equation. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_conservation_identity_requirements.py
```

The guiding question was:

```text
What conservation or Bianchi-like identities must a parent theory supply so
sector sources are not independent hand assignments?
```

The answer is:

```text
Conservation/source identities are not solved.
```

The script found:

```text
SATISFIED_REDUCED: 0
PARTIAL: 4
MISSING: 4
RISK: 0
```

This is an important result.

It means source-geometry compatibility is still a parent-theory gap.

---

## Method Note

This script continued the stricter group-08 style.

It classified requirements using:

```text
SATISFIED_REDUCED
PARTIAL
MISSING
RISK
```

Unlike earlier algebraic consistency probes, this script did not simply check whether a proposed identity worked.

It asked whether the theory actually has the identities a parent structure would need.

The answer was no.

That is useful.

---

## Conservation Identity Problem

The core problem is:

```text
Sector sources cannot be independent hand assignments.
```

The current sector source assignments are approximately:

```text
A_constraint <- mass density / total mass
W_i          <- mass current / angular momentum
kappa        <- pressure / stress / trace candidate
h_ij^TT      <- trace-free quadrupole derivatives
```

A parent theory must tie these together through continuity-like or Bianchi-like identities.

Otherwise, sector equations may not close consistently.

---

## C1: Mass Continuity for Scalar Source

Status:

```text
PARTIAL
```

Current support:

```text
Scalar A_constraint uses mass density rho or total mass M.
Binary guardrails used conserved M.
```

Parent must supply:

```text
Continuity equation relating mass density and current, for example:
partial_t rho + div j = 0
in the appropriate limit.
```

Risk if missing:

```text
A_constraint source could change inconsistently with matter flow.
```

This is partial because the reduced studies use conserved mass correctly, but they do not derive continuity from a parent theory.

---

## C2: Current Conservation for W_i

Status:

```text
MISSING
```

Current support:

```text
W_i is assigned to mass current/angular momentum, but no equation or
conservation identity has been derived.
```

Parent must supply:

```text
Relation between W_i source, mass current, angular momentum, and continuity
identities.
```

Risk if missing:

```text
Frame-dragging sector could violate source conservation or double-count gauge
shift.
```

This is a blocking gap.

The vector sector cannot become a real parent sector until current conservation and gauge behavior are clarified.

---

## C3: Stress / Pressure Consistency for Kappa

Status:

```text
MISSING
```

Current support:

```text
Kappa is assigned to pressure/stress/trace candidate response.
```

Parent must supply:

```text
A stress/trace identity showing when kappa is sourced and why it is suppressed
in exterior vacuum.
```

Risk if missing:

```text
Kappa may be arbitrary or conflict with scalar/tensor sectors.
```

This is another blocking gap.

The current \(\kappa\) interpretation is useful, but not yet sourced by a parent identity.

---

## C4: Quadrupole Source Consistency for h_ij^TT

Status:

```text
PARTIAL
```

Current support:

```text
Tensor studies use trace-free quadrupole derivatives and conservation kills
monopole/dipole scalar radiation proxies.
```

Parent must supply:

```text
Derive quadrupole radiation source from conserved stress-energy or
vacuum-source identities.
```

Risk if missing:

```text
Quadrupole source may be matched rather than derived.
```

This is partial.

The tensor source structure is strong at the reduced level, but not yet derived from a conserved parent stress-energy structure.

---

## C5: Constraint Propagation

Status:

```text
MISSING
```

Current support:

```text
A_constraint is treated as elliptic and h_ij^TT as hyperbolic.
```

Parent must supply:

```text
Show that if constraints hold initially, evolution preserves them.
```

Risk if missing:

```text
Constraint equations could become inconsistent over time.
```

This is a major parent-theory requirement.

A theory with both constraints and evolution equations must explain why evolution does not violate the constraints.

---

## C6: No-Source Exterior Consistency

Status:

```text
PARTIAL
```

Current support:

```text
Exterior scripts set rho=0, kappa suppressed, A_rad controlled, and h_ij^TT
source-free except radiation.
```

Parent must supply:

```text
A unified vacuum identity defining which sectors may remain active in
source-free regions.
```

Risk if missing:

```text
Exterior vacuum could contain incompatible leftover sector sources.
```

This is partial because the reduced exterior policy is coherent, but the parent vacuum identity is not derived.

---

## C7: Bianchi-Like Geometric Identity

Status:

```text
MISSING
```

Current support:

```text
No parent geometric identity exists yet.
```

Parent must supply:

```text
A geometric identity analogous in role to Bianchi conservation, ensuring
source-geometry compatibility.
```

Risk if missing:

```text
The theory cannot be a covariant parent; sector equations may not close.
```

This is the largest missing structure.

Without a Bianchi-like identity or equivalent closure mechanism, the reduced sector bundle cannot be called a covariant parent theory.

---

## C8: Energy Flux Balance

Status:

```text
PARTIAL
```

Current support:

```text
Tensor radiation energy-flux scaling was checked at reduced level.
```

Parent must supply:

```text
Energy balance law connecting source energy loss to tensor radiation and
excluding uncontrolled scalar/vector losses.
```

Risk if missing:

```text
Radiation sector may not conserve energy or may miss extra channels.
```

This remains partial.

The scaling is promising, but energy balance is not derived.

---

## Source-Sector Compatibility Table

The script produced this table:

| Sector | Source object | Required identity | Status |
|---|---|---|---|
| \(A_{\rm constraint}\) | \(\rho / M\) | mass continuity | PARTIAL |
| \(W_i\) | mass current / angular momentum | current continuity / angular momentum relation | MISSING |
| \(\kappa\) | pressure / stress / trace | stress/trace consistency | MISSING |
| \(h_{ij}^{TT}\) | \(Q_{ij}^{TF}\) derivatives | conserved quadrupole source derivation | PARTIAL |
| constraints | initial data | constraint propagation | MISSING |
| radiation | energy flux | source energy balance | PARTIAL |

This table is the current map of source-identity gaps.

---

## Blocking Identity Gaps

The script identified these blocking missing identities:

```text
C2: Current conservation for W_i
C3: Stress/pressure consistency for kappa
C5: Constraint propagation
C7: Bianchi-like geometric identity
```

These must be supplied before claiming a closed parent field equation.

---

## Minimal Safe Policy

Until parent identities exist:

1. Treat source couplings as reduced-sector assignments, not final laws.
2. Do not claim full stress-energy coupling.
3. Keep \(A_{\rm rad}\) and vector radiation controlled unless energy balance permits them.
4. Treat tensor quadrupole power scaling as matched/reduced, not derived.
5. Mark the \(\kappa\) source law as open.
6. Do not claim covariant closure.

This is the safe policy for the current stage.

---

## What This Study Established

This study established:

1. Conservation/source identities are not solved.
2. No conservation identity requirement is fully satisfied at parent level.
3. Mass continuity assumptions are partially supported.
4. Quadrupole source structure is partially supported.
5. Tensor radiation energy scaling is partially supported.
6. \(W_i\) current identity is missing.
7. \(\kappa\) stress/trace identity is missing.
8. Constraint propagation is missing.
9. A Bianchi-like geometric identity is missing.

---

## What This Study Did Not Establish

This study did not derive conservation laws.

It did not derive stress-energy coupling.

It did not derive a Bianchi-like identity.

It did not derive constraint propagation.

It did not derive energy balance.

It only identified what the parent theory must supply.

---

## Current Best Interpretation

The reduced sector program has source assignments.

It does not yet have source-geometry closure.

The current safe statement is:

```text
The sector sources are reduced assignments, not final parent laws.
```

The parent theory must still derive:

```text
mass continuity,
current conservation,
stress/trace consistency,
constraint propagation,
Bianchi-like closure,
energy-flux balance.
```

---

## Next File

The script recommended closing group 08 with:

```text
covariant_parent_structure_summary.md
```

Reason:

```text
Group 08 has identified its main blockers:
  gauge structure,
  recombination,
  invariant diagnostics,
  conservation identities.
```

A summary should state the parent-theory gap clearly.

---

## Summary

The conservation identity requirements study is the hardest group-08 check so far.

It found:

```text
SATISFIED_REDUCED: 0
PARTIAL: 4
MISSING: 4
```

This means conservation/source compatibility is not yet solved.

The biggest missing structures are:

```text
current/W_i identity,
kappa stress/trace identity,
constraint propagation,
Bianchi-like geometric identity.
```

Therefore the reduced theory is not yet a closed covariant parent.

That is the correct conclusion.
