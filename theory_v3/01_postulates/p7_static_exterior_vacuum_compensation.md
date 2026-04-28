# P7: Static Exterior Vacuum Compensation

## What This Postulate Says

In a static, source-free exterior vacuum configuration, curvature is a redistribution of vacuum extent, not a net creation or destruction of vacuum substance.

A region outside a localized constraint, such as the exterior region around an isolated spherical mass, can be curved while containing no matter source of its own and undergoing no net vacuum exchange. In such a region, the vacuum may be directionally redistributed — temporal and spatial mappings may vary from radius to radius — but the local vacuum measure is preserved. P7 commits the framework to this preservation taking a specific form: temporal and radial distortions compensate.

In the static spherically symmetric case, this compensation implies that the temporal-mapping factor and radial-spatial-mapping factor are reciprocal. If the temporal factor is written as $A(r)$ and the radial spatial factor as $B(r)$, then

$$A(r)B(r) = \text{constant}.$$

With asymptotic flatness,

$$A(r) \to 1, \qquad B(r) \to 1$$

as $r \to \infty$, so the constant is $1$, giving

$$A(r)B(r) = 1.$$

This is the framework-native counterpart of the Schwarzschild exterior relation between temporal and radial metric coefficients. It is not a general law for all vacuum behavior. It applies only in static, source-free exterior regions where no net vacuum substance is being created or destroyed.

---

## Epistemic Status

P7 is not derived from P1–P6.

P3 establishes local constancy of vacuum density. P3a establishes that curvature is variation in vacuum amount rather than density. These commitments motivate P7 — they make it natural to ask what happens in a region where no substance exchange is occurring — but they do not logically force the specific compensation condition $A(r)B(r) = 1$. P3 is a constraint on density, not on the relationship between coordinate and proper measures. P3a leaves the mathematical form of the differential open. Neither alone, nor in combination, fixes the specific form of compensation.

P7 is therefore a new structural postulate. It states how source-free static exterior vacuum behaves in the configuration regime. Its role is analogous to the source-free Einstein equation in the Schwarzschild exterior derivation: it supplies the missing condition that relates temporal and radial mappings.

A later version of the framework may derive P7 from a deeper configuration-energy functional or field equation. The framework's general program is to eventually derive field equations from a more complete account of the configuration energy functional and its dynamics; P7 is one of the constraints that such field equations would need to reproduce in the appropriate limit. Until that derivation exists, P7 stands as an independent postulate, and downstream theorems that depend on reciprocal scaling are conditional on it.

The framework's commitment is not that P7 is logically forced by deeper principles. The commitment is that P7 is a useful node in the search over possible postulate sets — consistent with existing commitments, productive of the right downstream results, and precisely localized so that future work can attempt to derive it or replace it with something more fundamental.

---

## The Question This Answers

The framework already derives gravitational redshift and gravitational time dilation in the weak-field limit. T1 shows that photons lose energy climbing through a curvature gradient, and T2 shows that clocks lower in the gradient are assigned slower rates by observers higher in the gradient.

Those results establish the temporal side of weak-field gravity.

But recovering the rest of weak-field general relativity requires more. Light deflection, Shapiro delay, and perihelion precession depend not only on the temporal mapping but also on the spatial mapping. In standard general relativity, the Schwarzschild exterior solution satisfies a reciprocal relation between the temporal and radial metric coefficients. In one common convention,

$$g_{tt}g_{rr} = -1,$$

or, ignoring the sign convention,

$$AB = 1.$$

The previous version of the framework did not derive this relation. It could reproduce the temporal part, but it had no internal reason why the spatial response should be reciprocal to the temporal response. That gap left the recovery of weak-field GR incomplete; the framework's earlier proofs of light deflection, Shapiro delay, and perihelion precession all depended on a "unity assumption" that was adopted because observation required it, not because the framework's postulates forced it.

P7 is the new framework's response to that gap. Where the previous version's unity assumption asserted the needed recovery condition globally and vaguely, P7 restricts the claim to static, source-free exterior vacuum and ties it to the framework's configuration/substance distinction. The condition is the same; the localization and structural interpretation are new.

P7 does not derive the result from deeper principles. It localizes the missing commitment precisely. The framework's epistemic position with P7 adopted is: the postulates plus SR plus this specific exterior compensation principle commit the framework to recovering weak-field GR's tests. The compensation principle is a structural commitment about source-free static exterior configurations, not a consequence of more fundamental commitments.

---

## Configuration Regime versus Substance Regime

P7 depends on a distinction already present in the framework: configuration changes and substance changes are not the same thing.

A **substance-regime** process changes the amount of vacuum present. Vacuum is created or destroyed. Since P1 identifies vacuum with energy and P2 identifies vacuum with spacetime, substance-regime processes are real changes in the amount of spacetime-energy present.

A **configuration-regime** process changes how the vacuum is arranged without changing the amount of vacuum substance present. The directional structure changes. Curvature changes. Configuration energy changes. But there is no net creation or destruction of vacuum substance.

P7 applies only to configuration-regime exterior gravity.

In the static exterior of an isolated mass, the mass imposes a constraint on the surrounding vacuum. The surrounding vacuum settles into the minimum-energy configuration consistent with that constraint (P5). But outside the matter source itself, the exterior region is source-free. It is not a region where vacuum substance is being steadily created or destroyed. It is a region where the vacuum arrangement is held in a curved configuration by the constraint.

P7 adds the further commitment that in such a region, the absence of substance exchange is expressed as compensated temporal-radial distortion — that the directional distortions take the specific form $A(r)B(r) = \text{constant}$. This is not forced by the absence of substance exchange alone; many forms of directional distortion would be consistent with no substance exchange. P7 commits to this particular form.

---

## What Compensation Means

Compensation means that directional distortions balance.

A curvature gradient can change how temporal intervals and radial spatial intervals map between observers at different radii. A lower clock can be assigned a slower rate by a higher observer. A radial span can be assigned a different proper length than its coordinate length would suggest. These are real mapping differences.

P7 commits the framework to those differences taking a specific form in static source-free exteriors. The temporal and radial distortions are not independent. A temporal compression is matched by a radial expansion, or vice versa, so that the local temporal-radial product remains unchanged.

In spherical symmetry, after choosing the radial coordinate $r$ as the areal radius, the angular sector is fixed by convention:

$$d\Omega^2 = d\theta^2 + \sin^2\theta\,d\phi^2,$$

and spheres at radius $r$ have area $4\pi r^2$.

The remaining exterior directional freedom is in the temporal and radial factors. Let those be called $A(r)$ and $B(r)$. P7 says that in the static source-free exterior, their product is constant:

$$A(r)B(r) = \text{constant}.$$

This can also be written as

$$\frac{d}{dr}\ln(A(r)B(r)) = 0,$$

or

$$\frac{A'(r)}{A(r)} + \frac{B'(r)}{B(r)} = 0.$$

With asymptotic flatness,

$$A(r) \to 1, \qquad B(r) \to 1$$

at infinity, so

$$A(r)B(r) = 1.$$

Thus,

$$B(r) = \frac{1}{A(r)}.$$

This is reciprocal scaling.

---

## Relationship to Constant Vacuum Density

P3 commits the framework to a finite locally constant vacuum energy density. That means curvature cannot be density variation. The vacuum cannot be denser in one region and thinner in another in the local-density sense. Every observer locally measures the same vacuum density.

P3a then identifies curvature with spatial differential of vacuum amount across neighboring regions. This makes curvature an extensive variation, not an intensive one. The amount of vacuum associated with a region or direction can vary, while the density of vacuum itself remains fixed.

P7 adds a further structural restriction for static source-free exterior regions. In those regions, because no net substance exchange is occurring, the directional variations are committed to preserving the local vacuum measure in a specific way: as compensated temporal-radial distortion. The vacuum is redistributed among temporal and radial directions, but the product of the temporal and radial scaling factors remains constant.

The relationship to P3 is motivational, not derivational. P3's constant density makes it natural to ask whether some analogous "incompressibility" condition holds for vacuum amount in the absence of exchange. P7 is the framework's specific commitment about how that incompressibility manifests in static source-free exteriors. P3 alone does not force this specific form, but the form is consistent with P3 and extends its spirit to the configuration-regime context.

---

## Relationship to Cosmic Expansion

P7 does not apply to cosmic expansion.

Cosmic expansion is not a static source-free exterior configuration. In the framework's vocabulary, cosmic expansion is a substance-regime process: new vacuum/spacetime is created as space expands. The local or global vacuum amount changes. Therefore the compensation condition does not apply.

This matters because a too-broad version of P7 would be false. The framework cannot say that vacuum amount is always conserved. P1 and P2 explicitly allow vacuum creation and destruction, and P6 uses vacuum exchange to account for energy changes in gradients.

P7 says something narrower:

**When the region is static, exterior, source-free, and undergoing no net vacuum exchange, curvature is compensated directional redistribution.**

That restriction prevents conflict with cosmic expansion, collapse, radiation, redshift exchange, or any process involving net vacuum creation or destruction.

---

## Relationship to P6

P6 says that energy in a curvature gradient experiences a force, and that kinetic-energy changes associated with this force are sourced or sunk by vacuum exchange.

P7 does not deny this. It applies to a different question.

P6 concerns what happens when energy moves through a gradient. A photon climbing through a gradient loses energy; that lost energy is matched by vacuum creation. A falling body gains kinetic energy; that gain is matched by vacuum destruction. These are substance-regime exchange events associated with motion through a gradient.

P7 concerns the static exterior configuration itself. It commits the framework to the background exterior vacuum configuration, when no net exchange is occurring, having compensated directional structure. The field configuration around the source is a configuration-regime structure. Objects moving through that configuration may trigger P6 exchanges, but the static source-free exterior geometry itself is governed by P7's compensation condition.

Thus P6 and P7 operate at different levels:

- P7 constrains the static exterior vacuum configuration.
- P6 governs energy exchange for bodies or photons moving through a gradient.

They are compatible.

---

## Relationship to General Relativity

In general relativity, the Schwarzschild exterior solution begins with a static spherically symmetric metric, usually written in areal-radius coordinates as

$$ds^2 = -A(r)c^2dt^2 + B(r)dr^2 + r^2d\Omega^2.$$

The vacuum Einstein equations imply

$$\frac{A'}{A} + \frac{B'}{B} = 0,$$

so

$$A(r)B(r) = \text{constant}.$$

Asymptotic flatness fixes the constant to $1$, giving

$$A(r)B(r) = 1.$$

P7 plays the same mathematical role in the framework that the source-free vacuum Einstein equations play in GR's Schwarzschild derivation. The framework does not begin with the metric as a primitive field, and it does not derive curvature from the metric-connection-Riemann chain. Instead, it treats curvature as directional variation of vacuum amount and treats exterior gravity as a compensated configuration of the vacuum.

The mathematical role is parallel:

- GR: source-free Einstein equations force reciprocal temporal/radial coefficients.
- This framework: static source-free exterior compensation forces reciprocal temporal/radial mappings.

If P7 is accepted, then the framework has the structural ingredient needed to recover the weak-field Schwarzschild relation. P7 functions as a design constraint for any future field equations the framework develops: those equations must reproduce P7 in the static source-free exterior limit, just as Einstein's equations reproduce $AB = 1$ in the Schwarzschild exterior.

---

## What the Postulate Does Not Say

P7 is deliberately narrow.

It does not say that vacuum substance is always conserved. The framework allows vacuum creation and destruction.

It does not apply to cosmology. Expanding space is not a static exterior configuration.

It does not apply inside matter. The region containing the source is not source-free.

It does not apply automatically to rotating systems. Rotation introduces additional directional structure and frame-dragging-like effects.

It does not apply automatically to time-dependent systems. Gravitational radiation, collapse, changing mass distributions, and propagating disturbances require additional dynamics.

It does not specify the full configuration energy functional. P4 says curvature contains configuration energy, and P5 says the vacuum seeks minimum-energy configurations, but P7 does not provide the full functional form.

It does not by itself derive the gravitational potential profile $A(r)$. T1 and T2 fix the temporal weak-field behavior in a given gradient; a full source law is still needed to derive the gradient profile from a mass distribution.

It does not prove the strong-field Schwarzschild metric. It supplies the reciprocal scaling condition. Strong-field recovery still depends on the framework's source law, configuration-energy functional, and constraint structure.

---

## The Postulate

**P7: Static Exterior Vacuum Compensation.**

In a static, source-free exterior vacuum configuration undergoing no net vacuum substance creation or destruction, curvature is compensated directional redistribution of vacuum extent. The local temporal-radial vacuum measure is preserved by the framework's commitment that temporal and radial distortions take a reciprocal form. In a static spherically symmetric exterior configuration, using areal-radius coordinates, this implies that the temporal-mapping factor $A(r)$ and radial-spatial-mapping factor $B(r)$ satisfy

$$A(r)B(r) = \text{constant}.$$

With asymptotic flatness,

$$A(r)B(r) = 1.$$

---

## Consequences

The immediate consequence is reciprocal scaling:

$$B(r) = \frac{1}{A(r)}.$$

In the weak-field limit, if T1 and T2 give the temporal factor

$$A(r) \approx 1 + \frac{2\Phi(r)}{c^2},$$

then P7 gives the radial factor

$$B(r) \approx 1 - \frac{2\Phi(r)}{c^2}$$

or the reciprocal form depending on the convention used for $A$ and $B$. The sign and placement of the factors depend on whether $A$ and $B$ are defined as metric coefficients, proper-to-coordinate mappings, or coordinate-to-proper mappings. The invariant content is the reciprocal relation.

This is the missing weak-field recovery condition. It supplies the framework's analogue of the PPN result

$$\gamma = 1.$$

With this relation in place, the framework can attempt unconditional derivations of the remaining weak-field gravitational tests:

- light deflection,
- Shapiro delay,
- perihelion precession.

Those derivations are conditional on P7 in the same sense that P7 itself is — they depend on the structural commitment P7 makes, which is not derived from the framework's other postulates. If P7 is later derived from a deeper field equation, those theorems become unconditional. If P7 is later modified or rejected, those theorems would need revisiting.

---

## Open Work

P7 closes one gap but exposes several others.

First, the framework needs precise definitions of the mapping factors $A(r)$ and $B(r)$. These should be defined in framework-native terms before being compared to metric coefficients.

Second, the framework needs a source law connecting localized mass-energy constraints to gradient profiles. P7 gives reciprocal scaling once a static exterior configuration exists; it does not derive the radial dependence of the configuration from the source.

Third, the framework needs a fuller account of time-dependent configurations. If static exterior compensation is broken during changing constraints, the theory must explain how disturbances propagate and whether the resulting behavior reproduces gravitational waves.

Fourth, the framework should aim to eventually derive P7 from a deeper configuration-energy functional or field equation. The framework's general program is to derive field equations from a more complete account of the configuration energy and its dynamics; P7 is one of the constraints those field equations would need to reproduce in the static source-free exterior limit. The framework's epistemic position improves significantly when P7 is demoted from postulate to derived consequence of a more fundamental account.

---

## Summary

P7 states that static source-free exterior curvature is compensated directional redistribution, not net vacuum substance creation or destruction.

This gives the framework an explicit structural commitment about the relationship between temporal and radial spatial mappings in the exterior spherical case. It supplies the missing condition needed to recover the weak-field Schwarzschild relation $AB = 1$, while remaining narrow enough not to conflict with cosmic expansion or vacuum exchange in gradients.

P7 is not derived from P1–P6. It is a new structural postulate, motivated by the framework's ontology but not entailed by it. Its role in the framework is as a design constraint for future field equations and as the precise localization of the structural commitment that earlier versions of the framework adopted globally and vaguely as the unity assumption.

---

## Imports

This postulate depends on:

- P1: Vacuum-Energy Equivalence (the vacuum being preserved is real energy)
- P2: Vacuum-Spacetime Identity (the vacuum being preserved is spacetime)
- P3: Vacuum Energy Density (the constant density that motivates the incompressibility extension)
- P3a: Spatial Differential is Curvature (the directional structure that the compensation condition restricts)
- P4: Curvature Contains Energy (configuration energy is what's being held in static configuration)
- P5: Vacuum Seeks Minimum Energy Configuration (the minimum-energy configuration under static constraints is what P7 characterizes)
- P6: Vacuum Exchange in Gradients (P7 is restricted to regions not undergoing P6's substance exchange)
