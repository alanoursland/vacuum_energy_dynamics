# The Power Problem in VED's Gravitational Wave Prediction

## Summary

Vacuum Energy Dynamics (VED) predicts that a NEMS Casimir cavity oscillating at MHz frequencies will radiate scalar ("breathing mode") gravitational waves with strain amplitude *h* ~ 10⁻¹⁹ at a nearby detector. The strain prediction is derived cleanly from the identity principle and a conservation-of-energy argument that fixes the local vacuum energy density at ρᵥ = ρₘc². The framework is internally consistent up to that point.

But strain at a distant detector is not the same thing as energy flux from the source, and any radiating wave — reactive near field or not — must carry net positive energy outward in proportion to the square of its amplitude. VED specifies the strain amplitude. It does not specify the relationship between strain amplitude and radiated power. That gap is the power problem, and it sits between the framework's prediction and the experimental claim that a quartz resonator can detect the wave.

## The reactive defense and what it accomplishes

A natural first objection to VED is that radiating significant gravitational power from a tabletop device should show up as a missing-energy anomaly in precision Casimir measurements, and no such anomaly is observed. This objection can be answered: the vacuum oscillation in VED is mean-zero. Gap closing destroys vacuum energy (positive-phase strain); gap opening recreates it (negative-phase strain). Over a full cycle, the net energy change in the local vacuum is zero. The pump is dominantly reactive, like a capacitor in an AC circuit — energy sloshes between the actuator and the vacuum without net dissipation. Static Casimir force measurements would not see a sink because there is no sink to see.

This defense is correct as far as it goes, and it dissolves the naive energy-budget objection. The "all voltage and no current" framing captures the right intuition: the dominant energy economy of the device is reactive storage and recovery, not radiative loss.

## Where the defense becomes insufficient

The experimental proposal requires that the wave reach a quartz resonator placed at some distance from the source — tens of centimeters in the proposed geometry — and deposit enough energy in the crystal to produce a measurable piezoelectric signal. The moment a wave propagates from a source to a distant detector and does work on that detector, it is no longer purely reactive. Energy has been transported across space. That transport requires a real (not imaginary) component of the radiated flux.

This is the same distinction that governs antennas in classical electromagnetism. A driven dipole is dominantly reactive, with most of the input energy stored in the near field and returned to the source each cycle. But a small fraction of the input couples into the radiation resistance — the real part of the impedance that represents power leaving as propagating EM waves. That small fraction is what reaches a distant receiver. Without it, there is nothing to detect.

VED's Casimir pump must therefore have an analogous radiative component. Most of the work the actuator performs is recovered each cycle (the reactive bulk), but some fraction leaks into the propagating scalar mode that reaches the detector. The size of that fraction determines two things simultaneously: how much power the device radiates, and how much energy the detector receives per unit time. These are not independent quantities — they are linked by whatever propagator governs the scalar channel.

## The missing relation

In standard physics, the link between strain amplitude and radiated power is fixed by the field equations of the theory in question. Maxwell's equations give the EM Poynting flux. Einstein's equations give the gravitational wave power as

$$ P_{\text{GW}} \sim \frac{c^3}{G} \, h^2 \, f^2 \, A $$

for a wave of strain *h* and frequency *f* crossing area *A*. The coupling constant c³/G is large, which is why detectable gravitational waves carry enormous power — LIGO's binary merger sources radiate solar-mass equivalents of energy in seconds.

VED explicitly rejects the c³/G coupling at the vacuum scale. That is the entire content of the identity principle: vacuum modulation couples to geometry through *h* = Δρᵥ/ρ̄ᵥ rather than through G/c⁴. But once that coupling is removed, the framework no longer has a formula relating strain to radiated power. The strain prediction *h* ~ 10⁻¹⁹ stands; the corresponding power flux is undefined.

This is not a minor omission. The detection argument depends on it. A quartz piezoelectric resonator does not respond to "strain" as an abstract geometric quantity — it responds to mechanical deformation of its bulk, which requires energy to be deposited in the crystal lattice. The amount of energy deposited per cycle depends on the wave's energy flux, the crystal's cross-section, and its coupling to the mode. Without a strain-to-flux relation, you cannot calculate whether the predicted wave actually moves the crystal enough to register above thermal noise.

## Two horns of the dilemma

The framework can be pushed in two directions, and neither is comfortable.

**If the strain-to-power relation is anything like the GR formula** — using c³/G or any coupling within a few orders of magnitude of it — then *h* ~ 10⁻¹⁹ at 10 MHz corresponds to a radiated power density on the order of 10¹² W/m². This is absurd. The NEMS device would vaporize within microseconds, and the discrepancy with observed Casimir experiments (which do not vaporize) would be obvious without any new detector. So this branch is ruled out by inspection.

**If the strain-to-power relation is much weaker** — so weak that *h* ~ 10⁻¹⁹ corresponds to a radiated power small enough to be hidden in the noise floor of existing experiments — then the framework is energetically consistent with what we already know. But this branch creates a new problem: the energy reaching the quartz detector per cycle is also tiny, by the same factor. The detector responds to deposited energy, not to bare strain amplitude. If the wave carries almost no power, the crystal barely moves, and the detection prediction loses its quantitative grounding. The argument "h ~ 10⁻¹⁹ is within reach of resonant mechanical detectors" implicitly assumes a strain-to-energy conversion comparable to what tensor gravitational waves provide, because that is the regime in which historical resonant-bar sensitivity figures were calibrated. If VED's scalar channel has a fundamentally different (weaker) coupling, the sensitivity comparison to AURIGA or NAUTILUS no longer applies in the way the paper suggests.

The framework needs to land somewhere between these extremes: weak enough not to vaporize the source or contradict precision Casimir measurements, strong enough to drive a quartz resonator above its noise floor. Whether such a window exists depends on the radiation resistance of the scalar channel, which the framework does not derive.

## Why this is harder than it looks

One might hope to fix the problem by writing down a wave equation for vacuum perturbations within VED and reading off the propagator. But the framework as currently formulated does not have such an equation. The identity *h* = Δρᵥ/ρ̄ᵥ is a local relation between vacuum density and metric strain. It is not a dynamical equation governing how perturbations propagate, what their dispersion relation is, how they couple to detectors, or what their stress-energy carries. All of those would need to be derived from a more fundamental Lagrangian or field equation that the paper does not provide.

Section 6 of the paper acknowledges related gaps — the identity is axiomatic, the transition between identity and coupling regimes is undefined, the scalar-vs-tensor mode separation has not been derived from field equations. The power problem is a specific instance of the same family of gaps. Without a wave equation for the scalar mode, the framework can predict that a strain exists at the detector location, but it cannot predict the energy flux carrying that strain, and therefore cannot predict the detector response in a calculable way.

## What this does and does not falsify

The power problem is not a refutation of VED. It is a gap in the chain of reasoning between the axiom and the experimental claim. The identity principle could still be correct; the conservation-of-energy derivation of the local vacuum density could still be correct; the prediction of scalar modes from vacuum modulation could still be correct. What is missing is the dynamical content needed to translate any of these into a quantitative prediction for what a detector will measure.

A serious development of the framework would need to do at least one of the following: derive a wave equation for scalar vacuum perturbations from a candidate Lagrangian; specify the radiation resistance of the scalar channel by some independent argument; or identify the strain-to-flux coupling constant empirically by calibration against a known scalar source (which raises the obvious problem that no known scalar source exists). Until one of these is done, the experimental prediction is half-specified — the strain amplitude is set, but the power carried by that strain is not, and detector response calculations therefore rest on an assumed coupling that the framework has not earned.

## A note on what would change the picture

If the experiment were performed and a signal at *h* ~ 10⁻¹⁹ were detected at the predicted frequency, the power problem would resolve itself empirically: the measured detector response would imply a specific strain-to-energy coupling for the scalar channel, and the framework would be retrofitted with that value. The experiment is therefore worth running even with the gap unresolved, because a positive result would supply the missing constant. But a null result would be ambiguous in a way the paper does not fully acknowledge: it could mean the identity principle is wrong, *or* it could mean the scalar channel's radiation resistance is too small for the wave to deposit detectable energy in a quartz resonator even though the strain at the detector location is technically *h* ~ 10⁻¹⁹. These are different failure modes, and the proposed experiment cannot distinguish them.

The cleanest version of VED would close this gap before going to the bench. The current version asks the experiment to do work that the theory has not yet done.

## Proposed Resolution: The Scalar Flux Equation

While this gap represents a critical vulnerability in the initial framing, the framework has since been updated to include a formal mathematical solution. By defining the VED scalar wave equation and its corresponding energy flux vector (detailed in `scalar_wave_equation.md`), we can mathematically link the metric strain to the energy flux.

The derivation proves that the total radiated power $P$ scales with the square of the strain's time derivative ($\dot{h}^2$). This formally resolves the "mean-zero" paradox: even though the strain amplitude $h$ oscillates between positive (vacuum compression) and negative (vacuum rarefaction) phases, the squared rate of change ensures the wave carries strictly positive energy away from the source.

By establishing this scalar flux equation, the framework now provides the missing link required to calculate the exact radiation resistance acting on the NEMS pump. This proves that the wave can carry detectable energy without violating thermodynamic laws, closing the gap between the predicted strain and the required mechanical work.