# Einstein-Hilbert Origin Test 122: Torsion Gate and Extra Field Test

## Purpose

This report tests whether metric compatibility alone removes torsion.

It does not. Torsion is an extra connection field unless the framework imposes
a torsion-free condition or supplies dynamics for torsion.

## Validated Checks

- nonzero torsion example is metric-compatible: passed
- torsion component is nonzero when tau is nonzero: passed
- torsion-free gate removes torsion parameter: passed
- totally antisymmetric torsion drops from symmetric velocity contraction: passed
- metric interval independent of torsion parameter: passed

## Metric-Compatible Torsion Example

Use a flat Euclidean metric and define:

```text
Gamma^a_bc = tau epsilon_abc.
```

SymPy verifies:

```text
nabla_c delta_ab = 0.
```

So this connection is metric-compatible.

But its torsion is:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

For example:

```text
T^0_12 = 2 tau.
```

Therefore metric compatibility does not force torsion to vanish.

## Torsion-Free Gate

The condition:

```text
T^0_12 = 0
```

forces:

```text
tau = 0.
```

## Interpretation

The Einstein-Hilbert chain assumes the Levi-Civita connection, which is both
metric-compatible and torsion-free. Proof `115` showed that these conditions
select the connection uniquely. This proof shows that torsion-free is a real
gate, not a consequence of metric compatibility by itself.

If the vacuum ontology permits independent rotational or defect-like connection
structure, the natural completion may be Einstein-Cartan-like rather than pure
Einstein-Hilbert. If no such field is present, the torsion-free gate is the
clean route back to EH.
