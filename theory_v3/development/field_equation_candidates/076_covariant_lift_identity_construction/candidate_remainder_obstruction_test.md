# candidate_remainder_obstruction_test — Result Note

## Result

`candidate_remainder_obstruction_test.py` tests the shared identity with a remainder:

```text
L_bulk = K
L_gauge = -K + rho
R_lift = rho
```

Closure requires:

```text
rho = 0
```

## Main Findings

This script identifies the main Group 76 obstruction.

The shared lift route can remain open only if a theorem proves one of:

```text
rho = 0;
rho is inert;
rho is gauge-exact with no physical remainder.
```

The script correctly rejects:

```text
dropping rho by prose;
choosing rho = 0 by hand.
```

## Boundary

The script does not prove `rho = 0`. It names `rho` as the live theorem burden.

## Steering Consequence

Proceed to gauge-exact remainder testing. The next question is whether the remainder can be separated into exact and physical parts.
