# Appendix B. Admissibility Details

The base admissibility condition is

```text
C_R[P] = 0.
```

For the two-term row

```text
chi_{R,k}(y) = y^k - r y^(k-1),
```

this condition becomes

```text
C_R[y^k] - r C_R[y^(k-1)] = 0.
```

Therefore the unique coefficient is

```text
r = C_R[y^k]/C_R[y^(k-1)]
  = (2k - 1)/(2k + 2R + 3).
```

In the boundary-reduction interpretation, higher `R` corresponds to imposing
additional endpoint suppression at `y = 1`.  Algebraically, this appears as
an extra factor of `(1-y)^R` in the balanced source family and as a shift in
the beta weight.

The final paper should make the finite admissible space `H_{R,N}` explicit in
one notation system and prove that the row and balanced families are both
bases of it.  The present draft records the intended proof route.

