# Proof: Gravitational Time Dilation

---

## What This Document Is

This is the framework's second derivation. It shows that the core postulates produce a known physical result — gravitational time dilation — in the weak-field limit, and provides a physical account of the phenomenon that standard physics leaves interpretive.

The known physical result is that clocks at lower gravitational potential tick more slowly than clocks at higher potential, by a factor of approximately $1 + gh/c^2$ in the weak-field limit. This has been verified by the Pound-Rebka experiment (1960) when analyzed as a time-dilation effect, by Hafele-Keating (1972) with atomic clocks on aircraft, by the operation of GPS satellites, and by modern optical-clock experiments at centimeter-scale height differences [Chou et al., 2010].

The framework's contribution is twofold. First, the quantitative result falls out of the gravitational redshift proof directly, without new machinery — time dilation and redshift are two aspects of the same underlying phenomenon in this framework. Second, the framework provides a physical account of the phenomenon that is relational rather than absolute. Clocks do not locally run slow; their local rates are unchanged. What differs is the mapping between local proper times at different gravitational potentials, and the framework attributes that mapping to vacuum extent rather than to a metric field. The same variation in vacuum extent that produces the time mapping also produces a spatial mapping, and the two together are the framework's gravitational analogue of special relativity's time dilation and length contraction.

---

## The Setup

Two clocks are placed at different heights in a static gravitational gradient of local strength $g$. Clock A sits at height $0$; Clock B sits at height $h$. Both clocks are identical in construction — they tick at the same local proper rate $\tau$ (time per tick) when measured in their own local frames. The question is how their rates compare when one observes the other.

The derivation invokes the following.

Postulate 1 establishes that the vacuum has finite locally constant energy density. Postulate 3 establishes that energy in a gradient experiences force along the gradient, with vacuum exchange coordinated to the motion. Mass-energy equivalence (from SR; see `sr_mass_energy_equivalence.md`) establishes that all forms of energy participate in vacuum exchanges per unit energy. Special relativity provides the relation $p = E/c$ for photons, through which Postulate 3's force-per-unit-energy structure applies to photons.

The derivation also uses the result of the gravitational redshift proof: a photon emitted at height $0$ with frequency $\nu_0$ and received at height $h$ has frequency $\nu(h) = \nu_0 \exp(-gh/c^2)$, which reduces to $\nu(h) \approx \nu_0 (1 - gh/c^2)$ in the weak-field limit. This result itself depends on Postulates 1 and 3, mass-energy equivalence, and special relativity, so the time dilation derivation inherits exactly those dependencies and adds nothing formal beyond the observation that clocks emit photons at their local rate.

The physical interpretation in the later section additionally invokes the identity postulate and the curvature-as-spatial-volume-differential consequence. These are used to explain *why* the mapping between clocks at different potentials takes the form it does, not to derive the mapping itself. Readers who accept the formal derivation but are uncommitted on the identity postulate can accept the quantitative result while reserving judgment on the interpretation.

---

## The Derivation

Let Clock A, at height $0$, emit a photon at each tick. The photons have frequency $\nu_A = 1/\tau$ in Clock A's local frame, where $\tau$ is the time between ticks as measured by Clock A.

Each photon travels upward to Clock B. By the redshift proof, a photon emitted at height $0$ with frequency $\nu_A$ arrives at height $h$ with frequency:

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

The derivation above produces the formula. What the derivation also tells us — and what standard physics does not make explicit — is the physical mechanism behind the mapping it captures.

**Lower clocks do not locally run slow.** They run at their normal local rate, in their own local vacuum, and local observers at any location measure their own clocks, rulers, and speed of light exactly as they would in flat space. Special relativity requires this, and the framework preserves it. What differs between clocks at different gravitational potentials is not an absolute property of either clock but the *mapping* between local proper time at one location and local proper time at another.

The framework attributes that mapping to vacuum extent rather than to a metric field. This is the key interpretive claim: there is no separate geometric object (a metric) that has independent dynamics and happens to govern how clocks at different locations relate. There is only the vacuum, which is spacetime, and whose extent per coordinate span varies between locations in a gradient. The variation in extent is what produces the variation in mapping.

A clock is a process that depends on information propagating through the vacuum it is embedded in. Any clock — atomic transitions, light bouncing between mirrors, a pendulum swinging — involves some internal dynamics that require signals or correlations to traverse some portion of the clock's own extent. The rate at which any such process completes depends on how fast these signals propagate through the local vacuum, and locally that rate is $c$, the same at every location. What varies between locations is not the local rate but the amount of vacuum per coordinate span, which determines how local rates map to rates observed from elsewhere.

The vacuum is the substrate that constrains information propagation, per the identity postulate. The amount of vacuum per coordinate span differs between flat regions and gravitational wells, per the curvature-as-spatial-volume-differential consequence. A coordinate span in a gravity well contains less vacuum than the same coordinate span in flat space. Local observers inside the well do not see this — they measure their local vacuum content as whatever it is, they measure light's speed as $c$, and their clocks tick at their local rate. But when Clock B (in flatter vacuum) receives signals from Clock A (in more depleted vacuum), the signals have traversed a region whose vacuum-per-coordinate-span differs from B's own, and the received rate differs from B's local rate accordingly. This is the mapping that the derivation quantifies.

The photon-derivation in the previous section is a proof of principle for a universal claim. Because Postulate 3 applies to every form of energy uniformly, any process used to compare clocks at different potentials — photon exchange, particle decay timing, any signal-based comparison — would yield the same mapping. The universality of gravitational time dilation, which standard physics treats as a fact about the metric's time-time component, has a direct physical cause in the framework: every process that compares two locations is constrained by the same vacuum structure, and that structure determines the mapping for all of them.

---

## Time Dilation and Redshift Are One Phenomenon

The derivation above uses the redshift formula to derive time dilation. This is not a coincidence or a technical convenience. In the framework, time dilation and redshift are two aspects of the same underlying phenomenon.

Redshift is what happens to the frequency of a photon as it traverses a vacuum gradient: it loses energy going up, gains energy going down, with the change reflected in the frequency shift. Time dilation is what happens to clock rates at different depths in a well: clocks tick more slowly in deeper regions. Both effects arise from the same physical fact — the vacuum's extent per coordinate span differs between locations in a gradient.

A photon crossing between locations experiences this as a frequency shift. A clock at either location, measured locally, ticks at its normal rate — but the mapping between that local rate and a local rate at another potential depends on the vacuum traversed between them. An observer comparing two clocks at different depths sees both manifestations of the same phenomenon: the photons used to compare the clocks shift in frequency during the comparison, and the rate assignment each observer makes for the other differs from their own local rate. Two observational channels, one underlying fact about the vacuum between them.

General relativity also unifies redshift and time dilation, through the metric. The framework unifies them through vacuum content and its effect on propagation. The two unifications are compatible at the level of observable predictions but locate the unification differently. Under GR, the metric is the primary object and both effects are consequences of its variation. Under the framework, the vacuum is the primary substance and both effects are consequences of its variation in extent.

---

## The Spatial Companion Effect

The same vacuum-per-coordinate-span variation that produces the time-mapping difference also produces a spatial-mapping difference. These are not separate effects with separate causes; they are two sides of the same underlying fact.

Consider a radial span through a gravity well. Local observers inside the well measure the proper length of the span using their own local rulers, and they get some value. An external observer in flatter space, using coordinates anchored far from the well, measures the same span in their coordinate system, and they get a different value — the coordinate span corresponds to *more* proper length than the external coordinate extent would suggest, because the well contains less vacuum per unit of external coordinate. This is the radial stretching noted in the curvature-as-spatial-volume-differential consequence: proper radial distances near a mass are longer than the external geometry alone indicates.

This is the framework's gravitational analogue of special relativity's length contraction, standing alongside gravitational time dilation as the corresponding analogue of SR's time dilation. In SR, two observers in relative motion assign each other different time and length measurements through the Lorentz transformation, with the differences linked and neither observer's measurements being absolute. In the framework, two observers at different gravitational potentials assign each other different time and length measurements through vacuum-per-coordinate-span variation, with the differences linked and neither observer's local measurements being absolute.

Naming this explicitly closes a coordinate-confusion question the time-dilation derivation alone might leave open. If vacuum extent per coordinate span is reduced in a well, does the framework claim clocks physically shrink? Does it claim only time is affected and spatial extent is preserved? Neither. The framework claims that both proper time intervals and proper spatial intervals differ between local and coordinate measurements in wells, and that both differences arise from the same vacuum-extent variation. Local observers, in their own frames, measure their own clocks and rulers normally; what varies across locations is the mapping, not the local measurements.

This preserves Lorentz invariance of the underlying structure. Special relativity says that at a single location, different inertial frames are related by Lorentz transformations that mix time and space measurements in a linked way. The framework adds that at different gravitational potentials, local frames are related by vacuum-extent-mediated mappings that likewise link time and space in a coordinated way. The two layers do not conflict: SR handles the single-location-different-velocity case; the framework handles the different-location-different-vacuum case. Both say that absolute local measurements are preserved while relations between observers differ in structured ways.

---

## Scope and Limitations

The derivation is valid in the weak-field limit, where $g$ is approximately constant over the height $h$ and $gh \ll c^2$. This covers all precision clock experiments performed to date:

- Pound-Rebka (1960) at 22.5 meters, which tests the redshift-time-dilation relationship at the level of $\Delta\nu/\nu \sim 10^{-15}$.
- Hafele-Keating (1972) with cesium clocks carried on commercial aircraft at cruising altitude.
- GPS satellites, which require time-dilation corrections of about 38 microseconds per day to maintain positioning accuracy.
- Optical-clock experiments at centimeter-scale height differences [Chou et al., 2010], which detect time dilation at height differences small enough to demonstrate the effect over laboratory scales.

All are consistent with the derivation's prediction within experimental precision.

For strong fields, the derivation inherits the limitations of the redshift proof. The exponential form $\tau_{\text{observed}} = \tau \exp(gh/c^2)$ differs from GR's strong-field result $\tau_{\text{observed}} = \tau / \sqrt{1 - 2GM/rc^2}$ at higher order in $GM/rc^2$. The two forms agree to leading order but diverge as the field strengthens. Reconciling them — or determining whether the framework's strong-field prediction genuinely differs from GR's — requires deriving the $\rho_v$ profile around a mass, which is currently open work. The weak-field agreement is established; the strong-field comparison awaits further development of the framework.

---

## Dependency Structure

The derivation depends only on Postulates 1 and 3, mass-energy equivalence, the identity postulate (for interpretation), the curvature-as-spatial-volume-differential consequence (for interpretation), and special relativity. It does not invoke Postulates 4 or 5, which handle configuration energy and minimum-energy dynamics.

This narrow dependency is a feature worth noting. Time dilation is insulated from any future revisions to the framework's treatment of configuration energy or wave dynamics. The prediction stands on a tighter base than the framework as a whole. If Postulates 4 or 5 need revision in light of work on field equations, wave modes, or cosmological dynamics, the time-dilation and redshift results do not need to be redone.

The narrow dependency also means that the pair of results (redshift and time dilation) together form a tight subframework: Postulates 1 and 3, mass-energy equivalence, the identity postulate, and special relativity together yield both results, and together they reproduce two independent precision tests of gravitational physics. Any alternative framework that denies these postulates must find another way to account for both observations; any framework that accepts them inherits both predictions.

---

## What This Proof Accomplishes

As a consistency check, the proof demonstrates that the framework produces the observed weak-field time dilation formula. Together with the redshift proof, the framework now reproduces two independent precision tests of gravitational physics from the same postulate base.

As a demonstration, the proof shows the framework unifying two seemingly distinct gravitational effects — redshift and time dilation — under a single underlying mechanism. Vacuum-per-coordinate-span varies between locations in a gradient; photons traversing the gradient shift in frequency; the mapping between local proper times at different depths differs from the flat-space mapping; both effects are visible manifestations of the same variation. GR provides a similar unification through the metric. The framework provides it through vacuum content, with the physical account being framework-native content that GR does not supply.

As a commitment, the proof binds the framework to a specific physical account of the time-mapping difference: it arises from vacuum extent per coordinate span varying between locations, not from any absolute slowing of clocks or any independent metric field. This account is in principle testable beyond the time-dilation formula itself — tests that probe the detailed structure of the well rather than integrated effects on clocks or photons could in principle distinguish this account from GR's metric-level account. Such tests are beyond current experimental capability, but the framework's commitment is specific enough to be, in principle, falsifiable.

The derivation does not show that the framework is superior to GR. It shows that the framework reproduces GR's weak-field prediction through different machinery and provides a distinctive physical account of what the effect is. Whether that account is correct — whether the vacuum's extent per coordinate span is literally what produces the mapping between clocks at different potentials — is a question beyond the proof itself. The framework commits to the answer; verification awaits experimental regimes we cannot yet reach.

---

## References

Chou, C. W., Hume, D. B., Rosenband, T., & Wineland, D. J. (2010). Optical clocks and relativity. *Science*, 329(5999), 1630–1633.

Hafele, J. C., & Keating, R. E. (1972). Around-the-world atomic clocks: Predicted relativistic time gains. *Science*, 177(4044), 166–168.

Pound, R. V., & Rebka, G. A. (1960). Apparent weight of photons. *Physical Review Letters*, 4(7), 337–341.