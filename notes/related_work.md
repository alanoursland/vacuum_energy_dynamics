# Related Work: VED in the Landscape of Theoretical Physics

VED does not emerge from a vacuum (so to speak). Several established research programs share structural features with VED — treating gravity as emergent, treating spacetime as a medium, or deriving Einstein's equations from thermodynamic principles. This document maps those connections, identifies where VED aligns with prior work, where it diverges, and what it claims to add.

Understanding this landscape is important for two reasons: it establishes that VED's core intuitions have serious precedent, and it clarifies exactly what is novel so that the new claims are not confused with the old ones.

-----

## 1. Sakharov's Induced Gravity (1967)

Andrei Sakharov proposed that gravity is not fundamental but emergent — that the Einstein-Hilbert action arises as a one-loop quantum correction from matter fields propagating on a background manifold. In his picture, the gravitational constant $G$ is not a free parameter of nature but is determined by the number and type of quantum fields present. Spacetime has an "elasticity" that resists curvature, and this elasticity is induced by vacuum fluctuations.

**Alignment with VED:** Sakharov's central claim — that gravity emerges from the vacuum rather than being put in by hand — is the same intuition driving VED. His framework also implies that $G$ is derivable rather than fundamental, which is exactly the claim in VED's [Derivation of G](derivation_of_g.md). The idea that vacuum fluctuations generate the rigidity of spacetime maps onto VED's claim that vacuum energy density *is* the metric substance.

**Divergence from VED:** Sakharov worked within the standard quantum field theory formalism. He derived $G$ from loop integrals over quantum fields, producing the correct Einstein-Hilbert action as an effective low-energy result. VED takes a more radical position: rather than deriving $G$ from QFT, it proposes that $G$ is an emergent scaling ratio ($G = c^4 / \bar{\rho}_v L^2$) and that at the vacuum scale the coupling is replaced entirely by the identity $h = \Delta\rho_v / \bar{\rho}_v$. Sakharov preserved the standard coupling structure; VED eliminates it at small scales.

**Key reference:** Sakharov, A. D. (1967). "Vacuum Quantum Fluctuations in Curved Space and the Theory of Gravitation." *Doklady Akademii Nauk SSSR*, 177, 70–71. See also Visser, M. (2002). "Sakharov's Induced Gravity: A Modern Perspective." *Modern Physics Letters A*, 17, 977–991. arXiv: gr-qc/0204062.

-----

## 2. The Polarizable Vacuum (Dicke, Puthoff)

Beginning with Robert Dicke in the 1950s and developed extensively by Harold Puthoff from the late 1990s onward, the Polarizable Vacuum (PV) approach recasts general relativity as the physics of a medium with variable dielectric properties. In PV, the presence of mass changes the vacuum's effective permittivity and permeability by a scalar factor $K$, which in turn alters the speed of light, the length of rulers, and the rate of clocks. The standard GR weak-field predictions (gravitational redshift, light deflection, perihelion precession) are recovered exactly.

**Alignment with VED:** PV is structurally the closest existing framework to VED. Both treat the vacuum as a physical medium whose properties vary in the presence of mass. Both recover Schwarzschild-level GR results through medium-based reasoning. VED's refractive index derivation ($n(r) \approx 1 + 2GM/rc^2$) is essentially the same mathematical object as Puthoff's dielectric function $K$. Both programs use the language of "metric engineering" — the idea that if you understand the medium, you can in principle manipulate it.

**Divergence from VED:** PV remains an analogy — it reformulates GR in optical language but does not claim the vacuum literally *is* energy in the way VED does. PV uses a scalar field $K$ and therefore cannot reproduce the full tensor structure of GR (it fails for the Kerr metric and for gravitational wave inspiral rates, as shown by Ibison in 2003). VED explicitly addresses this limitation by promoting the scalar deficit $\Phi_v$ to a full deficit tensor $\Delta V_{\mu\nu}$, preserving the tensor degrees of freedom needed for rotation and radiation.

PV also does not make the thermodynamic claims central to VED — it does not frame gravity as energy extraction from a consumable medium, and it does not predict scalar gravitational waves from vacuum modulation.

**Critical note:** The PV program has been classified as "fringe physics" by parts of the mainstream community, partly due to the known limitations of scalar gravity theories (no scalar theory can reproduce all of GR's successes, per the Weinberg-Witten theorem and related no-go results). VED must carefully distinguish its tensor-capable framework from PV's scalar limitation to avoid the same classification.

**Key references:** Puthoff, H. E. (2002). "Polarizable-Vacuum (PV) Approach to General Relativity." *Foundations of Physics*, 32, 927–943. Dicke, R. H. (1957). "Gravitation Without a Principle of Equivalence." *Reviews of Modern Physics*, 29, 363–376.

-----

## 3. Jacobson's Thermodynamic Derivation (1995)

Ted Jacobson showed that the Einstein field equations can be derived from the fundamental thermodynamic relation $\delta Q = T \, dS$, applied to local Rindler horizons at every spacetime point. The temperature is the Unruh temperature seen by an accelerated observer, the heat flux is the energy flowing through the horizon, and the entropy is proportional to the horizon area. This derivation implies that the Einstein equation is an equation of state — a macroscopic thermodynamic identity — rather than a fundamental microscopic law.

**Alignment with VED:** Jacobson's result is perhaps the strongest existing support for VED's philosophical core. If the Einstein equation is thermodynamic, then treating gravity as a thermodynamic process (as VED does in [Gravitational Energy Transfer](gravitational_energy_transfer.md)) is not a metaphor — it is the correct level of description. Jacobson's conclusion that "it may be no more appropriate to canonically quantize the Einstein equation than it would be to quantize the wave equation for sound in air" aligns directly with VED's position that gravity is emergent from a medium rather than fundamental.

**Divergence from VED:** Jacobson derived the Einstein equations; he did not propose a specific physical medium or predict new phenomena. His work is a structural result about the thermodynamic form of GR, not a competing theory with different predictions. VED goes further by identifying the medium (the vacuum energy field), specifying its dynamics ($d\bar{\rho}_v/dt = \Gamma(t)$), and making predictions that differ from GR (scalar gravitational waves from Casimir modulation). Jacobson would likely view VED's specific claims about the vacuum medium as going beyond what his derivation supports.

**Key reference:** Jacobson, T. (1995). "Thermodynamics of Spacetime: The Einstein Equation of State." *Physical Review Letters*, 75, 1260–1263. arXiv: gr-qc/9504004.

-----

## 4. Verlinde's Emergent / Entropic Gravity (2011, 2016)

Erik Verlinde proposed that gravity is an entropic force arising from changes in the information associated with material bodies' positions, building on the holographic principle and black hole thermodynamics. In his 2016 extension, he argued that dark energy (the de Sitter entropy associated with the cosmological horizon) competes with the area-law entropy near masses, producing an additional "dark gravitational force" that could explain galaxy rotation curves without dark matter. He derived the MOND acceleration scale $a_0 \sim cH_0$ from cosmological parameters.

**Alignment with VED:** Verlinde's program shares VED's conviction that gravity is emergent and thermodynamic, that $G$ is derivable from cosmological quantities, and that dark energy is intimately connected to gravitational dynamics. His derivation of $a_0$ from $H_0$ is structurally similar to VED's derivation of $G$ from $\bar{\rho}_v$ and a cosmological length scale — both programs claim the gravitational coupling emerges from the large-scale properties of the universe.

**Divergence from VED:** Verlinde's framework is information-theoretic and holographic; VED is thermodynamic and fluid-dynamic. Verlinde does not identify a specific physical medium — his "microscopic degrees of freedom" are abstract informational entities on holographic screens. VED claims the medium is concrete: it is the vacuum energy density, and it can be physically manipulated (via Casimir cavities). Verlinde makes no prediction about laboratory-scale gravitational wave generation; VED does.

Verlinde's emergent gravity has faced observational challenges (inconsistency with some dwarf galaxy rotation curves, and the criticism by Wang and Braunstein (2018) that ordinary spacetime surfaces do not obey thermodynamic first laws). VED's experimental test is more direct: the Casimir cavity experiment produces a binary result.

**Key references:** Verlinde, E. (2011). "On the Origin of Gravity and the Laws of Newton." *Journal of High Energy Physics*, 2011, 29. Verlinde, E. (2017). "Emergent Gravity and the Dark Universe." *SciPost Physics*, 2, 016. arXiv: 1611.02269.

-----

## 5. Analog Gravity (Unruh, Visser, Barceló)

The analog gravity program, initiated by Unruh in 1981 and extensively developed by Visser, Barceló, and others, uses physical systems (flowing fluids, Bose-Einstein condensates, optical media) to simulate curved-spacetime effects in the laboratory. The key insight is that perturbations in a moving fluid obey a wave equation governed by an "effective metric" that is mathematically identical to a curved spacetime metric. Sonic horizons in supersonic flows are the acoustic analog of black hole event horizons, and phononic Hawking radiation has been experimentally observed (Steinhauer, 2016).

**Alignment with VED:** VED is, in one sense, an analog gravity model taken literally — it proposes that the vacuum itself is the fluid, and that the effective metric is not an analogy but the actual spacetime metric. VED's "river model" of black holes (space flowing inward faster than light) is directly borrowed from the analog gravity toolkit (Hamilton and Lisle, 2008). The refractive index formulation ($n(r) \approx 1 + 2GM/rc^2$) is the Gordon metric — a standard result from the analog gravity literature.

**Divergence from VED:** Analog gravity models are explicitly analogies. They capture the *kinematic* features of curved spacetime (wave propagation, horizons, Hawking radiation) but not the *dynamics* (they do not reproduce the Einstein field equations). The analog gravity community is careful to distinguish "analogue of" from "explanation for." VED claims to be the latter — not that fluids can simulate gravity, but that gravity literally *is* the hydrodynamics of the vacuum energy field.

This is a much stronger claim and carries a correspondingly higher burden of proof. The analog gravity program has shown that Hawking radiation is a generic feature of any system with a horizon in an effective geometry — it does not require Einstein's equations specifically. VED can use this result to support its dynamical Casimir mechanism for black hole evaporation, but it cannot cite analog gravity as support for the identity $h = \Delta\rho_v / \bar{\rho}_v$, which goes beyond anything the analog program claims.

**Key references:** Unruh, W. G. (1981). "Experimental Black-Hole Evaporation?" *Physical Review Letters*, 46, 1351. Barceló, C., Liberati, S., & Visser, M. (2005, 2011). "Analogue Gravity." *Living Reviews in Relativity*, 8, 12 (updated 14, 3). Visser, M. (1998). "Acoustic Black Holes: Horizons, Ergospheres, and Hawking Radiation." *Classical and Quantum Gravity*, 15, 1767.

-----

## 6. Padmanabhan's Thermodynamic Gravity

T. Padmanabhan developed an extensive program arguing that gravitational dynamics are fundamentally thermodynamic. He showed that the Einstein-Hilbert action can be decomposed into a bulk term and a surface term, and that the surface term carries all the dynamical content — suggesting that gravity is a boundary phenomenon tied to horizon thermodynamics. He derived the Friedmann equations from thermodynamic identities applied to the apparent horizon, and argued that spacetime has microscopic degrees of freedom whose dynamics give rise to Einstein's equations.

**Alignment with VED:** Padmanabhan's program provides the most rigorous existing support for VED's thermodynamic framing. His demonstration that the Friedmann equations follow from $\delta Q = T \, dS$ on the apparent horizon directly supports VED's treatment of cosmic expansion as a thermodynamic process. His emphasis on the surface/bulk decomposition resonates with VED's distinction between the cosmological background $\bar{\rho}_v$ (bulk) and localized deficits $\Phi_v$ (boundary-mediated).

**Divergence from VED:** Padmanabhan works entirely within the mathematical structure of GR. He reinterprets existing equations thermodynamically but does not propose a specific medium, does not eliminate $G$ as fundamental, and does not predict new phenomena. VED extends the thermodynamic interpretation into a physical theory with testable predictions that differ from GR.

**Key reference:** Padmanabhan, T. (2010). "Thermodynamical Aspects of Gravity: New Insights." *Reports on Progress in Physics*, 73, 046901.

-----

## 7. Stochastic Electrodynamics (Boyer, Cole, Puthoff)

Stochastic Electrodynamics (SED) is a research program that treats the quantum vacuum zero-point field (ZPF) as a real, classical, stochastic electromagnetic field rather than a mathematical artifact of quantization. In SED, the vacuum is not empty — it is filled with a fluctuating electromagnetic radiation field whose spectral energy density is $\rho(\omega) = \hbar\omega^3 / 2\pi^2 c^3$. SED attempts to reproduce quantum mechanical results (atomic stability, the blackbody spectrum, van der Waals forces) from classical electrodynamics plus this real background field. Cole and Zou (2003) showed that in SED simulations, electron orbits in hydrogen are stabilized by a balance between Larmor radiation loss and ZPF absorption — the electron is dynamically sustained by continuous interaction with the vacuum field.

**Alignment with VED:** SED provides VED's closest ontological ally. Both programs treat the vacuum as a real, physical, dynamical energy field — not a bookkeeping artifact. The Cole and Zou result maps directly onto VED's picture of matter as a dynamic process sustained by vacuum interaction: mass is not a static property but a steady-state condition maintained by continuous energy exchange with the vacuum. SED also supports VED's claim that the vacuum is a "consumable medium" — if the ZPF is real and interacts with matter, then local modifications to the ZPF (such as those produced by Casimir boundaries) are real physical changes, not merely formal ones.

**Divergence from VED:** SED works within classical electrodynamics and does not make claims about spacetime geometry. It treats the ZPF as an electromagnetic field in flat spacetime, not as the substance of the metric. SED does not propose an identity between energy density and metric strain, does not predict scalar gravitational waves, and does not claim that $G$ is emergent. VED extends the SED ontology (the vacuum is real and dynamical) into a gravitational framework (the vacuum is the metric).

**Key references:** Boyer, T. H. (1975). "Random Electrodynamics: The Theory of Classical Electrodynamics with Classical Electromagnetic Zero-Point Radiation." *Physical Review D*, 11, 790. Cole, D. C. & Zou, Y. (2003). "Quantum Mechanical Ground State of Hydrogen Obtained from Classical Electrodynamics." *Physics Letters A*, 317, 14–20. de la Peña, L. & Cetto, A. M. (1996). *The Quantum Dice: An Introduction to Stochastic Electrodynamics*. Kluwer.

-----

## 8. Quantum Energy Teleportation (Hotta)

Masahiro Hotta proposed in 2008 that quantum vacuum entanglement can mediate real energy transfer between spatially separated regions without any physical carrier traversing the gap. In Quantum Energy Teleportation (QET), a measurement at one location extracts information about the local vacuum state, which is communicated classically to a distant location, where a conditional operation extracts real energy from the vacuum using the correlations. QET has been experimentally demonstrated in quantum spin chains and superconducting circuits.

**Alignment with VED:** QET proves a specific mechanism that VED's broader framework relies on: the vacuum is not merely a passive background but a medium through which real energy can be transferred via its internal correlations. If vacuum entanglement can mediate energy transfer in QET, it supports VED's claim that the vacuum is a dynamical energy field capable of participating in physical processes — not just a ground state from which nothing can be extracted.

**Divergence from VED:** QET is a narrow, well-defined quantum information protocol. It does not make claims about gravity, spacetime geometry, or the identity between energy density and metric strain. The energy transfers in QET are microscopic and mediated by classical communication of measurement results — a very different mechanism from VED's proposed macroscopic vacuum energy modulation via Casimir cavities. VED cannot cite QET as evidence for its specific predictions, only as evidence that the vacuum is a richer physical system than the "inert ground state" picture suggests.

**Key references:** Hotta, M. (2008). "A Protocol for Quantum Energy Distribution." *Physics Letters A*, 372, 5671–5676. Hotta, M. (2010). "Quantum Energy Teleportation with Electromagnetic Field: Discrete vs. Continuous Variable Schemes." *Journal of Physics A*, 43, 105305.

-----

## 9. The Dynamical Casimir Effect (Moore, Wilson)

Predicted by Moore in 1970 and experimentally confirmed by Wilson et al. in 2011 using a superconducting circuit, the Dynamical Casimir Effect (DCE) demonstrates that rapidly modulating vacuum boundary conditions produces real photons from the quantum vacuum. The DCE is a direct experimental proof that the vacuum is a physical system from which real energy can be extracted by nonadiabatic driving.

**Alignment with VED:** The DCE is the experimental cornerstone that VED builds its Casimir cavity prediction upon. If the vacuum can produce real photons when boundaries are modulated (electromagnetic channel), VED argues it should also produce real metric perturbations (gravitational channel). The DCE provides the proof of concept that nonadiabatic vacuum modulation has physical consequences.

**Divergence from VED:** The DCE produces electromagnetic quanta — photons — from modulation of electromagnetic boundary conditions. VED's prediction requires a different channel: metric perturbations (scalar gravitational waves) from modulation of vacuum energy density. The DCE does not establish that metric perturbations follow from the same mechanism. That is the leap VED makes, and it is the leap the Casimir cavity experiment is designed to test.

**Key references:** Moore, G. T. (1970). "Quantum Theory of the Electromagnetic Field in a Variable-Length One-Dimensional Cavity." *Journal of Mathematical Physics*, 11, 2679. Wilson, C. M. et al. (2011). "Observation of the Dynamical Casimir Effect in a Superconducting Circuit." *Nature*, 479, 376–379.

-----

## 10. The Gordon Metric and Gravitational Optics

Walter Gordon (1923) showed that light propagation in a moving dielectric medium is mathematically equivalent to propagation in a curved spacetime with an effective metric. This "Gordon metric" formalism has been used extensively to derive gravitational lensing and light deflection from a refractive-index perspective. In the weak-field limit, the Schwarzschild geometry acts on light exactly like a medium with refractive index $n(r) = 1 + 2GM/rc^2$.

**Alignment with VED:** VED's derivation of light deflection via Huygens' principle and a spatially varying refractive index is a direct application of the Gordon metric. The factor-of-2 in the deflection angle, which Soldner and early Einstein missed, follows automatically from VED because the energy deficit and spatial contraction are identified as the same event — both temporal and spatial components of the effective refractive index contribute simultaneously.

**Divergence from VED:** The Gordon metric is a mathematical reformulation, not a physical claim about the nature of the vacuum. VED takes the refractive index literally — the vacuum has variable optical properties because its energy density varies, and this is the physical mechanism of gravity. The Gordon formalism treats it as a useful calculational tool.

**Key reference:** Gordon, W. (1923). "Zur Lichtfortpflanzung nach der Relativitätstheorie." *Annalen der Physik*, 377, 421–456.

-----

## 11. Wheeler's Geometrodynamics (1955–1973)

John Archibald Wheeler — who coined the term "black hole" — spent decades developing a program he called Geometrodynamics. His goal was to show that all physical phenomena, including particles and fields, could be reduced to the geometry of spacetime. His slogan was "mass without mass, charge without charge, field without field" — the idea that what we call matter is really just highly concentrated, topologically complex spacetime geometry. Wheeler envisioned "geons" (gravitational-electromagnetic entities): self-sustaining knots of curved spacetime that would behave like particles without containing any material substance.

**Alignment with VED:** Wheeler and VED arrive at the same destination from opposite directions. Wheeler tried to eliminate energy in favor of geometry: everything is curvature. VED tries to eliminate geometry in favor of energy: everything is vacuum energy density. Both programs deny that mass, energy, and spatial geometry are independent entities. Both conclude that what we call "mass" is a particular configuration of the underlying substrate — for Wheeler, a knot in the metric; for VED, a deficit in the vacuum energy field. Wheeler's program also treated spacetime as a dynamical, physical entity rather than a passive background, which is the same ontological commitment VED makes.

**Divergence from VED:** Wheeler worked entirely within (and beyond) the mathematical framework of GR, using topology and quantum gravity concepts that VED does not invoke. His program ultimately stalled because the "geons" were unstable and the topological structures he needed could not be shown to reproduce the observed particle spectrum. VED avoids this problem by not attempting to derive particle physics from the vacuum — it treats mass as a "black box" (a localized vacuum deficit) without specifying the internal structure. VED is also thermodynamic where Wheeler was geometric; VED frames gravity as energy transfer from a medium, while Wheeler framed it as pure geometry with no medium at all.

**Key references:** Wheeler, J. A. (1955). "Geons." *Physical Review*, 97, 511–536. Wheeler, J. A. (1962). *Geometrodynamics*. Academic Press. Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman. (Especially Chapters 43–44 on superspace and geometrodynamics.)

-----

## Summary: Where VED Sits

| Program | Shared with VED | Distinct from VED |
| :--- | :--- | :--- |
| **Sakharov** | $G$ is emergent from vacuum | Stays within QFT; preserves coupling structure |
| **Polarizable Vacuum** | Vacuum as medium; metric engineering | Scalar only; no thermodynamics; fringe status |
| **Jacobson** | Einstein equation is thermodynamic | No specific medium; no new predictions |
| **Verlinde** | Gravity is emergent; $G$ from cosmology | Information-theoretic; no laboratory prediction |
| **Analog Gravity** | Fluid models of curved spacetime | Explicit analogy, not literal claim |
| **Padmanabhan** | Thermodynamic derivation of GR | Works within GR; no new phenomena |
| **SED** | Vacuum is a real, dynamical energy field | Electromagnetic only; no geometric claims |
| **QET (Hotta)** | Vacuum mediates real energy transfer | Narrow QI protocol; no gravity connection |
| **Dynamical Casimir** | Vacuum modulation produces real quanta | Electromagnetic channel only |
| **Gordon Metric** | Refractive-index gravity | Mathematical tool, not physical claim |
| **Wheeler** | Mass/energy/geometry are one entity | Pure geometry; no medium; no thermodynamics |

VED draws on all of these programs. Its thermodynamic framing comes from Jacobson and Padmanabhan. Its medium-based picture inherits from Dicke, Puthoff, and the analog gravity program. Its experimental prediction builds on the Dynamical Casimir Effect. Its claim that $G$ is emergent echoes Sakharov and Verlinde.

What VED adds — and what separates it from all of the above — is the specific identity $h = \Delta\rho_v / \bar{\rho}_v$, the claim that this identity replaces the coupling constant at the vacuum scale, and the resulting prediction of detectable scalar gravitational waves from a laboratory Casimir cavity. None of the programs above make that prediction. The experiment is the bright line between VED and its predecessors.

-----

## References

1. Sakharov, A. D. (1967). "Vacuum Quantum Fluctuations in Curved Space and the Theory of Gravitation." *Doklady Akademii Nauk SSSR*, 177, 70–71.
2. Visser, M. (2002). "Sakharov's Induced Gravity: A Modern Perspective." *Modern Physics Letters A*, 17, 977–991.
3. Dicke, R. H. (1957). "Gravitation Without a Principle of Equivalence." *Reviews of Modern Physics*, 29, 363–376.
4. Puthoff, H. E. (2002). "Polarizable-Vacuum (PV) Approach to General Relativity." *Foundations of Physics*, 32, 927–943.
5. Jacobson, T. (1995). "Thermodynamics of Spacetime: The Einstein Equation of State." *Physical Review Letters*, 75, 1260–1263.
6. Verlinde, E. (2011). "On the Origin of Gravity and the Laws of Newton." *Journal of High Energy Physics*, 2011, 29.
7. Verlinde, E. (2017). "Emergent Gravity and the Dark Universe." *SciPost Physics*, 2, 016.
8. Unruh, W. G. (1981). "Experimental Black-Hole Evaporation?" *Physical Review Letters*, 46, 1351.
9. Barceló, C., Liberati, S., & Visser, M. (2005, 2011). "Analogue Gravity." *Living Reviews in Relativity*, 8, 12 (updated 14, 3).
10. Padmanabhan, T. (2010). "Thermodynamical Aspects of Gravity: New Insights." *Reports on Progress in Physics*, 73, 046901.
11. Moore, G. T. (1970). "Quantum Theory of the Electromagnetic Field in a Variable-Length One-Dimensional Cavity." *Journal of Mathematical Physics*, 11, 2679.
12. Wilson, C. M. et al. (2011). "Observation of the Dynamical Casimir Effect in a Superconducting Circuit." *Nature*, 479, 376–379.
13. Gordon, W. (1923). "Zur Lichtfortpflanzung nach der Relativitätstheorie." *Annalen der Physik*, 377, 421–456.
14. Hamilton, A. J. S. & Lisle, J. P. (2008). "The River Model of Black Holes." *American Journal of Physics*, 76, 519–532.
15. Wheeler, J. A. (1955). "Geons." *Physical Review*, 97, 511–536.
16. Wheeler, J. A. (1962). *Geometrodynamics*. Academic Press.
17. Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman.
18. Boyer, T. H. (1975). "Random Electrodynamics: The Theory of Classical Electrodynamics with Classical Electromagnetic Zero-Point Radiation." *Physical Review D*, 11, 790.
19. Cole, D. C. & Zou, Y. (2003). "Quantum Mechanical Ground State of Hydrogen Obtained from Classical Electrodynamics." *Physics Letters A*, 317, 14–20.
20. de la Peña, L. & Cetto, A. M. (1996). *The Quantum Dice: An Introduction to Stochastic Electrodynamics*. Kluwer.
21. Hotta, M. (2008). "A Protocol for Quantum Energy Distribution." *Physics Letters A*, 372, 5671–5676.
22. Hotta, M. (2010). "Quantum Energy Teleportation with Electromagnetic Field: Discrete vs. Continuous Variable Schemes." *Journal of Physics A*, 43, 105305.