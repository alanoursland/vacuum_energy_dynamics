# How does a constant vacuum energy stay invisible to gravity?

A reader who already knows the floor is a real, constant energy density needs to know why that density doesn't blow up Λ by 122 orders of magnitude — this is the mechanism that stops it.

## The idea

The frustration floor is a real energy density, constant everywhere the packing sits in its ground configuration. A naive reading says: gravity couples to energy density, so a constant floor density is just a huge cosmological constant, and the theory has the same 10^122 problem everyone else has. Sequestering is the proof that this naive reading is wrong.

The mechanism, in two steps:

- **Shift invariance.** On FRW with a perfect fluid, shift the stress tensor by a constant: `T_ab -> T_ab - rho_f g_ab`. Because Λ is not a coupling in the action but an *integration constant* of the trace-free (unimodular) conservation law, this shift doesn't perturb the field equations at all — it just reshuffles the integration constant exactly: `Lambda' = Lambda - k*rho_f`. Same physical equations, relabeled constant. A constant floor density is therefore not a separate physical input the way an ordinary w = -1 fluid would be; it is absorbed into the very quantity (Λ) that was already free.
- **No isolated time-variation escapes it either.** If the floor density were time-varying in isolation, `nabla^a(-rho_f(t) g_ab) = -d_b rho_f` forces `rho_f = const` by conservation alone. So a floor that varies can only do so by exchanging energy explicitly with another component — and that exchange is dark-excess bookkeeping (w != -1 physics), not a Λ mechanism. There is no back door where "the floor gravitates a little" sneaks in.

Net result: **no constant vacuum floor gravitates, full stop.** The observed Λ is not ρ_floor. This is a branch decision, not a hand-wave — it closes the "floor = local gravitating w = -1 density" branch outright, forge-verified (033 check 4, plus the dedicated sequestering script). What survives is a re-posed, harder target: the floor may still matter for Λ, but only by selecting the *global datum* (the constant of integration itself, conjugate to the total four-volume in Henneaux–Teitelboim language) — not by acting as a local source term. That global-datum route is the subject of the Λ trail; sequestering is what forces the question onto that harder ground instead of letting it hide in a local density.

Why this matters for the 122-orders problem specifically: the standard cosmological-constant problem is "why doesn't vacuum energy gravitate at the scale QFT predicts." Sequestering answers the *mechanism* half of that directly — constant vacuum energy is structurally decoupled from Λ by the unimodular conservation law, independent of what the number is. The *value* half (why Λ is what it is) is a separate, open question — see the cc-problem node for how the two faces split apart.

```text
T_ab -> T_ab - rho_f g_ab  leaves the trace-free field equations unchanged;
Lambda' = Lambda - k*rho_f  (same physics, relabeled constant)
```

**Proof:** forge 033 (check 4) and the dedicated sequestering script → [../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md](../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md), verification detail in [../theory_v3/development/vacuum_sector/floor_sequestering_constraint_vacuumforge.md](../theory_v3/development/vacuum_sector/floor_sequestering_constraint_vacuumforge.md).

**Where next:**
- [The Unimodular Constraint →](idea_unimodular_constraint.md) — the P3 identity that makes Λ an integration constant in the first place, the fact sequestering depends on.
- [The Floor →](idea_floor.md) — what the density being sequestered actually is and where its number comes from.
- [The Cosmological Constant Problem →](idea_cc_problem.md) — why splitting "does it gravitate" from "what's its value" is the whole move, and where sequestering lands on that split.
- [The Cosmological-Constant Trail →](hub_lambda.md) — the full argument this node is one step of, start to finish.
