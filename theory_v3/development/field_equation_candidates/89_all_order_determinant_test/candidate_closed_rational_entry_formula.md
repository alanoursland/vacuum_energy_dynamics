# candidate_closed_rational_entry_formula — Analysis Note

## Result

`candidate_closed_rational_entry_formula.py` derives a closed rational form for the matrix entries.

The Beta moment is:

```text
beta_moment(s) =
768 / ((2s+1)(2s+3)(2s+5)(2s+7)(2s+9))
```

The hierarchy matrix entry is:

```text
A_N[k,j] =
1536*(4j - 6k + 3)
/
((2k + 3)
 (2j + 2k - 1)
 (2j + 2k + 1)
 (2j + 2k + 3)
 (2j + 2k + 5)
 (2j + 2k + 7)
 (2j + 2k + 9))
```

A test case gives:

```text
k=2, j=3:
entry = 512/4849845
direct check difference = 0
```

## Interpretation

This is a key technical cleanup and a real mathematical refinement.

Group 88 already had the Beta system. Group 89 turns that system into a fully rational matrix-entry formula. That matters for two reasons.

First, it makes the determinant problem explicit:

```text
determinant of a rational matrix with known entry formula.
```

Second, it removes symbolic-special-function ambiguity and runtime bloat. The matrix no longer depends on SymPy’s Beta/Gamma simplification behavior.

## What Changed

The all-order determinant problem is now about a concrete rational matrix:

```text
A_N[k,j] = rational function of k and j.
```

That is a much sharper theorem target than:

```text
determinant of some Beta-function matrix.
```

## What Did Not Change

This entry formula does not prove determinant positivity. It only gives the exact object whose determinant must be studied.

## Steering Consequence

This result sets up determinant and pivot tests cleanly. It also suggests future theorem routes involving rational Cauchy-like matrices, sign-regularity, or moment-pairing nondegeneracy.
