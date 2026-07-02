# Why split the cosmological constant problem into two problems, not one?

The textbook CC problem is a single number, 10^122; VED's grounding work shows it is actually two separable questions with different current status.

## The idea

The standard statement: naive QFT vacuum energy summed to the Planck cutoff gives a density ~10^120 to 10^122 times the observed Lambda. Usually this is presented as one catastrophe. It is not — it is two catastrophes bolted together, and they get solved (or not solved) independently.

**Face 1 — the stability problem.** *Why doesn't a huge vacuum energy density gravitate and curl space up to Planck-scale curvature?* This is the "old" CC problem in Weinberg's sense: any large constant vacuum density should source curvature at the same coupling as everything else, so the universe should look nothing like it does. VED's answer here is structural, not a cancellation:
  - Configuration energy gravitates as a genuine source, counted once (P9) — this is load-bearing, it's what selects the Schwarzschild exterior.
  - Constant *bulk* density, by contrast, enters the field equations only as the P3 constraint (`AB = 1`, i.e. `kappa = (1/2) ln(AB) = 0`) — never as a curvature source.
  - Consequence: bucket-(1) substance bulk cannot produce a Lambda catastrophe no matter how large it is, because it structurally never enters as a source. This is the field-equation-level shadow of unimodular sequestering (see `idea_sequestering.md`). **This face is closed** — grounded in the derived field equations, not proposed.

**Face 2 — the value problem.** *Given that some constant-density component CAN gravitate (bucket-(2), the configuration/frustration floor, since P9 says configuration energy gravitates), why is its value ~(meV)^4 and not ~(Planck scale)^4?* This is a live, unsolved magnitude gate. The floor is a genuinely new, non-zero configuration energy of flat, frustrated 3+1 vacuum — current flat empty space in the bare theory has `u_field = 0` (no mass -> s = 0), so Lambda sits in an open slot the floor is proposed to fill. But the theory does not yet derive the floor's *number*. **This face is open.**

```text
Face 1 (stability): huge density -> curls space up      STRUCTURALLY CLOSED
                     (bulk never sources; only configuration energy does)
Face 2 (value):      why THIS density, ~(meV)^4?         OPEN (magnitude gate)
```

The iron rule underlies why this split is legitimate at all: for any component with `rho' = 0` under expansion, the continuity equation `rho' + 3(a'/a)(rho + p/c^2) = 0` forces `p = -rho c^2`, i.e. `w = -1` — a cosmological constant is nothing but "energy created in step with expansion." That reframes creation as ordinary, and lets the two faces be asked as separate structural questions instead of one unexplained coincidence.

The honest boundary: "bulk never gravitates" is grounded in how P3 currently enters the derivation (a constraint, not a source) — it is not yet elevated to a standalone theorem. And the floor = Lambda identification for face 2 is a proposal that survives only in re-posed form (derivation 035): a constant floor is sequestered like the bulk, so it can't be the local w=-1 density directly — instead it's a candidate for *selecting the global datum* that fixes Lambda (Henneaux–Teitelboim: Lambda conjugate to total four-volume).

**Proof:** grounding in `04_field_equations/proof.md` (P9 configuration-energy count-once, P3 -> `AB=1` shadow); the two-face split and the iron rule are worked in [../theory_v3/development/vacuum_sector/dark_energy_accounting.md](../theory_v3/development/vacuum_sector/dark_energy_accounting.md); the re-posed floor/global-datum result is derivation 035, referenced there as `floor_sequestering_constraint_vacuumforge.md`.

**Where next:**
- [How does constant density become invisible to gravity? →](idea_sequestering.md) — the mechanism behind why face 1 closes structurally.
- [What is the frustration floor? →](idea_floor.md) — the candidate content for face 2's open magnitude.
- [Why is constant density the unimodular constraint? →](idea_unimodular_constraint.md) — the derivation behind the `AB=1` shadow that keeps bulk from sourcing curvature.
- [The cosmological-constant trail →](hub_lambda.md) — the full argument chain from frustration to Lambda.
