
# Quadratic Response Physical Selector — Proof Chain Plan

## Purpose

The previous `quadratic_response_selector` folder proved the formal metric gate:
exact quadratic/parallelogram response is equivalent to symmetric bilinear metric
reconstruction. This folder asks the next, more physical question:

```text
What conditions would actually select the exact quadratic branch rather than a
Finsler-like, quartic, scale-dependent, or nonlinear directional response?
```

The goal is not to claim that nonquadratic response is mathematically impossible.
The goal is to separate:

```text
metric branch: exact quadratic, scale-independent, polarization-stable response;
nonmetric branch: higher directional response that must be routed as extra
structure rather than hidden inside a metric tensor.
```

## Proof strategy

The scripts test the following selector pressures:

1. parallelogram identity;
2. degree-two homogeneity;
3. scale-independent effective metric/Hessian;
4. polarization path independence;
5. linear superposition of response channels;
6. calibration coherence under rescaling;
7. universal null-cone preservation;
8. Finsler/fundamental-tensor direction dependence;
9. exact quadratic versus local Hessian approximation;
10. nonlinear constitutive response and superposition failure;
11. reciprocity/parity exclusion of odd response;
12. coefficient-level branch selection.

## Expected conclusion

If exact parallelogram law, degree-two homogeneity, scale-independent calibration,
polarization stability, universal null-cone ownership, and linearized
superposition are imposed, the quartic/Finsler residual coefficients are forced
to vanish and the response collapses to the metric branch.

If those conditions are not imposed, nonquadratic response is allowed but must be
routed as an explicit additional medium/Finsler/constitutive branch. It cannot be
quietly treated as a pseudo-Riemannian metric.
