# Proof: Weak-Field Metric

---

## What This Document Is

This is the framework's third derivation. It reconstructs the weak-field metric — the mathematical object general relativity uses to describe spacetime geometry around a mass in the limit where gravitational effects are small — from the framework's existing postulates, without importing general relativity's field equations.

The reconstruction is partial. The time component $g_{00}$ is derived cleanly from the gravitational time dilation proof, giving the standard weak-field form. The spatial components are identified as existing — the framework's spatial companion effect commits to a spatial-mapping difference between local and coordinate measurements — but their quantitative coefficient is not pinned down by the current postulates. The document introduces a parameter $\gamma_v$ to name this coefficient, notes that GR corresponds to $\gamma_v = 1$, and identifies the derivation of $\gamma_v$ as a concrete open question downstream of the mathematical structure of the vacuum.

The purpose of the document is threefold. First, it consolidates the time-mapping result from the time dilation proof into metric form, so that geodesic motion and other metric-based calculations can be performed within the framework. Second, it surfaces the spatial-mapping underdetermination explicitly, as a named parameter rather than a vague gap. Third, it establishes a methodology for using metric notation in the framework without letting GR's ontology silently replace the framework's own.

---

## The Metric Is a Derived Descriptor, Not a Primitive Field

Before the reconstruction, a methodological commitment.

In general relativity, the metric $g_{\mu\nu}$ is the primary geometric object. Matter tells the metric how to curve (through the Einstein field equations), and the metric tells matter how to move (through the geodesic equation). The metric is treated as a field with its own dynamics, and gravitational phenomena are features of the metric's variation.

The framework does not adopt this picture. Under Postulate 1, the vacuum is spacetime; there is no metric field separate from the vacuum that could have independent dynamics. What we call a metric is a mathematical descriptor of how the vacuum's configuration produces relational interval structure — how clocks at different locations map onto each other, how proper lengths map onto coordinate lengths, how light cones open, which events can causally influence which others. The metric is bookkeeping for these relations.

The ontological chain is:

> vacuum substrate → vacuum configuration → relational interval structure → $g_{\mu\nu}$

The metric appears late in this chain. It is not the substance of the framework, not the full configuration, not even a direct representation of the configuration. It is a mathematical shadow cast by the configuration onto the space of intervals between points. Different configurations of the same vacuum produce different metrics; the vacuum itself is what varies, and the metric records the relational consequences.

This matters for how we use metric notation. When the framework writes down $g_{00}$ or $g_{ij}$, it is not introducing a new substance or a new field. It is giving a mathematical form to a relation the framework has already committed to through its vacuum-configuration language. Every metric component, to be used honestly, must be introducible with its framework-native physical meaning attached. If we cannot say what vacuum-configuration fact a metric component is recording, we have not earned the right to write it down.

This rule is the operational content of keeping the framework's ledger visible while using GR's mathematical language.

---

## Two Mappings from One Underlying Fact

The framework's content about weak-field geometry, stripped to its essentials, is that vacuum-per-coordinate-span varies between locations in a gradient. This single physical fact produces two observationally distinguishable consequences.

The first is the time-mapping. Signals traverse the vacuum at local speed $c$ everywhere (Postulate 1 plus the propagation argument from the gravitational-waves consequence), but the amount of vacuum in a given coordinate span differs between locations. When an observer at one potential receives signals from a clock at another, the received signal rate differs from the local rate by a factor determined by the vacuum traversed between them. This is what the time dilation proof derived: Clock B assigns Clock A a tick interval longer than Clock A's local tick interval by a factor of $\exp(gh/c^2)$ in a static gradient, approximating $(1 + gh/c^2)$ in the weak-field limit.

The second is the spatial-mapping. The same vacuum-per-coordinate-span variation that produces the time-mapping also produces a difference between proper lengths and coordinate lengths. A radial span through a well contains more proper length per unit of external coordinate than the same coordinate span in flat space, because the well's vacuum-per-coordinate-span is reduced. This is the framework's gravitational analogue of special relativity's length contraction, as committed to in the time dilation proof's Spatial Companion Effect section.

Both mappings come from the same physical source: vacuum-per-coordinate-span variation. But they are independent observables. The time-mapping is measured by comparing clocks at different potentials; the spatial-mapping is measured by comparing distances. Metric reconstruction amounts to putting each mapping in metric notation, yielding $g_{00}$ for the time-mapping and $g_{ij}$ for the spatial-mapping.

---

## The Time Component

Start from the time dilation result. In the weak-field limit, with $\Phi$ denoting the Newtonian gravitational potential (so that $\Phi = -GM/r$ for a point mass, and $g = -d\Phi/dr$ in a gradient), the mapping between a local tick interval and the tick interval assigned by an observer at a different potential is:

$$d\tau^2 \approx \left(1 + \frac{2\Phi}{c^2}\right) dt^2$$

where $d\tau$ is the proper-time interval at the lower potential and $dt$ is the coordinate-time interval assigned from the higher potential. The factor $(1 + 2\Phi/c^2)$ is less than 1 for $\Phi < 0$ (inside the well), reflecting that proper-time intervals there correspond to longer coordinate-time intervals — the mapping effect established by the time dilation derivation.

In metric notation, using the signature $(-,+,+,+)$:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right)$$

Under the framework's ledger-visible rule, this component is introduced with its framework-native meaning: $g_{00}$ records the vacuum-extent-mediated mapping between proper-time intervals at one location and coordinate-time intervals measured from elsewhere. The mapping exists because vacuum-per-coordinate-span varies between locations in a gradient, and clocks are processes whose local rates are referenced to local vacuum content. The metric component is the mathematical shadow of this mapping.

This matches the weak-field limit of GR's Schwarzschild metric at leading order in $GM/rc^2$. The agreement is not an import from GR; it is a restatement of the time dilation proof in different notation.

---

## The Spatial Components

The framework's Postulate 1, combined with the curvature-as-spatial-volume-differential consequence, commits to vacuum variation affecting spatial intervals as well as temporal ones. A coordinate span in a gravity well corresponds to more proper length than the same coordinate span in flat space, because the well's vacuum-per-coordinate-span is reduced — this is the radial-stretching side of the spatial-volume differential. The precise relation between radial stretching and angular compression is part of the unresolved spatial-structure problem and is not pinned down by the current postulates. The spatial components of the metric record whatever mapping results.

The qualitative claim is unambiguous. The quantitative coefficient is not.

The time-mapping coefficient was pinned down by the redshift proof's derivation, which used Postulate 3's force-per-unit-energy structure to compute how photon energy changes during vertical traversal. The coefficient of the time-mapping effect — the $2\Phi/c^2$ factor in the weak-field limit — falls out of that calculation directly.

No analogous calculation is available for the spatial-mapping. The framework commits to the spatial-mapping existing as a consequence of vacuum-extent variation, but the current postulates do not determine how strongly the spatial interval responds to a given amount of vacuum depletion. Three different assumptions about the mathematical structure of the vacuum could each be consistent with the postulates we have:

The spatial-mapping could respond equally strongly to vacuum depletion as the time-mapping does, giving spatial metric components that mirror the time component's form. This would reproduce the Schwarzschild structure in the weak-field limit.

The spatial-mapping could respond with a different coefficient, giving metric components of similar form but different magnitude. This would produce a weak-field metric that agrees with Schwarzschild only at the $g_{00}$ level, diverging in the spatial sector.

The spatial-mapping could have a more complex response — perhaps anisotropic, or dependent on additional vacuum properties not yet specified — producing a metric structure that doesn't match Schwarzschild's simple form at all.

The current postulates do not distinguish between these possibilities. Pinning down the spatial coefficient requires resolving the open question of the vacuum's mathematical structure — specifically, whether the vacuum's extent variation affects time and space intervals in linked or independent ways.

To make this underdetermination explicit and tractable, we introduce a parameter $\gamma_v$ defined as the ratio of the spatial-mapping response to the time-mapping response in the weak static limit. With this parameter, the spatial components of the weak-field metric take the form:

$$g_{ij} \approx \left(1 - 2\gamma_v \frac{\Phi}{c^2}\right) \delta_{ij}$$

where $\delta_{ij}$ is the flat-space spatial metric and $\gamma_v$ is the spatial-response coefficient. The framework commits to $\gamma_v$ being nonzero (the spatial-mapping exists) but does not currently pin down its value.

Under the framework's ledger-visible rule, the physical meaning of this component is: $g_{ij}$ records the vacuum-extent-mediated mapping between proper spatial intervals at one location and coordinate spatial intervals measured from elsewhere, with $\gamma_v$ quantifying how strongly this spatial mapping responds to the same vacuum-extent variation that produces the time mapping. The metric form is not an assumption; it is the most general isotropic spatial response consistent with the framework's current commitments, with $\gamma_v$ as the coefficient that future work must determine.

---

## The GR Target

General relativity's Schwarzschild metric, expanded to first order in $GM/rc^2$, has:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

In the $\gamma_v$ parameterization, this corresponds to $\gamma_v = 1$. GR's weak-field metric is the $\gamma_v = 1$ case of the framework's parameterization.

This is not just a theoretical convention. Precision tests of gravity in the solar system have constrained $\gamma_v$ (or its PPN analogue $\gamma$) extremely tightly:

The Cassini spacecraft's radio tracking during its solar conjunction in 2002 measured $\gamma = 1 + (2.1 \pm 2.3) \times 10^{-5}$ [Bertotti, Iess, & Tortora, 2003], constraining $\gamma_v = 1$ to about two parts in $10^5$.

Very-long-baseline interferometry (VLBI) measurements of quasar positions during solar conjunctions provide similarly tight constraints, at the level of $10^{-4}$ or better depending on the observational campaign.

Gravitational lensing observations of distant masses, while less precise, are consistent with $\gamma_v = 1$.

The framework's derivation target is therefore not merely theoretical agreement with GR. It is reproduction of the observed value $\gamma_v = 1$, which solar-system precision tests have pinned down to high accuracy. A framework that predicted $\gamma_v \neq 1$ would conflict directly with observation, not just with GR's theoretical structure.

---

## Why $\gamma_v$ Matters Observationally

The time-mapping and spatial-mapping contribute differently to different observations, so different precision tests probe them in different combinations.

Gravitational redshift and time dilation measurements primarily test $g_{00}$. They are sensitive to the time-mapping alone. Pound-Rebka, Hafele-Keating, GPS timing corrections, and optical-clock comparisons at different altitudes all probe the time-mapping. The framework already reproduces the weak-field result for these, independently of $\gamma_v$.

Gravitational light deflection, in contrast, tests the metric in a way that weights $g_{00}$ and $g_{ij}$ equally. For a light ray passing a mass at impact parameter $b$, the deflection angle in the weak-field limit is:

$$\Delta\theta = (1 + \gamma_v) \frac{2GM}{bc^2}$$

With $\gamma_v = 1$, this gives the full GR deflection angle $4GM/bc^2$, which was confirmed by Eddington's 1919 expedition and by numerous subsequent observations. With $\gamma_v = 0$, this gives the half-deflection $2GM/bc^2$ that Einstein originally predicted in 1911 based on the equivalence principle alone, before incorporating spatial curvature. The historical factor-of-two difference between Einstein's 1911 and 1915 predictions reflects precisely the addition of the spatial-mapping contribution.

Light bending is thus a direct diagnostic of $\gamma_v$. So is the Shapiro delay of radio signals passing near the Sun, which depends on the same combination $(1 + \gamma_v)$ through the integrated effect of both $g_{00}$ and $g_{ij}$ along the signal's path.

For the framework, this means: reproducing the weak-field time dilation and redshift observations does not yet require pinning down $\gamma_v$, because those observations are blind to it. Reproducing light bending and Shapiro delay does require $\gamma_v = 1$. Deriving $\gamma_v$ from the framework's postulates is thus a prerequisite for extending the framework's observational reach beyond the time-mapping-only tests it currently handles.

---

## What This Proof Accomplishes

As a derivation, the proof gives the weak-field time component of the metric cleanly from the time dilation proof. The spatial components are parameterized in the simplest isotropic weak-field form, with $\gamma_v$-dependent magnitude; the coefficient $\gamma_v$ is left open.

As a methodological contribution, the proof establishes how metric notation can be used within the framework without letting GR's ontology silently replace the framework's own. The rule is that every metric component must be introduced with its framework-native physical meaning, and that underdeterminations must be named explicitly rather than closed by fiat.

As a framing contribution, the proof names the spatial-response parameter $\gamma_v$ and identifies its derivation as a concrete open question downstream of the mathematical structure of the vacuum. This converts a vague gap ("we don't yet have the spatial part of the metric") into a precise one ("we need to derive $\gamma_v$"), which future work can attack directly.

As a bridge to downstream work, the partial metric gives the framework its first foothold on GR-style calculations. Geodesic motion in the $g_{00}$-only part of the metric reproduces the framework's equations of motion for test bodies in the weak-field limit, at the order where only time-mapping matters. Extending to null geodesics and to spatial-mapping-sensitive phenomena (light bending, Shapiro delay) awaits a derivation of $\gamma_v$.

The framework's remaining work on $\gamma_v$ is a derivation challenge, not a prediction challenge. Observation has already pinned down the answer to parts in $10^5$. The question the framework must answer is whether its internal structure entails $\gamma_v = 1$, not whether $\gamma_v = 1$ is the right value.

### Summary of Result

Current framework result:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right)$$

$$g_{ij} \approx \left(1 - 2\gamma_v \frac{\Phi}{c^2}\right) \delta_{ij}$$

with $\gamma_v$ currently underived by the framework.

GR and observational target:

$$\gamma_v = 1$$

Next task: derive $\gamma_v = 1$ from the framework's postulates, or identify the framework revision required.

---

## Dependency Structure

The derivation depends on Postulates 1, 2, and 3, mass-energy equivalence, the curvature-as-spatial-volume-differential consequence, the gravitational redshift proof, the gravitational time dilation proof, and special relativity. It does not invoke Postulates 4 or 5.

The document uses "configuration" language that overlaps with Postulate 4's terminology but does not rely on Postulate 4's content. "Configuration" in this document means how the vacuum is arranged — the distribution of vacuum-per-coordinate-span across locations — and is inherited from Postulate 1 and the curvature-as-spatial-volume-differential consequence. Postulate 4's claim that configurations carry energy is a separate commitment, not used here. If later work assigns configuration energy to the arrangements described in this document, Postulate 4 will become relevant; the formal reconstruction itself does not require it.

This narrow dependency joins the redshift and time dilation proofs in a tight subframework insulated from the framework's configuration-energy and minimum-energy-dynamics machinery. If future work leads to revisions of Postulates 4 or 5, this proof and its companions are unaffected.

The proof adds one new commitment to the framework: the $\gamma_v$ parameterization of the spatial-mapping response. This parameterization is not itself a postulate — it is a named placeholder for a coefficient that the framework will need to derive from its underlying structure. Naming the placeholder explicitly is progress because it identifies what needs to be derived; deriving it remains open.

---

## What Remains Open

The central open question, newly made precise: derive $\gamma_v$ from the framework's underlying structure.

This question has two plausible paths.

One path is through the mathematical structure of the vacuum. If the vacuum's formal structure turns out to be such that vacuum-extent variation affects time and space intervals symmetrically — with a single parameter controlling both — then $\gamma_v$ is fixed by that symmetry. The specific value would depend on the details of the structure.

A second path is through a symmetry argument at the level of the postulates themselves, without requiring the full mathematical structure. For instance, one might argue that the framework's commitment to local Lorentz invariance of vacuum physics, combined with the flat-vacuum limit reducing to Minkowski spacetime, forces $\gamma_v$ to a specific value. Whether such an argument can be constructed from the current postulates is not clear; this document does not attempt it.

Both paths are open. Producing a derivation of $\gamma_v = 1$ would close the weak-field metric and open the path to light bending, Shapiro delay, and the standard tests of gravity beyond the time-mapping-only regime. Producing a derivation of $\gamma_v \neq 1$ would commit the framework to predictions that conflict with observation, and the framework would need to be reconsidered at a deeper level.

Either outcome is informative. The value of naming the question precisely is that future work can target it directly, rather than working on "the mathematical structure of the vacuum" as a general research program.

---

## References

Bertotti, B., Iess, L., & Tortora, P. (2003). A test of general relativity using radio links with the Cassini spacecraft. *Nature*, 425(6956), 374–376.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.