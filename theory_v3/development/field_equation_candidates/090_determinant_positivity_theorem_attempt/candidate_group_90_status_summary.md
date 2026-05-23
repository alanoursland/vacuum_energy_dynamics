# candidate_group_90_status_summary — Analysis Note

## Result

`candidate_group_90_status_summary.py` reports:

```text
derivative/Sturm-like factorization derived;
Andreief determinant representation derived;
simple Chebyshev fixed-sign route blocked in tested form;
Hankel difference structure A=H1-RH0 derived;
determinant and pivot positivity evidence extended through N=12;
all-order determinant positivity theorem not proven;
proof target refined toward biorthogonal/Hankel/pivot recurrence routes;
all-order limit/convergence remains open;
parent divergence identity remains unproven;
recombination blocked.
```

The first, second, third, and fourth items are supported by the raw results.

The fifth item is incorrect.

The pivot-extension script shows determinant/pivot positivity fails at `N=11`, and pivot positivity also fails at `N=12`.

## Interpretation

The summary needs correction.

The honest Group 90 result is stronger and more negative than the planned summary:

```text
all-order determinant positivity is disproven as stated.
```

This is not bad news for the hierarchy itself, because coefficient generation only needs nonzero determinant, not positive determinant. But it is fatal to the positivity theorem target.

Corrected stable result:

```text
derivative/Sturm-like factorization derived;

Andreief determinant representation derived;

simple Chebyshev fixed-sign route blocked/not established;

Hankel difference structure A=H1-RH0 derived;

det(A_N)>0 through N=10;

det(A_11)<0;

det(A_12)>0;

pivot positivity fails at N=11 and N=12;

det(A_N) remains nonzero through N=12;

all-order positivity theorem disproven as stated;

all-order nonzero/invertibility theorem remains open;

determinant sign-pattern theorem now required;

all-order limit/convergence remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What Changed

Group 90 does not merely fail to prove positivity. It finds a counterexample to positivity at `N=11`.

That is real progress. It prevents a false theorem from carrying forward.

## What Did Not Change

All determinant values through `N=12` are nonzero, so the hierarchy/invertibility route is still alive.

The determinant theorem target changes from positivity to nonzero/sign-pattern.

## Steering Consequence

The next group should not be `91_biorthogonal_polynomial_construction` unless it is explicitly retargeted away from positivity.

Better next group:

```text
91_determinant_sign_pattern_and_nonzero_audit
```

Purpose:

```text
verify the N=11 sign flip;
test whether it is a script/indexing artifact or real;
generate determinant signs through a wider range;
separate positivity, nonzero invertibility, and sign-pattern claims.
```

Only after that audit should the project return to biorthogonal or recurrence theorem work.
