# Quadratic Response Selector 25: Downstream GR Gate Dependency

## Purpose

This report prevents downstream geometric gates from being read as independent
proofs of the quadratic response primitive.

## Dependency Table

| Downstream Gate | Dependency |
|---|---|
| polarization reconstruction | requires exact quadratic response |
| metric compatibility | requires a metric tensor to preserve |
| Levi-Civita minimal branch | requires metric compatibility plus torsion-source absence |
| stress variation | requires symmetric metric variation |
| EH+GHY action gate | requires metric/diffeomorphism action class |

## Interpretation

The quadratic response selector is upstream of the usual metric geometry gates.
If it fails, the correct continuation is not EH geometry by default but a
nonmetric or explicitly routed higher-response branch.
