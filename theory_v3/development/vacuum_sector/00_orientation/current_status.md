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
