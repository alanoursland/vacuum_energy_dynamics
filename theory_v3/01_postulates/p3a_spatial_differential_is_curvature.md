# P3a: Spatial Differential is Curvature

## What This Postulate Says

Curvature, in this framework, is the spatial differential of vacuum amount across neighboring regions. A region where the amount of vacuum per unit of geometric extent varies from neighbor to neighbor is curved; a region where it is uniform is flat.

The postulate distinguishes two properties of vacuum that P3 leaves implicit:

**Vacuum energy density** is energy per unit of vacuum, measured locally. P3 commits to this being constant: every observer at every location measures the same value. Density is an intensive property — it does not depend on how much vacuum is present, only on what each unit of vacuum is.

**Vacuum energy volume** is the total energy of vacuum present in a given region. This is an extensive property — it does depend on how much vacuum is present. Two regions with the same density can have different energy volumes if they contain different amounts of vacuum.

Under P3's constant density, geometric variation between regions cannot be variation in density. It must be variation in the amount of vacuum present — variation in the energy volume per unit of geometric extent. The spatial differential of this amount, across neighboring regions, is what the framework means by curvature.

---

## The Question This Answers

P1 commits to vacuum being energy. P2 commits to vacuum being spacetime. P3 commits to vacuum density being constant. None of these directly say what curvature is, even though the framework's larger project will need curvature as a working concept.

Standard physics arrives at curvature through a specific chain: a manifold is equipped with a metric, the metric determines a connection, the connection's failure to commute under parallel transport defines the Riemann curvature tensor. Curvature in standard physics is the end of this chain — derived from more basic mathematical structure.

Our framework cannot follow that chain without committing to mathematical machinery (specific manifold structure, metric tensor, connection) that the postulates have not introduced. We need a definition of curvature that lives at the level our postulates operate on, in the framework's own vocabulary.

P3a provides that definition. It states what curvature is in framework-native terms, building only on what P1, P2, and P3 have already committed to.

---

## Why This Has to Be a Postulate

In the previous iteration of this framework, curvature-as-spatial-volume-differential was a *consequence* of the postulates, derived through a process of elimination: density variation is forbidden by P3, separate-structure variation is forbidden by P2, so the only remaining option is amount variation.

That argument is sound as far as it goes, but it leaves the framework in an awkward position. The "consequence" is load-bearing for everything that follows — every later postulate that involves curvature depends on this definition, and the elimination argument doesn't actually pin down the definition tightly enough to support that load.

Specifically, the elimination argument tells us *what curvature isn't*. It doesn't tell us positively what curvature *is* in terms specific enough for later content to build on. The framework needs curvature to have a definite meaning before later postulates can refer to it.

Promoting the curvature definition to a postulate (or a postulate-like commitment, hence the "P3a" labeling) acknowledges this. The definition is foundational structure, not a derived consequence. The framework's later content — energy of curved configurations, dynamics of relaxation, exchange of vacuum with kinetic energy — all depend on having a working notion of curvature in place. P3a installs that notion.

---

## Energy Density and Energy Volume

The distinction between energy density and energy volume is structurally important and worth making explicit.

Standard physical vocabulary uses "density" in a way that presupposes a container. Mass density is mass per unit volume, where "volume" is part of a pre-existing space the mass is distributed within. Charge density, energy density, particle density — all share this presupposition. The container is one thing; the stuff in it has a density measured against the container.

Under P2, the framework rejects this picture. Vacuum is spacetime; there is no separate container. So "energy density" of vacuum cannot mean "energy of vacuum-stuff per unit of separate-container-volume." The container and the stuff are the same thing.

What "energy density" *can* mean, in framework terms, is energy per unit of the vacuum's own extent. A small piece of vacuum — measured by the geometric extent it occupies as part of itself — carries some amount of energy. That ratio (energy to self-measured extent) is what P3 commits to being constant. Every piece of vacuum, measured in its own terms, has the same energy per unit of itself.

"Energy volume," by contrast, is an extensive property. It is how much energy is present in a region, full stop. Two regions can have the same density (same energy per unit of self-measured extent) but contain different total amounts of energy, because they contain different total amounts of vacuum.

The picture that does *not* work is of vacuum-stuff distributed throughout some separate space, with density measured against that separate space's volume. Under P2, there is no separate space. The picture that *does* work is of a substance whose internal extent and energy are properties of the substance itself. Density is intrinsic; volume is extensive; the two are independent.

This is the same kind of distinction that runs through any extensive-vs-intensive analysis. Temperature is intensive; heat is extensive. Pressure is intensive; force is extensive. Density is intensive; mass is extensive. The novelty here is that the "container" against which we ordinarily measure extensive properties has been identified with the substance itself, so the standard vocabulary undergoes some strain. The distinction between density and volume survives the strain; what doesn't survive is the picture of the container.

---

## Curvature Defined

With the density/volume distinction in place, curvature can be stated cleanly.

**Curvature is the spatial differential of vacuum energy volume across neighboring regions of equal geometric extent.**

A region where every neighbor contains the same amount of vacuum (within its geometric extent) has zero curvature. A region where neighbors contain different amounts of vacuum has nonzero curvature, with the amount and direction of curvature determined by the pattern of differences.

By P3, density is the same everywhere. So differences in vacuum amount are not differences in how much energy each piece of vacuum carries; they are differences in how much vacuum is present per region of geometric extent. The framework's curvature is entirely about extensive variation, with intensive properties held constant.

Several features of this definition are worth flagging.

**Curvature is local.** It is a property of how a region relates to its immediate neighbors, not a global property of spacetime as a whole. A region's curvature can be determined by examining the region and its neighbors, without reference to anything more distant.

**Curvature is relational.** A single region in isolation has no curvature; curvature is what the differential of vacuum amount, region-to-region, picks out. Curvature exists in the relationship between neighboring regions, not within any single region considered alone.

**Curvature is bidirectional.** A region with less vacuum than its neighbors is curved one way; a region with more vacuum than its neighbors is curved the other way. Both are forms of curvature, distinguished by sign or direction.

**Curvature has spatial structure.** The differential of vacuum amount can vary directionally — one neighbor having more, another having less. This directional variation is part of the curvature's structure. The framework does not yet specify the mathematical form this directional structure takes, but the definition allows for it.

---

## Why a Manifold Lets Us Describe This

The discussion above describes curvature as a property of how vacuum amount varies between neighboring regions, without invoking any specific mathematical structure. But to make the description precise, we need a way to talk about "neighboring regions" and "geometric extent" without secretly importing a separate coordinate system that the framework has not committed to.

The natural mathematical structure for this is a manifold.

A manifold is a space where, around every point, there is a local notion of nearness — a local geometry that lets you say which points are close to which others, and how close. Manifolds do not require an embedding in any larger space; they are self-contained geometric objects. A 4-dimensional manifold has 4-dimensional local structure at every point, but does not need to "live in" a 5-dimensional or higher space to do so.

This is exactly what the framework needs. P2 commits to vacuum being spacetime, and the description of curvature requires being able to talk about neighboring regions of vacuum and the geometric extent they cover. A manifold lets us do this without committing to anything beyond what the framework has already accepted: vacuum has internal geometric structure (regions, extents, neighbors), and that structure is intrinsic to the vacuum rather than imposed from outside.

The framework therefore takes the mathematical structure of vacuum-spacetime to be a manifold, with the vacuum's geometric extent at each point being a property of the manifold itself. Curvature, defined as the spatial differential of vacuum amount, is then a property of how this manifold's local structure varies from point to point.

We are not committing here to specific manifold features beyond this. Whether the manifold has a specific metric, a specific connection, a specific dimensionality, or specific topological features is left open. What we are committing to is that vacuum-spacetime has manifold-like structure — local nearness, intrinsic geometric extent, no separate coordinate background — and that this is enough to make the curvature definition precise.

This is a minimal commitment. It says less than committing to a Riemannian or Lorentzian manifold with a specific metric (which would import the standard GR machinery). It says more than committing to nothing (which would leave the curvature definition without mathematical grounding). It commits to exactly what the framework needs in order to talk about vacuum amount varying across neighboring regions, in framework-native terms.

---

## What the Postulate Buys

P3a's definition of curvature lets later postulates refer to curvature with a specific framework-native meaning. Several specific moves become available.

**Curvature can carry energy.** A subsequent postulate can commit to configurations with curvature having energy beyond the substance energy of the vacuum present. Without P3a, "configurations with curvature" would be undefined; with P3a, it has a specific meaning.

**Curvature can have gradients.** A subsequent postulate can talk about gradients of curvature as drivers of dynamics, with specific framework meaning: gradients are how the spatial differential of vacuum amount changes from one region to another.

**Curvature relaxation has meaning.** A subsequent postulate can commit to curved configurations relaxing toward less curved configurations, with specific framework meaning: relaxation moves toward configurations where the spatial differential of vacuum amount is smaller.

**Mass-as-constraint can be specified.** Mass, in the framework, will eventually be characterized by the constraints it imposes on the surrounding vacuum. Those constraints are constraints on the spatial pattern of vacuum amount — specifically, on the curvature pattern. P3a lets the framework make this characterization specific.

Each of these is open work that later postulates address. P3a doesn't do that work; it provides the foundation on which the work can be done.

---

## What the Postulate Does Not Do

P3a is a definition, not a derivation of physical content. Several things are left open.

**The mathematical form of the differential.** P3a says curvature is a spatial differential of vacuum amount. It does not specify whether this differential is a scalar, a vector, a tensor, or a richer object. The mathematical form depends on additional commitments the framework has not made, and is part of the open work on the vacuum's mathematical structure.

**The relationship to standard curvature tensors.** P3a's curvature is a framework-native concept. Whether it can be identified with the Riemann curvature tensor of standard differential geometry, or with the Ricci tensor, or with some other standard quantity, depends on whether the framework's vacuum manifold turns out to have the structure required for those tensors to be defined. This is open work.

**The relationship between curvature and matter.** P3a defines curvature without saying anything about what causes it or what configurations of matter produce specific curvature patterns. The relationship is the subject of later postulates and consequences.

**The dynamics of curvature change.** P3a says what curvature is at a moment, not how it evolves. Dynamics is the subject of later postulates.

**Quantitative content.** P3a defines curvature qualitatively (variation in vacuum amount across neighbors). It does not quantify the relationship between vacuum amount differences and curvature magnitude. Quantification depends on the mathematical structure of the vacuum manifold and is open work.

---

## Imports

This postulate invokes:

- SR9: Local Validity of SR in Inertial Frames (the local geometric structure of the manifold reduces to Minkowski in the absence of curvature)

It depends on:

- P1: Vacuum-Energy Equivalence (the substance whose amount is being differentiated is vacuum-as-energy)
- P2: Vacuum-Spacetime Identity (vacuum is spacetime, so vacuum amount differentials are spatial differentials)
- P3: Vacuum Energy Density (density is constant, so geometric variation must be in extensive vacuum amount rather than intensive density)
