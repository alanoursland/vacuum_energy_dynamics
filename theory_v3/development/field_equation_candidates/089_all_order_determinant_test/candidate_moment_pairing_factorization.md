# candidate_moment_pairing_factorization — Analysis Note

## Result

`candidate_moment_pairing_factorization.py` rewrites the hierarchy matrix as a moment-pairing matrix.

With weight:

```text
mu(t)=t^(-1/2)(1-t)^4
```

and:

```text
q_k(t) = t^k - ((2k-1)/(2k+3)) t^(k-1)
```

the matrix entries are:

```text
A_N[k,j] = <t^j, q_k(t)>_mu
```

The derived rational entry is:

```text
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

with difference check:

```text
0
```

## Interpretation

This is the most important conceptual result of Group 89.

The determinant is no longer opaque. It is a pairing determinant between two finite subspaces:

```text
coefficient subspace:
  span{t, t^2, ..., t^N}

constraint subspace:
  span{q_1, q_2, ..., q_N}
```

under the positive Beta-type weight:

```text
mu(t)=t^(-1/2)(1-t)^4.
```

That reframes the all-order determinant theorem as a subspace nondegeneracy problem.

## What Changed

The all-order theorem target becomes much sharper.

Before:

```text
prove det(A_N) != 0.
```

After:

```text
prove the moment pairing between span{t..t^N}
and span{q_1..q_N} is nondegenerate for all N.
```

This is a better mathematical problem. It may connect to orthogonal polynomials, biorthogonal systems, sign-regular matrices, or Gram determinant theory.

## What Did Not Change

The script does not prove the subspace pairing is nondegenerate for all `N`. It identifies the structure.

## Steering Consequence

This result makes `90_determinant_positivity_theorem_attempt` much more plausible. The future proof should attack this moment-pairing nondegeneracy directly, not just compute more determinants.
