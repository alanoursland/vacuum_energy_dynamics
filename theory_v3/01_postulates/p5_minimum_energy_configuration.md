# P5: Vacuum Seeks Minimum Energy Configuration

## What This Postulate Says

The vacuum's configuration evolves toward the lowest configuration energy consistent with whatever constraints are present. Configurations of higher energy are unstable; they relax toward lower-energy configurations. When constraints are absent, the vacuum settles into its unconstrained minimum-energy configuration. When constraints are present, the vacuum settles into the minimum-energy configuration consistent with those constraints.

This is the framework's dynamical principle. P4 commits to configurations carrying energy. P5 commits to the vacuum finding the minimum of that energy under whatever conditions obtain.

---

## Flat Space as the Ground State

In the absence of mass or other constraints, the vacuum's configuration is what we call flat. Flat is not just one configuration among many — it is the configuration the vacuum settles into when nothing is forcing it to do otherwise.

This gives flat vacuum a specific physical meaning in the framework. Flat is the ground state. Far from any mass, away from any gravitational source, the vacuum is in flat configuration because that is what minimizes its configuration energy when no constraints are imposed. The framework's notion of flat is therefore not arbitrary; it picks out the unique configuration that the dynamics drive toward in the absence of disturbance.

This is consistent with SR9's commitment that local physics in inertial frames reduces to SR's Minkowski structure. The Minkowski structure is what the vacuum settles into when nothing is constraining it; it is the framework's ground state, and it is what SR describes.

---

## The Ground State May Have Nonzero Configuration Energy

A subtlety worth addressing: the ground state being a minimum does not mean its configuration energy is zero.

A useful metaphor for thinking about this comes from the graph model we discussed earlier in the framework's development. Imagine vacuum modeled as a graph of points connected by edges, with edge lengths governed by spring-like potentials that prefer all edges to have a particular target length. The minimum-energy configuration is the one that comes closest to having all edges at the target length.

In two dimensions, this minimum is achievable: regular triangular tilings have all edges at equal length, with zero residual energy in the springs. But in three or four dimensions, no regular tiling exists where every edge has the same length and every cell has the same shape. The geometry of higher-dimensional space prevents perfect equalization. The minimum-energy configuration in 3D or 4D is therefore not zero — it is whatever the springs settle into given the unavoidable frustration imposed by dimensionality.

We use this only as a metaphor. The framework is not committed to a discrete graph structure; the metaphor is meant to make plausible a structural feature that the continuous version of the framework may share. The structural feature is: the vacuum's minimum-energy configuration may carry positive configuration energy density even in flat space, because the dimensionality of spacetime may prevent the configuration from reaching zero energy. Whether this is actually the case for the framework depends on the specific configuration energy functional, which the framework has not yet specified. We flag the possibility because it is consistent with the framework's commitments and would have specific consequences if true.

What this would mean concretely: the configuration energy of flat vacuum is some baseline value, and configurations with curvature have configuration energies above this baseline. The framework's "departure from flat costs energy" content is a statement about deviations from the baseline, not from zero. Flat has nonzero energy; curved has more.

This is a possibility, not a commitment of P5. P5 commits to flat being the ground state — the minimum-energy configuration in the absence of constraints — without committing to whether the ground-state energy is zero or positive.

---

## Mass Imposes Constraints

The framework's account of how mass affects vacuum is that mass imposes constraints on the vacuum's configuration. Mass holds the vacuum's configuration away from the unconstrained ground state in some local region, preventing the vacuum from relaxing fully to flat.

The mass-as-constraint reading is what lets the framework treat mass without committing to a specific mass ontology. We don't say what mass *is* at this stage; we say what mass *does* to the vacuum: it imposes constraints on the configuration in its vicinity. The constraints determine, given the vacuum's configuration energy structure, what configuration the vacuum takes around the mass.

The mass's specific constraint structure is not committed to at the level of P5. Different physical situations involve different constraints — a stationary mass imposes one kind of constraint, a moving mass another, a rotating mass yet another. The framework's specific predictions about gravitational phenomena depend on what constraints specific physical situations impose, which is downstream content that later work develops.

---

## Gravity Wells as Constrained Minimum Energy

Given P5 and the mass-as-constraint reading, gravity wells emerge as a specific kind of minimum-energy configuration.

A region with mass present has a constraint at the mass's location. The vacuum surrounding the mass cannot settle into flat configuration globally, because the constraint forces it to deviate from flat in the mass's vicinity. What the vacuum can do is settle into the minimum-energy configuration *consistent with the constraint*. This minimum is what we call a gravity well.

The well's specific shape is whatever configuration minimizes total configuration energy given the constraint at the mass's location. Far from the mass, where the constraint's influence is weak, the configuration is close to flat — close to the unconstrained ground state. Near the mass, the configuration is more curved, with the curvature pattern set by what minimum-energy demands. The transition between these — the well's profile — is whatever the configuration energy functional and the constraint together produce.

A consequence worth stating explicitly: gravity wells do not fill in on their own, even though flat space has lower configuration energy than curved space. This is because "minimum-energy configuration" is always minimum *given the constraints*. Flat space is the minimum-energy configuration for a region without mass. A gravity well is the minimum-energy configuration for a region with mass. As long as the constraint persists — as long as the mass remains in place imposing its constraint on the surrounding vacuum — the well persists as the constrained minimum. If the constraint lifts, the vacuum can relax toward flat. But in the absence of such a process, the well is stable.

This gives the framework a specific account of why gravity wells exist and what determines their shape. They exist because mass imposes constraints that prevent unconstrained relaxation. Their shape is the minimum-energy response to those constraints. Without P5's variational principle, mass-as-constraint would not produce well-defined geometric structures around mass; with P5, it produces specific configurations that the framework can in principle compute given the configuration energy functional.

The framework's later derivations will try to reproduce known gravitational phenomena (light deflection, time dilation, perihelion precession, and so on) by computing what minimum-energy configurations look like under various constraint structures. Whether the framework reproduces these phenomena correctly depends on the configuration energy functional, which is open work.

---

## Propagation Cannot Be Instantaneous

P5 commits to disturbances from minimum being unstable — they relax toward minimum. But relaxation cannot happen instantaneously across space. When the minimum-energy configuration changes at some location, the rest of space cannot adjust simultaneously; the change must propagate from where it originated outward.

This is not an additional claim beyond the minimum-energy principle; it is a consequence of it combined with general physical reasonableness. If the minimum-energy configuration changes at some location, the rest of space can only learn of the change and respond to it through some process that propagates. No process is instantaneous. Whatever the propagation speed turns out to be, it is finite.

The framework does not commit at the postulate level to a specific propagation speed. SR2 commits to $c$ being the speed of light, and the broader framework commits (under P1 and P2) to information propagation through the vacuum being limited by $c$. Whether the configuration's relaxation propagates exactly at $c$ or at some other speed determined by the configuration energy functional is a question the framework's specific dynamics will need to answer. What P5 commits to is that the speed is finite, not that it has any particular value.

---

## Slow versus Rapid Constraint Changes

The propagation content has a structural consequence worth flagging at the postulate level.

If a constraint changes slowly enough, propagation reaches each location before the next change arrives. The configuration at each location has time to settle into the current minimum before anything new happens. The vacuum remains approximately at minimum throughout, with only smooth quasi-static transitions between minima.

If a constraint changes rapidly, propagation cannot keep pace. A region near the change finds itself away from minimum because the change is already happening there while earlier adjustments are still in transit elsewhere. The region's configuration departs from the local minimum, and that departure is itself a non-minimum configuration that, by P5's own dynamics, must propagate outward.

This gives the framework a qualitative distinction between two kinds of dynamics. Slow changes produce smooth tracking, with the vacuum staying near minimum throughout. Rapid changes produce departures from minimum that propagate outward as waves through the surrounding vacuum.

P5 commits to this qualitative distinction without committing to its specific quantitative content. What counts as "slow" or "rapid" depends on the framework's specific propagation speed and on the configuration energy functional. Specific predictions about which physical situations produce wave radiation, with what intensity and what wave structure, are downstream content depending on these specifics.

---

## Excess Energy Has to Go Somewhere

When constraints change such that the new minimum-energy configuration has lower configuration energy than the current configuration, the vacuum is releasing energy as it relaxes. Energy conservation requires this released energy to go somewhere.

The framework allows several places for this energy to go.

**Reabsorbed locally as the configuration relaxes.** When a region transitions from a higher-energy configuration toward a lower-energy one, some of the released energy can stay locally — converting back to vacuum substance, or settling into the local configuration without propagating. In the slow-change limit, where propagation keeps up with constraint changes, most or all of the released energy stays local in this way.

**Propagated outward as waves.** When the change is rapid enough that propagation cannot keep up, the resulting non-minimum configuration propagates outward through the surrounding vacuum, carrying configuration energy away from the original location. These propagating disturbances are the framework's wave content.

**Substance changes.** The released energy can drive changes in vacuum substance amount. P3's strict density-constancy means substance amount changes have to be real creation or destruction, which involves specific physical processes that the framework's later content develops.

**Other mechanisms.** The framework does not commit to having identified all the channels through which excess configuration energy can be released. Other mechanisms may exist that the framework hasn't yet developed.

What P5 commits to is that excess configuration energy is real and must be accounted for. When configurations change in ways that release energy, that energy goes into specific physical channels rather than disappearing. The split between local reabsorption, wave radiation, and substance changes depends on the specific dynamics, which is downstream content. P5 is committed to the channels existing and to total energy being conserved across them; the specific accounting for any given physical situation is for later work.

---

## What the Postulate Buys

P5 lets the framework do several things that would otherwise be unavailable.

**Configurations have predictable structure.** Without P5, the framework would describe configurations as carrying energy (P4) but would have no commitment about which configurations actually obtain physically. With P5, the configurations that obtain are specifically those that minimize energy subject to the present constraints. This makes configurations predictable in principle, given the configuration energy functional and the constraints.

**Mass affects vacuum through a specific mechanism.** P5 plus the mass-as-constraint reading gives the framework a specific account of how mass affects the surrounding vacuum: through constraints that determine the minimum-energy configuration the vacuum settles into.

**Dynamics has a variational structure.** P5 commits the framework to dynamics being driven by minimization of configuration energy under constraints. This is the same variational structure that underlies standard physics derivations from action principles, expressed in framework-native vocabulary. The framework's specific dynamics depends on the configuration energy functional, but the variational structure is committed to at the postulate level.

**Wave propagation is licensed.** P5's relaxation dynamics combined with the propagation-cannot-be-instantaneous content commits the framework to wave-like dynamics being a consequence of rapid constraint changes. Specific wave properties depend on the functional, but the existence of wave-like dynamics is licensed by P5.

**Stability of constrained configurations.** Gravity wells and other constrained configurations are stable as long as their constraints persist. The framework's static gravitational structures are not arbitrary; they are constrained minima that remain in place because their constraints remain in place.

---

## What the Postulate Does Not Do

P5 commits to the variational principle, to flat being the ground state, and to wave dynamics being licensed by rapid constraint changes. It does not commit to specifics that would require more development.

**The configuration energy functional is not specified.** P5 says the vacuum minimizes configuration energy. It does not say what the energy functional is. Different functional forms give different specific predictions, and the framework's quantitative content depends on this functional.

**The propagation speed is not specified.** P5 commits to propagation being finite, but does not pin down a specific speed. Whether the framework's propagation occurs exactly at $c$ depends on the functional and on the framework's specific dynamics.

**Specific wave properties are not specified.** P5 commits to disturbances propagating, but does not commit to wave polarization or specific generation mechanisms. The framework's wave content depends on the functional and on what kinds of source dynamics produce what kinds of waves, both of which are downstream content.

**The relationship between specific motions and radiation is not specified.** Whether specific kinds of source motion produce specific kinds of radiation, and the relationships between source dynamics and wave content, depend on the functional and on the specific dynamics, which the framework has not pinned down.

**The constraint structure imposed by mass is not specified.** P5 says constraints determine the minimum-energy configuration, but does not say what specific constraints mass imposes. Different mass states (stationary, moving, rotating, deformed) impose different constraints, and the specific constraint structures are downstream content.

**The split between local reabsorption and wave radiation is not specified.** P5 commits to released energy going into specific channels but does not commit to how much goes where in any specific physical situation. The split depends on the dynamics.

**Quantitative content is not provided.** P5 commits to qualitative features of the dynamics — minimization, relaxation, slow-vs-rapid distinction, wave propagation — without quantitative commitments. Quantitative predictions require pinning down the functional and the constraint structure.

---

## Imports

This postulate invokes:

- SR9: Local Validity of SR in Inertial Frames (the unconstrained ground state reduces to the local Minkowski structure that SR describes)

It depends on:

- P1: Vacuum-Energy Equivalence (the energy being minimized is real energy of vacuum-as-energy)
- P2: Vacuum-Spacetime Identity (the configuration is the configuration of spacetime itself)
- P3: Vacuum Energy Density (the substance content of the vacuum is determined by the constant density)
- P3a: Spatial Differential is Curvature (the configurations being varied over have curvature in the framework's sense)
- P4: Curvature Contains Energy (configurations carry the energy that is being minimized)
