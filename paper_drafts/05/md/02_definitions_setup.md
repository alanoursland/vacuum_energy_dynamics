# 2. Definitions and Setup

All polynomial spaces are over the real numbers.  The basic variable is

```text
y = x^2,        0 <= y <= 1.
```

For each integer `R >= 0`, define the weighted moment functional

```text
C_R[P] = int_0^1 P(y) w_R(y) dy,
w_R(y) = (1-y)^(R+1)y^(-1/2).
```

The monomial moments are

```text
mu_{R,k} = C_R[y^k] = B(k + 1/2, R + 2),
```

where `B` is the beta function.

For `k >= 1`, define

```text
r_{R,k} = mu_{R,k}/mu_{R,k-1}
```

and the adapted row polynomial

```text
chi_{R,k}(y) = y^k - r_{R,k} y^(k-1).
```

By construction,

```text
C_R[chi_{R,k}] = 0.
```

Thus the row family lies in the first admissibility kernel

```text
K_R = {P : C_R[P] = 0}.
```

For finite truncation degree `N`, we use the row subspace

```text
K_{R,N} = K_R cap span{1,y,...,y^N}.
```

The collection

```text
chi_{R,1}, ..., chi_{R,N}
```

is a basis of `K_{R,N}`.

We also use a balanced source basis.  One convenient normalization is

```text
B_{R,q}(y) = (1-y)^R [y^q - c_{R,q}],
```

with

```text
c_{R,q} = B(q + 1/2, R + 2)/B(1/2, R + 2).
```

This normalization enforces the same admissibility cancellation against the
base endpoint functional.

