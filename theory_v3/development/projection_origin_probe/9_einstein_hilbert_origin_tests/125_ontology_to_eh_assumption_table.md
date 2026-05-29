# Einstein-Hilbert Origin Test 125: Ontology-to-EH Assumption Table

## Purpose

This report separates what has been proved inside the bridge from what still
has to be derived from the vacuum ontology.

The script validates that every referenced support report exists and that each
gate has an explicit status.

## Assumption Table

| Gate | Status | Supporting Reports | Remaining Open Point |
|---|---|---|---|
| local interval gives metric | conditional proven | `121_metric_from_local_interval_gate.md` | Show that the vacuum ontology supplies this local interval. |
| Levi-Civita connection | conditional proven | `115_levi_civita_uniqueness_gate.md`<br>`122_torsion_gate_and_extra_field_test.md` | Derive or justify the absence of independent torsion. |
| local second-order action | conditional proven | `117_curvature_squared_fourth_order_gate.md`<br>`123_locality_second_order_density_gate.md` | Derive locality and second-order character from vacuum energy dynamics. |
| diffeomorphism/source consistency | conditional proven | `116_diffeomorphism_noether_divergence_gate.md`<br>`119_nonlinear_bianchi_identity_frw.md` | Derive diffeomorphism invariance from vacuum-as-spacetime ontology. |
| boundary bookkeeping | conditional proven | `104_ghy_boundary_term_toy_model.md`<br>`124_boundary_variation_fuller_model.md` | Connect this boundary term to the original projection-ladder boundary flux. |
| four-dimensional Lovelock selection | external theorem gate | `107_lovelock_uniqueness_gate_summary.md`<br>`109_cosmological_constant_gate.md`<br>`110_gauss_bonnet_topological_4d_gate.md` | Show the vacuum ontology satisfies the Lovelock assumptions. |
| weak-field bridge | proven within bridge | `101_eh_field_equation_newtonian_recovery.md`<br>`106_adm_komar_mass_boundary_flux.md`<br>`111_eh_plus_boundary_source_reduced_newtonian.md`<br>`113_projection_ladder_to_boundary_flux_summary.md` | None inside the weak-field bridge; origin assumptions remain upstream. |

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
