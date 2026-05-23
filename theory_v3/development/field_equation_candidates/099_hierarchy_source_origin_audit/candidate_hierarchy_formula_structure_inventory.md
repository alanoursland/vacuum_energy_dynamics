# candidate_hierarchy_formula_structure_inventory — Analysis Note

## Result

`candidate_hierarchy_formula_structure_inventory.py` records the explicit hierarchy structure:

```text
beta_moment(s)
=
768 / [(2s+1)(2s+3)(2s+5)(2s+7)(2s+9)]
```

and:

```text
A[k,j]
=
1536(4j - 6k + 3)
/
[
(2k+3)
(2j+2k-1)
(2j+2k+1)
(2j+2k+3)
(2j+2k+5)
(2j+2k+7)
(2j+2k+9)
].
```

The script records the important structural observations:

```text
beta_moment depends on s through five consecutive odd linear factors;

A[k,j] uses beta_moment(k+j) and beta_moment(k+j-1);

the row coefficient (2k-1)/(2k+3) depends on k only.
```

It also finds that raw `A_N` is not symmetric:

```text
A_4 symmetry failures:
  nonempty.
```

The governance section records:

```text
moment-like structure:
  PASS

Gram/Hessian symmetry:
  WARN, A_N is not symmetric in raw form

physical origin:
  OBLIGATION, formula inventory is not a derivation.
```

## Interpretation

This is a strong formula-inventory result.

The hierarchy is unmistakably moment-like: entries are built out of shifted moment values `k+j` and `k+j-1`. That supports the idea that `A_N` may come from a projection or moment system.

But the raw asymmetry is important. A simple variational-Hessian interpretation is not licensed by inspection, because a Hessian/Gram matrix would normally be symmetric unless there is a weighting, row operation, non-self-adjoint projection, or nontrivial variable/test basis pairing.

So Group 099 sharpens the plausible origin:

```text
moment/projection origin:
  plausible

raw Hessian/Gram origin:
  not licensed without additional structure.
```

## What Changed

The formula for `A[k,j]` is now simplified into a direct rational expression. That is useful.

The numerator:

```text
4j - 6k + 3
```

may become important. It shows why signs are not trivially positive and why row-sign normalization mattered earlier.

## What Did Not Change

Moment-like structure is not a physical source law.

Raw `A_N` is not a covariant energy functional.

## Carry-forward status

```text
A_N_FORMULA_INVENTORIED
BETA_MOMENT_ODD_FACTOR_STRUCTURE_IDENTIFIED
A_N_MOMENT_LIKE_STRUCTURE_SUPPORTED
RAW_A_N_NOT_SYMMETRIC
VARIATIONAL_HESSIAN_ORIGIN_NOT_LICENSED_BY_RAW_FORM
PHYSICAL_ORIGIN_NOT_DERIVED
```
