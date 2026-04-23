# A Vacuum-Consumption Ontology for Gravity

## Working Notes Toward a Relativistic Theory of Gravitation

---

## Preface

These notes develop a physical interpretation of gravity in which the vacuum is not an empty backdrop for physics but is itself the substance of spacetime, carrying energy density and participating in energy exchange with matter. The motivating intuition is that gravitational potential energy — a quantity treated as pure bookkeeping in Newtonian mechanics and as geometrically encoded in General Relativity — should correspond to something physically real and locally conserved.

The approach is deliberately minimalist. We begin from two foundations: special relativity (in particular, mass-energy equivalence) and a small set of postulates about the vacuum. From these, we attempt to derive gravitational phenomena without importing the machinery of General Relativity. Where our predictions coincide with GR, we learn that the framework is at least an interpretation. Where they diverge, we have candidates for a falsifying experiment.

This document captures the opening moves. It is not a complete theory, and it does not yet contain field equations. It is closer in spirit to Einstein's 1907 "happiest thought" — the equivalence principle as a thought experiment — than to the 1915 field equations. The aim is to see how far sharp postulates and careful reasoning can take us before we are forced into the heavier mathematical apparatus.

---

## 1. Motivation: The Problem of Gravitational Potential Energy

Consider a mass falling through a gravitational field. It gains kinetic energy. In Newtonian mechanics we say this kinetic energy comes from the mass's gravitational potential energy, defined such that the total energy is conserved:

$$E_{\text{total}} = \frac{1}{2}mv^2 + U(r) = \text{constant}$$

This is internally consistent, but it is not a physical mechanism. Gravitational potential energy is defined as the quantity that makes the books balance. It is not stored anywhere in particular. It has no local density. It is a mathematical convenience.

General Relativity handles this differently and, in some ways, less satisfyingly. In a general curved spacetime there is no global energy conservation law at all, because there is no preferred timelike Killing vector. Energy conservation in GR is either local (via the covariant divergence of the stress-energy tensor, which does not yield a conserved total) or confined to spacetimes with special symmetries (static, asymptotically flat). The question "where does the kinetic energy of a falling mass come from?" is, in GR, not so much answered as dissolved.

We take the unfashionable view that the question is a good one. If energy is conserved — and all our experimental evidence says it is, locally — then when a mass gains kinetic energy, that energy came from somewhere physical. This document proposes an answer: it came from the vacuum.

---

## 2. The Postulates

We adopt the following postulates. Special relativity is assumed throughout; no part of General Relativity is assumed.

**Postulate 1 (Vacuum Energy Density).** The vacuum possesses an energy density $\rho_v$, with units of energy per unit volume.

**Postulate 2 (Descent Consumes Vacuum).** When a mass or an energy quantum moves through a gradient in $\rho_v$ in the direction of decreasing $\rho_v$, it gains kinetic energy. This energy is drawn from the vacuum, which is locally consumed:
$$\Delta E_{\text{kinetic}} = -\Delta E_{\text{vacuum in region}}$$

**Postulate 3 (Ascent Regenerates Vacuum).** The reverse process also holds. Energy moving against a gradient in $\rho_v$ (climbing out of a gravity well) regenerates vacuum and loses an equivalent amount of its own energy.

**Postulate 4 (Mass-Energy Equivalence).** All energy, including the kinetic energy of a photon and the rest energy of a massive particle, participates in these exchanges equivalently. A photon of energy $E$ behaves, for the purposes of vacuum exchange, as if it possessed mass $E/c^2$.

Postulate 4 is not an independent assumption; it follows from special relativity, which we have adopted as background. We state it explicitly because it will do heavy lifting in the derivations.

### Interpretive Commitment (Not a Postulate)

The above postulates are sufficient for the derivations that follow. We also adopt, as an interpretive stance rather than a mathematical postulate, the view that **the vacuum is the substance of spacetime itself** — not a state of fields living on a pre-existing manifold, but the manifold's own constitutive stuff. Regions with more vacuum are regions where more space exists. Gravitational curvature corresponds to spatial variation in $\rho_v$.

We flag this as interpretation rather than postulate because, at present, no derivation in this document depends on it. A reader who rejected this interpretation and treated $\rho_v$ as a field on an independent spacetime could still follow all the calculations that follow. The interpretation does, however, motivate the ontological picture and is expected to become load-bearing when we attempt to derive the spatial structure of $\rho_v$ around a mass (a derivation not yet completed). If and when that derivation succeeds, this interpretation may be promoted to a postulate. If it turns out the derivation can be completed without it, it should remain demoted, or dropped entirely. We keep it here because it distinguishes this framework from ordinary scalar field theories and gives the work its distinctive ontological character.

---

## 3. Visualization: The Stitched Sheet

The standard rubber-sheet visualization of gravity is pedagogically useful but ontologically misleading. It depicts spacetime as a pre-existing elastic surface that is dented downward by the weight of objects placed upon it. This conceals the fact that in GR, there is no "underneath" the sheet. The sheet is everything.

A more faithful visualization for our purposes is the following. Imagine a flat rubber sheet. Remove a small disk of material from one region. Now stitch together the edges of the resulting hole. The sheet cannot remain flat: forced to close around the missing area, it must pucker into the third dimension, forming a region of concentrated curvature near the stitching, with curvature gradually diminishing at larger radii.

This is, mathematically, a conical defect. Crucially, no force was applied to produce the curvature. The curvature arose entirely from the removal of area. The sheet is curved because there is less of it than there "should" be.

In our framework, this is precisely what a mass is. A mass is not an object sitting on spacetime and denting it. A mass is our name for the geometrical consequence of a region where vacuum has been consumed and the surrounding space has closed in around the deficit. The gravitational field is the pucker.

This inversion of the usual causal story is worth dwelling on. In standard GR:

> Mass-energy sources curvature. Curvature is the response of spacetime to the presence of matter.

In our framework:

> The deficit is primary. What we call "mass" is the puckered region surrounding a vacuum deficit. Matter does not cause curvature; matter *is* curvature, and curvature is the manifold's closure around missing vacuum.

---

## 4. First Derivation: Gravitational Redshift

We now derive a quantitative consequence of the postulates, without appealing to GR.

Consider a photon of energy $E$ at height $h$ in a static gravitational field, traveling upward through a region in which $\rho_v$ increases with height. (We take "up" as the direction of increasing $\rho_v$ — climbing out of a gravity well.) As the photon rises by an amount $dh$, Postulate 3 requires that it regenerate vacuum, losing energy in the process.

The rate of energy loss per unit height must depend on the local gradient of the vacuum field. Let us call this local gradient $g$, with units of acceleration (we will not yet assume any relationship between $g$ and the Newtonian gravitational acceleration; the notation is suggestive but the identification must be earned).

By Postulate 4, the photon's effective mass is $E/c^2$. The energy required to lift an effective mass $E/c^2$ against the gradient by $dh$ is, dimensionally and by analogy with the work-energy relation:

$$dE = -\frac{E}{c^2} \cdot g \cdot dh$$

This is a natural ansatz: the energy lost is proportional to the effective mass being lifted, the strength of the gradient, and the distance traveled. Rearranging:

$$\frac{dE}{E} = -\frac{g \, dh}{c^2}$$

Integrating from height $0$ to height $h$, assuming $g$ is approximately constant over the range of integration:

$$\ln\left(\frac{E(h)}{E_0}\right) = -\frac{gh}{c^2}$$

$$\boxed{E(h) = E_0 \, \exp\left(-\frac{gh}{c^2}\right)}$$

For weak fields ($gh \ll c^2$), we can expand the exponential:

$$E(h) \approx E_0 \left(1 - \frac{gh}{c^2}\right)$$

$$\frac{\Delta E}{E} \approx -\frac{gh}{c^2}$$

This is precisely the gravitational redshift formula. It was verified experimentally by Pound and Rebka in 1959 using gamma rays emitted at the top and bottom of a 22.5-meter tower at Harvard, and has since been confirmed with ever-increasing precision by atomic clocks at different altitudes.

We have derived gravitational redshift from our postulates alone. We did not invoke the Schwarzschild metric, Einstein's field equations, the equivalence principle as a separate assumption, or any feature of General Relativity. We used only special relativity (via mass-energy equivalence) and our vacuum-exchange postulates.

---

## 5. What We Have and Have Not Shown

It is worth being precise about what this derivation establishes and what it leaves open.

**We have shown:** If the vacuum-consumption postulates hold, then an energy quantum climbing a gradient in vacuum density loses energy in the manner described by the gravitational redshift formula, in agreement with experiment to the precision at which redshift has been measured.

**We have not shown:** That $g$ in our formula equals $GM/r^2$. We treated $g$ as an input — the local gradient of the vacuum field. To connect to Newtonian gravity and beyond, we must derive the spatial dependence of $\rho_v$ near a mass, which we have not yet done.

**We have not shown:** Why massive objects fall. We asserted in Postulate 2 that they do consume vacuum when moving through a gradient, but we have not derived the equation of motion from more fundamental principles.

**We have not shown:** The inverse-square law, the bending of light, perihelion precession, or any other classical test of GR beyond redshift.

**We have not shown:** That our framework gives the same predictions as GR in strong fields. In fact, the exponential form $E(h) = E_0 \exp(-gh/c^2)$ is suggestive. In weak fields it matches GR to first order. In strong fields, whether it continues to match depends on how $g$ itself varies with position, and on whether the exponential form is exact or is itself a weak-field approximation to some more complete expression. This is the most promising place to look for a falsifying divergence from GR.

---

## 6. Self-Consistency: The Energy Ledger

One check we can perform immediately is whether the full cycle of infall and escape conserves both energy and vacuum. Consider the following thought experiment.

A massive object of rest mass $m$ is released from rest at height $h$ and falls to the bottom of a gravitational well, reaching the floor with kinetic energy $K$. By Postulate 2, an amount of vacuum energy equal to $K$ was consumed during the fall.

The object strikes the floor, thermalizes, and radiates its kinetic energy away as photons of total energy $K$ (measured locally at the floor). These photons climb out of the well. By Postulate 3, as they climb, they regenerate vacuum, losing energy in the process. By the redshift formula, the energy arriving at height $h$ is reduced by the same factor by which an equal energy would have been blueshifted on the way down.

The vacuum regenerated by the escaping photons, integrated along their outward path, equals the vacuum consumed by the infalling mass, integrated along its inward path. The energy arriving at infinity is less than the original rest energy by exactly the binding energy that would be quoted in standard analyses.

**Net vacuum change: zero. Net energy change: zero (when including radiated photons).**

The ledger balances. This is reassuring but also somewhat worrying: if the ledger balances exactly as GR predicts, then to the order we have calculated, our framework may be an interpretation of GR rather than a distinct theory. The question of whether there is any regime in which the ledger balances differently is open.

---

## 7. Open Questions and Next Steps

Several questions remain before this framework can be called a theory rather than an intuition.

**On the spatial structure of $\rho_v$ near a mass.** We must determine how the vacuum density varies around a massive object. Two routes are available. The first is to derive it from a symmetry argument combined with the interpretive commitment that vacuum is spacetime itself (a spherically symmetric mass should produce a spherically symmetric vacuum deficit, and that deficit should translate into a specific geometric structure). The second is to derive it from a variational principle once we have identified an appropriate Lagrangian. Either route should, at leading order, yield Newton's law; the interesting question is what corrections appear. Note that a successful derivation along the first route would promote the interpretive commitment from stance to load-bearing postulate.

**On the equation of motion.** Why does a massive object accelerate down a gradient in $\rho_v$? One candidate is a principle of least action applied to the combined matter-plus-vacuum system: the object moves so as to maximize the rate at which vacuum is consumed (or equivalently, to minimize some action). Another is to posit that the object is in equilibrium with its local vacuum density and follows gradients passively. These are not equivalent and will give different predictions in sufficiently careful tests.

**On time dilation.** The framework so far treats gravitational redshift as a physical energy exchange. Gravitational time dilation is the same phenomenon viewed from a different angle: clocks at the bottom of a well run slow. It is natural to conjecture that the rate of a local clock is tied to the local vacuum density — lower $\rho_v$ means slower time. This needs to be formalized.

**On strong fields.** The exponential form of our redshift expression is interesting. If $g$ itself depends on position, the integrated redshift over a large height difference could differ from GR's prediction. This is a candidate falsifiable test that does not require extreme regimes, only careful accounting.

**On the cosmological constant.** If the vacuum has energy density $\rho_v$ and that energy gravitates, we recover something like the cosmological constant problem — but possibly with a cleaner interpretation, since $\rho_v$ here is literally the stuff spacetime is made of rather than the zero-point energy of fields living on spacetime. This may or may not be illuminating. It should be examined.

**On the quantum regime.** Vacuum consumption is, in this framework, a continuous classical process. In reality, matter is quantized and so presumably is any consumption process. The framework will eventually need a quantum formulation, or at least an account of how classical vacuum consumption emerges from quantum-scale dynamics.

The goal of the next phase is to make progress on the first two of these: the spatial structure of $\rho_v$ near a mass, and the equation of motion. With those in hand, we can compute orbital dynamics from first principles within the framework and compare the results to GR in regimes where the two might diverge.

---

## Appendix: Relationship to Existing Ideas

For completeness, we note that several ideas in this framework have partial precedents in the literature, though no single existing program combines them in the way proposed here.

The notion that gravity might be an emergent or entropic phenomenon rather than a fundamental force has been explored by Jacobson (1995), Verlinde (2011), and others. Our framework differs in that vacuum consumption is a locally physical exchange rather than a thermodynamic or informational relation.

The identification of vacuum energy with a physical substance has been periodically proposed in various "aether" revivals throughout the twentieth century, most of them incompatible with special relativity. Our framework is explicitly relativistic from the outset, so these historical objections do not apply without modification.

Scalar theories of gravity, beginning with Nordström (1912) and continuing through Brans-Dicke (1961) and scalar-tensor theories generally, provide examples of relativistic gravity theories that are not GR. Our framework may or may not fall within this family; this requires further development to determine.

The language of "vacuum deficit" producing curvature has some resonance with topological defect models in cosmology (cosmic strings, domain walls), but the ontology here is different: the vacuum is not a field with topological structure but the spacetime substrate itself.

None of these parallels should be taken as endorsements or derivations. They are noted so that, as the framework develops, it can be compared to adjacent ideas with appropriate care.
