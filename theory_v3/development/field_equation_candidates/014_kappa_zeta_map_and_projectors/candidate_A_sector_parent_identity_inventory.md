# Candidate A-Sector Parent Identity Inventory

## Canonical Filename

```text
candidate_A_sector_parent_identity_inventory.md
```

This document summarizes the output of:

```text
candidate_A_sector_parent_identity_inventory.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a derivation of the parent identity, not a parent action, and not a field equation.

Its purpose is to inventory what kind of parent identity could derive \(A\) and \(A_{\rm spatial}\) together without GR smuggling.

The guiding question was:

```text
What kind of parent identity could derive A and A_spatial together without GR smuggling?
```

The answer is:

```text
The A-sector parent identity search has narrowed.

Rejected:
  GR rewrite,
  B=1/A identity,
  gamma=1 coefficient fit.

Surviving identity classes:
  action/stiffness,
  constraint propagation,
  conservation/Bianchi-like,
  volume-exchange,
  recombination/no-overlap identity.

Best next test:
  candidate_parent_constraint_propagation_identity.py

Reason:
  It is the nearest possible bridge from the existing A-sector constraint to A_spatial.
```

---

## Why This Study Matters

The \(A_{\rm spatial}\) recovery audit found:

```text
A_spatial is currently a recovery theorem target,
not a derived metric component.
```

The best surviving branch was:

```text
derive A and A_spatial together from a parent scalar/spatial identity.
```

The parent-identity inventory asked which identity classes are legitimate search directions and which are just GR imports or renamed missing equations.

---

## Compact Parent-Identity Ledger

| Entry | Identity Class | Status | Consequence |
|---|---|---|---|
| PI1: action / stiffness identity | \(A\) and \(A_{\rm spatial}\) arise from one variational stiffness / action principle | CANDIDATE | could derive \(\gamma=1\)-like recovery without coefficient repair |
| PI2: constraint propagation identity | scalar constraint for \(A\) forces compatible spatial response through propagation / closure | CANDIDATE | would keep \(A\)-sector local but requires non-decorative closure |
| PI3: conservation / Bianchi-like identity | \({\rm Div}\,E_{\rm parent}=B_{\rm closed}[T]+B_{\rm relax}\) | CANDIDATE | could derive \(A/A_{\rm spatial}\) relation plus trace / residual routing |
| PI4: vacuum-volume exchange identity | \(A_{\rm spatial}\) follows from volume / curvature exchange with \(\zeta\) | RISK | may force \(\zeta\) to be \(A_{\rm spatial}\) bookkeeping or kill independent residual trace |
| PI5: projector recombination identity | \(P_{\rm recombination}\) derives \({\rm Trace}_{A,{\rm mass}}+{\rm Trace}_{\rm residual,neutral}\) with zero overlap | THEOREM_TARGET | would decide what remains for \(\zeta/\kappa\) after \(A_{\rm spatial}\) |
| PI6: exterior recovery identity | identity is inferred from Schwarzschild-like exterior recovery | RECOVERY_TARGET | keeps \(AB/\gamma\) targets as tests, not construction rules |
| PI7: pure boundary matching identity | \(A_{\rm spatial}\) determined by matching interior to exterior boundary conditions | SAFE_IF | cannot by itself derive \(A_{\rm spatial}\) throughout the domain |
| PI8: GR-rewrite identity | rewrite Einstein equations / Schwarzschild metric with new variable names | REJECTED | would end field-equation search by smuggling GR |
| PI9: \(B=1/A\) identity | \(AB=1\) or \(B=1/A\) imposed as parent identity | REJECTED | \(AB=1\) remains recovery check, not identity |
| PI10: coefficient-fit identity | choose stiffness / coefficient ratios to recover \(\gamma=1\) | REJECTED | prevents \(\gamma=1\) tuning from masquerading as derivation |
| PI11: \(A\)-only local scalar constraint | \(A\) equation alone derives lapse response but not spatial companion | CONSTRAINED | if no companion identity exists, \(A\)-sector-local branch is insufficient |
| PI12: recommended next search | inventory narrows to action / stiffness, constraint-propagation, conservation / Bianchi-like, or volume-exchange identities | RECOMMENDED | next work should test surviving identity classes rather than add new projectors |

---

## Status Counts

The run counted:

```text
CANDIDATE:      3
CONSTRAINED:    1
RECOMMENDED:    1
RECOVERY_TARGET: 1
REJECTED:       3
RISK:           1
SAFE_IF:        1
THEOREM_TARGET: 1
```

Interpretation:

```text
A pure A-only scalar constraint is not enough unless a companion identity is found.
Surviving identity classes are action/stiffness, constraint propagation, conservation/Bianchi-like, volume-exchange, and recombination identity.
GR rewrite, B=1/A identity, and coefficient-fit identity are rejected.
The next step should test one surviving identity class concretely.
```

---

## Legitimate Parent Identity Test

A proposed parent identity is useful only if it rules in or rules out future field-equation classes.

Useful identity statement:

```text
This identity derives A and A_spatial together,
preserves Trace_A_mass + Trace_residual_neutral with no overlap,
and does not import B=1/A or gamma=1 by hand.
```

Unhelpful identity statement:

```text
There exists a parent identity that does the needed thing.
```

Rule:

```text
An identity must carry a mechanism, a closure condition, or a no-go consequence.
```

---

## Count-Once Trace Theorem Target

Any viable parent identity must derive or resolve:

\[
{\rm Trace}[g_{ij}^{\rm scalar}]
=
{\rm Trace}_{A,{\rm mass}}
+
{\rm Trace}_{\rm residual,neutral}.
\]

with:

\[
{\rm overlap}=0.
\]

Allowed resolutions:

1. Derive both terms and their orthogonality.
2. Derive \({\rm Trace}_{\rm residual,neutral}=0\).
3. Make \(\zeta/\kappa\) diagnostic or non-metric after \(A_{\rm spatial}\).

Forbidden:

```text
overlapping A_spatial and zeta/kappa trace.
```

---

## Revisit Triggers

Revisit provisional conventions if:

```text
zeta primary:
  revisit if parent identity makes zeta the A_spatial companion.

kappa residual unresolved:
  revisit if parent identity leaves no residual trace.

K_lock diagnostic only:
  revisit only if parent identity derives a locking term.

A_spatial recovery theorem target:
  revisit if parent identity derives it or kills independent A_spatial.
```

---

## Failure Controls

Parent identity inventory fails if:

1. Einstein equations are rewritten with new labels.
2. \(B=1/A\) is called a parent identity.
3. Schwarzschild form is used as variational target.
4. \(\gamma=1\) is tuned by coefficient choice.
5. \(\zeta/\kappa\) residual is hidden inside \(A_{\rm spatial}\) without no-overlap proof.
6. Conservation identity is declared without conserved current.
7. Gauge condition is called a parent identity.
8. Exterior matching alone determines local field equations.
9. Vacuum minimization uses tunable weights as black box.
10. \(\epsilon_{\rm vac,config}\) or \(\Sigma_{\rm creation}\) patches ordinary recovery.

---

## What This Study Established

This study established that the \(A\)-sector parent identity search has narrowed.

Rejected:

```text
GR rewrite,
B=1/A identity,
gamma=1 coefficient fit.
```

Surviving identity classes:

```text
action/stiffness,
constraint propagation,
conservation/Bianchi-like,
volume-exchange,
recombination/no-overlap identity.
```

The nearest route from the existing \(A\)-sector success is:

```text
constraint propagation.
```

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive \(A_{\rm spatial}\).

It did not define \(E_{\rm parent}\), \(B_{\rm closed}\), or \(B_{\rm relax}\).

It did not derive a parent action.

It did not decide whether \(\zeta\) is \(A_{\rm spatial}\) bookkeeping or a residual.

It did not decide whether \(\kappa/\zeta\) survive as residual geometry after \(A_{\rm spatial}\).

---

## Current Best Interpretation

The current bottleneck is no longer another projector.

It is:

```text
Can the existing A-sector constraint force a compatible A_spatial companion
through a real propagation / closure identity?
```

If yes, the \(A\)-sector local branch survives.

If no, the search likely has to move to action / stiffness, conservation / Bianchi-like, or volume-exchange parent identities.

---

## Next Development Target

The next script should be:

```text
candidate_parent_constraint_propagation_identity.py
```

Purpose:

```text
Test whether a scalar constraint can force its spatial companion.
```

Reason:

```text
The closest surviving route from the existing A-sector success is constraint propagation:
can the A constraint force a compatible spatial companion without GR import?
```

Expected result:

```text
A constraint-propagation ledger:
  A constraint plus source conservation,
  spatial companion forced by closure,
  compatibility with gamma=1 recovery,
  no B=1/A decree,
  no GR rewrite,
  no zeta patch without no-overlap,
  branch-killed outcome if A-only closure fails.
```

---

## Summary

The parent-identity inventory result is:

```text
Do not add another projector yet.
Test whether the A constraint propagates into A_spatial.
```

The next goblin gate is:

```text
can A force its spatial companion without secretly borrowing GR?
```
