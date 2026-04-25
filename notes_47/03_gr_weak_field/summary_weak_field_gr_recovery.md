# Summary: Weak-Field GR Recovery

---

## What This Document Is

This document consolidates the framework's current state. It surveys what the framework has derived, what it has adopted as provisional commitments, what gaps remain, and what the natural research priorities are.

The document exists because the framework has reached a phase boundary. The classical weak-field tests of general relativity have been reproduced. The dependency structure is now complex enough that holding it all in mind from scattered proof and candidate documents is difficult. A consolidation lets future work see at a glance what the framework derives, what it provisionally assumes, and what is genuinely open.

This is a `summary_` document — a new prefix in the framework's taxonomy. Unlike postulates, proofs, candidates, and consequences (which produce or contain framework content), summary documents survey and consolidate. They are stable references that get updated as the framework develops.

---

## What the Framework Recovers

The framework currently reproduces six results that match general relativity in the weak-field regime, organized below by their dependency status.

**Foundationally robust** (depend only on the core postulates and SR):

The Newtonian limit of equations of motion, derived directly from Postulate 3 plus mass-energy equivalence: a body in a gradient experiences force $F = (E_{\text{total}}/c^2) \cdot g$, reducing to $F = mg$ and $\vec{a} = -\nabla\Phi$ in the non-relativistic limit. This depends on Postulates 2 and 3, mass-energy equivalence, and SR; no metric, no unity, no second-order time-metric needed. See `proof_weak_field_equations_of_motion.md`.

**Derived from foundations through the redshift-time-dilation chain** (depend on the core postulates plus the redshift exponential at first order):

Gravitational redshift: photons climbing a gradient lose energy through active vacuum exchange, giving $E(h) = E_0 \exp(-gh/c^2)$, which matches the Pound-Rebka result. See `proof_gravitational_redshift.md`.

Gravitational time dilation: clocks in gravitational wells run slower than clocks at higher potential, by a factor inherited from the redshift formula. Matches GPS timing, Hafele-Keating, and optical-clock comparisons. See `proof_gravitational_time_dilation.md`.

Weak-field $g_{00}$ at first order: $g_{00} \approx -(1 + 2\Phi/c^2)$, derived cleanly from the time dilation result in metric notation. See `proof_weak_field_metric.md`.

**Derived conditionally on unity** (depend additionally on $\gamma_v = 1$ from `candidate_vacuum_variation_unity.md`):

Light deflection: $\Delta\theta = (1+\gamma_v)(2GM/bc^2) \to 4GM/bc^2$ with unity, matching Eddington 1919 and subsequent observations. See `proof_light_deflection.md`.

Shapiro delay: $\Delta t_{\text{round-trip}} = (1+\gamma_v)(2GM/c^3)\ln(4r_1 r_2/b^2) \to$ standard GR formula with unity, matching Cassini at parts in $10^5$. See `proof_shapiro_delay.md`.

**Derived conditionally on unity plus the second-order time-metric identification** (depend additionally on $\beta = 1$ from `candidate_second_order_time_metric_from_redshift.md`):

Perihelion precession: $\Delta\varpi = (6\pi GM/[a(1-e^2)c^2]) \cdot (2 + 2\gamma_v - \beta)/3$, giving the standard GR result and Mercury's 43 arcseconds per century with $\gamma_v = \beta = 1$. See `proof_perihelion_precession.md`.

**Qualitative results** (depend on the framework's ontological commitments without quantitative observational tests yet):

Gravitational wave existence and energy transport: Postulate 5's relaxation dynamics implies that disturbed configurations propagate as waves carrying configuration energy. See `consequence_gravitational_waves.md` and `consequence_wave_matter_interaction.md`.

---

## Metric Status

The framework's weak-field metric in its current form:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2} + 2\frac{\Phi^2}{c^4}\right)$$

$$g_{ij} \approx \left(1 - 2\gamma_v \frac{\Phi}{c^2}\right)\delta_{ij}$$

The first-order $g_{00}$ term $(2\Phi/c^2)$ is foundationally derived from the redshift and time dilation proofs.

The second-order $g_{00}$ term $(2\Phi^2/c^4)$ is provisionally derived from `candidate_second_order_time_metric_from_redshift.md`, which extends the redshift exponential $E(h) = E_0\exp(-gh/c^2)$ to spherically symmetric potentials, giving $g_{00} \approx -\exp(2\Phi/c^2)$ in PPN-compatible coordinates. Expanding this to second order gives PPN $\beta = 1$.

The $g_{ij}$ form has the framework's spatial-mapping content. The coefficient $\gamma_v$ is provisional via `candidate_vacuum_variation_unity.md`, which adopts $\gamma_v = 1$ to match observation. With unity, $g_{ij} \approx (1 - 2\Phi/c^2)\delta_{ij}$, matching GR.

The framework has not derived $g_{0i}$ components, which would describe rotating sources. This is a natural extension that hasn't been pursued yet.

The framework has not addressed strong-field corrections beyond second order. The exponential form of $g_{00}$ differs from Schwarzschild beyond second order, which becomes a divergence point in the strong-field regime that hasn't been worked out.

---

## PPN Status

The Parameterized Post-Newtonian formalism describes the most general post-Newtonian metric in terms of ten parameters. Each parameter captures a specific kind of departure from general relativity. Translating the framework into PPN language gives a precise statement of what the framework predicts, parameterizes, and is silent about.

**Parameters provisionally fixed by framework candidates:**

$\gamma$ (spatial-curvature parameter): Identified with the framework's $\gamma_v$. Provisionally fixed at $\gamma = 1$ via the unity candidate. Tested by light deflection, Shapiro delay, and (with $\beta$) perihelion precession.

$\beta$ (nonlinearity parameter): Provisionally fixed at $\beta = 1$ via the second-order time-metric candidate. Tested by perihelion precession and the Nordtvedt effect.

**Parameters that should follow from existing framework commitments but have not been formally argued:**

$\alpha_3$ (preferred-frame plus conservation): The framework's commitment to local Lorentz invariance and to energy conservation through vacuum exchange should give $\alpha_3 = 0$ (the GR value). Formal derivation from the framework's postulates has not been written.

$\zeta_1, \zeta_2, \zeta_3, \zeta_4$ (conservation-law violations): The framework's energy bookkeeping (vacuum exchange conserving total energy plus mass-energy in interactions) should give these all equal to 0 (the GR values). Formal derivation has not been written.

**Parameters not addressed:**

$\xi$ (preferred-location effects): The framework's static spherically-symmetric content doesn't directly engage with whether the laws of gravity vary with location in the universe. A formal commitment requires more structural work than the framework currently has.

$\alpha_1, \alpha_2$ (preferred-frame anisotropy effects): Similar to $\alpha_3$, these should follow from local Lorentz invariance, but the formal argument hasn't been made. Solar-system tests constrain them tightly.

If all the parameters that "should follow from existing commitments" were formally derived, and the two provisional candidates were promoted to derivations, the framework would have $\gamma = \beta = 1$ derived, $\alpha_3 = \zeta_i = 0$ derived, and $\xi, \alpha_1, \alpha_2$ remaining as items needing additional structural commitments. This is a substantial future research program but a tractable one.

---

## What the Framework Has Not Recovered

This section organizes the remaining gaps by what kind of work each requires.

**Rigorous derivations of existing provisional commitments** (the highest-priority foundational work):

Derive the Equal-Response component of unity, closing $\gamma_v = 1$ from deeper structure. This would remove provisional status from light deflection, Shapiro delay, and (partially) perihelion precession. See `candidate_vacuum_variation_unity.md`'s derivation paths section for candidate approaches.

Derive the rigorous extension of the redshift exponential to spherically symmetric potentials, closing $\beta = 1$. This would remove the remaining provisional status from perihelion precession. See `candidate_second_order_time_metric_from_redshift.md`'s derivation section.

**Extensions of existing machinery** (concrete next steps within the weak-field program):

Frame dragging and the $g_{0i}$ sector for rotating sources. Required for geodetic precession and Lense-Thirring frame-dragging measurements (both confirmed by Gravity Probe B). The framework's static-spherically-symmetric machinery would need extension to rotating sources.

Nordtvedt effect / Strong Equivalence Principle behavior. Tests whether gravitational binding energy contributes to a body's gravitational mass. Constrains $\beta$ in the PPN framework and provides another test of the second-order time-metric candidate.

Geodetic precession of orbiting gyroscopes. Standard application of the geodesic equation to spinning test bodies in the weak-field metric.

Higher-order post-Newtonian content for binary systems. Required to compute orbital decay rates of binary pulsars and compare with Hulse-Taylor's precision constraints.

**New structural work** (foundational gaps that need substantial development):

Source equation for $\Phi = -GM/r$. The framework currently asserts that masses produce $1/r$ potentials but does not derive this from vacuum structure. Closing this requires deriving how a localized mass shapes the surrounding vacuum's extent profile.

Strong-field metric structure. The framework's exponential form of $g_{00}$ diverges from Schwarzschild beyond second order. Whether the exponential form is correct in the strong field, whether Schwarzschild is correct, or whether some other form emerges from the framework's structure is open.

Gravitational wave mode structure and polarizations. The framework commits to waves existing but does not specify whether they have purely tensor (GR-like) modes, scalar-tensor modes, or richer structure. This is where the framework might make a falsifiable prediction distinct from GR.

Full Einstein-equation analogue. The framework reproduces GR's predictions in the weak field but has no full source-coupled field equation that determines the metric from a stress-energy distribution. Whether the framework should have such an equation, or whether vacuum-exchange machinery replaces it, is not currently clear.

Mass formation and the deep structure of matter. The framework treats masses as constraints on vacuum without deriving how masses come to exist as such constraints. This connects to quantum content and to the early universe.

Mathematical structure of the vacuum. The framework treats the vacuum as having sufficient structure to support its postulates but does not specify whether the vacuum is fundamentally a scalar field, a tensor field, scalar-tensor, or something richer. This is the deepest open question, and resolving it would close several of the items above.

**Deferred** (questions held as future work without active development):

Cosmological dynamics beyond the existing consequence document. The framework's cosmic expansion content sketches a picture but doesn't quantitatively engage with current observational cosmology (dark energy, dark matter, inflation, large-scale structure formation).

Quantum content and connection to quantum field theory. The framework is currently a classical-level theory of gravity. Connection to quantum mechanics and to QFT-style vacuum content is deferred.

Casimir-effect-style direct vacuum manipulation. Speculative possibilities for engineering vacuum configurations directly are held but not developed.

---

## Research Priority Ranking

Based on which gaps are most foundational and most reachable from the framework's current state:

**Tier 1 — Close existing provisional commitments.**

1. Derive Equal-Response of unity (closes $\gamma_v = 1$).
2. Formalize the redshift exponential extension (closes $\beta = 1$).

These are the highest-priority because they remove provisional status from existing results rather than adding new ones. They sharpen what the framework has rather than extending what it covers. Each is potentially within reach with careful work on the framework's existing content.

**Tier 2 — Extend existing machinery to additional weak-field tests.**

3. Frame dragging and $g_{0i}$ sector. Brings the framework into contact with Gravity Probe B and pulsar timing.
4. Geodetic precession. Standard application of existing geodesic machinery.
5. Nordtvedt / SEP. Tests $\beta$ through a new observational channel.

These are concrete next applications of the framework's machinery that don't require new structural commitments.

**Tier 3 — Develop foundational structure.**

6. Source equation for $\Phi$. Closes the loop on weak-field gravity.
7. Wave mode structure. Where the framework might predict something distinct from GR.
8. Mathematical structure of the vacuum. Deepest foundational question.

These require substantial new development. The vacuum's mathematical structure is probably the most important because resolving it would likely close several other items, but it's also the hardest.

**Tier 4 — Strong-field and exotic territory.**

9. Strong-field metric structure.
10. Black hole interiors and singularity question.
11. Cosmological dynamics in detail.
12. Quantum content.
13. Direct vacuum manipulation (Casimir-style).

These are downstream of the foundational work. Pursuing them now without the foundations would mostly produce speculation without enough machinery to constrain it.

---

## Summary

**Six precision-test results reproduced**, drawn from the framework's postulate base plus two provisional candidate commitments:

| Result | Foundationally robust | Conditional on unity | Conditional on second-order time-metric |
|--------|-----------------------|----------------------|------------------------------------------|
| Newtonian motion | ✓ | | |
| Redshift / time dilation | ✓ | | |
| Light deflection | | ✓ | |
| Shapiro delay | | ✓ | |
| Perihelion precession | | ✓ | ✓ |

**Two provisional candidates** track the load-bearing commitments:

| Candidate | What it closes | Status |
|-----------|----------------|--------|
| `candidate_vacuum_variation_unity.md` | $\gamma_v = 1$ | Adopted; not derived |
| `candidate_second_order_time_metric_from_redshift.md` | $\beta = 1$ | Adopted; informal extension |

**Highest-priority next work**: Derive the Equal-Response component of unity, then formalize the second-order time-metric extension. Both close existing provisional commitments and would substantially strengthen the framework's foundations.

The framework's current position is a real milestone. The classical tests of weak-field gravity have been reproduced from a compact postulate base plus two clearly tracked provisional commitments. The dependency structure is clean. The next research program is well-defined. The framework is ready for the next phase of work, whether that is closing the existing provisional commitments or extending into the open territory beyond.
