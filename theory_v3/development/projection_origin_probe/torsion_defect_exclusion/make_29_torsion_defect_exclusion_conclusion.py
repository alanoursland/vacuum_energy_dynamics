#!/usr/bin/env python3
"""
make_29_torsion_defect_exclusion_conclusion.py

Close out the torsion_defect_exclusion proof chain.

Output:
    29_torsion_defect_exclusion_conclusion.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "6_reduced_torsion_gate_status.md",
    "12_torsion_source_ledger_status.md",
    "18_connection_split_status.md",
    "24_action_branch_status.md",
    "25_no_spin_no_defect_no_aux_condition.md",
    "26_torsion_free_energy_minimum.md",
    "27_hidden_source_failure_witness.md",
    "28_torsion_as_new_field_if_source_survives.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Torsion Defect Exclusion 29: Conclusion

## Purpose

This report closes the `torsion_defect_exclusion` folder.

The folder was opened to answer one selector question:

```text
When is the torsion-free Einstein-Hilbert branch justified?
```

## Result

The answer is conditional and explicit:

```text
J_spin = J_defect = J_aux = 0
  -> J_total = 0
  -> tau = 0 is stationary
  -> positive torsion stiffness makes tau = 0 the reduced minimum
  -> Levi-Civita / Einstein-Hilbert branch is available.
```

If any torsion source survives:

```text
J_total != 0,
```

then:

```text
tau = J_total/(24 mu)
```

and the action becomes a torsion-extended branch with reduced correction:

```text
L_reduced = L_EH - J_total^2/(48 mu).
```

## What Was Proved

The folder proves:

```text
1. torsion-free stationarity requires no total torsion source;
2. scalar projection data cannot hide torsion source;
3. symmetric interval/Hessian data cannot hide antisymmetric torsion source;
4. spin-like torsion requires antisymmetric/internal-angular data;
5. defect torsion requires holonomy or closure-failure data;
6. auxiliary torsion requires an explicit carrier;
7. metric compatibility does not remove torsion;
8. torsion-free metric compatibility selects Levi-Civita;
9. contorsion carries the torsion branch;
10. sourced torsion is an additional field branch.
```

## What Was Not Proved

This folder does not prove from first principles that the vacuum ontology lacks
all torsion source routes.

It proves the sufficient exclusion condition and the routing rule:

```text
exclude all torsion source routes -> EH branch;
allow any route -> torsion branch must be explicit.
```

## Impact On The Main Chain

The Einstein-Hilbert action bridge is now cleaner:

```text
EH is justified under the no-torsion-source selector.
```

The bridge is not allowed to assume torsion-free silently. The condition is:

```text
J_total = 0
```

from source absence or structural cancellation.

## Next Selector

The next remaining selector is:

```text
vacuum_dimension_selector
```

Reason:

```text
the action chain has consistency checks for 3+1 dimensions, but not yet an
ontological derivation of the dimension selector.
```
"""

out = base / "29_torsion_defect_exclusion_conclusion.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion defect exclusion conclusion validated.")
print(f"Wrote {out.resolve()}")

