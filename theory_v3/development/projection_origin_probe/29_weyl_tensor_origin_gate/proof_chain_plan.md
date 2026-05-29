# Weyl Tensor Origin Gate — Proof Chain Plan

## Purpose

The earlier `weyl_sector_boundary_gate` showed a negative result:

```text
scalar r_k boundary/admissibility data sees only the trace / monopole / Newtonian sector.
```

This folder asks the next positive-but-bounded question:

```text
What additional structure is sufficient to recover traceless shear / Weyl-like tensor data?
```

The target is not to derive full nonlinear radiative GR. The target is to separate three layers:

```text
directional quadratic interval probes -> symmetric metric perturbation data;
trace removal -> traceless shear data;
transport/constraint closure -> free Weyl / TT dynamics.
```

## Strategy

Use small SymPy witnesses to check:

1. A directional quadratic response `Q(v)=v^T H v` reconstructs the full symmetric matrix `H` by polarization.
2. Trace projection extracts only the isotropic scalar component.
3. The traceless part is nonzero data invisible to the scalar trace.
4. The traceless part carries shear/eigenvalue shape data.
5. A Newtonian Hessian has trace equal to source density while its trace-free part gives tidal/Weyl-like data.
6. In vacuum, the Hessian trace can vanish while the trace-free tidal tensor remains nonzero.
7. TT tensors are trace-free and divergence-free witnesses of radiative data.
8. Directional probes detect TT/shear components that scalar trace misses.
9. Local directional metric data does not itself supply propagation law; Weyl dynamics requires transport, constraints, and boundary symplectic data.

## Expected status

Closed by this folder:

```text
Directional quadratic probes are sufficient to reconstruct local symmetric metric/shear data.
Scalar trace data is insufficient.
Trace-free Hessian/tidal witnesses exist even when scalar trace vanishes.
TT witnesses are non-scalar data.
```

Still imported after this folder:

```text
hyperbolic propagation of TT data;
full nonlinear constraint closure;
boundary symplectic radiative dynamics;
Einstein equation / Bianchi structure.
```

## Reading anchors

Use:

```text
6_tracefree_tidal_vacuum_witness.md
10_directional_probe_recovers_traceless_matrix_entries.md
13_tt_witness_trace_divergence_free.md
17_transport_needed_for_weyl_dynamics.md
20_weyl_tensor_origin_gate_conclusion.md
```
