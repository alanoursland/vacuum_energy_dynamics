# 5. Endpoint contact order gate

For `(1-x)^m`, all derivatives of order `< m` vanish at `x=1`, while the `m`th derivative is generally nonzero.

This is the elementary endpoint-contact mechanism behind boundary-safe compact support and admissibility ladders.

- m=1: lower derivatives = [0]; mth derivative = -1
- m=2: lower derivatives = [0, 0]; mth derivative = 2
- m=3: lower derivatives = [0, 0, 0]; mth derivative = -6
- m=4: lower derivatives = [0, 0, 0, 0]; mth derivative = 24
- m=5: lower derivatives = [0, 0, 0, 0, 0]; mth derivative = -120

Conclusion: endpoint contact is ordinary boundary regularity bookkeeping. It is a condition imposed by reduction/variation, not a claim that physics is located at the endpoint.
