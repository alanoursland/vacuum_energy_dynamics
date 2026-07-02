# The P7' Scoping Ruling (Route i) -- VacuumForge Record

## Status

```text
result type:   theory-owner scoping ruling (2026-07-02, derivation 048)
ruling:        ROUTE (i) ADOPTED. P7' is scoped as the double
               idealization H -> 0 (static; F1 kappa-leak correction)
               AND a -> 0 (continuum; packing-scalaron correction).
               O-P10-3 is CLOSED against this ruling.
rejected:      route (ii), the f''(Delta_0) = 0 inflection constraint --
               recovery-shaped without independent motivation; retained
               on record as the fallback.
verification:  vacuum_forge/src/vacuum_sector/048_p7prime_scoping_ruling/
               (witnesses re-verified at ruling time; dependencies 047, 044)
```

## What the Ruling Says

"The four-derivative sector is exactly empty" (P7', proof.md Theorems
6-7) is a statement about the continuum idealization a -> 0. At finite
packing scale the R^2-class term exists with coefficient
alpha ~ f''(Delta_0) a^2-class, and derivation 047 proved its scalaron
survives the unimodular constraint (the Bianchi reconstruction). The
ruling scopes the postulate rather than constraining the wedge energy:

```text
P7' holds exactly in the (H -> 0, a -> 0) idealization.

The physical vacuum carries exactly two derived corrections to the
static shadow, both controlled, both sub-observable:

  expansion:     AB - 1 = (3/2) Omega_m (H0 r/c)^2     (trial F1)
  discreteness:  Yukawa of range l* = sqrt(6 alpha) ~ sqrt(6) a
                 ~ 4e-35 m at Planck packing              (047)

Each is quadratic in its small parameter; neither reopens a closed
coefficient; neither is observable at any accessible range.
```

## The Limit-Result Reading (the owner's observation, made doctrine)

The field-equation derivation's "no static flow, exactly zero"
statements were always candidates for limit results rather than
exact-at-all-scales facts. This ruling makes that the official
reading: exactness lives in the idealization; the physical packing's
deviations from it must be DERIVED, CONTROLLED, and INDIVIDUALLY
RECORDED -- never assumed away, never invoked ad hoc. The register of
such corrections currently has exactly two entries (above). Any third
must arrive the same way: with a derivation, a magnitude, and a kill
condition.

## What Does Not Change

```text
- every closed field-equation coefficient (the corrections do not
  reopen the response)
- the A3/F-P10-3 null test: any DETECTED gravitational-strength
  Yukawa at any accessible range still kills -- the scoped reading
  predicts NONE will ever be found short of the packing scale
- the E3/G20 kills of macroscopic higher-curvature couplings
- the sequestering chain, Lambda as integration constant, the
  floor's inertness
```

## The New Falsifier Face

The ruling adds a sharpened structural commitment: if the packing
scale a were ever independently measured (any confirmed discreteness
probe), the theory PREDICTS a scalaron Yukawa at range sqrt(6) a with
the wedge-energy coefficient -- a parameter-free consistency test
between two would-be discoveries. Recorded alongside C4 (the
floor-Newton lock) as the second entry in the "if discreteness is ever
seen" consistency battery.

## Ledger

```text
derivation:  p7prime_scoping_ruling_record_048
satisfies:   p7prime_scoping_ruling_047 (and closes O-P10-3)
rejected:    route (ii) f''(Delta_0) = 0 (fallback, on record)
depends on:  scalaron_unimodular_047, p10_adoption_record_044,
             trial F1 (precedent)
```
