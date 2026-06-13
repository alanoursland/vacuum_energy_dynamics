# 1. Introduction

Projection calculations often produce rational coefficients that initially
look accidental.  In the hierarchy studied here, the recurring coefficient is

```text
r_{0,k} = (2k - 1)/(2k + 3).
```

The first interpretation of this number was determinant-oriented: one forms a
finite projection matrix, computes exact determinants, and asks whether a
positive determinant pattern explains why the systems remain solvable.  That
question is too narrow.  The determinant sequence is evidence of
nondegeneracy, but positivity is not the structural property.

This paper gives a standalone mathematical interpretation of the coefficient
and its higher-contact generalization.  The coefficient is an adjacent moment
ratio.  More precisely, for each nonnegative endpoint-contact index `R`,

```text
r_{R,k} = (2k - 1)/(2k + 2R + 3)
```

is selected by the weighted beta functional

```text
C_R[P] = int_0^1 P(y)(1-y)^(R+1)y^(-1/2) dy.
```

The index `R` is not an ordinary differentiability label.  It records how
many endpoint contact conditions are imposed after the projection problem is
written in its boundary-adapted variable.

The second point is linear algebraic.  The finite projection matrices are best
viewed as cross-Gram matrices.  Their rows and columns are two different
bases, or coordinate families, for the same admissible finite-dimensional
space.  Once this is recognized, invertibility follows from nondegeneracy of
the positive weighted pairing on that space.  A cross-Gram matrix need not
have the determinant behavior one expects from a symmetric positive Gram
matrix; asking for determinant positivity was therefore the wrong diagnostic.

The paper is intentionally independent of the physical program from which the
coefficient was extracted.  Its purpose is to isolate the reusable
mathematics: a regularity ladder, a moment hierarchy, and a cross-Gram
invertibility mechanism.

