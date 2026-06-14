# Metric Branch vs Finsler Gap

## Status

Open rigor/ontology obligation.

This note records a load-bearing scope issue in the field-equation proof's
kinematic layer. It is not a coefficient problem and it does not change the
closed metric-branch result. It does limit what is currently derived from P2.

## The Gap

P2 says the vacuum substance's configuration is what clocks and rods read.
That licenses the statement that local vacuum configuration assigns rates and
lengths to directions.

It does not, by itself, force those assignments to come from a symmetric
bilinear form. A general direction-dependent norm is possible. In geometric
language, P2 alone leaves Finsler-type structures open.

The field-equation proof needs a stronger statement before invoking the
Fierz-Pauli spin-2 classification:

```text
local interval is quadratic
  => polarization identity
  => symmetric nondegenerate rank-2 tensor g_ab
  => perturbation h_ab is a symmetric spin-2 field
```

That quadratic-line-element premise is currently supplied by the SR import:
zero-source vacuum is Minkowski, and admissible weak configurations are taken
inside the local Lorentz/quadratic branch.

## What Is Still Valid

Within the metric/SR branch, the proof can proceed:

- K1 supplies a symmetric tensor perturbation `h_ab`;
- K2 supplies universal matter coupling to the shared metric structure;
- K3 supplies relabeling gauge freedom;
- the Fierz-Pauli/Deser route then applies to the spin-2 field.

The result is still a clean closure of the metric branch. The correction is
about novelty and scope, not about whether the branch reproduces GR.

## What Is Not Yet Derived

The current postulates do not yet prove:

- that all admissible vacuum clock/rod structures must satisfy the
  parallelogram law;
- that the local line element must be quadratic rather than Finslerian;
- that non-quadratic direction-dependent response is dynamically excluded;
- that a microscopic vacuum substrate coarse-grains only to metric geometry.

Those would require an additional theorem or postulate, such as a
quadratic-response selector, local isotropic calibration coherence strong
enough to imply the parallelogram law, or a stability/causality gate that kills
Finsler branches.

## Honest Wording

The field-equation proof should not say:

```text
P2 implies a symmetric nondegenerate rank-2 tensor.
```

It should say:

```text
P2 identifies clock/rod readings with vacuum configuration. Together with
the SR import of a local quadratic Lorentz interval, this restricts the proof
to the metric branch, represented by a symmetric nondegenerate rank-2 tensor.
```

## Work Target

Build a branch-selector trial:

```text
Question:
  Can P1-P6 plus SR calibration coherence derive the parallelogram law
  or otherwise exclude Finsler-type local response?

Pass:
  quadratic metric structure becomes a theorem of the ontology.

Fail:
  metric structure remains an explicit SR-compatible branch assumption,
  and Finsler-like alternatives become a separate candidate family.
```
