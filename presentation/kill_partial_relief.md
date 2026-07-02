# Is Λ just a sliver of relieved frustration?

The most natural-looking route from the packing's frustration to the observed cosmological constant — tried, computed exactly, and killed.

## The kill

The hope was simple and, for a while, attractive: the vacuum's ground state is frustrated (the 7.36-degree deficit around every edge, [idea_frustration.md](idea_frustration.md)); a frustrated packing can shed some of that strain by curving; so let the ground state curve *just enough* to relieve a sliver of the deficit, and call that residual curvature the observed Λ. Λ's value would then be derived, not assumed — a number falling out of geometry.

The relief function is exact and computable (forge 037, resolving kill-condition 036):

```text
cos delta(s) = cos s / (1 + 2 cos s)
```

for a regular tetrahedron of edge arc s = a/L in a space of curvature radius L. Two facts kill the idea outright:

- **The sign is unambiguous.** Spherical curvature relieves the deficit monotonically (closing it exactly at the 600-cell, s = π/5); hyperbolic curvature only ever aggravates it. So *if* the ground state curves to relieve strain, it curves spherically — Λ_ground ≥ 0, conditionally, exactly.
- **The relief has no shoulder.** Near flat space the deficit expands as

```text
Delta(s) = Delta_0 - (5 sqrt(2)/24) s^2 + O(s^4)
```

— quadratic, not linear. There is no scale at which a small curving buys a proportionally small relief. Matching the observed Λ requires relieving a fraction ε ~ 10⁻¹²² of the ground-state deficit, which needs s so small the "relief" is numerical noise; any s large enough to relieve a physically meaningful chunk of the deficit sits within O(1) of the Planck packing scale, where the resulting Λ overshoots the observed value by roughly the same 122 orders in the other direction. There is no intermediate regime to select. The suppression this route would need does not exist anywhere in the geometry — not "small," *absent*.

This is a self-inflicted kill: derivation 036 raised the question, derivation 037 (same house) answered it by exact computation, in one pass, with no free parameter to retune. The surviving branch is coherent and different in kind: a flat ground state (Λ_ground = 0) whose frustration is fully retained but sequestered — gravitationally invisible ([idea_sequestering.md](idea_sequestering.md)) — leaving the observed Λ as the global datum it already was, now cleanly decoupled from the floor rather than explained by it.

**Proof:** forge 037 (`relief_exact_geometry_037`, resolving kill-condition `frustration_relief_suppression_required_036`) → [../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md), verified in `vacuum_forge/src/vacuum_sector/037_relief_exact_geometry/relief_exact_geometry.py`; narrated in [09_the_graveyard.md](09_the_graveyard.md)

**Where next:**
- [What does curving the packing actually cost, exactly? →](thm_relief_geometry.md) — the full exact-geometry derivation this kill is built on, including the 600-cell endpoint and the sign theorem.
- [The cosmological-constant trail →](hub_lambda.md) — where this kill sits alongside sequestering and the integration-constant reading of Λ.
- [The skeptic's entrance →](hub_graveyard.md) — the other mechanisms this program proposed and killed with its own hands.
- [The Frustration →](idea_frustration.md) — the ground-state deficit Δ₀ this relief is measured against.
