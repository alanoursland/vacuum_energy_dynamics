# candidate_conservation_exchange — Result Note

## Result

The script audits reduced conservation/exchange accounting.

It defines:

```text
D_total = D_A + D_layer + J_exchange
```

and finds:

```text
separate silence:
  D_A=0, D_layer=0, J_exchange=0 -> D_total=0

layer silence only:
  D_layer=0, J_exchange=0 -> D_total=D_A

forced exchange repair:
  J_exchange=-(D_A+D_layer) -> D_total=0
```

## Main Findings

Reduced layer divergence silence is not enough.

Even if `D_layer=0`, the total balance still depends on the A-sector and exchange channel. A forced exchange cancellation is rejected because it is repair, not theorem.

The safe reduced diagnostic is only:

```text
D_A=0
D_layer=0
J_exchange=0
```

and even that is only reduced, not covariant.

## Boundary

This does not prove covariant conservation. It does not prove source safety.

## Steering Consequence

The classifier should report that source safety is sharpened but still unclosed. The candidate should remain audit-only.
