# How does Einstein's equation fall out of a packing that never mentions gravity?

Trailhead for the field-equation trail: postulates in, GR out, sector by sector, with the anti-circularity ledger open the whole way.

## The trail

Start here if you want to watch general relativity get *derived* rather than assumed. The result, stated once:

```text
G_ab + Λ g_ab = (8πG/c⁴) T_ab
```

Einstein's field equations, exactly — not a deformation, not a low-energy limit. What makes this trail worth walking is not the destination (it's the equation everyone already knows) but the route: the derivation uses special relativity, one empirical constant (Newton's $G$, entering exactly once), the postulates (P1–P6, P7′, P9), and two declared external math theorems (Fierz–Pauli 1939 for linear spin-2 uniqueness; Christodoulou–Klainerman/Lindblad–Rodnianski for a global stability anchor that carries no coefficient). The Einstein tensor itself is never assumed as a response law — it's used as pure differential geometry until §4, where it's *derived* as the unique closure of the substance kinematics.

The trail, in order:

1. **Kinematics first, no dynamics yet.** P2 (vacuum configuration = spacetime) plus the SR quadratic-interval import restricts the substance's local structure to a symmetric metric $g_{ab}$; gauge freedom is just relabeling. This is where universal coupling comes from — matter's clocks and rods *are* the vacuum's mappings, so there's no adjustable charge to gravity.

2. **The static exterior, by pure bookkeeping — no field equation used.** A Gauss-type flux law (P3a + P6, additivity/isotropy/locality) fixed by the Newton anchor gives the areal flux law. P7′ (no preferred static t–r frame) gives the shadow $AB=1$. P9 (configuration energy counted once, geometry-side) selects the *unique* distortion variable among a one-parameter family, forcing the field's self-energy density to be exactly $u_{\text{field}} = -c^4(s')^2/8\pi G$ — negative, and forced, not chosen. Solving gives Schwarzschild exactly. Static-ness itself is then proved (a Birkhoff-type theorem), not assumed.

3. **Stability, checked before dynamics is even fixed.** The negative field energy can't run away: the scalar sector is forced elliptic (ghost exclusion), flat is the unique regular source-free state at full nonlinear strength, and quasilocal mass stays non-negative for any configuration (Misner–Sharp). There's no channel that mines the reservoir.

4. **The dynamical closure.** Fierz–Pauli fixes the linear spin-2 operator; P9 forces iterated self-coupling (the field sources itself at the same universal coupling); a seven-step in-house theorem (closure uniqueness) proves the *only* consistent nonlinear completion is Einstein–Hilbert, up to a cosmological term and inert Gauss–Bonnet. The normalization $N = c^4/8\pi G$ and the radiative constant $K_T = c^4/16\pi G$ both come out with zero remaining freedom — the second one is a quantity the linear theory *provably cannot fix on its own* (Lemma 4), closed only by P9's self-sourcing requirement.

5. **Closing the residual freedom.** Higher-curvature terms are checked and killed: quadratic terms that touch the propagating sector are ghosts (excluded by the same stability argument as step 3); Gauss–Bonnet is topological in 4D; the surviving $R^2$/scalaron term is killed outright by P7′ — a static scalaron always carries a preferred t–r frame, and no screening mechanism can hide it. This is the same postulate that fixed $AB=1$ in step 2, now closing the four-derivative sector too.

Two independent routes — substance bookkeeping (step 2) and field-theoretic closure (step 4) — land on the same Schwarzschild exterior with the same constant. That agreement was a possible internal falsifier; it passed.

**Proof:** [../theory_v3/04_field_equations/proof.md](../theory_v3/04_field_equations/proof.md) is the self-contained derivation (the anti-circularity ledger is §7 there — read it if the word "circular" is on your mind); [../theory_v3/04_field_equations/00_overview.md](../theory_v3/04_field_equations/00_overview.md) is the one-paragraph result and reading map for the rest of that section's files.

**Where next:**
- [The hook trail →](hub_why_eh.md) — start further back, at the frustration and the deficit angle, if you want the motivating picture before the proof.
- [The assumption ledger →](hub_postulates.md) — see exactly which postulates (P1–P6, P7′, P9) are doing the work above, one screen each.
- [The microstructure trail →](hub_packing.md) — the packing model underneath P9 and P7′, quantified.
- [The auditability spine →](hub_proof_index.md) — every theorem above, its derivation number, and its verification script in one table.
