# 6. Mandatory-Hair Lemma

Because the field equations are fourth order, a regular stellar surface must
match not only the metric variables but also the scalar curvature data. In the
simple uniform-density witness, the interior trace solution has the form

```text
R_in(r) = kappa rho c^2 + A sinh(mr)/r,
m = 1/ell.
```

The exterior solution is

```text
R_ext(r) = C exp(-mr)/r .
```

Hairless exterior means `C = 0`, so at the surface `r = R_b` the matching
conditions require

```text
R_in(R_b) = 0,
R_in'(R_b) = 0.
```

Eliminating the interior amplitude gives the condition

```text
x cosh x = sinh x,
x = m R_b > 0.
```

Define

```text
h(x) = x cosh x - sinh x .
```

Then

```text
h(0) = 0,
h'(x) = x sinh x > 0    for x > 0.
```

Therefore `h(x) > 0` for every positive `x`, and the hairless condition has no
positive solution. The only way out is the trivial unsourced case.

The lemma is:

```text
For a nontrivial sourced static body in the `R + a R^2` theory, exterior
scalaron hair is mandatory for every a != 0.
```

The final paper should generalize or carefully caveat this witness for smooth
density profiles. For this draft, the uniform-density calculation is the
explicit no-hairless-matching witness.
