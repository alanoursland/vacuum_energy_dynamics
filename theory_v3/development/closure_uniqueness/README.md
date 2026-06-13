# Closure Uniqueness Program

## Purpose

This directory holds the in-house proof program for the largest remaining
field-equation rigor debt: replacing the Deser 1970 self-coupled
spin-2 closure citation.

Status: started, not retired. The first forge-checked rung is:

```text
vacuum_forge/src/field_equation_trials/018_closure_uniqueness/closure_step_1.py
```

## What Must Eventually Be Proved

The theorem VED needs is:

> Given a local, two-derivative, massless spin-2 field on Minkowski
> space with relabeling gauge symmetry, universal coupling to stress,
> no extra propagating fields, and self-energy sourcing at the same
> universal coupling, the unique consistent nonlinear closure is the
> Einstein-Hilbert response, up to a cosmological term and inert
> Gauss-Bonnet in four dimensions.

This is structural and coefficient-free. The coefficients have already
been fixed elsewhere by the static bookkeeping anchor and P9. But the
proof's anti-circularity presentation depends heavily on showing that
the spin-2 closure theorem is mathematics, not imported GR as physics.

## Phase Plan

1. **First obstruction: conservation forces self-coupling.**

   The linear Fierz-Pauli operator has an identically conserved left
   side. Therefore its source must be conserved. But matter stress alone
   is not conserved once matter exchanges energy-momentum with the spin-2
   field. A compensating field stress is forced.

   Status: completed as the first forge-checked rung in 018.

2. **First self-coupling step.**

   Compute or organize the field stress that must be added at the next
   order, and show how it sources the same spin-2 field at the universal
   coupling.

3. **Iteration structure.**

   Show that repeating the consistency requirement reconstructs the
   nonlinear metric variables rather than an arbitrary tower of unrelated
   terms.

4. **First-order/Palatini closure.**

   Use a first-order form to make the finite closure transparent: the
   iterative self-coupling is equivalent to replacing the background
   density/connection structure with the dynamical metric density and
   connection.

5. **Uniqueness assumptions audit.**

   State exactly where locality, two-derivative order, no extra fields,
   universal coupling, and gauge consistency enter.

6. **Retirement decision.**

   Only after the full closure is reproduced in-house should
   `04_field_equations/05_open_obligations.md` move the Deser citation
   from active rigor debt to retired rigor debt.

## Boundary

This program does not change the field equations, their normalization,
or any observational coefficient. It strengthens the proof's independence
from an external spin-2 closure citation.

