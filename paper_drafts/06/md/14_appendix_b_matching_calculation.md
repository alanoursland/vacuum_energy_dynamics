# Appendix B. Scalaron Matching Calculation

For a uniform-density body, the static trace equation inside the source has a
particular solution plus a regular homogeneous solution:

```text
R_in(r) = kappa rho c^2 + A sinh(mr)/r .
```

Outside the source,

```text
R_ext(r) = C exp(-mr)/r .
```

Fourth-order matching requires continuity of `R` and `R'` at the surface.
Hairless exterior sets `C = 0`, so the interior solution must obey

```text
R_in(R_b) = 0,
R_in'(R_b) = 0.
```

Eliminating `A` gives

```text
x cosh x = sinh x,
x = m R_b .
```

Appendix C proves this has no positive solution. The final paper should state
the source-class assumptions precisely and either extend the result beyond the
uniform-density witness or present the witness as the theorem's demonstrated
case.
