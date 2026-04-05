# General Relativity Consistency

This document serves two purposes. First, it demonstrates systematically that VED reproduces every standard General Relativity result in the weak-field limit. Second, it draws a clear line between what VED recovers (which establishes consistency but not correctness) and where VED diverges from GR (which is testable).

A framework that fails to recover GR where GR has been tested is immediately falsified. A framework that only recovers GR and adds nothing is uninteresting. VED must do both: recover everything known, and predict something new. This document catalogues the recoveries. The predictions are described in the [Casimir Effect](casimir_effect.md) document.

-----

## 1. The Mapping Between VED and GR

VED defines the metric strain as a fractional change in vacuum energy density:

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v}$$

In the weak-field limit, this maps directly onto the standard GR gravitational potential:

$$h = \frac{2\Phi}{c^2}$$

where $\Phi$ is the Newtonian potential. This mapping is exact for static, spherically symmetric fields. Every GR result that depends on the Newtonian potential in the weak-field limit is therefore automatically recovered by VED, because VED and GR are describing the same quantity with different names.

This is important to understand clearly: **the weak-field recoveries below are not independent confirmations of VED. They are consequences of a mathematical equivalence.** They show that VED is consistent with GR. They do not show that VED is correct where GR might be wrong.

-----

## 2. Recovery of the Schwarzschild Metric Components

### The Time-Time Component

The Schwarzschild metric in the weak-field limit gives:

$$g_{00} = -\left(1 - \frac{r_s}{r}\right) \approx -\left(1 - \frac{2GM}{rc^2}\right)$$

In VED, the fractional vacuum energy deficit at distance $r$ from mass $M$ is:

$$\frac{\Phi_v}{\bar{\rho}_v} = \frac{2GM}{rc^2}$$

The metric component is therefore:

$$g_{00} = -(1 - h) = -\left(1 - \frac{\Phi_v}{\bar{\rho}_v}\right)$$

These are identical. The VED deficit field and the Schwarzschild time dilation encode the same information.

### The Radial-Radial Component

$$g_{rr} = \left(1 - \frac{2GM}{rc^2}\right)^{-1} \approx 1 + \frac{2GM}{rc^2}$$

In VED:

$$g_{rr} \approx 1 + h = 1 + \frac{\Phi_v}{\bar{\rho}_v}$$

Again identical. The spatial contraction in the Schwarzschild metric corresponds exactly to the vacuum energy deficit.

### The Numerical Confirmation

The fractional kinetic energy gained by a mass $m$ falling from infinity to radius $r$:

$$\frac{\Delta KE}{mc^2} = \frac{GM}{rc^2}$$

The fractional spatial contraction from the Schwarzschild metric:

$$\frac{r_s}{2r} = \frac{GM}{rc^2}$$

These are the same number, derived from independent calculations (energy accounting vs. geometry). VED interprets this as evidence that the energy extracted from the vacuum and the spatial contraction are the same event. GR encodes this as a mathematical consequence of the field equations. Both frameworks produce identical observables.

-----

## 3. Recovery of the Gravitational Frequency Shift

A photon emitted at radius $r$ in a gravitational field and observed at infinity has its frequency shifted:

$$\frac{f_\infty}{f_r} = \sqrt{1 - \frac{2GM}{rc^2}} \approx 1 - \frac{GM}{rc^2}$$

In VED, a photon climbing out of a vacuum energy deficit loses energy to the gradient. The frequency shift is:

$$\frac{f_\infty}{f_r} = \sqrt{1 - \frac{\Phi_v}{\bar{\rho}_v}}$$

Since $\Phi_v / \bar{\rho}_v = 2GM/rc^2$, this is the same expression. The Pound-Rebka experiment (1960), GPS satellite corrections, and all precision redshift measurements are equally well described by both frameworks.

-----

## 4. Recovery of the Vacuum Refractive Index

The Schwarzschild metric in isotropic coordinates produces an effective refractive index for light propagation:

$$n(r) = \frac{1}{1 - \dfrac{2GM}{rc^2}} \approx 1 + \frac{2GM}{rc^2}$$

In VED, the vacuum energy deficit creates a spatially varying refractive index:

$$n(r) = \frac{1}{1 - \dfrac{\Phi_v}{\bar{\rho}_v}} \approx 1 + \frac{\Phi_v}{\bar{\rho}_v}$$

This is the Gordon metric result — the standard formalism for gravitational optics. VED and GR produce identical refractive indices.

-----

## 5. Recovery of Light Deflection (Including the Factor of 2)

The total deflection angle for a photon passing a mass $M$ at closest approach $b$:

$$\Delta\theta = \frac{4GM}{bc^2}$$

This is twice the Newtonian prediction (Soldner, 1801) and twice Einstein's 1911 calculation using time dilation alone. The full factor of 2 requires both time dilation and spatial curvature contributions.

VED recovers the full factor automatically because the vacuum energy deficit and the spatial contraction are identified as the same event. A photon traversing a deficit region encounters both the temporal component ($g_{00}$) and the spatial component ($g_{rr}$) simultaneously, because in VED there is no way to have one without the other. The Eddington (1919) and all subsequent light deflection measurements are consistent with both GR and VED.

-----

## 6. Recovery of the Newtonian Potential and Geodesic Motion

In the weak-field, slow-motion limit, the geodesic equation reduces to:

$$\frac{d^2 x^i}{dt^2} = -\frac{c^2}{2} \frac{\partial h_{00}}{\partial x^i}$$

With $h_{00} = -2GM/(rc^2) = -\Phi_v/\bar{\rho}_v$, this gives:

$$\frac{d^2 x^i}{dt^2} = -\frac{\partial \Phi}{\partial x^i}$$

which is Newton's law of gravitation. In VED, this becomes:

$$\frac{d^2 x^i}{dt^2} = -\frac{c^2}{2\bar{\rho}_v} \frac{\partial (\Delta\rho_v)}{\partial x^i}$$

The mass accelerates down the vacuum energy gradient. The trajectories are identical to GR geodesics in the weak-field limit. All orbital mechanics — Keplerian orbits, escape velocities, tidal forces — are recovered exactly.

-----

## 7. Recovery of Frame-Dragging (Lense-Thirring)

For a rotating mass with angular momentum $J$, GR predicts frame-dragging at the rate:

$$\omega_{LT} = \frac{2GJ}{c^2 r^3}$$

In VED, a rotating vacuum energy deficit creates a vortex in the surrounding vacuum field. The off-diagonal component of the deficit tensor $\Delta V_{0\phi}$ sources the frame-dragging, and the angular velocity of the surrounding vacuum recovers the Lense-Thirring rate in the weak-field, slow-rotation limit.

The $1/r^3$ dependence (vs. $1/r^2$ for static gravity) follows from the topological distinction between monopole deficits (mass) and dipole-like circulating deficits (spin). Gravity Probe B measurements (2011) are consistent with both GR and VED.

-----

## 8. Recovery of the FLRW Cosmology

The Friedmann equations governing the expansion of a homogeneous, isotropic universe:

$$H^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}$$

VED replaces $\Lambda$ with the generation term $\Gamma(t)$ representing continuous vacuum energy production. In the limit where $\Gamma(t)$ produces a constant vacuum energy density (equivalent to $w = -1$ dark energy), VED reproduces the standard $\Lambda$CDM expansion history.

The continuity equation in VED:

$$\frac{d\bar{\rho}_v}{dt} = \Gamma(t)$$

reduces to $\bar{\rho}_v = \text{constant}$ when $\Gamma(t)$ exactly balances the dilution from expansion — which is the standard dark energy behavior. CMB, BAO, and supernovae Ia observations constrain $\Gamma(t)$ but do not currently distinguish it from constant $\Lambda$.

-----

## 9. Summary of Recoveries

| GR Result | VED Recovery | Observational Test | Status |
| :--- | :--- | :--- | :--- |
| Schwarzschild $g_{00}$ | $-(1 - \Phi_v/\bar{\rho}_v)$ | Gravitational redshift | Exact match |
| Schwarzschild $g_{rr}$ | $1 + \Phi_v/\bar{\rho}_v$ | Spatial contraction | Exact match |
| Gravitational frequency shift | Photon energy exchange with deficit gradient | Pound-Rebka, GPS | Exact match |
| Vacuum refractive index | $n(r) = 1 + \Phi_v/\bar{\rho}_v$ | Light deflection | Exact match |
| Light deflection angle | $4GM/bc^2$ (factor of 2 automatic) | Eddington, VLBI | Exact match |
| Newtonian potential | $\Phi = c^2 \Phi_v / (2\bar{\rho}_v)$ | Orbital mechanics | Exact match |
| Frame-dragging | Rotating deficit vortex | Gravity Probe B | Exact match |
| FLRW expansion | $\Gamma(t)$ with $w = -1$ limit | CMB, BAO, SNIa | Consistent |

Every result in this table is a recovery, not a discovery. None of them constitute evidence for VED over GR. They establish that VED does not contradict any tested prediction of general relativity.

-----

## 10. Where VED Diverges from GR

VED makes predictions that differ from GR in three regimes:

### 10.1 Vacuum-Scale Gravitational Coupling

GR treats all energy — including Casimir vacuum energy — as a component of the stress-energy tensor $T_{\mu\nu}$, coupled to geometry through $G/c^4$. For a NEMS Casimir cavity oscillating at MHz frequencies, GR predicts:

$$h_{\text{GR}} \sim 10^{-50}$$

VED predicts that vacuum energy modulation couples to geometry directly through the identity principle, without the $G/c^4$ suppression:

$$h_{\text{VED}} \sim 10^{-19}$$

This is a 31-order-of-magnitude discrepancy. The Casimir cavity experiment is designed to distinguish between these predictions. A null result at $10^{-19}$ falsifies VED at this scale. A positive result falsifies GR's treatment of vacuum energy coupling.

### 10.2 Black Hole Interior

GR predicts a singularity at $r = 0$ with infinite density and curvature. VED predicts that the vacuum energy deficit saturates at $\Phi_v = \bar{\rho}_v$ (the vacuum is fully depleted), replacing the singularity with a maximally contracted but finite core. This is not currently testable by direct observation, but it has implications for gravitational wave ringdown signatures that may become accessible to future detectors.

### 10.3 Gravitational Wave Polarization

GR predicts exclusively tensor (plus and cross) polarizations for gravitational waves. VED predicts scalar (breathing mode) polarizations from vacuum energy modulation sources. LIGO observations of astrophysical mergers are consistent with tensor-only polarizations, but LIGO operates at frequencies ($10^{-9}$ to $10^3$ Hz) far below the MHz range where VED's scalar waves would be produced by a Casimir pump. The two predictions do not currently conflict because they apply to different source types and frequency bands.

-----

## 11. The Transition Question

VED claims that the identity $h = \Delta\rho_v / \bar{\rho}_v$ holds at the vacuum scale, while the $G/c^4$ coupling holds at macroscopic scales. This raises an unavoidable question: **where is the transition, and what controls it?**

The current framework does not provide a precise answer. The "Derivation of G" document shows that $G = c^4 / (\bar{\rho}_v L^2)$ is consistent with the identity, suggesting that $G/c^4$ emerges when the identity is averaged over a cosmological length scale $L$. But the averaging procedure is not formalized, and the transition scale is not specified.

Possible approaches to resolving this:

**Length-scale crossover:** The identity holds below some characteristic scale $\ell_*$ and the $G/c^4$ coupling emerges above it, analogous to how thermodynamic equations of state emerge from statistical mechanics above the mean free path.

**Source-type distinction:** The identity holds when the vacuum state itself is modulated (Casimir boundaries change which modes exist), while $G/c^4$ holds when energy is added on top of an unmodified vacuum state (mass, radiation, electromagnetic fields). This would explain why a Casimir cavity produces $h \sim 10^{-19}$ while a laser beam with the same energy does not.

**Formal coarse-graining:** Starting from the identity at the microscopic level, $G/c^4$ emerges after integrating over a macroscopic volume containing many individual vacuum-scale interactions. This would make $G$ analogous to a transport coefficient in statistical mechanics.

None of these approaches has been developed rigorously within VED. This is an open problem (see [Gaps](gaps.md), entry 14).

-----

## 12. What This Document Does and Does Not Establish

**It establishes:** VED is mathematically consistent with every tested prediction of general relativity in the weak-field limit. No existing observation contradicts VED.

**It does not establish:** That VED is correct. That the identity principle holds at the vacuum scale. That $G/c^4$ is emergent rather than fundamental. That scalar gravitational waves exist.

The recoveries in Sections 2–8 are necessary conditions for VED to be viable. They are not sufficient conditions for VED to be true. The evidence for or against VED can only come from the regimes identified in Section 10, where VED and GR make different predictions.

-----

## References

1. Schwarzschild, K. (1916). "Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*.
2. Pound, R. V. & Rebka, G. A. (1960). "Apparent Weight of Photons." *Physical Review Letters*, 4, 337–341.
3. Soldner, J. (1801). "Über die Ablenkung eines Lichtstrahls von seiner geradlinigen Bewegung." *Berliner Astronomisches Jahrbuch*.
4. Dyson, F. W., Eddington, A. S., & Davidson, C. (1920). "A Determination of the Deflection of Light by the Sun's Gravitational Field." *Philosophical Transactions of the Royal Society A*, 220, 291–333.
5. Everitt, C. W. F. et al. (2011). "Gravity Probe B: Final Results of a Space Experiment to Test General Relativity." *Physical Review Letters*, 106, 221101.
6. Kerr, R. P. (1963). "Gravitational Field of a Spinning Mass as an Example of Algebraically Special Metrics." *Physical Review Letters*, 11, 237–238.
7. Friedmann, A. (1922). "Über die Krümmung des Raumes." *Zeitschrift für Physik*, 10, 377–386.
8. Planck Collaboration (2020). "Planck 2018 Results. VI. Cosmological Parameters." *Astronomy & Astrophysics*, 641, A6.
9. Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman.
10. Will, C. M. (2014). "The Confrontation between General Relativity and Experiment." *Living Reviews in Relativity*, 17, 4.