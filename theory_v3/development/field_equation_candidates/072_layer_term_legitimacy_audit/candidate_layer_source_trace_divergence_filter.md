# candidate_layer_source_trace_divergence_filter — Result Note

## Result

`candidate_layer_source_trace_divergence_filter.py` applies source, trace, and divergence role filters to `D_layer`.

The source incidence residual is:

```text
S_M*(i_A + i_layer_src - 1)
```

The trace incidence residual is:

```text
T_zeta*(i_B + i_layer_trace + i_res - 1)
```

The safe source and trace routes require the layer not to carry ordinary source or trace payload.

## Main Finding

The script confirms that a legitimate `D_layer` cannot be:

```text
ordinary source carrier;
trace payload carrier;
residual reentry path;
repair divergence current.
```

The allowed role is much narrower:

```text
D_layer may only be a boundary-divergence component if geometrically derived.
```

This is not a proof of that role. It is a filter.

## Rejected Routes

The rejected routes are explicit:

```text
layer source:
  residual = S_M

layer trace:
  residual = T_zeta

residual reentry:
  residual = T_zeta

repair divergence:
  D_layer chosen after the fact to cancel parent divergence.
```

## Boundary

This script does not prove boundary-divergence legitimacy. It leaves an open obligation:

```text
derive D_layer as boundary-divergence component without source/trace payload.
```

## Steering Consequence

Proceed to `candidate_layer_legitimacy_route_classifier.py`.

At this point, the group has enough filters to classify the route: diagnostic insertion is rejected, geometric `D_layer` remains possible only as theorem target, and legitimacy is not yet established.
