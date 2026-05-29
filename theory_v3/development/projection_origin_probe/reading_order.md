# Projection Origin Probe Reading Order

## Purpose

This folder now contains several proof chains. They are related, but they do
not all serve the same role.

The best reading order is not raw chronological order. Read from the core
projection object outward:

```text
projection ratio
  -> admissibility ladder
  -> archive provenance
  -> source-safety gates
  -> matter source origin gates
  -> radial boundary field bridge
  -> geometric lift
  -> Einstein-Hilbert gates
  -> vacuum-action origin gates
  -> selector-level gates
```

The chain is conditional. It proves a sequence of formal bridges and gates; it
does not claim that the projection hierarchy alone is already a physical field
equation.

## Short Path

For a fast orientation, read these first:

```text
overview.md
conclusion.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
field_search_survivor_audit/7_corrected_provenance_summary.md
field_search_survivor_audit/8_mathematical_context_for_rk.md
field_search_survivor_audit/9_archive_to_math_interpretation.md
source_safety_gate/7_source_safety_gate_status.md
matter_source_origin_gate/6_matter_source_origin_gate_status.md
matter_source_origin_gate/12_positive_source_origin_status.md
matter_source_origin_gate/18_covariant_matter_lift_status.md
matter_source_origin_gate/24_interval_matter_origin_status.md
matter_source_origin_gate/30_operational_interval_universality_status.md
matter_source_origin_gate/36_vacuum_interval_uniqueness_status.md
matter_source_origin_gate/42_interval_to_action_link_status.md
boundary_flux_field_bridge/75_scalar_bridge_final_status.md
geometric_field_lift/97_geometric_lift_final_status.md
einstein_hilbert_origin_tests/126_status_after_assumption_origin_gates.md
vacuum_action_origin/33_vacuum_action_origin_conclusion.md
vacuum_action_origin/39_nonlinear_boundary_interval_action_status.md
vacuum_action_origin/45_eh_ghy_normalization_status.md
vacuum_action_origin/51_projection_tensor_boundary_completion_status.md
vacuum_action_origin/57_remaining_physical_selectors_status.md
vacuum_interval_directional_probe_origin/6_directional_selector_initial_status.md
vacuum_interval_directional_probe_origin/12_directional_selector_tensor_gate_status.md
vacuum_interval_directional_probe_origin/18_metric_origin_gate_status.md
vacuum_interval_directional_probe_origin/24_hessian_origin_status.md
vacuum_interval_directional_probe_origin/25_directional_probe_conclusion.md
torsion_defect_exclusion/proof_chain_plan.md
torsion_defect_exclusion/6_reduced_torsion_gate_status.md
torsion_defect_exclusion/12_torsion_source_ledger_status.md
torsion_defect_exclusion/18_connection_split_status.md
torsion_defect_exclusion/24_action_branch_status.md
torsion_defect_exclusion/29_torsion_defect_exclusion_conclusion.md
vacuum_dimension_selector/proof_chain_plan.md
vacuum_dimension_selector/5_flux_dimension_gate_status.md
vacuum_dimension_selector/10_time_channel_status.md
vacuum_dimension_selector/15_polarization_selector_status.md
vacuum_dimension_selector/20_action_dimension_status.md
vacuum_dimension_selector/25_boundary_dimension_status.md
vacuum_dimension_selector/29_vacuum_dimension_selector_conclusion.md
```

This gives the whole state of the work without reading every proof script.

## Full Conceptual Order

### 1. Orientation

Start with:

```text
overview.md
conclusion.md
```

These establish the original caution: the projection hierarchy is a structured
formal object, but physical interpretation requires external derivation.

### 2. The Original Projection Object

Then read the four root-level proofs:

```text
1_psi_k_ibp_origin.md
2_operator_L_origin_tests.md
3_primitive_power_family_test.md
4_m2_selector_tests.md
```

These show that:

```text
r_k = (2k - 1)/(2k + 3)
```

has a clean primitive / integration-by-parts origin, that the operator `L`
exists, and that `m=2` is selected by matching the survivor ratio rather than
by an independent physical principle.

### 3. Endpoint-Contact / Admissibility Ladder

Next read:

```text
regularity_admissibility_ladder/
```

Use the final report as the anchor:

```text
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

This is where the projection object becomes a general admissibility ladder.
The key result is that the original ratio is the base case of:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

Read this before the field-bridge folders, because it fixes what the projection
hierarchy actually is.

### 4. Archive Provenance

Then read:

```text
field_search_survivor_audit/
```

Use:

```text
field_search_survivor_audit/7_corrected_provenance_summary.md
field_search_survivor_audit/8_mathematical_context_for_rk.md
field_search_survivor_audit/9_archive_to_math_interpretation.md
```

This folder connects the focused proof chain back to the archived search tree.
The important correction is historical:

```text
Group 88 discovered r_k through a moment-ratio identity.
The later primitive identity explains the same ratio compactly.
```

This folder also records that:

```text
w = (1 - x^2)^4
```

was algebraically identified from beta-moment structure, not physically
derived.

### 5. Source-Safety Gates

Then read:

```text
source_safety_gate/
```

Use:

```text
source_safety_gate/7_source_safety_gate_status.md
```

This folder is not another derivation of the projection hierarchy. It proves
the bookkeeping and reduced-flux gates that a source-origin theorem must obey:

```text
ordinary matter enters once;
residual terms do not re-enter;
non-A sectors do not duplicate ordinary source;
scalar tails and far-zone currents must be silent unless explicitly routed;
compact support requires flux-safe boundary contact.
```

This feeds the matter-source-origin gate.

### 6. Matter Source Origin Gate

Then read:

```text
matter_source_origin_gate/
```

Use:

```text
matter_source_origin_gate/6_matter_source_origin_gate_status.md
matter_source_origin_gate/12_positive_source_origin_status.md
matter_source_origin_gate/18_covariant_matter_lift_status.md
matter_source_origin_gate/24_interval_matter_origin_status.md
matter_source_origin_gate/30_operational_interval_universality_status.md
matter_source_origin_gate/36_vacuum_interval_uniqueness_status.md
matter_source_origin_gate/42_interval_to_action_link_status.md
```

This folder starts the positive source-origin gate. The first status report
records the exclusions and routing rules. The second status report records the
positive reduced source origin: the A-sector variational Poisson law, Gauss
mass flux, Newtonian weak-limit normalization, boundary-source equivalence, and
zero-monopole auxiliary-source silence. The third status report records the
standard weak metric matter-coupling lift into the A-sector source law. The
fourth status report records the interval/clock-rate origin gates for ordinary
matter coupling and the exclusion of independent nonmetric clock tails. The
fifth status report records operational interval universality, many-particle
source emergence, weak current conservation, source partitioning, and the
distinction between exterior mass neutrality and local clock neutrality. The
sixth status report records interval uniqueness by polarization, the
clock-only data limitation, the single-interval universal-beta gate, auxiliary
second-interval exclusion, and weak boundary-action compatibility. The seventh
status report records the interval-to-action link: relabeling/tensor behavior,
shared matter/vacuum variation variable, auxiliary interval source ledgers,
locked-channel normalization shifts, and the weak A-sector boundary flux
normalization.

### 7. Boundary Flux Field Bridge

Then read:

```text
boundary_flux_field_bridge/
```

Use:

```text
boundary_flux_field_bridge/75_scalar_bridge_final_status.md
```

This folder proves the scalar bridge:

```text
boundary flux -> 1/r potential -> inverse-square field
```

and clarifies how reduced boundary-source mechanics produce the Newtonian
sector.

### 8. Geometric Field Lift

Then read:

```text
geometric_field_lift/
```

Use:

```text
geometric_field_lift/97_geometric_lift_final_status.md
```

This folder lifts the scalar bridge into linearized geometry. The key result
is that the scalar bridge lands in the Newtonian sector of the linearized
metric rather than in an arbitrary scalar theory.

### 9. Einstein-Hilbert Origin Tests

Then read:

```text
einstein_hilbert_origin_tests/
```

Use:

```text
einstein_hilbert_origin_tests/126_status_after_assumption_origin_gates.md
```

This folder tests why the Einstein-Hilbert structure is the natural geometric
action once locality, metric compatibility, second-order equations, boundary
completion, and standard tensor assumptions are imposed.

### 10. Vacuum Action Origin

Finally read:

```text
vacuum_action_origin/
```

Use:

```text
vacuum_action_origin/33_vacuum_action_origin_conclusion.md
vacuum_action_origin/39_nonlinear_boundary_interval_action_status.md
vacuum_action_origin/45_eh_ghy_normalization_status.md
vacuum_action_origin/51_projection_tensor_boundary_completion_status.md
vacuum_action_origin/57_remaining_physical_selectors_status.md
```

This folder records the strongest conditional action-origin chain so far. The
newer status report continues the folder after the matter-source handoff and
records the weak boundary normalization, induced interval variable ownership,
projection boundary rank limitation, auxiliary boundary promotion gate, and
no-extra-copy boundary normalization rule. The newest status report records the
EH/GHY normalization match, induced-metric boundary component gate,
trace/traceless limitation, conformal trace-sector prefactor, and projection
boundary current role classification. The latest status report answers the
projection-to-GHY completion question: the scalar projection ladder does not
produce full tensor boundary data unless a tensor-valued extension is
independently derived. The final status report in this folder isolates the
remaining physical selectors: directional tensor boundary data, torsion-source
absence, the 3+1 dimensional selector, and Lambda branch selection.

### 11. Directional Interval Selector

Then read:

```text
vacuum_interval_directional_probe_origin/
```

Use:

```text
vacuum_interval_directional_probe_origin/selector_level_work_plan.md
vacuum_interval_directional_probe_origin/6_directional_selector_initial_status.md
vacuum_interval_directional_probe_origin/12_directional_selector_tensor_gate_status.md
vacuum_interval_directional_probe_origin/18_metric_origin_gate_status.md
vacuum_interval_directional_probe_origin/24_hessian_origin_status.md
vacuum_interval_directional_probe_origin/25_directional_probe_conclusion.md
```

This folder starts the selector-level work. The first batch proves that local
directional interval comparisons can recover symmetric tensor data by
polarization, while scalar trace probes cannot recover shear/traceless data.
It also separates null-cone information from interval-scale information and
shows that tangent boundary probes recover induced metric data rather than
normal/bulk data. The second status report closes the algebraic tensor-data
gate: enough local directional probes recover a frame-covariant symmetric
bilinear form, one non-null calibration fixes scale, tangent/normal probes
separate boundary and bulk data, and full tensor source coupling is required
to use shear data. The third status report sharpens the physical origin gate:
metric interval data requires parallelogram/quadratic behavior, one shared
local scale, preserved directional comparisons, and no un-routed nonquadratic
directional channel. The fourth status report gives the conditional origin:
a stationary local second variation supplies a Hessian, whose directional
quadratic form is metric-like; first variation and higher-order response must
be separately routed. The conclusion closes the folder as a conditional
tensor-boundary-data bridge and identifies `torsion_defect_exclusion` as the
next selector folder.

### 12. Quadratic Response Selector

Then read:

```text
quadratic_response_selector/
````

Use:

```text
quadratic_response_selector/proof_chain_plan.md
quadratic_response_selector/6_hessian_vs_exact_quadratic_status.md
quadratic_response_selector/12_finsler_obstruction_status.md
quadratic_response_selector/18_null_cone_stability_status.md
quadratic_response_selector/24_metric_branch_selection_status.md
quadratic_response_selector/29_quadratic_response_selector_conclusion.md
```

This folder tests the central selector exposed by the directional interval
program:

```text
When does a local directional interval response actually define a metric?
```

The folder separates exact quadratic response from mere local Hessian
approximation. It proves that the parallelogram identity is equivalent to
quadratic/bilinear metric reconstruction, that polarization recovers a
symmetric bilinear form only on the exact quadratic branch, and that smooth
stationary response supplies only a second-order Hessian approximation unless
higher-order directional terms are suppressed or routed.

The folder also constructs explicit nonquadratic obstruction witnesses. These
show that quartic/Finsler-like directional response breaks exact polarization,
introduces scale-dependent effective metrics, destabilizes universal null-cone
structure, and prevents a single direction-independent metric tensor from
owning all interval comparison data.

The conclusion is conditional:

```text
pseudo-Riemannian metric geometry is selected only after the local response
satisfies the exact quadratic/parallelogram gate, or after all nonquadratic
directional response is routed as explicit extra structure rather than hidden
inside the metric branch.
```

This folder should be read before the affine/torsion and dimension selectors,
because metric compatibility, Levi-Civita transport, EH/GHY boundary variation,
and spin-2 polarization counting all assume that the directional response has
already collapsed to the quadratic metric branch.



### 13. Torsion Defect Exclusion

Then read:

```text
torsion_defect_exclusion/
```

Use:

```text
torsion_defect_exclusion/proof_chain_plan.md
torsion_defect_exclusion/6_reduced_torsion_gate_status.md
torsion_defect_exclusion/12_torsion_source_ledger_status.md
torsion_defect_exclusion/18_connection_split_status.md
torsion_defect_exclusion/24_action_branch_status.md
torsion_defect_exclusion/29_torsion_defect_exclusion_conclusion.md
```

This folder tests the next selector:

```text
When is the torsion-free Einstein-Hilbert branch justified?
```

It starts from the already-proved reduced gate:

```text
tau = J_total/(24 mu)
```

and makes the key condition explicit:

```text
torsion-free stationarity requires J_total = 0.
```

The folder should either prove torsion-source absence from the vacuum ontology
or route torsion as an explicit additional field branch. The first status
report localizes the reduced torsion gate: `tau = 0` is stationary iff
`J_total = 0`, nonzero torsion source leaves a reduced correction, and the
existing scalar projection and symmetric interval channels cannot hide that
source. The second status report classifies the possible source routes:
spin-like sources require antisymmetric/internal-angular data, rotational
defects require holonomy or closure failure, auxiliary torsion requires an
explicit carrier, and cancellation must be structural rather than unexplained
tuning. The third status report separates metric data from connection data:
metric compatibility preserves interval data but does not remove torsion,
torsion-free metric compatibility selects Levi-Civita, and contorsion carries
the torsion branch when it is not excluded. The fourth status report makes the
action branch explicit: `K=0` and `J_total=0` gives the Levi-Civita/EH branch,
while sourced torsion gives a torsion-extended branch with source corrections
and boundary/current gates. The conclusion closes the folder with a conditional
selector: if spin, defect, and auxiliary torsion sources are absent, positive
torsion stiffness selects `tau=0`; if any source survives, torsion is an
explicit additional field branch. The next selector is `vacuum_dimension_selector`.

### 14. Vacuum Dimension Selector

Then read:

```text
vacuum_dimension_selector/
```

Use:

```text
vacuum_dimension_selector/proof_chain_plan.md
vacuum_dimension_selector/5_flux_dimension_gate_status.md
vacuum_dimension_selector/10_time_channel_status.md
vacuum_dimension_selector/15_polarization_selector_status.md
vacuum_dimension_selector/20_action_dimension_status.md
vacuum_dimension_selector/25_boundary_dimension_status.md
vacuum_dimension_selector/29_vacuum_dimension_selector_conclusion.md
```

This folder tests the next selector:

```text
Why 3 spatial dimensions plus 1 time dimension?
```

The plan starts from existing consistency gates:

```text
inverse-square flux -> n=3;
one clock channel -> D=n+1;
two massless spin-2 polarizations -> D=4;
4D Lovelock gate -> EH is the unique dynamical local metric curvature term.
```

The folder now closes as a conditional selector chain. It proves that the
flux-plus-clock gate, the two-polarization spin-2 gate, the four-dimensional
Lovelock gate, and the three-boundary induced-metric gate all converge on
`D=4`. It also records the dependencies explicitly: time, Lorentzian signature,
massless spin-2 metric lift, diffeomorphism invariance, second-order locality,
and boundary source origin are not derived inside this folder.


### 15. Lambda Branch Selector

Then read:

```text
lambda_branch_selector/
````

Use:

```text
lambda_branch_selector/proof_chain_plan.md
lambda_branch_selector/5_asymptotic_flat_selects_lambda_zero.md
lambda_branch_selector/10_trace_equation_lambda_shift.md
lambda_branch_selector/14_finite_flux_boundary_condition_gate.md
lambda_branch_selector/15_lambda_requires_global_or_auxiliary_route.md
lambda_branch_selector/21_branch_intersection_selector.md
lambda_branch_selector/24_lambda_branch_selector_conclusion.md
```

This folder tests the vacuum-baseline selector left open after the scalar
bridge, metric lift, quadratic response selector, torsion audit, and dimension
selector:

```text
Why the asymptotically flat / zero-Lambda branch, and what changes when Lambda
is nonzero?
```

The folder separates local connection strain from vacuum baseline density. It
checks that Lambda behaves as a volume baseline term, not as quadratic
connection strain; that nonzero Lambda produces a different radial weak-field
asymptotic class; and that finite asymptotically flat Gauss flux selects

```text
Lambda = 0.
```

The folder also records the complementary fact that constant Lambda is allowed
by the metric branch: it is compatible with metric compatibility, Bianchi
structure, trace-shift algebra, and Lovelock/EH action allowance. Thus nonzero
Lambda is not mathematically forbidden by the metric action class; it is a
different global/asymptotic branch.

The conclusion is conditional:

```text
The zero-Lambda branch is selected by asymptotically flat inverse-square
boundary normalization and finite conserved flux. Nonzero Lambda remains an
allowed vacuum-baseline branch, but it changes the asymptotic class and
requires separate physical routing or a relaxation mechanism if it is to be
explained rather than chosen.
```

This folder should be read after the dimension selector and quadratic response
selector. It does not derive the observed cosmological constant, and it does
not prove Lambda must vanish from pure ontology. It isolates the branch
condition and the missing relaxation problem.


### 16 Scalar Ladder Geometric Embedding

Then read:

```text
scalar_ladder_geometric_embedding/
````

Use:

```text
scalar_ladder_geometric_embedding/proof_chain_plan.md
scalar_ladder_geometric_embedding/6_monopole_projection_legendre_gate.md
scalar_ladder_geometric_embedding/12_symmetric_tensor_rank_gap.md
scalar_ladder_geometric_embedding/15_polarization_recovers_metric_components.md
scalar_ladder_geometric_embedding/17_tt_mode_scalar_projection_zero.md
scalar_ladder_geometric_embedding/23_scalar_shadow_status.md
scalar_ladder_geometric_embedding/24_scalar_ladder_geometric_embedding_conclusion.md
```

This folder records the correct geometric placement of the original scalar
admissibility ladder. It does not re-prove the `r_k` ladder. Instead, it shows
that the scalar projection hierarchy is the trace / isotropic / monopole shadow
of the later directional metric branch.

The folder proves that scalar trace data can encode

```text
Tr(H)/m
```

for a symmetric bilinear response `H`, but cannot recover traceless shear,
off-diagonal metric components, higher multipoles, or TT radiative data. It
checks that angular scalar averaging keeps only the `l=0` monopole sector, that
higher Legendre modes have zero net scalar flux, and that a symmetric tensor
on an `m`-dimensional boundary has rank

```text
m(m+1)/2
```

while the scalar trace channel supplies only one component. The per-mode rank
gap is therefore

```text
m(m+1)/2 - 1.
```

The conclusion is conditional:

```text
scalar admissibility -> scalar trace/monopole sector;
directional quadratic probes -> full metric tensor sector.
```

This folder should be read after `quadratic_response_selector` and before
affine/torsion, dimension, or action-closure selectors. It protects the scalar
ladder from overpromotion: the ladder is the first visible projection shadow of
the relational geometry, not the whole geometry by itself.

### 17 Boundary Reduction Origin Gate

Then read:

```text
boundary_reduction_origin_gate/
````

Use:

```text
boundary_reduction_origin_gate/proof_chain_plan.md
boundary_reduction_origin_gate/6_rk_moment_kernel_gate.md
boundary_reduction_origin_gate/7_primitive_boundary_regular_identity.md
boundary_reduction_origin_gate/8_general_contact_ladder_gate.md
boundary_reduction_origin_gate/13_enclosing_surface_invariance_gate.md
boundary_reduction_origin_gate/18_beta_moment_standard_boundary_analysis.md
boundary_reduction_origin_gate/23_boundary_reduction_status.md
boundary_reduction_origin_gate/24_boundary_reduction_origin_gate_conclusion.md
```

This folder clarifies the interpretive status of the boundary throughout the
projection and field-bridge chain.

The main point is:

```text
boundary = reduction / ledger / admissibility interface;
physics = the local, bulk, or relational structure that generates the boundary data.
```

The folder proves that boundary terms arise from ordinary integration by parts,
bulk variation, compactification, Gauss flux, endpoint contact, and finite
moment-kernel admissibility. It places

```text
r_k = (2k - 1)/(2k + 3)
```

inside standard boundary/admissibility analysis. The ratio appears as a
moment-kernel coefficient, a primitive integration-by-parts coefficient, and
the base case of the endpoint-contact ladder

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

The folder also checks that conserved flux is independent of the enclosing
surface when no source crosses the shell, that compactified endpoints can
represent asymptotic infinity, and that quadratic contact is a flux-silence
condition rather than a source-origin law.

The conclusion is interpretive but proof-backed:

```text
r_k is a real boundary-reduction/admissibility object.
It is not an independent physical ontology by itself.
```

This folder should be read after the scalar ladder/geometric embedding folders
and before deeper source, action, or selector claims that use boundary data.
It protects the project from accidentally saying that the underlying physics
is “the boundary” merely because the reduced analysis naturally produces
boundary terms, endpoint ratios, and flux ledgers.

### 18 GR Boundary Reduction Comparison

Then read:

```text
gr_boundary_reduction_comparison/
````

Use:

```text
gr_boundary_reduction_comparison/proof_chain_plan.md
gr_boundary_reduction_comparison/5_finite_flux_asymptotic_selector.md
gr_boundary_reduction_comparison/7_rk_moment_kernel_ratio.md
gr_boundary_reduction_comparison/8_general_contact_ladder_ratio.md
gr_boundary_reduction_comparison/14_gr_boundary_same_universality_condition.md
gr_boundary_reduction_comparison/18_same_boundary_not_no_work_gate.md
gr_boundary_reduction_comparison/21_tensor_sector_not_decided_by_scalar_boundary.md
gr_boundary_reduction_comparison/24_gr_boundary_reduction_comparison_conclusion.md
```

This folder compares the projection-origin scalar boundary/admissibility
ledger with the ordinary weak-field GR/Newtonian scalar reduction.

The folder does not claim that the scalar projection hierarchy derives GR.
Instead, it asks a narrower question:

```text
After the same radial scalar reduction, compactification, field normalization,
and moment pairing, does the weak-field GR boundary ledger land in the same
admissibility/contact class as the projection-origin r_k ladder?
```

The folder checks the standard weak-field scalar chain:

```text
Poisson equation
  -> radial Gauss flux
  -> exterior 1/r finite-flux class
  -> compactified beta-moment admissibility comparison.
```

It then compares that ledger to the projection-origin coefficient

```text
r_k = (2k - 1)/(2k + 3),
```

which is the `R=0` base case of

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

The important interpretive result is:

```text
Matching the GR weak-field scalar boundary ledger would not mean the vacuum
ontology is doing no work. It would mean the ontology is not doing distinctive
work inside the already-reduced scalar boundary algebra. Any distinctive work
must be upstream: selecting the metric/quadratic interval structure,
calibration-coherent transport, EH/GHY variational class, matter coupling, or
the scalar weak-field reduction itself.
```

The folder also records the diagnostic for genuine boundary-condition novelty:
if a fully normalized GR reduction produced a different contact class `R != 0`,
the difference would appear directly in

```text
r_(R,k) - r_(0,k).
```

This folder should be read after `boundary_reduction_origin_gate` and
`scalar_ladder_geometric_embedding`. It stabilizes the status of `r_k` as a
solved boundary-admissibility coefficient and moves the ontology question
upstream to the structure being reduced.

### 19 GR Boundary Reduction Measurement

Then read:

```text
gr_boundary_reduction_measurement/
````

Use:

```text
gr_boundary_reduction_measurement/proof_chain_plan.md
gr_boundary_reduction_measurement/5_compactification_q_contact.md
gr_boundary_reduction_measurement/6_boundary_variable_changes_contact.md
gr_boundary_reduction_measurement/8_test_pairing_weight_shift.md
gr_boundary_reduction_measurement/10_projection_moment_ladder_ratio.md
gr_boundary_reduction_measurement/14_gr_can_be_embedded_as_R0_conditionally.md
gr_boundary_reduction_measurement/15_Rgr_requires_projection_embedding.md
gr_boundary_reduction_measurement/20_measurement_status_conclusion.md
```

This folder completes the scalar GR boundary-comparison scaffold by asking
whether the contact-class integer

```text
R_GR
```

is actually determined by weak-field GR's scalar boundary reduction.

The folder verifies the ordinary physical scalar ledger:

```text
weak-field GR -> Poisson equation -> finite Gauss flux -> 1/r exterior.
```

It also verifies the projection ladder:

```text
C_R[P] = ∫_0^1 P(y)(1-y)^(R+1)y^(-1/2) dy,
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

The observed projection-origin class is

```text
R = 0,
r_(0,k) = (2k - 1)/(2k + 3).
```

The main result is conservative:

```text
Weak-field GR scalar boundary data fixes the physical finite-flux class, but it
does not by itself specify the projection contact-class integer R.
```

The reason is that `R` belongs to the compactified moment/test pairing. It can
shift under boundary-variable choice, field rescaling, or additional endpoint
contact factors in the projection pairing. Thus `R_GR` is measured only after a
specific projection embedding is chosen.

If the GR scalar ledger is embedded using the same compactified moment
functional as the original projection problem, then by that embedding

```text
R_GR = 0.
```

This establishes GR-compatible scalar boundary reduction, not a novel boundary
condition. It also does not prove that the vacuum ontology is idle: any
distinctive ontology work remains upstream, in the selection of the quadratic
metric branch, calibration-coherent transport, EH/GHY variation, matter
coupling, or the scalar weak-field reduction itself.

## Optional Deep-Dive Order

If you want to audit the historical search process rather than the current
proof chain, use this order:

```text
field_equation_candidates/postmortem.md
field_search_survivor_audit/
regularity_admissibility_ladder/
source_safety_gate/
matter_source_origin_gate/
```

The archive should be treated as provenance and elimination history. The
focused proof folders are the current mathematical record.

## Current Frontier

The next missing bridge is not another proof of `r_k`.

The current frontier is now outside the scalar projection ladder and naturally
splits into selector-specific follow-up folders:

```text
vacuum_interval_directional_probe_origin
torsion_defect_exclusion
vacuum_dimension_selector
lambda_relaxation_mechanism
```

Expected target:

```text
derive tensor-valued boundary data from vacuum interval/comparison structure;
derive torsion-source absence or explicit torsion routing;
derive the 3+1 dimension selector rather than only checking consistency;
derive zero-Lambda/asymptotically-flat selection or a nonzero-Lambda relaxation branch.
```

Until one of those selector gates closes, the projection hierarchy remains a
structured admissibility/projection object with strong bridges, not a
standalone field equation, and the EH/action bridge remains conditional.
