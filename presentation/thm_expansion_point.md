# Why does a frustrated ground state force gravity to be linear in curvature?

A theorem, not a preference: expand any smooth per-hinge energy about the packing's actual minimum, and the sign of the ground-state slope decides whether you get Einstein-Hilbert or R².

## The theorem

Effective field theory alone doesn't pick R over R², R³, .... Something has to fix the expansion point. This theorem says the packing does, mechanically, once you take the ground state seriously as *frustrated* (sitting at nonzero deficit) rather than *relaxed* (sitting at zero deficit).

Setup: give every hinge $h$ of the Delaunay/Regge graph a smooth per-wedge energy $f(\delta_h)$, weighted by hinge measure $V_h$, and Taylor-expand about whatever deficit $\delta = D_0$ actually minimizes the packing's energy:

```text
E = Sum_h V_h f(D0)                    <- floor: substance energy, sequestered
  + f'(D0) Sum_h V_h (delta_h - D0)    <- linear: the Regge action -> Einstein-Hilbert
  + (f''(D0)/2) Sum_h V_h (...)^2      <- quadratic: R^2-class, suppressed by a^2*K
```

The three terms are not independent choices — they're forced by one Taylor series around one number, $D_0$.

**The branch point.** Whether the linear term survives depends entirely on whether $D_0 = 0$:

- **Frustrated ground state ($D_0 \neq 0$):** for regular tetrahedra, $D_0 = \Delta_0 = 2\pi - 5\arccos(1/3) \approx 7.36°$ is the *irreducible* minimum-energy deficit (curving to relieve it costs more than it saves at every sub-packing scale — derivation 037). Since the minimum sits away from $\delta=0$, there is no reason for $f'(D_0)$ to vanish; generically it doesn't. The **linear** term dominates the response to bending the packing, and the linear term in deficit angle is exactly the Regge form of $\int R\sqrt{g}$. Gravity comes out Einstein-Hilbert with no tuning.
- **Unfrustrated ground state ($D_0 = 0$):** if the packing could actually close ($\delta=0$ achievable), then $\delta=0$ being the true minimum forces $f'(0)=0$ by the ordinary calculus fact that a smooth function's derivative vanishes at its minimum. The linear term is killed identically. The **leading surviving response is the quadratic term** — $R^2$ gravity, a strictly weaker, higher-derivative theory.

So "gravity is linear in curvature, not quadratic" reduces to "the packing is geometrically frustrated, not geometrically closable." Frustration is not a footnote to the floor — it is the mechanism selecting Einstein-Hilbert as the generic leading term.

**The number that makes it concrete.** Triangulating the unit 3-sphere with the 600-cell (720 edges, five regular tetrahedra per edge, every hinge at exactly $\Delta_0$) gives $S_{\text{Regge}} = 720\,\Delta_0/\varphi = 0.9647 \times \tfrac12\int R\sqrt g$ — the frustration deficit reproduces the continuum EH integrand to 3.5% at the coarsest possible mesh.

**One free bonus.** The same stiffness $f'(\Delta_0)$ sets both the floor's substance density and the EH coefficient — $\rho_v = (c_e \Delta_0 / 2a^3)\, f'(\Delta_0)$ — so the vacuum's energy density and the strength of gravity are two readings of a single wedge-energy slope (the floor-Newton lock).

**Scope, stated plainly.** This is exact discrete geometry (checks 1–3, 5 in the source) plus an exact Taylor-expansion argument (check 4) — it is *not yet* a continuum-limit theorem (does mesh refinement converge to the smooth EH action?) and *not yet* a 4D/Lorentzian statement. Both are open obligations, not proved here. There is also a live tension: the quadratic term is R²-class with Planck-scale coefficient ($\sim a^2$), while P7′ (adopted elsewhere) forces the four-derivative sector exactly empty — unresolved, Planck-scale, on the books as `p7prime_packing_tension_039`.

**Proof:** derivation 039 (expansion-point theorem, discrete Gauss-Bonnet anchor, 600-cell cross-check, floor-Newton lock), building on derivation 037 (exact irreducibility of $\Delta_0$) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md)

**Where next:**
- [Why is gravity Einstein-Hilbert and not R²? →](hub_why_eh.md) — the full hook trail this theorem is the spine of, from packing to closed question.
- [The Frustration →](idea_frustration.md) — where $\Delta_0$ comes from and why relief always costs more than it saves.
- [The microstructure trail →](hub_packing.md) — the model, the ground state, the lab, and the self-tests this theorem sits inside.
- [Einstein Closure →](thm_einstein_closure.md) — the master result this feeds: the full field-equation derivation with zero matched coefficients.
