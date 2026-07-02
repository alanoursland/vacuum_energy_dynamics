# What does the whole program actually assume?

The full assumption ledger — every postulate the framework runs on, in one screen each, with what each buys and where it's fenced.

## The claim

Everything downstream — the field equations, the vacuum sector, the packing microphysics, the predictions — traces back to a short, named list. Nothing else is allowed in. If a derivation needs an assumption not on this list, that's a bug, not a shortcut.

**P1 — Vacuum-energy equivalence.** The vacuum *is* energy, the way mass is energy under $E=mc^2$ — not "contains," not "carries." Buys: vacuum has real, local, physical energy content. Fence: doesn't say how much (density), how it's arranged (geometry), or how it moves (dynamics) — those are separate postulates.

**P2 — Vacuum-spacetime identity.** The vacuum and spacetime are one substance, not two coupled things. A vacuum change *is* a spacetime change, not a cause of one. Buys: removes an entire layer of free parameters (no coupling constant, no mediation delay) and makes "spacetime is energy" literal. Fence: doesn't specify the vacuum's mathematical structure (scalar? tensor? richer?) — open until P10.

**P3 — Vacuum energy density.** $\rho_v$ is finite and locally constant: every observer, everywhere, every time, measures the same value. Buys: geometric variation can never hide in density — it has to live in *amount* of vacuum instead, which is what makes P3a possible. Fence: doesn't fix the value of $\rho_v$, and doesn't forbid it being negative in principle.

**P3a — Spatial differential is curvature.** Curvature is defined, in the framework's own vocabulary, as the spatial differential of vacuum *amount* (extensive) across neighboring regions, density (intensive) held fixed by P3. Buys: a framework-native definition of curvature that doesn't have to import a metric or connection from GR. Fence: doesn't say what mathematical object the differential is, or how it relates to the Riemann/Ricci tensors — that's resolved concretely only once P10 supplies a geometry.

**P4 — Curvature contains energy.** Configuration energy is a second energy ledger, distinct from substance energy: a curved region has more total energy than a flat region with the same amount of vacuum. Buys: the two-energy bookkeeping (substance vs. configuration) that the rest of the framework runs on — local gravity turns out to live almost entirely in the configuration ledger. Fence: doesn't specify the configuration-energy functional's exact form; that's supplied later.

**P5 — Minimum energy configuration.** The vacuum's configuration relaxes toward minimum configuration energy under whatever constraints apply; unconstrained, it settles to flat. Buys: dynamics — a reason curvature evolves at all, and a principled definition of "ground state." Fence: minimum doesn't mean zero — flat can carry nonzero configuration energy (this is exactly what P10 later cashes in as the frustration floor).

**P6 — Vacuum exchange in gradients.** Every quantum of energy feels the same force per unit energy in a curvature gradient; kinetic-energy changes along the gradient are sourced/sunk by vacuum creation/destruction. Buys: the equivalence principle, derived rather than assumed — $F = (g/c^2)E$ gives $a=g$ independent of mass, and photons fall on the same footing as rest mass. Fence: doesn't say which direction the force points for a given gradient structure — that's fixed by the specific geometry, not the postulate.

**P7′ — Static frame indifference (adopted).** A strictly static vacuum configuration carries no energy current and picks out no preferred frame in the t–r plane. Buys: $T^t{}_t=T^r{}_r$, whose metric shadow is $AB=1$ with asymptotic flatness — recovering old P7's content as a consequence rather than an assumption. Fence: exact only in the strictly static limit; a real exterior sits in an expanding cosmos, so there's a small correction (tracked as an open obligation, not swept under the rug).

**P9 — Configuration energy gravitates (adopted, fenced).** Configuration energy sources gravity at the same universal per-unit-energy coupling as everything else — gravity's own field energy is not exempt. Buys: self-coupling as ontology, which is what produces $\beta=1$ in the PPN chain and passes the Nordtvedt test. Fence — the load-bearing one: a term only counts as a source if it survives variation of the *adopted* dynamical law; being named an energy in a diagnostic ledger does not earn it a seat. No reservoir promotion, no bypassing the no-overlap/count-once gates.

**P10 — The packing axiom (adopted 2026-07-01, fenced).** The vacuum substance is a packing: a graph of edge lengths whose piecewise-flat geometry puts curvature on hinges as closure deficits, with smooth per-hinge energy $E[X]=\sum_h V_h f(\delta_h)$. Because regular tetrahedra can't tile flat 3-space (five around an edge fall short by $\Delta_0=2\pi-5\arccos\tfrac13$), the ground state is frustrated — flat, but carrying irreducible strain. Buys: the expansion-point theorem (frustration is *why* the leading response is Einstein–Hilbert, not $R^2$ gravity), the sector signature, and a concrete answer to what P1–P6 were describing all along. Fence: adopted on coherence evidence, not blind prediction — three pre-registered falsifiers (volume-mode restoring force; floor scale split from the P1 conversion factor; a detected Yukawa deviation), and a fence excluding dark-matter abundance claims, non-gravitational channels, and any reopening of the closed field equations.

Plus **SR1–SR9**, imported wholesale from special relativity (Lorentz invariance, $c$, Minkowski structure, $E=mc^2$) — not framework postulates, just the starting floor.

**Zero recovery-shaped postulates remain.** None of P1–P10 was adopted to force agreement with GR after the fact. P7′ and P9 were adopted on structural grounds before their consequences were known; P10 is the one exception that's honestly flagged — adopted after a verification campaign, so its evidential weight has to come from what it predicts next, not what it already fit.

**Proof:** [../theory_v3/01_postulates/00_overview.md](../theory_v3/01_postulates/00_overview.md) — the live ledger, with each postulate's own file carrying its full statement, epistemic status, and (for P9/P10) its fence in force.

**Where next:**
- [The hook trail →](hub_why_eh.md) — frustration to deficit angles to the expansion-point theorem: P10's central payoff, walked step by step.
- [The rules of the program →](hub_rules.md) — why postulates get fences and kill-conditions at all, and what "adopted on coherence" is allowed to mean here.
- [The field-equation trail →](hub_einstein.md) — what P1–P9 alone (no P10) already deliver: GR sector by sector, zero fitted coefficients.
- [The microstructure trail →](hub_packing.md) — P10 unpacked: the packing model, the ground state quantified, the self-tests.
- [The graveyard →](hub_graveyard.md) — postulates and mechanisms that were tried and killed before P7′/P9/P10 reached this ledger.
