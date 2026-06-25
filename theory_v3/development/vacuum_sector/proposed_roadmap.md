# Vacuum Sector Proposed Roadmap

This roadmap is a proof roadmap, not a mechanism wishlist.

The central operating rule is:

```text
A deviation or addition beyond the closed GR metric response is admissible only
if it either:

1. preserves the closed local Einstein metric response, or
2. explicitly routes the departure through a new ledger with its own variables,
   equations, conservation law, boundary data, mode count, source bookkeeping,
   weak-field face, and falsifier.
```

The current architecture already enforces this rule:

```text
local response alone does not choose K_strain;
X and neighboring mismatch are still contracts;
no residual is licensed as controlled epsilon != 0;
Lambda is separated from local strain residual work;
bare variational minimization over F(Lambda) does not derive nonzero Lambda.
```

## Master Proof-State Machine

Every candidate route should pass through the same state machine:

```text
candidate idea
-> X contract
-> neighboring-mismatch contract
-> invariant/action/selector object
-> boundary variation
-> conservation identity
-> mode/principal-symbol check
-> weak-field or observable face
-> source-ledger check
-> epsilon / baseline / channel classification
-> kill condition or live status
```

Allowed final statuses:

```text
epsilon = 0 equivalent
controlled epsilon != 0
Lambda selector candidate
dark-sector excess candidate
non-gravitational channel candidate
strong-interior candidate
fails accumulated gate
underdetermined without new axiom
```

No route should stop at "interesting." It should be forced into one of these
buckets.

## 1. EH/GHY Strain-Branch Selection

The deepest open question is:

```text
What chooses K_strain = K_EH/GHY?
```

Current state:

```text
pointwise interval response reconstructs local metric data under the quadratic
gate, but it does not determine connection, transport, curvature action,
boundary terms, modes, or epsilon.
```

There are three useful proof paths.

### 1A. Minimal Calibration-Coherent Strain

Candidate closure statement:

```text
If the vacuum strain rule is:
  local,
  calibration-coherent,
  diffeomorphism/relabeling invariant,
  metric-compatible,
  has no independent torsion or nonmetricity source,
  has no extra fields,
  is boundary differentiable with fixed induced metric,
  and gives second-order field equations,

then K_strain = EH/GHY + Lambda + inert/topological terms.
```

This path would not produce a deviation from GR. It would explain why the
closed GR branch is selected.

Suggested files:

```text
01_strain_functional/minimal_calibration_coherent_strain_axiom.md
02_candidate_branches/eh_ghy_selector_from_minimal_strain.md
vacuum_forge/src/vacuum_sector/012_minimal_strain_selector/minimal_strain_selector.py
```

The script should classify allowed scalar terms by derivative order and gate
status:

```text
constant term:
  Lambda baseline, not strain dynamics

R:
  EH/GHY candidate

Gauss-Bonnet / total derivative:
  inert or boundary/topological

R^2 / Ricci^2 / Weyl^2:
  higher-curvature residual route already blocked or quarantined

nonlocal terms:
  route to Lambda, dark-sector, or large-scale ledger

extra connection / torsion / Finsler / medium:
  extra-field or new-axiom route
```

Expected classification:

```text
Under the minimal calibration-coherent strain axiom, EH/GHY is selected.
Without that axiom, the current ontology remains underdetermined.
```

### 1B. Metric-Affine Route To Levi-Civita

This path attacks the "why Levi-Civita?" gap directly.

Candidate theorem:

```text
Given metric local response g_ab and an independent connection Gamma, the
minimal Palatini-like linear-curvature strain with no hypermomentum, no torsion
source, and no nonmetricity source forces Gamma to reduce to Levi-Civita, up
to projective or inert ambiguity.
```

Suggested files:

```text
02_candidate_branches/metric_affine_compatibility_probe.md
vacuum_forge/src/vacuum_sector/013_metric_affine_compatibility/metric_affine_compatibility.py
```

Useful outcomes:

```text
Gamma collapses to Levi-Civita:
  metric-affine route supports EH/GHY closure

Gamma has extra modes:
  route torsion/nonmetricity through residual gates

Gamma compatibility cannot be derived:
  new strain axiom required
```

### 1C. Holonomy / Regge Route

Holonomy is useful because it separates two possibilities:

```text
linear deficit / Regge-type action:
  sum area * deficit -> continuum EH

squared holonomy norm:
  curvature^2 -> higher-curvature residual route
```

Suggested files:

```text
02_candidate_branches/holonomy_small_loop_selector.md
vacuum_forge/src/vacuum_sector/014_holonomy_small_loop_selector/holonomy_small_loop_selector.py
```

Proof path:

```text
1. Small-loop transport failure scales like curvature times area.
2. A linear deficit action gives an EH-like term.
3. A squared mismatch norm gives curvature-squared terms.
4. Curvature-squared terms re-enter the higher-curvature gate and are blocked
   or quarantined.
5. Therefore holonomy selects EH only if the ontology supplies a reason for
   linear deficit/Regge weighting rather than squared mismatch energy.
```

Expected classification:

```text
Holonomy remains underdetermined unless the weighting rule is supplied.
```

## 2. Controlled Strain Residuals

The residual branch space is not empty, but it is heavily gated.

Current status:

```text
EH/GHY baseline:
  admissible at epsilon = 0

higher-curvature local residual:
  not licensed under the current closure

metric-affine, holonomy, Finsler, medium, and nonlocal branches:
  chartered or suggested routes, not live predictions
```

### 2A. Inert Boundary / Topological Terms

Goal:

```text
Classify whether a term is:
  epsilon = 0 equivalent,
  boundary-quarantined,
  or a real residual.
```

Suggested files:

```text
02_candidate_branches/inert_boundary_topological_probe.md
vacuum_forge/src/vacuum_sector/015_inert_boundary_topological/inert_boundary_topological.py
```

Toy checks:

```text
total derivative in 1D:
  changes boundary variation only, not bulk equation

Gauss-Bonnet in 4D:
  inert in bulk, may affect boundary/topological ledger

field redefinition:
  no independent epsilon
```

Expected classification:

```text
Boundary/topological terms do not become controlled epsilon != 0 unless they
supply an explicit boundary-sector observable without changing closed bulk GR.
```

### 2B. Higher-Curvature Residuals

This route is already mostly handled.

Current route classification:

```text
inert/topological:
  epsilon = 0 equivalent or boundary-quarantined

spin-2/Weyl:
  failed ghost route

scalaron/f(R):
  ghost-safe after mode routing but blocked by P7prime/weak-field closure
  unless P7prime is explicitly reopened

generic mixed curvature squared:
  must decompose before evaluation
```

Do not extend this route unless a concrete P7prime appeal or new decomposition
obligation is opened.

### 2C. Finsler / Nonquadratic Response

Goal:

```text
Determine whether nonquadratic directional response can be routed as a
controlled residual, or whether calibration/local Lorentz constraints force it
to zero.
```

Suggested files:

```text
02_candidate_branches/finsler_directional_perturbation_probe.md
vacuum_forge/src/vacuum_sector/016_finsler_directional_perturbation/finsler_directional_perturbation.py
```

Prototype:

```text
Q_p(v) = g_ab v^a v^b + epsilon H_p(v)
```

where `H_p(v)` violates the parallelogram/quadratic identity.

Tests:

```text
parallelogram identity residual;
null-cone shift;
species-independent matter calibration;
PPN/preferred-direction face;
whether H_p can be pure gauge or must be observable.
```

Expected theorem shape:

```text
Exact shared metric calibration plus exact quadratic gate forces H_p = 0.

If H_p != 0, it is not hidden inside the metric branch. It is a routed
nonmetric/Finsler residual with observable cone/calibration consequences.
```

### 2D. Medium / Configuration-Elastic Strain

Goal:

```text
Determine whether a deeper material X can reduce to metric response without
extra propagating medium modes, anisotropy, preferred-frame leakage, or source
double-counting.
```

Suggested files:

```text
02_candidate_branches/medium_constitutive_map_contract.md
vacuum_forge/src/vacuum_sector/017_medium_constitutive_map/medium_constitutive_map.py
```

Proof path:

```text
1. Define medium/order parameter X.
2. Define constitutive map X -> Q_p(v) -> g_ab.
3. Linearize around homogeneous vacuum.
4. Count elastic modes.
5. Check whether modes are frozen, constrained, or physical.
6. If physical, route preferred-frame, anisotropy, or longitudinal modes.
7. If frozen by infinite stiffness, ask whether the branch has become metric
   placeholder plus a new axiom.
```

Likely outcomes:

```text
extra modes appear:
  routed residual required

all modes frozen:
  no new local residual; branch may become ontology-only

constitutive law absent:
  underdetermined without new axiom
```

### 2E. Nonlocal / Relaxation Strain

Goal:

```text
Can a nonlocal or relaxation term affect Lambda, dark-sector, or large-scale
behavior while leaving closed local metric tests intact?
```

Suggested files:

```text
02_candidate_branches/nonlocal_local_limit_quarantine.md
vacuum_forge/src/vacuum_sector/018_nonlocal_local_limit_quarantine/nonlocal_local_limit_quarantine.py
```

Toy kernel:

```text
S_nonlocal = integral X(x) K(x,y) X(y)
```

Fourier/local-limit check:

```text
K(k) = K0 + K2 k^2 + K4 k^4 + ...
```

Interpretation:

```text
K0 only:
  possible homogeneous baseline/floor route

K2, K4, ... nonzero:
  local equations or propagator change; must pass residual gates

projection onto zero mode only:
  possible Lambda/global channel if conservation and boundary data work
```

Expected theorem:

```text
A nonlocal branch may stay quarantined only if its local perturbative leakage
vanishes or is explicitly bounded/routed.
```

## 3. Lambda Baseline Selection

This is the most immediate workstream.

Current result:

```text
Lambda = 0:
  asymptotically flat scalar boundary-flux sector when no nonzero background is
  supplied

Lambda free:
  allowed but unvalued EH/Lovelock background constant

Lambda nonzero derived:
  selector required
```

The selector charter and sieve are in place. The variational-minimum probe
blocks the empty route:

```text
bare stationarity over F(Lambda) leaves Lambda free, selects zero, has no
interior stationary point for a lone linear bias, or imports a bias/target/scale.
```

### 3A. Boundary / Admissibility Lambda Probe

This is the next stated obligation.

Suggested files:

```text
04_lambda_baseline/lambda_boundary_admissibility_probe.md
vacuum_forge/src/vacuum_sector/012_lambda_boundary_admissibility/lambda_boundary_admissibility.py
```

Test cases:

```text
asymptotic flatness:
  finite scalar bridge -> Lambda = 0

asymptotic de Sitter with radius L:
  Lambda = +3/L^2
  but L is boundary input unless derived

asymptotic anti-de Sitter with radius L:
  Lambda = -3/L^2
  but L is boundary input unless derived

compact constant-curvature 4D manifold:
  Gauss-Bonnet gives Lambda^2 * V proportional to chi
  so Lambda^2 = 12*pi^2*chi / V for constant-curvature Einstein spaces
  but V supplies the scale and sign still needs a selector

horizon/domain boundary:
  Lambda related to boundary radius or extrinsic curvature
  but the boundary scale is imported unless the ontology derives it
```

Expected conclusion:

```text
Boundary/admissibility data can select allowed Lambda families and can convert
a supplied length/volume scale into Lambda. It does not derive a nonzero value
unless the boundary scale itself is selected by the vacuum ontology.
```

### 3B. Topology / Global Constraint Probe

Suggested files:

```text
04_lambda_baseline/lambda_topology_global_constraint_probe.md
vacuum_forge/src/vacuum_sector/013_lambda_topology_global_constraint/lambda_topology_global_constraint.py
```

Path:

```text
1. Topology gives dimensionless invariants.
2. Lambda has dimension L^-2.
3. Therefore topology alone cannot set Lambda without a length, volume,
   measure, or quantization rule.
4. In constant-curvature 4D, Gauss-Bonnet can relate Lambda^2 V to chi.
5. Without V or a volume selector, no value is derived.
```

Expected conclusion:

```text
Topology may discretize or constrain Lambda only when paired with a volume,
measure, or admissibility selector. It cannot by itself derive a dimensionful
Lambda value.
```

### 3C. Measure Identity Probe

Suggested files:

```text
04_lambda_baseline/lambda_measure_identity_probe.md
vacuum_forge/src/vacuum_sector/014_lambda_measure_identity/lambda_measure_identity.py
```

Required checks:

```text
measure identity is explicitly written;
dimensions produce energy density or curvature scale;
identity is covariant;
source ledger is conserved;
observed value is not inserted;
dark excess remains separate.
```

Expected fork:

```text
identity supplies a real density scale:
  candidate Lambda selector

identity only fits dimensions:
  killed as dimensional fitting

identity produces transportable/clustered energy:
  route to dark-sector excess, not Lambda
```

### 3D. Relaxation / Nonlocal Lambda Probe

Suggested files:

```text
04_lambda_baseline/lambda_relaxation_fixed_point_probe.md
vacuum_forge/src/vacuum_sector/015_lambda_relaxation_fixed_point/lambda_relaxation_fixed_point.py
```

Toy cases:

```text
dLambda/dt = -gamma Lambda:
  selects zero

dLambda/dt = -gamma (Lambda - Lambda_star):
  selects imported target

kernel/history integral with no scale:
  no nonzero floor

kernel/history integral with scale:
  nonzero floor inherits kernel/domain scale
```

Expected conclusion:

```text
Relaxation can select nonzero Lambda only if the kernel/domain/fixed-point
equation supplies a scale and conservation law.
```

### 3E. Frustration-Floor Microphysics Probe

Suggested files:

```text
04_lambda_baseline/lambda_frustration_floor_microphysics_contract.md
vacuum_forge/src/vacuum_sector/016_lambda_frustration_floor_microphysics/lambda_frustration_floor_microphysics.py
```

Minimum required derivation:

```text
microstate variable;
coarse-graining map;
ground-state/frustration energy density;
why it is constant and w = -1;
why it does not cluster;
why it is not dark excess;
sign and scale before observation.
```

First warning:

```text
A Landau-style potential V(phi) can produce a vacuum floor, but the absolute
offset V0 is not derived unless the microphysics fixes it.
```

Expected conclusion:

```text
Frustration-floor microphysics is live only after it derives the absolute
constant floor, not merely a potential shape.
```

## 4. Dark-Sector Excess Over The Baseline

This work should stay downstream until the Lambda floor ledger is protected.

Suggested first files:

```text
05_dark_sector/README.md
05_dark_sector/dark_excess_source_ledger.md
05_dark_sector/dark_excess_equation_of_state_probe.md
vacuum_forge/src/vacuum_sector/017_dark_excess_source_ledger/dark_excess_source_ledger.py
```

Proof path:

```text
1. Split vacuum contribution:
   T_vac = T_floor + T_excess

2. Floor:
   T_floor_ab = -rho_Lambda g_ab
   w = -1
   constant baseline
   belongs to Lambda ledger

3. Excess:
   T_excess_ab must be separately conserved or have an explicit exchange law
   must cluster or transport
   must not be inserted as ordinary matter by declaration

4. Equation-of-state classifier:
   pointlike/gapped nonrelativistic excitations -> w ~= 0
   strings -> w ~= -1/3
   walls -> w ~= -2/3
   constant floor -> w = -1

5. Clustering gate:
   small sound speed;
   geodesic or controlled force law;
   no untracked pressure/support term

6. Abundance gate:
   production mechanism;
   freeze-out or formation yield;
   no observed abundance insertion.
```

First symbolic check:

```text
rho scales as a^(-3(1+w))

w = -1:
  constant floor -> Lambda

w = 0:
  dustlike excess -> dark-sector candidate

w = -1/3 or -2/3:
  strings/walls, not CDM-like without more structure
```

Expected conclusion:

```text
Dark-sector excess can become live only after it has production, abundance,
conservation, clustering, and source-ledger separation from Lambda.
```

## 5. Non-Gravitational Vacuum Channels

These are deviations/additions beyond ordinary vacuum expectations, not
necessarily deviations from GR gravity.

Suggested first files:

```text
06_non_gravitational_channels/README.md
06_non_gravitational_channels/channel_quarantine_contract.md
06_non_gravitational_channels/casimir_ufft_channel_contract.md
06_non_gravitational_channels/substance_frame_coupling_contract.md
vacuum_forge/src/vacuum_sector/018_non_grav_channel_quarantine/non_grav_channel_quarantine.py
```

Required channel contract:

```text
channel variable;
coupling object;
why it does not modify the closed metric response;
source ledger;
observable;
falsifier;
current bounds or target window;
failure route.
```

### Casimir / UFFT Route

Proof path:

```text
1. Define the vacuum-channel observable.
2. Show it is not a gravitational Yukawa force.
3. Show how boundary/material/Casimir data enter.
4. Write the falsifier.
5. Quarantine from metric T_ab unless explicitly routed.
```

Expected conclusion:

```text
Casimir/UFFT may be a non-gravitational vacuum channel only if it has its own
coupling and falsifier, and does not get counted as a local gravity residual.
```

### Substance-Frame Route

Proof path:

```text
1. Vacuum substance frame exists ontologically.
2. Closed metric sector has no coupling to the frame velocity.
3. Any detectable coupling must be a new non-gravitational channel.
4. Write the coupling operator.
5. Check preferred-frame, anisotropy, Lorentz-violation, and matter-calibration
   consequences.
```

Expected conclusion:

```text
The frame is not a prediction of preferred-frame forces unless a coupling is
added and gated.
```

## 6. Strong-Field / Interior Admissibility

This is open because the weak-field, exterior, and radiative sectors can be GR
while compact interiors still require vacuum-sector completion.

Suggested files:

```text
07_interior_cap/README.md
07_interior_cap/interior_cap_contract.md
07_interior_cap/exterior_matching_lemma.md
07_interior_cap/finite_strain_admissibility_probe.md
vacuum_forge/src/vacuum_sector/019_interior_cap_admissibility/interior_cap_admissibility.py
```

Proof path:

```text
1. Exterior preservation lemma:
   If the exterior field equations remain GR and the exterior source mass is M,
   then the outside metric remains Schwarzschild/Schwarzschild-de Sitter.

2. Interior freedom:
   Changes inside the compact object are allowed only if matching conditions
   preserve the tested exterior.

3. Finite-strain criterion:
   Identify which energy/action/strain quantity diverges as compactness
   approaches the GR singular/horizon threshold.

4. Scale test:
   If a cap radius or cutoff is introduced, determine whether it is derived
   from vacuum ontology or imported.

5. Observational face:
   compactness limit, echo/merger signature, maximum redshift, modified
   interior equation of state, or no exterior deviation.
```

Likely first result:

```text
Interior cap requires a new admissibility scale or rule. Without that rule, the
ontology localizes the problem but does not solve the strong-interior
completion.
```

## 7. Global / Boundary / Topological Selectors

This category overlaps Lambda, holonomy, and interiors, so it should be treated
as a cross-cutting selector class.

Suggested files:

```text
04_lambda_baseline/global_boundary_topology_selector_rules.md
vacuum_forge/src/vacuum_sector/020_global_boundary_topology_rules/global_boundary_topology_rules.py
```

General theorem:

```text
Global, boundary, or topological data may restrict allowed sectors or
backgrounds while leaving local equations unchanged.

But a dimensionful local value such as Lambda requires a dimensionful scale:
length, area, volume, cutoff, measure density, or microphysical parameter.
Topology alone is dimensionless and cannot set a value without such a scale.
```

Symbolic checks:

```text
2D Gauss-Bonnet:
  integral R dA = 4*pi*chi
  constant R gives R = 4*pi*chi / A
  value needs area A

4D constant-curvature Gauss-Bonnet:
  integral E dV = 32*pi^2 chi
  E = (8/3) Lambda^2
  Lambda^2 = 12*pi^2 chi / V
  value needs volume V and sign selector
```

Expected conclusion:

```text
Topology/global constraints can constrain Lambda or sectors only after a
volume, measure, or admissibility rule supplies the missing scale.
```

## Recommended Execution Order

Near-term order:

```text
012_lambda_boundary_admissibility_probe
013_lambda_topology_global_constraint_probe
014_metric_affine_compatibility_probe
015_holonomy_small_loop_selector_probe
016_nonlocal_local_limit_quarantine_probe
017_finsler_directional_perturbation_probe
018_dark_excess_source_ledger
019_non_grav_channel_quarantine
020_interior_cap_admissibility
```

The first four are highest value:

```text
Lambda boundary/admissibility:
  next stated obligation; likely produces a clean result

Topology/global constraint:
  pairs naturally with boundary Lambda and prevents topology overclaims

Metric-affine compatibility:
  attacks "why Levi-Civita?" directly

Holonomy small-loop:
  attacks "why EH rather than curvature-squared?" directly
```

The remaining routes should wait until these are closed or localized as
new-axiom gaps.

## File Template

Every new proof/probe file should use this structure:

```text
# Claim

# Scope

# Inputs Used

# What Is Not Assumed

# Candidate Object

# Symbolic / Variational / Ledger Check

# Gate Results

# Current Classification

# Non-Conclusions

# Satisfied Obligation

# Newly Opened Obligation
```

Every script should emit the same classification language:

```text
result type:
scope:
conclusion:
non-conclusion:
next technical target:
```

Every route should end in one of:

```text
passes as epsilon = 0 equivalent;
passes as controlled epsilon != 0;
passes as Lambda selector candidate;
passes as quarantined non-gravitational channel;
fails accumulated gate;
underdetermined without new axiom.
```

## Working Warning

Do not try to solve the vacuum sector in one file. The winning move is to turn
each remaining story into a proof-shaped fork. The project succeeds if each
fork either earns new physics, collapses to GR/EH/GHY, or exposes exactly which
new axiom would be needed.
