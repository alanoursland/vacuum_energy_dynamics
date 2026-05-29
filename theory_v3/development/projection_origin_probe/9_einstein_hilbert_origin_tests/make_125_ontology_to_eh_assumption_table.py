#!/usr/bin/env python3
"""
make_125_ontology_to_eh_assumption_table.py

Generate and validate an assumption table for the route from vacuum ontology to
Einstein-Hilbert.

Output:
    125_ontology_to_eh_assumption_table.md
"""

from pathlib import Path


here = Path(__file__).parent


rows = [
    {
        "gate": "local interval gives metric",
        "claim": "An even local quadratic interval determines a symmetric bilinear metric.",
        "status": "conditional proven",
        "proofs": ["121_metric_from_local_interval_gate.md"],
        "open": "Show that the vacuum ontology supplies this local interval.",
    },
    {
        "gate": "Levi-Civita connection",
        "claim": "Metric compatibility plus torsion-free condition uniquely selects Levi-Civita.",
        "status": "conditional proven",
        "proofs": ["115_levi_civita_uniqueness_gate.md", "122_torsion_gate_and_extra_field_test.md"],
        "open": "Derive or justify the absence of independent torsion.",
    },
    {
        "gate": "local second-order action",
        "claim": "Second-order macroscopic equations exclude generic higher-derivative densities.",
        "status": "conditional proven",
        "proofs": ["117_curvature_squared_fourth_order_gate.md", "123_locality_second_order_density_gate.md"],
        "open": "Derive locality and second-order character from vacuum energy dynamics.",
    },
    {
        "gate": "diffeomorphism/source consistency",
        "claim": "Gauge invariance requires a divergence-free geometric equation and conserved source coupling.",
        "status": "conditional proven",
        "proofs": ["116_diffeomorphism_noether_divergence_gate.md", "119_nonlinear_bianchi_identity_frw.md"],
        "open": "Derive diffeomorphism invariance from vacuum-as-spacetime ontology.",
    },
    {
        "gate": "boundary bookkeeping",
        "claim": "Second-derivative curvature form requires boundary completion for fixed-boundary variation.",
        "status": "conditional proven",
        "proofs": ["104_ghy_boundary_term_toy_model.md", "124_boundary_variation_fuller_model.md"],
        "open": "Connect this boundary term to the original projection-ladder boundary flux.",
    },
    {
        "gate": "four-dimensional Lovelock selection",
        "claim": "In 4D, local metric-only second-order Lovelock dynamics select EH up to Lambda/topology.",
        "status": "external theorem gate",
        "proofs": ["107_lovelock_uniqueness_gate_summary.md", "109_cosmological_constant_gate.md", "110_gauss_bonnet_topological_4d_gate.md"],
        "open": "Show the vacuum ontology satisfies the Lovelock assumptions.",
    },
    {
        "gate": "weak-field bridge",
        "claim": "EH contains the scalar boundary-flux Newtonian sector with standard source normalization.",
        "status": "proven within bridge",
        "proofs": ["101_eh_field_equation_newtonian_recovery.md", "106_adm_komar_mass_boundary_flux.md", "111_eh_plus_boundary_source_reduced_newtonian.md", "113_projection_ladder_to_boundary_flux_summary.md"],
        "open": "None inside the weak-field bridge; origin assumptions remain upstream.",
    },
]


valid_statuses = {"conditional proven", "external theorem gate", "proven within bridge"}

for row in rows:
    if row["status"] not in valid_statuses:
        raise AssertionError(f"unexpected status for {row['gate']}: {row['status']}")
    for proof in row["proofs"]:
        if not (here / proof).exists():
            raise AssertionError(f"missing referenced proof report: {proof}")


table = ["| Gate | Status | Supporting Reports | Remaining Open Point |", "|---|---|---|---|"]
for row in rows:
    proofs = "<br>".join(f"`{proof}`" for proof in row["proofs"])
    table.append(f"| {row['gate']} | {row['status']} | {proofs} | {row['open']} |")

table_text = "\n".join(table)

md = f"""# Einstein-Hilbert Origin Test 125: Ontology-to-EH Assumption Table

## Purpose

This report separates what has been proved inside the bridge from what still
has to be derived from the vacuum ontology.

The script validates that every referenced support report exists and that each
gate has an explicit status.

## Assumption Table

{table_text}

## Reading

The Einstein-Hilbert side of the bridge is no longer vague. It is a conditional
theorem chain:

```text
metric interval
  + torsion-free metric compatibility
  + locality
  + diffeomorphism/source consistency
  + second-order field equations
  + four spacetime dimensions
  -> Einstein-Hilbert bulk action, up to Lambda/topology.
```

The weak-field bridge has already been checked:

```text
projection ladder
  -> boundary flux
  -> inverse-square scalar field
  -> Newtonian metric sector
  -> EH weak-field source normalization.
```

## Current Gap

The open problem is not whether EH matches the bridge under standard geometric
assumptions. It does.

The open problem is whether the vacuum-energy ontology forces those assumptions
rather than merely being compatible with them.
"""

out = here / "125_ontology_to_eh_assumption_table.md"
out.write_text(md, encoding="utf-8")

print("All table references validated.")
print(f"Wrote {out.resolve()}")
