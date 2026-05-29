# Weyl Sector Boundary Gate — Proof Chain Plan

## Purpose

This folder tests the next scope boundary after the scalar projection and GR boundary comparison work.

The scalar ladder and its `r_k` coefficient live in the scalar boundary ledger: trace, monopole, finite flux, and Newtonian/Poisson reduction. The question here is what this scalar ledger cannot see.

The target result is not a derivation of the Weyl sector. The target is a gate:

```text
scalar boundary flux / trace data cannot reconstruct the traceless Weyl / TT / radiative sector.
```

The folder proves this by simple symbolic and representation checks:

- trace projection kills traceless tensors,
- scalar monopole averaging kills higher multipoles,
- TT tensors have zero trace and zero longitudinal divergence,
- scalar conserved charge is distinct from radiative tensor flux,
- Weyl-like tidal matrices are traceless and therefore invisible to trace-only ledgers,
- full boundary data requires tensor/shear-sensitive directional probes.

## Planned batches

### Batch A — Tensor decomposition and trace blindness

Show that any symmetric tensor decomposes into trace plus traceless part, and that scalar trace projection loses the traceless part.

### Batch B — Boundary scalar ledger and multipoles

Show that scalar monopole/flux data keeps only total charge and angular average, while higher multipoles and shear data require more boundary modes.

### Batch C — TT and Weyl witnesses

Show that TT/radiative tensors and traceless tidal matrices evade trace-only scalar probes while still carrying nonzero invariant content.

### Batch D — Boundary data requirements

Count the missing tensor components and classify what data must be added: directional probes, tensor boundary metric/shear data, or boundary symplectic/radiative flux.

## Expected conclusion

The scalar projection ladder is a solved scalar boundary/admissibility object. It is not supposed to contain the whole gravitational field. It captures the trace/monopole/Newtonian ledger. The Weyl/TT sector is precisely the part that requires tensorial boundary data beyond `r_k`.
