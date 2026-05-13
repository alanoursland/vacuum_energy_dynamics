# Candidate Trace-Normalization Declaration Option Sieve

## What this run is

This run classifies trace-normalization declaration options for Group 37.

It asks which ways of declaring how `B_s` reads `zeta` are coherent enough to carry into a joint declaration package sieve. It does not install any declaration value as theory state, select a normalization form, adopt Package B, derive a coefficient law, or open insertion.

## Main result

The run separates declaration-ready trace-normalization options from notation-risk, diagnostic-only, incomplete, and rejected options.

```text
scale-factor volume-log option: declaration-ready option
metric-coefficient volume-log option: declaration-ready option
per-dimension zeta option: notation-risk candidate option
linearized-only trace option: diagnostic-only
ambiguous convention option: incomplete
recovery-selected option: rejected shortcut
```

## Declaration-ready options

The scale-factor option is coherent if `B_s` is explicitly declared as scale-factor language, `zeta` is total volume-log trace, the traced dimension `d` is stated, and exact/linearized scope is specified. Its schematic form is:

```text
log(B_s) = zeta / d
```

The metric-coefficient option is coherent if `B_s` is explicitly metric-coefficient language, `zeta` is total volume-log trace, `d` is stated, and scope is explicit. Its schematic form is:

```text
log(B_s) = 2*zeta / d
```

Both are options only. Neither is selected, adopted, or derived.

## Fenced options

The per-dimension option may survive only if the `zeta_per_dim` convention is declared before comparison. It is notation-risk because dimension factors can be hidden in notation.

The linearized-only option is safe only as first-order diagnostic bookkeeping. It must not be promoted into an exact determinant law.

## Rejected option

A recovery-selected normalization is rejected as a declaration selector. Trace normalization may not be chosen because Schwarzschild recovery, PPN gamma, insertion convenience, or parent fit works.

## Rejected upgrades

The run rejects:

```text
hidden factor of two
hidden dimension
linearized as exact
recovery-selected normalization
```

## Final status

```text
Trace-normalization declaration options are classified.
Scale-factor and metric-coefficient volume-log options are declaration-ready options.
Per-dimension and linearized options require fencing.
No normalization form is selected, adopted, or derived.
Current status remains compatible-if-declared only.
Downstream gates remain closed.
```
