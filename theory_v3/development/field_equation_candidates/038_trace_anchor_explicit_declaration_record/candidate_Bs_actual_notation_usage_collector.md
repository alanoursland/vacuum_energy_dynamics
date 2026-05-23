# Candidate B_s Actual Notation Usage Collector

## Purpose

This script collected actual project-file usage of `B_s`, inherited `B`, and `F_zeta` before choosing between the scale-factor and metric-coefficient conventions.

It was an evidence collector only. It did not choose a `B_s` convention, fill trace-normalization declarations, adopt Package B, prove either Package B component, or open `B_s/F_zeta` insertion.

## Result

The collector found evidence in several classes:

```text
METRIC_LIKE: 16
SCALE_LIKE: 6
DETERMINANT_ROOT_LIKE: 10
FUNCTIONAL_NEUTRAL: 16
AMBIGUOUS: 16
RECOVERY_SELECTOR: 16
```

The overall classification was:

```text
CONFLICT
```

The important result is not that either convention won. The important result is that both metric-like and scale-like usage were found. This means a single undeclared `B_s` convention cannot be installed safely from the existing usage record.

## Interpretation

Metric-like hits support the possibility that `B_s` inherits radial or spatial metric-coefficient language. Under that convention, a volume-trace normalization would have the form:

```text
log(B_s) = 2*zeta/d
```

Scale-like and determinant-root hits support the possibility that `B_s` is being used as a scale factor, volume root, or per-direction response. Under that convention, a volume-trace normalization would have the form:

```text
log(B_s) = zeta/d
```

Functional-neutral `F_zeta` hits do not decide the factor of two by themselves. They can keep a response-function placeholder open, but cannot hide the convention choice.

Recovery-selector hits are not admissible convention selectors. Schwarzschild recovery, `AB=1`, `B=1/A`, gamma recovery, insertion convenience, and parent fit remain audits or downstream checks, not sources of declaration choice.

## Boundaries Preserved

The collector explicitly rejected these upgrades:

```text
found snippet -> declaration
conflicting snippets -> silent convention choice
recovery snippet -> notation selector
usage evidence -> Package B adoption
usage evidence -> B_s/F_zeta insertion
```

So the result is evidence conflict, not declaration, adoption, theorem proof, insertion, active `O`, residual control, or parent readiness.

## Safe Handoff

The next script should be:

```text
candidate_Bs_notation_conflict_repair.py
```

It should classify possible repair routes for the conflict:

```text
split B_s into named metric-coefficient and scale-factor notations,
choose one convention by explicit theory decision,
defer declaration until notation is repaired,
or keep F_zeta neutral while blocking trace-normalization installation.
```

It must not choose a convention automatically.

## Tiny Goblin Label

```text
The jars have old labels that disagree. Do not drink yet.
```
