# T2: Gravitational Time Dilation

## What This Theorem Establishes

Clocks at lower position in a curvature gradient tick more slowly than clocks at higher position, as measured by either observer comparing the other's rate to their own. In the weak-field limit:

$$\tau_A^{(B)} \approx \tau \left(1 + \frac{gh}{c^2}\right)$$

where $\tau$ is the local proper tick interval of identically-constructed clocks, $g$ is the gradient strength, $h$ is the height difference, $\tau_A^{(B)}$ is the tick interval that observer B (at height $h$) assigns to clock A (at height $0$), and the weak-field limit is $gh \ll c^2$.

This is the standard gravitational time dilation result, verified by Pound-Rebka (1960) when analyzed as time dilation, by Hafele-Keating (1972) with atomic clocks on aircraft, by GPS satellite operation (which requires time-dilation corrections of about 38 microseconds per day), and by modern optical-clock experiments at centimeter-scale height differences [Chou et al., 2010].

The framework derives this formula directly from T1 (gravitational redshift) plus the observation that clocks emit photons at their local rate. No new machinery is required beyond what T1 already establishes. Time dilation and redshift are two aspects of the same underlying phenomenon in the framework.

---

## The Setup

Two clocks are placed at different heights in a static gradient of local strength $g$. Clock A sits at height $0$; Clock B sits at height $h$. Both clocks are identical in construction — they tick at the same local proper rate $\tau$ (time per tick) when measured in their own local frames. The question is how their rates compare when one observes the other.

The derivation invokes T1 (gravitational redshift) and the observation that any physical clock can be thought of as an emitter of photons at its tick rate.

T1 in turn depends on P1, P2, P3, P4, P6, SR4, and SR5. The time dilation derivation inherits exactly these dependencies — adding nothing beyond the photon-emission observation.

---

## The Derivation

Let Clock A, at height $0$, emit a photon at each tick. The photons have frequency $\nu_A = 1/\tau$ in Clock A's local frame, where $\tau$ is the time between ticks as measured by Clock A.

Each photon travels upward to Clock B. By T1, a photon emitted at height $0$ with frequency $\nu_A$ arrives at height $h$ with frequency:

$$\nu_{\text{received}} = \nu_A \exp(-gh/c^2)$$

Clock B, which itself ticks at local proper frequency $\nu_B = 1/\tau$ (identical to Clock A's local rate by construction), measures the received photons in its own local frame. Clock B observes photons arriving at rate $\nu_{\text{received}} = \nu_A \exp(-gh/c^2)$.

Since the photons were emitted at rate $\nu_A$ in Clock A's frame — one photon per tick of Clock A — the arrival rate at Clock B equals the rate at which Clock B registers Clock A's ticks. Clock B therefore assigns Clock A a tick frequency:

$$\nu_A^{(B)} = \nu_A \exp(-gh/c^2) \approx \nu_B(1 - gh/c^2)$$

or equivalently a tick interval:

$$\tau_A^{(B)} = \tau \exp(gh/c^2) \approx \tau(1 + gh/c^2)$$

in the weak-field limit $gh \ll c^2$.

This is the standard weak-field gravitational time dilation result. The notation $\nu_A^{(B)}$ denotes "the tick frequency Clock B assigns to Clock A" rather than any absolute property of Clock A. Clock A ticks at its own local rate $\nu_A = 1/\tau$ in its own frame, unchanged; what the derivation establishes is the mapping between that local rate and the rate Clock B measures when it receives Clock A's signals. Framed this way, the result is relational by construction and matches general relativity's weak-field prediction and all precision clock experiments performed to date within their experimental precision.

---

## What This Means Physically

The derivation produces the formula. The framework's foundational postulates also support a specific physical interpretation of what's happening.

**Lower clocks do not locally run slow.** They run at their normal local rate, in their own local vacuum, and local observers at any location measure their own clocks, rulers, and speed of light exactly as they would in flat space. SR9 requires this, and the framework preserves it. What differs between clocks at different positions in a gradient is not an absolute property of either clock but the *mapping* between local proper time at one location and local proper time at another.

The framework attributes that mapping to vacuum extent rather than to a metric field treated as primitive. Under P1 and P2, vacuum is the substrate that information propagates through, and is identified with spacetime itself. Under P3a, the amount of vacuum per coordinate span varies between regions in a gradient — that's what curvature is in the framework's vocabulary. The variation in vacuum extent is what produces the variation in the mapping between local clock rates.

A clock is a process that depends on information propagating through the vacuum it is embedded in. Any clock — atomic transitions, light bouncing between mirrors, a pendulum swinging — involves some internal dynamics that require signals or correlations to traverse some portion of the clock's own extent. The rate at which any such process completes depends on how fast these signals propagate through the local vacuum. Locally, that rate is $c$ at every location (by SR2 and SR9). What varies between locations is the amount of vacuum per coordinate span, which determines how local rates map to rates observed from elsewhere.

A coordinate span in a region of strong gradient contains less vacuum than the same coordinate span in flatter region. Local observers inside the gradient region do not see this directly — they measure their local vacuum content as whatever it is, they measure light's speed as $c$, and their clocks tick at their local rate. But when Clock B (in flatter vacuum) receives signals from Clock A (in more depleted vacuum), the signals have traversed a region whose vacuum-per-coordinate-span differs from B's own, and the received rate differs from B's local rate accordingly. This is the mapping that the derivation quantifies.

The photon-derivation in the previous section is a proof of principle for a universal claim. Because P6 applies to every form of energy uniformly, any process used to compare clocks at different positions — photon exchange, particle decay timing, any signal-based comparison — would yield the same mapping. The universality of gravitational time dilation, which standard physics treats as a fact about the metric's time-time component, has a direct physical cause in the framework: every process that compares two locations is constrained by the same vacuum structure, and that structure determines the mapping for all of them.

---

## Time Dilation and Redshift Are One Phenomenon

The derivation uses the redshift formula to derive time dilation. This is not a coincidence or a technical convenience. In the framework, time dilation and redshift are two aspects of the same underlying phenomenon.

Redshift is what happens to the frequency of a photon as it traverses a vacuum gradient: it loses energy going up, gains energy going down, with the change reflected in the frequency shift. Time dilation is what happens to clock rates at different positions: clocks tick more slowly in deeper regions of the gradient. Both effects arise from the same physical fact — the vacuum's extent per coordinate span differs between locations in a gradient (P3a).

A photon crossing between locations experiences this as a frequency shift. A clock at either location, measured locally, ticks at its normal rate — but the mapping between that local rate and a local rate at another position depends on the vacuum traversed between them. An observer comparing two clocks at different positions sees both manifestations of the same phenomenon: the photons used to compare the clocks shift in frequency during the comparison, and the rate assignment each observer makes for the other differs from their own local rate. Two observational channels, one underlying fact about the vacuum between them.

---

## The Spatial Companion Effect

The same vacuum-per-coordinate-span variation that produces the time-mapping difference also produces a spatial-mapping difference. Under P3a, vacuum amount per coordinate span is directional — it varies with direction at each point. The same directional pattern that determines temporal mappings also determines spatial mappings. These are not separate effects with separate causes; they are two sides of the same underlying directional structure.

Consider a radial span through a region of gradient. Local observers measure the proper length of the span using their own local rulers, and they get some value. An external observer in flatter region, using coordinates anchored far from the gradient source, measures the same span in their coordinate system, and they get a different value — the coordinate span corresponds to *more* proper length than the external coordinate extent would suggest, because the gradient region contains less vacuum per unit of external coordinate (in some directions; the precise pattern depends on the directional structure).

This is the framework's gravitational analogue of special relativity's length contraction (SR7), standing alongside gravitational time dilation as the corresponding analogue of SR's time dilation (SR6). In SR, two observers in relative motion assign each other different time and length measurements through the Lorentz transformation, with the differences linked and neither observer's measurements being absolute. In the framework, two observers at different positions in a gradient assign each other different time and length measurements through vacuum-per-coordinate-span variation, with the differences linked and neither observer's local measurements being absolute.

Naming this explicitly closes a coordinate-confusion question the time-dilation derivation alone might leave open. If vacuum extent per coordinate span is reduced in a gradient, does the framework claim clocks physically shrink? Does it claim only time is affected and spatial extent is preserved? Neither. The framework claims that both proper time intervals and proper spatial intervals differ between local and coordinate measurements in gradient regions, and that both differences arise from the same vacuum-extent variation. Local observers, in their own frames, measure their own clocks and rulers normally; what varies across locations is the mapping, not the local measurements.

This preserves Lorentz invariance of the underlying structure (SR1, SR9). Special relativity says that at a single location, different inertial frames are related by Lorentz transformations that mix time and space measurements in a linked way. The framework adds that at different positions in a gradient, local frames are related by vacuum-extent-mediated mappings that likewise link time and space in a coordinated way. The two layers do not conflict: SR handles the single-location-different-velocity case; the framework handles the different-location-different-vacuum case. Both say that absolute local measurements are preserved while relations between observers differ in structured ways.

---

## Scope and Limitations

The derivation is valid in the weak-field limit, where $g$ is approximately constant over the height $h$ and $gh \ll c^2$. This covers all precision clock experiments performed to date:

- Pound-Rebka (1960) at 22.5 meters, which tests the redshift-time-dilation relationship at the level of $\Delta\nu/\nu \sim 10^{-15}$.
- Hafele-Keating (1972) with cesium clocks carried on commercial aircraft at cruising altitude.
- GPS satellites, which require time-dilation corrections of about 38 microseconds per day to maintain positioning accuracy.
- Optical-clock experiments at centimeter-scale height differences [Chou et al., 2010], which detect time dilation at height differences small enough to demonstrate the effect over laboratory scales.

All are consistent with the derivation's prediction within experimental precision.

For strong fields, the derivation inherits the limitations of T1. The exponential form $\tau_{\text{observed}} = \tau \exp(gh/c^2)$ differs from the standard general-relativistic strong-field result at higher order in the gradient strength. The two forms agree to leading order but diverge as the field strengthens. Whether the framework's strong-field prediction matches the GR result or differs from it depends on the framework's specific configuration energy functional and constraint structure. The weak-field agreement is established; the strong-field comparison awaits further development of the framework.

---

## Dependency Insulation

This theorem depends on T1 plus the photon-emission observation. T1 itself depends on P1, P2, P3, P4, P6, SR4, and SR5. The time-dilation theorem inherits exactly these dependencies and adds nothing formal beyond noting that any physical clock can be thought of as a periodic emitter.

The theorem does not invoke P5 (minimum-energy dynamics). This narrow dependency is a feature worth noting. Time dilation is insulated from any future revisions to the framework's treatment of configuration-energy dynamics. The prediction stands on a tight base — the foundational postulates plus the substance-regime exchange content of P6. If P5 needs revision in light of work on field equations, wave modes, or other dynamical content, the time-dilation result does not need to be redone.

The narrow dependency also means that the pair of results (redshift and time dilation) together form a tight subframework. P1, P2, P3, P3a, P4, P6, SR4, and SR5 together yield both T1 and T2, which together reproduce two independent precision tests of gravitational physics. The framework's foundational ontology is sufficient for these tests.

---

## What This Theorem Accomplishes

The derivation produces a specific quantitative result that matches observation, derived from T1 plus a single observation. This is one of the framework's solid wins — derived from foundational postulates and SR imports without invoking any provisional commitments.

Three specific accomplishments are worth noting.

First, the framework reproduces a precisely-tested gravitational prediction. GPS, Hafele-Keating, optical-clock experiments, and other precision tests confirm the formula to high precision. The framework's derivation gives the same result without invoking general relativity.

Second, the framework unifies redshift and time dilation under a single underlying mechanism. Both are consequences of vacuum-per-coordinate-span variation between locations (P3a). GR provides similar unification through the metric. The framework provides it through vacuum content, with the physical account being framework-native content that GR does not supply.

Third, the framework names the spatial companion effect explicitly. Time dilation has a parallel in spatial-mapping differences between observers at different positions in a gradient, with both effects arising from the same directional variation in vacuum extent. The framework's gravitational analogues of SR's time dilation and length contraction are coordinated, just as in SR they are coordinated through the Lorentz transformation.

The derivation establishes that two of the classical weak-field gravitational tests are unconditional in the new postulate structure. T1 (gravitational redshift) and T2 (gravitational time dilation) depend on foundational postulates plus SR — no hypotheses, no provisional commitments. The framework's foundational ontology is sufficient for these.

Light deflection, Shapiro delay, and perihelion precession involve spatial-curvature content that goes beyond what the foundational postulates plus SR alone can supply. Whether these become unconditional in the new structure depends on whether the new postulates' added structure (P3a's directional content, P4's configuration energy depending on directional structure) is sufficient to derive the equal-response symmetry that gives $\gamma_v = 1$. T2's spatial companion content is suggestive — the framework already commits to spatial and temporal mappings being coordinated through directional vacuum extent — but turning this into a derivation of $\gamma_v = 1$ is the structural work the new framework is set up to address.

---

## Imports

This theorem invokes:

- SR1: Lorentz Invariance (the relational interpretation depends on each observer's local frame being a valid SR frame)
- SR2: Invariance of the Speed of Light (local clocks tick by processes propagating at $c$ in their own frame)
- SR4: Mass-Energy Equivalence (inherited through T1)
- SR5: Energy-Momentum Relation (inherited through T1)
- SR6: Time Dilation in Inertial Frames (the framework's gravitational time dilation parallels SR's kinematic time dilation)
- SR7: Length Contraction in Inertial Frames (the framework's spatial companion parallels SR's length contraction)
- SR9: Local Validity of SR in Inertial Frames (local measurements at any location are valid SR measurements)

It depends on:

- T1: Gravitational Redshift (the photon frequency relation that the time dilation derivation uses)
- P1: Vacuum-Energy Equivalence (the framework-native interpretation depends on vacuum being the propagation substrate)
- P3a: Spatial Differential is Curvature (the directional structure that supports both temporal and spatial mappings)

T1's full dependency chain (P1, P2, P3, P4, P6, SR4, SR5) is inherited.

---

## References

Chou, C. W., Hume, D. B., Rosenband, T., & Wineland, D. J. (2010). Optical clocks and relativity. *Science*, 329(5999), 1630–1633.

Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Predicted relativistic time gains. *Science*, 177(4044), 166–168.

Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. *Physical Review Letters*, 4(7), 337–341.
