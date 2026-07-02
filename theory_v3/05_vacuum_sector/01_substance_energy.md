# The Substance Energy

**Claim (licensed by P10).** The vacuum's substance energy — the energy
P1 identifies the vacuum *with*, at the constant density P3 commits to
— is the uniform frustration strain of the packing's flat ground
state. It is real, Planck-scale dense, present in every cell of space,
and gravitationally invisible as a theorem.

## 1. Why Space Costs Energy

Regular tetrahedra cannot tile flat 3-space: five around an edge fall
short of closure by exactly

$$\Delta_0 = 2\pi - 5\arccos\tfrac13 \approx 7.3561^\circ$$

(exact; derivation 037, with the full relief function
$\cos\delta(s) = \cos s/(1+2\cos s)$ closing only on the 600-cell).
Flat embedding forces every hinge to close to $2\pi$ anyway, so the
cells distort — edges strained off rest length, dihedrals off
preference — and the mismatch that cannot exist as geometry exists as
energy. Measured, not asserted (derivation 041): the five-fold wedge is
the least-frustrated closure and still cannot reach zero
(E(5) = 0.00065 > 0 in the lab units, strict minimum over n = 3..7),
while FCC-type order relaxes to zero exactly — the floor is a property
of *tetrahedral* local order, i.e., of what this vacuum is.

> **The substance energy is unrealized curvature**: the curvature flat
> space refuses to permit, paid for in strain instead.

Two corollaries worth owning. First, P1's founding sentence — "the
vacuum's reality and its energy content are the same fact, viewed two
ways" — now has a mechanism: *being three-dimensional space* and
*carrying strain* are the same fact, because 3D packing cannot close
for free. Second, 2D packing *is* free (triangles tile): three is the
first dimension where existing costs energy.

## 2. The Density, and the Conversion Factor

In the harmonic wedge model the floor density is

$$\rho_v = \frac{c_e\,\kappa_w\,\Delta_0^2}{2\,a^3},$$

with $a$ the packing scale, $c_e$ the edge-density coefficient, and
$\kappa_w$ the wedge stiffness (derivation 038). By the floor–Newton
lock (039), $\kappa_w$ is eliminated against the gravitational
coupling:

$$\rho_v = \frac{c_e\,\Delta_0}{2\,a^3}\; f'(\Delta_0)
\qquad\text{with } f'(\Delta_0) \propto \frac{c^4}{16\pi G} :$$

**the vacuum's substance energy and the strength of gravity are two
readings of one wedge energy.** P1's open question — the conversion
factor between vacuum extent and vacuum energy, "the analog of $c^2$" —
is now a two-parameter target ($a$, $c_e$; obligation O-P10-1). For
Planck-scale $a$ the density is Planckian, which would be a
catastrophe in any theory where it gravitated. It does not:

## 3. The Sequestering Theorem Chain (why gravity never sees it)

This is the section's central result, and it is a theorem chain, not a
tuning (derivations 033, 034, 035, 038):

1. **The packing leaves the volume mode flat.** Dihedral angles are
   exactly scale-invariant, so any angle-based energy has identically
   zero restoring force under dilation (038, exact; 041, measured on
   relaxed many-body configurations). The volume mode has no dynamics
   of its own and must be fixed by a constraint.
2. **P3 is that constraint, and it is the unimodular constraint.** The
   reduced trace mode is exactly the metric volume density,
   $\kappa = \ln(\sqrt{-g}/\sqrt{-\bar g})$; P3's constant density
   fixes it (033). The constraint is covariant — $\kappa$ is a scalar,
   its multiplier is Λ, forced constant on shell (034).
3. **The unimodular constraint sequesters the constant sector.** The
   substance term splits exactly:
   $-\rho_v\!\int\!\sqrt{-g} = -\rho_v\!\int\!\sqrt{-\bar g}
   \;-\; \rho_v\!\int\!\sqrt{-\bar g}\,(e^\kappa - 1)$ — an inert
   constant plus a coupling that vanishes identically where the
   constraint is exact and is $O(\kappa) \sim 10^{-31}$ at the F1
   matter-era leak (038). Equivalently: a constant shift of $T_{ab}$ is
   pure trace, invisible to the trace-free dynamics, absorbed exactly
   by the integration constant (035).

**The postulate that defines the substance energy (P3) is the postulate
that hides it.** In one sentence: *gravity only ever sees changes in
the vacuum, never the vacuum itself.* This discharges the
radiative-stability face of the cosmological-constant problem in VED's
own vocabulary; the value face is Λ's, handled in
`03_lambda_and_the_global_datum.md`.

## 4. Access

The substance energy is real but reachable only through processes that
change the packing itself:

- **P6 exchange** (the closed sector): kinetic-energy changes of matter
  in gradients are funded by real vacuum exchange — see
  `04_excursions_and_exchange.md`.
- **The dimensional-relaxation channel** (quarantined): engineered
  quasi-2D re-packing releasing stored frustration — a finite,
  one-time, Casimir-family process, never over-unity; gated in
  `../development/vacuum_sector/dimensional_relaxation_channel.md`.

## Verification Pointers

```text
037  exact deficit and relief function        (relief_exact_geometry)
038  identity, action split, sector signature (substance_ledger_identity)
039  floor-Newton lock                        (regge_delaunay_bridge)
041  measured floor, five-fold minimum        (frustration_relaxation_lab)
033-035  unimodular chain, sequestering       (unimodular arc)
```
