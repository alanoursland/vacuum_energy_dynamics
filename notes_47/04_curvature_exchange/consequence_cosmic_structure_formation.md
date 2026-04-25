# Consequence: Cosmic Structure Formation

---

## What This Document Is

This is a consequence document. It works out what the framework's existing commitments imply about the formation and persistence of large-scale cosmic structure — voids, filaments, walls, the cosmic web. The result is qualitative: voids act as vacuum accumulation regions, mass-rich regions act as vacuum expulsion regions, and the cosmic web emerges as the equilibrium pattern of vacuum redistribution under cosmic expansion.

The document builds directly on `consequence_cosmic_expansion.md`, which establishes that cosmic expansion creates vacuum-energy under the framework's ontology. The present document picks up that commitment and asks: given that expansion is creating vacuum everywhere uniformly, where does the created vacuum actually go in a universe with non-uniform mass distribution?

The argument runs through Postulate 5's minimum-energy configuration principle. The mass-as-constraint reading from Postulate 5's gravity-well section is what makes the redistribution happen: mass-rich regions can't absorb the new vacuum because their configuration is pinned by the mass constraint, so the new vacuum migrates to regions that can absorb it.

This is a consequence document in the same sense as the cosmic expansion consequence — a readout of what existing postulates force, not a new postulate or a new derivation in the proof sense.

---

## Status and Risk

This document is more speculative than the framework's weak-field proofs. It is a high-level consequence that combines existing postulates with one parsimonious assumption (described in the next section), and arrives at qualitative claims about cosmological flow without quantitative machinery. It is not yet on the same footing as the redshift, light deflection, or Shapiro proofs.

The document's claims should be read as follows. The framework, given its existing commitments and the parsimonious assumption that expansion-created vacuum appears uniformly everywhere including inside mass-pinned wells, points toward a specific picture of cosmic structure formation: mass-rich regions expel surplus vacuum into surrounding regions, and voids accumulate the redistributed vacuum on top of locally created vacuum. The qualitative geometry of the cosmic web — voids surrounded by mass-rich filaments — emerges as the equilibrium pattern of this redistribution.

What this document does not establish: quantitative rates, formal continuity equations for vacuum flow, specific predictions about void size distributions or matter clustering, or rigorous derivation of how the redistribution mechanism interacts with standard cosmological dynamics. Each of these would require quantitative machinery the framework has not yet developed.

What this document does establish: that the framework's existing commitments, plus one parsimonious assumption about local vacuum creation, point toward a cosmological flow picture that is qualitatively distinct from standard cosmology's purely-gravitational structure-formation account. Whether the predicted flow has empirical signatures distinct from those of dark-matter-driven structure formation, and whether the framework's mechanism modifies, extends, or coexists with the standard picture, are questions for future quantitative work.

---

## What This Document Builds On

Two prior commitments are essential, plus one parsimonious assumption.

**Cosmic expansion creates vacuum-energy.** From `consequence_cosmic_expansion.md`: the universe is observed to expand, space under Postulate 1 is identical to vacuum, and vacuum is energy. So cosmic expansion creates vacuum, and creating vacuum creates energy. The mechanism is uniform across the universe — every region is creating new vacuum at the same rate per unit volume, since the vacuum's energy density is locally constant (Postulate 2).

**Mass pins the local vacuum configuration into a gravity well.** From `postulate_minimum_energy_configuration.md`: mass acts as a constraint on the surrounding vacuum, and the vacuum settles into the minimum-energy configuration consistent with that constraint. The well shape is the answer to this optimization problem. Critically, the well does not fill in on its own — it persists as long as the mass persists, because the constraint that produces it persists.

**The parsimonious assumption: expansion creates vacuum locally everywhere, including inside mass-pinned wells.** The cosmic expansion consequence treats expansion as creating vacuum uniformly at constant density. The framework has not stated anywhere that bound systems are exempt from this. The parsimonious reading is that the mechanism operates everywhere — the vacuum-creation rate per unit existing vacuum is the same inside a galaxy, inside a cluster, and in the deepest void.

Postulate 2 is what makes this the parsimonious reading rather than just one option among many. If vacuum density varied between locations, one could imagine wells having lower-density vacuum that expansion treats differently, or some other escape from uniform creation. Postulate 2 closes that escape: every observer measures the same finite vacuum energy density at every location. The vacuum is the same kind of thing everywhere, so expansion acts on it the same way everywhere.

A subtlety worth surfacing. Locally constant density means the density is the same per unit volume of vacuum, but a coordinate span in a gravity well contains less vacuum than the same coordinate span in flat space — that's what curvature is in the framework (per `consequence_curvature_as_spatial_differential.md`). So the rate of new vacuum creation per coordinate span is reduced in wells, even though the rate per unit of existing vacuum is the same as in flat space. Wells create less new vacuum locally than voids do, simply because there is less vacuum present in a well to begin with.

This subtlety reinforces rather than complicates the redistribution picture. Voids contain more vacuum per coordinate span and are unconstrained, so they create more new vacuum and absorb all of it. Wells contain less vacuum per coordinate span and are constrained by mass, so they create less new vacuum and expel essentially all of it. The flow direction — from wells to voids — is what both sides of this asymmetry favor.

This is a framework-specific commitment, not something inherited from standard cosmology. In standard cosmology, gravitationally bound systems decouple from Hubble expansion at scales where local gravitational binding dominates over the expansion rate. Galaxies do not expand with the Hubble flow; clusters mostly do not; superclusters partially do. The framework's parsimonious assumption is different: expansion-as-vacuum-creation operates uniformly per unit existing vacuum, and what bound systems do is *expel* the created vacuum rather than *opt out* of having vacuum created within them.

Carving out exemptions for bound systems would require additional commitments the framework does not have. The minimal commitment — expansion creates vacuum at the same per-unit-existing-vacuum rate everywhere, scaled by Postulate 2's constant density — is what we adopt. The redistribution mechanism described in this document is what becomes necessary if this minimal commitment is correct.

The present document is what happens when these commitments meet: expansion is everywhere creating new vacuum, including inside mass-pinned wells, and the wells must do something with it.

---

## The Setup

Consider a region containing mass — a galaxy, a cluster, anything with a settled gravitational well around it. The well is at minimum-energy configuration given the mass constraint. The vacuum-per-coordinate-span at each location in the well takes the specific value that minimizes total configuration energy given the constraint.

Cosmic expansion is happening throughout this region, as everywhere. New vacuum is being created continuously, including inside the well.

The framework's situation is that the well's local vacuum content was at the value the constraint specifies, and now there is more vacuum present than that. The configuration is no longer at minimum given the constraint; it has been displaced.

By Postulate 5, configurations away from minimum are not stable. The system relaxes toward minimum. The question is: how does it relax?

---

## Two Possible Relaxation Paths

In principle, there are two ways for the configuration to return to minimum.

**Path A: The well shape adjusts.** The well becomes less curved overall, accommodating the new vacuum within its structure. The mass-pinned configuration shifts to a new minimum that includes more vacuum than before.

**Path B: The new vacuum migrates outward.** The well shape is preserved, and the surplus vacuum flows outward to regions where it can be absorbed. The well rejects the new vacuum; voids and unconstrained regions receive it.

Path A is disfavored, or at least constrained, by the mass constraint itself. The well shape is determined by the mass — that's what "mass acts as a constraint" means in Postulate 5's gravity-well discussion. If the well filled in, becoming less curved, it would no longer satisfy the constraint that the mass imposes. The amount of vacuum-extent reduction the mass requires would no longer be present at the depth the constraint specifies. The mass is conserved (its rest mass-energy persists), so the constraint persists, so the well shape persists in its broad structure.

How tightly Path A is constrained depends on the precise nature of the mass constraint, which the framework has not yet pinned down quantitatively. Whether the constraint fixes total vacuum-extent reduction in the well, the radial profile, the local vacuum content at specific points, or some combination, affects how much "filling in" the well can absorb before it fails to satisfy the constraint. What the framework's existing commitments do establish is that arbitrary filling in is not allowed — the mass requires a well, so a well must persist, so most of the new vacuum must go somewhere other than into the well's interior.

Path B is what the framework consequently expects. If Path A is constrained — if the well cannot freely absorb new vacuum — then the bulk of the surplus vacuum must go elsewhere. By Postulate 5's propagation principle, the surplus configuration moves outward across space. The vacuum migrates from the mass-rich region to whatever surrounding regions can accommodate it.

The exact balance between local adjustment (some vacuum absorbed by the well's slight relaxation) and outward migration (the rest expelled) remains quantitative open work. The qualitative claim is that significant migration occurs.

This is the framework's first cosmological flow result: mass-rich regions expel a significant fraction of the vacuum that expansion creates locally.

---

## The Flow Picture

The well around a mass is not a static accessory. Under the framework, it is the steady-state configuration of an ongoing dynamic process. Expansion is continuously adding vacuum to the well's region; the mass constraint is continuously rejecting that vacuum; the rejected vacuum is continuously flowing outward. What we observe as "the gravity well around a mass" is the equilibrium pattern of this flow: the shape that persists when the rate of vacuum creation in the region equals the rate of vacuum outflow at the well's boundary.

This reframes what a gravity well is in the framework. The static picture from Postulate 5 — well as minimum-energy configuration given a constraint — is correct as a leading-order description, but the full picture includes the flow component. The well is being continuously deformed by expansion and continuously expelling the deformation outward as vacuum.

In the static limit (no expansion), there would be no flow, and the well would simply be the constrained minimum. In the actual universe, expansion provides a continuous source term, and the well's persistence is maintained by an outward current of vacuum.

---

## Where the Migrated Vacuum Goes

The migrated vacuum has to land somewhere. In the framework, "somewhere" means regions of space that can absorb new vacuum without violating any local constraints.

Voids — regions far from significant mass — are the natural recipients. A void's local minimum-energy configuration is approximately flat, since there's no mass constraint forcing a curved configuration. When new vacuum arrives in a void, the void simply gets larger. Adding vacuum to a flat region produces more flat region, which is consistent with the void's unconstrained minimum.

The contrast with mass-rich regions is sharp. A void is at unconstrained minimum, so it can absorb arbitrary amounts of new vacuum by extending its flat region. A mass-rich region is at constrained minimum, so it cannot absorb new vacuum without violating the constraint. Vacuum flows from the latter to the former.

The flow has a direction: from mass-rich regions to voids. Voids become vacuum accumulation regions. Mass-rich regions become vacuum expulsion regions. Note that mass-rich regions are not ultimate sources of vacuum — expansion creates vacuum everywhere — but they are *redistribution sources* in the sense that they expel a significant fraction of their locally created vacuum into the surrounding regions.

---

## Connection to the Cosmic Web

Observational cosmology reveals that matter at the largest scales is distributed in a specific pattern: clusters and galaxies are concentrated along filaments and walls, surrounded by large underdense voids. This is the cosmic web, mapped extensively by surveys including the Sloan Digital Sky Survey [York et al., 2000] and predicted from the dynamics of cold dark matter cosmology [Bond, Kofman & Pogosyan, 1996].

The framework's mechanism gives a qualitative account that aligns with this observation. Voids grow rapidly because they are receiving migrated vacuum from surrounding mass-rich regions in addition to vacuum created by local expansion. Mass-rich regions stay relatively unchanged in their vacuum content because the new vacuum that expansion creates locally is being expelled. The geometry of the cosmic web — voids surrounded by filaments — corresponds to the geometry of the vacuum-flow pattern, with matter concentrated in the expulsion regions and absent from the accumulation regions.

This is qualitative agreement, not a quantitative derivation of the cosmic web's specific structure. A possible empirical signature: voids may grow faster, or differently, than local expansion plus standard gravitational evacuation alone would predict. Mass-rich regions may be stable against expansion in a way unconstrained regions are not. The contrast between void and filament may sharpen over time at a rate distinct from what dark-matter-driven structure formation predicts. Whether the framework's mechanism produces any of these signatures at empirically detectable amplitudes — and whether it produces the observed statistical properties of the cosmic web (void size distributions, filament thickness, the matter power spectrum) — is open quantitative work.

---

## Relationship to Standard Cosmology

Standard cosmology accounts for cosmic structure through gravitational instability acting on initial density perturbations from the early universe, with cold dark matter providing the gravitational potential wells into which ordinary matter falls. This account is well-developed and quantitatively successful: it reproduces the cosmic microwave background's structure, large-scale matter clustering, and the cosmic web's statistical properties.

The framework's vacuum-flow mechanism is a separate physical phenomenon, not a replacement for the standard story. Gravitational instability operates on matter, redistributing matter into denser regions. The framework's mechanism operates on vacuum, redistributing vacuum from mass-rich regions to voids. Both processes can occur simultaneously.

The interaction between the two is not currently worked out. Several possibilities are open. The vacuum-flow mechanism might supplement gravitational clustering, contributing to void growth in a way that adds to gravitational evacuation of voids. It might modify the effective gravitational dynamics, since vacuum redistribution changes the curvature distribution that matter responds to. It might in some regimes substitute for some of dark matter's role, since both produce gravitational effects favoring structure formation. Determining which of these is the case requires quantitative work the framework has not yet done.

What the framework does establish is that vacuum redistribution under expansion is a real consequence of its commitments — a physical process distinct in its mechanism from gravitational instability, even though both contribute to similar observable patterns. Whether this consequence has observable signatures empirically distinguishable from those of dark-matter-driven structure formation, and whether it modifies or extends the standard picture, are questions for future work.

---

## What This Consequence Does Not Establish

**Quantitative rates of vacuum migration.** The mechanism predicts that vacuum flows from mass-rich regions to voids, but does not predict how fast. The propagation speed is presumably constrained by Postulate 1's information-propagation considerations — disturbances in the vacuum should propagate at a speed bounded by $c$ — but a formal derivation would require resolving the open question of the vacuum's mathematical structure.

**Quantitative size scales.** The framework's mechanism may produce voids that grow faster than local expansion alone would account for, but does not predict the specific size distribution of voids. Matching the observed cosmic web's statistical structure would require deriving how the flow rate depends on mass density, distance from mass concentrations, and other parameters that the framework currently treats qualitatively.

**Connection to the matter power spectrum.** Standard cosmology relates the observed clustering of matter to specific predictions from inflation plus dark matter. Whether the framework reproduces these predictions, modifies them, or makes different predictions is open.

**Relationship to dark matter.** Standard cosmology requires dark matter for structure formation to operate within the observed timescale. The framework's vacuum-flow mechanism might reduce, eliminate, or coexist with this requirement. Working out which is genuine open work.

**Effects on dark energy interpretation.** The cosmic expansion consequence noted that constant vacuum density during expansion aligns qualitatively with dark energy's observed behavior. The vacuum-flow mechanism complicates this: vacuum is created at constant density everywhere but redistributed non-uniformly afterward. Whether this changes how the framework relates to dark energy is open.

**Galactic-scale dynamics.** The framework's mechanism operates at scales where vacuum redistribution between regions is significant. Whether it has implications for galactic rotation curves, dwarf galaxy dynamics, or other galactic-scale phenomena that dark matter is invoked to explain is unresolved.

---

## Natural Quantitative Target

If this consequence is to become quantitative, the natural mathematical object is a continuity equation for vacuum extent — something of the form:

$$\frac{\partial V_{\text{vac}}}{\partial t} + \nabla \cdot \mathbf{J}_{\text{vac}} = S_{\text{expansion}} - S_{\text{constraint}}$$

where $V_{\text{vac}}$ is the local vacuum extent, $\mathbf{J}_{\text{vac}}$ is the vacuum current, $S_{\text{expansion}}$ is the source term from cosmic expansion, and $S_{\text{constraint}}$ is the rejection term from mass-pinned configurations. Expansion provides the source. Mass constraints produce rejection. Voids are regions where the divergence of the vacuum current allows accumulation.

This equation is sketched here as a direction, not adopted as a commitment. Writing it down rigorously would require pinning down what $V_{\text{vac}}$, $\mathbf{J}_{\text{vac}}$, and the source/rejection terms mean within the framework's machinery — which connects back to the open questions about the vacuum's mathematical structure. Until these are resolved, the equation is a target rather than a tool.

---

## What This Consequence Does Establish

The framework, given its existing commitments, predicts a specific kind of cosmological flow: vacuum is created uniformly by expansion but redistributed non-uniformly by the mass distribution, with mass-rich regions acting as expulsion regions and voids acting as accumulation regions. The cosmic web's qualitative structure — voids surrounded by mass-rich filaments — emerges as the equilibrium pattern of this flow.

The mechanism follows from existing postulates plus the parsimonious assumption about local vacuum creation, without requiring new commitments. Postulate 1 makes vacuum identical to spacetime, so vacuum creation by expansion is a real physical process rather than a coordinate artifact. The cosmic expansion consequence works out that this creation is happening uniformly. Postulate 5's minimum-energy principle, applied to mass-pinned configurations, establishes that mass-rich regions cannot freely absorb the created vacuum and the bulk must be expelled. The flow direction follows from where unconstrained absorption is available — voids.

Standard cosmology has no direct analogue of vacuum-substance redistribution, since vacuum in standard cosmology is not a physical substance that can flow between regions. Standard cosmology does, however, model void growth and cosmic-web formation through gravitational instability, dark matter dynamics, and expansion. The contrast is not "framework predicts void growth, standard cosmology doesn't" but rather "framework predicts void growth through vacuum redistribution, standard cosmology predicts void growth through gravitational evacuation, and the two mechanisms might coexist or one might be quantitatively dominant in regimes the framework cannot yet identify."

This places cosmic structure formation alongside the other phenomena the framework gives a distinctive account of: gravitational redshift (vacuum exchange during photon traversal), gravitational time dilation (vacuum-extent variation between locations), gravitational waves (propagating configuration changes). In each case, the framework reaches a known phenomenon through machinery distinct from the standard account, and offers a physical interpretation that the standard account does not supply.

---

## References

Bond, J. R., Kofman, L., & Pogosyan, D. (1996). How filaments of galaxies are woven into the cosmic web. *Nature*, 380(6575), 603–606.

York, D. G., et al. (2000). The Sloan Digital Sky Survey: Technical summary. *The Astronomical Journal*, 120(3), 1579–1587.