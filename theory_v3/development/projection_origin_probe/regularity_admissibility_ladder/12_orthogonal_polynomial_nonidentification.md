# Synthesis Proof 12: Orthogonal-Polynomial Non-Identification

## Purpose

This report checks a guardrail from `speculative_synthesis.md`:

```text
w=a^4 lies near Gegenbauer/Jacobi structure, but psi_k is not directly
identified as the corresponding orthogonal-polynomial family.
```

## Validated Checks

- psi_k differs from monic Gegenbauer C_(2k)^(9/2) for k=1..4: passed
- psi_k differs from shifted Jacobi family in y=x^2 for k=1..4: passed
- same-weight constant orthogonality fails for k=1..5: passed

## Gegenbauer Comparison

The full-interval weight:

```text
(1-x^2)^4
```

corresponds to Gegenbauer parameter:

```text
lambda = 9/2.
```

Comparing monic forms gives nonzero differences:

```text
psi_1 vs C_2^(9/2): -6/55
psi_2 vs C_4^(9/2): -(13*x**2 + 7)/455
psi_3 vs C_6^(9/2): (680*x**4 - 405*x**2 + 9)/2907
psi_4 vs C_8^(9/2): (47481*x**6 - 35530*x**4 + 3740*x**2 - 55)/81719
psi_1(y) vs shifted Jacobi P_1^(4,-1/2): 39/55
psi_2(y) vs shifted Jacobi P_2^(4,-1/2): (533*y - 280)/455
psi_3(y) vs shifted Jacobi P_3^(4,-1/2): (4811*y**2 - 4536*y + 1008)/2907
psi_4(y) vs shifted Jacobi P_4^(4,-1/2): (175389*y**3 - 227392*y**2 + 95744*y - 14080)/81719
```

## Same-Weight Orthogonality Check

If `psi_k` were the direct same-weight degree-k orthogonal row in the
`y=x^2` picture, its constant moment under `a^4` would vanish. It does not:

```text
k=1: integral psi_k a^4 dx = -256/5775
k=2: integral psi_k a^4 dx = -256/35035
k=3: integral psi_k a^4 dx = -256/135135
k=4: integral psi_k a^4 dx = -256/401115
k=5: integral psi_k a^4 dx = -768/3002285
```

Thus the orthogonal-polynomial setting is contextual. It is not a direct
identification of the row functions.
