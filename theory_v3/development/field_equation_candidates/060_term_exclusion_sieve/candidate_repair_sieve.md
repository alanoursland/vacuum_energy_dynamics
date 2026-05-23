# candidate_repair_sieve — Result Note

## Result

The script rejects raw residue insertion and arbitrary counterterm repair.

It checks:

```text
raw R1 insertion residual = H - R1
raw R2 insertion residual = H - R2
counterterm form = H + a*R1 + b*R2
```

The formal repair solve:

```text
a = (-H - R2*b)/R1
```

shows that the counterterm route works only by choosing coefficients to cancel a defect.

## Main Findings

This is a clean rejection.

The residues:

```text
R1
R2
```

remain useful as diagnostic clues from the transition layer, but they cannot be inserted directly as field-equation terms.

The counterterm route is also rejected because:

```text
counterterm-by-construction is not derivation.
```

That matters because the boundary-layer residues are tempting. They look like exactly the missing pieces. But if they are inserted merely to cancel a mismatch, they become repair terms, not field-equation structure.

## Boundary

This does not kill residue-guided candidate construction. It only kills direct residue insertion and arbitrary repair.

## Steering Consequence

The next filter should test derivative locality. If the candidate is to remain layer-local under a field equation, endpoint value locality alone is not enough.
