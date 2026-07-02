# What does curving the packing actually cost, exactly?

The dihedral angle around a shared edge as a function of curvature, computed exactly in S^3 and H^3 — the geometry that kills the partial-relief route to Lambda.

## The theorem

Take a regular tetrahedron with edge arc length s = a/L, sitting in a space of constant curvature radius L (S^3 for s real and positive, H^3 by analytic continuation). Two applications of the spherical law of cosines give the dihedral angle at any edge as an exact closed form in s alone:

```text
cos delta(s) = cos s / (1 + 2 cos s)
```

This is the whole relief geometry — one function, no approximation. Its endpoints are exact: delta(0) = arccos(1/3), the flat-space dihedral that leaves the familiar 7.36-degree gap at five-around-an-edge; and delta(pi/5) = 2*pi/5, the point at which the deficit closes exactly and five tetrahedra tile a hinge perfectly — that configuration is the 600-cell.

Differentiate once and the sign is unambiguous for the entire spherical branch:

```text
d(cos delta)/ds = -sin s / (1 + 2 cos s)^2 < 0   for all s in (0, pi/5)
```

cos delta decreases monotonically, meaning delta itself increases monotonically, meaning the deficit Delta(s) = 2*pi - 5*delta(s) decreases monotonically as s grows. Spherical curvature relieves frustration, everywhere on the branch, with no local extrema to complicate the story. Continue s to imaginary values (hyperbolic curvature) and the sign flips just as cleanly: cos delta_H = cosh s / (1 + 2 cosh s) > 1/3 for every s > 0, so hyperbolic curvature only ever aggravates the deficit. There is no ambiguity in which direction relief lives — the 036 sign question is answered exactly, at every scale, in both regimes.

The part that kills the value-route is the small-s behavior. Expand near flat:

```text
Delta(s) = Delta_0 - (5*sqrt(2)/24)*s^2 + O(s^4)
```

The correction is quadratic, not linear — there is no regime where a small curving buys a proportionally small relief. To relieve a fraction epsilon of Delta_0 costs s^2 ~ epsilon, so relieving the sliver of frustration needed to match the observed Lambda (epsilon ~ 1e-122 at Planck packing scale) requires s so small the "relief" is a strict rounding error, while any s large enough to relieve a physically meaningful fraction of Delta_0 sits within O(1) of the packing scale itself — where the resulting Lambda overshoots the observed value by roughly the same 122 orders of magnitude in the other direction. The function has no shoulder: it is flat to quadratic order at s=0 and essentially done relieving anything by the time s leaves the Planck neighborhood. No intermediate regime exists to select.

**Proof:** derivation 037 (`relief_exact_geometry_037`, resolving kill-condition `frustration_relief_suppression_required_036` by exact computation, verified in `vacuum_forge/src/vacuum_sector/037_relief_exact_geometry/relief_exact_geometry.py`) → [../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md)

**Where next:**
- [The skeptic's entrance →](hub_graveyard.md) — the death certificate this theorem writes: partial relief as a route to Lambda's *value* is dead, permanently.
- [The cosmological-constant trail →](hub_lambda.md) — where this result sits in the larger Lambda story, alongside sequestering and the integration-constant reading.
- [Lambda Is an Integration Constant →](thm_lambda_integration_constant.md) — the surviving mechanism this theorem clears the way for: Lambda as global datum, not local geometry.
- [The Frustration →](idea_frustration.md) — the ground-state deficit Delta_0 this function is measured relative to, and why it's irreducible in flat space to begin with.
