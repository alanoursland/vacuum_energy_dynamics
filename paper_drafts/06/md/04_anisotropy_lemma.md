# 4. Anisotropy Lemma

The higher-derivative response term in `R + a R^2` contains derivatives of the
scalar curvature. In a static radial configuration, these derivatives are not
isotropic between the temporal and radial directions.

Let `D^a_b` denote the derivative part of the `R^2` response. In the flat
static radial limit used by the verification script, the temporal-radial
difference satisfies

```text
D^t_t - D^r_r = -R'' .
```

Thus any nontrivial scalar curvature profile with `R'' != 0` carries an
intrinsic temporal-radial anisotropy.

The same fact appears in the weak-field potentials. In areal gauge, the
linearized departure from `AB = 1` is

```text
AB - 1 = 2(phi + r psi') / c^2 .
```

For the GR exterior `phi = psi = -GM/r`, this combination vanishes. For the
scalaron exterior above, it is nonzero within a range `ell` of the source. The
hair region therefore has `AB != 1`.

The lemma is:

```text
Any nontrivial static scalaron exterior profile violates static frame
indifference.
```

This does not require the scalaron to be a spin-2 ghost. The scalaron is
healthy as a scalar mode for `a > 0`. The problem is not radiative ghost
instability; it is incompatibility with the exact static-frame principle.
