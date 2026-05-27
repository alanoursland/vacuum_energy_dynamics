# Synthesis Proof 28: Higher-Contact Kernel Bridge

## Purpose

This report tests how the first-admissibility kernel bridge changes for higher
endpoint-contact classes.

For the `R` endpoint-contact source class:

```text
S(y) = (1-y)^R P(y),
```

the first admissibility condition becomes:

```text
integral a^(R+1) P dx = 0.
```

## Validated Checks

- a^R shifted psi families retain expected rank: passed
- balanced y^q-c_(R,q) bases span R-weighted first-admissibility kernels: passed
- unshifted psi kernel bridge is special to R=0: passed

## Result

For `R=0`, the `psi_k` rows span the first-admissibility kernel.

For `R>0`, the kernel changes because the balancing moment changes from
`a` to `a^(R+1)`. The corresponding balanced basis is:

```text
y^q - c_(R,q),
```

not the unshifted `psi_k` family.

The shifted family:

```text
(1-y)^R psi_k(y)
```

retains rank, but it is not the same as the canonical balanced kernel basis.

Exact tested data:

```text
R=0, N=1: rank(a^R psi)= 1, unshifted psi in R-kernel? True, balanced rank=1
R=0, N=2: rank(a^R psi)= 2, unshifted psi in R-kernel? True, balanced rank=2
R=0, N=3: rank(a^R psi)= 3, unshifted psi in R-kernel? True, balanced rank=3
R=0, N=4: rank(a^R psi)= 4, unshifted psi in R-kernel? True, balanced rank=4
R=0, N=5: rank(a^R psi)= 5, unshifted psi in R-kernel? True, balanced rank=5
R=0, N=6: rank(a^R psi)= 6, unshifted psi in R-kernel? True, balanced rank=6
R=0, N=7: rank(a^R psi)= 7, unshifted psi in R-kernel? True, balanced rank=7
R=0, N=8: rank(a^R psi)= 8, unshifted psi in R-kernel? True, balanced rank=8
R=1, N=1: rank(a^R psi)= 1, unshifted psi in R-kernel? False, balanced rank=1
R=1, N=2: rank(a^R psi)= 2, unshifted psi in R-kernel? False, balanced rank=2
R=1, N=3: rank(a^R psi)= 3, unshifted psi in R-kernel? False, balanced rank=3
R=1, N=4: rank(a^R psi)= 4, unshifted psi in R-kernel? False, balanced rank=4
R=1, N=5: rank(a^R psi)= 5, unshifted psi in R-kernel? False, balanced rank=5
R=1, N=6: rank(a^R psi)= 6, unshifted psi in R-kernel? False, balanced rank=6
R=1, N=7: rank(a^R psi)= 7, unshifted psi in R-kernel? False, balanced rank=7
R=1, N=8: rank(a^R psi)= 8, unshifted psi in R-kernel? False, balanced rank=8
R=2, N=1: rank(a^R psi)= 1, unshifted psi in R-kernel? False, balanced rank=1
R=2, N=2: rank(a^R psi)= 2, unshifted psi in R-kernel? False, balanced rank=2
R=2, N=3: rank(a^R psi)= 3, unshifted psi in R-kernel? False, balanced rank=3
R=2, N=4: rank(a^R psi)= 4, unshifted psi in R-kernel? False, balanced rank=4
R=2, N=5: rank(a^R psi)= 5, unshifted psi in R-kernel? False, balanced rank=5
R=2, N=6: rank(a^R psi)= 6, unshifted psi in R-kernel? False, balanced rank=6
R=2, N=7: rank(a^R psi)= 7, unshifted psi in R-kernel? False, balanced rank=7
R=2, N=8: rank(a^R psi)= 8, unshifted psi in R-kernel? False, balanced rank=8
R=3, N=1: rank(a^R psi)= 1, unshifted psi in R-kernel? False, balanced rank=1
R=3, N=2: rank(a^R psi)= 2, unshifted psi in R-kernel? False, balanced rank=2
R=3, N=3: rank(a^R psi)= 3, unshifted psi in R-kernel? False, balanced rank=3
R=3, N=4: rank(a^R psi)= 4, unshifted psi in R-kernel? False, balanced rank=4
R=3, N=5: rank(a^R psi)= 5, unshifted psi in R-kernel? False, balanced rank=5
R=3, N=6: rank(a^R psi)= 6, unshifted psi in R-kernel? False, balanced rank=6
R=3, N=7: rank(a^R psi)= 7, unshifted psi in R-kernel? False, balanced rank=7
R=3, N=8: rank(a^R psi)= 8, unshifted psi in R-kernel? False, balanced rank=8
R=4, N=1: rank(a^R psi)= 1, unshifted psi in R-kernel? False, balanced rank=1
R=4, N=2: rank(a^R psi)= 2, unshifted psi in R-kernel? False, balanced rank=2
R=4, N=3: rank(a^R psi)= 3, unshifted psi in R-kernel? False, balanced rank=3
R=4, N=4: rank(a^R psi)= 4, unshifted psi in R-kernel? False, balanced rank=4
R=4, N=5: rank(a^R psi)= 5, unshifted psi in R-kernel? False, balanced rank=5
R=4, N=6: rank(a^R psi)= 6, unshifted psi in R-kernel? False, balanced rank=6
R=4, N=7: rank(a^R psi)= 7, unshifted psi in R-kernel? False, balanced rank=7
R=4, N=8: rank(a^R psi)= 8, unshifted psi in R-kernel? False, balanced rank=8
R=5, N=1: rank(a^R psi)= 1, unshifted psi in R-kernel? False, balanced rank=1
R=5, N=2: rank(a^R psi)= 2, unshifted psi in R-kernel? False, balanced rank=2
R=5, N=3: rank(a^R psi)= 3, unshifted psi in R-kernel? False, balanced rank=3
R=5, N=4: rank(a^R psi)= 4, unshifted psi in R-kernel? False, balanced rank=4
R=5, N=5: rank(a^R psi)= 5, unshifted psi in R-kernel? False, balanced rank=5
R=5, N=6: rank(a^R psi)= 6, unshifted psi in R-kernel? False, balanced rank=6
R=5, N=7: rank(a^R psi)= 7, unshifted psi in R-kernel? False, balanced rank=7
R=5, N=8: rank(a^R psi)= 8, unshifted psi in R-kernel? False, balanced rank=8
```

## Interpretation

The exact `psi` kernel bridge is strongest at the first admissibility level
`R=0`.

Higher endpoint-contact classes require rebalanced source bases:

```text
B_(R,q) = a^R[y^q-c_(R,q)].
```

This matches the source-class ladder already found from the transformed energy
problem.
