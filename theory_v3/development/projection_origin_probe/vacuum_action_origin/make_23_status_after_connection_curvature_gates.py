#!/usr/bin/env python3
"""
make_23_status_after_connection_curvature_gates.py

Generate a status report after proofs 19-22.

Output:
    23_status_after_connection_curvature_gates.md
"""

from pathlib import Path


md = """# Vacuum Action Origin: Status After Proofs 19-22

## What This Batch Adds

Proofs `19` through `22` test the connection and curvature origin gates after
the metric self-reference step.

## Proof 19: Metric Comparison Forces Connection

Proof `19` validates:

```text
delta I
  =
  (partial_c g_ab
   - Gamma^d_ac g_db
   - Gamma^d_bc g_ad)
  v^a v^b dx^c.
```

So preserving the metric interval under local comparison gives:

```text
nabla_c g_ab = 0.
```

With torsion-free comparison, SymPy verifies that the unique connection is
Levi-Civita.

## Proof 20: Connection vs Curvature

Proof `20` validates that a nonlinear coordinate relabeling can create nonzero
connection coefficients even from a flat connection.

It also validates the flat polar plane:

```text
ds^2 = dr^2 + r^2 dtheta^2
```

has nonzero Christoffels but zero Riemann curvature.

So the connection is the comparison rule; curvature is the invariant field
strength.

## Proof 21: Gamma-Gamma Strain Action

Proof `21` validates on:

```text
g = diag(A(x), B(x), C(x))
```

the split:

```text
sqrt(g)R
  =
  sqrt(g)g^ab(
    Gamma^c_ad Gamma^d_bc
    - Gamma^c_ab Gamma^d_cd
  )
  + partial_c V^c.
```

The Gamma-Gamma part is first-derivative connection strain. The second
derivatives live in the boundary divergence.

## Proof 22: Connection Trace as Volume Flux

Proof `22` validates:

```text
Gamma^a_ac = partial_c log sqrt(g).
```

It also verifies the EH boundary vector:

```text
V^c = sqrt(g)(g^ab Gamma^c_ab - g^cb Gamma^a_ab)
```

as a connection/volume flux.

## Current Impact

The action-origin chain now has the following structure:

```text
response reciprocity
  -> metric interval
  -> metric self-reference
  -> local comparison connection
  -> Levi-Civita connection when torsion is absent
  -> curvature as invariant comparison field strength
  -> Gamma-Gamma connection strain plus boundary flux
  -> Einstein-Hilbert density.
```

This is the first point where the vacuum-action folder connects directly back
to the Einstein-Hilbert origin tests without simply importing them.

## Remaining Gap

The remaining question is action selection:

```text
why this connection-strain scalar,
and not another local scalar made from the same metric/connection data?
```

The earlier EH folder answered this conditionally through the Lovelock gate.
The next vacuum-action proofs should now test whether the vacuum-origin gates
themselves imply the Lovelock assumptions:

```text
24. second-order metric equation gate from local comparison energy;
25. relabeling invariance forces scalar curvature as the linear curvature term;
26. why R_ab R^ab and R^2 fail the second-order gate;
27. Lambda as vacuum baseline energy gate;
28. status after action-selection gates.
```
"""

out = Path(__file__).with_name("23_status_after_connection_curvature_gates.md")
out.write_text(md, encoding="utf-8")

print(f"Wrote {out.resolve()}")
