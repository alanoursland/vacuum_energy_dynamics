# Nonlinear Constraint Closure Proof Chain Plan

## Purpose

This folder tests the nonlinear closure pressure that appears after the scalar
boundary ladder, Weyl-sector audit, matter-action gate, and boundary symplectic
closure have been separated.

The question is not:

```text
Can the scalar projection ladder derive full nonlinear GR by itself?
```

The question is narrower:

```text
Once the theory has committed to a metric interval structure, universal stress
coupling, boundary Hamiltonian generators, and massless spin-2 gauge redundancy,
which nonlinear constraint architecture closes without producing extra un-routed
degrees of freedom?
```

## Strategy

The proof scripts are symbolic consistency checks. They do not prove a global
existence theorem for GR. They verify the algebraic skeleton behind the usual
closure pressure:

```text
linear spin-2 gauge redundancy
  -> constrained phase-space count
  -> Bianchi/divergence identity
  -> stress conservation compatibility
  -> Hamiltonian + momentum constraints
  -> hypersurface-deformation closure shape
  -> higher-derivative branches introduce extra initial data
  -> massive or gauge-broken branches add extra modes
  -> Einstein branch is the minimal known closure.
```

## Scope

The folder proves:

```text
The Einstein/Hamiltonian constraint architecture is the minimal closure target
under the assumed gates.
```

The folder does not prove:

```text
The projection ladder alone derives nonlinear GR.
```

It also does not prove:

```text
All conceivable modified gravities are impossible.
```

Instead it records which assumptions are doing work:

```text
metric interval structure,
diffeomorphism redundancy,
second-order locality,
universal stress coupling,
boundary differentiability,
and no additional independent field branches.
```
