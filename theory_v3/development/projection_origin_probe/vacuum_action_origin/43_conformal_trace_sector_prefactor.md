# Vacuum Action Origin 43: Conformal Trace-Sector Prefactor

## Purpose

This proof keeps the normalization comparison honest in the conformal trace
sector.

The EH/GHY prefactor has already been matched to the weak A-sector boundary
normalization. The conformal metric variable has its own trace coefficient and
requires an explicit map to the A variable.

## Validated Checks

- D=4 conformal boundary flux has coefficient -6: passed
- linearized conformal flux coefficient is -6: passed
- EH/GHY prefactor gives conformal trace coefficient -3c^2/(8*pi*G): passed
- conformal trace coefficient still needs an explicit A-sector variable map: passed

## Conformal Boundary Flux

For:

```text
g_ab = exp(2s) eta_ab,
```

the conformal boundary flux density is:

```text
-2(D-1) exp((D-2)s) s'.
```

For `D=4`:

```text
-6 exp(2s) s'.
```

The linearized coefficient is:

```text
-6.
```

Multiplying by the reduced EH/GHY prefactor:

```text
K_EH = c^2/(16*pi*G)
```

gives:

```text
-3 c^2/(8*pi*G).
```

## Interpretation

This is not a contradiction with the A-sector coefficient. It says the
conformal trace variable `s` is not identical to the reduced A variable without
a variable map. Normalization comparisons must specify which interval component
is being varied.
