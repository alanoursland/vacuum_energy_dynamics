# Current Status

This note records the inherited status of the vacuum-sector work. It should be
updated only when a later technical folder actually changes the status.

## Closed Or Strongly Closed

```text
r_k = (2k - 1)/(2k + 3)
```

is understood as the base scalar boundary/admissibility coefficient.

The scalar ladder is a trace, monopole, Newtonian boundary ledger. It is not
the full tensor theory.

Scalar boundary data cannot reconstruct Weyl curvature, traceless shear,
transverse-traceless radiation, full tensor boundary data, or nonlinear GR
dynamics by itself.

## Conditionally Closed

Exact quadratic directional response reconstructs local metric data.

Shared metric interval dependence of matter action gives the stress-tensor
source route.

Metric compatibility, no independent torsion/nonmetricity source, locality,
diffeomorphism invariance, boundary differentiability, and no extra fields
select the Einstein-Hilbert/GHY branch in the classical GR reconstruction.

The GR branch is therefore conditionally reconstructed at:

```text
epsilon = 0.
```

## Imported Or Not Yet Derived

The vacuum ontology has not yet supplied the field-equation-generating
strain/gradient functional:

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, grad grad X, ...) ).
```

The following are still imported, conditional, or open:

```text
the physical origin of exact quadratic response
the vacuum configuration variable X
the definition of neighboring mismatch
the allowed invariants in K_strain
transport as an Euler-Lagrange consequence
the field equation generated directly by S_vac
the value or relaxation rule for Lambda
any dark-sector excess dynamics
any non-gravitational vacuum-channel coupling
```

## Central Diagnostic

The current residual is:

```text
K_strain = K_EH/GHY + epsilon K_residual.
```

`epsilon` is not a free decorative parameter. It names whatever non-GR residual
survives after the GR-compatible strain branch is extracted.

The next technical phase must determine whether:

```text
epsilon = 0
```

is forced, whether a controlled:

```text
epsilon != 0
```

is permitted, or whether a new strain axiom is required.

## Practical Next Step

The next useful work is not another derivation of GR from the GR action. The
first deliverable is the branch-admissibility framework:

```text
complete the X contract;
complete the neighboring-mismatch contract;
maintain the strain branch admissibility matrix;
maintain the residual gate manifest;
develop the underdetermination witness.
```

Only after that should candidate branch charters be treated as live physics.

## First Vacuum-Sector Result

The local-response-only selector is now classified as:

```text
underdetermined without new axiom
```

The reason is narrow but important: pointwise interval response can reconstruct
metric data when the quadratic gate holds, but it does not specify
between-point comparison, transport, curvature action, boundary terms,
propagating modes, or `epsilon`.

A scalar SymPy prototype existence witness validates the narrow point by
showing that two functionals can share the same pointwise `V_local` Hessian
while differing in Euler-Lagrange equation, derivative order, and boundary
data.

The same witness is now recorded through VacuumForge as:

```text
derivation: local_response_underdetermines_strain_001
claim: local_response_only_selector_underdetermined_001
obligation: strain_branch_selector_required_001
```

## X Contract Inventory

The candidate `X` options are now inventoried through VacuumForge as:

```text
derivation: x_contract_inventory_002
obligation: neighboring_mismatch_contract_required_002
```

Current conclusion:

```text
No currently inventoried non-metric X option is complete enough to open
candidate strain dynamics without additional routing. The metric-data branch is
usable as the GR baseline but remains a metric-only placeholder for the vacuum
ontology unless a selector explains why vacuum configuration reduces to g_ab.
```

This is an inventory result, not a global no-go theorem against non-metric `X`.

## Neighboring-Mismatch Inventory

The candidate `X(p)` to `X(q)` comparison rules are now inventoried through
VacuumForge as:

```text
derivation: neighboring_mismatch_inventory_003
obligation: residual_gate_ledger_required_003
```

Current conclusion:

```text
No currently inventoried non-baseline neighboring-mismatch rule is complete
enough to open candidate strain dynamics without additional routing. The
Levi-Civita metric transport rule is usable as the GR baseline, but remains a
metric-transport placeholder for the vacuum ontology unless a selector explains
why vacuum strain uses that comparison rule.
```

This is an inventory result, not a global no-go theorem against nonmetric,
nonlocal, holonomy, Finsler, or medium mismatch rules.

## Residual Gate Ledger

The residual tests are now recorded through VacuumForge as:

```text
derivation: residual_gate_ledger_004
obligation: candidate_branch_charters_required_004
```

Current conclusion:

```text
No candidate residual is currently licensed as controlled epsilon != 0.
Candidate branches may be chartered only as not-yet-evaluated or
underdetermined until they provide gate evidence.
```

This is a gate-ledger result, not a no-go theorem against residuals.

Classification:

```text
result type: residual gate ledger / governance classification
scope: required tests for K_residual candidates
conclusion: controlled epsilon != 0 is unavailable until gates pass or route
non-conclusion: no residual tested; no residual killed; no epsilon computed
```

## Candidate Branch Charters

The starting candidate branch set is now chartered through VacuumForge as:

```text
derivation: candidate_branch_charters_005
obligation: higher_curvature_scalar_prototype_required_005
```

Current conclusion:

```text
The candidate space is chartered but not live as physics. Only the EH/GHY
baseline is currently admissible at epsilon = 0. The higher-curvature local
residual has failed as a controlled local residual under the current postulate
set. Other residual branches remain not-yet-evaluated or underdetermined until
their first concrete tests supply gate evidence.
```

This is a charter-ledger result, not a result that any residual branch passes.

The charter handoff:

```text
higher_curvature_scalar_prototype_required_005
```

is satisfied by `higher_curvature_scalar_prototype_006`.

## Higher-Curvature Scalar Prototype

The first concrete branch test is now recorded through VacuumForge as:

```text
derivation: higher_curvature_scalar_prototype_006
obligation: higher_curvature_tensor_route_audit_required_006
```

Current conclusion:

```text
A local higher-derivative residual can keep the same pointwise V_local Hessian
while changing the Euler-Lagrange derivative order, boundary data, mode
content, and weak-field pole structure. Therefore the higher-curvature local
residual branch is not licensed as controlled epsilon != 0 by the scalar
prototype.
```

This is a scalar prototype obstruction, not a full tensor/covariant no-go
theorem.

Next target:

```text
separate inert/topological terms, scalaron/f(R)-type routes that are
ghost-safe only after mode routing, and spin-2/Weyl-type ghost routes before
any higher-curvature residual is reused.
```

## Higher-Curvature Tensor-Route Audit

The higher-curvature route audit is now recorded through VacuumForge as:

```text
derivation: higher_curvature_tensor_route_audit_007
obligation: lambda_baseline_folder_required_007
```

Current conclusion:

```text
No higher-curvature route is currently licensed as controlled epsilon != 0.
The inert/topological route is not a bulk residual. The spin-2/Weyl route fails
as a controlled local higher-curvature residual by the ghost pole. The
scalaron/f(R)-type route is the only non-ghost local higher-curvature route,
but under the already adopted closure it remains blocked by P7prime/weak-field
routing unless that appeal is explicitly reopened.
```

This imports prior G20/E3 route context; it is not a new full tensor theorem.

Next target:

```text
open the Lambda baseline folder and keep baseline-selection questions separate
from local higher-curvature strain residuals.
```

## Lambda Baseline Inventory

The Lambda baseline workstream is now recorded through VacuumForge as:

```text
derivation: lambda_baseline_inventory_008
obligation: lambda_baseline_selector_required_008
```

Current conclusion:

```text
Lambda = 0 is the asymptotically flat scalar boundary-flux sector when no
nonzero background curvature is supplied. Nonzero Lambda is allowed by the
EH/Lovelock branch but remains unvalued. A derived nonzero vacuum floor
requires a selector: variational, admissibility, topology, measure, or
relaxation.
```

This is a baseline inventory, not a derivation of the observed cosmological
constant and not a dark-sector excess license.

Next target:

```text
state candidate Lambda baseline selectors and kill conditions before any
nonzero Lambda mechanism is used.
```

## Lambda Baseline Selector Charter

The candidate Lambda baseline selectors are now chartered through VacuumForge
as:

```text
derivation: lambda_baseline_selector_charter_009
obligation: lambda_selector_sieve_required_009
```

Current conclusion:

```text
The Lambda selector space is chartered, but no selector is adopted. Candidate
rows now state boundary data, sign/value mechanism, source ledger,
local-equation quarantine, falsifier, and first concrete test.
```

This is a selector charter, not a derivation of nonzero `Lambda`, not an
observed-value insertion, and not a dark-sector excess license.

Next target:

```text
apply the selector sieve before opening any specific nonzero Lambda mechanism.
```

## Lambda Selector Sieve

The first Lambda selector sieve is now recorded through VacuumForge as:

```text
derivation: lambda_selector_sieve_010
obligation: lambda_variational_minimum_probe_required_010
```

Current conclusion:

```text
No chartered Lambda selector currently passes the first evidence sieve. Each
row still lacks an instantiated selector object plus the evidence needed for
boundary instantiation, sign/value derivation, source conservation,
local-equation quarantine, and an operational falsifier.
```

This is not a global no-go theorem against nonzero `Lambda`; it is a
mechanism-readiness check.

Next target:

```text
test the variational-minimum selector first, because it is the lowest
additional-structure route to an explicit selector object.
```

## Lambda Variational-Minimum Probe

The variational-minimum selector is now probed through VacuumForge as:

```text
derivation: lambda_variational_minimum_probe_011
obligation: lambda_boundary_admissibility_probe_required_011
```

Current conclusion:

```text
A bare selector functional F(Lambda) does not derive a nonzero baseline.
It leaves Lambda free, selects Lambda = 0 for the no-scale convex case, has no
interior stationary point for a lone linear bias on an unconstrained continuous
domain, or produces a nonzero value only by importing a bias, target, boundary
class, or new scale.
```

This is not a no-go theorem against nonzero `Lambda`; it blocks only the empty
variational-minimum route. It is also not a variation of the full EH action
with respect to `Lambda`.

Next target:

```text
test whether boundary/admissibility data can supply the missing nonzero scale
without observed-value insertion or local-equation modification.
```

## Lambda Boundary/Admissibility Probe

The boundary/admissibility selector is now probed through VacuumForge as:

```text
derivation: lambda_boundary_admissibility_probe_012
obligation: lambda_topology_global_constraint_probe_required_012
```

Current conclusion:

```text
Boundary/admissibility data can select allowed Lambda families and can convert
a supplied boundary length, radius, volume, or asymptotic class into a Lambda
relation. It does not derive a nonzero value unless the boundary scale or
volume is itself selected by the vacuum ontology.
```

This is not a derivation of nonzero `Lambda`; it identifies the next missing
object as a topology, volume, measure, or admissibility-scale selector.

Next target:

```text
test whether topology/global constraints can supply a dimensionful Lambda
value or only constrain it after a scale is supplied.
```

## Lambda Topology/Global Constraint Probe

The topology/global constraint selector is now probed through VacuumForge as:

```text
derivation: lambda_topology_global_constraint_probe_013
obligation: lambda_measure_identity_probe_required_013
```

Current conclusion:

```text
Topology and global constraints can restrict allowed sectors and can relate
Lambda to supplied area, volume, length, or measure data. Topology alone is
dimensionless and cannot derive a dimensionful Lambda value.
```

This does not kill topology/global constraints; it says they need a scale
selector before they can set `Lambda`.

Next target:

```text
test whether a measure identity can supply a conserved density or curvature
scale without observed-value insertion.
```

## Lambda Measure Identity Probe

The measure-identity selector is now probed through VacuumForge as:

```text
derivation: lambda_measure_identity_probe_014
obligation: lambda_relaxation_fixed_point_probe_required_014
```

Current conclusion:

```text
A measure identity can be a Lambda selector only if it supplies a derived,
covariantly conserved, constant floor before observation is used. Dimensional
fits import a scale. Dustlike, defectlike, clustered, or transportable
densities belong to dark-sector or defect ledgers, not the constant Lambda
baseline.
```

This records a candidate route only for a derived conserved floor; it does not
derive that floor.

Next target:

```text
test whether relaxation/fixed-point dynamics can select a nonzero floor without
target insertion.
```

## Lambda Relaxation/Fixed-Point Probe

The relaxation/fixed-point selector is now probed through VacuumForge as:

```text
derivation: lambda_relaxation_fixed_point_probe_015
obligation: lambda_frustration_floor_microphysics_probe_required_015
```

Current conclusion:

```text
Scale-free relaxation selects Lambda = 0. Nonzero fixed points require a target,
domain length, kernel scale, or coefficient ratio, and become derived only if
that scale or ratio is itself derived.
```

This does not derive nonzero `Lambda`; it identifies the next missing object as
microphysical floor content or another derived-scale route.

Next target:

```text
test whether frustration-floor microphysics can derive the absolute constant
offset, w = -1 ledger, and non-clustering status.
```

## Lambda Frustration-Floor Microphysics Probe

The frustration-floor microphysics selector is now probed through VacuumForge
as:

```text
derivation: lambda_frustration_floor_microphysics_probe_016
obligation: dark_excess_source_ledger_required_016
```

Current conclusion:

```text
Microphysical potential shape can supply minima, excitation scales, and a
constant-floor ledger, but it does not derive a nonzero Lambda baseline unless
it derives the absolute constant offset before observation is used. Excitations
around the floor are transportable excess content, not Lambda.
```

This closes the first Lambda selector sweep without deriving nonzero `Lambda`.

Next target:

```text
open the dark-sector excess source ledger and separate constant floor,
transportable excess, conservation, clustering, and source bookkeeping.
```

## Dark Excess Source Ledger

The dark-sector excess ledger is now opened through VacuumForge as:

```text
derivation: dark_excess_source_ledger_017
obligation: dark_excess_clustering_conservation_required_017
```

Current conclusion:

```text
The constant w = -1 floor remains in the Lambda baseline ledger. A dustlike
w = 0 excess is the only first-pass CDM-like candidate, but it still needs
clustering, conservation, production, abundance, and source-bookkeeping gates.
Radiationlike and defectlike rows are not CDM-like without additional dynamics.
```

This is a source ledger, not a dark-matter derivation.

Next target:

```text
test whether dustlike excess can cluster and conserve without pressure support,
untracked exchange, or source double-counting.
```

## Dark Excess Clustering/Conservation Probe

The first clustering/conservation gate is now recorded through VacuumForge as:

```text
derivation: dark_excess_clustering_conservation_probe_018
obligation: dark_excess_abundance_production_required_018
```

Current conclusion:

```text
A separately conserved, pressureless w = 0 excess has the minimum
clustering-readiness face, but it is still only a candidate. Pressure-supported
or exchanging rows require their own routing. Ordinary matter insertion is
rejected as source double-counting.
```

This is not a dark-matter derivation.

Next target:

```text
derive a production or formation mechanism and abundance route before treating
dustlike excess as dark-sector physics.
```

## Dark Excess Abundance/Production Probe

The abundance/production gate is now recorded through VacuumForge as:

```text
derivation: dark_excess_abundance_production_probe_019
obligation: non_grav_channel_quarantine_required_019
```

Current conclusion:

```text
No dark-sector abundance route is currently licensed. Back-solving from the
observed density is rejected. Yield, freezeout-like, and formation-fraction
routes remain possible only after their production microphysics, interaction
scale, or formation fraction is derived before observation is used.
```

This leaves dustlike excess possible but unlicensed.

Next target:

```text
open non-gravitational vacuum-channel quarantine contracts.
```

## Non-Gravitational Channel Quarantine

The non-gravitational vacuum-channel workstream is now opened through
VacuumForge as:

```text
derivation: non_grav_channel_quarantine_020
obligation: casimir_ufft_channel_contract_required_020
```

Current conclusion:

```text
No non-gravitational vacuum channel is live yet. Casimir/UFFT,
substance-frame, and material-boundary routes are carried forward only as
quarantined candidates. They need a channel variable, coupling object, source
ledger, observable, falsifier, and explicit metric quarantine before they can
be used.
```

Direct gravitational-Yukawa reinterpretation and unbooked stress-tensor
insertion are rejected as wrong-ledger moves.

This is a channel-quarantine ledger, not a prediction of a Casimir/UFFT or
preferred-frame signal.

Next target:

```text
write the Casimir/UFFT channel contract.
```

## Casimir/UFFT Channel Contract

The first concrete non-gravitational channel contract is now recorded through
VacuumForge as:

```text
derivation: casimir_ufft_channel_contract_021
obligation: casimir_ufft_operator_instantiation_required_021
```

Current conclusion:

```text
The Casimir/UFFT channel now has a contract shape and a symbolic quarantine
from a gravitational-Yukawa misroute. It is not prediction-ready because the
channel operator and source/exchange ledger are still missing.
```

The contract uses a boundary/material variable and scaling placeholder:

```text
B = (L, chi_m, boundary class, frequency window)
Delta O_ch = eta_ch * chi_m / L^4
```

This is a schema only. It does not derive the operator, coefficient, target
window, or source bookkeeping.

Next target:

```text
instantiate or reject the Casimir/UFFT channel operator.
```

## Casimir/UFFT Operator Instantiation Audit

The Casimir/UFFT operator-instantiation audit is now recorded through
VacuumForge as:

```text
derivation: casimir_ufft_operator_instantiation_audit_022
obligation: substance_frame_coupling_contract_required_022
```

Current conclusion:

```text
No Casimir/UFFT operator route is live. Standard Casimir scaling belongs to
ordinary QFT/material boundary physics unless a new ontology coupling is
derived. Fitting the channel coefficient to that scaling is a backsolve, not a
derivation. A free boundary-channel schema remains possible but unlicensed.
```

This is not a global no-go theorem against Casimir/UFFT channels. It rejects
the currently audited routes as new vacuum-sector operators and moves the
non-gravitational channel program to the substance-frame coupling contract.

Next target:

```text
write the substance-frame coupling contract.
```

## Substance-Frame Coupling Contract

The substance-frame coupling contract is now recorded through VacuumForge as:

```text
derivation: substance_frame_coupling_contract_023
obligation: substance_frame_bounds_sieve_required_023
```

Current conclusion:

```text
No substance-frame coupling route is live. The frame may remain an ontological
object without predicting a preferred-frame signal. Observable routes require a
coupling operator, source/exchange ledger, metric quarantine, and preferred
frame or calibration bounds.
```

The silent-frame rule is:

```text
beta_frame = 0
Delta O_frame = 0
```

A coupled calibration-anisotropy schema is only a placeholder:

```text
Delta O_frame = beta_frame * cos(theta)^2
```

Metric preferred-frame insertion is rejected as a wrong-ledger reroute; it
belongs to residual gates if reopened.

Next target:

```text
apply the first substance-frame bounds sieve.
```

## Substance-Frame Bounds Sieve

The first substance-frame bounds sieve is now recorded through VacuumForge as:

```text
derivation: substance_frame_bounds_sieve_024
obligation: interior_cap_admissibility_contract_required_024
```

Current conclusion:

```text
No observable substance-frame channel is live. The silent frame remains
allowed but predicts no preferred-frame signal. Coupled routes require a
derived coupling, a source/exchange ledger, metric quarantine, and explicit
preferred-frame/calibration bounds before use.
```

The symbolic compatibility condition is:

```text
Delta O_frame = beta_frame * A
beta_required = delta_target / A
delta_target / A <= beta_bound
```

Observed-signal backsolves and unbounded preferred-frame claims are rejected.

Next target:

```text
open the strong-field/interior admissibility contract.
```

## Interior-Cap Admissibility Contract

The strong-field/interior admissibility workstream is now recorded through
VacuumForge as:

```text
derivation: interior_cap_admissibility_contract_025
obligation: exterior_matching_lemma_required_025
```

Current conclusion:

```text
No interior-cap route is live. Exterior-preserving interior modification is a
candidate contract only. A cap or finite-strain rule needs exterior matching,
junction/source bookkeeping, and a derived admissibility scale before it can be
used.
```

The symbolic cap placeholder is:

```text
C = 2GM / (c^2 R_cap)
K_int = 1 / (1 - C)
R_cap = 2GM kappa_max / (c^2 (kappa_max - 1))
```

This imports `kappa_max` unless the vacuum ontology derives it. Imported
cutoff radii and untracked exterior deviations are rejected.

Next target:

```text
prove the exterior matching lemma.
```

## Exterior Matching Lemma

The exterior matching lemma is now recorded through VacuumForge as:

```text
derivation: exterior_matching_lemma_026
obligation: finite_strain_admissibility_probe_required_026
```

Current conclusion:

```text
The fixed-charge exterior route preserves the exterior proxy at lemma level.
This licenses only the exterior-preservation contract, not an interior cap.
Surface charge shifts need source and junction bookkeeping. Lambda shifts and
exterior residual leaks are wrong-ledger moves here.
```

The exterior proxy used by the lemma is:

```text
f_ext(r) = 1 - 2GM_ext/(c^2 r) - Lambda_ext r^2/3
d f_ext / d R_cap = 0
```

Changing exterior mass or Lambda changes the exterior proxy and must be routed
through source/junction bookkeeping or the Lambda selector ledger.

Next target:

```text
probe the finite-strain admissibility scale.
```

## Finite-Strain Admissibility Probe

The finite-strain admissibility probe is now recorded through VacuumForge as:

```text
derivation: finite_strain_admissibility_probe_027
obligation: global_boundary_topology_selector_rules_required_027
```

Current conclusion:

```text
No finite-strain interior cap is licensed. The exterior matching lemma protects
the exterior only. It does not derive the interior admissibility bound,
cap scale, or nonsingularity rule.
```

The symbolic probe is:

```text
C = 2GM / (c^2 R_cap)
K_int = 1 / (1 - C)
R_cap = 2GM kappa_max / (c^2 (kappa_max - 1))
```

The cap scale depends on `kappa_max`. Unless the ontology derives that bound,
the cap scale is imported. Observed compactness backsolves are rejected.

Next target:

```text
consolidate global, boundary, topology, and admissibility selector rules.
```

## Global/Boundary/Topology Selector Rules

The cross-cutting selector rules are now recorded through VacuumForge as:

```text
derivation: global_boundary_topology_selector_rules_028
obligation: vacuum_sector_program_checkpoint_required_028
```

Current conclusion:

```text
Global, boundary, topology, and admissibility selectors can restrict sectors
or admissible classes, but they do not set dimensionful values unless the
missing scale is also derived. Observed-value backsolves are rejected.
```

The representative symbolic checks are:

```text
R = 4*pi*chi / A
Lambda^2 = 12*pi^2*chi / V
```

Topology supplies dimensionless sector information. Dimensionful values still
need area, volume, measure, length, or an admissibility scale.

Next target:

```text
checkpoint the vacuum-sector program before opening new branches.
```

## Vacuum-Sector Program Checkpoint

The first program checkpoint is now recorded through VacuumForge as:

```text
derivation: vacuum_sector_program_checkpoint_029
obligation: strain_branch_selector_decision_table_required_029
```

Current conclusion:

```text
No nonbaseline vacuum-sector mechanism is currently licensed as new physics.
The only licensed gravitational branch remains the conditionally reconstructed
EH/GHY baseline at epsilon = 0.
```

The checkpoint classifies the remaining side ledgers as routed obligations:

```text
Lambda: allowed but unvalued without a derived scale or floor
dark excess: candidate only, missing production and abundance
non-gravitational channels: quarantined, missing operators and source ledgers
substance frame: silent ontology allowed, observable coupling unlicensed
interior cap: exterior-preserving contract only, missing finite-strain bound
global/boundary/topology: sector selectors only without derived scale
```

Next target:

```text
return to the central strain-branch selector question.
```

## Strain-Branch Selector Decision Table

The selector decision table is now recorded through VacuumForge as:

```text
derivation: strain_branch_selector_decision_table_030
obligation: minimal_strain_axiom_contract_required_030
```

Current conclusion:

```text
The program has two disciplined choices: treat accumulated gates as the
operational selector and stay at epsilon = 0, or adopt an explicit new strain
axiom before any nonbaseline mechanism is used.
```

Side ledgers cannot select `K_strain` retroactively. Lambda, dark excess,
non-gravitational channels, substance-frame observables, interior caps, and
topology/global constraints may constrain later work only after a strain
selector exists.

Next target:

```text
write the minimal strain axiom contract.
```

## Minimal Strain Axiom Contract

The minimal axiom contract is now recorded through VacuumForge as:

```text
derivation: minimal_strain_axiom_contract_031
obligation: strain_axiom_candidate_sieve_required_031
```

Current conclusion:

```text
No new strain axiom is adopted. The contract states what a future axiom must
provide before it can license nonbaseline vacuum-sector physics.
```

The only currently complete route remains:

```text
no new axiom, retain EH/GHY baseline at epsilon = 0.
```

Mechanism-fit axioms chosen to rescue Lambda, dark excess, channels, or
interior targets are rejected.

Next target:

```text
apply the candidate sieve to possible strain axiom routes.
```

## Strain Axiom Candidate Sieve

The strain axiom candidate sieve is now recorded through VacuumForge as:

```text
derivation: strain_axiom_candidate_sieve_032
obligation: strain_axiom_adoption_decision_required_032
```

Current conclusion:

```text
No currently named nonbaseline strain axiom satisfies the minimal contract.
The only passing route is the baseline/null route: retain EH/GHY at
epsilon = 0. This is not a new strain axiom.
```

Open nonbaseline routes remain incomplete. Metric relabeling and
mechanism-fit axioms are rejected.

Next target:

```text
decide whether to adopt a fully specified new strain axiom or keep nonbaseline
mechanisms quarantined.
```

## Unimodular Lovelock Break (verification of lovelock_breaks.md)

The lovelock_breaks.md structural argument is now recorded through
VacuumForge as:

```text
derivation: unimodular_lovelock_break_033
obligation satisfied: lovelock_break_verification_033
obligation opened:    unimodular_covariant_constraint_lift_033
```

Current conclusion:

```text
All five forge obligations of lovelock_breaks.md are verified: the kappa /
volume-density identity; the H3 violation nabla^a(R_ab - (1/4) g_ab R) =
(1/4) nabla_b R on two independent families; Lambda as an integration
constant (FRW trace-free + conservation, with algebraic reconstruction of
G_ab + Lambda g_ab = k T_ab); vacuum-energy sequestering; and the F1 leak /
SdS exactness scope statement.
```

Consequences for the lanes: the Lambda baseline status changes from
"allowed but unvalued (selector missing)" to "integration constant fixed by
a global datum; bulk vacuum energy sequestered" — the 008-016 sweep
negatives are now theorems of the unimodular reading rather than empirical
findings. For the strain-axiom decision (032): the candidate constraint
axiom was already in the postulate set; P3 read through the kinematic
identity is a fixed-measure commitment. No nonbaseline physics is licensed;
Lambda's value is not derived.

Next target:

```text
unimodular_covariant_constraint_lift_033: state and verify the kappa = 0
constraint covariantly, including its interaction with the F1 leak.
```

## Covariant Form of the Unimodular Constraint

Recorded through VacuumForge as:

```text
derivation: unimodular_covariant_constraint_034
obligation satisfied: unimodular_covariant_constraint_lift_033/034
obligation opened:    lambda_global_datum_derivation_required_034
```

Current conclusion:

```text
kappa is a scalar given the fiducial volume form (distorted-chart witness);
the unimodular multiplier is forced constant on shell (metric compatibility
+ Bianchi + conservation, two families) and IS Lambda; and the constraint's
controlled violation is the exact sourced equation
kappa'(r) = -(rB/2N)(T^t_t - T^r_r), whose comoving-dust content re-derives
the F1 leak coefficient AB - 1 = (3/2) Omega_m (H0 r/c)^2 with no free
input. The Lambda lane's sole open item is the global datum.
```

## Sequestering Constraint on the Frustration Floor

Recorded through VacuumForge as:

```text
derivation: floor_sequestering_constraint_035
branch decision: kill_floor_as_local_lambda_density_035
obligation opened: floor_global_datum_reposing_035
```

Current conclusion:

```text
A constant frustration-floor density is gravitationally invisible (the
trace-free dynamics are blind to it; the integration constant compensates
exactly), and an isolated time-varying floor violates conservation. The
floor-as-local-gravitating-w=-1-density identification in
dark_energy_accounting.md is CLOSED. Surviving routes: (a) the floor fixes
the global datum (Lambda lane, re-posed microphysics target); (b) floor
variations with an explicit exchange ledger are dark-excess physics
(017-019 gates). The frustration ontology itself is neither licensed nor
excluded.
```

Next target:

```text
floor_global_datum_reposing_035 / lambda_global_datum_derivation_required_034:
derive the global datum (boundary condition / total four-volume conjugate)
from floor microphysics. This is the re-posed route to VED's first non-GR
number.
```

## The Global Datum and Frustration Relief

Recorded through VacuumForge as:

```text
derivation: global_datum_frustration_relief_036
obligation satisfied: lambda_global_datum_attacked_036 (sharpens 034/035 targets)
obligation opened:    frustration_relief_suppression_required_036
```

Current conclusion:

```text
The global datum is the intrinsic curvature of the vacuum's ground
configuration: 4 Lambda = R + kT on any slice (trace identity; SdS and de
Sitter witnesses), and in a floor-only epoch the floor's density cancels
exactly, leaving Lambda = R_ground / 4. Geometry, not energy.

Under the packing reading of P4/P5, geometric frustration relief selects
the SIGN: the flat dihedral deficit 2pi - 5 arccos(1/3) > 0 (exact witness
49 > 45) closes exactly on S^3 (the 600-cell), and worsens under negative
curvature, so a frustration-relieving ground configuration is spherical:
Lambda > 0. Matches observation; conditional on the packing reading;
stated as such.

The magnitude is gated: full relief at packing scale a gives
Lambda_naive = 3/(phi a)^2, which for a = l_P overshoots the observed
value by ~10^122. The lane's single decisive obligation is now a DERIVED
near-complete-relief suppression (defect dilution, frustration sharing,
relaxation depth, or an emergent Hubble-scale curvature radius). No
backsolve permitted. Kill condition: residual curvature pinned at the
packing scale kills the value route, leaving only the sign prediction.
```

Lambda lane state after 036:

```text
status:    integration constant (033/034)          -- settled
meaning:   ground-configuration curvature (036.B)  -- settled
sign:      positive, from frustration relief (036.C) -- conditional prediction
magnitude: open (036.D)                             -- the decisive obligation
```

## Exact Relief Geometry (the partial-relief kill)

Recorded through VacuumForge as:

```text
derivation: relief_exact_geometry_037
branch decision: kill_partial_relief_lambda_value_037
obligation resolved: frustration_relief_suppression_required_036
                     (RESOLVED BY NONEXISTENCE)
```

Current conclusion:

```text
The dihedral angle of a regular tetrahedron of edge arc s = a/L in S^3 is
exactly cos delta(s) = cos s/(1 + 2 cos s): arccos(1/3) at s = 0, exactly
2 pi/5 at the 600-cell arc s = pi/5. Spherical curvature relieves the
five-around-an-edge deficit monotonically (d cos delta/ds =
-sin s/(1+2 cos s)^2); hyperbolic strictly aggravates it. The 036 sign
statement is now an exact theorem.

But relief is quadratic-flat at small curvature:
Delta(s) = Delta_0 - (5 sqrt(2)/24) s^2 + O(s^4). At the curvature the
observed Lambda requires (s ~ 1e-61 for Planck packing) the relieved
fraction is ~1e-122 -- essentially none -- while near-complete relief
demands packing-scale curvature (Lambda ~1e122 too large). No
intermediate regime exists: the suppression 036 asked for does not exist
inside the relief geometry. The partial-relief route to Lambda's value is
DEAD.

Surviving branch (coherent): flat-frustrated ground state,
Lambda_ground = 0, floor retained and sequestered (035) -- exactly what
the trace-free dynamics require. The observed Lambda remains the global
datum, decoupled from the floor. The frustration ontology keeps the exact
conditional sign statement and the sequestered-floor picture; it loses
the value route.
```

Lambda lane after 037:

```text
status:    integration constant (033/034)        -- settled
meaning:   ground-configuration curvature (036)  -- settled
sign:      exact conditional theorem (037): any relief curvature is
           spherical; the coherent branch is flat (Lambda_ground = 0)
magnitude: the global datum, decoupled from the floor; no vacuum-sector
           mechanism currently values it
```

Reported as a result, not a failure: the 036 mechanism ran the gauntlet
and died in one derivation.

## The Substance-Ledger Identity

Recorded through VacuumForge as:

```text
derivation: substance_ledger_identity_038
obligation satisfied: substance_ledger_identity_recorded_038
obligation opened:    packing_stiffness_microphysics_038
```

Current conclusion:

```text
The theory-owner identification "the frustration floor IS the P1/P3
substance energy" is captured at forge grade:

- action-level sequestering: -rho_v sqrt(-g) splits exactly into an
  inert fiducial constant plus a coupling -rho_v sqrt(-g_bar)(e^kappa - 1)
  that is identically zero in the P7'-exact sector and O(kappa) ~ 1e-31
  at the F1 leak. "Substance energy does not gravitate" is a theorem of
  P3's own unimodular content: the postulate that defines the substance
  energy is the postulate that hides it.

- conversion-factor target: rho_v = c_e kappa_w Delta_0^2/(2 a^3), with
  Delta_0 = 2 pi - 5 arccos(1/3) exact. P1's "analog of c^2" question
  becomes a formula target; kappa_w, a, c_e are the open microphysics.

- sector signature bottom-up: on exact tetrahedron coordinates, every
  dihedral is exactly dilation-invariant and shifts at first order under
  volume-preserving shear. Any angle-based floor energy is therefore
  flat in the volume/trace (kappa) mode and stiff in the shear (s) mode:
  the trace-constrained / shear-energetic architecture of the closed
  theory emerges from the packing microphysics, and the volume mode must
  be fixed by a constraint -- which is P3.

- the split: gravity sees only excursions (curvature strain; gapped
  excess), never the floor. Weinberg's radiative-stability face in VED
  vocabulary: gravity only ever sees changes in the vacuum, never the
  vacuum itself.

P4's baseline relabels to the substance ledger; P6 destruction becomes
release of stored deficit energy; nothing in the closed chain changes.
```

Next target:

```text
packing_stiffness_microphysics_038: derive or reduce kappa_w, a, c_e.
Kill condition: a volume-mode restoring force in the packing energy
breaks the identification.
```

## The Regge/Delaunay Bridge (packing microphysics opens)

Recorded through VacuumForge as:

```text
derivation: regge_delaunay_bridge_039
obligations opened: regge_continuum_limit_039, p7prime_packing_tension_039
folder opened: 08_packing_microphysics/
```

Current conclusion:

```text
The owner's Delaunay-graph intuition is formalized as Regge calculus
with a frustrated ground state, and its first theorems are exact:
discrete Gauss-Bonnet (icosahedron, 4 pi exactly); curvature readable
from edge lengths alone (excess = K x area + O(s^4)); the 600-cell's
frustration deficit reproducing (1/2) int R sqrt(g) on S^3 to 3.5% at
the coarsest possible mesh (ratio = 120 Delta_0/(pi^2 phi) = 0.9648).

The central result is the EXPANSION-POINT THEOREM: expanding any smooth
wedge energy about the frustrated ground state gives the sequestered
floor (constant), the Regge/EH action (linear -- generic, because
f'(Delta_0) != 0 at a frustrated point), and a^2-suppressed R^2-class
corrections. An unfrustrated packing would have f'(0) = 0 and yield
curvature-squared gravity. Geometric frustration is why gravity is
Einstein-Hilbert -- roadmap 1C's weighting question answered,
conditional on the packing reading.

The floor-Newton lock eliminates kappa_w:
rho_v = (c_e Delta_0/(2 a^3)) f'(Delta_0) -- the substance energy and
the gravitational coupling are two readings of one wedge energy.

The strain-axiom contract now has a candidate with most fields filled
(mapping table in regge_delaunay_model.md); missing: discrete boundary
data, conservation identity, and the continuum limit. Honest tension
recorded: the a^2-suppressed R^2 term vs exact P7' (Planck-scale only;
no closed coefficient moves).
```

Next target:

```text
regge_continuum_limit_039 and the numerical relaxation module; then the
discrete boundary/conservation contract fields.
```

## Regge Refinement and Convergence

Recorded through VacuumForge as:

```text
derivation: regge_refinement_convergence_040
obligation discharged: regge_continuum_limit_039 (in-house portion)
obligation opened:     packing_model_4d_lorentzian_lift_040
```

Current conclusion:

```text
The 039 bridge is exact in the continuum limit.

2D: the deficit encoding of total curvature is a combinatorial identity
at EVERY refinement of EVERY closed surface (sum delta = 2 pi V - pi F
= 2 pi chi given 2E = 3F), and the local encoding converges
quadratically with EXACT coefficient:
excess = (sqrt(3)/4) s^2 [1 + (1/8) s^2 + O(s^4)].

3D: the complete regular tetrahedral family on S^3 -- there are exactly
three such triangulations in mathematics (5-cell, 16-cell, 600-cell
boundaries) -- converges monotonically to the EH action at quadratic
rate: ratios 0.6916 -> 0.7791 -> 0.9648 with (1-r)/s^2 = 0.0927,
0.0895, 0.0893 (drift 3.6% -> 0.3%).

The arbitrary-triangulation / higher-dimensional statement is a
declared external mathematical import (Cheeger-Muller-Schrader 1984;
Feinberg-Friedberg-Lee-Ren 1984), Fierz-Pauli class: discrete
differential geometry, no gravitational phenomenology input, no
framework coefficient dependent on it.

The expansion-point theorem's EH term (039) is therefore the exact
continuum response of the frustrated packing, with O(s^2)
discretization corrections.
```

Next target:

```text
packing_model_4d_lorentzian_lift_040 (hinge type, time's role, mode
count), p7prime_packing_tension_039, the numerical relaxation module,
and the remaining microphysics constants a, c_e.
```

## The Frustration Relaxation Lab (numerical module, phase 1)

Recorded through VacuumForge as:

```text
derivation: frustration_relaxation_lab_041
obligation opened: bulk_relaxation_scaling_041
```

Current conclusion:

```text
The forge's first experimental instrument: deterministic BFGS relaxation
of spring networks (no randomness; archive-stable). Measured:

E1  the 13-vertex icosahedral cluster relaxes to E = 0.0211 > 0
    (matching the exact symmetric optimum; grad ~ 1e-15), while the
    cuboctahedral (FCC-13) cluster relaxes to E < 1e-30: the frustration
    floor is a property of tetrahedral/icosahedral local order, exactly
    zero for FCC order. Measured, not asserted.

E2  wedge rings of n tetrahedra around a shared edge: E(3..7) =
    0.163, 0.061, 0.00065, 0.052, 0.243 -- strict minimum at n = 5 with
    a positive residual: Delta_0's arithmetic (037) as dynamical output
    of a relaxed network.

E3  the relaxed 5-ring's angle energy is dilation-invariant to machine
    precision (max |dE| ~ 4e-31 over lambda in [0.5, 2]) and shear-stiff
    with QUADRATIC response about equilibrium (dE(2e)/dE(e) = 3.96):
    linear deficit shifts cancel by symmetry -- the discrete analog of
    stationarity. The exact-flat vs quadratic-stiff mode asymmetry is
    the sector signature, measured at the many-body level.

E4  wrong-coordination rings (n = 4, 6) are locally stable relaxed
    configurations carrying quantized positive excess (0.0605, 0.0517)
    over the five-fold floor; decay requires a discrete topological
    move. Disclination-type defects have the persistence-and-excess
    profile the dark-excess lane requires of its gravitating
    excursions. Microstructure exhibit only: production/abundance
    remain fully gated.
```

Next target:

```text
bulk_relaxation_scaling_041 (phase 2): periodic bulk packings -- floor
intensivity vs system size, disclination-network formation, defect
energy spectrum.
```

## Discrete Conservation and Boundary Data (contract completion)

Recorded through VacuumForge as:

```text
derivation: discrete_conservation_boundary_042
obligation satisfied: contract_fields_filled_042
obligation opened:    strain_axiom_adoption_decision_live_042 (theory owner)
```

Current conclusion:

```text
The packing model's last two absent strain-axiom contract fields are
filled:

CONSERVATION: the flat Schlafli identity sum_e l_e d(delta_e) = 0
(2D exact symbolic; 3D verified to 50 digits at generic exact
configurations and exactly on the symmetric family) closes the Regge
variation -- dS = sum_e delta_e dl_e -- and under vertex displacements
(K3's discrete relabelings) the action varies only through the metric
data: the discrete diffeomorphism/Bianchi structure.

BOUNDARY: the Hartle-Sorkin hinge term psi_h = pi - sum(dihedrals) is
exactly additive under gluing (psi_1 + psi_2 = interior deficit;
wedge-ring 2+3 witness gives Delta_0 exactly) -- the property that
defines GHY -- and the 2D Gauss-Bonnet-with-boundary ledger closes
combinatorially.

Contract status: eight of nine fields filled (mode count partial,
pending the 4D/Lorentzian lift). The sector's head obligation --
the strain-axiom adoption decision (032) -- is now LIVE with a
near-complete candidate and pre-registered falsifiers (volume-mode
restoring force; floor/conversion-factor split). Adoption or
quarantine is a theory-owner call of the P7'/P9 class.
```

Next target:

```text
Theory-owner decision on the packing strain axiom; in parallel:
bulk_relaxation_scaling_041 (phase 2), p7prime_packing_tension_039,
and packing_model_4d_lorentzian_lift_040 (the one partial field).
```

## The 4D/Lorentzian Lift (contract complete)

Recorded through VacuumForge as:

```text
derivation: lorentzian_4d_lift_043
obligation discharged: packing_model_4d_lorentzian_lift_040 (scoped)
obligation opened:     4d_ground_coordination_043
```

Current conclusion:

```text
The ninth contract field is filled at kinematic + linearized level:

- 4D hinges are triangles; regular n-simplex dihedral = arccos(1/n)
  verified from exact coordinates (n = 2, 3, 4). Every integer
  coordination around a flat 4D triangle hinge is frustrated
  (n = 4: +57.91 deg; n = 5: -17.61 deg): the expansion-point theorem
  lifts to 4D and EH is the generic 4D response.
- The complete regular 4-simplex family on S^4 (5-simplex and
  5-orthoplex boundaries -- exactly two members) converges monotonically
  with matching quadratic-rate coefficients (0.2208, 0.2256): the 040
  convergence signature is dimension-stable.
- The action is algebraic in SQUARED edge lengths (polarization,
  verified exactly for the dihedral cosine): the Wick rotation to
  Lorentzian signature is term-by-term well-defined (Sorkin/CDT
  foundation), and the Lorentzian hinge algebra is exact rapidity
  additivity.
- Vertex displacements (K3's discrete relabelings) are exact zero
  modes of the deficit action (50-digit stationarity witnesses); the
  propagating mode count -- linearized Regge = linearized GR, massless
  spin-2, TT only -- is the declared Rocek-Williams (1981) import,
  Fierz-Pauli class.

THE STRAIN-AXIOM CONTRACT IS COMPLETE: NINE OF NINE FIELDS. The
adoption decision (strain_axiom_adoption_decision_live_042) is before
the theory owner with a full candidate and pre-registered falsifiers.

Honest boundaries: the 4D ground coordination (opposite deficit signs
at n = 4 vs n = 5) is open; no nonperturbative Lorentzian dynamics is
claimed (kinematic + linearized only).
```

Next target:

```text
Theory-owner adoption decision. In parallel: bulk_relaxation_scaling_041
(phase 2), p7prime_packing_tension_039, 4d_ground_coordination_043, and
the paper drafts for the unimodular and frustration arcs.
```

## P10 ADOPTED (theory-owner decision, 2026-07-01)

Recorded through VacuumForge as:

```text
derivation: p10_adoption_record_044
obligation resolved: strain_axiom_adoption_decision_required_032
                     (via _live_042) -- ADOPTED
obligations opened:  O-P10-1..5 (microphysics constants; 4D ground
                     coordination; P7' tension; Lorentzian dynamics;
                     bulk relaxation phase 2)
```

The head obligation of the vacuum-sector program is resolved: the
Regge/Delaunay packing model is adopted as P10, the packing axiom
(theory_v3/01_postulates/p10_packing_axiom.md), with fence and
pre-registered falsifiers (F-P10-1 volume-mode restoring force;
F-P10-2 floor/conversion-factor split; F-P10-3 inherited P7' null
test). The adoption's epistemic record is stated honestly in the
postulate file: adopted AFTER the 037-043 verification campaign, on
coherence evidence; forward weight from consequences not yet checked.

The section of record for the implied theory is now
theory_v3/05_vacuum_sector/ (00_overview through 05_open_obligations):
the substance energy (unrealized curvature, sequestered), the
gravitational response (EH from the frustrated expansion point), Lambda
and the global datum (settled status; value external, and why), and the
excursion/exchange ledger (potential/kinetic curvature, the exact P6
pipeline, defects as gated candidates).

The program transitions from axiom search to theory development under
an adopted axiom. The gates guard P10 now.

## The P6-P10 Consistency Audit

Recorded through VacuumForge as:

```text
derivation: p6_p10_consistency_045
obligation satisfied: p6_p10_seam_audited_045
obligation opened:    p6_p10_cosmological_creation_045
```

Current conclusion:

```text
The double-counting danger (P6's substance destruction vs the
configuration deepening as two funding sources for infall KE, against
P9's count-once fence) is resolved by theorem: KE = -Delta U_cross
EXACTLY at the Newtonian anchor (zero residual; pointwise rate face
smooth), so there is only one ledger entry -- and P1's identity
(vacuum IS energy) makes P6's substance vocabulary and P10's strain
vocabulary two descriptions of it. Destruction = strain content
dropping below the floor, no cell removed; the exterior deficit
integrates to 2GM^2/R, the weak-field form of the recorded cap-ledger
entry. P3 compatibility holds structurally (intensive self-measured
density protected by dilation invariance + P2; wells are extensive
content deficits per P3a). Strong-field rate face: the exact PG river
ledger (021).

Consistency verdict: P6-P10 consistent at every shared quantitative
anchor; satisfiability-by-common-model completed for the infall face.
Open (an underdetermination, not a contradiction): the cosmological-
creation reading -- graph growth vs content rise -- assigned to the
Lorentzian-dynamics program (O-P10-4).
```

## Predictions Register Opened

`theory_v3/development/predictions/predictions_register.md` inventories
every observable commitment the theory currently makes, tiered:

```text
Tier A (kill zone, now/near-term):
  A1  w(z) = -1 exactly, constant -- UNDER LIVE FIRE (DESI-class
      evolving-DE preferences); the discipline trap (no excess
      backsolve) is pre-registered
  A2  GW: two TT polarizations, no dispersion, quadrupole rate
  A3  no gravitational-strength Yukawa at any range (P7')
  A4  black-hole exteriors/ringdowns exactly GR
  A5  no linear-order LIV -- simultaneously a prediction and the
      sharpest currently-computable SELF-THREAT: the packing's own
      dispersion relation must be computed (new high-priority
      obligation; linear dispersion would kill P10 against existing
      GRB bounds)
Tier B: sequestering's falsifiable edge; defect-DM non-gravitational
      nulls (conditional); the Casimir/UFFT window; Lambda's sign
Tier C: dispersion computation, defect spectrum, cosmological-creation
      observable face, conversion-factor relation, kappa-leak scaling
```

The register's rule: no entry may be softened after an adverse result
except by a recorded postulate-level move. Backsolving forbidden.

## The Packing's Dispersion Relation (A5/C1 resolved)

Recorded through VacuumForge as:

```text
derivation: packing_dispersion_046
obligation satisfied: packing_dispersion_computed_046
obligation opened:    chiral_matter_dispersion_watch_046
```

Current conclusion:

```text
THE EVENNESS THEOREM: for any harmonic network whose energy is a real
quadratic form with finite-range couplings (pair, angle/wedge,
arbitrary multi-body -- the entire P10 class), the dynamical matrix
satisfies D(-k) = D(k)* and is Hermitian, so the spectrum omega^2(k)
is exactly even in k along every direction: NO linear-in-(E/E_Planck)
dispersion can exist, for any graph, with no lattice symmetry
required. Verified: exact monatomic chain (omega/ck = 1 - (ka)^2/24);
fully symbolic generic two-band model (trace and det even for
arbitrary real couplings); diatomic no-inversion witness (textbook
sound speed, zero k^3 term).

Numbers: linear scale infinite (theorem); quadratic scale ~ sqrt(24)
E_P ~ 6e19 GeV vs current GRB quadratic bounds ~1e11 GeV -- margin
~6e8; a 1 TeV photon's |dv/c| ~ 3e-34.

P10 SURVIVES ITS SHARPEST CURRENTLY-COMPUTABLE TEST -- protected by
the reality of the strain energy, the same structural fact behind the
sector. Register A5 sharpened: confirmed linear LIV now falsifies P10
outright. Watch item: chiral (TR-breaking) matter discretizations
evade the theorem; any future matter-ontology work must re-run the
check.
```

## The Scalaron vs the Unimodular Constraint (O-P10-3 attacked)

Recorded through VacuumForge as:

```text
derivation: scalaron_unimodular_047
obligation satisfied: o_p10_3_attacked_047
obligation opened:    p7prime_scoping_ruling_047 (theory-owner ruling)
```

Current conclusion:

```text
HONEST NEGATIVE: the proposed mechanism -- "the unimodular constraint
kills the scalaron" -- is REFUTED in-house. The f(R) EL tensor is
identically conserved (verified: FRW divergence of the full
f = R + alpha R^2 tensor vanishes with no field equations imposed), so
the divergence of the traceless/unimodular equations reconstructs the
trace equation up to an integration constant -- the same Bianchi
mechanism that made Lambda an integration constant in 033. The
scalaron equation returns exactly: (6 alpha box - 1) R = kappa T +
const, with m^2 = 1/(6 alpha). Unimodular f(R) = f(R) + free Lambda.

O-P10-3 therefore reduces to a scoping ruling on adopted P7', with
both routes pre-analyzed and no coefficient or observable moving
under either:

  (i) P7' scoped as the a -> 0 idealization (the F1-leak precedent):
      the packing scalaron has range l* = sqrt(6 alpha) ~ sqrt(6) l_P
      ~ 4e-35 m -- a factor ~1.4e30 below the 54 um laboratory
      frontier. A Planck-range Yukawa is operationally
      indistinguishable from none; the null-test falsifier face is
      unchanged. RECOMMENDED.

 (ii) strict exactness: forces f''(Delta_0) = 0, an inflection of the
      wedge energy at the frustrated ground state (verified: the
      R^2-class coefficient is exactly f''(Delta_0)/2). Kills the
      R^2 class exactly, leaves floor and EH intact -- but is
      recovery-shaped without independent motivation. Cost recorded.

The ruling (p7prime_scoping_ruling_047) is the theory owner's.
```

## The P7' Scoping Ruling: Route (i) Adopted (O-P10-3 closed)

Recorded through VacuumForge as:

```text
derivation: p7prime_scoping_ruling_record_048
obligation satisfied: p7prime_scoping_ruled_048
  (resolves p7prime_scoping_ruling_047; closes O-P10-3)
```

Current conclusion:

```text
THEORY-OWNER RULING (2026-07-02): ROUTE (i). P7' is scoped as the
double idealization -- exact at H -> 0 (static; the F1 kappa-leak is
the controlled correction) AND at a -> 0 (continuum; the Planck-range
packing scalaron of 047 is the controlled correction). "No static
flow, exactly zero" is officially a LIMIT RESULT: exactness is the
idealization's property, and the physical vacuum's deviations must be
derived, controlled, and individually recorded. The register of such
corrections has exactly two entries, both quadratic in their small
parameter, both sub-observable, neither reopening a closed
coefficient.

Route (ii) (the f''(Delta_0) = 0 inflection constraint) is REJECTED
as recovery-shaped without independent motivation; retained on record
as the fallback.

Unchanged: the A3/F-P10-3 null test (any DETECTED Yukawa at any
accessible range kills). New: the discreteness consistency battery --
if the packing scale a is ever independently measured, a scalaron
Yukawa at range sqrt(6) a is a parameter-free prediction (alongside
C4, the floor-Newton lock).

O-P10-3 is CLOSED. P10's remaining ledger: O-P10-1, -2, -4, -5.
```

## The Quadratic Selector Closure (metric vs Finsler audit closed)

Recorded through VacuumForge as:

```text
derivation: quadratic_selector_closure_049
obligation satisfied: quadratic_gate_import_closed_049
  (closes capstone imported-assumption rows 1-2)
```

Current conclusion:

```text
THE METRIC-VS-FINSLER AUDIT CLOSES UNDER P10. The projection-origin
probe's two root imports of the GR branch -- "exact quadratic
response" and "epsilon = 0" for interval response -- are theorems of
the flatness clause:

  1. FLAT IS QUADRATIC: for a generic symmetric form (n = 4, any
     signature) the parallelogram identity holds identically,
     polarization is exactly bilinear, and the fundamental tensor is
     direction-independent.
  2. FINSLER DATA IS UNSTORABLE: per n-cell the packing stores
     C(n+1,2) edge lengths = n(n+1)/2 quadratic components EXACTLY
     (every n); the smallest Finsler class (quartic) needs 35
     coefficients in 4D against 10 edges. Not suppressed -- no slot.
  3. EDGE DATA IS METRIC DATA, BIJECTIVELY: the law-of-cosines
     inversion reconstructs the generic form from edge lengths
     exactly.
  4. The probe's own quartic witness reproduced (residual 12 eps)
     and shown outside the axiom's state space.

The only direction dependence the packing can express lives at hinges
as deficit -- curvature, the theory's subject, not a hidden norm. The
routing rule becomes a theorem: the eps_Finsler branch has an empty
state space.

Watch item: ground-state isotropy (an anisotropic ground order could
give the long-wavelength effective response a preferred structure) --
guarded by O-P10-2/O-P10-5; recorded in the report's kill face.
```
