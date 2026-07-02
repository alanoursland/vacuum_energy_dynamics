# Does the unimodular constraint kill the packing's scalaron?

A proposed fix for the R^2 tension was tested in-house and failed; here is the failure, on the record.

## The kill

The packing's ground-state expansion carries an f''-class term that behaves like R^2 gravity
(see [The Expansion Point](thm_expansion_point.md)). P7' says the theory's response should be
pure Regge/Einstein-Hilbert, full stop -- no scalar-tensor propagator riding along. The obvious
patch: the unimodular constraint (P3's seat, the same mechanism that makes Lambda an
integration constant) restricts the field equations to their traceless part, so maybe it
projects the scalaron out before it can propagate.

It doesn't. The kill:

- Take f(R) = R + alpha R^2 and compute the Euler-Lagrange tensor on FRW *without* imposing any
  field equations. It is identically conserved -- this is just the contracted Bianchi identity,
  the same structural fact that turns Lambda into an integration constant in the P3 story.
- Because the tensor is identically conserved, its divergence is identically zero. Take the
  divergence of the unimodular (traceless-only) field equations and that identity forces the
  *trace* equation back into existence, up to a constant of integration:

```text
f'R - 2f + 3 box f' = kappa T + const
=>  (6 alpha box - 1) R = kappa T + const.
```

- That's the scalaron equation. Restricting to traceless equations doesn't remove the trace
  d.o.f. -- Bianchi reconstructs it for free. Unimodular f(R) is just f(R) with an extra free
  constant (Lambda); it is not scalaron-free. The scalaron mass is m^2 = 1/(6 alpha), exactly
  the ordinary full-diff f(R) result.
- The same mechanism that is a *feature* elsewhere in the theory -- Bianchi + unimodular gives
  Lambda for free -- is the reason this particular cancellation trick can't work here. There is
  no cheap escape hiding in the same identity twice.

Consequence check, not a rescue: the scalaron's range is set by the packing's own coefficient,
alpha ~ |f''/2f'| a^2, giving l* = sqrt(6 alpha) ~ a. At Planck packing that's ~4e-35 m against
a 54-micron laboratory frontier -- a margin of ~1e30. The unwanted field is there, but it is
unobservable by a vast margin; the refutation is of the *mechanism*, not of the theory's
observable face.

Two ways to close the tension remain, and both are cheap:

```text
(i)  P7'-SCOPED (recommended): P7' is exact only in the a -> 0 idealization; the Planck-range
     scalaron is a controlled O(a^2) correction WITHIN the postulate, same shape as the F1
     expansion leak P7' already carries. Nothing about the observable predictions changes.

(ii) STRICT EXACTNESS: impose f''(Delta_0) = 0 -- an inflection of the wedge energy at the
     frustrated ground state -- which kills the R^2 class exactly but costs an unmotivated
     constraint on f unless a microphysical reason for it turns up.
```

Recommendation on record is (i), by precedent and economy. Either route leaves every matched
coefficient and every falsifier untouched -- this is a scoping ruling, not a new adoption.

**Proof:** archive record `scalaron_unimodular_047`, verified against `f = R + alpha R^2` on
FRW with no field equations imposed →
[../theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md)

**Where next:**
- [The Expansion Point →](thm_expansion_point.md) — where the R^2-class term this scalaron rides on actually comes from.
- [Lambda as an Integration Constant →](thm_lambda_integration_constant.md) — the same Bianchi-plus-unimodular trick, but where it works instead of failing.
- [The Graveyard →](hub_graveyard.md) — other mechanisms tried and refuted in-house, same even tone.
- [Einstein Closure →](thm_einstein_closure.md) — the master result this tension sits underneath; see why it survives the kill unscoped.
