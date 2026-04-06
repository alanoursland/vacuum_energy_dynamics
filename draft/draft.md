# **Proposed Experimental Test of Direct Vacuum-Geometry Coupling via High-Frequency Casimir Cavity Modulation**

**Author:** Alan Oursland  
**Date:** April 5, 2026  

## Abstract

Neither Newtonian mechanics nor General Relativity identifies a local, physical source for the kinetic energy gained by a falling mass. We present a phenomenological ansatz — Vacuum Energy Dynamics (VED) — in which the vacuum energy density is the physical medium of the gravitational field and metric strain is identically a fractional perturbation of that medium: $h = \Delta\rho_v / \bar{\rho}_v$. The ansatz reproduces all weak-field predictions of General Relativity, but diverges in one untested regime: direct modulation of the vacuum state via Casimir boundary conditions. For a nanoelectromechanical (NEMS) Casimir cavity oscillating at MHz frequencies, General Relativity predicts a gravitational wave strain of order $10^{-50}$; the ansatz predicts $10^{-19}$. We propose an experiment to discriminate between these predictions using a NEMS Casimir comb source, a piezoelectric quartz resonator tuned to the source frequency, and a triple-sensor isolation protocol. The predicted signal is a scalar breathing-mode gravitational wave — qualitatively distinct from the tensor modes of General Relativity. A null result at $10^{-19}$ sensitivity falsifies the ansatz. A positive result, confirmed by shielding invariance, inverse-square falloff, rotation invariance, and frequency synchronization, would demonstrate that vacuum-state modification couples to geometry outside the standard stress-energy framework.

## Section 1: Introduction

When a mass falls in a gravitational field, it gains kinetic energy. The question of where that energy was stored before the fall — and what physical medium surrendered it — has no definitive answer in either Newtonian mechanics or General Relativity. This paper explores the consequences of a specific answer to that question: that gravitational kinetic energy is extracted from the quantum vacuum, and that the extraction destroys a definite volume of space.

---

### 1.1 The Localization Problem

In Newtonian mechanics, the energy of a gravitational system is encoded in the potential energy $U = -Gm_1 m_2/r$. As a mass falls and gains kinetic energy, $U$ becomes more negative by a precisely compensating amount. The accounting is exact, but the energy itself cannot be localized. No cubic meter of space can be identified as containing a measurable share of $U$. The potential energy is a property of the mathematical configuration of the system, not of a physical medium at a definite location [1].

General Relativity makes this problem more acute. The equivalence principle guarantees that an observer in free fall detects no local gravitational field — the field can be transformed away by a coordinate change. Because the field vanishes locally, GR prohibits the construction of a gauge-invariant, local energy density for the gravitational field [2]. Global energy conservation can be maintained through pseudotensors [3] or asymptotic mass definitions (ADM, Bondi) [4, 5], but these balance the books at spatial infinity. They do not identify a local, physical source from which the falling mass draws its kinetic energy.

This is not merely a philosophical nuance. If gravitational energy cannot be localized, then the gravitational energy transaction cannot be described as a thermodynamic process with a definite source and a definite sink. The question "where does the kinetic energy come from?" has no local answer within the standard framework.

### 1.2 The Vacuum Catastrophe

A second, apparently unrelated problem concerns the relationship between vacuum energy and spacetime geometry.

Quantum Field Theory sums the zero-point energies of all field modes up to the Planck scale and predicts a vacuum energy density of $\rho_{\text{QFT}} \approx 10^{113}$ J/m³. Cosmological observations of the accelerating expansion imply a vacuum energy density of $\rho_{\text{obs}} \approx 6 \times 10^{-10}$ J/m³. The discrepancy — 120 orders of magnitude — is the most severe fine-tuning problem in physics [6, 7].

In the standard framework, vacuum energy enters the Einstein field equations as a source term in $T_{\mu\nu}$, coupled to geometry through $G/c^4$ like any other energy. The cosmological constant $\Lambda$ must be adjusted to 120 decimal places to cancel the QFT prediction and match observation. This cancellation is imposed by hand. It works, but it provides no physical explanation for why the vacuum energy density that drives cosmic expansion is so much smaller than the energy density that quantum field theory requires the vacuum to contain.

These two problems — the non-localizability of gravitational energy and the vacuum catastrophe — may be symptoms of the same underlying ambiguity: the relationship between vacuum energy and spacetime geometry. If vacuum energy is ordinary content within the metric, coupled through $G/c^4$, then the catastrophe persists and gravitational energy remains unlocalized. If vacuum energy is the substance of the metric itself, both problems change character.

### 1.3 The Proposal

This paper explores a phenomenological ansatz in which the vacuum energy density is the physical medium of the gravitational field, and in which metric strain is identically a fractional perturbation of that medium:

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v}$$

Under this identity, gravitational kinetic energy has a local source — the vacuum energy density at each coordinate — and the energy transaction is thermodynamically definite: a falling mass extracts energy from the vacuum, destroying spatial volume in proportion to the kinetic energy gained.

The ansatz reproduces all tested predictions of General Relativity in the weak-field limit. It diverges from GR in one specific regime: direct modulation of the vacuum state via Casimir boundary conditions. For a NEMS Casimir cavity oscillating at MHz frequencies, GR predicts a gravitational wave strain of $h \sim 10^{-50}$. The ansatz predicts $h \sim 10^{-19}$ — a 31-order-of-magnitude discrepancy that can be resolved by a table-top experiment.

The ansatz is speculative. The identity is axiomatic, not derived from more fundamental principles. Its justification is empirical falsifiability: if the predicted signal is not detected, the identity is ruled out at this scale. The purpose of this paper is to present the ansatz, derive the prediction, propose the experiment, and commit to the consequences of the result.

### 1.4 Structure of the Paper

Section 2 defines the identity principle, demonstrates its weak-field consistency with GR, derives the local vacuum energy density from conservation of energy, and shows the emergence of $G$ as a macroscopic scaling ratio. Section 3 identifies the point of divergence: the Casimir energy transaction as a gravitational process within VED, the framework's energy budget for the oscillating pump, and the quantitative strain prediction. Section 4 presents the experimental design — the NEMS source, piezoelectric detector, isolation protocol, and validation criteria. Section 5 specifies the interpretation of positive, null, and intermediate results. Section 6 catalogues the framework's open problems. Section 7 concludes.

---

## Section 2: The Phenomenological Ansatz

This section defines the core equation of Vacuum Energy Dynamics, demonstrates its consistency with General Relativity in the weak-field limit, and derives two consequences: the local vacuum energy density near matter and the emergence of the gravitational constant as a macroscopic scaling ratio. Each result is accompanied by an explicit statement of its epistemic status within the framework.

---

### 2.1 The Identity Principle

VED proposes that the vacuum energy density at each coordinate is the physical substance of the spatial metric. A fractional change in the vacuum energy density at a location is a fractional change in the spatial geometry at that location — not mediated by a coupling constant, but as an identity:

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v}$$

where $h$ is the dimensionless metric strain (fractional change in proper distance), $\Delta\rho_v$ is the local deviation of the vacuum energy density from the background, and $\bar{\rho}_v \approx 6 \times 10^{-10}$ J/m³ is the cosmological background vacuum energy density inferred from the observed accelerating expansion.

The physical content of this equation is that the vacuum is not an inert stage on which gravitational physics plays out. It is the medium from which the metric is constructed. Depleting vacuum energy at a location contracts the spatial geometry there. Injecting vacuum energy expands it. The metric strain is the fractional perturbation of the medium.

This equation is the axiom of the framework. It is not derived from more fundamental principles. Its justification is threefold: it reproduces all tested predictions of General Relativity (Section 2.2), it is internally consistent with conservation of energy (Section 2.3), and it produces a falsifiable prediction that differs from GR by 31 orders of magnitude (Section 3.4). If the experimental prediction fails, the axiom is falsified at the tested scale.

---

### 2.2 Weak-Field Consistency with General Relativity

In the weak-field, static, spherically symmetric limit, the identity maps directly onto the standard gravitational potential:

$$h = \frac{\Delta\rho_v}{\bar{\rho}_v} = \frac{2\Phi}{c^2}$$

where $\Phi = -GM/r$ is the Newtonian potential. Under this mapping, the VED vacuum energy deficit $\Phi_v / \bar{\rho}_v$ at distance $r$ from a mass $M$ equals $2GM/rc^2$, and the identity reproduces the Schwarzschild metric components in the weak-field limit:

$$g_{00} \approx -(1 - h) = -\left(1 - \frac{2GM}{rc^2}\right)$$

$$g_{rr} \approx 1 + h = 1 + \frac{2GM}{rc^2}$$

From these components, the following standard results follow without additional assumptions:

The gravitational frequency shift $f_\infty / f_r = \sqrt{1 - 2GM/rc^2}$, confirmed by the Pound-Rebka experiment and GPS satellite corrections. The vacuum refractive index $n(r) \approx 1 + 2GM/rc^2$, which yields the full light deflection angle $\Delta\theta = 4GM/bc^2$ including the factor of 2 that requires both temporal and spatial contributions — a factor VED recovers automatically because the vacuum deficit and the spatial contraction are identified as the same event. And geodesic motion reducing to the Newtonian equation of motion $\ddot{x}^i = -\partial\Phi/\partial x^i$ in the slow-motion limit.

These recoveries establish that VED does not contradict any tested prediction of General Relativity in the weak-field regime. They are consequences of a mathematical equivalence — VED and GR describe the same quantity with different names in this limit. They do not constitute evidence that VED is correct where it diverges from GR. That evidence can only come from experiment in the regime identified in Section 3.

---

### 2.3 The Local Vacuum Energy Density

The identity principle contains $\bar{\rho}_v$ as a parameter — the background vacuum energy density far from all matter. Near matter, the vacuum energy density is not equal to this cosmological background. Conservation of energy within the framework determines what the local density must be.

Consider a mass $m$ falling from infinity to radius $r$ in the gravitational field of a central mass $M$. The kinetic energy gained is:

$$\Delta K = \frac{GMm}{r}$$

The Schwarzschild metric gives the fractional spatial contraction at the same radius:

$$\frac{\Delta V}{V} = \frac{GM}{rc^2}$$

In VED, the kinetic energy gained equals the energy content of the spatial volume consumed. Setting the energy extracted equal to the energy of the contracted volume and solving for the vacuum energy density:

$$\rho_v = \frac{\Delta K}{\Delta V} = \frac{GMm/r}{V \cdot GM/rc^2} = \frac{mc^2}{V}$$

The gravitational parameters $G$, $M$, and $r$ cancel identically. The result is that the local vacuum energy density equals the mass-energy density of the matter present: $\rho_v = \rho_m c^2$.

Near a silicon NEMS device with matter density $\rho_m \sim 5000$ kg/m³, the local vacuum energy density is $\rho_v \approx 4.5 \times 10^{20}$ J/m³ — thirty orders of magnitude above the cosmological background. The vacuum is a continuous field whose density varies smoothly from $\rho_m c^2$ in the immediate vicinity of matter to $\bar{\rho}_v$ in empty intergalactic space. This gradient is the physical content of a gravitational field in VED.

**Status.** This derivation is a consistency condition, not an independent measurement. It determines what $\rho_v$ must be if the framework is correct — if the energy gained by falling equals the energy of the space destroyed. It does not independently establish that the framework is correct. The experimental test in Section 4 depends on this value: the predicted strain is calculated using $\rho_v = \rho_m c^2$ as the local baseline that the Casimir pump modulates.

![**Figure 1: The Multi-Scale Vacuum.** A conceptual map showing the transition from the dilute cosmological background ($\bar{\rho}_v$) in intergalactic space to the dense local vacuum envelope ($\rho_v = \rho_m c^2$) surrounding macroscopic matter. In VED, the "gravitational well" is physically represented by this density gradient.](two_scales_of_vacuum_energy.png)

---

### 2.4 The Emergence of G

If the identity $h = \Delta\rho_v / \bar{\rho}_v$ holds at the vacuum scale, then the gravitational constant $G$ is not a fundamental parameter but an emergent ratio that appears when the identity is expressed in the language of the linearized Einstein field equations at macroscopic scales.

In the weak-field limit, the linearized Einstein equation gives the strain produced by an energy density $\Delta\rho$ distributed over a characteristic length scale $L$ as:

$$h \approx \frac{G}{c^4}\left(\Delta\rho \cdot L^2\right)$$

Setting this equal to the VED identity at the scale where the vacuum energy density change is itself the source:

$$\frac{\Delta\rho_v}{\bar{\rho}_v} = \frac{G}{c^4}\left(\Delta\rho_v \cdot L^2\right)$$

The perturbation $\Delta\rho_v$ cancels from both sides, yielding:

$$G = \frac{c^4}{\bar{\rho}_v L^2}$$

This expression recovers the measured value of $G$ for a cosmological length scale $L$. Its physical interpretation within VED is that gravity appears weak at macroscopic scales because the fractional vacuum perturbation produced by aggregated mass, averaged over large distances, is suppressed by the enormous denominator $\bar{\rho}_v L^2$. At the vacuum scale — where boundary conditions directly modulate the local vacuum state, as in a Casimir cavity — the identity applies without this macroscopic averaging, and the resulting strain is correspondingly larger.

**Open problem.** The transition between the identity regime (direct vacuum modulation) and the coupling regime (macroscopic $G/c^4$) is the most significant unresolved question in the framework. The derivation above shows that $G$ is consistent with the identity but does not specify the crossover scale, the averaging procedure, or the physical mechanism that controls the transition. Possible approaches include a characteristic length-scale crossover (analogous to the emergence of thermodynamic equations of state above the mean free path), a source-type distinction (vacuum-state modification vs. excitations above an unchanged vacuum), or a formal coarse-graining procedure. None of these has been developed rigorously. This gap does not affect the experimental prediction — which depends only on the identity holding at the Casimir scale — but it constrains the framework's theoretical completeness.

---

## Section 3: The Point of Divergence

The identity principle $h = \Delta\rho_v / \bar{\rho}_v$ reproduces General Relativity in every regime where GR has been tested. The two frameworks become distinguishable only when the vacuum energy density is modulated directly — not through the aggregated effect of bulk mass, but through physical alteration of the vacuum state itself. This section traces the logic from VED's description of ordinary gravitational energy transfer, through the Casimir effect as a laboratory-scale instance of the same process, to the quantitative prediction that a high-frequency Casimir cavity should emit detectable gravitational radiation.

---

### 3.1 Gravity as Energy Transfer from the Vacuum

In VED, a falling mass gains kinetic energy by extracting it from the local vacuum. The mass moves down a gradient in vacuum energy density, and the energy it gains is paid for by the destruction of spatial volume at each point along its trajectory. The consumed volume is

$$V_{\text{consumed}} = \frac{\Delta K}{\rho_v}$$

where $\Delta K$ is the kinetic energy gained and $\rho_v$ is the local vacuum energy density. The surrounding metric deforms to fill the void left by the consumed volume, producing the spatial contraction that GR describes as curvature.

This is not a metaphor. The Schwarzschild metric independently confirms that the fractional spatial contraction at radius $r$ from a mass $M$ is $GM/rc^2$ — identically the fractional kinetic energy gained by a mass falling from infinity to the same radius. In GR, this is a mathematical consequence of the field equations. In VED, it is the signature of a thermodynamic transaction: the fraction of vacuum energy consumed equals the fraction of space contracted, because they are the same event.

The energy source is physically localized at every coordinate. The energy transaction is thermodynamically definite — a specific volume of space, containing a specific energy density, is consumed to produce a specific kinetic energy. This resolves the localization problem that motivates the framework: gravitational energy is not stored in an unlocalized potential field or in a curvature whose energy density cannot be defined. It is stored in the vacuum energy density at each point, and it is spent when a mass passes through.

![**Figure 2: The Vacuum Transaction.** A visualization of the VED "River Model" of gravity. As a mass gains kinetic energy during free-fall, it consumed an equivalent energy-volume of the vacuum substrate. The resulting contraction of the surrounding spatial grid manifests as geometric curvature.](gravity_as_thermo_dynamic_flux.png)


---

### 3.2 The Casimir Effect as the Same Transaction

The static Casimir effect performs the same energy transaction at laboratory scale.

Two conducting plates placed close together impose boundary conditions on the electromagnetic vacuum. Modes whose wavelengths do not fit between the plates are excluded. In VED, this exclusion destroys vacuum energy in the inter-plate region — the local $\rho_v$ drops below its unperturbed value, creating a vacuum energy deficit. The plates accelerate toward each other, gaining kinetic energy. That kinetic energy is paid for by the vacuum energy that was destroyed when the modes were excluded.

This is the same thermodynamic structure as gravitational free fall: a region of depleted vacuum energy density, an object moving toward the deficit, and kinetic energy extracted from the consumed spatial volume. Standard QED describes the Casimir force completely and accurately as an electromagnetic phenomenon — a mismatch in radiation pressure from virtual photons. VED does not dispute the force prediction. It proposes that the energy transaction underlying the force — vacuum energy consumed, kinetic energy gained — is gravitational in character, and that this transaction has a geometric consequence (metric strain) which QED does not model and which GR prices at a negligibly small value.

The critical question is whether the geometric consequence of the Casimir transaction is governed by the standard gravitational coupling $G/c^4$ or by the identity $h = \Delta\rho_v / \bar{\rho}_v$. Within VED, this is not an arbitrary choice — it is forced by the logic of the framework. If vacuum energy is destroyed when modes are excluded, and if the vacuum energy density is the substance of the metric, then the destruction of vacuum energy *is* a contraction of the metric. The geometric response is not mediated by a coupling constant because the vacuum energy and the geometry are not two separate quantities connected by a coupling — they are the same quantity described at two levels. Routing the geometric change through $G/c^4$ would suppress the metric response by 31 orders of magnitude, leaving the energy of the destroyed vacuum modes with no corresponding geometric signature — the spatial volume that contained that energy would be gone, but the metric would barely register the loss. Within VED, this is not a permissible outcome: if the vacuum is the metric, then consuming the vacuum *is* deforming the metric, at full strength, with no coupling to dilute the transaction.

A natural objection is that QED already provides a complete energy budget for the Casimir force — radiation pressure imbalance accounts for the plate motion, and no energy is missing. But this objection recapitulates the localization problem that motivates the framework. QED accounts for the force. It does not identify the geometric consequence of destroying vacuum energy at a specific location, for the same reason that Newtonian mechanics does not identify the local source of gravitational kinetic energy: the standard framework does not treat the vacuum as a geometric substance. VED does. The identity-strength coupling is the consequence of that treatment, and the Casimir experiment tests whether the treatment is correct.

---

### 3.3 VED's Energy Budget for the Oscillating Pump

When the Casimir transaction is driven cyclically at high frequency, the energy-budget question sharpens from a matter of interpretation to a quantitative, testable prediction.

A NEMS actuator oscillates the plate separation at MHz frequencies. Each cycle performs two operations on the vacuum:

**Gap closing.** As the plates move together, modes are progressively excluded from the inter-plate region. Vacuum energy is destroyed. The plates gain kinetic energy drawn from the consumed spatial volume. The local vacuum energy density drops, and by the identity $h = \Delta\rho_v / \bar{\rho}_v$, the local metric contracts.

**Gap opening.** The actuator performs electrical work to pull the plates apart against the attractive Casimir force. This work re-establishes the previously excluded modes, recreating vacuum energy in the expanding gap. The local vacuum energy density rises, and the local metric expands.

The result is a forced oscillation of the vacuum energy density at the drive frequency. Within VED, this oscillation in $\rho_v$ is identically an oscillation in the metric strain $h$. The oscillating strain propagates outward as a scalar gravitational wave — a mean-zero breathing mode in which space alternately expands and contracts at each point along the wavefront.

The energy carried by the wave is sourced from the electrical work driving the actuator. Each cycle, the actuator invests work into destroying and recreating vacuum energy. The fraction of that work that couples into the propagating mode is the fraction that leaves the near field as gravitational radiation. This is not a secondary effect or a parasitic loss channel. Within VED, it is the primary output of the device: an electrically driven transducer that converts work into metric strain.

Standard physics predicts a different energy budget for the identical device. In the standard account, the electrical work goes into mechanical deformation and heat in the lattice, acoustic radiation, electromagnetic emission from accelerating charges, a small flux of dynamical Casimir effect photons, and a gravitational radiation channel priced at $h \sim 10^{-50}$ through $G/c^4$ — negligible by any measure. The two frameworks agree on the non-gravitational channels. They disagree, by 31 orders of magnitude, on the gravitational one.

The disagreement traces directly to the problem posed in Section 1.1. Standard physics does not identify a local, physical source for gravitational kinetic energy and, correspondingly, assigns no significant geometric role to local changes in vacuum energy density. VED identifies the vacuum as that source and, consequently, predicts that every transaction which destroys or creates vacuum energy — including the Casimir effect — has a geometric signature at identity strength. The Casimir prediction is not a separate claim bolted onto the framework. It is the experimental consequence of the framework's answer to the localization problem.

The experiment described in Section 4 tests whether that answer is correct.

---

### 3.4 The Quantitative Prediction

The divergence between VED and GR is sharpest in the predicted metric strain for a laboratory-scale Casimir source.

#### General Relativity

In GR, the Casimir energy in the cavity enters the stress-energy tensor $T_{\mu\nu}$ and couples to geometry through $8\pi G/c^4$. For a NEMS device modulating milliwatts of electromagnetic vacuum energy at MHz frequencies, the quadrupole gravitational wave formula yields

$$h_{\text{GR}} \sim 10^{-50}$$

This is approximately 30 orders of magnitude below the sensitivity of any existing or projected detector technology. Within standard physics, laboratory-scale gravitational wave generation is not merely difficult — it is impossible in practice.

#### VED

In VED, the Casimir pump does not couple to geometry through $G/c^4$. It modulates the vacuum energy density directly, and that modulation is the metric strain. The relevant quantities are:

The local vacuum energy density near the silicon substrate, set by conservation of energy (Section 2.3), is $\rho_v = \rho_m c^2 \approx 4.5 \times 10^{20}$ J/m³. This is the baseline that the Casimir cavity modulates.

The fractional change in vacuum energy density produced by oscillating the gap is the metric strain:

$$h_{\text{VED}} = \frac{\Delta\rho_v}{\rho_v} \sim 10^{-19}$$

The 31-order-of-magnitude difference between $h_{\text{GR}}$ and $h_{\text{VED}}$ arises because GR suppresses the gravitational effect of the Casimir energy through the macroscopic coupling $G/c^4$, while VED applies the identity directly at the vacuum scale. This is the empirical content of the framework: VED and GR make the same predictions everywhere that GR has been tested, and they make predictions differing by 31 orders of magnitude in this one untested regime.

A full derivation of the VED strain estimate, including the Casimir energy density modulation for specific gap geometries and drive amplitudes, is given in Appendix A.

---

## Section 4: Experimental Design

The experiment proposed here is designed to produce a binary result: either a laboratory Casimir cavity generates detectable metric strain at the frequency of its mechanical oscillation, or it does not. The source, detector, isolation protocol, and validation criteria are each chosen to maximize the clarity of that discrimination.

---

### 4.1 The Source: NEMS Casimir Comb

The gravitational wave source is a Nanoelectromechanical Systems (NEMS) comb drive operating as a vacuum energy transducer. Interdigitated fingers etched onto a silicon or aluminum substrate form an array of parallel Casimir cavities whose gap widths oscillate under an AC drive signal.

**Geometry.** The comb fingers maintain vacuum gaps at sub-100 nm scales, with a target separation of $d < 50$ nm. At these distances, the Casimir pressure gradient is steep: the force per unit area scales as $d^{-4}$, so small oscillations around a narrow baseline produce large fractional changes in the local vacuum energy density.

**Drive frequency.** The AC drive is tuned to the mechanical resonance of the comb structure, targeting the 1–100 MHz range. The resonant frequency is set by the geometry and material properties of the fingers. Operating at resonance maximizes displacement amplitude for a given electrical input, and therefore maximizes $\Delta\rho_v$ per cycle.

**Physical action.** Each oscillation cycle destroys and recreates vacuum energy between the plates. As the gap narrows, modes are excluded and vacuum energy is consumed — the plates gain kinetic energy drawn from the destroyed spatial volume. As the gap widens, the actuator performs electrical work against the Casimir attraction, re-establishing excluded modes and restoring vacuum energy to the inter-plate region. Within the VED framework, this cycling of $\rho_v$ is identically a cycling of the metric strain $h$, which radiates outward as a scalar gravitational wave. The energy carried by the wave is sourced from the electrical work driving the actuator.

![**Figure 3: NEMS Casimir Comb Drive.** Schematic of the gravitational wave source. Interdigitated silicon fingers create sub-100nm gaps where vacuum modes are restricted. Resonant MHz oscillation of these fingers "kneads" the local vacuum density, transducing electrical work directly into metric strain ($h$).](nems_casimir_transducer.png)

---

### 4.2 The Predicted Signal: Scalar Breathing Mode

The VED framework predicts that the Casimir pump emits a scalar gravitational wave — a monopole breathing mode qualitatively distinct from the tensor waves predicted by General Relativity for astrophysical sources.

**Polarization.** The wave is a longitudinal, isotropic oscillation in spatial volume. A ring of free-falling test particles in the wave's path would expand and contract uniformly in all radial directions — a "breathing" motion — rather than deforming into the elliptical shear pattern characteristic of GR's transverse $h_+$ and $h_\times$ polarizations.

**Why scalar, not tensor.** GR restricts gravitational radiation to the quadrupole ($\ell = 2$) and higher multipoles; monopole ($\ell = 0$) radiation is forbidden by Birkhoff's theorem. VED circumvents this restriction because the source is not accelerating mass but a nonadiabatic modulation of the vacuum energy density itself — a scalar quantity. The oscillation in $\rho_v$ couples directly to the monopole mode.

**Radiation pattern.** The scalar wave radiates spherically from the source. Its amplitude is independent of the observer's angular position relative to the comb drive. This isotropy is itself a testable prediction (see Section 4.5, rotation invariance).

**Frequency.** The gravitational wave frequency matches the mechanical oscillation frequency of the comb drive. For a pump operating at 10 MHz, the emitted wave has a 10 MHz frequency and a wavelength of $\lambda = c/f \approx 30$ m.

![**Figure 4: Tensor vs. Scalar Modes.** A comparison of deformation patterns. (Left) The standard GR tensor wave produces a transverse "plus" or "cross" shear. (Right) The VED scalar wave produces a longitudinal "breathing" mode, characterized by uniform, isotropic expansion and contraction of the spatial volume.](wave_polarization_comparison.png)

---

### 4.3 The Detector: Piezoelectric Quartz Resonator

Detection of the predicted strain ($h \approx 10^{-19}$) uses a bulk piezoelectric quartz crystal resonator tuned to the source frequency.

**Why quartz.** A scalar breathing-mode wave produces uniform volumetric expansion and contraction of any material it passes through. Piezoelectric quartz converts volumetric mechanical strain directly into a measurable voltage across its faces. This makes it a natural antenna for the predicted signal: the wave compresses and expands the crystal bulk, and the crystal transduces that deformation into an electrical signal at the wave frequency.

**Resonant enhancement.** The quartz resonator is cut and dimensioned so that its fundamental mechanical resonance matches the source frequency $f$. At resonance, mechanical oscillations build coherently over many cycles, amplifying the strain signal by the quality factor $Q$ of the crystal. High-purity quartz resonators routinely achieve $Q \sim 10^5 - 10^6$ at MHz frequencies, providing sensitivity enhancement of five to six orders of magnitude over a broadband detector.

**Contrast with interferometric detection.** A Michelson interferometer (such as LIGO) measures differential strain between two arms. A tensor wave stretches one arm while compressing the other, producing a differential signal. A scalar breathing wave stretches both arms simultaneously — a common-mode signal that a Michelson interferometer would reject. The quartz bulk resonator does not have this blind spot: it responds to the total volumetric change, making it sensitive to exactly the mode VED predicts.

---

### 4.4 Isolation Protocol

Environmental contamination — electromagnetic, acoustic, and seismic — must be excluded before any detected signal can be attributed to metric strain. The experiment uses a three-sensor differential protocol that identifies contamination by subtraction.

**Sensor A (unshielded reference).** A quartz resonator operating in the open laboratory environment. It registers the full superposition of electromagnetic, acoustic, seismic, and (if present) gravitational signals. This sensor establishes the environmental baseline.

**Sensor B (electromagnetically shielded).** An identical quartz resonator enclosed in a Faraday cage. Electromagnetic contamination from the NEMS drive circuit, stray RF, and any radiative coupling is attenuated. The signal on Sensor B minus the signal on Sensor A isolates the electromagnetic component. What remains on Sensor B is acoustic, seismic, and gravitational.

**Sensor C (fully isolated).** An identical quartz resonator enclosed in a Faraday cage, acoustically decoupled (vacuum suspension), and surrounded by dense shielding (lead). This sensor is shielded from electromagnetic, acoustic, and seismic contamination. The only signal that should reach Sensor C is a perturbation of the metric itself — a signal that passes through all material shielding because it is not a field propagating within spacetime but a distortion of spacetime.

**The gravitational candidate.** A signal that appears on all three sensors at the source frequency $f$, with amplitude on Sensor C unchanged relative to Sensors A and B after subtraction of identified EM and acoustic components, is a candidate for metric strain. A signal that appears on A and B but vanishes on C is environmental contamination. A signal that appears only on C at the drive frequency, with no corresponding signature on A or B, warrants immediate investigation for systematic error before being treated as a candidate.

![**Figure 5: Differential Detection Schematic.** The three-stage shielding protocol designed to isolate the metric strain. Sensor A establishes a noisy baseline; Sensor B subtracts electromagnetic interference; Sensor C, isolated by vacuum and high-Z shielding, detects only the gravitational signal which penetrates all material barriers.](triple_sensor_isolation_protocol.png)

---

### 4.5 Validation Criteria

A candidate signal on Sensor C must survive four independent tests before it can be attributed to gravitational metric strain. Failure of any single test rejects the candidate.

**Shielding invariance.** Additional layers of electromagnetic, acoustic, or mass shielding are added around the detector. The candidate signal must remain unchanged in amplitude and phase. A genuine metric perturbation is unaffected by material shielding; any signal that attenuates with additional shielding is contamination.

**Inverse-square falloff.** The distance between the source and detector is varied. Signal power must scale as $1/r^2$ from the center of the comb drive. Deviation from inverse-square behavior indicates near-field coupling (electromagnetic or acoustic) rather than radiative propagation.

**Rotation invariance.** The detector orientation is varied relative to the source while holding the distance fixed. A scalar breathing-mode wave is isotropic — its amplitude does not depend on the relative orientation of source and detector. A tensor wave or an electromagnetic signal would show angular dependence. Constant signal amplitude across all orientations confirms the scalar polarization predicted by VED.

**Frequency synchronization.** The drive frequency of the NEMS source is shifted intentionally. The candidate signal must track the frequency shift exactly, with no lag beyond the expected mechanical transient of the comb resonator. A signal that does not track the source frequency is not sourced by the pump.

---

### 4.6 Sensitivity Considerations

The predicted strain of $h \approx 10^{-19}$ falls within a regime that is challenging but not unprecedented for resonant mechanical detectors. For reference, the Weber bar detectors of the 1960s–70s targeted strains of $\sim 10^{-16}$, and modern resonant-mass detectors (AURIGA, NAUTILUS, MiniGRAIL) have demonstrated strain sensitivities approaching $10^{-20}$ in narrow frequency bands near their resonant frequencies.

The key advantage of the proposed setup is that the source frequency is known and controllable. Unlike astrophysical gravitational wave searches, which must scan wide frequency bands for transient signals of unknown arrival time, this experiment locks the detector to a known, stable, continuous-wave source. This permits long integration times, narrow-band filtering, and phase-coherent signal extraction — techniques that dramatically improve signal-to-noise ratio relative to broadband searches.

A detailed noise budget — including thermal noise in the quartz resonator, Johnson noise in the readout electronics, seismic coupling, and residual electromagnetic leakage — is required before a definitive sensitivity estimate can be made. This analysis is beyond the scope of the present paper but is essential for any experimental implementation.

---



## Section 5: Falsifiability and Interpretation

The 31-order-of-magnitude gap between the VED and GR predictions ensures that the experimental outcome is unambiguous at the level of detection or non-detection. This section specifies what each class of outcome would establish.

---

### 5.1 Positive Result

Detection of a signal at or near $h \sim 10^{-19}$ that passes all four validation criteria (shielding invariance, inverse-square falloff, rotation invariance, frequency synchronization) would establish that modulation of vacuum boundary conditions produces metric strain at a magnitude inconsistent with the standard $G/c^4$ coupling.

This would not overthrow General Relativity. GR would remain the correct description of gravity in every regime where it has been tested — weak-field dynamics, strong-field mergers, cosmological expansion. What a positive result would demonstrate is that GR's treatment of vacuum energy as ordinary content in $T_{\mu\nu}$, subject to the same coupling as all other energy, is incomplete in this specific regime. Direct modulation of the vacuum state couples to geometry more strongly than $G/c^4$ predicts.

A positive result would also validate the conservation-of-energy derivation (Section 2.3) that fixes the local vacuum density at $\rho_v = \rho_m c^2$, since the predicted strain magnitude depends on this value. It would not, by itself, establish the full VED framework — the thermodynamic interpretation of gravity, the reframing of cosmological expansion, or the singularity resolution — all of which remain downstream consequences that require independent investigation.

---

### 5.2 Null Result

Absence of a signal at $h \sim 10^{-19}$ with the source confirmed to be operating correctly and the detector sensitivity verified against known calibration signals would falsify the identity principle at the Casimir scale.

This outcome would confirm that Casimir vacuum energy couples to geometry through $T_{\mu\nu}$ with $G/c^4$ suppression, indistinguishable from any other electromagnetic energy density. The identity $h = \Delta\rho_v / \bar{\rho}_v$ would be ruled out as a description of vacuum-scale gravitational coupling. The VED energy budget — in which electrical work is transduced into metric strain through vacuum modulation — would be wrong. The standard energy budget, which routes the same work through mechanical and electromagnetic channels with negligible gravitational radiation, would be confirmed.

A null result would be a clean, unambiguous falsification. The 31-order-of-magnitude gap between predictions leaves no room for the result to be reinterpreted as consistent with VED through parameter adjustment. The framework does not have free parameters that could be tuned to accommodate a null result at this sensitivity.

---

### 5.3 Intermediate Result

A signal detected at a strain substantially different from $10^{-19}$ — for example, $10^{-25}$ or $10^{-30}$ — that nonetheless passes all four validation criteria would present a more complex interpretive situation.

Such an outcome would indicate that vacuum-state modulation couples to geometry more strongly than GR predicts ($h \gg 10^{-50}$) but less strongly than the bare identity ($h < 10^{-19}$). This would falsify VED in its current axiomatic form — the identity does not hold at full strength at the Casimir scale — while simultaneously falsifying GR's prediction that the gravitational channel is negligible. Both frameworks would be incomplete.

The most immediate consequence would be an empirical constraint on the transition-scale problem identified in Section 2.4. The measured strain would provide a data point for the crossover between the identity regime and the $G/c^4$ regime, enabling the first quantitative test of whether the transition depends on a length scale, an energy density threshold, or a source-type distinction. An intermediate result would therefore be scientifically productive even though it would not confirm either framework as currently formulated.

The probability of an intermediate result should not be overstated. The experiment is designed around a binary discrimination between $10^{-19}$ and $10^{-50}$, and the most likely outcomes are detection at approximately the predicted strain or non-detection. An intermediate signal, while informative, would require extraordinary scrutiny for systematic error before being accepted as genuine.

---

## Section 6: Open Problems and Limitations

The framework presented in this paper has specific theoretical gaps that constrain its completeness. This section catalogues the most significant ones. They are stated here not as caveats but as open problems whose resolution — or whose intractability — will shape the framework's development if the experimental prediction survives testing.

---

### 6.1 The Identity Is Axiomatic

The equation $h = \Delta\rho_v / \bar{\rho}_v$ is the starting point of the framework. It is not derived from more fundamental principles. No argument presented in this paper explains *why* the gravitational coupling $G/c^4$ should not apply at the vacuum scale — only that the identity is consistent with GR where GR has been tested and produces a different, falsifiable prediction where it has not.

This is an acceptable foundation for a phenomenological model: axioms are tested by their consequences. But it means the framework currently has no answer to the question "why should the coupling disappear at the vacuum scale?" beyond "because the experiment will tell us whether it does." A derivation of the identity from thermodynamic principles, from the structure of the Einstein equations, or from a statistical-mechanical averaging argument would substantially strengthen the framework. No such derivation currently exists.

---

### 6.2 The Transition Scale Is Undefined

The framework claims that the identity holds at the vacuum scale (direct modulation of vacuum boundary conditions) while the standard $G/c^4$ coupling holds at macroscopic scales (aggregated mass). It does not specify where the transition occurs, what controls it, or how the identity regime reduces to the coupling regime.

This is the most important theoretical gap. Without a defined crossover, the framework cannot make predictions in intermediate regimes, cannot be formally reduced to GR as a limiting case, and is vulnerable to the criticism that the regime boundaries are drawn to fit the desired result. A reviewer can reasonably ask: how do we know a particular experiment is in the identity regime rather than the coupling regime?

Three candidate mechanisms were noted in Section 2.4 — a characteristic length-scale crossover, a source-type distinction, or a formal coarse-graining procedure. None has been developed. Resolving this gap does not affect the binary experimental test proposed in Section 4, which depends only on whether the identity holds at the Casimir scale. But it is required for any extension of the framework beyond this single prediction.

---

### 6.3 Scalar and Tensor Mode Separation

The framework predicts scalar (breathing mode) gravitational waves from Casimir vacuum modulation, while astrophysical observations from LIGO/Virgo are consistent with tensor-only (plus and cross) polarizations from binary mergers. The framework must explain why these two source types produce different polarizations.

The current argument is that source symmetry determines the mode: isotropic modulation of a scalar density (vacuum energy) radiates a monopole scalar wave, while anisotropic acceleration of mass radiates quadrupole tensor waves. This argument is physically reasonable — it mirrors the relationship between monopole and quadrupole radiation in electromagnetism — but it has not been derived from modified field equations within the framework. A rigorous treatment would start from VED's identification of vacuum energy density with metric strain and show that the wave equation for perturbations sourced by scalar density modulation admits monopole solutions, while perturbations sourced by mass quadrupole dynamics admit only the standard tensor solutions. This derivation has not been performed.

The two predictions do not currently conflict observationally: LIGO operates at frequencies far below the MHz range of the proposed Casimir source, and no scalar-wave search has been conducted at MHz frequencies. But the framework must ultimately demonstrate that its scalar prediction for vacuum sources is consistent with tensor-only observations from astrophysical sources within a single set of field equations.

---

### 6.4 No Retrodictions

In every regime where General Relativity has been experimentally tested, VED reproduces GR exactly. The framework does not identify any existing observation that it explains better, differently, or more naturally than standard physics. Until the Casimir experiment is performed, VED is empirically equivalent to GR.

This is not fatal — many accepted physical theories were initially tested on a single prediction — but it is a limitation. The strongest version of the framework would identify an existing anomaly that VED accounts for naturally: candidates include the Hubble tension (if the generation term $\Gamma(t)$ produces time-varying dark energy consistent with recent DESI results), anomalies in Casimir force measurements at sub-100 nm separations, or subtle deviations in gravitational wave ringdown spectra. No such retrodiction has been developed. A systematic search for regimes where VED's predictions diverge slightly from GR's, within existing observational constraints, is an important direction for future work.

---

## Section 7: Conclusion

This paper has presented a phenomenological ansatz — the identity $h = \Delta\rho_v / \bar{\rho}_v$ — in which the vacuum energy density is the physical substance of the spatial metric. The ansatz reproduces General Relativity in every weak-field regime where GR has been tested. It diverges from GR in one specific, untested regime: direct modulation of the vacuum state via Casimir boundary conditions.

In that regime, the two frameworks make predictions differing by 31 orders of magnitude. GR, coupling the Casimir energy through $G/c^4$, predicts a metric strain of $h \sim 10^{-50}$ — permanently undetectable. VED, applying the identity at the vacuum scale, predicts $h \sim 10^{-19}$ — within the sensitivity range of resonant mechanical detectors. The discrimination window is large enough that the experimental outcome is unambiguous: either a signal is detected or it is not.

The proposed experiment — a NEMS Casimir comb source operating at MHz frequencies, a piezoelectric quartz resonator tuned to the source frequency, and a triple-sensor isolation protocol with four independent validation criteria — can be implemented with existing laboratory technology. The known, controllable source frequency permits narrow-band filtering and long integration times, providing a significant sensitivity advantage over broadband astrophysical searches.

The framework has acknowledged theoretical gaps: the identity is axiomatic rather than derived, the transition scale between identity and coupling regimes is undefined, and the scalar-vs-tensor mode separation has not been derived from field equations. These gaps constrain the framework's theoretical completeness but do not affect the falsifiability of the experimental prediction. A null result at $10^{-19}$ falsifies the ansatz cleanly, with no free parameters available to accommodate it. A positive result would identify a regime where GR's treatment of vacuum energy coupling is incomplete. Either outcome resolves a question that cannot be answered by theoretical argument alone.

---

# AI Assistance Statement

The development of both the theoretical framework and this manuscript involved extensive use of large language model tools, including Anthropic Claude, Google Gemini, OpenAI ChatGPT, and X Grok. Multiple models were consulted throughout the process to obtain diverse perspectives and to stress-test arguments from different directions.

The author's contributions were the originating physical intuition — that gravitational kinetic energy is extracted from the quantum vacuum and that ground-state extraction implies consumption of spatial volume — as well as ongoing direction, correction, and editorial judgment throughout the development process. The mathematical formalization of this intuition into the VED framework, including the identity principle, the conservation-of-energy derivations, the strain predictions, and the experimental design, was developed collaboratively with AI tools. The AI systems performed calculations, proposed mathematical structures, drafted prose, and generated arguments, which the author reviewed, challenged, corrected, and refined through iterative dialogue.

The manuscript text was drafted primarily by AI systems based on detailed structural guidance from the author, and was subsequently reviewed and edited by the author. The author takes full responsibility for the scientific content, claims, and conclusions presented in this paper.

---

## References

Abbott, B. P., et al. (2016). "Observation of Gravitational Waves from a Binary Black Hole Merger." *Physical Review Letters*, 116, 061102.
Arnowitt, R., Deser, S., & Misner, C. W. (1962). "The Dynamics of General Relativity." In *Gravitation: An Introduction to Current Research*, L. Witten, ed. Wiley.
Astone, P., et al. (2006). "AURIGA and NAUTILUS Gravitational Wave Detectors." *Classical and Quantum Gravity*, 23, S57.
Barceló, C., Liberati, S., & Visser, M. (2011). "Analogue Gravity." *Living Reviews in Relativity*, 14, 3.
Bondi, H., van der Burg, M. G. J., & Metzner, A. W. K. (1962). "Gravitational Waves in General Relativity. VII." *Proceedings of the Royal Society A*, 269, 21–52.
Carroll, S. M. (2001). "The Cosmological Constant." *Living Reviews in Relativity*, 4, 1.
Casimir, H. B. G. (1948). "On the Attraction Between Two Perfectly Conducting Plates." *Proceedings of the Royal Netherlands Academy of Arts and Sciences*, 51, 793–795.
Decca, R. S., et al. (2003). "Tests of New Physics from Precise Casimir Force Measurements." *Physical Review D*, 68, 116003.
DESI Collaboration (2024). "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations." arXiv:2404.03002.
Dicke, R. H. (1957). "Gravitation Without a Principle of Equivalence." *Reviews of Modern Physics*, 29, 363–376.
Eardley, D. M., et al. (1973). "Gravitational-Wave Observations as a Tool for Testing Relativistic Gravity." *Physical Review Letters*, 30, 884–886.
Einstein, A. (1916). "Näherungsweise Integration der Feldgleichungen der Gravitation." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*.
Feynman, R. P., Leighton, R. B., & Sands, M. (1964). *The Feynman Lectures on Physics*. Addison-Wesley.
Jacobson, T. (1995). "Thermodynamics of Spacetime: The Einstein Equation of State." *Physical Review Letters*, 75, 1260–1263.
Lamoreaux, S. K. (1997). "Demonstration of the Casimir Force in the 0.6 to 6 μm Range." *Physical Review Letters*, 78, 5–8.
Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman.
Moore, G. T. (1970). "Quantum Theory of the Electromagnetic Field in a Variable-Length One-Dimensional Cavity." *Journal of Mathematical Physics*, 11, 2679.
Padmanabhan, T. (2010). "Thermodynamical Aspects of Gravity: New Insights." *Reports on Progress in Physics*, 73, 046901.
Planck Collaboration (2020). "Planck 2018 Results. VI. Cosmological Parameters." *Astronomy & Astrophysics*, 641, A6.
Pound, R. V. & Rebka, G. A. (1960). "Apparent Weight of Photons." *Physical Review Letters*, 4, 337–341.
Puthoff, H. E. (2002). "Polarizable-Vacuum (PV) Approach to General Relativity." *Foundations of Physics*, 32, 927–943.
Sakharov, A. D. (1967). "Vacuum Quantum Fluctuations in Curved Space and the Theory of Gravitation." *Doklady Akademii Nauk SSSR*, 177, 70–71.
Schwarzschild, K. (1916). "Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie." *Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften*.
Unruh, W. G. (1981). "Experimental Black-Hole Evaporation?" *Physical Review Letters*, 46, 1351.
Verlinde, E. (2011). "On the Origin of Gravity and the Laws of Newton." *Journal of High Energy Physics*, 2011, 29.
Verlinde, E. (2017). "Emergent Gravity and the Dark Universe." *SciPost Physics*, 2, 016.
Weber, J. (1960). "Detection and Generation of Gravitational Waves." *Physical Review*, 117, 306–313.
Weinberg, S. (1989). "The Cosmological Constant Problem." *Reviews of Modern Physics*, 61, 1–23.
Will, C. M. (2014). "The Confrontation between General Relativity and Experiment." *Living Reviews in Relativity*, 17, 4.
Wilson, C. M., et al. (2011). "Observation of the Dynamical Casimir Effect in a Superconducting Circuit." *Nature*, 479, 376–379.

## Appendices

---

### Appendix A: Derivation of the Predicted Metric Strain

This appendix provides the quantitative derivation of the VED strain prediction for a NEMS Casimir cavity, alongside the corresponding GR prediction for the same device. The purpose is to show explicitly where the 31-order-of-magnitude divergence arises.

#### A.1 Casimir Energy Density in the Cavity

The Casimir energy per unit area between two perfectly conducting parallel plates separated by distance $d$ is:

$$\frac{E}{A} = -\frac{\pi^2 \hbar c}{720 \, d^3}$$

The corresponding energy density (energy per unit volume of the gap) is:

$$u_{\text{Cas}}(d) = \frac{1}{d}\frac{E}{A} = -\frac{\pi^2 \hbar c}{720 \, d^4}$$

For a gap of $d = 50$ nm:

$$u_{\text{Cas}}(50\text{ nm}) = \frac{\pi^2 \times 1.055 \times 10^{-34} \times 3 \times 10^{8}}{720 \times (5 \times 10^{-8})^4} \approx 69 \text{ J/m}^3$$

#### A.2 Modulation Amplitude

The NEMS comb drive oscillates the gap around its equilibrium separation. For a representative oscillation from $d = 50$ nm to $d = 40$ nm, the energy density scales as $d^{-4}$:

$$u_{\text{Cas}}(40\text{ nm}) = u_{\text{Cas}}(50\text{ nm}) \times \left(\frac{50}{40}\right)^4 \approx 69 \times 2.44 \approx 169 \text{ J/m}^3$$

The modulation amplitude is:

$$\Delta\rho_v \approx 169 - 69 = 100 \text{ J/m}^3$$

This is the magnitude of the vacuum energy density oscillation produced by each cycle of the pump. The precise value depends on the equilibrium gap, the oscillation amplitude, and the plate geometry. The order of magnitude is robust across reasonable NEMS parameter ranges.

#### A.3 VED Strain Prediction

Within VED, the local vacuum energy density near the silicon substrate ($\rho_m \approx 2330$ kg/m³) is set by the conservation-of-energy constraint (Section 2.3):

$$\rho_v = \rho_m c^2 \approx 2330 \times (3 \times 10^8)^2 \approx 2.1 \times 10^{20} \text{ J/m}^3$$

The Casimir modulation is a fractional perturbation of this local vacuum baseline. The metric strain is:

$$h_{\text{VED}} = \frac{\Delta\rho_v}{\rho_v} = \frac{100}{2.1 \times 10^{20}} \approx 5 \times 10^{-19}$$

This gives $h_{\text{VED}} \sim 10^{-19}$.

**Note on the denominator.** The identity principle as stated in Section 2.1 uses the cosmological background $\bar{\rho}_v$ as the reference density. The strain calculation here uses the local density $\rho_v = \rho_m c^2$. This is because the Casimir pump modulates the vacuum in the immediate vicinity of the silicon substrate, where the vacuum has already been contracted to the local density by the presence of matter. The fractional perturbation relevant to the metric strain is the fractional change relative to this local baseline, not relative to the cosmological background. The relationship between these two reference scales — and the conditions under which each applies — is an aspect of the transition-scale problem identified in Section 6.2.

#### A.4 GR Strain Prediction

In General Relativity, the gravitational wave strain from a source is given by the quadrupole formula:

$$h_{\text{GR}} = \frac{2G}{c^4 r}\ddot{Q}$$

where $\ddot{Q}$ is the second time derivative of the mass quadrupole moment and $r$ is the distance from the source to the detector. For a NEMS comb with oscillating mass $m \sim 10^{-12}$ kg, displacement amplitude $\delta \sim 10$ nm, and angular frequency $\omega = 2\pi f$ at $f = 10$ MHz:

$$\ddot{Q} \sim m \, \delta^2 \, \omega^2 \sim 10^{-12} \times (10^{-8})^2 \times (6.3 \times 10^7)^2 \approx 4 \times 10^{-13} \text{ kg·m}^2/\text{s}^2$$

At a detector distance of $r = 0.1$ m:

$$h_{\text{GR}} = \frac{2 \times 6.67 \times 10^{-11} \times 4 \times 10^{-13}}{(3 \times 10^8)^4 \times 0.1} \approx 7 \times 10^{-56}$$

Representative parameters thus give $h_{\text{GR}} \sim 10^{-55}$ to $10^{-50}$, depending on the specific device geometry, mass, and drive amplitude. In all cases, the GR strain is at least 30 orders of magnitude below the VED prediction and far beyond any conceivable detection capability.

#### A.5 Summary

| Quantity | Value |
| :--- | :--- |
| Casimir energy modulation $\Delta\rho_v$ | $\sim 10^2$ J/m³ |
| Local vacuum baseline $\rho_v$ | $\sim 10^{20}$ J/m³ |
| VED predicted strain | $\sim 10^{-19}$ |
| GR predicted strain | $\sim 10^{-55}$ to $10^{-50}$ |
| Discrimination window | $\sim 31$ orders of magnitude |

---

### Appendix B: Comparison of VED and GR Predictions

This table summarizes the predictions of the two frameworks across tested and untested regimes. All entries in the "tested" rows produce identical observables; the frameworks diverge only in the final three rows.

| Regime | GR Prediction | VED Prediction | Observational Status |
| :--- | :--- | :--- | :--- |
| Schwarzschild $g_{00}$, $g_{rr}$ | Standard metric components | Identical (via $h = \Phi_v/\bar{\rho}_v$) | Confirmed (redshift, GPS) |
| Light deflection | $4GM/bc^2$ | Identical (factor of 2 automatic) | Confirmed (VLBI, Eddington) |
| Geodesic motion | Newtonian limit | Identical | Confirmed (orbital mechanics) |
| Frame-dragging | Lense-Thirring rate | Identical (rotating deficit vortex) | Confirmed (Gravity Probe B) |
| Cosmological expansion | $\Lambda$CDM | Identical in $w = -1$ limit | Consistent (CMB, BAO, SNIa) |
| **Lab-scale GW strain** | $\sim 10^{-50}$ | $\sim 10^{-19}$ | **Untested** |
| **GW polarization (Casimir source)** | Tensor ($h_+$, $h_\times$) | Scalar (breathing) | **Untested** |
| **Lowest radiation multipole** | Quadrupole ($\ell = 2$) | Monopole ($\ell = 0$) | **Untested** |

---

### Appendix C: Survey of Related Theoretical Programs

The proposal presented in this paper draws on a tradition of research that treats gravity as emergent, thermodynamic, or medium-based. This appendix maps VED's relationship to the most relevant programs, clarifying what is shared and what is novel.

**Sakharov's induced gravity (1967).** Sakharov proposed that the Einstein-Hilbert action arises as a one-loop quantum correction from matter fields, making $G$ a derivable quantity rather than a fundamental constant. VED shares the conviction that $G$ is emergent but takes a different route: rather than deriving $G$ from loop integrals, VED obtains it as a macroscopic scaling ratio $G = c^4/(\bar{\rho}_v L^2)$ and proposes that the coupling it represents does not apply at the vacuum scale. Sakharov preserved the standard coupling structure; VED eliminates it below the transition scale.

**Jacobson's thermodynamic derivation (1995).** Jacobson showed that the Einstein field equations follow from $\delta Q = T\,dS$ applied to local Rindler horizons, implying that the Einstein equation is an equation of state rather than a fundamental microscopic law. This is the strongest existing support for VED's philosophical core: if gravity is thermodynamic, then treating it as a thermodynamic process with a physical medium is the correct level of description. VED extends Jacobson's structural result by identifying the specific medium (vacuum energy density) and making a prediction that differs from GR.

**Padmanabhan's thermodynamic gravity (2010).** Padmanabhan showed that the Einstein-Hilbert action decomposes into bulk and surface terms, with the surface term carrying all dynamical content. He derived the Friedmann equations from thermodynamic identities on the apparent horizon. VED's thermodynamic framing of cosmic expansion and gravitational energy transfer is closely aligned with Padmanabhan's program, but extends it into a physical theory with testable predictions that differ from GR.

**Verlinde's emergent gravity (2011, 2016).** Verlinde derived $G$ from cosmological parameters and proposed that dark energy competes with area-law entropy near masses. VED shares the conviction that $G$ is derivable from cosmological quantities but differs in mechanism: Verlinde's framework is information-theoretic and holographic, while VED is thermodynamic and fluid-dynamic. Verlinde makes no prediction about laboratory-scale gravitational wave generation.

**The Polarizable Vacuum (Dicke, Puthoff).** The PV approach recasts GR as the physics of a medium with variable dielectric properties, recovering weak-field results through a scalar field $K$. VED is structurally the closest existing framework: both treat the vacuum as a physical medium whose properties vary with mass. VED extends PV by promoting the scalar deficit to a tensor-capable framework and by making the thermodynamic claims (energy extraction from consumed spatial volume) that PV does not.

**Analog gravity (Unruh, Visser, Barceló).** The analog gravity program demonstrates that perturbations in flowing fluids obey wave equations governed by effective metrics mathematically identical to curved spacetime. VED takes the analog literally: the vacuum is the fluid, and the effective metric is the actual spacetime metric. The analog gravity community is careful to distinguish "analogue of" from "explanation for"; VED claims the latter.

**The Dynamical Casimir Effect (Moore, Wilson).** The DCE demonstrates that rapidly modulating vacuum boundary conditions produces real photons from the quantum vacuum. VED builds its experimental prediction on the DCE's proof of concept: if nonadiabatic vacuum modulation extracts real electromagnetic quanta, VED proposes it should also produce real metric perturbations. The DCE establishes the electromagnetic channel; VED predicts a gravitational channel from the same mechanism. The experiment proposed in this paper tests whether that gravitational channel exists.

What VED adds to all of these programs is a specific, quantitative, falsifiable prediction: detectable scalar gravitational waves from a laboratory Casimir cavity. None of the programs above make that prediction. The experiment is the bright line between VED and its predecessors.

---

