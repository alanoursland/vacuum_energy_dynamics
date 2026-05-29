
# Boundary Symplectic Closure Proof Chain Plan

## Purpose

This folder tests the boundary phase-space layer that sits beyond scalar
Gauss-charge accounting.

Earlier folders established that the scalar `r_k` ladder captures a
trace/monopole boundary-admissibility sector, and that Weyl/TT data requires
extra tensorial boundary information. This folder asks how that extra boundary
information is organized dynamically.

Target distinction:

```text
Coulombic/constraint boundary charge
  !=
radiative/symplectic boundary flux
```

The boundary is not merely a static ledger of enclosed scalar charge. For a
field theory with propagating degrees of freedom, the boundary also carries a
symplectic flux ledger: canonical pairs, shear/news data, Hamiltonian generator
boundary terms, and memory shifts.

## Strategy

### Batch A: Variational boundary terms

Show in a simple scalar model that integration by parts produces a bulk field
equation and a boundary potential.

### Batch B: Symplectic current and canonical pairs

Build the phase-space 2-form from the boundary potential. Check antisymmetry,
canonical-pair structure, and conservation when the equations of motion hold.

### Batch C: Hamiltonian generators and integrability

Show that a Hamiltonian generator is differentiable only after its boundary
variation is accounted for. Check integrability for charges and exhibit a
non-integrable flux witness.

### Batch D: Coulombic charge versus radiation

Separate static scalar/monopole charge from radiative symplectic flux. This
formalizes why the scalar boundary ledger is blind to the Weyl/TT sector.

### Batch E: Closure status

Record the conditional conclusion: boundary symplectic closure is the dynamic
extension of the boundary ledger. It is required for Weyl/TT/radiative sectors
and does not reduce to the scalar `r_k` admissibility ladder.

## Expected conclusion

```text
Scalar boundary charge is a constraint ledger.
Boundary symplectic flux is the dynamical ledger.
```
