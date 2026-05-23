# candidate_exact_pair_scaffold — Result Note

## Result

`candidate_exact_pair_scaffold.py` constructs the ideal exact-pair scaffold:

```text
L_bulk = dQ/dx
L_gauge = -dQ/dx
R_lift = 0
```

## Main Findings

The scaffold shows that exact cancellation is algebraically possible if the bulk and gauge lift residues are opposite oriented derivatives of the same object.

But this is only a compatibility scaffold. The script does not derive:

```text
the object Q;
why L_bulk is +dQ;
why L_gauge is -dQ;
the covariant lift structure that forces the signs.
```

The script correctly rejects writing `+dQ` and `-dQ` by hand as theorem proof.

## Boundary

Exact-pair cancellation is not a derived identity. It remains a theorem target.

## Steering Consequence

Proceed to the remainder obstruction test. The more honest route should allow a leftover `rho` and classify what must happen to it.
