# Boundary Flux Field Bridge 40: Finite-Sphere Monopole Interaction

## Purpose

This report checks whether the point-charge cross-energy result survives the
first finite-radius upgrade.

The tested setup is:

```text
sphere 1 radius R1
source 2 at center distance d, with d > R1
uniform total boundary flux Q1 on sphere 1
monopole flux Q2 at source 2
```

## Validated Checks

- finite sphere average kernel: passed
- average external monopole potential on sphere: passed
- finite sphere monopole cross energy: passed
- finite sphere inverse-square derivative: passed
- no R1 derivative in monopole cross term: passed

## Spherical Mean Identity

For a point outside the sphere, the spherical average of the Green kernel over
the sphere is:

```text
(1/2) integral_-1^1 [dmu / sqrt(d^2+R1^2-2dR1 mu)] = 1/d.
```

This is the spherical mean-value property for harmonic functions, written
explicitly for the monopole kernel.

## Cross Energy

The average potential from `Q2` over sphere 1 is:

```text
<phi_2>_sphere1 = Q2/(4*pi*d).
```

Uniform flux on sphere 1 gives:

```text
E_cross = Q1 <phi_2>_sphere1
        = Q1*Q2/(4*pi*d).
```

Therefore:

```text
-dE_cross/dd = Q1*Q2/(4*pi*d^2).
```

## Interpretation

The leading monopole interaction is not an artifact of ideal point sources.
For uniform boundary flux on a finite sphere, the same `1/d` interaction term is
obtained exactly as long as the other source lies outside the sphere.

What remains open is the induced-multipole problem: fixed-potential or mixed
boundary conditions can polarize the boundary and add finite-radius corrections.
