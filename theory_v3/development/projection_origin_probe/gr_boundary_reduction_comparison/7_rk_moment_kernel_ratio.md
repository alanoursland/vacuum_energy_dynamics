
# 7. Base `r_k` moment-kernel ratio

Using the compactified beta moments,

```text
M_j = ∫₀¹ y^j (1-y)y^{-1/2} dy,
```

the moment-kernel coefficient is

```text
r_k = M_k/M_{k-1} = (2k-1)/(2k+3).
```

Therefore

```text
y^k - r_k y^{k-1}
```

has zero moment under the same functional.

Interpretation: the observed ratio is exactly the base compactified
moment-kernel coefficient.
