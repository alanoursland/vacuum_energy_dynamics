# T1: Gravitational Redshift

## What This Theorem Establishes

A photon climbing through a curvature gradient loses energy in proportion to the height climbed and the local gradient strength. Specifically, in the weak-field limit:

$$\frac{\Delta E}{E} = -\frac{gh}{c^2}$$

where $g$ is the local gradient strength and $h$ is the height climbed against the gradient.

This is the gravitational redshift formula, well-established by the Pound-Rebka experiment in 1959 [Pound & Rebka, 1960] and many subsequent precision atomic-clock experiments. The framework derives this formula from its postulates plus SR imports, without invoking general relativity or any auxiliary commitments.

The framework also identifies a specific physical source for the photon's energy change: the energy lost during ascent is matched by vacuum creation in the region traversed, and the energy gained during descent comes from vacuum destruction. This is a contribution standard physics does not make — standard treatments give the formula but leave the energy change as bookkeeping without local physical content.

---

## The Setup

Consider a photon of energy $E$ traveling vertically through a region with local curvature gradient strength $g$. The gradient strength $g$ is the magnitude of the curvature gradient in the region, observable as the acceleration a test mass would experience there. The framework treats $g$ as a given quantity of the region, without deriving its value from an underlying mass distribution. What the framework can derive is what happens to a photon traversing a region of given gradient strength, which is sufficient to reach the redshift formula.

The derivation invokes the following postulates and SR imports.

**P3** (vacuum has finite locally constant energy density) establishes that vacuum is a physically real quantity in the region, with constant density.

**P6** (vacuum exchange in gradients) establishes that energy in a gradient experiences a force directed along the gradient, applied uniformly per unit energy, with kinetic energy (or, for photons, momentum-along-gradient) changes sourced and sunk by vacuum exchange.

**SR4** (mass-energy equivalence) establishes that the photon, though it has zero rest mass, participates in vacuum exchanges through its energy. The photon's effective inertial content for purposes of gradient force is $E/c^2$.

**SR5** (energy-momentum relation) provides the relationship $p = E/c$ for photons, linking momentum to energy.

---

## The Derivation

Let the photon be at height $h$ moving upward along the gradient direction. Over an infinitesimal height $dh$, the photon moves against the gradient, and we want to determine the change in its energy $dE$.

By P6, the force on the photon is directed along the gradient, opposing the photon's upward motion. The force per unit energy is $g/c^2$, where the factor of $c^2$ comes from converting the gradient (an acceleration) into a force-per-unit-energy via mass-energy equivalence (SR4). A photon of energy $E$ experiences a force of magnitude $(E/c^2) \cdot g$ directed downward.

As the photon moves upward by $dh$, the force does negative work on the photon. The work done equals the force times the displacement along the force direction:

$$dW = -\left(\frac{E}{c^2}\right) g \, dh$$

The negative sign reflects that the force (downward) and the displacement (upward) are opposite.

This work equals the change in the photon's energy:

$$dE = -\left(\frac{E}{c^2}\right) g \, dh$$

Rearranging:

$$\frac{dE}{E} = -\frac{g \, dh}{c^2}$$

Integrating from height $0$ to height $h$, treating $g$ as approximately constant over the range (valid in the weak-field limit, which we address in the scope section):

$$\ln\left(\frac{E(h)}{E_0}\right) = -\frac{gh}{c^2}$$

$$E(h) = E_0 \exp\left(-\frac{gh}{c^2}\right)$$

In the weak-field limit, where $gh \ll c^2$, the exponential expands to first order:

$$E(h) \approx E_0 \left(1 - \frac{gh}{c^2}\right)$$

$$\frac{\Delta E}{E} \approx -\frac{gh}{c^2}$$

This is the gravitational redshift formula. It matches the standard result and agrees with the Pound-Rebka measurement and subsequent precision tests within experimental precision.

---

## A Note on the Work-Energy Step

The step where we apply $dW = F \, dh$ to a photon deserves brief attention. The work-energy theorem in this form is a Newtonian construction, and applying it to a photon — which has no rest frame and travels at $c$ — is borrowing classical mechanics in a way that needs justification.

SR5's energy-momentum relation supplies the justification. For a photon, $dp/dt = F$ holds in the same way it does for any object under SR's framework, and $dE = c \, dp$ along the direction of motion. Combining these gives $dE = F \, dh$ along the photon's path. The work-energy step is therefore licensed by SR5 plus P6, not by Newtonian mechanics smuggled in.

This is worth being explicit about because the derivation looks Newtonian on the surface. The underlying structure is relativistic — SR's four-momentum framework is what makes "force on photon" and "work done on photon" well-defined.

---

## Where the Energy Goes

The derivation produces the redshift formula. P6 also commits the framework to a specific physical account of where the photon's energy goes during ascent.

By P6, kinetic energy changes (or, for photons, momentum-along-gradient changes) are sourced and sunk by vacuum exchange. The photon's energy loss during ascent is sunk by vacuum creation in the region traversed. The energy the photon loses over the height $dh$ does not vanish into bookkeeping — it becomes vacuum, which under P1 and P2 is energy and is spacetime.

Concretely: over the photon's full ascent from height $0$ to height $h$, the total energy the photon loses is $E_0 - E(h) = E_0 (1 - \exp(-gh/c^2))$. This energy has become vacuum in the region between the emission point and the reception point. The region now contains slightly more vacuum than it did before the photon passed through.

The reverse holds for descent. A photon falling from height $h$ to height $0$ arrives with more energy than it started with, by the inverse of the ascent factor. The additional energy has come from vacuum in the region of descent, which has been destroyed. The region now contains slightly less vacuum than before.

This is the contribution the framework makes that standard physics does not. The redshift formula is the same; the physical account of the energy flow is new. Under the framework, gravitational redshift is not an unexplained consequence of geometry but a concrete energy exchange between the photon and the vacuum it traverses.

The vacuum exchange is constrained by P4's smoothness requirement. Vacuum cannot be created or destroyed in a way that produces discontinuous changes in configuration. The exchange must be distributed in a way that keeps the configuration smooth, which generally means the vacuum changes are spread over a region rather than concentrated at the photon's instantaneous position. The framework commits to the total amount exchanged equaling the photon's energy change, but the specific spatial distribution of the exchange is downstream content depending on the configuration energy functional and the specific dynamics.

---

## Scope and Limitations

The theorem is valid in the weak-field limit, where $g$ is approximately constant over the integration range and $gh \ll c^2$. This covers most practically relevant situations: the Pound-Rebka experiment at 22.5 meters on Earth's surface, atomic-clock experiments at altitudes of meters to kilometers, and similar configurations.

For strong fields, the derivation needs modification in two places.

First, $g$ is not constant with height in strong fields. The integration would need to account for $g(h)$, which depends on the configuration of mass producing the gradient. The framework does not currently have a derivation of how mass configurations produce specific gradient profiles — mass-as-constraint determines the minimum-energy configuration, but the specific constraint structure imposed by mass and the resulting gradient profile are downstream content the framework hasn't fully developed.

Second, the exponential form $E(h) = E_0 \exp(-gh/c^2)$ assumes a particular relationship between the gradient and the energy-loss rate that may not hold exactly in strong fields. Whether the framework's strong-field result matches the standard general-relativistic result (which involves a square-root factor $\sqrt{1 - 2GM/rc^2}$) or differs from it depends on the framework's specific configuration energy functional and constraint structure. The framework's strong-field predictions are open work.

What this means practically: the theorem establishes that the framework reproduces the observed gravitational redshift formula in the regime where the formula has been experimentally tested. It does not establish that the framework matches GR in strong-field regimes, because the framework has not yet developed the structural content needed to perform strong-field calculations.

---

## What This Theorem Accomplishes

The derivation produces a specific quantitative result that matches observation, derived from the framework's postulates plus SR imports without auxiliary commitments. This is one of the framework's unconditional results — it depends only on foundational postulates and well-established physics, not on any provisional commitments the framework has had to make to enable other derivations.

Three specific accomplishments are worth noting.

First, the framework reproduces a precisely-tested gravitational prediction. Pound-Rebka and subsequent atomic-clock experiments confirm the formula to high precision. The framework's derivation gives the same result without invoking general relativity. This establishes that the framework's foundational ontology (vacuum is energy, energy in gradients experiences force, mass-energy equivalence) is sufficient to reach a known gravitational result.

Second, the framework provides a physical account of the energy flow that standard physics lacks. The photon's energy has a specific physical source and destination — real vacuum creation and destruction in the region traversed. This is the framework's distinctive contribution to gravitational redshift: not the formula (which is the same as GR's), but the local physical interpretation.

Third, the derivation establishes that two of the classical weak-field gravitational tests (gravitational redshift; gravitational time dilation, which follows from this theorem) are unconditional in the new postulate structure. They depend on P3, P6, SR4, and SR5 — foundational commitments — not on hypotheses or auxiliary assumptions. This sets a baseline for the framework's GR-recovery program: redshift and time dilation are solid wins from the foundational postulates alone.

The other classical weak-field tests (light deflection, Shapiro delay, perihelion precession) involve spatial-curvature content beyond what the foundational postulates plus SR can supply. Whether these become unconditional theorems in the new structure depends on whether the new postulates' added structure (P3a's directional content, P4's configuration energy depending on directional structure) is sufficient to derive the equal-response symmetry that gives $\gamma_v = 1$. This is the structural question the previous iteration of the framework left open and that the new iteration is set up to address.

---

## Imports

This theorem invokes:

- SR4: Mass-Energy Equivalence
- SR5: Energy-Momentum Relation

It depends on:

- P1: Vacuum-Energy Equivalence (the energy being created or destroyed during exchange is real energy)
- P2: Vacuum-Spacetime Identity (the vacuum being created or destroyed is spacetime)
- P3: Vacuum Energy Density (vacuum is a real quantity with constant density)
- P4: Curvature Contains Energy (the smoothness requirement constraining the spatial distribution of exchange)
- P6: Vacuum Exchange in Gradients (the force on energy and the substance-regime exchange)

---

## References

Einstein, A. (1907). Über das Relativitätsprinzip und die aus demselben gezogenen Folgerungen [On the Relativity Principle and the Conclusions Drawn from It]. *Jahrbuch der Radioaktivität und Elektronik*, 4, 411–462.

Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. *Physical Review Letters*, 4(7), 337–341.
