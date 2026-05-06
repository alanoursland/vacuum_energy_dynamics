# Candidate Vacuum Current Split Inventory

## Canonical Filename

```text
candidate_vacuum_current_split_inventory.md
```

This document summarizes the output of:

```text
candidate_vacuum_current_split_inventory.py
```

## What This Document Is

This document is the opening artifact for `18_vacuum_current_split/`.

It is not a definition of \(J_V\), not an operator-level decomposition, not a vacuum-current law, and not a parent correction tensor.

Its purpose is to inventory whether the unresolved vacuum-current language is hiding distinct roles:

```text
J_sub:
  substrate / background / pure vacuum transport candidate

J_exch:
  active exchange / source-relaxation current candidate
```

The locked-door question was:

```text
What distinct roles are being hidden inside J_V?
```

The result is:

```text
J_V remains unresolved.

J_sub/J_exch split is useful as role-level bookkeeping only.

Core live branches:

  J_sub pure substrate / pure wind candidate
  J_exch active exchange candidate
  zero-net-exchange ordinary sector
  zero-creation ordinary sector
  curvature-from-warping branch
  latent-exchange accounting branch

Best next script:

  candidate_pure_wind_neutrality_test.py
```

## Core Result

The split is useful, but only at role level.

Current safe notation:

```text
J_V = J_sub + J_exch
```

is allowed only as bookkeeping.

It is not yet an operator identity, not a field law, and not a balance closure.

## Compact Vacuum Current Split Ledger

| Entry | Split Role | Status | Consequence |
|---|---|---|---|
| VS1: vacuum current split target | \(J_V\) may contain distinct substrate-flow and active-exchange roles | THEOREM_TARGET | decides whether \(J_V\) can be decomposed without fake closure |
| VS2: single unresolved \(J_V\) | \(J_V\) remains umbrella notation for unresolved vacuum current | SAFE_IF | keeps vacuum-current branch honest if split is premature |
| VS3: \(J_{\rm sub}\) substrate-flow role | \(J_{\rm sub}\) as pure substrate / background / vacuum transport candidate | CANDIDATE | could represent vacuum substance flow without ordinary gravitational effect |
| VS4: \(J_{\rm exch}\) active-exchange role | \(J_{\rm exch}\) as exchange/source-relaxation current candidate | CANDIDATE | could carry active exchange if source side becomes real |
| VS5: role-level decomposition | \(J_V=J_{\rm sub}+J_{\rm exch}\) as bookkeeping only | SAFE_IF | lets later scripts test roles without pretending the split is derived |
| VS6: operator-level decomposition | \(J_V=J_{\rm sub}+J_{\rm exch}\) with real projection/support/divergence criterion | THEOREM_TARGET | stronger future target if role-level split survives |
| VS7: pure wind neutrality requirement | pure substrate flow has no ordinary gravitational effect by existence alone | REQUIRED | decides whether \(J_{\rm sub}\) can be harmless in ordinary sector |
| VS8: ordinary matter decoupling requirement | \(J_{\rm sub}/J_{\rm exch}\) do not alter ordinary matter routing unless theorem derives it | REQUIRED | prevents current split from becoming matter repair mechanism |
| VS9: exterior mass neutrality requirement | \(J_{\rm sub}/J_{\rm exch}\) do not shift \(M_{\rm ext}\) independently of A-sector | REQUIRED | protects strongest reduced A-sector result |
| VS10: \(\Sigma/R\) double-counting guard | \(\Sigma_V\) and \(R_V\) cannot be two names for one tuning mechanism | REQUIRED | prevents exchange current from hiding a tuning knob |
| VS11: zero-net-exchange branch | \(\Sigma_V-R_V=0\) in ordinary sector | CANDIDATE | keeps vacuum-substance ontology while ordinary net creation is zero |
| VS12: zero-creation branch | \(\Sigma_V=R_V=0\) in ordinary sector | CANDIDATE | cleanest ordinary-sector no-exchange branch |
| VS13: curvature-from-warping branch | curvature change arises from constrained spatial/time warping, not net vacuum creation/destruction | CANDIDATE | important alternative to active exchange in ordinary sector |
| VS14: latent-exchange branch | \(\Sigma/R\) exist as ontology/accounting but vanish or balance in ordinary sector | CANDIDATE | preserves substance language without forcing ordinary creation/destruction |
| VS15: \(J_{\rm curv}\)-related branch deferred | \(J_{\rm curv}\) participates in vacuum current split | DEFER | preserves Group 17 closure |
| VS16: dark-sector branch optional | dark-sector coupling attaches to \(J_{\rm exch}\) or vacuum current split | DEFER | keeps dark-sector speculation downstream |
| VS17: preferred-frame wind rejection | \(J_{\rm sub}\) as arbitrary preferred-frame wind | REJECTED | prevents arbitrary-frame current |
| VS18: repair-current rejection | \(J_{\rm exch}\) or \(J_V\) chosen to cancel boundary leakage, singularity behavior, or recovery mismatch | REJECTED | prevents vacuum current from becoming painted repair pipe |
| VS19: \(H_{\rm exch}/H_{\rm curv}\) premature use rejection | \(J_{\rm sub}/J_{\rm exch}\) used to justify \(H_{\rm exch}\) or \(H_{\rm curv}\) immediately | REJECTED | prevents decorative correction tensor |
| VS20: recovery downstream guard | \(\gamma_{\rm like}\), \(AB\), exterior recovery do not choose current split | REQUIRED | prevents recovery-shaped current split |
| VS21: recommended next move | test pure wind neutrality before defining \(J_{\rm sub}\) | RECOMMENDED | next script should be `candidate_pure_wind_neutrality_test.py` |

## Status Counts

```text
CANDIDATE:      6
DEFER:          2
RECOMMENDED:    1
REJECTED:       3
REQUIRED:       5
SAFE_IF:        2
THEOREM_TARGET: 2
```

Interpretation:

```text
J_V remains unresolved.

J_sub/J_exch split is useful as role-level bookkeeping,
not operator-level law.

Pure wind neutrality is the central safety requirement for J_sub.

J_exch requires real source/relaxation sides and cannot be repair.

Zero-net-exchange / zero-creation branches should stay live for ordinary sector.

J_curv and dark-sector branches remain deferred.

Next gate is pure wind neutrality.
```

## Split Role Distinctions

Candidate role distinctions:

```text
1. unresolved umbrella J_V
2. J_sub as pure substrate / background transport
3. J_exch as active exchange / source-relaxation current
4. zero-net exchange in ordinary sector
5. zero creation in ordinary sector
6. curvature-from-warping rather than net creation
7. latent exchange as ontology/accounting only
```

Deferred:

```text
J_curv-related branch
dark-sector branch
H_exch/H_curv branch
```

## Vacuum Current Split Decision Tree

```text
1. No split criterion:
   J_V remains unresolved umbrella notation.

2. Role-level split useful:
   write J_sub/J_exch as bookkeeping only.

3. J_sub candidate:
   must pass pure wind neutrality before definition.

4. J_exch candidate:
   must have real source/relaxation sides and cannot be repair.

5. Ordinary sector:
   preserve zero-net-exchange / zero-creation branches.

6. Dark sector:
   deferred and optional.

7. Parent correction tensor:
   deferred to Group 19.
```

## Good Failure / Branch Decision

Good failure:

```text
J_sub/J_exch split cannot be made operator-level.
```

Consequence:

```text
keep split as role-level bookkeeping only.
preserve pure wind neutrality and ordinary matter decoupling as theorem targets.
keep zero-net-exchange / zero-creation branches alive in ordinary sector.
```

Bad failure:

```text
name J_sub/J_exch and use them as currents, sources, or correction-tensor inputs.
```

## Failure Controls

Vacuum current split fails if:

1. \(J_V\) is assumed defined.
2. \(J_{\rm sub}\) is arbitrary preferred-frame wind.
3. \(J_{\rm sub}\) gravitates by existence.
4. \(J_{\rm sub}\) shifts \(M_{\rm ext}\).
5. \(J_{\rm sub}\) couples to ordinary matter.
6. \(J_{\rm exch}\) is repair current.
7. \(\Sigma/R\) become tuning knobs.
8. dark sector patches ordinary failure.
9. current split reopens \(\zeta\) metric trace.
10. \(H_{\rm exch}/H_{\rm curv}\) is introduced early.
11. recovery chooses the split.

## What This Study Established

This study established that the \(J_{\rm sub}/J_{\rm exch}\) split is useful as role-level bookkeeping.

It also established that the split is not yet an operator-level decomposition.

The strongest ordinary-sector branches now kept alive are:

```text
zero-net exchange:
  Sigma_V - R_V = 0

zero creation:
  Sigma_V = R_V = 0

curvature-from-warping:
  curvature changes arise from constrained time/space warping,
  not net vacuum creation/destruction

latent exchange:
  Sigma/R exist as ontology/accounting,
  but vanish or balance in ordinary sector
```

## What This Study Did Not Establish

This study did not define \(J_V\).

It did not define \(J_{\rm sub}\).

It did not define \(J_{\rm exch}\).

It did not derive pure wind neutrality.

It did not derive ordinary matter decoupling.

It did not derive \(\Sigma_V\) or \(R_V\).

It did not make dark-sector coupling active.

It did not justify \(H_{\rm exch}\) or \(H_{\rm curv}\).

## Current Best Interpretation

```text
J_V remains unresolved.

J_sub/J_exch is a useful role split,
but not yet a current split.

Pure wind neutrality must be tested before J_sub is defined.
```

## Next Development Target

The next script should be:

```text
candidate_pure_wind_neutrality_test.py
```

Purpose:

```text
Test whether pure vacuum substrate flow can exist
without ordinary gravitational effect.
```

Reason:

```text
Before J_sub can be defined,
pure wind must be shown harmless:
no M_ext shift,
no scalar trace,
no ordinary matter coupling,
no boundary repair.
```

Expected result:

```text
A pure-wind neutrality ledger:
  no divergence,
  no exchange,
  no endpoints,
  no boundary flux,
  no M_ext shift,
  no scalar trace,
  no ordinary matter coupling,
  pure wind as mass source rejected,
  preferred-frame force rejected,
  scalar charge rejected,
  recovery repair rejected,
  boundary patch rejected.
```

## Summary

The vacuum-current split inventory result is:

```text
The split is a useful ledger,
not a law.

J_sub is wind only if wind is neutral.
J_exch is exchange only if exchange has real source sides.
```

Tiny goblin plaque:

```text
Two buckets may hang from one hook.
Do not call them rivers yet.
