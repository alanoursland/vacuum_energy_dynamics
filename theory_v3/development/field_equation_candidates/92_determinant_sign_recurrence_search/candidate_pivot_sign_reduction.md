# candidate_pivot_sign_reduction — Analysis Note

## Result

`candidate_pivot_sign_reduction.py` derives the determinant sign reduction.

Define:

```text
D_N = det(A_N)
p_N = D_N / D_(N-1)
D_0 = 1
```

Then:

```text
sign(D_N) = product_{m=1}^N sign(p_m).
```

The script verifies through `N=30` that the product of pivot signs matches the determinant sign pattern:

```text
finite reduction failures through N=30: []
```

The verified pattern is:

```text
N=1..10:
  product_sign = det_sign = +1

N=11..30:
  product_sign = det_sign = (-1)^N
```

## Interpretation

This is the central structural reduction of Group 92.

The determinant sign theorem no longer needs to be attacked directly. It can be reduced to the pivot sign theorem:

```text
p_N > 0 for N <= 10
p_N < 0 for N >= 11.
```

That is a smaller and sharper theorem target.

This matters because determinant signs accumulate multiplicatively from pivots. Once the pivot signs are known, the determinant signs are automatic.

## What Changed

The sign-pattern problem is reduced from:

```text
prove sign(det(A_N))
```

to:

```text
prove sign(p_N).
```

That is real progress.

## What Did Not Change

This reduction does not prove the pivot sign theorem. It only identifies the right object.

The finite verification through `N=30` remains evidence, not all-order proof.

## Steering Consequence

The next useful target is the sign-normalized pivot:

```text
pi_N = p_N   for N<=10
pi_N = -p_N  for N>=11
```

If `pi_N>0` can be proven for all `N`, the determinant sign pattern follows.
