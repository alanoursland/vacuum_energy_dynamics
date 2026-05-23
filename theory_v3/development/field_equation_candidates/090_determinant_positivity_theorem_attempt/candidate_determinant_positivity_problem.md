# candidate_determinant_positivity_problem — Analysis Note

## Result

`candidate_determinant_positivity_problem.py` opens Group 90 as a determinant positivity theorem attempt.

The imported Group 89 state is correct:

```text
closed rational A_N entry formula derived;
det(A_N)>0 verified through N=10;
pivots nonzero through N=10;
moment-pairing factorization derived;
profile generation validated through N=10;
all-order determinant theorem open;
all-order limit/convergence open;
parent divergence identity unproven;
recombination blocked.
```

The group target is also correct:

```text
test proof routes, not just more finite examples.
```

## Interpretation

This opener was the right move after Group 89.

Group 89 had sharpened the determinant problem into a moment-pairing nondegeneracy target. Group 90 correctly asks whether positivity can be proven from that structure.

The important starting distinction is:

```text
det(A_N) nonzero:
  enough for hierarchy coefficient existence and uniqueness.

det(A_N) positive:
  stronger than needed, but attractive if true because it would suggest a clean positivity theorem.
```

Group 90 begins by testing the stronger positivity route.

## What Changed

The determinant problem becomes an explicit theorem attempt rather than a computational ledger. That is real progress because it starts testing proof strategies.

## What Did Not Change

The opener correctly prevents the dangerous overclaim:

```text
finite determinant evidence is not all-order proof.
```

This matters because the later outputs show why that warning was necessary.

## Steering Consequence

The group should be judged by whether it closes, refines, or breaks the positivity route. The raw outputs show that it breaks the all-order positivity conjecture at `N=11`, while leaving the weaker nonzero/invertibility route alive.
