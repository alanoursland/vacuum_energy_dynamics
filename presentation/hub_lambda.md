# What is the cosmological constant, in this theory?

A trailhead: Λ is not a coupling to fit — it is an integration constant of a conservation law, and the theory can tell you exactly what it means without being able to tell you its value.

## The trail

**1. The floor exists and doesn't move.** The vacuum's ground state carries
a real energy density — the frustration that five tetrahedra leave
unrelieved (the 7.36° gap, cornered but never closed). That density is
constant by construction: intensive, the same everywhere the packing
sits in its ground configuration. Start at [The Frustration →](idea_frustration.md)
if you haven't met the floor yet, or go straight to the number at
[num_floor_density.md](num_floor_density.md).

**2. Constant density is a constraint, not a free coupling.** P3 (the
unimodular constraint) is read here as an *exact identity*,
$\kappa = \ln(\sqrt{-g}/\sqrt{-\bar g})$: the vacuum's volume mode is
fixed, not dynamical. The microphysics explains why — the packing gives
the volume mode no restoring force. See
[idea_unimodular_constraint.md](idea_unimodular_constraint.md).

**3. Sequestering: the floor cancels out of the dynamics exactly.** A
constant vacuum energy density contributes nothing to the field
equations or to Λ — proven as an action-split identity, not asserted.
See [idea_sequestering.md](idea_sequestering.md) and the theorem itself,
[thm_sequestering.md](thm_sequestering.md).

**4. Λ falls out as a constant of integration.** Under the constrained
variation, the Bianchi identity plus matter conservation give

```text
R + (8*pi*G/c^4)*T = 4*Lambda = const
```

Λ enters the theory here — as the constant fixed by this conservation
law, not as a term hand-placed in the action. The full Einstein
equations with a Λ term reconstruct exactly; nothing in the
field-equation derivation moves. See
[thm_lambda_integration_constant.md](thm_lambda_integration_constant.md).
This also retroactively explains an earlier nine-derivation sweep that
tried six independent local routes to a Λ *mechanism* and found none —
see [kill_lambda_selectors.md](kill_lambda_selectors.md).

**5. What Λ means.** Since $4\Lambda = R + \kappa T$ is a constant of
motion, and the floor's density sequesters out of it, what's left is
$\Lambda = \tfrac14 R_{\text{ground}}$ — the intrinsic curvature of the
vacuum's ground configuration. Λ measures geometry, not energy.

**6. Sign and magnitude: what the packing's geometry says.** The exact
relief function, $\cos\delta(s) = \cos s/(1+2\cos s)$, shows spherical
curvature monotonically relieves the frustration (closing exactly on
the 600-cell) while hyperbolic curvature aggravates it — so *if* the
ground state curved to relieve frustration, it would curve spherically
(Λ ≥ 0). But the relief is quadratic-flat: matching the observed Λ
would relieve only ~$10^{-122}$ of the frustration, while any
meaningful relief overshoots by the same 122 orders the other
direction. No intermediate regime exists — this kills the idea that
Λ's *value* is a partial-relief effect. See
[thm_relief_geometry.md](thm_relief_geometry.md) and
[kill_partial_relief.md](kill_partial_relief.md). The theory's actual
position: a flat ground state (Λ_ground = 0) with its frustration
retained and sequestered.

**7. The value is external, and the theory says so.** The observed Λ
is a genuine global datum — in Henneaux–Teitelboim language, the
variable conjugate to the total four-volume, a boundary condition on
the universe rather than a local quantity. Three independent
structures converge on this (the unimodular constraint, the
sequestering theorem, the relief geometry). The theory owes an account
of every *local* quantity; Λ isn't one. Open, honestly:
[q_lambda_value.md](q_lambda_value.md).

**8. What's still live nearby.** The F1 leak — a matter-era violation
of the unimodular constraint, $AB - 1 = \tfrac32\Omega_m(H_0r/c)^2
\approx 6\times10^{-31}$ at 1 AU — is a derived honesty entry, not a
target. It belongs to the falsifier trail:
[num_kappa_leak.md](num_kappa_leak.md).

**Proof:** forge 033–037 (unimodular break and sequestering; covariant
constraint and F1; floor decoupling; datum-as-curvature; exact relief
function) →
[../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md](../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md).

**Where next:**
- [The microstructure trail →](hub_packing.md) — where the floor's density is actually quantified, cell by cell.
- [The field-equation trail →](hub_einstein.md) — see the Einstein equations Λ sits inside, derived with zero fitted coefficients.
- [The falsifier trail →](hub_predictions.md) — w = −1 and the sequestering edge are live observational commitments downstream of this page.
- [The skeptic's entrance →](hub_graveyard.md) — the full death certificate for the partial-relief idea and the six-route Λ-selector sweep.
