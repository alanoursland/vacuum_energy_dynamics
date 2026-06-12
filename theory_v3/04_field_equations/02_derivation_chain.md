# The Derivation Chain: Postulates → Field Equations

Every link below is either a machine-verified theorem (forge script
cited) or a recorded theory-owner adoption. Nothing in the chain is a
fit, and the two adoptions (P9, P7′) were made on structural grounds
*before* their strongest consequences were known.

## The chain

```text
P1-P3a  vacuum = energy = spacetime; constant density;
        curvature = spatial differential of vacuum amount
   |
P6      exchange in gradients (KE changes sourced by vacuum exchange)
   |    -> the source law's structure: density sources curvature flux
   v
AREAL-FLUX LAW   Delta_areal A = (8 pi G/c^2) rho        [02_foundations, C2]
   |
P4/P9   curvature configurations carry energy; that energy gravitates
        at the universal coupling, counted once (P9 fence)
   |    -> the self-coupling bootstrap: Delta_areal s = -(s')^2 + src
   |    -> sign forced NEGATIVE; family selector lambda = -1
   v
SCHWARZSCHILD EXTERIOR, EXACT                            [trial C2, 002]
   |
P7'     static frame indifference (adopted; AB = 1 its shadow)
   |    -> count-once placement forced geometry-side
   |    -> explicit-source placement KILLED                [trial C3, 002]
   v
STATIC SECTOR CLOSED; response normalization N = c^4/8piG  [008 T2]
   |
G02/G03 flat-vacuum uniqueness; TT positivity; ghost exclusion
   |    -> sector-indefinite signature: scalar = constraint (forced),
   |       radiative = positive                            [006]
   v
RADIATIVE BOOTSTRAP: K_T = c^4/16piG, quadrupole G/5c^5    [008]
   |    (P9 self-sourcing at coupling N; pulsar anchor passes)
   |
G20     ghost gate on higher-curvature content:
   |    only a R^2 (a>0) + Gauss-Bonnet survives           [010]
   v
E3      P7' vs the scalaron: hair mandatory for a != 0,
   |    hair violates AB = 1 in static vacuum  ==>  a = 0  [009]
   v
LOCAL SECTOR CLOSED:  S = (c^4/16piG) Int sqrt(-g)(R - 2 Lambda) + GB
   |
F1      kappa-leak derived: Lambda-era exactly leak-free;
   |    matter-era AB - 1 = (3/2) Omega_m (H_0 r/c)^2      [011]
   |
012     vector sector: Lap w = (16piG/c^2) rho v;
        Lense-Thirring; GPB/LAGEOS pass                     [012]
   v
EINSTEIN'S EQUATIONS, ALL SECTORS DERIVED
```

## What was killed along the way (the equations' negative space)

The equations are defined as much by what failed as what passed:

| candidate | killed by | record |
|---|---|---|
| traceless local exchange (v2 core) | exact-recovery contradiction | v2 post-mortem |
| tidal vacuum nucleation (TVN) | up-set theorem, 4.7e33 hierarchy | trial A2 |
| burden-reduction long-range force | repulsive sign, separation-blind | trial C1 |
| explicit-source placement of config energy | breaks P7′ shadow | trial C3 |
| depletion-history dark matter | budget shortfall ≥ 2000× | trial D1 |
| boundary smoothing (β ≠ 0) | P7′ contradiction (mandatory hair) | trial E3 |
| Weyl-class quadratic curvature | TT ghost (residue −1) | gate G20 |
| NS-tidal discovery channel for ℓ\* | bench-top hierarchy ≥ 3×10⁷ | trial E2 |
| linear κ-leak prediction | derived: gauge (frame velocity) | trial F1 |

## Provenance

- Forge scripts: `vacuum_forge/src/field_equation_trials/000…012`
  (each script re-derives its theorems from scratch on every run;
  archive dependency checks enforce the chain's integrity).
- Lab reports: `development/field_equation_trials/lab_reports/`.
- Adoption records: `005_postulate_adoptions` (P9, P7′, with fences).
- The pre-program corpus (103 candidate groups, the projection-origin
  probe, the regularity ladder) is mapped in
  `development/field_equation_candidates/proof_chain_seam_map.md`.
