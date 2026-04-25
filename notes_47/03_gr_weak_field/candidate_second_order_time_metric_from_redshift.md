# Candidate: Second-Order Time Metric from Redshift Exponential

---

## What This Document Is

This is a candidate document. It adopts a specific identification — the framework's $g_{00}$ at second order in $\Phi/c^2$ matches the standard PPN form with $\beta = 1$ — that the framework cannot currently derive rigorously but that follows from a natural extension of the gravitational redshift proof's exponential form.

The status is provisional. The identification is plausible and consistent with the framework's existing content, but it depends on extending the redshift proof's uniform-gradient result to spherically symmetric potentials in a specific way that the framework has not formally derived. Future work may make this extension rigorous, replace it with a different identification, or refute it.

This document exists for the same reason as `candidate_vacuum_variation_unity.md`: to state a load-bearing provisional commitment explicitly so future work can track what depends on it. The perihelion precession proof, and any future post-Newtonian derivations involving $g_{00}$ at second order, depend on this identification. Tracking it as a separate candidate keeps the dependency map clean.

---

## The Situation

The framework's gravitational redshift proof derives that a photon's energy in a gradient evolves as:

$$E(h) = E_0 \exp(-gh/c^2)$$

where $g$ is the local gradient strength and $h$ is height. This was derived for a uniform gradient over a height — the regime of the Pound-Rebka experiment.

The weak-field metric proof gives $g_{00}$ at first order in $\Phi/c^2$:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right)$$

Several derivations require $g_{00}$ at second order in $\Phi/c^2$. The standard PPN expansion of $g_{00}$ for a spherically symmetric mass is:

$$g_{00} = -1 + \frac{2U}{c^2} - 2\beta \frac{U^2}{c^4} + ...$$

where $U = -\Phi = GM/r > 0$ and $\beta$ is the PPN nonlinearity parameter. In general relativity (in isotropic coordinates), $\beta = 1$. Solar-system tests including perihelion precession and the Nordtvedt effect constrain deviations from $\beta = 1$ to high precision under standard PPN assumptions.

The framework needs to either derive $\beta$ from its existing content or adopt it as an additional commitment. This document does the latter, adopting $\beta = 1$ via an informal extension of the redshift exponential, and tracks the commitment as provisional.

---

## Statement of the Identification

**Second-Order Time Metric Identification.** The framework's $g_{00}$ for a spherically symmetric mass, extended from the redshift proof's exponential form to varying gradients in static spherical geometry, takes the form:

$$g_{00} \approx -\exp(2\Phi/c^2)$$

in suitable coordinates. Expanded to second order in $\Phi/c^2$:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2} + 2\frac{\Phi^2}{c^4}\right)$$

Comparing with the PPN form, this gives $\beta = 1$.

Operationally, this means that any framework derivation requiring $g_{00}$ at second order can use the exponential form, and the result will match general relativity's $\beta = 1$ predictions in the weak-field regime.

---

## Why the Identification Is Plausible

The redshift exponential $E(h) = E_0\exp(-gh/c^2)$ was derived for a uniform gradient. If the gradient varies along the path, the natural generalization is to integrate $g \, dh$ along the path:

$$E = E_0 \exp\left(-\int g \, dh / c^2\right)$$

For motion through a static gravitational field, the integral $\int g \, dh$ is the change in gravitational potential $\Delta\Phi$. So the natural generalization is:

$$E = E_0 \exp(-\Delta\Phi/c^2)$$

This is consistent with the redshift proof's content — same exponential structure, with the local gradient replaced by the integrated potential difference.

The corresponding $g_{00}$ component, in coordinates where the proper time of a stationary clock relates to coordinate time through $\sqrt{-g_{00}}$, takes the form $g_{00} = -\exp(2\Phi/c^2)$. This is the metric that produces the redshift exponential when applied to a clock at potential $\Phi$ relative to a reference at $\Phi = 0$.

Expanded to first order: $g_{00} \approx -(1 + 2\Phi/c^2)$, which matches the weak-field metric proof's first-order result.

Expanded to second order: $g_{00} \approx -(1 + 2\Phi/c^2 + 2\Phi^2/c^4)$, which gives $\beta = 1$ in the PPN form.

The identification is plausible because it's the natural extension of the framework's existing redshift content to higher orders. Nothing in the framework currently suggests a different second-order form; the exponential structure is the simplest extension that keeps the first-order result intact.

---

## Why It Is an Identification and Not a Derivation

The argument above is plausible but not rigorous. Several steps are informal:

The redshift exponential was derived for a uniform gradient. Generalizing $\int g \, dh \to \Delta\Phi$ assumes the gradient integrates along the path in the standard way, which is reasonable but not a derived consequence of the framework's postulates.

The identification of the energy ratio $E/E_0$ with $\sqrt{-g_{00}}$ assumes a specific relationship between vacuum-extent variation and the metric's time component. The framework has been careful about this relationship at first order (the weak-field metric proof's machinery), but the second-order extension involves a coordinate choice (which coordinates correspond to the redshift exponential's "height" parameter) that the framework hasn't formally pinned down.

The PPN parameter $\beta$ depends on coordinate conventions. In Schwarzschild coordinates, the second-order term in $g_{00}$ is different from what it is in isotropic coordinates. The identification $\beta = 1$ is specific to PPN-compatible coordinates (the coordinate convention used in the standard PPN expansion), and matching the framework's exponential to those coordinates requires an additional step.

These informalities don't undermine the identification — the result is plausible and matches GR — but they mean the identification is provisional pending a rigorous derivation. This is why the document is labeled a candidate rather than a proof.

---

## What the Identification Gives

With $\beta = 1$ adopted, framework derivations requiring $g_{00}$ at second order can proceed with the exponential form. Specific consequences include:

**Perihelion precession.** The second-order $g_{00}$ contribution to the orbital effective potential combines with the first-order $g_{ij}$ (from unity) to produce the standard GR perihelion advance. The PPN expression $\Delta\varpi \propto (2 + 2\gamma_v - \beta)/3$ gives the GR result with $\gamma_v = \beta = 1$.

**Future post-Newtonian effects.** The Nordtvedt effect (testing whether gravitational binding energy contributes to inertial mass via $\beta$), the second-order Shapiro delay, and other post-Newtonian observables depend on the second-order $g_{00}$ structure. The identification gives the framework a working answer for all of these.

**General-relativistic limit verification.** The exponential form's match to GR's PPN $\beta = 1$ at second order is suggestive rather than guaranteed by the first-order result alone — the second-order coefficient could in principle have differed from the GR value. The fact that the framework's exponential gives the right $\beta$ is consistent with the framework's underlying structure being compatible with GR at higher orders, not just at first order.

---

## What It Does Not Imply

The identification is specifically about the second-order $g_{00}$ term, not about the framework's full strong-field structure.

In the strong-field regime, the framework's exponential form $g_{00} = -\exp(2\Phi/c^2)$ differs from GR's Schwarzschild metric $g_{00} = -(1 - 2GM/rc^2)$. At second order they agree (giving $\beta = 1$); at higher orders they diverge. The redshift proof's discussion of strong-field limits noted this divergence as a place where the framework potentially makes different predictions from GR.

So the identification commits the framework to GR-matching $\beta = 1$ in the weak-field regime but does not commit the framework to Schwarzschild-matching strong-field behavior. The strong-field $g_{00}$ structure remains open, with the framework's exponential providing one specific candidate (which may or may not be the right answer in that regime).

This is parallel to how the unity assumption is a static-case statement that doesn't commit the framework to scalar gravitational waves: the identification controls a specific regime without locking down the framework's full structure.

---

## What Kind of Derivation Would Make This Rigorous

The path to rigorous derivation runs through formalizing how the redshift exponential extends to varying gradients in spherically symmetric geometry. Two pieces of formal content are needed.

First, a formal statement of how the framework's $g \, dh$ relationship in the redshift proof generalizes to integrals along radial paths in static spherical geometry. This is essentially the relationship $\int g \, dh = \Delta\Phi$, but stated within the framework's own machinery rather than imported from standard physics. The connection between the framework's vacuum-extent gradient and the standard gravitational potential needs to be formal at the order required.

Second, a formal statement of which coordinates the exponential form $g_{00} = -\exp(2\Phi/c^2)$ refers to, and how those coordinates relate to standard coordinate choices (Schwarzschild, isotropic, harmonic) used in PPN analyses. The identification $\beta = 1$ is specific to PPN-compatible coordinates; the framework needs to identify its preferred coordinates or to translate between them.

Both pieces are open work. Neither is dramatically out of reach — the framework has the structural commitments to handle them — but they haven't been written out yet.

---

## Relationship to the Unity Assumption

The unity assumption (`candidate_vacuum_variation_unity.md`) closes the spatial-mapping content of the weak-field metric at $\gamma_v = 1$. The second-order time-metric identification (this document) closes the second-order time-mapping content at $\beta = 1$.

The two candidates are independent in their content but parallel in their structural role. Both adopt a provisional commitment that closes a specific underdetermination in the framework's metric content. Both are needed for the framework to reproduce specific GR tests (light deflection, Shapiro delay, perihelion precession). Both should ideally be derived from deeper structure rather than adopted, and both name the derivation as open work.

The two candidates are also independent in their derivation paths. Unity might be derived from the vacuum's mathematical structure or from a symmetry argument at the postulate level. The $\beta = 1$ identification needs the formalization described above. Neither derivation depends on the other; either could be made rigorous independently.

If both are eventually derived, the framework's weak-field metric becomes fully foundational rather than partly provisional, and the proofs that depend on them lose their provisional status.

---

## Warning: Building on the Identification

Derivations that depend on the second-order $g_{00}$ identification inherit its provisional status. Future work should treat the following as provisional closure of otherwise-open questions:

The perihelion precession result, which depends on both $\gamma_v = 1$ and $\beta = 1$.

Any future derivations of post-Newtonian effects involving $g_{00}$ at second order.

Strong-field extrapolations that use the exponential form as a starting point.

If the identification is later refuted or modified, every dependent result needs revisiting. Tracking the dependency explicitly through this candidate is what allows future work to know what's at stake.

---

## Status Summary

**Claim:** The framework's $g_{00}$ for a spherically symmetric mass takes the form $g_{00} \approx -\exp(2\Phi/c^2)$ in suitable coordinates, giving $\beta = 1$ in the PPN expansion.

**Status:** Provisional. The form is plausibly the natural extension of the redshift proof's exponential, but the extension to varying gradients in spherical geometry is informal and the coordinate choice needs formalization.

**Consequences if adopted:** Framework reproduces GR's $\beta = 1$ predictions in the weak field, including perihelion precession, second-order Shapiro delay corrections, and the Nordtvedt-effect bounds.

**What it does not determine:** The framework's strong-field $g_{00}$ structure. The exponential form differs from Schwarzschild beyond second order, and which structure (if either) describes physics in the strong-field regime is open.

**Next work:** Formalize the extension of the redshift exponential from uniform gradients to spherically symmetric potentials, and identify the coordinate convention in which $\beta = 1$ holds.

---

## References

Misner, C. W., Thorne, K. S., & Wheeler, J. A. (1973). *Gravitation*. W. H. Freeman, chapters 39-40 on PPN formalism.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.