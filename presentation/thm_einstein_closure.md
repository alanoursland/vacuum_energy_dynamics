# Does the framework actually land on Einstein's equations, with nothing dialed in by hand?

The master result, condensed: P1–P6, P7′, P9 plus one empirical constant close on the exact Einstein field equations, with every coefficient forced.

## The theorem

*Statement.* From the postulates alone — no Einstein–Hilbert action assumed, no Einstein tensor assumed as a response law — the gravitational field equation is exactly

```text
G_ab + Λ g_ab = (8πG/c⁴) T_ab
```

with $N = c^4/8\pi G$ and the radiative constant $K_T = c^4/16\pi G$ both fixed, zero free coefficients left except $\Lambda$ (permitted, not valued — that's a separate proof, see below). This is not a low-energy limit or a deformation of GR; it's the equation, closed.

The inputs, exhaustively: special relativity (Minkowski as the zero-source state), Newton's $G$ entering exactly once (the only empirical anchor), P1–P6/P7′/P9, and two declared external math theorems that assume nothing about gravity's actual dynamics — Fierz–Pauli 1939 (linear massless spin-2 uniqueness) and Christodoulou–Klainerman/Lindblad–Rodnianski (global small-data stability, used only as an anchor; no coefficient depends on it). The Einstein tensor appears before §4 only as differential geometry — an identity that holds for *any* metric — never as a response law until it is derived as one.

**The route, four movements:**

1. **Kinematics (§1).** P2 (vacuum configuration = spacetime) restricted to the SR-compatible quadratic branch forces a symmetric metric $g_{ab}$; gauge freedom is relabeling; matter's universal coupling falls out with no adjustable charge, because matter's clocks and rods *are* the vacuum's mappings.

2. **Static bookkeeping, no field equation yet (§2).** A Gauss-type flux law (P3a/P6, Newton-anchored) plus P7′'s shadow ($AB=1$) plus P9's variable selection (the *unique* distortion variable whose nonlinear content equals its own bookkeeping energy) together force the exact Schwarzschild exterior and a forced-sign negative field energy $u_{\text{field}} = -c^4(s')^2/8\pi G$. Lifted covariantly (§2.4): the flux law is the chart-free tt-equation, the shadow is chart-invariant, staticity itself is a theorem (Birkhoff-type), not an assumption.

3. **Stability, checked before dynamics is fixed (§3).** The negative-energy mode is forced elliptic (ghost exclusion); flat is the unique regular source-free state at full nonlinear strength (Theorem 3n); quasilocal (Misner–Sharp) mass stays non-negative for any configuration, exactly, no weak-field expansion (Theorem 3m). No channel mines the reservoir.

4. **Dynamical closure (§4).** Fierz–Pauli fixes the unique linear spin-2 operator. P9 forces iterated self-coupling — the field must source itself at the universal coupling. Theorem 5u (proved in-house, seven steps, not imported from Deser) shows the *unique* consistent nonlinear completion of that iteration is Einstein–Hilbert/Palatini, up to boundary terms, field redefinitions, a cosmological term, and inert 4D Gauss–Bonnet. Normalizations follow with no remaining freedom.

5. **Closing the residual freedom (§5).** Quadratic-curvature terms that touch the propagating sector are ghosts (same stability argument as step 3); Gauss–Bonnet is topological in 4D; the surviving scalaron ($R^2$) is killed outright by P7′ — any static scalaron profile carries a preferred t–r frame, and no screening mechanism hides it (the P7′ shadow of a screened profile forces the profile to vanish identically).

**The internal cross-check.** Two independent routes — substance bookkeeping (movement 2) and field-theoretic closure (movement 4) — derive the same Schwarzschild exterior with the same constant. A mismatch would have falsified the framework from the inside; there is none.

**Proof:** [../theory_v3/04_field_equations/proof.md](../theory_v3/04_field_equations/proof.md) — self-contained, every theorem (1 through 7, 5u, 3n, 3m) proved in place with a machine-verification pointer per step; the anti-circularity ledger is §7 there, the verification index is §9.

**Where next:**
- [Why the frustrated ground state matters →](thm_expansion_point.md) — the packing-level reason the leading response has to be Regge/EH shape at all, before this closure even runs.
- [Why nothing depends on Deser →](thm_evenness.md) — a different piece of the anti-circularity argument: the spectrum's exact evenness rules out linear Lorentz violation by construction.
- [Λ as an integration constant →](thm_lambda_integration_constant.md) — what happens to the one term this theorem leaves unfixed.
- [The honest negative: the scalaron reconstruction →](thm_scalaron_reconstruction.md) — the counter-case, where a cancellation mechanism the theory owner hoped for gets refuted using this same closure machinery.
- [The falsifier trail →](hub_predictions.md) — the observational tests this closure's corollaries stake themselves on.
- [The skeptic's entrance →](hub_graveyard.md) — if "no free coefficients" sounds too clean, start where the failed mechanisms are buried.
