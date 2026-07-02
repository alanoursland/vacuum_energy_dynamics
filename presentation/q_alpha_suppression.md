# Does mass suppress local vacuum creation, and by how much?

The creation reading of expansion (see the graveyard's stretch-vs-growth kill) left one coefficient on the table, unfixed and — as of this writing — unfixable without physics the theory doesn't have yet.

## The question

Once growth wins (new cells at fixed packing scale, not a dilating fixed graph — see the 045 seam), the natural next question is *where* the new cells appear. The founding intuition, older than the formalism, was that mass should push creation away from itself: space opens up preferentially in voids, suppressed in wells. Derivation 054 writes that intuition down as a single clause on the local creation rate:

```text
C = 3H(1 - alpha delta)
```

`3H` is the background rate the growth reading already forces. `delta` is the local density contrast — the "am I near a mass concentration" variable, with `<delta> = 0` by construction over any large enough volume. `alpha` is the one number nobody has computed: how strongly, if at all, creation actually cares about local strain.

Two facts pin down exactly how open this question is:

- **It is unconstrained by everything derived so far.** Because `<delta> = 0`, `<C> = 3H` for *any* value of alpha — zero, one, a googol. The Friedmann sector, the floor's equation of state, the G-constancy result (register A6) — none of them see alpha. The clause could vanish (alpha = 0, creation is uniform) or dominate local dynamics (alpha large) and the background cosmology derived to date wouldn't move.
- **It is not computable with statics.** Alpha is a coefficient in front of a *local, mass-sourced* effect, and everything the theory has proven about the floor (039, 051) is a global, equilibrium statement about a fixed-topology packing. Turning alpha into a number requires treating creation as a functional of local strain in a packing that is actually evolving — which is exactly what the theory does not yet have. The clause is a placeholder with a name, not a mechanism.

What would close it: the Lorentzian initial-value problem for the packing (O-P10-4) — an actual dynamical law for how cells nucleate, rearrange, and disappear under local stress, CDT-adjacent in spirit. Alpha falls out of that dynamics as a derived number, not a fit. Until O-P10-4 exists, alpha is formally present in the theory (register: `creation_suppression_dynamics_054`) and empirically silent — no observable has been claimed for it, and none should be, on pain of backsolving.

**Proof:** derivation 054, "The Vacuum-Flow Clause" → [../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md)

**Where next:**
- [Does creation know where the mass is? →](idea_vacuum_flow.md) — the idea-level writeup of the same clause, with the full term-by-term reading.
- [The Lorentzian dynamics frontier →](q_lorentzian_dynamics.md) — the initial-value problem that alpha is downstream of; nothing computes alpha until this exists.
- [The packing scale →](q_packing_scale.md) — the other free constant in the microphysics, open for a different reason (assumption, not missing dynamics).
- [The skeptic's entrance →](hub_graveyard.md) — where the stretch reading that alpha's clause survived gets killed twice, for context on why growth was the reading worth building this clause onto.
