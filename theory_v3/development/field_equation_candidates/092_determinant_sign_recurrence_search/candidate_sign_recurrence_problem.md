# candidate_sign_recurrence_problem — Analysis Note

## Result

`candidate_sign_recurrence_problem.py` opens Group 92 as a determinant sign-recurrence search.

It imports the corrected Group 91 status:

```text
determinant positivity disproven by N=11;
determinant nonzero verified through N=30;
sign pattern supported through N=30;
profile generation survives sign flip;
all-order nonzero theorem open;
sign-pattern theorem open;
parent divergence identity unproven;
recombination blocked.
```

The script sets the correct target:

```text
reduce sign pattern to pivot-sign theorem or recurrence.
```

It also explicitly rejects:

```text
reviving positivity;
treating finite pattern as proof;
using recurrence work as a parent-equation jump.
```

## Interpretation

This is the right opening after Group 91.

Group 91 cleaned up the determinant branch by killing positivity and preserving nonzero invertibility. Group 92 now asks whether the corrected sign pattern has a recurrence explanation.

That is a meaningful next step because the sign pattern is now structured enough to deserve a theorem attempt:

```text
det(A_N)>0 for N<=10;
sign(det(A_N))=(-1)^N for N>=11 in tested range.
```

The natural way to explain that is through the pivot sequence.

## What Changed

The determinant branch moves from audit to mechanism search.

Group 91 said:

```text
here is the corrected sign pattern.
```

Group 92 asks:

```text
what generates that sign pattern?
```

## What Did Not Change

The opener correctly preserves the boundary:

```text
finite evidence is not theorem;
raw positivity remains false;
parent divergence remains unproven;
recombination remains blocked.
```

## Steering Consequence

The group should be judged by whether it derives a useful reduction or recurrence target, not by whether it magically proves all-order invertibility. The results show it derives the pivot reduction and identifies a bounded recurrence failure.
