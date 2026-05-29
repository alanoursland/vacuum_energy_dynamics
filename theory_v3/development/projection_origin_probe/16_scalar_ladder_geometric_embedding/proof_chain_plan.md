# Scalar Ladder Geometric Embedding Proof Chain Plan

## Purpose

This folder tests and records the correct embedding of the original scalar
admissibility/projection ladder inside the later directional interval geometry.

The goal is not to re-prove the original ratio ladder. The goal is to prevent a
wrong promotion of that ladder. The scalar ladder is powerful and real, but it
is only the isotropic / trace / monopole projection sector of the full
directional metric branch.

## Strategy

The chain separates four claims:

1. **Trace projection**
   A scalar interval response can encode the isotropic trace of a symmetric
   bilinear form.

2. **Traceless and shear invisibility**
   A scalar trace/monopole projection cannot recover shear, off-diagonal, or
   transverse-traceless data.

3. **Monopole boundary role**
   The scalar boundary-flux ladder naturally matches the monopole / l=0 sector
   of boundary field data. Higher multipoles and tensor modes require extra
   directional probes.

4. **Rank bookkeeping**
   In dimension `m`, a symmetric metric on the relevant boundary/tangent space
   has `m(m+1)/2` components. A scalar trace channel has one. The rank gap is
   therefore `m(m+1)/2 - 1` per mode.

## Expected Output

The expected conclusion is conditional:

```text
The scalar admissibility ladder is the trace/monopole shadow of the directional
metric branch. It correctly captures scalar admissibility, flux closure, and the
Newtonian boundary charge channel. It does not by itself reconstruct full tensor
boundary data, shear response, TT radiation, or off-diagonal metric components.
Those require directional interval probes and polarization reconstruction.
```

## Proof Script Style

Each `make_*.py` script performs exact SymPy checks for the algebraic,
combinatorial, or angular-average claim it reports, then writes the
corresponding Markdown file. The folder is a placement and embedding proof, not
another derivation of the original `r_k` ladder.
