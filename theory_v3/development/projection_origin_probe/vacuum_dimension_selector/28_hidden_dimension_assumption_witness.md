# Vacuum Dimension Selector 28: Hidden Dimension Assumption Witness

## Purpose

This proof distinguishes two different moves:

```text
evaluate a formula after assuming D=4
solve a selector equation whose positive solution is D=4
```

## Validated Checks

- assuming `D=4` gives two spin-2 degrees of freedom: passed
- solving `D(D-3)/2 = 2` gives positive solution `D=4`: passed

## Computation

Assumption route:

```text
N_spin2(4) = 2
```

Selector route:

```text
N_spin2(D) = D*(D - 3)/2
N_spin2(D) = 2
solutions = [-1, 4]
positive solution = 4
```

## Interpretation

The folder should prefer selector equations over post-hoc evaluation whenever
possible. Where a report assumes `D=4`, it should label that assumption rather
than presenting the result as a dimension derivation.
