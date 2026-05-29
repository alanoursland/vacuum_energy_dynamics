#!/usr/bin/env python3
"""
make_25_directional_probe_conclusion.py

Close out the vacuum_interval_directional_probe_origin proof chain.

Output:
    25_directional_probe_conclusion.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "6_directional_selector_initial_status.md",
    "12_directional_selector_tensor_gate_status.md",
    "18_metric_origin_gate_status.md",
    "24_hessian_origin_status.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Interval Directional Probe Origin 25: Conclusion

## Purpose

This report closes the `vacuum_interval_directional_probe_origin` folder.

The folder was opened to answer one selector question:

```text
Can local interval/comparison data supply the tensor boundary information
missing from the scalar projection ladder?
```

## Result

Yes, conditionally.

The folder proves the algebraic bridge:

```text
directional interval comparisons
  -> quadratic probe Q(v)
  -> symmetric bilinear tensor by polarization
  -> frame-covariant metric-like object
  -> induced boundary metric from tangent probes
  -> full tensor boundary/source coupling can use shear data.
```

It also proves the metricity guardrails:

```text
metric interval data requires quadratic/parallelogram behavior;
one shared local scale is required for conformal calibration;
isotropic averaging collapses directional data back to trace-only data;
nonquadratic response must be routed outside the metric tensor.
```

Finally, it identifies a viable conditional origin:

```text
local stationary second variation
  -> Hessian
  -> quadratic directional interval branch
  -> symmetric metric-like tensor.
```

## What Was Not Proved

This folder does not derive the local vacuum interval functional whose second
variation would be the metric.

It proves what such an origin must look like:

```text
first variation must vanish or be routed as a source/force channel;
higher-order response must be separated from the metric branch;
one local scale field must calibrate all directions;
direction-dependent scale must be treated as tensor/shear data.
```

## Impact On The Main Chain

The scalar projection ladder remains auxiliary. It does not become a tensor
boundary term by itself.

The directional interval selector supplies a conditional route around that
rank obstruction:

```text
scalar ladder cannot supply full GHY boundary data;
directional interval Hessian data can supply induced boundary metric data.
```

This is enough to hand the tensor-boundary-data question back to the action
origin chain as a conditional selector, not enough to close the full physical
origin of the metric.

## Next Folder

The next selector-level folder should be:

```text
torsion_defect_exclusion
```

Reason:

```text
the action-origin chain still depends on the torsion-free EH branch.
```

The torsion folder should test whether torsion is absent, separately sourced,
or must be routed as an additional field.
"""

out = base / "25_directional_probe_conclusion.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Directional probe conclusion validated.")
print(f"Wrote {out.resolve()}")

