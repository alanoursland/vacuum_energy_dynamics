# Does the theory get the Schwarzschild radius for free, or does it earn it?

The static exterior derivation hands you $r_s = 2GM/c^2$ almost by accident — this node shows why that's not the same trap Michell fell into in 1784.

## The theorem

The exterior field-equation derivation (no tensor response law, just P3a/P6 flux-counting plus the P9-selected distortion variable $A = e^s$ and the P7′ compensation $B = 1/A$) produces

```text
A(r) = 1 - 2GM/(c^2 r)
```

whose zero is the Schwarzschild radius. That looks suspiciously like Michell and Laplace's 1784/1799 Newtonian escape-velocity trick ($\tfrac12 v^2 = GM/r$, set $v=c$), which lands on the *same number* by canceling two wrong ingredients (nonrelativistic KE, Newtonian potential). If VED's route were just a rediscovery of that cancellation, the agreement would be worthless — a coincidence, not evidence.

It isn't. Embed the derivation in its one-parameter family of possible countings, the C2 bootstrap family $A_\lambda = (1+\lambda\, r_s/r)^{-1/\lambda}$, all consistent with the flux law at first order:

- $\lambda = -1$ (count-once, the P9-selected member): $A = 1 - r_s/r$ — zero at $r=r_s$. **Horizon exists.**
- $\lambda \to 0$ (log-linear counting, no self-energy): $A = e^{-r_s/r} > 0$ everywhere. **No horizon at any radius.**
- $\lambda = +1$ (wrong-weight counting): $A = (1+r_s/r)^{-1} > 0$ everywhere. **No horizon at any radius.**

All three agree with Michell to first post-Newtonian order — Michell-grade reasoning cannot tell them apart. Only $\lambda=-1$, forced by P9's count-once accounting, produces a horizon at all, and it sits exactly at $r_s$. So horizon *existence*, not just its location, is a corollary of counting configuration energy exactly once at the universal coupling.

Three discriminators separate the two routes decisively: the spatial response ($B=1/A$ here, giving $\gamma=1$ and full light deflection, vs. Michell's implicit $B=1$, $\gamma=0$ — half the deflection, falsified in 1919 and excluded at $10^{-5}$ by Cassini); the second-order PPN coefficient ($\beta=1$ here, undefined there); and the fact that the derivation produces the exact metric at all orders, not one number.

The deeper reason the coincidence happens at all: the derived exterior admits a Painlevé–Gullstrand slicing in which the infall velocity satisfies $\tfrac12 v^2 = GM/r$ *exactly, at every radius*, with $v(r_s)=c$ exactly — GR's "river model" curiosity. In VED this isn't a curiosity, it's literally the P6 kinetic-exchange ledger, exact because the P9 resummation makes the flux law linear in $A=e^s$ and self-energy corrections cancel at every order. Michell's cancellation of two wrong ingredients works *because* the true theory's ledger happens to be Newtonian-shaped in this one chart. The horizon is the radius where the P6 exchange rate saturates the causal bound $v=c$ — a bookkeeping statement that happens to coincide with the metric statement $A=0$.

**Honest boundaries:** exterior only — the same ledger diverges as $-2GM^2/(R-r_s)$ at the doorstep, and the interior is an open obligation. No new prediction: everything here is GR-exact, the content is explanatory (why naive accounting works) and structural (horizon existence as a P9 selection witness). And it supersedes older "vacuum furnace" language: the static ledger closes without any funding current, so a standing mass does not consume vacuum — only the dynamic infall exchange saturates at the horizon.

**Proof:** forge trial 021, eleven checks (Michell/derived radius agreement, zero-set of all three family members, the $\gamma$ discriminator, PG-vacuum and Kretschmann verification, ledger exactness, horizon saturation) → [../theory_v3/development/horizon_accounting/horizon_accounting_note.md](../theory_v3/development/horizon_accounting/horizon_accounting_note.md), building on the exterior bookkeeping of `04_field_equations/proof.md` §2 and the Birkhoff lift of trial 019.

**Where next:**
- [Frustrated ground state forces the Einstein response →](thm_expansion_point.md) — the deeper reason the flux law has the shape it does.
- [No double counting →](thm_no_double_count.md) — the same P6 ledger discipline that makes the PG slicing exact, applied to a falling body's kinetic energy.
- [Einstein closure, condensed →](thm_einstein_closure.md) — the master result this exterior derivation is a corollary of.
- [The graveyard →](hub_graveyard.md) — where the theory's honest failures and open obligations (like the interior cap) are catalogued.
