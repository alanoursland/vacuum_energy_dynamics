# Proof: Weak-Field Equations of Motion

---

## What This Document Is

This is the framework's sixth derivation. It establishes how massive test bodies move in the framework's weak-field gravitational regime, deriving the equations of motion through two complementary routes that should and do agree at leading order.

The first route works directly from Postulate 2 plus mass-energy equivalence: gravitational force per unit energy acting on a body's total energy gives a force law that reduces to Newton's $\vec{a} = -\nabla\Phi$ in the non-relativistic limit.

The second route works from the timelike geodesic equation in the weak-field metric (with unity adopted): the trajectory of a free-falling massive test body is the geodesic, and expansion of the geodesic equation at leading order in $v/c$ and $\Phi/c^2$ recovers the same Newtonian result.

Both routes recover Newton, by construction the same physics. The two-route structure provides an internal consistency check on the framework's machinery and exposes what each route can say that the other cannot. Direct-from-Postulate-2 stays close to the vacuum-exchange ontology and works in the non-relativistic limit. The geodesic route uses the metric machinery and extends naturally to relativistic speeds and post-Newtonian corrections, where bound-system effects like perihelion precession live.

This document closes the weak-field version of one of the framework's stated open-work items (equations of motion for test bodies in a curvature gradient) and unlocks downstream proofs that depend on having timelike trajectories worked out. It does not close the deeper open question of deriving the source gradient $\Phi = -GM/r$ from the vacuum's structure, which remains separate.

---

## Provisional Status

The geodesic-route derivation depends on the weak-field metric proof, which inherits the provisional status of the unity assumption from `candidate_vacuum_variation_unity.md`. Specifically, the metric components $g_{00}$ and $g_{ij}$ together produce specific post-Newtonian corrections, and the relationship between the two depends on $\gamma_v = 1$ via unity.

The Postulate-2-route derivation does not depend on unity. Its content is the leading-order Newtonian limit, which falls out of Postulate 2 plus mass-energy equivalence directly without invoking the metric's spatial components.

The Newtonian limit itself is therefore on firmer foundational ground than the post-Newtonian corrections. If unity were refuted, the Newtonian-limit content of this document would survive; the post-Newtonian corrections derived through the geodesic route would need revisiting.

---

## Route 1: From Postulate 2 to Newton

Postulate 2 commits the framework to a force on every quantum of energy in a curvature gradient, applied uniformly per unit energy. By Postulate 3, the relevant energy for a massive body is its total energy, $E_{\text{total}} = mc^2 + \text{kinetic terms}$.

For a body in a weak gradient with local strength $g$, the gravitational force is:

$$F = \frac{E_{\text{total}}}{c^2} \cdot g$$

In the non-relativistic limit, $E_{\text{total}} \approx mc^2$ to leading order, and the kinetic terms are higher-order in $v/c$. Substituting:

$$F \approx \frac{mc^2}{c^2} \cdot g = mg$$

This is the Newtonian force law for gravity. Acceleration is $a = F/m = g$, which depends only on the gradient strength and not on the body's mass — the equivalence principle.

For a static spherically symmetric mass $M$ producing the gradient, the framework's weak-field machinery gives $g = -\nabla\Phi$ with $\Phi = -GM/r$ as the Newtonian potential. The acceleration of the test body is therefore:

$$\vec{a} = -\nabla\Phi = -\frac{GM}{r^2}\hat{r}$$

This is Newton's law of gravitation, recovered at leading order from Postulate 2 plus mass-energy equivalence.

The derivation does not invoke the weak-field metric or the unity assumption. It is foundationally independent of those structures, depending only on the framework's core postulates plus special relativity.

---

## Route 2: From the Geodesic Equation

A free-falling test body in the framework's weak-field metric follows a timelike geodesic. The geodesic equation extremizes the proper time $\tau$ along the body's worldline, given the metric components $g_{\mu\nu}$.

In the weak-field metric with unity adopted:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

The geodesic equation in standard form is:

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0$$

where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols of the metric.

For a body moving slowly ($v \ll c$) and in a weak field ($|\Phi|/c^2 \ll 1$), the proper time $\tau$ approximates coordinate time $t$ at leading order, and the only Christoffel symbol contributing at leading order is $\Gamma^i_{00}$. Because the metric is static, $\partial_0 g_{\mu\nu} = 0$. The standard expression for this Christoffel component is:

$$\Gamma^i_{00} = -\frac{1}{2} g^{ij} \partial_j g_{00}$$

To leading order, $g^{ij} \approx \delta^{ij}$ and $\partial_j g_{00} = -\frac{2}{c^2} \partial_j \Phi$, giving:

$$\Gamma^i_{00} \approx \frac{1}{c^2} \partial_i \Phi$$

The spatial components of the geodesic equation become:

$$\frac{d^2 x^i}{dt^2} + c^2 \Gamma^i_{00} \approx 0$$

which gives:

$$\frac{d^2 x^i}{dt^2} = -\partial_i \Phi$$

or in vector form:

$$\vec{a} = -\nabla\Phi$$

Newton's law, recovered through the geodesic route.

Note that at this leading order, only $g_{00}$ contributes — the spatial components of the metric do not enter the Newtonian limit. This matches the Postulate-2 derivation, which also produced Newton from the time-mapping content alone.

---

## Where the Two Routes Agree and Diverge

Both routes produce the Newtonian limit. They agree because they describe the same physics: gravitational interaction acting on a massive body in a weak field.

Where they diverge in content is at higher orders.

The Postulate-2 route suggests that the gravitational coupling is to total energy, not rest energy alone. This means the framework predicts that a fast-moving body's coupling to gravity exceeds what its rest mass alone would suggest. A fully relativistic treatment of the resulting motion should be handled through the metric/geodesic route or a relativistic reformulation of the exchange law, rather than by extrapolating the non-relativistic force law $F = mg$ to high speeds. The Postulate-2 route in its non-relativistic form is foundationally robust; its extension to relativistic speeds is more delicate and is best done through the geodesic machinery.

The geodesic route extends naturally to next-to-leading order in $v/c$ and $\Phi/c^2$, where the spatial components $g_{ij}$ start contributing through the geodesic's full content. This is where post-Newtonian corrections live, including:

- Relativistic corrections to bound orbital motion
- Non-closure of Keplerian ellipses, producing the perihelion precession effect
- Time-dilation effects on orbital periods
- Frame-dragging-adjacent effects in higher-order treatment

The geodesic route is the natural framework for computing these corrections. Specific applications (perihelion precession, geodetic precession) follow as standard expansions of the geodesic equation in the weak-field metric and become candidates for subsequent derivations.

---

## Framework-Native Interpretation

In the framework's vocabulary, the equation of motion describes how vacuum exchange shapes the trajectory of a massive body.

A body descending through a gradient consumes vacuum (Postulate 2), and the consumed vacuum's energy becomes kinetic energy of the body. The body's rest mass-energy is conserved through the trajectory; what changes is the kinetic component of its total energy. The trajectory is the path along which this consumption-and-gain proceeds.

For a free-falling body — geodesic motion — the consumption is matched smoothly by the relaxation of the surrounding configuration (per Postulate 5: the vacuum's minimum-energy configuration tracks the moving constraint). The body and its surrounding configuration evolve together, with the body's trajectory being whatever path corresponds to smooth consumption everywhere along it. An ideal test body following a geodesic in a fixed external field does not radiate by itself. Radiation arises from time-changing source configurations — binaries, accelerated multi-body systems, asymmetric mass distributions — not from the mere fact of free fall along a geodesic.

For a non-geodesic trajectory — a body held in place against gravity, or accelerated by a non-gravitational force — the consumption is mismatched with the configuration's relaxation. The mismatch shows up as deviation from the natural trajectory and can produce a radiative loss to gravitational waves in the case of accelerated motion. This is the same mismatch principle that produces wave radiation in Postulate 5's account.

The geodesic equation is the metric-level aggregation of this consumption-and-relaxation dynamics. In the same way that the photon's null geodesic in the light deflection proof aggregates active vacuum exchange into a metric trajectory, the massive body's timelike geodesic aggregates vacuum exchange between the body and the surrounding configuration into a trajectory in the metric.

The exact equivalence between the metric calculation and a local vacuum-exchange account of the body's motion has not been independently derived. The framework expects them to agree (and at leading order they do, by both routes producing Newton's law), but the equivalence is consistency the framework expects rather than a result it has independently proved.

---

## The Equivalence Principle

The equivalence principle — that all bodies fall at the same rate in a gravitational field, regardless of mass or composition — emerges from both routes.

In the Postulate-2 route, force per unit energy times total energy gives force proportional to mass (in the non-relativistic limit), and acceleration is force divided by mass, which gives acceleration independent of mass.

In the geodesic route, the geodesic equation is independent of the test body's mass by construction — the trajectory depends on the metric and the initial conditions, not on the mass of the body following the trajectory.

These two formulations of the equivalence principle agree because they describe the same physics. The framework's universality clause in Postulate 2 (force acts uniformly per unit energy) is the equivalence principle in vacuum-exchange terms. The geodesic-equation formulation is the equivalence principle in metric terms. The framework gives both naturally.

This consistency is a useful check. A framework that produced the Newtonian limit by one route but failed the equivalence principle by another would have hidden tensions. The framework's two routes both producing Newton plus the equivalence principle indicates the postulates are working consistently.

---

## Scope and Limitations

The derivation is valid in the weak-field limit, where $|\Phi|/c^2 \ll 1$ along the body's trajectory. This covers all observed gravitational dynamics in the solar system and most astrophysical regimes outside compact objects.

For strong fields — orbital motion near compact objects, near-horizon trajectories, motion through regions where the field is comparable to $c^2$ — the weak-field derivation does not apply. The framework would need a strong-field treatment, which depends on deriving the $\rho_v$ profile around a mass beyond the weak-field limit. This is currently open.

The Newtonian limit recovered by both routes is foundationally robust within the framework. The post-Newtonian corrections derived through the geodesic route are conditional on the weak-field metric structure, which depends on unity. Future work computing specific corrections (perihelion precession, geodetic precession) will inherit unity's provisional status.

---

## Dependency Structure

The Postulate-2 route depends on Postulates 1, 2, and 3 plus special relativity, treating the gradient strength $g$ as a given observable. It does not require the identity postulate, the curvature consequence, the weak-field metric, or unity once $g$ is treated as given. The Newtonian limit derived through this route is the most foundationally robust quantitative prediction in the framework.

The geodesic route depends additionally on the identity postulate, the curvature-as-spatial-volume-differential consequence, the redshift proof, the time dilation proof, the weak-field metric proof, and the unity assumption. The same chain of dependencies as the light deflection and Shapiro delay proofs.

Neither route invokes Postulates 4 or 5 directly. Both are insulated from the framework's configuration-energy and minimum-energy-dynamics machinery, in the sense that the equations of motion can be derived without those postulates. (Postulate 5 contributes to the framework-native interpretation — explaining why geodesic motion is the natural trajectory through the smooth-tracking-of-constraint argument — but the formal derivation does not require it.)

This split dependency structure has a useful property: the leading-order Newtonian content of the framework is independent of unity, while the post-Newtonian content depends on it. Anyone evaluating the framework can accept the Newtonian content without accepting the unity assumption, and the framework's claim to reproduce Newtonian gravity does not rest on a provisional commitment.

---

## What This Proof Accomplishes

As a derivation, the proof recovers Newton's law of gravitation through two routes that depend on different parts of the framework. The first route depends only on Postulates 1-3 plus SR; the second depends on the full weak-field metric machinery plus unity. Both produce $\vec{a} = -\nabla\Phi$ as the leading-order equation of motion.

As a closure of an open question, the proof addresses the weak-field version of one of the framework's stated open-work items: equations of motion for test bodies in a curvature gradient. The framework now has a derived equation of motion in the weak-field regime, which removes a load-bearing gap in the framework's coverage of bound-system dynamics. The deeper open question of deriving the source gradient $\Phi = -GM/r$ from the vacuum's structure remains separate.

As a setup for downstream work, the proof unlocks subsequent derivations that depend on having timelike trajectories worked out. Perihelion precession is the most direct application — it falls out of the geodesic equation at next-to-leading order — and other classical tests of GR involving bound orbital motion become accessible through the same machinery.

As a consistency check, the proof confirms that the framework's two main approaches to gravitational dynamics (direct from Postulate 2, and via the metric+geodesic) agree at leading order. This is non-trivial: a framework that produced different answers via different routes would have hidden inconsistencies. The agreement here indicates the framework's structural commitments are working together rather than against each other.

The derivation does not show the framework predicts anything different from GR or Newton. It shows the framework reproduces the standard results through framework-native machinery and provides an interpretation of the equations of motion grounded in vacuum exchange. The framework's distinctive content lives in the interpretation rather than in numerical predictions, at this stage of development.

### Summary of Result

Newtonian limit from Postulate 2 (foundationally robust, no unity dependency):

$$F = \frac{E_{\text{total}}}{c^2} \cdot g \approx mg \quad \text{in the non-relativistic limit}$$

$$\vec{a} = -\nabla\Phi$$

Geodesic equation in the weak-field metric (with unity adopted):

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0$$

Newtonian limit (leading order in $v/c$ and $\Phi/c^2$): $\vec{a} = -\nabla\Phi$, agreeing with the Postulate-2 route.

Post-Newtonian corrections: live at next-to-leading order in the geodesic equation, with $g_{ij}$ contributing. Specific applications (perihelion precession, geodetic precession) become accessible as standard expansions, inheriting unity's provisional status through the metric.

---

## References

Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman, chapters 8 and 13.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.