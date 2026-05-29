# 19. Boundary regularization does not create source gate

For contact order `m >= 2`, a compact-support cutoff profile `s^m` has zero first derivative at the support edge.

- m=2: d(s^m)/ds at boundary = 0
- m=3: d(s^m)/ds at boundary = 0
- m=4: d(s^m)/ds at boundary = 0
- m=5: d(s^m)/ds at boundary = 0

Conclusion: flux-safe regularization can remove boundary leakage. It should not be misread as creating the underlying source; it prevents the cutoff from adding a spurious boundary source.
