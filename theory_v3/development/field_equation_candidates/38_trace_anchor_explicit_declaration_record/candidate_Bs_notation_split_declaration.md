# Candidate B_s Notation Split Declaration

## Result

The script records a notation-split repair surface for the `B_s` conflict. The split separates metric-coefficient usage from scale-factor usage by naming two distinct candidate objects:

```text
B_s_metric
b_s_scale
```

This repairs the overloaded notation enough for later branch-choice work, but it does not select either branch as the active declaration.

## Split Objects

`B_s_metric` is the metric-coefficient spatial-response notation. Its candidate normalization is:

```text
log(B_s_metric) = 2*zeta/d
```

`b_s_scale` is the scale-factor or per-direction spatial-response notation. Its candidate normalization is:

```text
log(b_s_scale) = zeta/d
```

`F_zeta` remains a neutral response-functional placeholder. It does not install a concrete normalization and must not hide the factor-of-two choice.

## Active Branch Status

The active declaration branch was not configured:

```text
ACTIVE_DECLARATION_BRANCH = None
```

Therefore the result is:

```text
DECLARATION_DEFERRED
```

The split repairs naming conflict, but declaration remains incomplete until a later explicit branch-choice or declaration-completion script selects one branch.

## Guardrails

The script rejects the following upgrades:

```text
split as active declaration
split as theorem
F_zeta as hidden branch
branch choice as adoption
split as insertion
```

The key rule is that split notation is not a choice. Naming `B_s_metric` and `b_s_scale` prevents the same symbol from carrying two meanings, but it does not decide which object becomes the active Package B declaration.

## Downstream Status

No trace-normalization declaration is completed. No safe-membership declaration is completed. No Package B component is adopted or derived.

The following remain closed:

```text
B_s/F_zeta insertion
active O
residual control
parent closure
```

## Safe Handoff

The next script should classify explicit branch-choice routes:

```text
candidate_Bs_explicit_branch_choice_sieve.py
```

That script should preserve three possible outcomes:

```text
metric_coefficient branch chosen by explicit theory decision
scale_factor branch chosen by explicit theory decision
branch choice remains deferred
```

It must not choose a branch from recovery, hit counts, insertion convenience, or parent fit.
