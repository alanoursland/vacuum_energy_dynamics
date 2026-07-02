# Does gravity radiate in scalar or vector polarizations too, alongside the tensor waves?

A reader who already accepts the derived field equations might expect the closure to leave room for extra radiative channels; it doesn't.

## The kill

The field-equation closure (theory_v3/04_field_equations/proof.md, §4.4) proves the nonlinear response law is unique — Einstein–Hilbert, up to normalization, a cosmological term, and inert Gauss–Bonnet — given a local two-derivative massless spin-2 field on Minkowski space with relabeling gauge symmetry and universal stress coupling. That uniqueness proof, run against the actual sector-by-sector content of the closed theory, forecloses scalar and vector propagation by two independent, already-derived mechanisms. Nothing new has to be assumed to kill them; the closure already did it.

**Scalar sector.** Theorem 2 (§3) shows that promoting the static shear variable $s$ to a propagating field gives a Hamiltonian unbounded below ($H[\lambda s] \to -\infty$) — a ghost. Stability (P5) forces the scalar sector to be elliptic/constraint-type, not dynamical: it doesn't propagate at all in the base theory. The only place a genuine scalar *pole* could reappear is the $R^2$ higher-derivative term (the scalaron, Theorem 6, §5.1), and Theorem 7 (§5.2) kills that too: any static scalaron profile carries $D^t{}_t - D^r{}_r = -R'' \neq 0$, a preferred t–r frame, which P7′ forbids. The screening corollary closes the escape hatch explicitly — for a screened profile $\phi = \phi_{GR} - q(r)$, the P7′ shadow is $rq'(r) - q(r)$, and exact P7′ plus asymptotic flatness force $q \equiv 0$. No scalar radiative channel survives at any coupling strength or screening scheme.

**Vector sector.** §4.5(d) works the vector (gravitomagnetic) sector through general linear time dependence in transverse gauge ($g_{ti}=w_i$, $\partial_i w_i = 0$):

```text
G_ti^(1) = -½Δw_i,   G_ij^(1) = -(1/2c²)(∂_i ẇ_j + ∂_j ẇ_i)
```

The first equation is elliptic — a constraint, not a wave equation — and with slow matter momentum it reduces to the stationary Lense–Thirring law $\Delta w_i = (16\pi G/c^2)\rho v_i^T$, not an independent radiative degree of freedom. For a source-free transverse Fourier mode $w_i = W_i e^{i(kz-\Omega t)}$, the constraint gives $\tfrac12 k^2 W_i = 0$, forcing $W_i = 0$ for any $k \neq 0$: there is no vector dispersion relation.

What's left, verified rather than assumed: only the transverse-traceless (TT) sector propagates, with energy density a sum of squares (Theorem 4, positive definite) and coefficient $K_T = c^4/16\pi G$ per polarization (§4.3). Two tensor polarizations, full stop — the massless spin-2 architecture that Fierz–Pauli classification predicted at linear order is confirmed to survive the nonlinear closure exactly, with no smuggled-in extra modes.

**Proof:** §3 Theorem 2 (scalar ghost exclusion), §5.1–5.2 Theorems 6–7 (scalaron killed by P7′), §4.5(d) (vector sector, no dispersion relation), §4.3 Theorem 4 (TT positivity, $K_T$) → [../theory_v3/04_field_equations/proof.md](../theory_v3/04_field_equations/proof.md). Machine checks: `012_vector_sector/vector_sector_closure.py`, `017_vector_time_dependent/vector_time_dependent.py`, `009_.../trial_E3_p7prime_vs_scalaron.py`, `010_gate_G20_beta_health/gate_G20_beta_health.py`.

**Where next:**
- [The Scalaron Cancellation Kill →](kill_scalaron_cancellation.md) — the sharpest instance of this pattern: a proposed escape hatch for the scalar mode, refuted the same week it was proposed.
- [The Finsler Kill →](kill_finsler.md) — a different degree-of-freedom-counting kill, this one on the kinematic input side rather than the radiative output side.
- [The Prediction Trail →](hub_predictions.md) — where this kill turns into a standing null test (no gravitational-strength Yukawa deviation at any range).
- [The Graveyard →](hub_graveyard.md) — the full list of dead mechanisms and refuted proposals, for the skeptical entry point.
