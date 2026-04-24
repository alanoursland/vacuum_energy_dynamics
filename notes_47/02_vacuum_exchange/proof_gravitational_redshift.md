# Proof: Gravitational Redshift

---

## What This Document Is

This is the framework's first derivation — a demonstration that the core postulates produce a known physical result, with a specific addition that standard physics does not provide.

The known physical result is gravitational redshift: a photon climbing out of a gravitational gradient loses energy, with the energy change related to the height of the climb and the local gravitational acceleration by $\Delta E / E = -gh/c^2$ in the weak-field limit. This formula is well-established, verified by the Pound-Rebka experiment in 1959 [Pound & Rebka, 1960] and by many subsequent atomic-clock experiments at different altitudes. Deriving it is a necessary consistency check for any framework proposing to account for gravitational phenomena.

The addition our framework provides is a physical source and sink for the energy change. Standard physics gives the formula but leaves the energy change as unexplained bookkeeping — the photon loses energy going up, gains energy going down, and the energy's origin or destination is handled (in general relativity) through coordinate-dependent pseudo-tensor machinery that does not correspond to any local physical process. Our framework identifies what happens to the energy: it goes into vacuum regeneration on ascent, and comes from vacuum consumption on descent. Energy that appears to vanish in standard treatments has a specific physical location in ours.

---

## The Setup

Consider a photon of energy $E$ traveling vertically through a region with a local gravitational acceleration $g$. Here, $g$ is the magnitude of the curvature gradient, observable as the acceleration a test mass would experience at that location. We treat $g$ as a given quantity of the region, without deriving its value from an underlying mass distribution — the framework does not yet have a mechanism for how mass produces gradients (see the force-mechanism open question). What the framework can derive is what happens to a photon traversing a region of gradient strength $g$, which is sufficient to reach the redshift formula.

Three postulates are invoked.

Postulate 1 establishes that the vacuum has finite locally constant energy density, so the vacuum is a physically real quantity in the region.

Postulate 2 establishes that energy in a gradient experiences force along the gradient and that motion along the gradient is coordinated with vacuum exchange. A photon moving upward against the gradient has its momentum along the gradient reduced, and this reduction is coordinated with vacuum regeneration in the region traversed. A photon moving downward has its momentum along the gradient increased, coordinated with vacuum consumption.

Postulate 3 establishes that the photon, though it has zero rest mass, participates in vacuum exchanges as if it possessed mass $E/c^2$. This lets us apply the force-per-unit-energy structure of Postulate 2 to the photon through its total energy.

Special relativity provides the relationship $p = E/c$ for photons, linking momentum to energy.

---

## The Derivation

Let the photon be at height $h$ moving upward. Over an infinitesimal height $dh$, the photon moves against the gradient, and we want to determine the change in its energy $dE$.

By Postulate 2, the force on the photon is directed along the gradient, opposing its motion. The force per unit energy is proportional to the gradient strength — specifically, to $g/c^2$, where the factor of $c^2$ comes from converting the gradient (an acceleration) into a force-per-unit-energy via Postulate 3's mass-energy equivalence. A photon of energy $E$ experiences a force of magnitude $(E/c^2) \cdot g$ directed downward.

As the photon moves upward by $dh$, the force does negative work on the photon. The work done on the photon equals the force times the displacement along the force direction:

$$dW = -\left(\frac{E}{c^2}\right) g \, dh$$

The negative sign reflects that the force (downward) and the displacement (upward) are opposite.

This work equals the change in the photon's energy:

$$dE = -\left(\frac{E}{c^2}\right) g \, dh$$

Rearranging:

$$\frac{dE}{E} = -\frac{g \, dh}{c^2}$$

Integrating from height $0$ to height $h$, treating $g$ as approximately constant over the range (valid in the weak-field limit, which we address below):

$$\ln\left(\frac{E(h)}{E_0}\right) = -\frac{gh}{c^2}$$

$$E(h) = E_0 \exp\left(-\frac{gh}{c^2}\right)$$

In the weak-field limit, where $gh \ll c^2$, the exponential expands to first order:

$$E(h) \approx E_0 \left(1 - \frac{gh}{c^2}\right)$$

$$\frac{\Delta E}{E} \approx -\frac{gh}{c^2}$$

This is the gravitational redshift formula. It matches the standard result and agrees with the Pound-Rebka measurement and subsequent tests to within experimental precision.

---

## Where the Energy Goes

The derivation above produces the redshift formula. What the derivation also tells us — and what standard physics does not — is where the photon's energy goes during its ascent.

By Postulate 2, the coordinated counterpart to the photon's energy loss is vacuum regeneration in the region traversed. The energy the photon loses over the height $dh$ is not destroyed and not passed into any geometric bookkeeping quantity without physical location. It is converted into vacuum energy, which restores vacuum in the region the photon has just climbed through.

Concretely: over the photon's full ascent from $h = 0$ to height $h$, the total energy the photon loses is $E_0 - E(h) = E_0 (1 - \exp(-gh/c^2))$. This energy has become vacuum in the region between the emission point and the reception point. The region now contains slightly more vacuum than it did before the photon passed through, and under the identity postulate, slightly more spacetime, meaning the region has slightly relaxed its curvature.

The reverse holds for descent. A photon falling from height $h$ to height $0$ arrives with more energy than it started with, by the inverse of the ascent factor. The additional energy has come from vacuum in the region of descent, which has been consumed. The region now contains slightly less vacuum than before, with correspondingly increased curvature.

This is the contribution the framework makes that standard physics does not. The redshift formula is the same; the physical account of the energy flow is new. Under our framework, gravitational redshift is not an unexplained consequence of geometry but a concrete energy exchange between the photon and the vacuum it traverses.

---

## The Two Pictures for Light

In the document introducing Postulate 2, we flagged that how light interacts with the vacuum exchange mechanism is an open question. Two candidate pictures were named: Picture 1, in which light fully participates in vacuum exchange (photons pay energy to regenerate vacuum during ascent); and Picture 2, in which light refracts through the reshaped vacuum geometry without direct participation, with observable effects being geometric consequences of the traversal.

The derivation above, on its face, uses Picture 1 — it treats the photon as actively regenerating vacuum and losing energy in the process. This is the natural reading under the vacuum-as-energy commitments of the framework.

Picture 2 does not give a different numerical result. Under Picture 2, the frequency ratio between emitter and receiver is a geometric consequence of the vacuum's arrangement in the region between them, rather than the result of active energy exchange by the photon. The formula $\Delta E/E = -gh/c^2$ falls out of either picture, because it is ultimately a statement about how energy observed at one height relates to energy observed at another, and both pictures agree on this relation.

Where the pictures differ is on the physical meaning of the energy change. Under Picture 1, energy literally moves between photon and vacuum. Under Picture 2, the energy measurements at different heights are different quantities related by the geometry, without an underlying transfer.

The proof above, strictly speaking, is a Picture 1 derivation. It invokes Postulate 2's exchange mechanism as operating on the photon. If we want the proof to be agnostic between pictures, we would reframe it as deriving the frequency ratio without specifying whether an exchange is happening — but we would also lose the "where the energy goes" contribution that makes the proof distinctive from standard derivations. Under Picture 2, there is no source or sink in the framework's sense; the energy's apparent disappearance or appearance is a measurement relationship, not a physical transfer.

We note this honestly. The proof's strongest contribution — identifying a source and sink for the energy change — depends on Picture 1 being correct. Under Picture 2, the proof reduces to a consistency check with the standard formula, without the distinctive content. Resolving which picture is correct is open work for the framework.

---

## Scope and Limitations

The proof is valid in the weak-field limit, where $g$ is approximately constant over the integration range and $gh \ll c^2$. This covers most practically relevant situations: the Pound-Rebka experiment at 22.5 meters on Earth's surface, atomic-clock experiments at altitudes of meters to kilometers, and similar configurations.

For strong fields, the proof needs modification in two places.

First, $g$ is not constant with height in strong fields. The integration would need to account for $g(h)$, which depends on the configuration of mass producing the gradient. Our framework does not currently have a mechanism for how mass produces gradients (see the force-mechanism open question), so we cannot derive $g(h)$ from first principles. We could import it from an external theory (such as GR) to do the integration, but that would be using that theory's machinery rather than our framework's.

Second, the exponential form $E(h) = E_0 \exp(-gh/c^2)$ assumes a particular relationship between the gradient and the energy-loss rate that may not hold exactly in strong fields. The correct strong-field result in general relativity involves a square-root factor $\sqrt{1 - 2GM/rc^2}$ rather than a simple exponential. Whether our framework, once it has a working mechanism and a derivation of how $g$ depends on mass configuration, would produce the GR result or something different is not known.

What this means practically: the proof establishes that the framework is consistent with all currently-tested gravitational redshift observations. It does not establish that the framework matches GR in strong-field regimes, because we cannot yet perform the strong-field calculation in our framework's own terms.

---

## What This Proof Accomplishes

The proof is a consistency check and a demonstration.

As a consistency check, it shows that the framework's postulates produce the observed gravitational redshift formula in the regime where the formula has been experimentally tested. The framework is not ruled out by this observation; it reproduces the expected result.

As a demonstration, it shows the framework doing what it was designed to do: treat vacuum as an energy participant rather than an unexplained geometric backdrop. The photon's energy change has a specific physical location under this framework. Standard physics gives the formula without specifying where the energy goes. Our framework gives the formula and specifies where the energy goes.

The proof does not show our framework is better than GR. It shows our framework is consistent with the best-tested gravitational prediction and contributes an account of energy flow that GR lacks. Whether this account is correct — whether vacuum is literally regenerated by climbing photons in the amounts our framework predicts — is a question beyond the proof itself. The framework commits to an answer; verifying that answer requires experiments we cannot currently perform.

---

## References

Einstein, A. (1907). Über das Relativitätsprinzip und die aus demselben gezogenen Folgerungen [On the Relativity Principle and the Conclusions Drawn from It]. *Jahrbuch der Radioaktivität und Elektronik*, 4, 411–462.

Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. *Physical Review Letters*, 4(7), 337–341.
