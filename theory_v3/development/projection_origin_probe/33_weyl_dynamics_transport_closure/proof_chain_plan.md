# Weyl Dynamics Transport Closure — Proof Chain Plan

## Purpose

This folder continues after:

```text
weyl_sector_boundary_gate
weyl_tensor_origin_gate
radiative_boundary_memory_gate
boundary_symplectic_closure
```

The previous folders established that scalar boundary data is blind to Weyl/TT
structure and that directional quadratic probes can recover local traceless
tensor data. This folder tests the next bridge:

```text
local traceless tensor data + transport/constraint closure -> radiative Weyl/TT dynamics.
```

## What this folder should close

It should validate finite algebraic witnesses for:

```text
TT trace-free and transverse plane waves;
wave transport preserving TT structure;
plus/cross polarization basis;
Weyl electric/magnetic transport toy closure;
Ricci/scalar-trace blindness to free Weyl waves;
news, memory, and flux as tensor radiative boundary data;
local tensor data not being sufficient without a transport law.
```

## What this folder must not claim

It must not claim a full nonlinear derivation of GR. It also must not claim that
the scalar `r_k` ladder generates Weyl dynamics by itself.

The correct conclusion is conditional and structural:

```text
directional probes supply local traceless tensor data;
hyperbolic transport and constraint closure supply the dynamical Weyl/TT sector.
```

## Scripts

The scripts in this folder are SymPy witness checks. They validate algebraic
statements about traces, divergences, wave equations, polarization bases,
energy/flux witnesses, and closure dependencies.
