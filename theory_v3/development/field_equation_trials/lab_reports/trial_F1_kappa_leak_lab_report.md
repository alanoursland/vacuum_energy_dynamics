# Lab Report: Trial F1 -- The kappa-leak Derived (and Honestly Downgraded)

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/011_trial_F_cosmology/trial_F1_kappa_leak_coefficient.py`
**Experiment type:** Derivation / prediction revision (armchair, exact + linear order)
**Trial:** F (cosmology branch), first script
**Status:** COEFFICIENT CLOSED -- the adoption-note estimate is superseded
**Run date:** 2026-06-12
**Dependencies verified:** P7' adoption record; E3 closure of the local sector.

## Purpose

P7' was adopted with the expansion correction recorded as an *estimate*:
AB - 1 = O(H_0 r/c) (~1e-15 at 1 AU), billed as the framework's first
naturally-sized deviation prediction. With the local sector closed (E3),
the correction is derivable. Derive it; revise the record.

## Results

**T1 (pure-Lambda era: NO leak, exactly).** Schwarzschild-de Sitter with
B = 1/A solves the closed parent's vacuum equations (G + Lambda g = 0,
machinery-verified): **AB = 1 exactly for any Lambda.** P7''s shadow is
not a limit statement in the dark-energy era -- it is exact. The adoption
scoping was too cautious.

**T2 (the O(H r/c) sector is frame, not geometry).** The Painleve form
(-c^2 dt^2 + (dr - Hr dt)^2 + r^2 dOmega^2) is exact de Sitter with all
curvature O(H^2); the O(H) metric content -- the comoving velocity
v = H r -- is curvature-free (flat space in falling coordinates). The
original estimate was tracking the **frame current**, which is gauge in
GR and physical in VED only through substance-frame couplings the closed
sector does not contain (quarantined at the engineering seams).

**T3 (the real leak: second order, matter-sourced, coefficient 3/2).**
Uniform background dust in the quasi-static patch gives
phi = psi = (2 pi G rho/3) r^2, and via the E3 areal shadow and Friedmann:

    AB - 1 = 4 pi G rho r^2 / c^2 = (3/2) (H r/c)^2  per clustering component,

so at the present epoch (Lambda contributing zero by T1):

    AB - 1 = (3/2) Omega_m (H_0 r/c)^2  ~  5.6e-31 at 1 AU.

## Verdict

```text
kappa-leak COEFFICIENT CLOSED, prediction REVISED:
  Lambda era:  AB - 1 = 0 exactly (P7' shadow exact)
  O(H):        frame velocity v = H_0 r (~0.33 um/s at 1 AU); gauge in GR
  matter era:  AB - 1 = (3/2) Omega_m (H_0 r/c)^2  -- derived, parameter-
               free, and hopeless as an observable (~1e-30 class)
The record's O(H_0 r/c) linear-scaling prediction is SUPERSEDED.
```

This is an honest downgrade: the program loses its advertised
"first naturally-sized deviation prediction" and gains a theorem that
P7' is stronger than adopted. The first-order quantity survives only as
the substance-frame velocity -- meaningful exactly insofar as something
couples to the vacuum frame, which is seam territory by standing rule.

## Relation to the program

Second prediction-of-record correction in two days (after the boundary
question). The pattern is consistent: closing the local sector keeps
converting estimates into theorems, and the theorems keep saying "GR,
exactly, plus quarantined novelty." The cosmology branch's live content
is now: Lambda's origin, the structure-era leak profile (registered
obligation), and the dark-sector excess EoS (Trial D2).

## Next steps

1. Banner updates: P7' adoption note (done in this commit), status of
   record (done in this commit).
2. Structure-era leak profile (perturbed cosmology) -- registered.
3. Trial D2 remains the cosmology branch's main physics target.
