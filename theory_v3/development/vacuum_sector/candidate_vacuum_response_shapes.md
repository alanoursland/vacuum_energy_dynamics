# Candidate Vacuum-Response Shapes

## Status

```text
result type:   exploration / candidate shapes, not gated, not adopted
scope:         possible functional forms for the vacuum response and K_strain
conclusion:    none — this note proposes shapes and their kill conditions
non-conclusion: nothing here is licensed; no shape has passed a gate
```

This is a working note, not a claim. It proposes structurally motivated
candidate shapes for the vacuum response and routes each into the program's
existing discipline (the master proof-state machine in
[proposed_roadmap.md](proposed_roadmap.md)). Every shape below must pass the X
contract, neighboring-mismatch contract, boundary variation, conservation
identity, mode/principal-symbol check, weak-field face, and source-ledger check
before it is anything more than an analogy.

The closed result is not reopened. Everything here either lives inside a term
the closed theory already permits (`Lambda`), inside the not-yet-specified
`K_strain` residual, or inside the `X -> g` constitutive map — never in the
admitted `<= 4`-derivative metric response.

## Organizing Idea: The Response As Incompressible Elasticity

The reduced variables are already the elastician's variables. The log-scale
split

```text
kappa = (1/2) ln(AB)   volumetric (trace) strain
s     = (1/2) ln(A/B)  deviatoric (shear) strain
```

is the standard decomposition of the **Hencky (logarithmic) strain** into a
volumetric and an isochoric part. That the theory lands on a logarithmic strain
measure (`A = e^s`) rather than a Green-Lagrange measure is itself a
constitutive hint: log strain composes multiplicatively, the same
multiplicativity the demoted-P8 temporal-composition theorem needed.

Under this reading the postulates become material properties:

```text
P3 (constant energy density)  ~ incompressibility (infinite bulk modulus)
                              -> volumetric/trace mode frozen
P7' (static frame indifference) ~ AB = 1, the saturated volume constraint
                              -> kappa = 0 in statics
shear modulus sector          -> static Newtonian s AND the two TT gravitons
```

So gravity is the **deviatoric (shape-changing) response at constant volume**:
"gravity changes the configuration, not the amount" becomes "isochoric strain."
`K_EH/GHY` is then the quadratic isotropic strain energy at the one modulus
ratio (Fierz-Pauli / Lovelock-tuned) that keeps the trace mode non-ghost. This
reframes the central question:

```text
"why epsilon = 0 / why EH-GHY?"  ==  "why the Fierz-Pauli modulus ratio?"
```

and the theory already answered the latter with the negative-scalar-sector
ghost argument (G02/G03) plus P7'. This is the same content as **Lovelock's
theorem**: in 4D the only local, second-order, divergence-free symmetric
2-tensor from the metric is `alpha G_ab + beta g_ab`. Roadmap routes 1A/1B are
physics-motivated re-derivations of Lovelock; this note recommends invoking
Lovelock explicitly to close the `<= 2`-derivative branch in one move, after
which the only routes to `epsilon != 0` are to break a Lovelock hypothesis.

## Lovelock's Hypotheses And Their Breakability

```text
A. built from the metric alone (no extra field / no independent connection)
B. at most second order in derivatives
C. divergence-free (full diffeomorphism invariance)
D. symmetric rank-2
E. local
F. four-dimensional
```

| hypothesis | breaking it gives | VED disposition |
|---|---|---|
| B second-order | f(R), higher-curvature | already gated off (ghosts + P7'); the dead end |
| A metric-only | Palatini / torsion / nonmetricity | roadmap 1B; collapses to Levi-Civita unless substance motivates extra structure |
| E locality | nonlocal gravity | chartered (2E); IR/Lambda only if local leakage vanishes |
| F D = 4 | Lovelock/Gauss-Bonnet dynamical | not a free cheat; we live in 4D |
| **C divergence-free** | **unimodular, aether, foliation-preserving** | **arguably already broken by P3 (see below)** |

## Shape 1 — Unimodular Structure From P3 (candidate *result*, not just shape)

**Claim shape.** P3 (constant energy density) constrains the volume form
`sqrt(-g)`, which is the defining move of **unimodular gravity**. Varying under
that constraint yields the **trace-free** Einstein equations, and `Lambda`
re-emerges as a **constant of integration** fixed by global/boundary data
rather than a Lagrangian coupling.

**Why this is more than analogy.** Two of the program's most robust findings
are the fingerprint of unimodular gravity:

```text
frozen trace mode (kappa constraint-like; G02/G03; P7')
  == unimodular removal of the volumetric mode from the dynamics

Lambda allowed but unvalued by the local equation; needs a global / boundary /
measure selector (the entire 008-016 Lambda sweep)
  == Lambda as a unimodular integration constant, set by boundary data
```

A third unimodular property is the escape hatch every floor mechanism needs:

```text
a constant added to the Lagrangian does not gravitate in unimodular gravity
  -> the absolute frustration floor decouples; only the integration constant
     Lambda gravitates
```

**Disposition.** If the correspondence holds it is a result, not a candidate:
it would explain the `Lambda`-baseline sweep's "unvalued by local equation"
conclusion in one structural stroke. It belongs in `04_lambda_baseline/` as a
probe with this gate:

```text
gate: derive the unimodular (trace-free) field equation from P3's volume
constraint without importing it; show kappa-suppression and the Lambda
integration-constant status follow; confirm the absolute floor decouples.
```

## Shape 2 — Finite-Strain Constitutive Residual (candidate controlled epsilon != 0)

**Claim shape.** The deviation channel that the program has been hunting in the
derivative-order direction (and correctly killing via ghosts) may instead live
in the *constitutive* direction:

```text
K_strain = c2 I(eps)        (quadratic = EH)
         + c3 I(eps)^(3/2)
         + c4 I(eps)^2 + ...  (higher powers of the SAME first-derivative strain)
```

These are higher powers of the first-derivative strain invariants, **not**
higher derivatives.

**Why it dodges the gate that kills higher curvature.**

```text
no new derivatives   -> second-order field equations preserved
                     -> no new propagating modes, no ghost
suppressed by powers of the strain itself
                     -> invisible in every weak-field test (small exterior strain)
                     -> switches on only where strain is large (interior / horizon)
```

**Disposition.** This is the natural mechanism for the **interior cap**: a
constitutive law that stiffens near a jamming limit caps compactness, and the
imported `kappa_max` becomes the substance's own close-packing / elastic limit
rather than an inserted cutoff. It lives in the `X -> g` map / `V_local`, the
corner Lovelock does not constrain. Recommended as the first concrete
candidate-branch charter, with gate:

```text
gate: (a) keep two-derivative field equations; (b) vanish to tested order in the
weak exterior; (c) produce a finite-strain admissibility bound from a DERIVED
modulus ratio, not an imported kappa_max; (d) match the exterior preservation
lemma.
```

## Shape 3 — Lambda As Frustration / Prestress (candidate Lambda selector)

**Claim shape.** In the elastic reading `Lambda` is the reference-configuration
energy density — the constant term the frustration-floor probe could not derive.
In ordinary elasticity that constant is a free choice of zero **unless the
medium is geometrically frustrated** (cannot satisfy all locally preferred
configurations at once). The theory already names it the frustration floor.

**Geometric-frustration packing route (owner intuition, 3D + 1).** A concrete,
literature-backed mechanism for the frustration:

```text
regular tetrahedra do not tile flat 3D space (icosahedral local order is
  frustrated in E^3)
the same order tiles the 3-sphere S^3 perfectly (the {3,3,5} / 600-cell ideal
  template; Frank-Kasper / Nelson / Sadoc-Mosseri)
frustration is relieved by curvature; embedding in flat space requires
  disclination defects that carry curvature
```

Mapping onto VED:

```text
flat-space residual frustration energy        -> the Lambda floor, with an origin
substance prefers a definite (positive) curvature -> a sign and scale for Lambda
matter = disclination defects carrying curvature  -> P3a (curvature = spatial
                                                     differential of vacuum amount)
defect gas over the floor                      -> the w ~ 0 dark excess candidate
3D-specialness of tetrahedral/icosahedral frustration -> the "+1" is the
                                                  repacking/relaxation direction
                                                  (P6 exchange vs creation)
maximal isotropy of {3,3,5}                    -> best protects the metric branch
                                                  against a Finsler continuum limit
```

**Disposition.** Promising but heavily gated. The honest kill conditions:

```text
1. magnitude: the naive frustration energy is huge (CC catastrophe). This route
   REQUIRES Shape 1 (unimodular floor decoupling) so the absolute floor does not
   gravitate; frustration alone reproduces the catastrophe.
2. curvature-scale: the ideal template radius is microscopic -> huge Lambda.
   A reason the net preferred curvature is almost cancelled (defect balance /
   slow relaxation) is the unsolved core. Backsolving the radius from the
   observed Lambda is rejected.
3. continuum limit / frame isotropy: coarse-grain to a smooth Lorentzian metric
   with no detectable lattice anisotropy or preferred-frame signal (ties to the
   Einstein-aether bounds and the metric-vs-Finsler debt).
```

Gate 2 is the one that decides whether the route lives or dies.

## Shape 4 — Substance Frame As Gated Aether Terms

**Claim shape.** The substance rest frame is a unit timelike vector `u^a`
(`u^a u_a = -1`). The only covariant local couplings to it are the
**Einstein-aether** terms:

```text
K_frame = c1 (grad u)^2 + c2 (div u)^2 + c3 (grad u)(grad u)^T + c4 (u.grad u)^2
```

P7' is the statement that **all c_i vanish in the closed sector**. The
substance-frame bounds sieve's `beta_frame` is a bound on these coefficients;
the observational face is the PPN preferred-frame parameters `alpha_1, alpha_2`
(currently `~1e-4 / ~1e-7`). A controlled frame channel is a small bounded
aether coefficient.

**Disposition.** This is the concrete form the
[06_non_gravitational_channels/substance_frame_bounds_sieve.md](06_non_gravitational_channels/substance_frame_bounds_sieve.md)
placeholder should carry. Gate: derive any `c_i != 0` before observation; bound
by `alpha_1, alpha_2`; quarantine from the metric response.

## Summary Table

| shape | lives in | bucket | first gate |
|---|---|---|---|
| EH+Lambda (FP-tuned elasticity) | K_strain, 2-deriv | epsilon = 0 | invoke Lovelock to close 1A |
| unimodular from P3 | trace sector + Lambda status | candidate result | derive trace-free eqn + Lambda-as-integration-constant from P3 |
| finite-strain residual | X -> g map / V_local | controlled epsilon != 0 | 2nd-order, weak-field-invisible, derived cap scale |
| frustration / packing Lambda | the constant term | Lambda selector | the curvature-scale (smallness) problem |
| Einstein-aether frame terms | non-grav channel | quarantined channel | c_i -> 0 in closed sector; alpha_1, alpha_2 bounds |

## Strategic Reading

The single new strategic point: **if a deviation from the closed GR response
exists, it is most likely a constitutive nonlinearity in the strain measure,
not a higher-derivative curvature term.** The program has searched the
derivative-order direction (where the ghost gates keep killing it) and
concluded "underdetermined without a new axiom." The finite-strain direction is
orthogonal to those gates, is forced to be invisible in the tested regime, and
is the natural mechanism for the one place the closed theory genuinely breaks
down (the interior). Shapes 1 and 3 then form one coherent `Lambda` story
(unimodular floor decoupling + frustration as the residual integration
constant), and Shape 4 is the gated form of the frame channel.

## Caveats

These are structurally motivated candidate shapes and analogies, not
derivations. The elasticity / linearized-gravity correspondence and Lovelock
uniqueness are standard; the incompressibility reading of P3, the unimodular
correspondence, and the frustration reading of `Lambda` are interpretive
bridges that must each pass their own gate. The geometric-frustration packing
mechanism is an owner intuition with a real condensed-matter lineage but an
unsolved smallness problem (gate 2 of Shape 3). Nothing here changes the closed
result or licenses any nonbaseline mechanism.

## Suggested Next Steps

```text
1. Charter Shape 2 (finite-strain residual) in 02_candidate_branches/ using the
   roadmap file template; it is the cleanest concrete epsilon != 0 route.
2. Open a probe for Shape 1 (unimodular from P3) in 04_lambda_baseline/; if it
   holds it is a result that explains the whole Lambda sweep.
3. Treat Shape 3's gate 2 (curvature-scale smallness) as the decision point for
   the packing route before investing further in it.
```
