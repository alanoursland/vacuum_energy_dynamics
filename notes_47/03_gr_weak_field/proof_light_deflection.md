# Proof: Gravitational Light Deflection

---

## What This Document Is

This is the framework's fourth derivation. It computes the angular deflection of a light ray passing near a mass in the weak-field regime, giving $\Delta\theta = 4GM/bc^2$ for a ray with impact parameter $b$ past a mass $M$. This matches general relativity's prediction, Eddington's 1919 solar-eclipse measurement, and the broad body of subsequent optical and radio observations of gravitational deflection.

The derivation inherits the weak-field metric proof's machinery, including the provisional closure of that metric at $\gamma_v = 1$ via the unity assumption. Without the unity assumption, the framework produces $\Delta\theta = (1 + \gamma_v)(2GM/bc^2)$ with $\gamma_v$ undetermined. With unity adopted, $\gamma_v = 1$ and the deflection becomes the full GR value.

The framework's contribution to this well-tested result is specifically about the structure of the answer. The factor of two that distinguishes the correct deflection from Einstein's 1911 prediction — which used the equivalence principle alone and gave only half the value — is exactly the contribution of the spatial part of the metric. In framework-native terms, it is the contribution of the spatial-mapping effect on top of the time-mapping effect. The unity assumption supplies this contribution by committing to $\gamma_v = 1$.

---

## Provisional Status

This proof depends on the unity assumption from `candidate_vacuum_variation_unity.md`, which is adopted provisionally rather than derived from the framework's postulates. Specifically, the derivation below produces the parameterized result $\Delta\theta = (1 + \gamma_v)(2GM/bc^2)$, and the closure to the observed $4GM/bc^2$ requires setting $\gamma_v = 1$ via unity.

Until the unity assumption is derived from deeper structural commitments, this proof's agreement with observation is a consistency check rather than an independent prediction. If unity is later refuted or requires modification, this derivation becomes invalid and its result needs revisiting.

Any future result that builds on this proof — or on any component of the weak-field metric with unity adopted — inherits the same provisional status. Readers encountering chains of derivations should track this dependency explicitly.

---

## The Historical Factor of Two

Einstein predicted gravitational light deflection twice. His 1911 calculation, based on the equivalence principle alone, gave a deflection of $2GM/bc^2$ for light grazing the Sun — about 0.87 arcseconds. His 1915 calculation, using the full machinery of general relativity, gave $4GM/bc^2$ — about 1.75 arcseconds. The 1919 solar-eclipse expedition measured deflection consistent with the 1915 value, not the 1911 value.

The difference is not arithmetic error. The 1911 calculation correctly captured the effect of gravitational time dilation on light propagation but did not include the contribution of spatial curvature. In modern metric language, the 1911 result uses $g_{00}$ alone; the 1915 result uses both $g_{00}$ and $g_{ij}$. The factor of two between them comes from the spatial components contributing an amount equal to the temporal contribution.

In the framework's vocabulary, this corresponds to the $(1 + \gamma_v)$ factor that appears in the weak-field deflection formula. Setting $\gamma_v = 0$ recovers Einstein's 1911 half-deflection; setting $\gamma_v = 1$ recovers his 1915 full deflection. Observations pin $\gamma_v = 1$ to parts in $10^5$. The unity assumption commits the framework to this value.

This historical arc is useful for the document because it identifies where the unity assumption's content is doing observable work. Time dilation and redshift would not have distinguished between $\gamma_v = 0$ and $\gamma_v = 1$. Light deflection does. The framework's derivation of the full $4GM/bc^2$ is its first derivation that uses the spatial part of the metric non-trivially.

---

## The Setup

The framework's weak-field metric, with the unity assumption adopted, has components:

$$g_{00} \approx -\left(1 + \frac{2\Phi}{c^2}\right), \quad g_{ij} \approx \left(1 - \frac{2\Phi}{c^2}\right) \delta_{ij}$$

where $\Phi = -GM/r$ is the Newtonian gravitational potential for a point mass $M$. Consider a light ray propagating past this mass at impact parameter $b$, where $b$ is the closest coordinate distance the ray would have reached if it traveled in a straight line.

A light ray is a null geodesic: a path through spacetime along which $ds^2 = 0$ at every point, and which extremizes the integral of $ds$ along its length. For a light ray, this means the ray's trajectory is determined by the metric's structure through the null condition plus the extremization.

In the weak-field regime, the ray's path is nearly straight and its deflection is small. The framework can compute the deflection by treating the curvature of the path as a perturbation of the straight-line trajectory the ray would follow in flat space.

---

## The Derivation

For a light ray propagating in the weak-field metric, the deflection can be computed by integrating the effective gradient of the gravitational potential along the ray's path. The calculation is standard; the key observation is how the metric components enter.

The null condition for a light ray in the weak-field metric gives:

$$0 = -\left(1 + \frac{2\Phi}{c^2}\right) c^2 \, dt^2 + \left(1 - \frac{2\Phi}{c^2}\right) d\vec{x}^2$$

to first order in $\Phi/c^2$. Solving for the coordinate speed of light:

$$\left(\frac{d\vec{x}}{dt}\right)^2 = \frac{1 + 2\Phi/c^2}{1 - 2\Phi/c^2} c^2 \approx c^2 \left(1 + \frac{4\Phi}{c^2}\right)$$

The coordinate speed differs from $c$ by a factor that depends on $(1 + \gamma_v) \cdot 2\Phi/c^2 = 4\Phi/c^2$ with $\gamma_v = 1$. This is the two-part contribution: $2\Phi/c^2$ from $g_{00}$ and $2\Phi/c^2$ from $g_{ij}$, summing because both shift the effective speed in the same direction.

For a light ray with impact parameter $b$, the deflection angle is the integrated transverse gradient of this effective speed along the ray's path. At first order, the transverse acceleration of the ray is governed by the transverse gradient of the effective optical potential $(1 + \gamma_v)\Phi$, giving the standard weak-field lensing integral along the unperturbed straight-line trajectory:

$$\Delta\theta = \frac{1}{c^2} \int_{-\infty}^{+\infty} \frac{\partial}{\partial b} \left[(1 + \gamma_v) \Phi\right] dl$$

where $l$ is the coordinate along the unperturbed ray and $b$ is the impact parameter. Substituting $\Phi = -GM/\sqrt{l^2 + b^2}$:

$$\frac{\partial \Phi}{\partial b} = \frac{GM \, b}{(l^2 + b^2)^{3/2}}$$

and the integral evaluates to:

$$\int_{-\infty}^{+\infty} \frac{GM \, b}{(l^2 + b^2)^{3/2}} \, dl = \frac{2GM}{b}$$

Therefore:

$$\Delta\theta = (1 + \gamma_v) \frac{2GM}{bc^2}$$

With $\gamma_v = 1$ from the unity assumption:

$$\Delta\theta = \frac{4GM}{bc^2}$$

For light grazing the Sun ($M = M_\odot$, $b = R_\odot$), this gives $\Delta\theta \approx 1.75$ arcseconds, the value Eddington's expedition confirmed in 1919.

---

## Where the Factor of Two Comes From

The derivation makes explicit that the $4GM/bc^2$ result is built from two equal contributions of $2GM/bc^2$ each.

The first contribution comes from $g_{00}$ — the time-mapping effect. This is the contribution Einstein had in 1911. It arises from the fact that clocks run slower in gravitational wells (or in the framework's language: the time-mapping between distant and local observers depends on vacuum depletion), which causes light to appear to propagate more slowly through the coordinate region near the mass. A ray passing near the mass bends in response to this apparent speed difference.

The second contribution comes from $g_{ij}$ — the spatial-mapping effect. This is the contribution Einstein added in 1915. It arises from the fact that proper spatial distances near the mass are longer than coordinate distances (or in the framework's language: the spatial-mapping between distant and local observers depends on vacuum depletion), which further increases the apparent time for light to traverse the region near the mass. A ray bends additionally in response to this spatial effect.

Both contributions are present in the framework because the weak-field metric has both $g_{00}$ and $g_{ij}$ components. The ratio between them is controlled by $\gamma_v$. The unity assumption commits $\gamma_v = 1$, which makes the two contributions equal in magnitude, which produces the factor of two.

In the framework's vocabulary: the spatial-mapping effect is not an independent phenomenon separate from the time-mapping effect. Both arise from the same underlying fact of vacuum-per-coordinate-span variation in the region near the mass. The unity assumption says that variation affects time and space through a single coupling. Light bending is where this single coupling produces an observable factor of two.

---

## Reconciliation with the Active-Exchange Picture

A reader familiar with the gravitational redshift proof may notice a tension. The redshift proof committed to an active-exchange account of photon behavior in gradients: photons ascending lose energy by regenerating vacuum, photons descending gain energy by consuming vacuum. The present derivation, in contrast, treats the photon as a null geodesic in a metric — a test particle responding to geometric structure, with no explicit vacuum-exchange mechanism invoked.

These are the same phenomenon described from different angles, not two competing pictures. Under Postulate 1, the metric is bookkeeping for vacuum configuration. A null geodesic in the metric is the path along which a photon's local propagation remains at $c$ through vacuum of varying extent. The curve of the path is the metric-level representation of the accumulated vacuum-exchange effects on the photon's trajectory: the photon's momentum along the gradient changes on each side of the mass because the vacuum-per-coordinate-span differs on each side, and Postulate 3's force-per-unit-energy is acting on the photon throughout its traversal. The framework interprets the geodesic path as what this accumulated vacuum exchange produces, though the exact equivalence between a local two-dimensional vacuum-exchange force law and the metric's geodesic equation has not been independently derived — it is a consistency the framework expects rather than a result it has proved.

The $(1 + \gamma_v)$ factor admits a corresponding decomposition in the active-exchange language. The $g_{00}$ contribution corresponds to the force-per-unit-energy acting on the photon through the time-mapping gradient — Postulate 3's force applied to the photon's energy per mass-energy equivalence (from SR). The $g_{ij}$ contribution corresponds to the photon traversing proper distances that differ from coordinate distances — the spatial mapping shaping which paths correspond to null propagation. Both are effects of vacuum-per-coordinate-span variation on the photon's trajectory, aggregated by the metric into a single geodesic equation.

The metric machinery is therefore not a replacement for the active-exchange account but a mathematical aggregation of it. Where the redshift proof makes the exchange visible by isolating a single dimension (vertical propagation), the light-deflection calculation makes it less visible by aggregating multiple dimensions into a geodesic equation. What looks like "photon follows pre-optimized path" in metric language is "photon's vacuum exchange in two dimensions summed into a trajectory" in framework-native language. The framework has one account of photon behavior, stated in two mathematically equivalent ways for different computational convenience.

---

## Observational Tests

Gravitational light deflection has been measured with increasing precision since 1919.

Eddington's 1919 solar-eclipse expedition measured deflection consistent with the $4GM/bc^2$ value at precision of roughly 30 percent. Subsequent solar-eclipse observations through the twentieth century improved this to a few percent.

Radio interferometry measurements of quasar positions during solar occultations give precision at the $10^{-4}$ level, constraining $\gamma_v$ (or the PPN parameter $\gamma$) to be $1$ within that precision. The most precise of these come from very-long-baseline interferometry measurements.

The Cassini spacecraft's radio tracking experiment in 2002, conducted during its solar conjunction, measured $\gamma = 1 + (2.1 \pm 2.3) \times 10^{-5}$, pinning $\gamma_v = 1$ to roughly two parts in $10^5$. This is currently the tightest single-system constraint.

Gravitational lensing at galactic and cluster scales tests the framework in different regimes. At these scales, the weak-field approximation is usually still adequate, but the lensing masses are much larger and the impact parameters are much larger, probing the framework at different $GM/bc^2$ values than solar-system tests. Observations are consistent with the weak-field prediction throughout.

The framework reproduces all of these results through its weak-field metric, given unity.

---

## Scope and Limitations

The derivation is valid in the weak-field limit, where $GM/bc^2 \ll 1$. This covers solar-system deflection tests and many astrophysical lensing situations where the gravitational potentials along the ray's path are small. Strong-lensing configurations that produce multiple images and caustics require a more complete lensing treatment even when the local gravitational potential remains weak, because the non-perturbative geometry of the lensing situation is not captured by a first-order deflection formula applied along a single straight-line path.

For strong gravitational fields — light deflection near compact objects, photon capture, and near-horizon lensing — the weak-field derivation does not apply. The framework would need a strong-field treatment, which depends on deriving the $\rho_v$ profile around a mass beyond the weak-field limit. This is currently open. Multiple-image strong lensing by galaxies or clusters may still occur in weak local fields, but requires a full lens-equation treatment rather than a single first-order deflection along one straight-line path; this is a geometric limitation of the present calculation, not a strong-field regime.

The derivation inherits the provisional status of the unity assumption. The $\gamma_v = 1$ closure is not derived from the framework's postulates; it is an additional commitment that matches observation. If unity is later shown to be wrong or to require modification, this derivation would need to be revisited. Specifically, a framework that ended up with $\gamma_v \neq 1$ would predict deflection angles different from the observed $4GM/bc^2$, in direct conflict with precision solar-system tests.

The derivation also depends on the whole chain of framework results that the weak-field metric rests on: the redshift proof, the time dilation proof, and the associated postulates. Any revision of these would propagate to the light deflection result.

---

## Dependency Structure

This proof inherits the dependencies of the weak-field metric proof: Postulates 1, 2, and 3, mass-energy equivalence, the curvature-as-spatial-volume-differential consequence, the redshift proof, the time dilation proof, and special relativity. It additionally depends on the unity assumption from `candidate_vacuum_variation_unity.md`, which closes the metric at $\gamma_v = 1$.

The derivation does not invoke Postulates 4 or 5. The light deflection result, like the earlier proofs in this subframework, is insulated from the framework's configuration-energy and minimum-energy-dynamics machinery.

Because the derivation depends on unity, it inherits unity's provisional status. If unity is later derived from deeper structure, this proof's status becomes unconditional. If unity is refuted, this proof becomes invalid and the framework must explain why observation appears to support $\gamma_v = 1$.

---

## What This Proof Accomplishes

As a derivation, the proof reproduces the standard weak-field gravitational deflection result $4GM/bc^2$ from the framework's existing content plus the unity assumption. This adds a second quantitative weak-field contact point to the framework, joining redshift/time dilation. Separately, the framework has qualitative contact with gravitational-wave existence and energy transport.

As a demonstration, the proof is the framework's first that depends on the spatial components of the metric in a non-trivial way. Redshift and time dilation probe $g_{00}$ only; this proof's factor-of-two content depends on both $g_{00}$ and $g_{ij}$. The unity assumption's observational consequence — the factor of two in the deflection — becomes explicit here in a way it was not in the earlier proofs.

As a consistency check, the proof confirms that the framework's metric machinery, combined with unity, reproduces the correct deflection. Because unity was adopted in part because $\gamma_v = 1$ is what observation requires, this is not an independent test of unity. It is a consistency check that the framework's machinery is being used correctly: if the machinery did not produce $4GM/bc^2$ given unity, something would be wrong internally.

The derivation does not show the framework is superior to GR. It shows that the framework, with unity adopted, reproduces GR's weak-field light deflection result through vacuum-exchange machinery and gives a framework-native physical account of what is happening. Whether that account is correct — whether vacuum-per-coordinate-span variation is literally what produces the deflection — remains open to further work.

### Summary of Result

Current framework result:

$$\Delta\theta = (1 + \gamma_v) \frac{2GM}{bc^2}$$

With unity adopted ($\gamma_v = 1$):

$$\Delta\theta = \frac{4GM}{bc^2}$$

For light grazing the Sun: $\Delta\theta \approx 1.75$ arcseconds.

Observational status: matches Eddington 1919 and the broad body of subsequent solar-system and cosmological deflection measurements.

Dependency status: inherits the weak-field metric proof's dependencies plus the unity assumption. Provisional until unity is derived or refuted.

---

## References

Bertotti, B., Iess, L., & Tortora, P. (2003). A test of general relativity using radio links with the Cassini spacecraft. *Nature*, 425(6956), 374–376.

Dyson, F. W., Eddington, A. S., & Davidson, C. (1920). A determination of the deflection of light by the Sun's gravitational field, from observations made at the total eclipse of May 29, 1919. *Philosophical Transactions of the Royal Society A*, 220, 291–333.

Einstein, A. (1911). Über den Einfluß der Schwerkraft auf die Ausbreitung des Lichtes [On the influence of gravity on the propagation of light]. *Annalen der Physik*, 340(10), 898–908.

Einstein, A. (1915). Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie [Explanation of the perihelion motion of Mercury from the general theory of relativity]. *Sitzungsberichte der Preußischen Akademie der Wissenschaften*, 831–839.

Shapiro, S. S., Davis, J. L., Lebach, D. E., & Gregory, J. S. (2004). Measurement of the solar gravitational deflection of radio waves using geodetic very-long-baseline interferometry data, 1979–1999. *Physical Review Letters*, 92(12), 121101.

Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17(1), 4.