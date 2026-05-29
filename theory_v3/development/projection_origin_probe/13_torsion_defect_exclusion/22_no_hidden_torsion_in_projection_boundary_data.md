# Torsion Defect Exclusion 22: No Hidden Torsion In Projection Boundary Data

## Purpose

This proof checks whether scalar projection boundary data can absorb torsion
boundary data.

It cannot do so silently. An oriented carrier must be supplied explicitly.

## Validated Checks

- scalar projection boundary action is insensitive to torsion components: passed
- torsion boundary coupling requires explicit carriers: passed
- carrier sensitivity is nonzero when carrier is introduced: passed

## Scalar Boundary Data

Let scalar projection boundary data have the form:

```text
B_scalar = p F_scalar.
```

For torsion boundary components:

```text
C12, C13, C23,
```

Sympy verifies:

```text
dB_scalar/dC12 = dB_scalar/dC13 = dB_scalar/dC23 = 0.
```

## Routed Torsion Coupling

To couple scalar projection data to torsion components, one must introduce
explicit carriers:

```text
B_torsion = p(eta12 C12 + eta13 C13 + eta23 C23).
```

Then:

```text
dB_torsion/dC12 = eta12*p
dB_torsion/dC13 = eta13*p
dB_torsion/dC23 = eta23*p.
```

The carrier is visible:

```text
dB_torsion/deta12 = C12*p.
```

## Interpretation

The scalar projection ladder cannot hide torsion boundary data. If torsion is
coupled to projection defects, the orientation carriers are additional fields
or routing data.
