# Covariant Lift of the C2/C3 Static Bookkeeping Sector

## Purpose

This directory holds the final phase of the targeted covariant-lift
program: the covariant lift of the static bookkeeping sector (Lemma 1,
Lemma 2, Theorem 1 of `04_field_equations/proof.md`), which was proved
in reduced variables (areal gauge, staticity assumed) in trials C2/C3.

Current status: completed. See `static_covariant_lift_note.md` and the
forge script:

```text
vacuum_forge/src/field_equation_trials/019_static_covariant_lift/static_covariant_lift.py
```

## Scope

Four statements lift the reduced sector to the closed parent:

1. **Flux law (Lemma 1).** The covariant tt-equation is exactly the
   areal flux law with the gauge-invariant Misner–Sharp mass
   $m = (c^2 r/2G)\,(1 - (\nabla r)^2)$ as the enclosed source:
   $m'(r) = (4\pi r^2/c^2)\,\rho$, identically and nonperturbatively.

2. **P7′ shadow (Lemma 2).** $AB = 1$ is the chart-free statement
   $(\nabla r)^2 = -\xi^2/c^2$ (areal-gradient norm equals static
   Killing norm). The C3 t–r block identity is verified in an arbitrary
   radial gauge, where the shadow variable is the invariant
   $a b / R'^2$.

3. **Bootstrap equation (Theorem 1).** The C2 self-coupling equation
   $\Delta_{\rm areal} s = -(s')^2$ (equivalently
   $\Delta_{\rm areal} A = 0$) is the covariant vacuum tt-equation on
   the compensated branch: $d/dr[r^2 G^t{}_t] = r\,\Delta_{\rm areal}A$,
   and the two solution families coincide under asymptotic flatness.
   The angular equation is implied on the solution (Bianchi).

4. **Staticity derived (Birkhoff-type).** In the spherical vacuum
   sector, $G_{tr} = \dot B/(rB)$ forces the spatial mapping static;
   the tt-equation fixes it; the t–r identity forces $A = h(t)/B$, and
   $h(t)$ is pure time relabeling (equal Kretschmann invariant with the
   static solution for arbitrary $h$). Staticity is a theorem, not an
   assumption.

Archive result:

```text
covariant_statics_lift_019
```

This retires the C2/C3 covariant statics lift rigor debt. Nonlinear
stability is handled separately (020).
