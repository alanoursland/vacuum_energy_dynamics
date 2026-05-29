# Matter Source Origin Gate 16: Covariant To Radial Reduction Gate

## Purpose

This proof records the radial reduction used when the weak covariant matter
coupling is compared to the reduced A-sector source law.

## Validated Checks

- radial Laplacian equals (1/r^2)(r^2 f')': passed
- A=1+2Phi/c^2 scales the radial source by 2/c^2: passed
- Delta Phi=4*pi*G*rho gives Delta A=8*pi*G*rho/c^2: passed
- C0+C1/r is the source-free radial exterior: passed

## Radial Laplacian

For a radial field:

```text
Delta f = f'' + 2f'/r
        = (1/r^2) d/dr [r^2 f'].
```

## A-Sector Scaling

With:

```text
A = 1 + 2 Phi/c^2,
```

one has:

```text
Delta A = 2 Delta Phi/c^2.
```

Therefore:

```text
Delta Phi = 4*pi*G rho
```

implies:

```text
Delta A = 8*pi*G rho/c^2.
```

## Exterior

The source-free radial exterior is:

```text
C0 + C1/r.
```

That is the origin of the flux ledger used in the reduced proof chain.
