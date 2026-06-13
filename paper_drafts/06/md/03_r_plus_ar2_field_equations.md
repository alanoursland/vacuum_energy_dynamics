# 3. `R + a R^2` Field Equations and Scalaron Mode

The action considered is

```text
S = c^4/(16 pi G) int sqrt(-g) (R + a R^2 - 2 Lambda) d^4x + S_matter .
```

The coefficient `a` has dimensions of length squared. Linearizing about flat
space and taking the trace gives the scalar equation

```text
(1 - 6a Lap) R = kappa rho c^2
```

in the static weak-field limit, where `kappa = 8 pi G / c^4`.

For `a > 0`, this is a healthy massive scalar constraint with

```text
m^2 = 1/(6a),
ell = 1/m = sqrt(6a).
```

The case `a < 0` is tachyonic and is not the target of the selection theorem.
It is removed by ordinary flat-vacuum stability. The only live higher-curvature
coefficient after the ghost gate is therefore `a >= 0`.

The point-source weak-field potentials for the ghost-safe `R^2` realization
are

```text
phi(r) = -(GM/r) [1 + (1/3) exp(-r/ell)],
psi(r) = -(GM/r) [1 - (1/3) exp(-r/ell)].
```

The scalaron therefore gives a Yukawa correction with fixed coupling
`alpha = +1/3`. This is the phenomenological face of the same coefficient
that static frame indifference will eliminate.
