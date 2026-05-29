# 8. General endpoint-contact ladder gate

For the contact-order moment weight

```text
w_R(y) = (1-y)^(R+1) y^(-1/2),
```

the cancellation ratio is

```text
r_(R,k) = B(k+1/2,R+2) / B(k-1/2,R+2)
        = (2*k - 1)/(2*R + 2*k + 3).
```

SymPy verifies the Beta recurrence form

```text
(k-1/2)/(k+R+3/2) = (2*k - 1)/(2*R + 2*k + 3).
```

Conclusion: the original `r_k` is the `R=0` base case of a standard endpoint-contact admissibility ladder.
