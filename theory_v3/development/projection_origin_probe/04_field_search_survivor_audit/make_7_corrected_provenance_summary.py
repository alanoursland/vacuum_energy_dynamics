#!/usr/bin/env python3
"""
make_7_corrected_provenance_summary.py

Summarize the corrected provenance after incorporating the detailed archive
answers.

Output:
    7_corrected_provenance_summary.md
"""

from pathlib import Path


here = Path(__file__).resolve().parent
development = Path(__file__).resolve().parents[2]
field_candidates = development / "field_equation_candidates"
projection_probe = development / "projection_origin_probe"

required = {
    "group_88": field_candidates / "088_hierarchy_formula_derivation_summary.md",
    "group_99": field_candidates / "099_hierarchy_source_origin_audit_summary.md",
    "group_100": field_candidates / "100_moment_projection_derivation_attempt_summary.md",
    "group_101": field_candidates / "101_residual_source_reconstruction_attempt_summary.md",
    "audit_2": here / "2_rk_discovery_trail_reconstruction.md",
    "audit_5": here / "5_candidate_tree_to_current_chain_map.md",
    "audit_6": here / "6_survivor_audit_status.md",
    "source_safety": projection_probe / "source_safety_gate" / "7_source_safety_gate_status.md",
}

missing = [label for label, path in required.items() if not path.exists()]
if missing:
    raise AssertionError(f"missing required provenance inputs: {missing}")

audit_2 = required["audit_2"].read_text(encoding="utf-8")
audit_5 = required["audit_5"].read_text(encoding="utf-8")
audit_6 = required["audit_6"].read_text(encoding="utf-8")

for label, text, phrase in [
    ("audit_2", audit_2, "Group 88"),
    ("audit_2", audit_2, "later compact primitive proof"),
    ("audit_5", audit_5, "w=(1-x^2)^4"),
    ("audit_5", audit_5, "m=2 / R=0 is matched"),
    ("audit_6", audit_6, "matter-source origin"),
]:
    if phrase not in text:
        raise AssertionError(f"{label} missing corrected provenance phrase: {phrase}")

input_lines = "\n".join(
    f"- `{label}` -> `{path.relative_to(development)}`"
    for label, path in required.items()
)

md = f"""# Field Search Survivor Audit 7: Corrected Provenance Summary

## Purpose

This report records the improved provenance after comparing the focused proof
chain against the archived search summaries.

## Inputs Checked

{input_lines}

## Corrected Provenance

### r_k

The archive did not first find `r_k` through the primitive identity.

The historical route is Group 88:

```text
I_k(P) = ((2k - 1)/(2k + 3)) I_(k-1)(P).
```

The later primitive identity:

```text
d/dx [x^(2k-1)(1-x^2)^2]
  =
  -(2k+3)(1-x^2) psi_k
```

is the compact explanation of the same ratio.

### Projection Weight

The projection weight:

```text
w = (1 - x^2)^4
```

was algebraically identified from the beta-moment structure in Groups 99/100.
It was not physically derived.

### m=2 / R=0

The observed ratio selects:

```text
m = 2
R = 0
```

by matching the survivor ratio and the later admissibility ladder. This is not
yet an independent physical selector.

### Source Status

Group 101 gives the formal projection source vector:

```text
b_k(S) = 2 integral psi_k S w dx.
```

The physical source remains unidentified. The source-safety gates now prove
necessary bookkeeping and flux-silence conditions, but they do not derive the
matter-source law.

## Current Bottleneck

The next proof target is therefore:

```text
matter_source_origin_gate
```

with the target:

```text
ordinary matter enters the A-sector once;
residual/projection sectors remain source-neutral;
the formal projection source b_k(S), if used, attaches without double counting.
```
"""

out = here / "7_corrected_provenance_summary.md"
out.write_text(md, encoding="utf-8")

print("Corrected provenance summary validated.")
print(f"Wrote {out.resolve()}")
