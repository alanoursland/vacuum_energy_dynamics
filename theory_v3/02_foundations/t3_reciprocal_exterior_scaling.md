# T3: Reciprocal Exterior Scaling

## What This Theorem Establishes

In a static, spherically symmetric, source-free exterior vacuum configuration, the temporal mapping and radial spatial mapping are reciprocal.

Using areal-radius coordinates and writing the exterior temporal and radial factors as $A(r)$ and $B(r)$, the theorem establishes

$$A(r)B(r) = 1.$$

Equivalently,

$$B(r) = \frac{1}{A(r)}.$$

In weak-field language, this gives the framework's analogue of the PPN result

$$\gamma = 1.$$

This is the missing relation needed to recover the standard weak-field spatial response of general relativity. T1 and T2 establish the temporal side of weak-field gravity; T3 supplies the reciprocal radial-spatial side.

---

## The Setup

Consider a static, spherically symmetric exterior vacuum configuration around a single localized constraint.

The assumptions are:

1. **Staticity:** the configuration is unchanging in time.
2. **Spherical symmetry:** the configuration depends only on radial distance from the source.
3. **Exterior region:** the theorem applies outside the matter source or localized constraint.
4. **Source-free vacuum:** the exterior region contains no matter source of its own.
5. **No net vacuum substance exchange:** the static exterior configuration is not undergoing net vacuum creation or destruction.
6. **Areal-radius convention:** the radial coordinate $r$ is chosen so that spheres at radius $r$ have area $4\pi r^2$.
7. **Asymptotic flatness:** far from the source, the vacuum approaches its flat configuration.

The areal-radius convention fixes the angular part of the spherical geometry. It does not follow from spherical symmetry alone. Spherical symmetry says the angular directions are equivalent; the areal-radius coordinate choice says their area is represented by $4\pi r^2$.

The remaining exterior directional freedom is therefore captured by two radial functions:

- a temporal mapping factor $A(r)$,
- a radial spatial mapping factor $B(r)$.

Both approach $1$ at infinity:

$$A(r) \to 1, \qquad B(r) \to 1$$

as

$$r \to \infty.$$

---

## Convention Note

There are two common ways to use $A(r)$ and $B(r)$.

One can define them as **metric coefficients**, as in

$$ds^2 = -A(r)c^2dt^2 + B(r)dr^2 + r^2d\Omega^2.$$

In that convention, the Schwarzschild exterior has

$$A(r) = 1 - \frac{2GM}{rc^2},$$

$$B(r) = \left(1 - \frac{2GM}{rc^2}\right)^{-1},$$

so

$$A(r)B(r) = 1.$$

Alternatively, one can define $A(r)$ and $B(r)$ as **observer-to-observer mapping factors** between proper and coordinate intervals. Depending on whether the mapping is defined from proper-to-coordinate or coordinate-to-proper, reciprocal factors may appear inverted.

This theorem uses $A(r)$ and $B(r)$ in the metric-coefficient sense unless otherwise stated. The invariant content is not the naming convention. The invariant content is reciprocal temporal-radial scaling.

---

## The Postulate Used

This theorem depends on P7: Static Exterior Vacuum Compensation.

P7 states that in a static, source-free exterior vacuum configuration undergoing no net vacuum substance creation or destruction, curvature is compensated directional redistribution of vacuum extent. The local temporal-radial vacuum measure is preserved.

In the static spherically symmetric exterior case, P7 says

$$A(r)B(r) = \text{constant}.$$

T3 applies that postulate to the exterior spherical setup and fixes the constant using asymptotic flatness.

---

## The Derivation

By P7, the static source-free exterior configuration is a configuration-regime structure, not a substance-regime exchange process.

That means the exterior curvature represents directional redistribution of vacuum extent. Temporal and radial spatial mappings may vary with radius, but the local temporal-radial vacuum measure is preserved.

In areal-radius coordinates, the angular sector has already been fixed. The remaining compensation condition applies to the temporal and radial factors.

Therefore,

$$A(r)B(r) = C$$

for some constant $C$.

Equivalently,

$$\frac{d}{dr}(A(r)B(r)) = 0.$$

Writing this in logarithmic form,

$$\frac{d}{dr}\ln(A(r)B(r)) = 0,$$

which gives

$$\frac{A'(r)}{A(r)} + \frac{B'(r)}{B(r)} = 0.$$

Thus the product $A(r)B(r)$ is independent of radius.

Now impose asymptotic flatness. Far from the source, the exterior vacuum approaches the flat Minkowski configuration. Therefore,

$$A(r) \to 1,$$

and

$$B(r) \to 1$$

as

$$r \to \infty.$$

So the constant is

$$C = 1.$$

Therefore,

$$A(r)B(r) = 1.$$

This is the reciprocal exterior scaling relation.

---

## Weak-Field Form

In the weak-field limit, the temporal coefficient can be written in terms of the Newtonian gravitational potential $\Phi(r)$, where $\Phi < 0$ near an attractive mass and $\Phi \to 0$ at infinity.

The standard weak-field temporal coefficient is

$$A(r) \approx 1 + \frac{2\Phi(r)}{c^2}.$$

Since T3 gives

$$B(r) = \frac{1}{A(r)},$$

we have

$$B(r) \approx \left(1 + \frac{2\Phi(r)}{c^2}\right)^{-1}.$$

To first order in $\Phi/c^2$,

$$B(r) \approx 1 - \frac{2\Phi(r)}{c^2}.$$

Since $\Phi < 0$, this means $B(r) > 1$ near an attractive mass.

For a point mass,

$$\Phi(r) = -\frac{GM}{r},$$

so

$$A(r) \approx 1 - \frac{2GM}{rc^2},$$

and

$$B(r) \approx 1 + \frac{2GM}{rc^2}.$$

This is the standard weak-field Schwarzschild form.

---

## Relation to $\gamma = 1$

In the parametrized post-Newtonian weak-field form, the spatial part of the metric is commonly written with a parameter $\gamma$ that measures the amount of spatial curvature produced per unit gravitational potential.

In a simplified radial comparison, the weak-field coefficients take the form

$$g_{tt} \approx -\left(1 + \frac{2\Phi}{c^2}\right),$$

and

$$g_{rr} \approx 1 - \frac{2\gamma\Phi}{c^2}.$$

T3 gives

$$g_{rr} \approx 1 - \frac{2\Phi}{c^2}.$$

Therefore,

$$\gamma = 1.$$

This is the same value predicted by general relativity.

The result is important because several weak-field gravitational tests depend on $\gamma$, including:

- light deflection,
- Shapiro delay,
- perihelion precession.

T3 therefore supplies the missing spatial-response condition needed for the framework's weak-field GR recovery program.

The PPN parameter $\gamma$ is the framework-external observational anchor for what T3 establishes. Solar-system measurements (Cassini, VLBI, lunar laser ranging) constrain $\gamma$ to be $1$ within parts in $10^5$. T3's prediction of $\gamma = 1$ is therefore consistent with all current observations to high precision, conditional on P7's structural commitment.

---

## Relationship to T1 and T2

T1 establishes gravitational redshift in the weak-field limit:

$$\frac{\Delta E}{E} \approx -\frac{gh}{c^2}.$$

T2 uses T1 to establish gravitational time dilation:

$$\tau_A^{(B)} \approx \tau\left(1 + \frac{gh}{c^2}\right).$$

Together, T1 and T2 establish the temporal mapping between observers at different positions in a curvature gradient.

But temporal mapping alone does not determine radial spatial mapping. A theory can reproduce gravitational redshift and time dilation while still failing to reproduce the full weak-field spatial structure of GR.

T3 supplies the missing radial relation. It says that in the static source-free exterior case, the radial spatial mapping is not independent of the temporal mapping. The two are reciprocally related by exterior compensation.

Thus:

- T1 gives photon energy shift.
- T2 gives clock-rate mapping.
- T3 gives reciprocal radial spatial mapping.

Together, they recover the weak-field Schwarzschild temporal-radial structure.

---

## Relationship to General Relativity

In standard general relativity, the Schwarzschild exterior solution begins with the static spherically symmetric metric

$$ds^2 = -A(r)c^2dt^2 + B(r)dr^2 + r^2d\Omega^2.$$

The vacuum Einstein equations imply

$$\frac{A'}{A} + \frac{B'}{B} = 0.$$

Therefore,

$$A(r)B(r) = \text{constant}.$$

Asymptotic flatness fixes the constant to $1$, giving

$$A(r)B(r) = 1.$$

T3 reaches the same relation through different conceptual machinery.

GR obtains the relation from the source-free Einstein field equations.

This framework obtains the relation from P7: static exterior vacuum compensation.

The mathematical role is parallel. P7 is not the full Einstein equation, but in the static spherically symmetric exterior case it supplies the specific source-free condition needed to recover the reciprocal temporal-radial relation.

---

## What This Theorem Does Not Establish

T3 does not derive the full Schwarzschild solution.

It establishes

$$A(r)B(r) = 1.$$

It does not, by itself, derive

$$A(r) = 1 - \frac{2GM}{rc^2}.$$

That requires a source law connecting the localized mass-energy constraint to the radial gradient profile.

T3 also does not establish strong-field agreement with GR. The reciprocal relation may hold exactly under P7's assumptions, but the strong-field form of $A(r)$ still depends on the framework's future source law and configuration-energy functional.

T3 does not apply to cosmology. Cosmic expansion is not static exterior compensation; it is a substance-regime process involving vacuum/spacetime creation.

T3 does not apply inside matter. The theorem is exterior and source-free.

T3 does not apply automatically to rotating, time-dependent, radiating, or nonspherical configurations.

T3 does not derive P7. It depends on P7. P7 is a structural postulate adopted as a node in the framework's search over possible postulate sets, motivated by the configuration/substance distinction but not derived from P1–P6. P7 functions as a design constraint for any future field equations the framework develops: those equations would need to reproduce P7's compensation condition in the static source-free exterior limit. If P7 is later derived from a deeper postulate or from a more complete configuration-energy functional, T3 becomes downstream of that deeper structure. Until then, T3 is unconditional only relative to P7.

---

## Status of the Result

T3 is a theorem conditional on P7.

Given:

- staticity,
- spherical symmetry,
- exterior source-free vacuum,
- no net vacuum substance exchange,
- areal-radius coordinates,
- asymptotic flatness,
- and P7's compensation principle,

the result follows:

$$A(r)B(r) = 1.$$

In the weak-field limit, this gives

$$\gamma = 1.$$

This closes the specific gap left by the earlier version of the framework: the failure to derive reciprocal temporal-radial scaling. The earlier version adopted this condition globally and vaguely as a unity assumption with no precise localization. T3 derives the condition from P7's specific structural commitment, with the conditional status now precisely identified rather than hidden.

---

## Imports and Dependencies

This theorem invokes:

- SR1: Lorentz Invariance, as part of the local consistency structure of the framework.
- SR3: Spacetime Interval and Minkowski Structure, for asymptotic flatness and the flat exterior limit.
- SR9: Local Validity of SR in Inertial Frames, for the interpretation of local measurements.

It depends on:

- P1: Vacuum-Energy Equivalence
- P2: Vacuum-Spacetime Identity
- P3: Vacuum Energy Density
- P3a: Spatial Differential is Curvature
- P4: Curvature Contains Energy
- P5: Vacuum Seeks Minimum Energy Configuration
- P7: Static Exterior Vacuum Compensation
- T1: Gravitational Redshift
- T2: Gravitational Time Dilation

The direct dependency is P7. The earlier postulates provide the ontology and motivation for P7. T1 and T2 supply the temporal-side weak-field mappings that the radial-side mapping derived here completes.

---

## Summary

T3 establishes reciprocal temporal-radial scaling in a static, spherically symmetric, source-free exterior vacuum configuration.

By P7, the static exterior curvature is compensated directional redistribution rather than net vacuum substance exchange. Therefore the temporal and radial factors satisfy

$$A(r)B(r) = \text{constant}.$$

Asymptotic flatness fixes the constant to $1$:

$$A(r)B(r) = 1.$$

In weak-field form, this gives the framework's analogue of

$$\gamma = 1.$$

T3 therefore supplies the missing spatial-response condition needed for weak-field recovery of general relativity. Together with T1 and T2, it establishes the framework's temporal-radial weak-field structure, with the conditional status carried by P7's structural commitment about static source-free exterior configurations.
