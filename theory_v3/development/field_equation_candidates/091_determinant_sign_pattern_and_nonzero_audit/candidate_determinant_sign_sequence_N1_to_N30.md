# candidate_determinant_sign_sequence_N1_to_N30 — Analysis Note

## Result

`candidate_determinant_sign_sequence_N1_to_N30.py` computes exact determinant and pivot signs through `N=30`.

The tested pattern is perfectly matched:

```text
N=1..10:
  det_sign = +1
  pivot_sign = +1

N=11..30:
  det_sign = (-1)^N
  pivot_sign = -1
```

The script reports:

```text
mismatches = []
zero failures = []
```

and governance:

```text
det(A_N) nonzero through N=30;
tested sign pattern matches through N=30;
N=1..30 is strong finite evidence, not all-order proof.
```

## Interpretation

This is the main positive result of Group 91.

The determinant did not become chaotic after the positivity failure. It appears to follow a simple corrected sign law:

```text
det(A_N)>0 for N<=10;
sign(det(A_N))=(-1)^N for N>=11
```

with pivot signs:

```text
pivot_N>0 for N<=10;
pivot_N<0 for N>=11.
```

That is a much better state than merely saying “positivity failed.”

The sign flip becomes structure, not noise.

## What Changed

The determinant branch now has a concrete sign-pattern conjecture.

Carry-forward status should be:

```text
DETERMINANT_NONZERO_VERIFIED_N1_TO_N30
SIGN_PATTERN_SUPPORTED_N1_TO_N30
```

not:

```text
DETERMINANT_POSITIVITY_SUPPORTED
```

## What Did Not Change

This is finite evidence. It does not prove the sign law for all `N`.

## Steering Consequence

The next theorem target should be a determinant or pivot recurrence that explains:

```text
why pivot_N changes sign at N=11
and remains negative in the tested range.
```
