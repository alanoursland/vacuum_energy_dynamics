# Appendix A. Beta Function Evaluation

For `R >= 0`, define

```text
mu_{R,k} = int_0^1 y^k(1-y)^(R+1)y^(-1/2) dy.
```

Then

```text
mu_{R,k}
  = int_0^1 y^(k - 1/2)(1-y)^(R+1) dy
  = B(k + 1/2, R + 2).
```

Using

```text
B(a,b) = Gamma(a)Gamma(b)/Gamma(a+b),
```

the adjacent ratio is

```text
mu_{R,k}/mu_{R,k-1}
  = [Gamma(k + 1/2)/Gamma(k + R + 5/2)]
    [Gamma(k + R + 3/2)/Gamma(k - 1/2)].
```

Canceling gamma factors gives

```text
mu_{R,k}/mu_{R,k-1}
  = (k - 1/2)/(k + R + 3/2)
  = (2k - 1)/(2k + 2R + 3).
```

This proves the scalar ladder formula.

The compact verification sequence

```text
beta(s) = 2 int_0^1 x^(2s)(1-x^2)^4 dx
```

is evaluated by setting `y = x^2`, so `2 dx = y^(-1/2) dy`.  Hence

```text
beta(s) = int_0^1 y^s(1-y)^4 y^(-1/2) dy
        = B(s + 1/2, 5)
        = 24 Gamma(s + 1/2)/Gamma(s + 11/2).
```

