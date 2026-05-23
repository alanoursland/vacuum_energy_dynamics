# candidate_difference_numerator_probe — Analysis Note

## Result

`candidate_difference_numerator_probe.py` probes numerator and denominator signs for exact positive difference expressions through `N=30`.

It checks branch differences and interlacing differences.

The result is:

```text
sign failures: []
probe count: 54
```

The first probes all show:

```text
numerator_sign = 1
denominator_sign = 1
expr_sign = 1.
```

Examples include:

```text
branch_gap_11_13
branch_ratio_11_13
interlace_left_11_12
interlace_right_12_13
```

all with positive numerator, denominator, and expression signs.

## Interpretation

This is the most important theorem-target refinement in Group 97.

The branch and interlacing differences are rational expressions. In the tested range, their positivity is not coming from denominator sign ambiguity; both numerator and denominator are positive.

That means the next theorem target can become:

```text
prove numerator positivity for exact rational difference expressions.
```

This is sharper than proving raw difference positivity, because it tells the next group what to factor, simplify, or structurally interpret.

## Carry-forward status

```text
DIFFERENCE_NUMERATOR_POSITIVITY_SUPPORTED_THROUGH_N30
DIFFERENCE_DENOMINATOR_POSITIVITY_SUPPORTED_THROUGH_N30
DIFFERENCE_NUMERATOR_POSITIVITY_TARGET_IDENTIFIED
ALL_ORDER_DIFFERENCE_NUMERATOR_THEOREM_OPEN
```
