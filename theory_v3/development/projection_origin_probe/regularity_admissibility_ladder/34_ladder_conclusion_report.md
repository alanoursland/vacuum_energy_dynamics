# Regularity-Admissibility Ladder: Conclusion

## Status

This sub-branch gives a concrete mathematical interpretation of the projection
origin probe after the first four notes.

The key transformation is:

```text
u = a^3 f.
```

Under this transformation:

```text
L_w^*L[f] = S
```

becomes:

```text
-u'' = aS.
```

The candidate weighted energy becomes ordinary Dirichlet energy:

```text
1/2 <L[f],L[f]>_w
  =
1/2 integral_0^1 (u')^2 dx.
```

## Regularity Interpretation

Regularity of:

```text
f = u/a^3
```

at `x=1` imposes admissibility conditions on:

```text
F = aS.
```

The first condition is:

```text
integral_0^1 aS dx = 0.
```

The regularity ladder is:

```text
C^0 f:
  integral aS = 0

C^1 f:
  integral aS = 0
  S(1)=0

C^R f:
  integral aS = 0
  S vanishes to order R at x=1.
```

## Row Families

In `y=x^2`, the original row functions are:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1).
```

They span the finite coefficient-space kernel of the first admissibility
functional:

```text
S -> integral_0^1 aS dx.
```

For higher regularity level `R`, the adapted row family is:

```text
chi_(R,k)(y)
  =
  y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

The primitive-power parameter is:

```text
m = R + 2.
```

So the observed primitive power:

```text
m = 2
```

corresponds to:

```text
R = 0,
```

the boundedness level for `f = u/a^3`.

## Balanced Source Classes

The balanced source basis for regularity level `R` is:

```text
B_(R,q)(y) = (1-y)^R[y^q-c_(R,q)].
```

The coefficient is:

```text
c_(R,q)
  =
  B(q+1/2,R+2)/B(1/2,R+2)
  =
  (1/2)_q/(R+5/2)_q.
```

These sources satisfy the first admissibility cancellation for the `C^R`
class.

## Main Interpretation

The original projection hierarchy is no longer best described as a candidate
energy matrix.

It is best described as:

```text
the row family adapted to the first regularity/admissibility kernel generated
by the transformed energy problem.
```

Higher primitive powers are not arbitrary replicas. They correspond to higher
regularity levels:

```text
m = R + 2.
```

## What Remains Open

The internal mathematical structure is now substantially clarified. The
remaining open questions are external:

```text
Why should this energy functional be physically fundamental?
Why should boundedness of f be the selected regularity target?
Why should the domain be the transformed Green domain used here?
Why should w=a^4 be the projection weight from first principles?
```

The strongest internal result is:

```text
m=2 is selected by the boundedness-level regularity problem.
```

The strongest external gap is:

```text
the boundedness-level regularity problem itself has not been physically
derived.
```
