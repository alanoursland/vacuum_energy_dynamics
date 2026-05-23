# Candidate A Spatial Recovery Constraint

## Canonical Filename

```text
candidate_A_spatial_recovery_constraint.md
```

This document summarizes the output of:

```text
candidate_A_spatial_recovery_constraint.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of \(A_{\rm spatial}\), not a covariant parent identity, and not a metric construction rule.

Its purpose is to identify recovery requirements and candidate mechanisms for \(A_{\rm spatial}\) without importing GR spatial metric structure.

The guiding question was:

```text
What must A_spatial recover without copying GR?
```

The answer is:

```text
A_spatial is currently:

  a recovery theorem target,
  not a derived metric component.

Best branch:

  derive A and A_spatial together from a parent scalar/spatial identity.

Rejected:

  copying GR spatial metric,
  imposing B=1/A,
  tuning gamma=1,
  using kappa_areal as physical scalar.
```

---

## Why This Study Matters

The areal-\(\kappa\) diagnostic was fenced as:

```text
reduced diagnostic,
exterior recovery check,
A/B mismatch test instrument.
```

It is not allowed as:

```text
covariant physical scalar,
independent trace insertion,
physical e_kappa basis,
parent field-equation building block.
```

That fencing allowed the \(A_{\rm spatial}\) recovery problem to be asked without silently using:

\[
\kappa_{\rm areal}
=
\frac12\ln(AB)
\]

as a physical scalar.

---

## Compact \(A_{\rm spatial}\) Recovery Ledger

| Entry | Branch | Status | Consequence |
|---|---|---|---|
| AS1: \(A_{\rm spatial}\) derived with \(A\) from parent scalar constraint | lapse \(A\) and spatial scalar response arise together from one parent identity | THEOREM_TARGET | would make \(A_{\rm spatial}\) a derived companion, not a GR import |
| AS2: \(A_{\rm spatial}\) as recovery constraint only | \(A_{\rm spatial}\) is specified only as required recovery behavior | SAFE_IF | recombination remains bookkeeping until parent identity is found |
| AS3: copy GR spatial metric | set spatial metric response equal to GR / Schwarzschild form | REJECTED | would collapse search into GR import |
| AS4: impose \(B=1/A\) by decree | set \(B=1/A\) as construction rule | REJECTED | \(AB=1\) remains check, not construction |
| AS5: PPN \(\gamma=1\) as coefficient tuning | choose coefficients so weak-field spatial curvature matches \(\gamma=1\) | REJECTED | \(\gamma=1\) can constrain candidates but cannot be fitted by repair knob |
| AS6: \(\zeta\) supplies missing \(A_{\rm spatial}\) companion | \(\zeta\) volume configuration provides the spatial scalar response associated with \(A\) | RISK | may force \(\zeta\) to be \(A_{\rm spatial}\) bookkeeping rather than independent residual |
| AS7: boundary-neutral residual after \(A_{\rm spatial}\) | \(A_{\rm spatial}\) handles mass-sector trace; \(\zeta/\kappa\) residual remains boundary-neutral | CANDIDATE | supports prior count-once recombination rule |
| AS8: \(A_{\rm spatial}\) consumes all scalar trace | \(A_{\rm spatial}\) fully determines scalar trace in \(g_{ij}\) | SAFE_IF | \(\kappa/\zeta\) become diagnostic, residual energy bookkeeping, or non-metric variables |
| AS9: areal kappa patch | use \(\kappa_{\rm areal}=\frac12\ln(AB)\) to justify \(A_{\rm spatial}\) | CONSTRAINED | areal \(\kappa\) remains fenced; cannot derive \(A_{\rm spatial}\) |
| AS10: coordinate gauge-only derivation | spatial response follows only from coordinate / gauge choice | REJECTED | gauge can organize variables but not supply physical field equation |
| AS11: recovery targets | Schwarzschild-like exterior, \(AB\) diagnostic, weak-field \(\gamma=1\) behavior | RECOVERY_TARGET | keeps observational safety without GR smuggling |
| AS12: recommended framing | \(A_{\rm spatial}\) is recovery theorem target; derive with \(A\) or keep bookkeeping | RECOMMENDED | pushes next search toward parent scalar / spatial identity if local branches fail |

---

## Status Counts

The run counted:

```text
CANDIDATE:       1
CONSTRAINED:     1
RECOMMENDED:     1
RECOVERY_TARGET: 1
REJECTED:        4
RISK:            1
SAFE_IF:         2
THEOREM_TARGET:  1
```

Interpretation:

```text
A_spatial is not derived yet.
The best branch is joint derivation of A and A_spatial from a parent scalar/spatial identity.
GR metric copying, B=1/A by decree, and gamma=1 tuning are rejected.
Zeta can only help if it does not become both A_spatial patch and independent residual.
```

---

## Recovery Targets, Not Construction

Safe phrasing:

```text
The ordinary weak/static exterior must recover Schwarzschild-like behavior.
The reduced exterior should pass the AB -> 1 diagnostic.
The weak-field spatial response should match gamma=1 behavior.
These are tests on acceptable parent equations.
```

Unsafe phrasing:

```text
Set B=1/A.
Insert the GR spatial metric.
Tune the spatial coefficient to gamma=1.
```

Rule:

```text
Recovery targets constrain the search; they do not construct the equation.
```

---

## Count-Once Constraint Carried Forward

Active theorem target:

\[
{\rm Trace}[g_{ij}^{\rm scalar}]
=
{\rm Trace}_{A,{\rm mass}}
+
{\rm Trace}_{\rm residual,neutral}.
\]

with:

\[
{\rm overlap}
(
{\rm Trace}_{A,{\rm mass}},
{\rm Trace}_{\rm residual,neutral}
)
=
0.
\]

The \(A_{\rm spatial}\) question focuses on:

```text
What is Trace_A_mass required to be?
Can it be derived with A rather than imported?
What residual trace, if any, remains?
```

---

## Good Failure Mode

A useful failure would be:

```text
A-sector alone cannot derive spatial response without a parent identity
or without explicitly routing zeta as non-overlapping spatial volume response.
```

This means:

```text
A_spatial remains a theorem target,
and the next search must derive lapse and spatial response together,
or define zeta's non-overlapping role.
```

Bad failure:

```text
copy GR spatial response and move on.
```

---

## Failure Controls

\(A_{\rm spatial}\) recovery fails if:

1. GR spatial metric is copied as derivation.
2. \(B=1/A\) is imposed by decree.
3. \(\gamma=1\) is tuned by coefficient choice.
4. \(\zeta/\kappa\) patch missing spatial response while also remaining independent residual.
5. \(A_{\rm spatial}\) duplicates residual trace.
6. \(\kappa_{\rm areal}\) becomes physical scalar.
7. Spatial response is derived from coordinate gauge only.
8. \(A_{\rm spatial}\) changes \(M_{\rm ext}\) independently of \(A_{\rm flux}\).
9. Recovery bookkeeping is called parent identity.

---

## What This Study Established

This study established that \(A_{\rm spatial}\) is currently:

```text
a recovery theorem target,
not a derived metric component.
```

The best surviving branch is:

```text
derive A and A_spatial together from a parent scalar/spatial identity.
```

This is now the field-equation bottleneck.

---

## What This Study Did Not Establish

This study did not derive \(A_{\rm spatial}\).

It did not derive the \(A\)-sector parent identity.

It did not prove \(\gamma=1\).

It did not derive \(B=1/A\).

It did not decide whether \(\zeta\) is the \(A_{\rm spatial}\) companion, an independent residual, or only bookkeeping.

It did not decide whether \(\kappa/\zeta\) become diagnostic, residual energy bookkeeping, or non-metric variables if \(A_{\rm spatial}\) consumes all scalar trace.

---

## Current Best Interpretation

\(A_{\rm spatial}\) should be treated as:

```text
a recovery theorem target,
not a derived metric component.
```

The next search must find what kind of parent identity could derive \(A\) and \(A_{\rm spatial}\) together without copying GR.

---

## Next Development Target

The next script should be:

```text
candidate_A_sector_parent_identity_inventory.py
```

Purpose:

```text
Inventory parent identities that could derive A and A_spatial together.
```

Reason:

```text
A_spatial appears to require joint derivation with A from a parent scalar/spatial identity.
That is now the field-equation bottleneck.
```

Expected result:

```text
A parent-identity class ledger:
  action / stiffness identity,
  constraint propagation identity,
  conservation / Bianchi-like identity,
  exterior recovery identity,
  vacuum-volume minimization identity,
  projector recombination identity,
  pure matching identity,
  GR-rewrite identity,
  forbidden shortcuts,
  consequences for zeta/kappa residuals.
```

---

## Summary

The \(A_{\rm spatial}\) result is:

```text
Do not copy the spatial metric.
Find the parent identity that makes A and A_spatial arrive together.
```

The next goblin gate is:

```text
what kind of parent identity could do that?
```
