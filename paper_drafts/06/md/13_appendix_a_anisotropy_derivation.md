# Appendix A. Anisotropy Derivation

The derivative part of the `R^2` response contains terms of the schematic form

```text
D_ab = nabla_a nabla_b R - g_ab Box R
```

up to convention-dependent signs and factors.

In a static radial weak-field limit, time derivatives vanish. The temporal
component receives only the `Box R` contribution, while the radial component
also receives the second radial derivative. In the conventions used by the
verification script,

```text
D^t_t - D^r_r = -R'' .
```

This appendix must be made convention-clean before submission, including all
signs, metric factors, and any terms that vanish only in the linearized
static-radial limit.
