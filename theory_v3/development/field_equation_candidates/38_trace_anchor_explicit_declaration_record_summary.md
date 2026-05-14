# 38 Trace Anchor Explicit Declaration Record — Summary

## Group Purpose

Group 38 attempted to move from declaration-option audit toward an explicit trace-anchor declaration record.

The group asked whether one trace-anchor declaration package could be installed as the declared candidate surface for later theorem, adoption, or precondition routes.

## Actual Outcome

Group 38 did not complete an explicit declaration record.

Instead, it discovered and repaired a notation conflict.

The actual `B_s` usage collector found both metric-like and scale-like usage. Because those meanings differ by the factor-of-two relation between metric coefficient language and scale-factor language, the same overloaded `B_s` symbol could not safely carry both meanings.

The repair was to split the notation:

```text
B_s_metric:
  metric-coefficient spatial response branch
  candidate normalization: log(B_s_metric) = 2 zeta / d

b_s_scale:
  scale-factor / per-direction spatial response branch
  candidate normalization: log(b_s_scale) = zeta / d

F_zeta:
  neutral functional placeholder until an active branch is explicitly chosen
```

This split repairs the naming conflict, but it does not choose the active branch.

## Final Group Status

```text
DECLARATION_DEFERRED
```

Group 38 closes as a deferred declaration attempt, not as a completed declaration record.

## Current Trace-Anchor State After Group 38

```text
Package B:
  still minimal plausible-to-audit only
  still compatible-if-declared only

Trace normalization:
  not selected
  not declared
  not adopted
  not derived

Safe membership:
  not selected
  not declared
  not adopted
  not derived

B_s notation:
  conflict repaired by split
  active branch not chosen
```

## What Improved

Group 38 made the notation surface cleaner.

Before Group 38, `B_s` carried a dangerous ambiguity between metric-coefficient and scale-factor language. After Group 38, those meanings have distinct names. This prevents later scripts from hiding a factor-of-two convention choice inside one overloaded symbol.

The group therefore improved the audit state even though it did not complete the declaration.

## What Remains Open

The following remain open:

```text
explicit branch choice:
  metric_coefficient or scale_factor

trace-normalization declaration:
  B_s convention, zeta convention, traced dimension, scope, expression

safe-membership declaration:
  membership form, object, sector, domain/codomain, criterion, role purity, scope

joint Package B declaration:
  no joint declaration surface installed

adoption:
  still separate

theorem support:
  still separate

downstream use:
  not ready
```

## Guardrails Preserved

Group 38 preserves the key boundaries:

```text
notation split is not active declaration
active branch choice is not adoption
branch choice would not be theorem proof
F_zeta neutrality cannot hide a convention
Package B remains compatible-if-declared only
B_s/F_zeta insertion remains not ready
active O remains not ready
residual control remains not ready
parent equation remains not ready
```

## Recommended Next Work

There are four honest next routes.

```text
1. explicit branch-choice record
   Choose metric_coefficient or scale_factor as a declared candidate branch.

2. notation-quality source hierarchy
   Rank earliest or authoritative notation sources before choosing a branch.

3. neutral F_zeta deferral
   Keep F_zeta neutral while no concrete zeta/d or 2 zeta/d declaration is installed.

4. theorem/precondition work that does not require completed declaration
   Continue only if the route explicitly does not depend on an active B_s branch.
```

The most direct route is an explicit branch-choice record, but only if the theory owner is ready to make that choice as a declaration, not as a derivation or adoption.

## One-Line Summary

```text
Group 38 labeled the two jars but did not choose one.
```
