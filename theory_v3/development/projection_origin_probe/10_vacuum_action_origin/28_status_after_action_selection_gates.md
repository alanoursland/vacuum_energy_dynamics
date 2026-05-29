# Vacuum Action Origin: Status After Proofs 24-27

## What This Batch Adds

Proofs `24` through `27` test the action-selection gates after the
connection/curvature origin step.

## Proof 24: Second-Order Metric Equation Gate

Proof `24` validates in the conformal EH strain sector:

```text
L = 6 exp(2s)(s')^2
delta L / delta s = -12 exp(2s)[s'' + (s')^2].
```

The field equation contains no third or fourth derivatives.

This supports:

```text
first-derivative connection strain -> second-order metric equation.
```

## Proof 25: Scalar Curvature Contraction Gate

Proof `25` validates:

```text
R' = J^T R J
g'^(-1) = J^(-1) g^(-1) J^(-T)
trace(g'^(-1)R') = trace(g^(-1)R).
```

So the relabeling-invariant linear curvature scalar is:

```text
R = g^ab R_ab.
```

## Proof 26: Curvature-Squared Exclusion

Proof `26` validates in a conformal model:

```text
sqrt(g)R^2 = 36[s'' + (s')^2]^2
```

whose Euler-Lagrange equation contains:

```text
72 s''''.
```

It also validates the momentum-order gate:

```text
R^2, Ricci^2 -> k^4 h
EH           -> k^2 h.
```

So generic curvature-squared terms fail the local second-order metric-equation
gate.

## Proof 27: Lambda Baseline Energy

Proof `27` validates:

```text
L_Lambda = -2 Lambda sqrt(g)
```

varies as a metric-proportional term.

It also validates the Newtonian branch:

```text
Delta[-Lambda r^2/6] = -Lambda.
```

So Lambda is baseline vacuum energy, not connection strain. It is compatible
with the gates but separate from the inverse-square boundary-flux bridge.

## Current Impact

The vacuum-action path now reaches the same selection structure as the
Einstein-Hilbert origin tests, but from inside the action-origin chain:

```text
metric self-reference
  -> local comparison connection
  -> Levi-Civita branch when torsion is absent
  -> curvature as invariant connection field strength
  -> relabeling-invariant linear scalar g^ab R_ab
  -> first-derivative Gamma-Gamma strain plus boundary flux
  -> second-order metric equation
  -> exclusion of generic curvature-squared corrections
  -> Lambda as separate baseline energy branch.
```

This is a strong conditional derivation of the Einstein-Hilbert action
structure from the vacuum-action gates.

## Remaining Gap

The remaining open point is not algebraic. It is physical selection:

```text
why must the vacuum ontology choose exactly these gates?
```

The most important remaining selectors are:

```text
1. torsion-free branch versus torsion defect branch;
2. four-dimensionality as a vacuum-state count or external input;
3. whether Lambda is zero, nonzero, or dynamically relaxed;
4. whether the projection-origin boundary flux fixes the GHY boundary term
   beyond the conformal and scalar analogies;
5. whether matter stress-energy is derived from vacuum perturbation structure
   or imported as an external source.
```

## Next Proof Targets

The next useful batch should decide whether this folder is ready for a closure
report or needs one more selector round:

```text
29. torsion-free branch selector summary;
30. dimensionality selector gate;
31. Lambda relaxation/baseline alternatives;
32. projection-boundary to GHY stronger matching table;
33. vacuum action origin conclusion.
```
