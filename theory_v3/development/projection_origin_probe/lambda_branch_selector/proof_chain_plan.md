# Lambda Branch Selector Proof Chain Plan

## Purpose

This folder tests the selector gate left open after the scalar boundary bridge,
metric lift, quadratic response selector, torsion exclusion, and dimension
selector:

```text
Why the asymptotically-flat / zero-Lambda branch, and what exactly changes when
Lambda is nonzero?
```

The goal is not to prove `Lambda = 0` from pure ontology. The goal is to make
explicit which parts of the existing proof chain select the zero-Lambda branch,
which parts merely permit a cosmological baseline, and what extra structure is
required for a relaxation mechanism.

## Strategy

The chain separates four questions that are often conflated:

1. **Local strain versus baseline vacuum density**
   A cosmological term is a volume baseline term, not connection strain.

2. **Localized flux versus global/asymptotic curvature branch**
   Ordinary localized sources produce finite Gauss flux. A nonzero uniform
   baseline produces flux growing with radius in the Newtonian reduction.

3. **Einstein/Lovelock allowance versus branch selection**
   The cosmological term is allowed by the same metric action class but is not
   fixed by local spin-2 polarization counting or scalar admissibility.

4. **Relaxation versus tuning**
   Driving an effective Lambda toward zero requires an additional routed
   relaxation channel or global boundary condition; it does not follow from the
   scalar projection ladder alone.

## Expected Output

The expected conclusion is conditional:

```text
The zero-Lambda branch is selected by asymptotically flat inverse-square
boundary normalization and finite conserved flux. Nonzero Lambda is an allowed
vacuum baseline branch of the metric action, but it changes the asymptotic
class and requires separate routing or a relaxation mechanism if it is to be
explained dynamically.
```

## Proof Script Style

Each `make_*.py` script performs exact SymPy checks for the algebraic or
classification claim it reports, then writes the corresponding Markdown file.
The scripts validate the formal gates only; they do not claim to solve the
observed cosmological constant problem.
