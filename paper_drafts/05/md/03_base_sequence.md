# 3. Base Sequence

At contact level `R = 0`, the functional is

```text
C_0[P] = int_0^1 P(y)(1-y)y^(-1/2) dy.
```

The adjacent monomial ratio is

```text
r_{0,k}
  = B(k + 1/2, 2)/B(k - 1/2, 2)
  = (2k - 1)/(2k + 3).
```

The base row family is therefore

```text
chi_{0,k}(y) = y^k - ((2k - 1)/(2k + 3)) y^(k-1).
```

This formula is not a fitted pattern.  It is the scalar condition that removes
the `C_0` moment from the two-term row.  In the `x` variable, it is equivalent
to the cancellation

```text
int_0^1 [x^(2k) - r_{0,k}x^(2k-2)] (1-x^2) dx = 0.
```

The same coefficient also appears from the primitive identity

```text
G_{k,2}(x) = x^(2k-1)(1-x^2)^2.
```

Differentiating `G_{k,2}` gives a weighted two-term polynomial with the same
survivor ratio.  This identifies the base coefficient as an endpoint
admissibility coefficient, not as an arbitrary projection artifact.

It is useful to distinguish this base ratio from a second compact moment
sequence that appears in verification scripts:

```text
beta(s) = 2 int_0^1 x^(2s)(1-x^2)^4 dx
        = B(s + 1/2, 5).
```

This sequence belongs to the projection pairing weight.  The survivor ratio
itself is selected one layer earlier by the admissibility functional `C_R`.

