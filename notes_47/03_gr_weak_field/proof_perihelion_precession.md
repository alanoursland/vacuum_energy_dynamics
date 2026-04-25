# Proof: Perihelion Precession

---

## What This Document Is

This is the framework's seventh derivation. It computes the anomalous perihelion precession of a bound orbit around a static mass, recovering Mercury's observed advance of approximately 43 arcseconds per century beyond Newtonian predictions. The result per orbit is:

$$\Delta\varpi = \frac{6\pi GM}{a(1-e^2)c^2}$$

where $a$ is the orbit's semi-major axis and $e$ is its eccentricity, matching the standard general relativity prediction and the observed Mercury anomaly.

Perihelion precession is the framework's first derivation of a *bound orbital* effect. The four prior precision-test derivations (redshift, time dilation, light deflection, Shapiro delay) all involved either clock comparisons or signal propagation between two locations. Perihelion precession instead probes the structure of repeated orbital motion: the angle by which a closed Keplerian ellipse fails to close in successive cycles. This makes it a genuinely new kind of contact point with observation — and historically it is the first test that convinced Einstein his theory was right, predating the 1919 light-deflection observation by four years.

---

## Provisional Status

The derivation depends on two pieces of provisional structure, each tracked by its own candidate document.

The first is the unity assumption from `candidate_vacuum_variation_unity.md`, which closes the weak-field metric at $\gamma_v = 1$. This contributes the spatial-mapping content of the precession.

The second is the second-order time-metric identification from `candidate_second_order_time_metric_from_redshift.md`, which closes $\beta = 1$ via the framework's redshift exponential extended to spherically symmetric potentials. This contributes the second-order time-mapping content.

Both candidates state their provisional status, argue for their plausibility, and identify what would be needed to derive them rigorously. Until both are derived, this proof's agreement with observation is a consistency check rather than an independent prediction. If either is later refuted or modified, this derivation becomes invalid and its result needs revisiting.

This proof carries a heavier provisional load than the earlier weak-field proofs (light deflection, Shapiro delay), which depended only on unity. Perihelion precession reaches into second-order metric structure, which the framework has not formally derived. The dependency on two provisional candidates is honestly tracked here so future work can know exactly what is at stake if either fails.

---

## The Setup

Consider a test body of mass $m$ in a bound orbit around a static central mass $M$, with $m \ll M$ so that the central mass is approximately fixed at the origin. The framework's weak-field metric with unity applies, and the derivation works in the quasi-Newtonian regime where the orbital velocity is non-relativistic ($v \ll c$) but next-to-leading-order corrections are kept.

The metric components (with both provisional commitments adopted, and to the order needed for perihelion precession):

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2} + 2\frac{\Phi^2}{c^4}\right)$$

$$g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right)\delta_{ij}$$

where $\Phi = -GM/r$ is the Newtonian potential. The $g_{00}$ second-order term comes from the framework's redshift exponential under the second-order time-metric identification (corresponding to PPN $\beta = 1$). The $g_{ij}$ form comes from the weak-field metric proof with unity adopted.

The body follows a timelike geodesic in this metric, per the equations-of-motion proof. The geodesic equation for a bound orbit has two conserved quantities arising from the metric's symmetries: the orbital energy $E$ (from time-translation invariance) and the angular momentum $L$ (from rotational invariance about the orbital axis).

---

## The Radial Equation and the Newtonian Limit

For an orbit confined to a plane, the geodesic equation can be reduced to an effective one-dimensional radial equation. Using the standard substitution $u = 1/r$ and parameterizing by the orbital angle $\varphi$, the orbit equation in the weak-field metric — expanded to first post-Newtonian order with $\gamma_v = \beta = 1$ — takes the form:

$$\frac{d^2u}{d\varphi^2} + u = \frac{GM}{h^2} + \frac{3GM}{c^2}u^2$$

where $h$ is the orbital specific angular momentum (angular momentum per unit mass). This is the standard post-Newtonian orbit equation for a test body in a Schwarzschild-like geometry, and the framework's weak-field metric with both provisional commitments adopted reproduces it.

The Newtonian limit drops the second term on the right-hand side. The remaining equation,

$$\frac{d^2u}{d\varphi^2} + u = \frac{GM}{h^2}$$

has solution $u_0 = (GM/h^2)(1 + e\cos\varphi)$, which is Kepler's closed ellipse. The orbit returns to its starting orientation after each cycle. This is the framework's leading-order recovery of Newtonian orbital mechanics, consistent with the equations-of-motion proof's Newtonian-limit result.

---

## The Relativistic Correction

The full equation includes the additional term $3GM/c^2 \cdot u^2$, which is the next-to-leading-order correction. This term breaks the Newtonian closure and produces perihelion precession.

To handle the correction, treat it as a perturbation on the Newtonian orbit. Writing $u = u_0 + u_1$ where $u_0$ is the Newtonian solution and $u_1$ is small, and substituting into the equation, the correction satisfies (to first order in the perturbation):

$$\frac{d^2 u_1}{d\varphi^2} + u_1 = \frac{3GM}{c^2}u_0^2$$

The right-hand side, when $u_0 = (GM/h^2)(1 + e\cos\varphi)$, contains a constant piece, a $\cos\varphi$ piece, and a $\cos^2\varphi$ piece. The $\cos\varphi$ piece is at the resonant frequency of the equation's left-hand side and produces a secular term — a contribution that grows linearly with $\varphi$ rather than oscillating.

The secular term shifts the orbit's effective period in $\varphi$ slightly away from $2\pi$, so that successive perihelia occur at slightly increasing angles. Working through the standard calculation, the perihelion advances per orbit by:

$$\Delta\varpi_{\text{per orbit}} = \frac{6\pi GM}{a(1-e^2)c^2}$$

where $a = h^2/[GM(1-e^2)]$ is the semi-major axis. This is the standard general relativity result for perihelion precession.

For Mercury, with $a \approx 5.79 \times 10^{10}$ m, $e \approx 0.206$, and $M = M_\odot$, this gives approximately 0.103 arcseconds per orbit. With Mercury's orbital period of about 88 days, this accumulates to approximately 43 arcseconds per century — matching the long-observed anomaly that pre-relativistic theories could not explain.

---

## The PPN Decomposition and the Two Provisional Inputs

The result can be made dependency-transparent by writing it in PPN form. The general post-Newtonian expression for perihelion precession around a spherically symmetric mass is:

$$\Delta\varpi_{\text{per orbit}} = \frac{6\pi GM}{a(1-e^2)c^2} \cdot \frac{2 + 2\gamma - \beta}{3}$$

where $\gamma$ is the spatial-curvature parameter and $\beta$ is the time-component nonlinearity parameter. In general relativity, $\gamma = \beta = 1$, and the prefactor $(2 + 2\gamma - \beta)/3 = 1$, giving the result above.

The framework's content gives both parameters via its provisional commitments:

The unity assumption (`candidate_vacuum_variation_unity.md`) closes $\gamma_v = 1$, providing the framework's $\gamma$.

The second-order time-metric identification (`candidate_second_order_time_metric_from_redshift.md`) closes $\beta = 1$ via the redshift exponential extended to spherically symmetric potentials.

With both provisional commitments adopted, the framework's PPN-form precession matches GR exactly, giving the $6\pi GM/[a(1-e^2)c^2]$ result and Mercury's observed 43 arcseconds per century.

If either parameter departed from 1, the precession would change measurably. Specifically, if $\gamma_v$ deviates from 1 by $\Delta\gamma$ or $\beta$ deviates from 1 by $\Delta\beta$, the precession changes by a factor $(2 + 2\Delta\gamma - \Delta\beta)/3$, which is tightly constrained by solar-system ephemerides. Mercury's observed precession therefore tests both provisional commitments simultaneously through a single observable.

---

## Framework-Native Interpretation

Closed Keplerian orbits in Newtonian gravity are a special and somewhat surprising feature. Most central force laws produce orbits that don't close — that is, the body doesn't return to the same point in space after each radial cycle. The $1/r$ potential is one of the few exceptions, due to a coincidence between the angular and radial frequencies that makes successive cycles align exactly.

This closure is a special property of the Newtonian limit, not a general feature of central-force motion. Any perturbation to the force law away from $1/r$, or any deviation of the spatial geometry from flat Euclidean, breaks the closure.

In the framework, the geometry near a mass is not exactly Euclidean. The spatial-mapping content of the metric ($g_{ij}$ at first order, depending on unity) means that proper radial distance and proper angular distance scale slightly differently from coordinate distances. This deviation from Euclidean spatial structure is one source of the perihelion precession.

The other source is the relativistic correction to the time-mapping. Coordinates near the mass have proper-time-to-coordinate-time mapping that is non-trivial at second order in $\Phi/c^2$, contributing to the orbit's effective dynamics in a way that further breaks Newtonian closure.

In framework-native terms: orbits don't close because the vacuum-extent variation around the mass is not flat. The body nearly returns to its starting orientation after each orbit, but each radial cycle covers slightly more angular extent than $2\pi$ (because the spatial mapping isn't Euclidean and the time mapping isn't Newtonian), so the perihelion advances. Mercury's observed precession is a measurement of this non-flatness in the vacuum geometry around the Sun.

This connects to the active-exchange picture in the same way as the previous bound-system content. The body in orbit is continuously consuming and regenerating vacuum as it moves through the gradient — descending toward perihelion (consuming, gaining kinetic energy), receding toward aphelion (regenerating, losing kinetic energy). The orbit's trajectory is the timelike geodesic that aggregates this exchange. The metric calculation aggregates this into a trajectory whose closure is broken by the spatial-mapping and time-mapping content of the metric.

---

## Mercury Specifically

The general result $\Delta\varpi = 6\pi GM/a(1-e^2)c^2$ per orbit gives Mercury's specific precession when its orbital parameters are inserted.

Mercury's semi-major axis: $a \approx 5.791 \times 10^{10}$ m.

Mercury's eccentricity: $e \approx 0.2056$.

Solar mass: $M_\odot \approx 1.989 \times 10^{30}$ kg, giving $GM_\odot/c^2 \approx 1.477$ km.

Computing $6\pi GM/a(1-e^2)c^2$:

$$\Delta\varpi_{\text{per orbit}} \approx \frac{6\pi \cdot 1.477 \times 10^3 \text{ m}}{5.791 \times 10^{10} \text{ m} \cdot (1 - 0.0423)} \approx 5.02 \times 10^{-7} \text{ rad/orbit}$$

Converting to arcseconds: $5.02 \times 10^{-7}$ rad $\times (180/\pi) \times 3600$ arcsec/deg $\approx 0.103$ arcsec/orbit.

Mercury's orbital period is about 87.97 days, giving approximately 415 orbits per century. The precession per century is therefore:

$$\Delta\varpi_{\text{per century}} \approx 0.103 \times 415 \approx 42.9 \text{ arcsec/century}$$

This matches the observed anomalous precession of approximately 43 arcseconds per century within the precision of both the calculation and the observation.

The agreement confirms that the framework's machinery — weak-field metric with unity, geodesic motion of test bodies, and the second-order $g_{00}$ content from the redshift exponential — correctly reproduces the most precisely tested anomaly in solar-system gravitation that GR was originally designed to explain.

---

## Scope and Limitations

The derivation is valid in the weak-field, slow-motion regime where $|\Phi|/c^2 \ll 1$ and $v/c \ll 1$ along the orbit. This covers Mercury and all other observed solar-system orbits.

For binary pulsar systems, where the orbital velocities can reach a few percent of $c$ and the gravitational potentials are stronger, the weak-field approximation begins to break down. The framework's perihelion-precession derivation would need extension to handle these systems, which probe gravity at higher precision than solar-system tests through the systems' decay-driven orbital evolution. This extension is open work.

For motion near compact objects (neutron stars, black holes), the strong-field regime applies and the derivation does not. As with previous proofs, strong-field treatment requires deriving the $\rho_v$ profile around a mass beyond the weak-field limit, which is currently open.

The derivation depends on both unity and the $\beta = 1$ identification from the redshift exponential. If either is later refuted or modified, this proof's result would change accordingly. Specifically, if $\gamma_v$ deviates from 1 by a fraction $\Delta\gamma$ or $\beta$ deviates from 1 by $\Delta\beta$, the precession changes by a factor $(2 + 2\Delta\gamma - \Delta\beta)/3$, which is tightly constrained by solar-system ephemerides.

---

## Dependency Structure

This proof inherits the dependencies of the weak-field equations-of-motion proof: Postulates 1 and 2, mass-energy equivalence, the identity postulate, the curvature-as-spatial-volume-differential consequence, the redshift proof, the time dilation proof, the weak-field metric proof, and special relativity. It additionally uses two provisional candidates: `candidate_vacuum_variation_unity.md` (closing $\gamma_v = 1$) and `candidate_second_order_time_metric_from_redshift.md` (closing $\beta = 1$ via the redshift exponential extended to spherically symmetric potentials).

The derivation does not invoke Postulates 4 or 5 directly, continuing the pattern established by the other proofs in this subframework: the framework's quantitative weak-field content is insulated from the configuration-energy and minimum-energy-dynamics machinery.

The two provisional commitments make this proof's result conditional on both being right. Refutation of either would invalidate the result. Derivation of either from deeper structure would strengthen the framework's foundation for this and related results.

---

## What This Proof Accomplishes

As a derivation, the proof reproduces the standard general relativity prediction for perihelion precession from the framework's weak-field metric machinery plus the redshift exponential extended to second order. This is the framework's first result for a bound orbital effect — distinct from the photon-based and signal-based tests of the previous four proofs.

As a closure of the traditional classical tests of weak-field gravity, the proof completes the framework's reproduction of the specific precision tests classically used to compare gravity theories: gravitational redshift, time dilation, light deflection, Shapiro delay, and now perihelion precession. Other weak-field solar-system tests (geodetic precession, frame-dragging, the Nordtvedt effect) remain available as future targets and would extend the framework's contact with observation further. All five tests derived so far come from the same core postulate base plus the unity assumption (with the $\beta = 1$ identification additionally needed for perihelion precession).

As a consistency check on unity, the proof tests the unity assumption through a fourth observational channel beyond redshift/time dilation, light deflection, and Shapiro delay. Mercury's observed precession matches the framework's prediction with $\gamma_v = 1$, providing another instance where the unity assumption produces the right answer.

As a consistency check on $\beta = 1$, the proof similarly tests the framework's redshift exponential extended to second order. Agreement with observation supports the informal $\beta = 1$ identification, though it is still informal pending a rigorous derivation of how the redshift exponential extends to spherically symmetric potentials.

The proof does not show the framework predicts anything different from GR. It shows the framework reproduces GR's precision result through framework-native machinery — geodesic motion in a metric whose components come from vacuum-extent variation around a mass — and provides a framework-native interpretation of why orbits don't close (because the vacuum geometry around a mass isn't flat).

### Summary of Result

Result per orbit:

$$\Delta\varpi = \frac{6\pi GM}{a(1-e^2)c^2}$$

For Mercury: approximately 0.103 arcseconds per orbit, accumulating to approximately 43 arcseconds per century.

Observational status: matches the long-known anomalous precession of Mercury's orbit, which was the first quantitative success of general relativity.

Dependency status: depends on unity ($\gamma_v = 1$) for the spatial-mapping content and on the framework's $\beta = 1$ identification from the redshift exponential for the second-order time-mapping content. Both are provisional pending derivation from deeper structure.

---

## References

Einstein, A. (1915). Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie [Explanation of the perihelion motion of Mercury from the general theory of relativity]. *Sitzungsberichte der Preußischen Akademie der Wissenschaften*, 831–839.

Le Verrier, U. J. J. (1859). Theorie du mouvement de Mercure. *Annales de l'Observatoire impérial de Paris*, 5.

Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman, chapter 25.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.