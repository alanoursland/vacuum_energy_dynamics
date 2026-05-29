#!/usr/bin/env python3
"""
make_8_zero_time_channel_obstruction.py

Validate that removing the time channel removes the hyperbolic wave symbol and
leaves a spatial elliptic symbol.

Output:
    8_zero_time_channel_obstruction.md
"""

from pathlib import Path
import sympy as sp


x, t, k, omega = sp.symbols("x t k omega", real=True)
u = sp.exp(sp.I * (k * x - omega * t))

wave_expr = -sp.diff(u, t, 2) + sp.diff(u, x, 2)
spatial_expr = sp.diff(u, x, 2)

wave_symbol = sp.simplify(wave_expr / u)
spatial_symbol = sp.simplify(spatial_expr / u)


def require_zero(label, expr):
    result = sp.simplify(expr)
    if result != 0:
        raise AssertionError(f"{label} failed: {result}")


require_zero("wave symbol", wave_symbol - (omega**2 - k**2))
require_zero("spatial symbol", spatial_symbol + k**2)
require_zero("spatial symbol has no omega", sp.diff(spatial_symbol, omega))

md = f"""# Vacuum Dimension Selector 8: Zero Time Channel Obstruction

## Purpose

This proof checks the opposite failure mode from the multiple-time branch. If no
time channel is present, the wave operator loses its hyperbolic dispersion
structure.

## Validated Checks

- plane-wave symbol of `-d_t^2 + d_x^2` is `omega^2 - k^2`: passed
- plane-wave symbol of the spatial-only operator is `-k^2`: passed
- the spatial-only symbol contains no `omega`: passed

## Computation

For:

```text
u = exp(i(k x - omega t))
```

the wave operator gives:

```text
(-d_t^2 + d_x^2)u / u = {wave_symbol}
```

The spatial-only operator gives:

```text
d_x^2 u / u = {spatial_symbol}
```

## Interpretation

Without a clock channel, the lift is static or elliptic rather than a dynamical
wave theory. This is a gate result, not an ontology derivation: a time channel
must be supplied by the parent theory if the lift is to reproduce wave-like
weak-field behavior.
"""

out = Path(__file__).with_name("8_zero_time_channel_obstruction.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Zero-time obstruction symbol check passed.")
print(f"Wrote {out.resolve()}")

