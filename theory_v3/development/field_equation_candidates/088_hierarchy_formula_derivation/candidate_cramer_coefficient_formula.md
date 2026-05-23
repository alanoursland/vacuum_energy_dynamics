# candidate_cramer_coefficient_formula — Analysis Note

## Result

`candidate_cramer_coefficient_formula.py` states and verifies the Cramer determinant formula:

```text
a_j = det(A_N with column j replaced by b_N) / det(A_N)
```

for:

```text
det(A_N) != 0.
```

For `N=1..4`, the determinants are nonzero and the Cramer coefficients match exactly:

```text
N=1:
  coeffs = [39]

N=2:
  coeffs = [-12, 51]

N=3:
  coeffs = [153, -969, 1615]

N=4:
  coeffs = [-4332/131, 51186/131, -166060/131, 163875/131]
```

All Cramer differences are zero.

## Interpretation

This result identifies the exact mathematical bottleneck for the hierarchy.

For every finite `N`, if:

```text
det(A_N) != 0
```

then the hierarchy profile exists and is unique, with coefficients given by Cramer’s rule.

That is important because it turns the general existence question into a determinant theorem.

Before this script, the open all-order question was vague:

```text
does the hierarchy continue?
```

After this script, the open question is precise:

```text
is det(A_N) nonzero for all N?
```

## What Changed

The finite hierarchy now has a determinant-based coefficient formula.

That is real progress because it gives future groups a specific target. We do not need to guess at profiles forever. We need to understand the determinant structure of the Beta moment matrix.

## What Did Not Change

The script only verifies determinants through `N=4`. It does not prove nonzero determinant for all `N`.

So the correct status is:

```text
Cramer coefficient formula derived;
all-order determinant theorem open.
```

## Steering Consequence

The next natural route is either:

```text
all_order_determinant_test
```

or:

```text
hierarchy_recurrence_search.
```

The determinant route is sharper if the goal is existence/uniqueness. The recurrence route is sharper if the goal is closed-form coefficient structure.
