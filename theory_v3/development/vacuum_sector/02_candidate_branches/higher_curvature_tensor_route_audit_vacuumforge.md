# VacuumForge Higher-Curvature Tensor-Route Audit

## Purpose

This report discharges the route-audit obligation opened by the
higher-curvature scalar prototype. It is a tensor-route classifier, not a full
new covariant derivation.

This report depends on:

```text
higher_curvature_scalar_prototype_006
```

It satisfies:

```text
higher_curvature_tensor_route_audit_required_006
```

## Symbolic Checks

The inert/topological proxy leaves the TT symbol unchanged:

```text
EH TT symbol      = k**2
inert correction  = 0
total TT symbol   = k**2
```

The scalaron/f(R)-type route carries a scalar scale and weak-field face:

```text
mass^2  = 1/(6*a)
range^2 = 6*a
alpha   = 1/3
```

This is ghost-safe only after mode routing. Under the already adopted
GR-branch closure, the later P7prime gate still blocks the route unless that
postulate is explicitly reopened.

The spin-2/Weyl-type TT propagator decomposes as:

```text
symbol      = b*k**4 + k**2
propagator  = -1/(k**2 + 1/b) + k**(-2)
massive pole coefficient = -1
```

In the normalized partial-fraction form, the massive pole has negative
coefficient. This is the ghost route identified in the prior G20 gate.

## Route Audit

| route | representative terms | symbolic result | imported context | disposition | epsilon status | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
| inert_topological | Gauss-Bonnet in 4D, total derivatives, field redefinitions, boundary-local completions | no bulk TT symbol change in the inert proxy | topological or pure-boundary terms may change bookkeeping but do not license a bulk residual | retained only as epsilon = 0 equivalent or boundary-quarantined | not controlled epsilon != 0 | prove inertness or boundary quarantine for each concrete term |
| scalaron_fR | R + a R^2 with a > 0, plus inert topological terms | mass^2 = 1/(6a), range^2 = 6a, weak-field alpha = 1/3 in the imported G20 route | G20 treats this as ghost-safe after mode routing; E3 later kills it under adopted P7prime through mandatory scalaron hair unless P7prime is reopened | routed but not licensed under the current adopted closure | not controlled epsilon != 0 under current postulate set | only reopen through an explicit P7prime scope appeal plus weak-field/source ledger |
| spin2_weyl | Weyl^2, Ricci^2 combinations that reach the TT propagator | quartic TT propagator has a massive pole with negative residue | G20 kills quartic TT kinetic content as a ghost in the dynamical radiative sector | fails as controlled local higher-curvature residual unless reduced to inert/topological combination | failed residual route | do not reuse except as a killed route or after proving degeneracy/topological cancellation |
| generic_mixed_curvature_squared | arbitrary R^2, Ricci^2, Riemann^2 mixture | must decompose into inert, scalaron, and spin-2 pieces before evaluation | generic labels hide which gate is active; the scalar prototype alone is insufficient | not evaluated until decomposed | underdetermined without decomposition | decompose concrete invariant into topological, scalaron, and spin-2 sectors |

## Current Conclusion

The higher-curvature local residual branch still does not supply a controlled
`epsilon != 0` route. The inert/topological sector is not a bulk residual. The
spin-2/Weyl sector fails by the ghost route unless it degenerates to an inert
combination. The scalaron/f(R)-type sector is the only non-ghost local
higher-curvature route, but under the already adopted project closure it is
blocked by P7prime/weak-field routing unless that appeal is explicitly reopened.

## Classification

```text
result type: tensor-route audit / higher-curvature branch classifier
scope: local curvature-squared residual routes after scalar prototype
conclusion: no higher-curvature route is currently licensed as controlled epsilon != 0
non-conclusion: no new covariant tensor theorem is proved here; prior G20/E3 closures are imported as route context
```

The next technical target is to return to branch selection rather than keep
decorating the killed higher-curvature branch:

```text
open the Lambda baseline folder and separate baseline-selection questions from
local higher-curvature strain residuals.
```
