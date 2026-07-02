# The 4D Ground Coordination (O-P10-2) -- VacuumForge Record

## Status

```text
result type:   ground-state structure theorem, mean-field (2026-07-02,
               derivation 050)
conclusion:    the flat 4D ground state selects NEITHER n = 4 nor n = 5
               purely -- it is a FORCED MIXTURE with exact fractions
               x_4 = 5 - 2 pi/arccos(1/4) = 0.233208
               x_5 = 2 pi/arccos(1/4) - 4 = 0.766792
               mean coordination n_bar = 2 pi/arccos(1/4) = 4.766792
               -- parameter-free structural numbers of the 4D vacuum.
fence:         MEAN-FIELD (deficits treated as independently assignable);
               realizability in a periodic triangulation is opened as
               mixture_realizability_050, joint with O-P10-5.
verification:  vacuum_forge/src/vacuum_sector/050_4d_ground_coordination/
```

## The Question and the Answer's Shape

O-P10-2 asked which coordination the 4D ground state selects, given
that n = 4 and n = 5 around a triangle hinge carry opposite-sign
deficits. The question presupposed a single winner. The answer is that
the flatness of the ground state (037/041) makes a single winner
impossible:

```text
delta(n) = 2 pi - n arccos(1/4):
    n = 3: +133.44 deg     n = 5:  -17.61 deg
    n = 4:  +57.91 deg     n = 6:  -93.13 deg

- n = 5 is the SOFTEST wedge (smallest |delta|; confirmed by the 4D
  relaxation lab below) -- the same selection as 3D.
- but every hinge of a pure n = 5 packing carries negative deficit:
  by the Regge encoding (039) that configuration is negatively
  curved, not flat.
- the flat ground state must therefore mix, and zero mean deficit
  fixes the mixture EXACTLY: x_4 delta(4) + x_5 delta(5) = 0.
```

## The Payoff: Flatness Is Bought

The mixed floor is strictly positive and exactly computable
(quadratic witness): E/hinge = x_4 delta_4^2 + x_5 delta_5^2 =
0.310691 rad^2, sitting strictly between the pure-n=5 and
pure-n=4 costs. The vacuum pays ~23% expensive n = 4 hinges as the
price of zero curvature. This is the substance-energy identity (038)
in its sharpest form: the frustration floor is not incidental to
flatness -- it is flatness's PRICE, and both the price and the
mixture are functions of arccos(1/4) alone.

## The 4D Wedge-Ring Lab (numerical face)

Relaxed spring energy of n regular 4-simplices sharing a fixed unit
triangle hinge (scipy BFGS, the 041 pattern lifted to R^4):

```text
    n = 3:  E = 0.197289
    n = 4:  E = 0.047293
    n = 5:  E = 0.004778
    n = 6:  E = 0.135732
    n = 7:  E = 0.435967
```

Strict minimum at n = 5 with positive residual: 4D frustration is
real and measured, one dimension up from 041 E2.

## What This Does NOT Settle

```text
- realizability: which hinge fractions actual periodic 4D
  triangulations achieve (mixture_realizability_050; the natural
  cross-check is the coordination statistics of 4D Delaunay
  complexes) -- joint with O-P10-5.
- the (3+1) question: the SPATIAL 3D packing (edge hinges,
  arccos(1/3), all-positive ground deficits at n = 5) and the
  Euclidean-4D packing (triangle hinges, arccos(1/4), mixed-sign
  ground hinges) are different objects; which the Lorentzian vacuum
  instantiates belongs to O-P10-4.
- no observable moves: the mixture is a structural (sub-Planckian)
  statement; its long-wavelength shadow is exactly the flat, EH-
  responding vacuum already derived.
```

## Ledger

```text
derivation:  ground_coordination_4d_050
satisfies:   o_p10_2_resolved_meanfield_050 (O-P10-2 at mean-field)
opens:       mixture_realizability_050 (joint with O-P10-5)
depends on:  lorentzian_4d_lift_043, frustration_relaxation_lab_041,
             p10_adoption_record_044
watch:       ground-state isotropy (guards 049's selector closure):
             the mixture must not order anisotropically -- a face for
             the O-P10-5 lab.
```
