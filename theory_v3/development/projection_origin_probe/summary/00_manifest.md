# Projection Origin Probe — LLM Distill Manifest

This packet is a curated compression of the uploaded `projection_origin_probe` markdown corpus. It is not a concatenation and not a line-extraction dump. It keeps the mathematical spine, conclusions, guardrails, and source breadcrumbs needed for another LLM to continue the work without inheriting the full discussion bulk.

## Files in this packet

- `00_manifest.md`: packet map, source map, and use guidance.
- `01_core_math_packet.md`: definitions, identities, operators, transforms, admissibility rows, balanced bases, and determinant/invertibility facts.
- `02_results_conclusions.md`: established results, negative results, interpretation limits, and open targets.
- `03_llm_research_seed.md`: the smallest practical file to hand to another LLM for new math work.
- `04_speculation_quarantine.md`: speculative physical readings, isolated from the formal results.

## Recommended use

For new mathematical work, start with:

```text
03_llm_research_seed.md
```

If the next task requires derivations or reconstruction, also provide:

```text
01_core_math_packet.md
02_results_conclusions.md
```

Only include:

```text
04_speculation_quarantine.md
```

when explicitly exploring interpretation. Do not let speculative language leak into theorem statements.

## Source map

Root files:

```text
overview.md
1_psi_k_ibp_origin.md
2_operator_L_origin_tests.md
3_primitive_power_family_test.md
4_m2_selector_tests.md
conclusion.md
speculation.md
```

Regularity/admissibility ladder:

```text
5_synthesis_operator_energy.md
6_synthesis_source_weight_diagnostics.md
7_synthesis_family_ladder_selectors.md
8_projection_matrix_closed_form.md
9_galerkin_variational_matrix_test.md
10_boundary_domain_classifier.md
11_low_order_matrix_patterns.md
12_orthogonal_polynomial_nonidentification.md
13_energy_minimization_u_transform.md
14_u_green_regular_solution.md
15_regularity_admissibility_conditions.md
16_regular_source_basis.md
17_regularity_ladder_source_classes.md
18_projection_vs_admissibility_rowspace.md
19_balanced_projection_signatures.md
20_balanced_signature_factorization.md
21_projection_determinant_evidence.md
22_psi_adapted_balanced_basis.md
23_y_variable_pairing_structure.md
24_span_complement_tests.md
25_symbolic_determinant_pattern_probe.md
26_psi_missing_direction_closed_form.md
27_first_admissibility_kernel_bridge.md
28_higher_regular_kernel_bridge.md
29_r0_invertibility_theorem.md
30_generalized_admissibility_rows.md
31_primitive_m_regular_ladder_connection.md
32_general_chi_kernel_theorem.md
33_general_cross_gram_invertibility.md
34_ladder_conclusion_report.md
speculative_synthesis.md
```

## Status reconciliation

The root `conclusion.md` pauses the branch as "formal but structured" because the first four notes had not independently selected `m=2`.

The later ladder files refine that status:

```text
m=2 is not selected by compactified measure, same-weight orthogonality,
or family-wide adjoint closure.

But m=2 is selected internally as the R=0 member of the regularity/admissibility ladder,
where R=0 corresponds to boundedness of f=u/a^3.
```

This is an internal mathematical selection, not yet a physical derivation. The external gap remains:

```text
Why should the transformed energy/domain/regularity problem itself be physically fundamental?
```

## Hard guardrail

Do not treat the projection hierarchy as any of these without new input:

```text
field equation
source law
curvature energy
exchange energy
vacuum burden
physical radial measure
black-hole prediction
derived gravity model
```

Current best formal label:

```text
regularity-adapted weighted projection/admissibility hierarchy
```
