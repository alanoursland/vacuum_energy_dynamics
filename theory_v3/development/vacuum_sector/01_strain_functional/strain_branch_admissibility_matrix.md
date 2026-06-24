# Strain Branch Admissibility Matrix

This matrix is the first vacuum-sector deliverable. It should be filled before
candidate branches are treated as live physics.

## Status Labels

Use only these branch-status labels unless a later note explicitly extends the
ledger:

```text
admissible at epsilon = 0
controlled epsilon != 0 possible
fails accumulated gate
underdetermined without new axiom
not yet evaluated
```

## Matrix Columns

Each candidate strain branch should be evaluated with this row format:

```text
branch:
X variable:
neighboring mismatch rule:
candidate invariant/scalar:
boundary term:
metric-limit status:
diffeomorphism/relabeling status:
mode count:
hyperbolicity status:
source-ledger status:
epsilon status:
kill condition:
next test:
```

## Accumulated Gates

A branch must pass or explicitly route each gate:

```text
metric reduction at lowest order
routed nonquadratic response
calibration coherence
diffeomorphism/relabeling invariance
Lorentzian hyperbolicity
two TT degrees of freedom in the GR branch
boundary differentiability
symplectic radiation bookkeeping
source-ledger purity
```

## Empty Starting Matrix

The following rows are placeholders. They should be completed only when the
branch has a contract and a test plan.

```text
branch: local-response-only selector
X variable: interval-response data Q_p(v), reducing pointwise to g_ab when quadratic
neighboring mismatch rule: absent
candidate invariant/scalar: V_local only
boundary term: absent
metric-limit status: reconstructs pointwise metric data when quadratic
diffeomorphism/relabeling status: not enough information
mode count: not determined
hyperbolicity status: not determined
source-ledger status: not determined
epsilon status: underdetermined without new axiom
kill condition: treats pointwise metric reconstruction as transport, curvature action, boundary variation, mode content, or epsilon classification
next test: supply a between-point strain principle or prove accumulated gates force EH/GHY
```

```text
branch: EH/GHY baseline
X variable: metric data g_ab
neighboring mismatch rule: Levi-Civita curvature branch
candidate invariant/scalar: EH bulk plus GHY boundary
boundary term: GHY
metric-limit status: admissible at epsilon = 0
diffeomorphism/relabeling status: passes by construction
mode count: two TT modes in GR branch
hyperbolicity status: GR branch
source-ledger status: stress route already conditionally reconstructed
epsilon status: epsilon = 0 definition
kill condition: none; baseline, not a new result
next test: use only as comparison branch
```

```text
branch: EH/GHY plus residual
X variable: not yet evaluated
neighboring mismatch rule: not yet evaluated
candidate invariant/scalar: K_EH/GHY + epsilon K_residual
boundary term: not yet evaluated
metric-limit status: not yet evaluated
diffeomorphism/relabeling status: not yet evaluated
mode count: not yet evaluated
hyperbolicity status: not yet evaluated
source-ledger status: not yet evaluated
epsilon status: not yet evaluated
kill condition: residual violates any accumulated gate without explicit route
next test: classify residual type in ../03_epsilon_tests/
```

```text
branch: configuration-elastic strain
X variable: not yet evaluated
neighboring mismatch rule: medium/configuration gradient
candidate invariant/scalar: not yet evaluated
boundary term: not yet evaluated
metric-limit status: not yet evaluated
diffeomorphism/relabeling status: not yet evaluated
mode count: not yet evaluated
hyperbolicity status: not yet evaluated
source-ledger status: not yet evaluated
epsilon status: not yet evaluated
kill condition: hidden preferred structure, anisotropy, or extra modes without explicit route
next test: complete X and mismatch contracts
```

```text
branch: holonomy mismatch strain
X variable: not yet evaluated
neighboring mismatch rule: loop/transport failure
candidate invariant/scalar: not yet evaluated
boundary term: not yet evaluated
metric-limit status: not yet evaluated
diffeomorphism/relabeling status: not yet evaluated
mode count: not yet evaluated
hyperbolicity status: not yet evaluated
source-ledger status: not yet evaluated
epsilon status: not yet evaluated
kill condition: curvature-squared or higher-derivative modes appear without allowed route
next test: explain why leading scalar is EH-like or explicitly residual
```

```text
branch: Finsler/nonquadratic residual
X variable: directional response data
neighboring mismatch rule: not yet evaluated
candidate invariant/scalar: not yet evaluated
boundary term: not yet evaluated
metric-limit status: requires explicit routing
diffeomorphism/relabeling status: not yet evaluated
mode count: not yet evaluated
hyperbolicity status: not yet evaluated
source-ledger status: not yet evaluated
epsilon status: not yet evaluated
kill condition: hidden null-cone, PPN, matter-calibration, or propagation deviation
next test: nonquadratic routing and weak-field residual tests
```

```text
branch: nonlocal/relaxation strain
X variable: not yet evaluated
neighboring mismatch rule: nonlocal kernel or global constraint
candidate invariant/scalar: not yet evaluated
boundary term: not yet evaluated
metric-limit status: not yet evaluated
diffeomorphism/relabeling status: not yet evaluated
mode count: not yet evaluated
hyperbolicity status: not yet evaluated
source-ledger status: not yet evaluated
epsilon status: not yet evaluated
kill condition: silently modifies closed local gravitational equations
next test: route to Lambda/dark-sector/large-scale behavior if local branch stays closed
```
