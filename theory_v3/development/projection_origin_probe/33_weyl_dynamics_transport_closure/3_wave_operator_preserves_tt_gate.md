# 3. Wave operator preserves TT gate

A TT component `u = A cos(kz - wt)` obeys the wave equation when

```text
w^2 = k^2.
```

The plus polarization has `h_xx = u`, `h_yy = -u`, so trace cancellation is preserved by the same wave operator.

Validated checks:

```text
(∂_t^2 - ∂_z^2) u = 0 when w^2 = k^2
(∂_t^2 - ∂_z^2)(h_xx + h_yy) = 0
```

Result: TT transport can propagate without leaking into the scalar trace channel.
