# Why is Λ a constant of integration instead of a coupling?

A reader who already accepts that P3 freezes the metric's volume mode needs the next step spelled out: what that freeze does to the field equations, and specifically to Λ.

## The theorem

Start from the trace-free Einstein equation, the only field equation the unimodular constraint (κ = 0, i.e. √(−g) = √(−ḡ), forced by P3 with P7′ as its static shadow) leaves standing:

```text
R_ab - (1/4) g_ab R  =  (8*pi*G/c^4) (T_ab - (1/4) g_ab T)
```

This tensor is not identically divergence-free — it fails Lovelock's H3 hypothesis by construction (see the companion node on which hypothesis breaks). Take its divergence and use the contracted Bianchi identity ∇^a R_ab = ½∇_b R:

```text
nabla^a (R_ab - (1/4) g_ab R) = (1/4) nabla_b R   (identically, off shell)
```

Now feed in matter conservation, ∇^a T_ab = 0, as a genuinely separate input — it is not implied by the trace-free equation the way it is in full GR. Subtracting the two divergence conditions gives

```text
d/dt ( R + kappa*T ) = 0   =>   R + kappa*T = 4*Lambda = const
```

(κ ≡ 8πG/c⁴ here, not the volume mode of the companion node — an unfortunate but standard double use of the symbol). Substituting this constant back into the trace-free equation *algebraically reconstructs* the full field equations:

```text
G_ab + Lambda g_ab = kappa * T_ab
```

with zero new physics injected — this is not a fit, it's bookkeeping. Λ enters the theory at exactly this step: as the constant of integration of a conservation law that only closes when matter conservation is supplied as extra input, not as a term anyone placed in the action. Forge-verified on two independent nontrivial families (general static spherical; flat FRW with a perfect fluid), where the H3-failure computation is checked componentwise and the FRW route is carried through to the reconstructed field equations. On Schwarzschild-de Sitter (pure-Λ, matter-free) the constraint is exact identically (AB = 1), consistent throughout.

Two things this buys immediately, both landing on the Λ trail:

- **Sequestering falls out for free.** A constant shift T_ab → T_ab − ρ_vac g_ab is pure trace, so it's invisible to the trace-free equation — the equation that actually does the work here. Bulk vacuum energy doesn't gravitate; full derivation and consequences live in the sequestering node.
- **The Lambda baseline sweep (derivations 008–016) is retroactively explained, not just consistent.** That sweep tried six independent local routes to a Λ-selecting mechanism and found none. This theorem says that outcome was never going to change: no local principle can value Λ, because Λ is structurally a global datum (one boundary/initial condition — in Henneaux–Teitelboim language, the variable conjugate to the total four-volume), not a coupling any local variation could ever touch.

Scope, stated plainly: this does not derive Λ's *value* — the global datum stays external. It changes no closed local result (classical unimodular gravity and GR+Λ share a solution space). And the fully covariant statement of the κ = 0 constraint (beyond the reduced areal-gauge identity and the two witness families) is an open obligation, not yet closed.

**Proof:** forge 033 (`vacuum_forge/src/vacuum_sector/033_unimodular_lovelock_break/unimodular_lovelock_break.py`), obligations 2–3 specifically → [../theory_v3/development/vacuum_sector/lovelock_breaks_vacuumforge.md](../theory_v3/development/vacuum_sector/lovelock_breaks_vacuumforge.md), full structural argument in [../theory_v3/development/vacuum_sector/lovelock_breaks.md](../theory_v3/development/vacuum_sector/lovelock_breaks.md).

**Where next:**
- [The Unimodular Constraint →](idea_unimodular_constraint.md) — the P3 identity κ = ln(√(−g)/√(−ḡ)) that supplies the trace-free equation this theorem starts from.
- [Sequestering →](thm_sequestering.md) — the direct corollary: why the constant floor density cancels out of Λ term by term.
- [The Cosmological-Constant Trail →](hub_lambda.md) — the full argument this theorem is the hinge of, start to finish.
- [The Skeptic's Entrance →](hub_graveyard.md) — the six-route Lambda-selector sweep this theorem retroactively explains as a theorem rather than a coincidence.
