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

## Boundary-Contact Interpretation

Boundedness and boundary contact of:

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

The endpoint-contact ladder is:

```text
R=0 bounded/non-contact level:
  integral aS = 0

R=1 contact level:
  integral aS = 0
  S(1)=0

R contact level:
  integral aS = 0
  S vanishes to order R at x=1.
```

This is not ordinary `C^R` regularity. A smooth function can have only the base
contact order in `u=a^3 f`. For example, `f=1` gives `u=a^3` and the source
`S=-u''/a=6a-24x^2`, so `S(1)=-24`. Thus higher `R` labels endpoint contact /
source suppression, not ordinary differentiability.

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

For higher endpoint-contact level `R`, the adapted row family is:

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

The balanced source basis for endpoint-contact level `R` is:

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

These sources satisfy the first admissibility cancellation and the endpoint
suppression for the `R` contact class.

## Main Interpretation

The original projection hierarchy is no longer best described as a candidate
energy matrix.

It is best described as:

```text
the row family adapted to the first regularity/admissibility kernel generated
by the transformed energy problem.
```

Higher primitive powers are not arbitrary replicas. They correspond to higher
boundary-contact/admissibility levels:

```text
m = R + 2.
```

## What Remains Open

The internal mathematical structure is now substantially clarified. The
remaining open questions are external:

```text
Why should this energy functional be physically fundamental?
Why should boundedness/contact level zero of f be the selected target?
Why should the domain be the transformed Green domain used here?
Why should w=a^4 be the projection weight from first principles?
```

The strongest internal result is:

```text
m=2 is selected by the bounded/non-contact admissibility problem.
```

The strongest external gap is:

```text
the bounded/non-contact admissibility problem itself has not been physically
derived.
```
