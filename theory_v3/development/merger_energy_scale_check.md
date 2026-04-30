# Merger Energy Scale: A Consistency Check for the Configuration-Energy Functional

## What This Document Is

This document records a development target. It identifies a specific quantitative consistency check that the framework's future configuration-energy functional must pass, and explains why this check is the natural first test for distinguishing the framework from a pure ontological reformulation of general relativity.

The document is not a postulate, theorem, or prediction. It is a planning note. It describes work that cannot be completed at the framework's current development stage, because the configuration-energy functional has not yet been specified. The document's role is to make explicit what the future functional will need to reproduce, so that the work of constructing the functional is guided by clear targets.

## The Check

Binary mergers release energy. The release is observed: LIGO and similar detectors have measured gravitational wave signals from binary black hole and binary neutron star mergers, and the radiated energy can be inferred from the signal. For a typical binary black hole merger, a few percent of the system's total mass-energy is released as gravitational wave radiation over the final inspiral and merger phases.

The framework's working picture of mergers (recorded separately in the mass-vacuum interaction picture document) is that mergers release energy because the configuration burden of supporting two separated wells exceeds the burden of supporting one combined well. The released energy is the burden difference, partitioned among kinetic energy of the merging masses, gravitational wave radiation, and the residual configuration energy of the merged well.

The consistency check is simply this: when the framework's configuration-energy functional is specified, it must produce a burden difference for binary mergers that matches the observed energy release.

This is not optional. The framework claims to recover gravitational physics in regimes where general relativity has been tested. Binary mergers are now among those regimes, with measured energy releases. Any configuration-energy functional that gives substantially different merger energies than observation would falsify that piece of the framework.

## Why This Check Matters

The framework's current development stage has produced a complete weak-field recovery (T1 through T9). That recovery is conditional on P7 and P8, which were selected to conform to general relativity's weak-field structure. The recovery establishes that the framework's ontology can support known weak-field physics, but it does not yet distinguish the framework from a substantivalist reformulation of general relativity that would make all the same predictions.

The merger energy scale check is one of the first places where the framework moves from "compatible with GR" to "predicting specific numbers that can be compared to observation." The configuration-energy functional, once specified, will give some specific value for the burden difference between separated and merged configurations. That value either matches observation (in which case the framework retains empirical viability) or it does not (in which case the functional must be revised).

Three outcomes are possible.

The functional matches general relativity's predictions for merger energies. In this case the framework's content is GR's content, expressed in different ontological language. This is philosophically interesting but does not give the framework distinct empirical content.

The functional gives different predictions but the differences are within current observational uncertainty. In this case the framework remains empirically viable while having distinct content, and future precision measurements could distinguish it from GR.

The functional gives different predictions outside observational uncertainty. In this case the framework is falsified at current observational precision and must be revised.

The check is therefore informative regardless of which outcome occurs. It tells the framework's developers where they actually stand relative to observation.

## Why the Check Cannot Be Performed Now

The check requires the configuration-energy functional. The framework currently does not specify the functional.

P4 commits the framework to configuration energy existing and depending on directional structure. It does not commit to a specific functional form. Different functionals would give different specific predictions for merger energies. Until the functional is chosen, the check cannot return a number.

Several functional forms are conceivable.

A functional proportional to the integral of curvature scalar over a region would be roughly analogous to general relativity's Einstein-Hilbert action. If the framework adopted such a functional, the merger energies would likely match GR's by construction, and the framework would be GR with substantivalist commentary.

A functional proportional to the integral of curvature squared over a region would give different merger energies than GR. Whether they would match observation is open.

A functional with substance-flow terms or interface terms (corresponding to the burden picture's interface energy and substance-exchange contributions) would give different predictions again, and the differences could be large or small depending on the term structure.

The framework has not committed to any of these. The work of choosing among them, or of constructing some other form, is the framework's current frontier as physics.

## What the Check Constrains

Even without performing the check, several constraints on the future functional can be stated now.

The functional must give subadditive burden for clumping. If the burden of two separated wells were less than or equal to the burden of one combined well, mergers would not release energy, and the framework would predict no gravitational wave radiation from binary inspirals. This contradicts observation. So the functional must satisfy a subadditivity condition: the burden of a combined configuration must be less than the sum of burdens of separated configurations of equivalent total mass.

The functional must be local. Configuration energy under P4 is locally located, depending on local curvature structure. A functional that required integrating over distant regions to determine local configuration energy would be inconsistent with the framework's commitment to local energy.

The functional must be Lorentz-invariant. By the framework's import of SR1, physical laws are the same in all inertial frames. The configuration-energy functional, as a physical law, must respect this.

The functional must produce smooth dynamics. By the framework's smoothness requirement (implicit in P4), configurations cannot have discontinuous curvature with finite energy. The functional must be such that smooth configurations have finite configuration energy and discontinuous configurations have infinite or undefined energy, ensuring that the dynamics never produces discontinuous configurations.

The functional must reproduce the static exterior recovery. P7 and T3 give γ=1 in the static spherical exterior; P8 and T4 give β=1 in the same regime. The functional, when specialized to the static spherical exterior, must produce these results. Otherwise the framework's weak-field recovery would not survive the introduction of the functional.

These constraints do not uniquely determine the functional. They narrow the search space but leave substantial freedom.

## A Specific Sub-Check: Two-Body Energy Release Scaling

Within the broader merger energy check, a specific sub-check is worth identifying.

For binary mergers, the energy released as gravitational wave radiation depends on the masses of the merging bodies. General relativity gives a specific scaling law: the radiated energy depends on the mass ratio and the total mass in particular ways, with the dominant dependence being on the chirp mass. This scaling has been confirmed across the LIGO observation catalog.

The framework's burden functional, whatever its specific form, must reproduce this scaling. The burden difference between two separated wells of masses M₁ and M₂ and one combined well of mass M₁+M₂ must scale with M₁ and M₂ in a way consistent with the observed chirp-mass dependence.

This is a more constrained check than the overall energy-scale check. It tests not just the magnitude of the burden difference but its functional dependence on the masses. A functional that gave the right total energy for one specific merger but the wrong scaling across mergers would fail this sub-check.

The sub-check is also more discriminating among possible functional forms. Different functionals would give different mass-scaling laws, and most of them would fail to match the observed chirp-mass scaling. The functional space consistent with the observed scaling is therefore much smaller than the space consistent with the order-of-magnitude check alone.

## Beyond Binary Black Hole Mergers

Binary black hole mergers are the cleanest test case because the components are well-modeled (Kerr black holes in GR), the inspiral is purely gravitational, and the radiated energy is dominated by gravitational waves rather than by other channels.

Binary neutron star mergers add complications. Some of the released energy goes into electromagnetic radiation, into ejecta, into heat, and into other channels beyond gravitational waves. The total released energy is harder to determine, and the partition among channels involves matter physics the framework has not yet developed.

For the framework's merger energy check, binary black hole mergers are therefore the appropriate test. The framework can check that its burden functional gives the right total energy release and the right mass scaling for these mergers, without yet needing to handle the additional complications of matter content.

If the framework eventually develops matter-side content (substance-regime dynamics for masses that are not black holes), the check can be extended to neutron star mergers. This is downstream work that depends on developments not currently in the framework.

## What the Check Does Not Establish

The merger energy check is necessary but not sufficient for the framework's empirical viability.

A functional that passes this check could still fail other checks. The framework's predictions for cosmology, for stellar dynamics, for gravitational wave waveforms (not just total energy), and for many other phenomena would each need to be checked against observation. The merger energy check is one test among many.

Conversely, a functional that fails this check is not necessarily wrong as a candidate for the framework. The failure could indicate that the burden picture itself needs revision (perhaps mergers do not release exactly the burden difference, but some related quantity), or that the framework's substance-regime dynamics need additional structure beyond what the picture currently includes.

The check is a necessary milestone for the framework to be taken seriously as physics. It is not the final word on whether the framework is correct.

## Status

The merger energy scale check is currently a development target. It cannot be performed at the framework's current development stage because the configuration-energy functional has not been specified.

When the functional is specified, the check should be performed early in the evaluation of that functional. If the check is passed, further checks (cosmological consistency, gravitational wave waveform structure, strong-field corrections to weak-field tests) can proceed. If the check is failed, the functional must be revised before further development.

The check is independent of whether the framework's distinct content turns out to be empirically distinguishable from general relativity. It is a consistency check that any candidate functional must pass, regardless of what other content the framework eventually claims.

This document records the check as an open development target so that future work on the configuration-energy functional is guided by clear quantitative targets. The framework's empirical viability beyond the weak-field regime depends on passing checks of this kind.

## Summary

The framework's working picture identifies binary merger energy as the difference between separated-well configuration burden and merged-well configuration burden. Observed merger energies (a few percent of total mass-energy radiated as gravitational waves for typical binary black hole mergers) place a quantitative target on the framework's future configuration-energy functional.

The check cannot be performed until the functional is specified. When it is specified, the check requires the burden difference for representative mergers to match observed energy releases, and the mass-dependence of the burden difference to match the observed chirp-mass scaling.

Constraints on the functional already include subadditivity under clumping, locality, Lorentz invariance, smoothness, and recovery of γ=1 and β=1 in the static spherical exterior weak-field limit. The merger energy check adds the requirement that the functional give the right energy scale and scaling for binary mergers.

The check is necessary but not sufficient for the framework's empirical viability. It is the first quantitative test that distinguishes a framework that has chosen a specific functional from a framework that has only chosen an ontology. Until the framework can pass this check, its content beyond the weak-field exterior remains unverified.
