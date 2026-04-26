# VacuumForge Overview

VacuumForge is a symbolic research workbench for developing and testing candidate mathematical structures in a vacuum-based theory of gravity.

The project exists because the theory has reached a point where verbal postulates are no longer enough. Several weak-field gravitational results can be recovered or provisionally recovered, but a central mathematical gap remains: deriving the equal-response relationship between temporal and spatial metric response from the theory's own vacuum ontology rather than assuming it.

VacuumForge is designed to help with that gap.

## The Core Problem

In the framework's weak-field metric language, the temporal and spatial scale factors are written as

```math
A(r) = \sqrt{-g_{00}},
```

```math
B(r) = \sqrt{g_{ii}}.
```

The redshift and time-dilation derivations constrain the temporal scale factor:

```math
A(r) \approx 1 + \frac{\Phi(r)}{c^2}.
```

The spatial scale factor remains underdetermined:

```math
B(r) \approx 1 - \gamma_v \frac{\Phi(r)}{c^2}.
```

Observation requires

```math
\gamma_v = 1.
```

In the theory's preferred formulation, this is the reciprocal-scale condition:

```math
A(r)B(r)=1.
```

The open question is why this should follow from the vacuum postulates.

VacuumForge focuses on this question by working in logarithmic mode variables:

```math
a = \ln A,
```

```math
b = \ln B,
```

```math
\kappa = \frac{a+b}{2},
```

```math
\sigma = \frac{a-b}{2}.
```

In this language, reciprocal scaling is equivalent to

```math
\kappa = 0.
```

The theory needs to show that static gravitational exchange excites the shear mode `sigma`, but not the conformal cell mode `kappa`.

## What VacuumForge Does

VacuumForge helps define and test candidate symbolic structures for vacuum response.

It can be used to explore questions such as:

- What source rules make local vacuum exchange trace-free?
- What source rules distinguish exchange from creation?
- What energy functionals make unsourced `kappa` relax to zero?
- What assumptions are sufficient to derive `A B = 1`?
- What assumptions accidentally insert `A B = 1` by hand?
- Which candidate structures recover `gamma_v = 1`?
- Which candidate structures also recover `beta = 1`?
- Which structures fail, and why?

VacuumForge is not intended to replace physical reasoning. It is intended to make the reasoning executable.

## Why Symbolic Software Is Needed

The equal-response problem is algebraically delicate.

Small choices about signs, logarithms, reciprocal scale factors, source decomposition, expansion order, or coordinate conventions can change the conclusion. A candidate equation may look conceptually natural while secretly assuming the result it is meant to derive.

VacuumForge reduces that risk by keeping the symbolic ledger visible.

It allows candidate structures to be written explicitly, expanded, simplified, varied, solved, and checked against required consequences. This helps separate three cases:

1. A result genuinely follows from the candidate structure.
2. A result follows only after adding an extra assumption.
3. A result was already inserted into the equations in disguised form.

The purpose is disciplined exploration, not automated theory generation.

## Reduced Field-Equation Laboratory

VacuumForge begins as a reduced field-equation laboratory.

The first target is not the full theory of gravity. The first target is the static weak-field mode sector.

A minimal symbolic model might contain equations of the form

```math
\mathcal{D}_\sigma \sigma = J_\sigma,
```

```math
\mathcal{D}_\kappa \kappa = J_\kappa.
```

The desired static-exchange result is

```math
J_\kappa = 0 \quad \Rightarrow \quad \kappa = 0,
```

under appropriate boundary conditions, while

```math
J_\sigma \neq 0 \quad \Rightarrow \quad \sigma \neq 0.
```

This would imply

```math
A B = 1,
```

and therefore

```math
\gamma_v = 1.
```

VacuumForge is meant to help search for source operators, energy functionals, and mode equations that produce this structure naturally.

## Exchange vs Creation

A central distinction explored by VacuumForge is the difference between local vacuum exchange and vacuum creation.

The candidate structural principle is:

```math
\text{local exchange} \Rightarrow J_\kappa = 0,
```

while

```math
\text{vacuum creation} \Rightarrow J_\kappa \neq 0.
```

In words:

- Static gravity proceeds by exchange.
- Exchange is trace-free in metric mode space.
- Cosmic expansion proceeds by creation.
- Creation is traceful.

If this distinction can be derived from deeper vacuum structure, then the theory can derive equal-response rather than adopting it as a provisional assumption.

VacuumForge provides the symbolic environment for testing that possibility.

## Planned Capabilities

Early versions of VacuumForge should support:

- symbolic definitions of scale factors and mode variables;
- transformation between `A, B`, `a, b`, and `kappa, sigma`;
- source decompositions into trace and shear components;
- construction of candidate quadratic and higher-order energy functionals;
- symbolic minimization and Euler-Lagrange variation;
- weak-field expansions in powers of `Phi/c^2`;
- checks for reciprocal scaling;
- extraction of weak-field parameters such as `gamma_v` and `beta`;
- tests for whether a candidate equation derives or assumes the target result.

Later versions may support:

- 3+1-dimensional generalizations of the mode decomposition;
- gauge and coordinate-condition checks;
- symbolic PPN comparisons;
- candidate wave equations and polarization analysis;
- source-response equations for matter distributions;
- automated search over families of candidate source laws or energy functionals.

## What VacuumForge Is Not

VacuumForge is not a completed gravitational theory.

It is not a numerical relativity code.

It is not a replacement for physical interpretation.

It is not an oracle that can determine which theory is true.

VacuumForge is a symbolic tool for theory development. It helps identify which mathematical structures are consistent with the framework's postulates and which ones fail.

## Long-Term Goal

The long-term goal of VacuumForge is to support the construction of genuine vacuum field equations.

A mature version of the theory would need equations that map

```math
\text{matter-energy distribution}
\rightarrow
\text{vacuum configuration}
\rightarrow
\text{metric response}
\rightarrow
\text{motion, waves, and cosmology}.
```

VacuumForge starts with the smallest high-value piece of that problem: the equal-response wall.

If it can help identify the structural reason that static exchange forces `kappa = 0`, then it will have converted one of the framework's most important provisional assumptions into a derivable result.
