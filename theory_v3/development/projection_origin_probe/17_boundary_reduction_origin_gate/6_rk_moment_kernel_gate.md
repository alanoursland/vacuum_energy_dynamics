# 6. r_k moment-kernel gate

With the boundary/admissibility moment weight

```text
w(y) = (1-y)y^(-1/2),
```

the ratio that cancels the moment of

```text
chi_k(y) = y^k - r_k y^(k-1)
```

is computed from Beta moments:

```text
I[y^k]     = B(k+1/2,2)
I[y^(k-1)] = B(k-1/2,2)
```

SymPy verifies

```text
r_k = I[y^k] / I[y^(k-1)] = (2*k - 1)/(2*k + 3)
I[chi_k] = 0
```

Conclusion: `r_k` is a standard moment-kernel coefficient for a boundary-reduced
admissibility functional.
