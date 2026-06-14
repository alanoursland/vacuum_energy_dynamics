# Appendix D. Yukawa Parameter Translation

The weak-field potentials of `R + a R^2` gravity around a point source are

```text
phi(r) = -(GM/r) [1 + (1/3) exp(-r/ell)],
psi(r) = -(GM/r) [1 - (1/3) exp(-r/ell)].
```

The scalaron range is

```text
ell = sqrt(6a).
```

The Newtonian potential therefore receives a Yukawa correction with

```text
alpha = 1/3,
lambda = ell.
```

The live data gate uses the validated Lee 2020 supplemental `chi^2` table
[Lee et al., 2020] and the Tan 2020 author-provided `alpha(lambda)` table
[Tan et al., 2020]. Their relevant crossings are:

```text
Lee 2020:
  |alpha| = 1      lambda = 38.63 um
  alpha = 1/3      lambda = 54.03 um

Tan 2020:
  |alpha| = 1      lambda = 47.74 um
  alpha = 1/3      lambda = 57.29 um
```

Lee 2020 [Lee et al., 2020] is therefore the binding current curve for the
scalaron coupling, giving

```text
ell < 54.03 um
```

if `a` is allowed. This number is a bound on the `R^2` route after dropping
static frame indifference; it is not an input to the selection theorem. The
earlier vector-path extraction from Lee Fig. 5 [Lee et al., 2020] gave
`54.05 um`, providing an independent cross-check of the supplemental-table
extraction.
