# What actually governs the packing's evolution in time?

the CDT-adjacent frontier: everything checked so far is kinematic or linearized, and neither is a dynamics.

## The question

Two prior results look like they cover motion but don't. [The Lorentzian lift](thm_lorentzian_lift.md) (derivation 043) shows the 4D action *can* be continued past the light cone term-by-term and linearizes correctly — that's kinematics plus perturbation theory, not an equation of motion. [Gdot = 0](pred_gdot_zero.md) (derivation 054) settles which *reading* of cosmic expansion the packing uses — graph growth, not stretch — but a reading is a boundary condition, not a solver. Neither result says what determines the next triangulation from the current one. That's O-P10-4, and it is still open.

What derivation 054 narrowed, concretely:

- **The stretch-vs-growth ambiguity is resolved.** The metric sector alone can't distinguish "graph fixed, cells dilate" from "graph fixed-scale, cells added" — both give the same `a^3` volume history. Stretch is killed twice on existing data (G drift ~480x over the LLR bound; the floor turned to dust overshoots closure by ~10^122). Growth survives, self-funded by the floor's measured `w = -1`.
- **A standing commitment falls out for free:** Gdot = 0 exactly, at every epoch (register A6) — not a fit, a consequence of growth being the only surviving reading.

What's still owed, and it's the harder half:

```text
C = 3H(1 - alpha delta)
```

the vacuum-flow clause — the rate of new-cell creation `C`, proportional to the Hubble rate but modulated by local strain `delta` through a coefficient `alpha` that is currently free. The clause is background-invisible for *any* value of `alpha`: it doesn't touch the homogeneous cosmology derivation 054 already checked, which is exactly why it isn't pinned by that derivation. Pinning `alpha` needs its own dynamics (see [The vacuum-flow coefficient](q_alpha_suppression.md)).

Beyond `alpha`, the actual initial-value problem is unstarted: given a triangulation and its strain field at time `t`, what rule produces the triangulation at `t + dt`? This is the CDT-adjacent question by design — Causal Dynamical Triangulations solved the analogous problem for a different discretization (sum over triangulations, not a packing ground state relaxing under frustration), and its machinery is the natural neighbor to borrow from or contrast with, not yet attempted here. No local evolution rule, no path integral or classical relaxation dynamics, no statement about what "time" means for a single triangulation between growth events, is on the books.

**Proof:** derivation 054 narrows the question but does not close it → [../theory_v3/05_vacuum_sector/05_open_obligations.md](../theory_v3/05_vacuum_sector/05_open_obligations.md) (O-P10-4); the kinematic ceiling this frontier sits above is derivation 043 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/lorentzian_4d_lift_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/lorentzian_4d_lift_vacuumforge.md).

**Where next:**
- [The vacuum-flow coefficient alpha →](q_alpha_suppression.md) — the one piece of O-P10-4 with a name and a place in the equation, still numerically free.
- [Does Newton's constant drift with cosmic time? →](pred_gdot_zero.md) — the boundary-condition result (growth, not stretch) that this open question has to build a dynamics on top of, not replace.
- [The Lorentzian lift →](thm_lorentzian_lift.md) — the kinematic + linearized ceiling this frontier sits directly above.
- [What does this program not know yet? →](hub_open_problems.md) — O-P10-4 alongside the other four live debts on the adopted axiom.
