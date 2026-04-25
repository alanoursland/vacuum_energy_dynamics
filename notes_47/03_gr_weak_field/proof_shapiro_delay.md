# Proof: Shapiro Time Delay

---

## What This Document Is

This is the framework's fifth derivation. It computes the Shapiro time delay — the extra round-trip time for radar signals passing near a massive body, beyond what flat-space propagation through the same coordinate distance would give. The result for the round-trip delay is $\Delta t_{\text{round-trip}} = (1 + \gamma_v)(2GM/c^3)\ln(4r_1 r_2 / b^2)$ for a signal passing at impact parameter $b$ between emitter at coordinate distance $r_1$ and reflector at coordinate distance $r_2$, with $r_1, r_2 \gg b$. The one-way delay is half this value.

With the unity assumption giving $\gamma_v = 1$, this reduces to the standard general relativity Shapiro delay formula, matching the Cassini spacecraft's 2002 solar-conjunction tracking measurement to parts in $10^5$ [Bertotti et al., 2003].

This is the framework's second derivation that uses the weak-field metric's spatial components non-trivially. The light deflection proof used the $(1 + \gamma_v)$ factor to show the framework's account of the historical factor-of-two difference between Einstein's 1911 and 1915 predictions. The Shapiro delay probes the same $(1 + \gamma_v)$ factor through a different observational channel — temporal delay rather than angular deflection — and provides an independent consistency check at higher precision than any other solar-system test.

---

## Provisional Status

This proof depends on the unity assumption from `candidate_vacuum_variation_unity.md`, which is adopted provisionally rather than derived from the framework's postulates. Specifically, the derivation below produces the parameterized result $\Delta t = (1 + \gamma_v)(2GM/c^3)\ln(4r_1 r_2 / b^2)$, and the closure to the observed value requires setting $\gamma_v = 1$ via unity.

Until the unity assumption is derived from deeper structural commitments, this proof's agreement with observation is a consistency check rather than an independent prediction. If unity is later refuted or requires modification, this derivation becomes invalid and its result needs revisiting.

Any future result that builds on this proof — or on any component of the weak-field metric with unity adopted — inherits the same provisional status.

---

## The Setup

Consider a radar signal emitted from a location at coordinate distance $r_1$ from a central mass $M$, traveling past the mass at impact parameter $b$, reflecting off a target at coordinate distance $r_2$ on the other side, and returning to the emitter. The question is: how much longer does this round trip take than it would in flat space?

The framework's weak-field metric with unity is:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

where $\Phi = -GM/r$ is the Newtonian potential. A radio signal is a null geodesic in this metric: $ds^2 = 0$ along its path.

---

## The Derivation

From the null condition on the weak-field metric, the coordinate speed of light along the signal's path is (to first order in $\Phi/c^2$):

$$\frac{dl}{dt} = c\left(1 + (1 + \gamma_v)\frac{\Phi}{c^2}\right)$$

where $l$ is the coordinate distance along the signal's path. With $\Phi < 0$ near the mass, the coordinate speed is less than $c$ — signals take longer to traverse a given coordinate distance than they would in flat space.

The coordinate-time duration for the signal to traverse an infinitesimal coordinate distance $dl$ is:

$$dt = \frac{dl}{c} \left(1 - (1 + \gamma_v)\frac{\Phi}{c^2}\right)$$

to first order. The first term gives the flat-space propagation time; the second term is the Shapiro correction.

For the one-way trip from emitter to reflector, the total time is:

$$t = \int \frac{dl}{c} - \frac{(1 + \gamma_v)}{c^3} \int \Phi \, dl$$

The second integral is the delay beyond flat-space propagation. With the mass at the origin and the signal passing at impact parameter $b$ along a straight line parameterized by $l$, the distance from the mass at position $l$ is $r(l) = \sqrt{l^2 + b^2}$, so $\Phi(l) = -GM/\sqrt{l^2 + b^2}$.

Integrating from the emitter to the reflector along the unperturbed straight-line path, with $l$ ranging over the line coordinate (approximating the line endpoints by $-r_1$ and $+r_2$ in the $r_1, r_2 \gg b$ limit, where the exact endpoint coordinates are $\pm\sqrt{r_{1,2}^2 - b^2}$):

$$\int_{-r_1}^{+r_2} \Phi \, dl = -GM \int_{-r_1}^{+r_2} \frac{dl}{\sqrt{l^2 + b^2}} = -GM \ln\left(\frac{r_2 + \sqrt{r_2^2 + b^2}}{-r_1 + \sqrt{r_1^2 + b^2}}\right)$$

For $r_1, r_2 \gg b$, this approximates to:

$$\int_{-r_1}^{+r_2} \Phi \, dl \approx -GM \ln\left(\frac{2 r_2}{b^2 / (2 r_1)}\right) = -GM \ln\left(\frac{4 r_1 r_2}{b^2}\right)$$

The one-way delay is therefore:

$$\Delta t_{\text{one-way}} = \frac{(1 + \gamma_v) GM}{c^3} \ln\left(\frac{4 r_1 r_2}{b^2}\right)$$

For a round-trip signal (emitter to reflector and back), the delay doubles:

$$\Delta t_{\text{round-trip}} = \frac{2 (1 + \gamma_v) GM}{c^3} \ln\left(\frac{4 r_1 r_2}{b^2}\right)$$

With $\gamma_v = 1$ from the unity assumption:

$$\Delta t_{\text{round-trip}} = \frac{4 GM}{c^3} \ln\left(\frac{4 r_1 r_2}{b^2}\right)$$

This is the standard general relativity Shapiro delay formula.

For a radar signal bouncing off a target behind the Sun with $r_1 = r_2 \approx 1$ AU and $b \approx R_\odot$, this gives a round-trip delay of approximately 240 microseconds — small but precisely measurable with modern timing equipment.

---

## Framework-Native Interpretation

The $(1 + \gamma_v)$ factor in the Shapiro delay decomposes in the same way as in the light deflection proof, but through the temporal channel rather than the angular channel.

The $g_{00}$ contribution: coordinate time runs slower near the mass from the external observer's perspective. A signal traversing the region near the mass takes longer in coordinate time for a given local proper-time progress, contributing half the delay.

The $g_{ij}$ contribution: proper spatial distance near the mass is longer than coordinate distance. A signal covering a given coordinate distance near the mass is actually traversing more proper distance, contributing the other half of the delay.

Both contributions arise from the same underlying fact — vacuum-per-coordinate-span variation in the region near the mass — and the unity assumption commits to them being equal in magnitude, giving the factor of two.

As in the light deflection proof, the metric description of the signal's path is a mathematical aggregation of the active-exchange account of photon behavior from the gravitational redshift proof. The signal's extra coordinate-time duration is what the framework interprets accumulated vacuum exchange as producing along the path, though the exact equivalence between the metric calculation and a local vacuum-exchange force law has not been independently derived.

Relative to the light deflection proof, the Shapiro delay is the same physics observed through a different channel. Light deflection is the integrated transverse gradient of the effective optical potential. Shapiro delay is the integrated path-length correction. Both are integrals of $(1 + \gamma_v)\Phi/c^2$ along the signal's path, weighted differently to produce different observables.

---

## Observational Tests

Shapiro predicted the effect in 1964 as a new test of general relativity [Shapiro, 1964]. The prediction is specific: for a radar signal reflecting off a target on the far side of the Sun, the round-trip delay near solar conjunction should be larger than the flat-space prediction by a logarithmic term depending on the geometry.

Early tests used planetary radar bouncing signals off Mercury and Venus during solar conjunctions, confirming the effect at 20% precision. The Viking spacecraft lander on Mars (1976-1978) provided an improved test using radar tracking of the lander's position over several years, confirming the Shapiro delay at 0.1% precision [Reasenberg et al., 1979].

The most precise test to date is the Cassini spacecraft's 2002 solar-conjunction tracking. As Cassini passed behind the Sun during its transit to Saturn, radio signals between the spacecraft and Earth passed through the Sun's gravitational field at a range of impact parameters. Measuring the resulting delay pattern gave $\gamma = 1 + (2.1 \pm 2.3) \times 10^{-5}$ [Bertotti et al., 2003], constraining $\gamma_v = 1$ to approximately two parts in $10^5$. This remains the tightest solar-system constraint on any parameter of gravity.

The framework reproduces all of these results through its weak-field metric with unity.

---

## Scope and Limitations

The derivation is valid in the weak-field limit, where $GM/rc^2 \ll 1$ along the signal's entire path. This covers all performed tests of the Shapiro delay.

For strong gravitational fields — signals passing near compact objects, or near-horizon propagation — the weak-field derivation does not apply. The framework would need a strong-field treatment, which depends on deriving the $\rho_v$ profile around a mass beyond the weak-field limit. This is currently open.

The derivation also assumes the signal's path is well-approximated by a straight line in the unperturbed geometry. For signals passing very close to the mass, where the light-deflection angle becomes comparable to the geometric angles involved, both the bending and the delay need to be computed together rather than separately. The present calculation is accurate for the solar-system regime where deflections are small.

---

## Dependency Structure

This proof inherits the dependencies of the weak-field metric proof: Postulates 1 and 2, mass-energy equivalence, the identity postulate, the curvature-as-spatial-volume-differential consequence, the redshift proof, the time dilation proof, and special relativity. It additionally depends on the unity assumption from `candidate_vacuum_variation_unity.md`, which closes the metric at $\gamma_v = 1$.

The derivation does not invoke Postulates 4 or 5. Like the other proofs in this subframework, it is insulated from the framework's configuration-energy and minimum-energy-dynamics machinery.

Because the derivation depends on unity, it inherits unity's provisional status. If unity is later derived from deeper structure, this proof's status becomes unconditional. If unity is refuted, this proof becomes invalid.

---

## What This Proof Accomplishes

As a derivation, the proof reproduces the standard weak-field Shapiro delay formula from the framework's weak-field metric with unity adopted. This adds a third quantitative weak-field contact point to the framework, joining redshift/time dilation and light deflection. Separately, the framework has qualitative contact with gravitational-wave existence and energy transport.

As a demonstration, the proof is the framework's second application of the weak-field metric machinery beyond the time-mapping regime. Together with the light deflection proof, it establishes that the framework's spatial-metric content — the unity assumption's contribution through the $(1 + \gamma_v)$ factor — reproduces observations through multiple independent observational channels.

As a consistency check, the proof confirms that the framework's machinery, given unity, matches the most precise solar-system test of gravity currently available. The Cassini measurement pins $\gamma_v = 1$ to parts in $10^5$; the framework's reproduction of this result is a tight check that the machinery works as intended, but not an independent test of unity itself, since unity was adopted in part because observation requires $\gamma_v = 1$.

The derivation does not show the framework is superior to GR. It shows that the framework, with unity adopted, reproduces GR's Shapiro delay through vacuum-exchange machinery and gives a framework-native physical account of what is happening. Whether that account is correct — whether vacuum-per-coordinate-span variation is literally what produces the signal delay — remains open to further work.

### Summary of Result

Current framework result:

$$\Delta t_{\text{round-trip}} = \frac{2 (1 + \gamma_v) GM}{c^3} \ln\left(\frac{4 r_1 r_2}{b^2}\right)$$

With unity adopted ($\gamma_v = 1$):

$$\Delta t_{\text{round-trip}} = \frac{4 GM}{c^3} \ln\left(\frac{4 r_1 r_2}{b^2}\right)$$

For a signal bouncing off a target behind the Sun: approximately 240 microseconds.

Observational status: matches the Shapiro predictions confirmed by planetary radar, Viking, and Cassini measurements, most tightly by Cassini at parts in $10^5$.

Dependency status: inherits the weak-field metric proof's dependencies plus the unity assumption. Provisional until unity is derived or refuted.

---

## References

Bertotti, B., Iess, L., & Tortora, P. (2003). A test of general relativity using radio links with the Cassini spacecraft. *Nature*, 425(6956), 374–376.

Reasenberg, R. D., Shapiro, I. I., MacNeil, P. E., Goldstein, R. B., Breidenthal, J. C., Brenkle, J. P., Cain, D. L., Kaufman, T. M., Komarek, T. A., & Zygielbaum, A. I. (1979). Viking relativity experiment: Verification of signal retardation by solar gravity. *The Astrophysical Journal Letters*, 234, L219–L221.

Shapiro, I. I. (1964). Fourth test of general relativity. *Physical Review Letters*, 13(26), 789–791.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.