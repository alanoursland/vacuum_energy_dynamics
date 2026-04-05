# Gravity Waves

## Two Theories, Two Wave Modes

Gravitational waves are ripples in the fabric of spacetime. But the *character* of those ripples depends on what you believe spacetime fundamentally is. General Relativity predicts **tensor waves**—transverse oscillations that stretch and squeeze space perpendicular to their direction of travel. Vacuum Energy Dynamics predicts an additional mode: **scalar waves**—longitudinal "breathing" oscillations where space itself expands and contracts along the direction of propagation.

This note lays out both predictions and explains why the distinction is experimentally testable.

## GR Gravitational Waves: The Tensor Mode

### Linearized Gravity

In General Relativity, gravitational waves arise as solutions to the linearized Einstein field equations. Starting from a small perturbation $h_{\mu\nu}$ on a flat Minkowski background:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \qquad |h_{\mu\nu}| \ll 1$$

the vacuum Einstein equations reduce to a wave equation:

$$\Box \bar{h}_{\mu\nu} = 0$$

where $\bar{h}_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h$ is the trace-reversed perturbation and $\Box = -\frac{1}{c^2}\partial_t^2 + \nabla^2$ is the d'Alembertian operator.

Solutions propagate at the speed of light $c$.

### The Quadrupole Formula

GR gravitational waves are sourced by the second time derivative of the mass quadrupole moment:

$$h_{ij}^{TT} \sim \frac{2G}{c^4 r}\ddot{Q}_{ij}$$

where:
- $Q_{ij} = \int \rho(x_i x_j - \frac{1}{3}\delta_{ij}r^2)\,dV$ is the traceless quadrupole moment
- $r$ is the distance to the source
- The superscript $TT$ denotes the transverse-traceless gauge

This means:
- **Monopole radiation is forbidden**: a spherically pulsating mass produces no GR waves
- **Dipole radiation is forbidden**: linear momentum conservation prevents it
- **Quadrupole is the leading order**: you need asymmetric acceleration of mass

### Polarizations: $h_+$ and $h_\times$

GR waves have exactly **two polarizations**, both transverse:

- **Plus ($h_+$)**: stretches space along one axis while squeezing along the perpendicular axis
- **Cross ($h_\times$)**: the same pattern rotated by 45°

A ring of free-falling test particles in the path of a GR wave deforms into an ellipse, alternating between two perpendicular orientations. The wave propagates perpendicular to the plane of deformation—it is a **transverse, traceless tensor** perturbation.

### LIGO and Observational Confirmation

On September 14, 2015, the Laser Interferometer Gravitational-Wave Observatory (LIGO) detected gravitational waves from the merger of two black holes (GW150914). The signal matched GR predictions with extraordinary precision:

- Frequency swept from ~35 Hz to 250 Hz during the inspiral and merger
- Strain amplitude $h \sim 10^{-21}$
- Consistent with a 36 + 29 solar mass binary at ~410 Mpc
- Waveform matched numerical relativity templates to within measurement uncertainty

Subsequent detections by LIGO and Virgo (and now KAGRA) have confirmed GR tensor waves from binary black holes, binary neutron stars (GW170817), and mixed mergers.

## VED Scalar Waves: The Breathing Mode

### A Different Source Mechanism

In VED, gravitational effects arise from local changes in the vacuum energy density $\rho_v$ relative to the background $\bar{\rho}_v$. The [VED Identity](derivation_of_g.md):

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v}$$

is a **scalar** relationship. The strain $h$ is a single number at each point—not a tensor with independent components. This means the wave mode is fundamentally different from GR.

### Monopole (Breathing) Mode

A VED scalar wave is a **longitudinal, volumetric oscillation**:

- During the **compression phase**, local $\rho_v$ increases above $\bar{\rho}_v$, and space locally expands ($h > 0$)
- During the **rarefaction phase**, local $\rho_v$ decreases below $\bar{\rho}_v$, and space locally contracts ($h < 0$)
- The oscillation propagates outward as a spherical "breathing" pulse

A ring of test particles in the path of a VED scalar wave would **uniformly expand and contract**—all particles moving radially inward and outward together, like a circle breathing. This is in stark contrast to the elliptical deformation of GR tensor waves.

### Comparison of Wave Modes

| Property | GR Tensor Wave | VED Scalar Wave |
|----------|---------------|-----------------|
| Polarization | Two transverse modes ($h_+$, $h_\times$) | One isotropic breathing mode |
| Deformation pattern | Elliptical (stretch/squeeze) | Radial (expand/contract) |
| Lowest multipole | Quadrupole ($\ell = 2$) | Monopole ($\ell = 0$) |
| Source requirement | Asymmetric mass acceleration | Any oscillation of $\rho_v$ |
| Propagation | Transverse at $c$ | Longitudinal at $c$ |
| Radiation pattern | Anisotropic (quadrupole) | Isotropic (spherical) |

### The "Mean Zero" Property

VED scalar waves are **mean zero**: over one complete cycle, the net displacement is zero. Space expands by $+h$ for half a cycle and contracts by $-h$ for the other half. There is no permanent deformation—only a transient oscillation that transports energy through the vacuum.

This is analogous to a sound wave in air: molecules oscillate back and forth, transmitting energy without any net material transport. In VED, the "molecules" are cubic volumes of space, and the "pressure" is the vacuum energy density.

### Why Monopole Radiation Is Possible in VED

GR forbids monopole gravitational radiation because of Birkhoff's theorem: a spherically symmetric vacuum solution is necessarily static (Schwarzschild). A pulsating sphere with constant mass produces no waves.

VED circumvents this because the source is not mass in the traditional sense—it is a **modulation of the vacuum energy density itself**. A [Casimir cavity oscillating at MHz frequencies](casimir_gravity_wave_pump.md) changes $\rho_v$ locally without requiring asymmetric mass motion. The oscillation is scalar (a density change), not tensorial (a shear), so it couples to the monopole mode.

## Distinguishing the Two Modes

The scalar vs. tensor distinction provides a clean experimental test:

### 1. Polarization Test
- **GR tensor wave**: A LIGO-style interferometer with perpendicular arms sees differential strain (one arm stretches, the other squeezes)
- **VED scalar wave**: Both arms stretch and contract together—the signal appears as a **common mode**, not a differential mode

### 2. Rotation Invariance
- **GR tensor wave**: The signal amplitude depends on the detector's orientation relative to the source (antenna pattern)
- **VED scalar wave**: The signal is **isotropic**—it should be independent of detector orientation. Rotating the detector changes nothing.

### 3. Distance Law
- Both modes should fall off as $1/r$ in amplitude (equivalently, $1/r^2$ in power), following from energy conservation in three-dimensional propagation.

### 4. Shielding Test
- **Electromagnetic mimics**: Blocked by a Faraday cage
- **Acoustic mimics**: Blocked by vacuum isolation
- **Gravitational signal (GR or VED)**: Passes through all electromagnetic and acoustic shielding

These tests are described in detail in the [Macro Gravity Wave Detection](macro_gravity_wave_detection.md) protocol.

## Energy Transport

Both GR and VED waves transport energy. In GR, the energy flux is given by the Isaacson stress-energy tensor:

$$T_{\mu\nu}^{GW} = \frac{c^2}{32\pi G}\langle\partial_\mu h_{\alpha\beta}\,\partial_\nu h^{\alpha\beta}\rangle$$

In VED, energy transport follows from the oscillating vacuum density: each cycle of expansion and contraction carries the energy injected by the source outward through the vacuum medium. The wave does not permanently displace space—it transfers the energy of each oscillation to adjacent vacuum regions, propagating the disturbance at $c$.

This is the mechanism by which the [Casimir Gravity Wave Pump](casimir_gravity_wave_pump.md) would transmit its signal to a distant detector.

---

## References

1. Einstein, A. (1916). "Näherungsweise Integration der Feldgleichungen der Gravitation." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 688–696.
2. Einstein, A. (1918). "Über Gravitationswellen." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*, 154–167.
3. Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration) (2016). "Observation of Gravitational Waves from a Binary Black Hole Merger." *Physical Review Letters*, 116(6), 061102.
4. Abbott, B. P., et al. (2017). "GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral." *Physical Review Letters*, 119(16), 161101.
5. Maggiore, M. (2007). *Gravitational Waves: Theory and Experiments*. Oxford University Press.
6. Maggiore, M. (2018). *Gravitational Waves: Astrophysics and Cosmology*. Oxford University Press.
7. Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman.
8. Isaacson, R. A. (1968). "Gravitational Radiation in the Limit of High Frequency. I & II." *Physical Review*, 166(5), 1263–1280.
9. Will, C. M. (2014). "The Confrontation between General Relativity and Experiment." *Living Reviews in Relativity*, 17(1), 4.
10. Eardley, D. M., Lee, D. L., & Lightman, A. P. (1973). "Gravitational-Wave Observations as a Tool for Testing Relativistic Gravity." *Physical Review D*, 8(10), 3308–3321.
