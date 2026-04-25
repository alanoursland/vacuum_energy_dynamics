# Candidate: Vacuum Variation Unity

---

## What This Document Is

This is a candidate document. It adopts a specific commitment — the "unity assumption" — that the framework cannot currently derive from its postulates but that is natural given the framework's other commitments. The assumption closes the weak-field metric derivation at $\gamma_v = 1$, which is what observation requires.

The status is provisional. The unity assumption is plausible and consistent with the framework's existing content, but it is not proven. Future work may derive it from deeper structural commitments, replace it with a better-grounded commitment, or refute it and force a reconsideration of what the framework predicts. Until then, derivations that depend on the unity assumption inherit its provisional status.

This document exists for two reasons. First, to state the assumption explicitly so that future work can track what depends on it. Second, to prevent a pitfall: the unity assumption applies to the static spherically-symmetric response of the vacuum, not to the vacuum's full mathematical structure. Confusing the two would accidentally commit the framework to scalar gravitational waves, which Hulse-Taylor observations rule out. The document is careful to distinguish these.

---

## The Situation

The weak-field metric proof derives the time component $g_{00}$ cleanly from the gravitational time dilation proof, giving $g_{00} \approx -(1 + 2\Phi/c^2)$ in the weak-field limit. The spatial components are parameterized by:

$$g_{ij} \approx \left(1 - 2\gamma_v \frac{\Phi}{c^2}\right) \delta_{ij}$$

where $\gamma_v$ measures the ratio of spatial-mapping response to time-mapping response. General relativity has $\gamma_v = 1$, and solar-system precision tests (Cassini, VLBI) constrain $\gamma_v = 1$ to parts in $10^5$. The framework commits to the spatial mapping existing but does not currently pin down its coefficient.

The framework must either derive $\gamma_v = 1$ from its postulates or adopt it as an additional commitment. This document does the latter, acknowledging it as an assumption pending future derivation.

---

## Statement of the Unity Assumption

The assumption has two components that are worth stating separately, because they do different amounts of work and may succumb to different lines of derivation or refutation.

**Static Single-Function Assumption.** The static spherically-symmetric response of the vacuum to a mass is characterized by a single radial function $f(r)$. The vacuum's configuration in this case has one symmetry-invariant degree of freedom relevant to weak-field metric structure.

**Equal-Response Assumption.** Both the time-mapping (encoded in $g_{00}$) and the spatial-mapping (encoded in $g_{rr}$) depend on this function through the same response coefficient. If $g_{00} \approx -(1 + a\,(1 - f))$ and $g_{rr} \approx (1 + b\,(1 - f))$ to leading order, the Equal-Response Assumption states that $a = b$.

**Unity Assumption.** The Static Single-Function Assumption and the Equal-Response Assumption together.

The Static Single-Function Assumption is the easier part to justify. Under spherical symmetry, the vacuum's response to a mass reduces to functions of radius — but symmetry alone does not guarantee that there is only one such function. In general, a spherically symmetric metric has multiple independent radial functions (for example $g_{00}(r)$ and $g_{rr}(r)$ as independent functions in GR's Schwarzschild solution, related only by the field equations and not by symmetry). Symmetry reduction plus the framework's "amount of vacuum per coordinate span" language makes one radial function a natural candidate for summarizing the vacuum's response, but getting from "functions of radius" to "one function of radius" is additional work, not a consequence of symmetry alone.

The Equal-Response Assumption is where the real content lives. Having one function does not by itself fix the relationship between its time coupling and its space coupling. A framework with richer internal structure could have two independent coefficients $a$ and $b$ that both happen to couple to the same scalar function. Only the claim that these coefficients are equal gives $\gamma_v = 1$ and closes the metric to the Schwarzschild form.

Future work that derives single-function reduction from symmetry alone has not yet derived unity. Equal-response is an additional step, and deriving it is what would promote this candidate to a full proof.

With both assumptions adopted, the weak-field metric closes to:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

---

## Why the Assumption Is Plausible

The identity postulate treats the vacuum as a single unified substance — spacetime itself, not a field residing on spacetime. The curvature-as-spatial-volume-differential consequence introduces "amount of vacuum per coordinate span" as the quantity in which curvature lives. Under static spherical symmetry, this variation can be represented by a single radial function: at each radius, the configuration has one symmetry-invariant degree of freedom relevant to the weak-field mapping. This does not mean the full vacuum structure is scalar; it means the symmetry-reduced response is summarizable by one function of radius.

If the symmetry-reduced variation is one function of radius, it is natural to posit that its effects on the metric are also characterized by a single response relationship — that the time-mapping and the spatial-mapping are governed by the same coupling to this one function, rather than by independent couplings that happen to coincide.

Under this reading, the unity assumption is the most natural extension of the identity postulate to the quantitative question of how vacuum variation produces metric variation. Vacuum is one substance; under spherical symmetry its variation reduces to one function; and the natural commitment is that one function produces one coupled response, not two independent ones.

Nothing in the existing postulates suggests that the time response and the spatial response should be governed by independent coefficients. The postulates commit to both mappings existing; they do not commit to the mappings being independent.

---

## Why It Is an Assumption and Not a Derivation

"Most natural reading" is not "logically forced." A reader who wanted to reject the unity assumption could posit that the vacuum has richer mathematical structure than the current postulates reveal, with internal degrees of freedom that support independent time-response and space-response coefficients. Nothing in the current postulates directly rules this out.

Specifically, the framework's current commitments leave open:

- Whether "amount of vacuum per coordinate span" is a complete description of the vacuum's variation, or only a symmetry-reduced summary of richer structure.
- Whether the static spherically-symmetric response is characterized by one function or several.
- Whether the vacuum's coupling to the metric has one coefficient (equal-response) or more.

The Static Single-Function Assumption takes a position on the first two. This is a weaker commitment — symmetry plus the framework's existing language strongly suggests one radial function is enough in the spherical case. A derivation of the Single-Function part from symmetry and existing postulates may be tractable.

The Equal-Response Assumption takes a position on the third. This is the stronger commitment. Even granting that one function summarizes the static spherical response, nothing in the current postulates forces the time-coupling and space-coupling coefficients to be equal. Independent coefficients are logically available; the framework's commitments do not rule them out.

This is why the document is labeled a candidate rather than a proof. The framework is provisionally committing to the unity assumption — particularly its Equal-Response component — without deriving it.

---

## What the Assumption Gives

With unity adopted, the weak-field metric is fully determined:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

This reproduces the linearized Schwarzschild metric and matches solar-system precision tests.

Downstream consequences that become derivable:

- **Light bending** at a mass: the deflection angle becomes $(1 + \gamma_v)(2GM/bc^2) = 4GM/bc^2$, matching Eddington's 1919 observation and the GR prediction.
- **Shapiro delay** of radio signals passing near a mass: the integrated delay along a null geodesic through the weak-field metric gives the GR result, matching Cassini observations.
- **Geodesic motion of test bodies** in weak fields: the standard Newtonian limit plus GR's post-Newtonian corrections fall out of the metric's geodesic equation.

Each of these becomes a proof-document-level derivation once the unity assumption is adopted. Without it, they remain parameterized by $\gamma_v$ and cannot be quantitatively closed.

---

## What the Assumption Does Not Imply About Gravitational Waves

This section is important because the unity assumption could be misread in a way that would unnecessarily restrict what the framework predicts.

The unity assumption is a statement about the **static spherically-symmetric response** of the vacuum. It says that in this specific case, the vacuum's variation is summarizable by a single radial function with a single coupling relationship between time-mapping and spatial-mapping.

The unity assumption is **not** a statement about the vacuum's full mathematical structure. It does not say the vacuum is fundamentally a scalar field. It does not say the vacuum has only scalar degrees of freedom. It does not say dynamic disturbances of the vacuum are scalar.

The distinction matters because of what observation requires of gravitational radiation.

Observational constraints on gravitational wave polarization structure are substantial but specific. Pure scalar gravitational theories — in which all radiation is scalar, with dipole channels as the dominant emission mode — are ruled out by binary-pulsar orbital decay measurements (Hulse-Taylor and subsequent systems), because strong dipole radiation would produce orbital decay rates inconsistent with observation. LIGO and Virgo observations of compact binary mergers strongly favor GR-like transverse tensor modes over pure scalar or pure vector alternatives.

What observation does *not* rule out is scalar-tensor structures, in which gravitational radiation has both tensor and scalar components, with the scalar contribution suppressed sufficiently to avoid conflict with binary-pulsar and LIGO constraints. Brans-Dicke gravity is the classical example: tensor radiation dominates, scalar radiation is suppressed by a large coupling parameter, and the theory is observationally viable in the appropriate parameter regime.

So the observational landscape is: pure scalar gravitational waves are excluded; tensor waves are required; scalar waves in addition to tensor waves are permitted provided the scalar component is suitably small.

If the unity assumption implied that the framework's gravitational radiation was pure scalar, the framework would conflict with observation. It does not imply this. Here is why.

Consider the analogy with electromagnetism. The static electric field around a point charge is fully described by a single scalar function — the Coulomb potential $\phi(r)$. But electromagnetic radiation is not scalar. It is the propagation of transverse oscillations of the electromagnetic field, with two polarization modes. The scalar character of the static case does not force the dynamic case to be scalar. The electromagnetic field has richer structure (four-potential, or $\vec{E}$ and $\vec{B}$) that is only fully revealed in dynamic situations.

The same structure could hold for the vacuum in this framework. The static spherically-symmetric response of the vacuum might be summarizable by a scalar function $f(r)$ — as the unity assumption says — while the vacuum's full structure, revealed in dynamic non-symmetric situations, is tensor or richer. Two masses in orbit do not produce a spherically symmetric situation; the vacuum's response in that case could have tensor character even while its response to a static single mass is summarizable by one radial function.

Under this reading, the unity assumption is consistent with several possible wave structures:

- **Pure tensor** — the vacuum's full structure is tensor, with no scalar degree of freedom in the wave regime. The framework reproduces GR's tensor-only wave prediction.
- **Tensor with small scalar** — the vacuum has mostly tensor structure but with a scalar component that produces suppressed scalar waves. The framework lives in scalar-tensor territory, with observational viability depending on how strongly the scalar component couples.
- **Something richer** — the vacuum's structure might have additional degrees of freedom not captured by either tensor or scalar descriptions alone.

The unity assumption does not decide between these possibilities. It constrains the static spherically-symmetric case and leaves the wave structure open, to be settled by further work on the vacuum's full mathematical structure.

---

## What Kind of Vacuum Structure Would Satisfy All Constraints

The unity assumption, combined with the framework's other commitments, places specific requirements on the vacuum's mathematical structure. The structure must support:

1. **Symmetry-reduced scalar response in the static spherically-symmetric case**, so that $\gamma_v = 1$ and the weak-field metric reproduces Schwarzschild. This is what the unity assumption says, and what observation requires.

2. **At least tensor polarization in the dynamic case**, so that gravitational radiation includes the plus-and-cross transverse modes consistent with LIGO observations and Hulse-Taylor's orbital decay. Pure scalar or pure vector wave structures are excluded observationally. Tensor-plus-scalar or richer structures are permitted provided the scalar (or other) component is suppressed enough to respect binary-pulsar and LIGO constraints.

3. **Propagation at $c$**, following from the identity postulate and the fact that curvature carries energy (Postulate 4) and the vacuum defines how energy propagates.

A tensor field of the right kind can satisfy all three simultaneously. The metric perturbation $h_{\mu\nu}$ in linearized general relativity is an example: it is tensor-valued, produces scalar-character response for a static spherically-symmetric source (the Schwarzschild solution), has transverse polarization modes for dynamic perturbations, and propagates at $c$.

A scalar-tensor structure — where the vacuum has tensor degrees of freedom plus a scalar component suitably coupled — is also consistent. This is where Brans-Dicke gravity lives, and it is where the framework might turn out to live if the vacuum's structure is richer than pure tensor. In Brans-Dicke specifically, $\gamma$ depends on the scalar coupling parameter $\omega$ and approaches unity only in the large-$\omega$ limit where scalar effects become negligible.

This means: the framework's commitments are consistent with a range of possible vacuum structures, including GR-like pure tensor, Brans-Dicke-like scalar-tensor in the large-coupling limit, and potentially richer alternatives. The unity assumption is compatible with these structures, and may be implied by some of them. For GR-like pure tensor, unity falls out of the specific structure of linearized $h_{\mu\nu}$ plus spherical symmetry. For scalar-tensor theories, unity is generically not implied — it is a constraint on the theory's parameters, with observational viability requiring the scalar coupling to be close to the decoupling limit. Specifying the vacuum's full mathematical structure within the framework's own language, and determining which observational regime the framework actually sits in, remains the framework's deepest open question.

---

## Warning: Building on the Unity Assumption

Derivations that depend on the unity assumption inherit its provisional status.

Future work should treat the following as provisional closure of otherwise-open questions:

- The weak-field metric in its Schwarzschild-matching form.
- Light bending at the full GR-predicted angle.
- Shapiro delay at the full GR-predicted magnitude.
- Geodesic motion in the full weak-field metric.

If the unity assumption is later shown to be wrong — either through a derivation of a different coefficient relationship, or through an observational anomaly — every result that depends on it needs revisiting. Proof documents that build on the weak-field metric should explicitly note that they depend on the unity assumption through the metric, and acknowledge the provisional character of their results.

This is not a reason to avoid building on the unity assumption. It is a reason to track the dependency explicitly so that if the assumption fails, the damage is contained and the affected derivations can be identified cleanly.

---

## What Would Derive or Refute the Assumption

**Derivation paths.** The unity assumption could be derived from deeper structural commitments the framework has not yet made. Different paths apply to the two components.

For the Static Single-Function component, derivation may be approachable. Spherical symmetry applied to the existing framework content reduces the vacuum's response to functions of radius, and the framework's "amount of vacuum per coordinate span" language makes a single radial function a natural candidate. But symmetry alone does not force the response to be one function rather than several, and showing the single-function form rigorously requires pinning down enough of the vacuum's mathematical structure to see how spherical symmetry constrains it.

For the Equal-Response component, derivation is harder. Two candidate routes:

- Pinning down the vacuum's mathematical structure sufficiently to show that time-coupling and space-coupling coefficients are forced equal. If the vacuum is shown to be tensor-valued with the specific structure of linearized GR's $h_{\mu\nu}$, equal response follows from tensor algebra plus spherical symmetry.
- A symmetry argument at the postulate level. Local Lorentz invariance combined with the flat-vacuum limit plus some additional constraint might force time and spatial responses to share a coefficient. Null propagation consistency is a candidate direction here, though initial brainstorming suggested it is not by itself sufficient.

**Refutation paths.** The unity assumption could be refuted by:

- Observational anomalies inconsistent with $\gamma_v = 1$ at precision beyond current constraints. Improved solar-system tests, more stringent VLBI observations, or novel tests at different scales could reveal $\gamma_v \neq 1$.
- A derivation from deeper postulates showing that time-response and space-response coefficients are independent, producing a specific $\gamma_v \neq 1$ prediction that conflicts with observation.

Either outcome would reshape the framework. A derivation of unity — particularly of the Equal-Response component — would promote this candidate to a proof. A refutation would force the framework to explain why observation appears to support unity despite the framework's deeper structure rejecting it — or to revise the deeper structure.

---

## Dependency Structure

The unity assumption depends directly on the weak-field metric proof (which it closes), on the identity postulate (which grounds the "vacuum as unified substance" intuition), and on the curvature-as-spatial-volume-differential consequence (which introduces "amount of vacuum per coordinate span" as the extensive quantity in which curvature lives).

Through the weak-field metric proof, the candidate inherits dependencies on Postulates 1 and 2, mass-energy equivalence, the redshift proof, the time dilation proof, and special relativity. The candidate does not invoke these directly but they are in the chain.

The candidate does not depend on Postulates 4 or 5. Configuration energy and minimum-energy dynamics play no role in the assumption or its consequences.

This dependency structure is worth tracking because anything that depends on the closed weak-field metric (light bending, Shapiro delay, full geodesic motion) depends transitively on the unity assumption. If unity is refuted, those derivations become invalid. If any of its direct dependencies (the identity postulate, the curvature consequence) is revised, the argument for unity's plausibility may need reworking even if the assumption itself remains consistent with observation.

---

## Status Summary

**Claim:** The Unity Assumption has two components. (1) Static Single-Function: the vacuum's static spherically-symmetric response to a mass is characterized by a single radial function. (2) Equal-Response: both the time-mapping and the spatial-mapping depend on this function through the same coupling coefficient.

**Status:** Provisional. The Single-Function component may be approachable through symmetry plus existing postulates, but spherical symmetry alone does not guarantee a single function — it only reduces independent degrees of freedom to functions of radius. Deriving the single-function form requires additional argument beyond pure symmetry. The Equal-Response component is the stronger claim and the one that actually sets $\gamma_v = 1$; it is natural given the identity postulate but is not derived.

**Consequences if adopted:** $\gamma_v = 1$, weak-field metric closes to linearized Schwarzschild, light bending and Shapiro delay match GR.

**What it does not determine:** The vacuum's full mathematical structure or its wave mode content. The framework remains compatible with pure tensor structure, scalar-tensor structure, or richer alternatives, subject to observational constraints on wave polarization.

**Next work:** Derive the Equal-Response component from deeper structural commitments, or identify what additional commitment is needed to close it.

---

## References

Bertotti, B., Iess, L., & Tortora, P. (2003). A test of general relativity using radio links with the Cassini spacecraft. *Nature*, 425(6956), 374–376.

Hulse, R. A., & Taylor, J. H. (1975). Discovery of a pulsar in a binary system. *The Astrophysical Journal*, 195, L51–L53.

Taylor, J. H., & Weisberg, J. M. (1982). A new test of general relativity: Gravitational radiation and the binary pulsar PSR 1913+16. *The Astrophysical Journal*, 253, 908–920.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.