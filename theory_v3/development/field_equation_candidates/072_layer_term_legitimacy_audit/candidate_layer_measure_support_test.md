# candidate_layer_measure_support_test — Result Note

## Result

`candidate_layer_measure_support_test.py` audits endpoint locality and support diagnostics for possible layer profiles.

It reports that `w` and `eta_like` have endpoint value and slope silence:

```text
value(-1)=0
value(1)=0
slope(-1)=0
slope(1)=0
```

while a constant layer fails endpoint locality because:

```text
value(-1)=1
value(1)=1
```

## Main Finding

Endpoint-local profiles can be useful necessary diagnostics for a layer component. They can reject obviously nonlocal/background candidates such as a constant layer.

But the script correctly states the core limitation:

```text
endpoint locality is not D_layer legitimacy;
endpoint silence is not a covariant boundary theorem;
passing support checks does not promote old diagnostics into D_layer.
```

This is important because previous finite-layer work produced many useful support and weighted-neutrality diagnostics. Group 72 must preserve them as constraints, not convert them into field-equation components.

## Rejected Routes

The script rejects:

```text
constant layer;
diagnostic promotion by endpoint support;
support as theorem.
```

## Boundary

No boundary/layer measure is derived. No covariant component status is proven.

## Steering Consequence

Proceed to `candidate_layer_source_trace_divergence_filter.py`.

After endpoint support, the next necessary filter is whether the layer carries source, trace, or repair-divergence payloads.
