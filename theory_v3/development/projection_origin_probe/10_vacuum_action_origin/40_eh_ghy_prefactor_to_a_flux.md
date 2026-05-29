# Vacuum Action Origin 40: EH/GHY Prefactor To A-Flux

## Purpose

This proof validates the coefficient handoff:

```text
matter-source gate -> weak boundary normalization -> EH/GHY reduced prefactor.
```

## Validated Checks

- K=c^2/(16*pi*G) is equivalent to K=1/(2 alpha_A): passed
- weak boundary balance gives F=M/(2K): passed
- K=c^2/(16*pi*G) gives F_A=(8*pi*G/c^2)M: passed
- the A-sector target fixes the weak boundary prefactor uniquely: passed

## Target Flux

The reduced A-sector source law uses:

```text
alpha_A = 8*pi*G/c^2.
```

The matter-source boundary balance has:

```text
K F - M/2 = 0,
```

so:

```text
F = M/(2K).
```

Matching:

```text
F_A = alpha_A M
```

requires:

```text
K = 1/(2 alpha_A) = c^2/(16*pi*G).
```

## Interpretation

In the reduced static boundary convention used by the A-sector chain, the weak
EH/GHY boundary prefactor must be:

```text
c^2/(16*pi*G).
```

This is the same coefficient supplied by the matter-source-origin handoff.
