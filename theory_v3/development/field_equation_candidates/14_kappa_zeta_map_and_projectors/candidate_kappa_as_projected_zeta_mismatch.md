# Candidate Kappa As Projected Zeta Mismatch

## Canonical Filename

```text
candidate_kappa_as_projected_zeta_mismatch.md
```

This document summarizes the output of:

```text
candidate_kappa_as_projected_zeta_mismatch.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(P_{\rm trace}\), not a parent projector identity, and not a final \(\kappa\)-\(\zeta\) map.

Its purpose is to test whether projection can safely relate \(\kappa\) to:

\[
\zeta-\zeta_{\min}.
\]

The guiding question was:

```text
Can kappa be defined safely as P_trace(zeta-zeta_min)?
```

The answer is:

```text
Projected kappa is the best current relation target:

  kappa = P_trace(zeta-zeta_min)

Safer version:

  kappa = P_relax P_trace(zeta-zeta_min)

This is safe only if:
  P_trace removes exterior charge,
  P_trace excludes A-sector mass,
  P_trace annihilates TT,
  P_boundary enforces zero flux,
  P_recombination counts trace/volume once.
```

---

## Compact Projected-Map Ledger

| Entry | Condition | Status | Missing |
|---|---|---|---|
| PZ1: raw projected map | \(\kappa=P_{\rm trace}(\zeta-\zeta_{\min})\) | CANDIDATE | definition of \(P_{\rm trace}\) |
| PZ2: relaxed projected map | \(\kappa=P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min})\) | CANDIDATE | \(P_{\rm relax}\) definition and relation to \(\Gamma_{\rm relax}\) |
| PZ3: compensation requirement | \(\int P_{\rm trace}(\zeta-\zeta_{\min})d^3x=0\) or \(Q_\kappa=0\) | REQUIRED | \(Q_\kappa/Q_{\rm volume}\) relation and parent origin |
| PZ4: exterior fixed point | \(\zeta_{\rm ext}=0,\zeta_{\min,\rm ext}=0,\kappa_{\rm ext}=0\) | REQUIRED | exterior stability theorem |
| PZ5: zero boundary flux | \(F_\kappa(R+)=0\) and \(F_\zeta(R+)=0\) | REQUIRED | \(P_{\rm boundary}\) relation |
| PZ6: \(A\)-sector mass separation | \(\delta M_{\rm ext}|_{\rm projected\ zeta/\kappa}=0\) | REQUIRED | boundary mass theorem and scalar constraint propagation |
| PZ7: \(\epsilon/e_\kappa\) accounting | \(\epsilon_\zeta\) and \(e_\kappa\) counted separately; no \(K_{\rm lock}\) energy | SAFE_IF | whether \(e_\kappa\) is residual energy or should be absorbed later |
| PZ8: diagnostic versus energetic projection | \(P_{\rm trace}\) map may be diagnostic, energetic, or constraint-defining | UNRESOLVED | degree-of-freedom count |
| PZ9: trace / TT separation | \(P_{\rm trace}h_{TT}=0\) and \(P_{TT}P_{\rm trace}=0\) | CONSTRAINED | nonlinear / covariant projector structure |
| PZ10: no scalar wave promotion | no \(\Box\kappa\), no \(\Box\zeta\) | FORBIDDEN | parent proof of no scalar inertia |
| PZ11: recombination compatibility | \(A,\zeta,\kappa\) assembled once into \(g_{ij}\) | REQUIRED | \(P_{\rm recombination}\) |
| PZ12: recommended projected convention | \(\kappa=P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min})\), with \(K_{\rm lock}\) diagnostic only | RECOMMENDED | definitions of \(P_{\rm trace},P_{\rm relax},P_{\rm boundary}\) |

---

## Status Counts

```text
CANDIDATE:    2
CONSTRAINED:  1
FORBIDDEN:    1
RECOMMENDED:  1
REQUIRED:     5
SAFE_IF:      1
UNRESOLVED:   1
```

Interpretation:

```text
Projected kappa is promising, but only if P_trace also supports compensation / exterior neutrality.
The relaxed projected map is safer than raw equality.
The main unresolved issue is whether the projection is diagnostic, energetic, or constraint-defining.
```

---

## Minimal Projected Map

Minimal map:

\[
\kappa=P_{\rm trace}(\zeta-\zeta_{\min}).
\]

Safer relaxed map:

\[
\kappa=P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min}).
\]

Required exterior conditions:

\[
\zeta_{\rm ext}\to0,
\qquad
\kappa_{\rm ext}\to0,
\qquad
Q_{\rm volume}=0,
\qquad
Q_\kappa=0,
\]

\[
F_\zeta(R+)=0,
\qquad
F_\kappa(R+)=0,
\qquad
\delta M_{\rm ext}=0.
\]

Accounting:

```text
epsilon_zeta counted separately,
e_kappa counted separately only if kappa is a residual,
K_lock not counted as physical energy.
```

---

## \(P_{\rm trace}\) Requirements

\(P_{\rm trace}\) must:

1. Extract trace / volume mismatch.
2. Remove or compensate exterior monopole.
3. Exclude \(A\)-sector mass charge.
4. Annihilate TT modes.
5. Cooperate with \(P_{\rm boundary}\).
6. Avoid becoming a wave operator.
7. Support first-order relaxation if \(P_{\rm relax}\) is included.
8. Leave recombination with only one trace / volume contribution.

---

## Failure Controls

The projected map fails if:

1. \(P_{\rm trace}\) is just identity on \(\zeta-\zeta_{\min}\) and exterior charge survives.
2. \(P_{\rm trace}\) is raw pressure / trace source and duplicates \(A\)-sector mass.
3. \(\kappa_{\rm ext}\) or \(\zeta_{\rm ext}\) has a \(1/r\) tail.
4. \(e_\kappa\) duplicates \(\epsilon_\zeta\) displacement.
5. \(K_{\rm lock}\) becomes physical energy before derivation.
6. \(\Box\kappa\) or \(\Box\zeta\) reappears.
7. TT modes alter \(\zeta\) through projector leakage.
8. Recombination counts \(A\) spatial response, \(\zeta\), and \(\kappa\) separately.

---

## What This Study Established

This study established that projected \(\kappa\) is the best current relation target:

\[
\kappa=P_{\rm trace}(\zeta-\zeta_{\min}).
\]

The safer form is:

\[
\kappa=P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min}).
\]

This is safe only if \(P_{\rm trace}\) is much more than a raw trace extractor. It must cooperate with neutrality, boundary, source-separation, TT, and recombination constraints.

---

## What This Study Did Not Establish

This study did not define \(P_{\rm trace}\).

It did not derive \(P_{\rm relax}\).

It did not derive \(P_{\rm boundary}\).

It did not prove \(Q_\kappa=0\) or \(Q_{\rm volume}=0\).

It did not decide whether projected \(\kappa\) is diagnostic, energetic, or constraint-defining.

It did not derive \(P_{\rm recombination}\).

---

## Current Best Interpretation

Projected \(\kappa\) is plausible.

Raw projected equality is not enough.

The safest provisional form is:

\[
\kappa=P_{\rm relax}P_{\rm trace}(\zeta-\zeta_{\min}).
\]

with:

```text
K_lock diagnostic only,
no Box kappa,
no Box zeta,
no exterior kappa/zeta charge,
no A-sector mass duplication,
one trace/volume contribution in recombination.
```

---

## Next Development Target

The next script should be:

```text
candidate_trace_projector_definition.py
```

Purpose:

```text
Define P_trace directly.
```

Reason:

```text
The projected map is only as good as P_trace.
```

---

## Summary

The projected-map result is:

```text
kappa can only be a safe zeta residual if P_trace is a real projector,
not a new scalar gravity source.
```

The next goblin gate is:

```text
what exactly does P_trace do?
```
