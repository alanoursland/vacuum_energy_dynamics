# 22. r_k is not an independent physical selector

The base ratio is

```text
r_(0,k) = (2k-1)/(2k+3).
```

A higher endpoint-contact family gives

```text
r_(1,k) = (2k-1)/(2k+5).
```

For `k=1`, SymPy checks

```text
r_(0,1) = 1/5
r_(1,1) = 1/7
```

Conclusion: the ratio changes with the boundary/contact admissibility class.
Thus `r_k` is evidence of a particular reduced boundary class, not by itself a
complete physical selection principle.
