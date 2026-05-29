# 14. Torsion/Affine Status

## Claim

The torsion-free branch is selected only when torsion/spin/defect sources are
absent or routed away.

## SymPy check

In the reduced gate

```text
tau = J_total/(24 mu),
```

torsion vanishes when `J_total=0` and responds linearly when the source is
nonzero.

## Ledger status

Conditional. Levi-Civita is the minimal affine branch under source absence and
calibration coherence, not a proof that torsion is mathematically impossible.
