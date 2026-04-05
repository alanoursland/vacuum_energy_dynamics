# Spatial Curvature

## Curvature as a Vacuum Pressure Gradient

In General Relativity, spacetime curvature is the fundamental expression of gravity: mass-energy tells spacetime how to curve, and curvature tells matter how to move. The mathematical language—Riemann tensors, Christoffel symbols, geodesic equations—is purely geometric. In Vacuum Energy Dynamics, this geometry is given a physical substrate: **curvature is a gradient in vacuum energy density.** The "bending" of space is the pressure difference between regions of high and low $\rho_v$, and the "attraction" of gravity is the resulting flow of space from high pressure to low.

Most importantly, this reinterpretation reveals that gravity is **symmetrical**. If depleting $\rho_v$ produces attraction, then injecting energy into the vacuum—*increasing* $\rho_v$ above the background—must produce **repulsion**. This is the theoretical basis for negative gravity.

## Curvature in General Relativity

### The Riemann Curvature Tensor

The intrinsic curvature of spacetime is encoded in the Riemann tensor $R^\alpha{}_{\beta\gamma\delta}$, which measures how parallel transport around an infinitesimal loop rotates a vector. In four-dimensional spacetime, it has 20 independent components.

Its contraction gives the Ricci tensor:

$$R_{\mu\nu} = R^\alpha{}_{\mu\alpha\nu}$$

and the Ricci scalar:

$$R = g^{\mu\nu}R_{\mu\nu}$$

The Einstein field equations relate these curvature quantities to the stress-energy content:

$$R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu}$$

### Geodesic Deviation

The physical meaning of curvature is captured by **geodesic deviation**: two initially parallel freely falling particles will converge (positive curvature / attractive gravity) or diverge (negative curvature / repulsive effects) depending on the local Riemann tensor.

The deviation equation:

$$\frac{D^2 \xi^\alpha}{d\tau^2} = -R^\alpha{}_{\beta\gamma\delta}\,u^\beta\,\xi^\gamma\,u^\delta$$

where $\xi^\alpha$ is the separation vector and $u^\beta$ is the four-velocity. Convergence means attraction; divergence means repulsion.

### Weak-Field Limit

In the weak-field, slow-motion limit, GR reduces to Newtonian gravity. The metric perturbation is:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right)$$

where $\Phi$ is the Newtonian potential. The spatial curvature is directly related to the gradient of $\Phi$:

$$\nabla^2 \Phi = 4\pi G \rho$$

This Poisson equation tells us that curvature (encoded in $\nabla^2 \Phi$) is sourced by mass density $\rho$.

## The VED Reinterpretation

### Curvature as a Pressure Gradient

In VED, the vacuum energy density $\rho_v(\mathbf{x})$ plays the role that pressure plays in fluid dynamics. Curvature is not an abstract geometric property—it is the physical consequence of **spatial pressure differences**.

Near a mass:
- The mass consumes vacuum energy (see [Gravitational Energy Transfer](gravitational_energy_transfer.md))
- Local $\rho_v$ drops below the background $\bar{\rho}_v$
- The surrounding vacuum, at higher $\rho_v$, pushes inward toward the deficit
- This pressure gradient *is* the curvature
- The resulting inward flow *is* gravity

Far from any mass:
- $\rho_v = \bar{\rho}_v$ everywhere
- No pressure gradient exists
- Space is flat

This is directly analogous to atmospheric pressure: air flows from high-pressure regions to low-pressure regions, creating wind. In VED, space "flows" from high-$\rho_v$ regions to low-$\rho_v$ regions, creating gravitational attraction.

### The VED Identity

The central equation of VED connects vacuum density perturbations to metric strain:

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v}$$

where:
- $h$ is the dimensionless metric strain (fractional change in proper distance)
- $\Delta\rho_v = \rho_v(\mathbf{x}) - \bar{\rho}_v$ is the local deviation from the background
- $\bar{\rho}_v \approx 6 \times 10^{-10}\;\text{J/m}^3$ is the cosmological average

This equation is a **direct identity**, not mediated by a coupling constant. It applies at all scales, though at macroscopic scales the [emergent gravitational constant](derivation_of_g.md) $G = c^4 / (\bar{\rho}_v L^2)$ recovers the standard GR predictions.

### Mapping to the Weak-Field Metric

In the Newtonian limit, the VED Identity relates to the gravitational potential:

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v} \approx \frac{2\Phi}{c^2}$$

This gives the mapping:

$$\Delta\rho_v \approx \frac{2\bar{\rho}_v}{c^2}\,\Phi$$

At the Earth's surface: $\Phi/c^2 \approx -7 \times 10^{-10}$, so $\Delta\rho_v/\bar{\rho}_v \approx -1.4 \times 10^{-9}$—an incredibly small fractional deficit, yet sufficient to hold the atmosphere, oceans, and everything else firmly in place.

## Negative Gravity: The Symmetry of the VED Identity

### The Key Insight

The VED Identity $h = \Delta\rho_v / \bar{\rho}_v$ is **algebraically symmetrical**:

- When $\Delta\rho_v < 0$ (vacuum energy consumed, density below background): $h < 0$, space contracts, geodesics converge → **attractive gravity**
- When $\Delta\rho_v > 0$ (vacuum energy injected, density above background): $h > 0$, space expands, geodesics diverge → **repulsive gravity**

There is no mathematical asymmetry in the identity. If depleting the vacuum produces attraction, **inflating the vacuum must produce repulsion.**

### Physical Meaning

Negative gravity (repulsion) corresponds to a region where the local vacuum energy density has been *increased* above the background:

$$\rho_v(\mathbf{x}) > \bar{\rho}_v \implies h > 0 \implies \text{spatial expansion (repulsion)}$$

In this region:
- Space is "over-inflated" relative to the background
- The pressure gradient points outward (from high $\rho_v$ to the surrounding lower $\bar{\rho}_v$)
- Geodesics diverge—test particles are pushed apart
- The geometry is locally de Sitter-like (expanding)

This is precisely what the cosmological constant $\Lambda$ does at the global scale: it maintains $\rho_v > 0$ everywhere, driving the accelerating expansion of the universe. VED proposes that this effect can be produced **locally** by injecting sufficient energy into the vacuum.

### The Cosmological Precedent

The universe already exhibits "negative gravity" at the largest scales. The accelerating expansion driven by dark energy is a global manifestation of $\Delta\rho_v > 0$ (relative to a hypothetical zero-energy vacuum). VED simply asks: can we reproduce this locally?

The cosmological constant provides a uniform $\rho_\Lambda$ everywhere. A localized energy injection would create a non-uniform perturbation $\delta\rho_v(\mathbf{x}) > 0$ in a finite region—producing a localized "pocket" of repulsive gravity surrounded by normal space.

### Conditions for Negative Gravity

For a measurable repulsive effect, the injection must:

1. **Raise $\rho_v$ above $\bar{\rho}_v$** in a localized region
2. Be **sustained or oscillatory** (a transient injection produces a transient pulse, not a static field)
3. Produce a strain $h = \Delta\rho_v / \bar{\rho}_v$ large enough to detect

The [Casimir Gravity Wave Pump](casimir_gravity_wave_pump.md) is designed to achieve this through high-frequency oscillation: each compression phase of the NEMS comb momentarily raises $\rho_v$ between the plates, producing a brief expansion pulse. The alternation of expansion ($+h$) and contraction ($-h$) generates a propagating [scalar gravity wave](gravity_waves.md).

## Curvature Spectrum

The VED framework produces a continuous spectrum from the strongest curvature (black holes) to the weakest (cosmological background):

| Regime | $\Delta\rho_v / \bar{\rho}_v$ | Character |
|--------|-------------------------------|-----------|
| [Black hole](black_holes.md) interior | $\to -1$ (saturation) | Maximum consumption, inflow $> c$ |
| Neutron star surface | $\sim -0.4$ | Deep well, strong-field GR |
| White dwarf surface | $\sim -10^{-4}$ | Moderate well |
| Earth surface | $\sim -10^{-9}$ | Shallow well, Newtonian limit |
| Interstellar space | $\sim 0$ | Flat, near background |
| Cosmological expansion | $> 0$ (global) | Dark energy, universal repulsion |
| **NEMS injection zone** | $> 0$ (local, oscillating) | Engineered repulsion / scalar wave |

## Connections

- The VED Identity and its derivation are in [Derivation of G](derivation_of_g.md)
- The mechanism of vacuum consumption is in [Gravitational Energy Transfer](gravitational_energy_transfer.md)
- The scalar wave produced by oscillating curvature is in [Gravity Waves](gravity_waves.md)
- The extreme-curvature limit is in [Black Holes](black_holes.md)
- The global expansion maintaining $\bar{\rho}_v$ is in [Spatial Expansion](spatial_expansion.md)

---

## References

1. Einstein, A. (1915). "Die Feldgleichungen der Gravitation." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 844–847.
2. Carroll, S. M. (2004). *Spacetime and Geometry: An Introduction to General Relativity*. Addison-Wesley.
3. Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman.
4. Wald, R. M. (1984). *General Relativity*. University of Chicago Press.
5. Padmanabhan, T. (2010). *Gravitation: Foundations and Frontiers*. Cambridge University Press.
6. Schutz, B. F. (2009). *A First Course in General Relativity*. 2nd ed. Cambridge University Press.
7. Poisson, E. (2004). *A Relativist's Toolkit: The Mathematics of Black-Hole Mechanics*. Cambridge University Press.
8. Visser, M. (1995). *Lorentzian Wormholes: From Einstein to Hawking*. AIP Press.
