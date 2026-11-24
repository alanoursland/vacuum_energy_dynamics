# VacuumForge: Letting the Quanta Change Neighbours

## Status

```text
result type:   numerical experiment (stage 3 step 2, one seed;
               2026-11-24, derivation 061); TRIAL angle energy, K = 1
question:      when spatial quanta can move far enough to acquire new
               geometric neighbours, how much of the strain seen in 060
               remains, and does it still point in the direction
               favoured by the starting mesh?
satisfies:     p10_bulk_neighbour_changes_060 (one seed)
opens:         p10_neighbour_ensemble_061
endpoints:     vacuum_forge/src/vacuum_sector/061_neighbour_changes/
               packing_061.npz (content sha256 fc72609da8f191a3...)
verification:  vacuum_forge/src/vacuum_sector/061_neighbour_changes/
```

## Two Neighbour Rules

```text
A  VED's Delaunay adjacency: neighbours = periodic Delaunay
   triangulation of the current positions; relax, re-triangulate,
   repeat to a fixed point or a cycle.
B  energy-selected neighbours: any valid periodic 2-3 / 3-2 flip that
   lowers E_w, in random order, alternated with relaxation; replayed
   over flip orders [1, 2, 3].
energy:  E_w = sum over (tet, edge) of l_e (1/2)(theta - arccos(1/3))^2
         (the 060 P10 candidate), barrier mu = 0.001 during relaxation
checks:  after every round: E = V + T, sum n_h = 6T,
         sum (6 - n_h) = 6V, all volumes positive and summing to L^3,
         every hinge closes; every accepted flip conserves volume and
         lowers E_w.
```

## Measured Results

```text
                           E_w       E_w/vol  unavoid.   extra    hinge len   T     aniso   ov.start  ov.060
    060 start (057 mesh)     948.550  12.58545   441.129   553.039   1214.35   1078  0.0275  +0.884  +1.000
    A: Delaunay restored     824.874  10.94451   339.081   509.139   1161.08   1044  0.0187  -0.651  -0.884
    A: endpoint              368.818  4.89351   194.957   214.465   1072.76    993  0.0218  -0.225  -0.255
    B: flips, order 1        363.824  4.82726   139.737   247.487   1056.95    958  0.0189  +0.825  +0.683
    B: flips, order 2        359.023  4.76356   143.366   238.741   1051.29    953  0.0273  +0.507  +0.309
    B: flips, order 3        376.209  4.99158   144.845   254.424   1054.69    956  0.0277  +0.249  +0.142
(unavoidable and extra are the unweighted per-hinge sums; ov = overlap
of the deviatoric energy fabric, +1 = same pattern)

Coordination histograms (n: number of hinges):
    060 start:   {3: 160, 4: 309, 5: 273, 6: 239, 7: 143, 8: 85, 9: 20, 10: 7, 11: 2}
    A endpoint:  {3: 40, 4: 274, 5: 439, 6: 280, 7: 96, 8: 21, 9: 3}
    B order 1:   {4: 304, 5: 461, 6: 258, 7: 81, 8: 14}
    B order 2:   {4: 318, 5: 433, 6: 263, 7: 89, 8: 10}
    B order 3:   {4: 318, 5: 438, 6: 258, 7: 90, 8: 12}

Rule A history (fixed point; restoring Delaunay at 060's coordinates
changed ~426 tetrahedra):
    round  1: relaxed E_w 698.9294; re-Delaunay changes 194 tets -> E_w 622.6403
    round  2: relaxed E_w 565.1709; re-Delaunay changes 95 tets -> E_w 518.9882
    round  3: relaxed E_w 487.1319; re-Delaunay changes 73 tets -> E_w 526.7723
    round  4: relaxed E_w 501.1276; re-Delaunay changes 49 tets -> E_w 477.5338
    round  5: relaxed E_w 461.7027; re-Delaunay changes 37 tets -> E_w 480.7219
    round  6: relaxed E_w 464.6886; re-Delaunay changes 51 tets -> E_w 428.1177
    round  7: relaxed E_w 413.3872; re-Delaunay changes 16 tets -> E_w 418.8667
    round  8: relaxed E_w 411.9647; re-Delaunay changes 10 tets -> E_w 405.7768
    round  9: relaxed E_w 401.5454; re-Delaunay changes 10 tets -> E_w 395.8092
    round 10: relaxed E_w 392.0707; re-Delaunay changes 15 tets -> E_w 381.4404
    round 11: relaxed E_w 377.7486; re-Delaunay changes 5 tets -> E_w 380.0284
    round 12: relaxed E_w 377.7603; re-Delaunay changes 10 tets -> E_w 390.6047
    round 13: relaxed E_w 386.9999; re-Delaunay changes 7 tets -> E_w 382.4217
    round 14: relaxed E_w 379.1797; re-Delaunay changes 6 tets -> E_w 374.9902
    round 15: relaxed E_w 372.7823; re-Delaunay changes 2 tets -> E_w 379.1510
    round 16: relaxed E_w 377.8473; re-Delaunay changes 2 tets -> E_w 386.5762
    round 17: relaxed E_w 384.7626; re-Delaunay changes 7 tets -> E_w 371.8395
    round 18: relaxed E_w 368.8176; re-Delaunay changes 0 tets -> E_w 368.8176

Rule B:
    order 1: 0 2-3 and 120 3-2 flips in 2 rounds
    order 2: 0 2-3 and 125 3-2 flips in 2 rounds
    order 3: 0 2-3 and 122 3-2 flips in 2 rounds
    replay spread of E_w across orders: 17.1859 (mean 366.352);
    fabric overlaps between orders: [0.869, 0.704, 0.91]
    every accepted flip was 3-2. Round-trip test (3-2 then 2-3 on the
    created face, 5 cases): originals restored with the opposite energy
    change. 2-3 census at the endpoints (valid candidates, smallest
    dE): order 1: 1150, +2.5945; order 2: 1129, +2.4969; order 3: 1109, +2.4742.
    Every valid 2-3 flip creates an n = 3 hinge and raises E_w, so
    greedy descent can only remove n = 3 edges.
```

## Reading

- **Moving quanta with geometric (Delaunay) neighbours releases most of
  the fixed-neighbour strain.** Rule A takes E_w from 948.5 to
  368.8 (61% released). The unavoidable coordination cost
  falls from 441.1 to 195.0 as the histogram moves toward n = 5, and
  the uneven-sharing extra from 553.0 to 214.5. Restoring Delaunay
  adjacency at 060's own coordinates already lowers E_w to
  824.9. The iteration is not monotone (re-triangulation can
  raise E_w), but it reaches a fixed point: a packing that is both
  Delaunay and relaxed.
- **Energy-selected flips reach about the same energy, by a different
  route.** Rule B ends at 359.0–376.2, within its own order-to-order spread
  of rule A. Its greedy flips remove every n = 3 edge but cannot make
  the uphill 2-3 moves that would open other rearrangements. It ends
  with a lower unavoidable cost but more uneven-sharing extra than
  rule A.
- **Energy per volume is similar across rules:** 4.89 (A) and
  4.76–4.99 (B), against 12.59 with neighbours fixed. Whether
  that number is reproducible across seeds and sizes is the ensemble's
  question.
- **Direction.** Rule A loses the starting mesh's orientation (overlap
  -0.22). Rule B keeps a variable amount of it (+0.25 to
  +0.82 across orders). The strong alignment seen in 060 was
  largely a property of the frozen triangulation.
- **What this says, for one seed.** Most of the excess disappears in
  both runs, so moving quanta and updating their geometric neighbours
  is enough to release it. The theory needs no extra neighbour-choice
  rule to reach this level, although greedy flips are a weak search
  (see Fences).
- **Still far above the floor.** If every hinge sat at n = 5 the
  unavoidable cost would be about 0.0016 per unit hinge length. Mixed
  coordination keeps it near 195. The positive floor 059 predicts
  is present, but this packing is nowhere near it.

## Fences

```text
- TRIAL angle energy (059/060), K explicit.
- one seed, one size, one cubic box; endpoints are local results of
  the stated procedures (greedy flips, Delaunay iteration), not global
  minima. The ensemble is p10_neighbour_ensemble_061.
- rule B is greedy: it cannot pass through the uphill 2-3 moves, so it
  bounds what local energy-selected flips can reach only from above.
  Composite moves (4-4 flips) or annealing would search further.
- no EM coupling.
```

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     incremental face/edge maps and per-tetrahedron energies
             make each flip test local; relaxation reuses 060's exact
             per-tetrahedron Hessian and eigenvalue-modified Newton.
validation:  another Claude Code session with GPU access should rerun
             this module, confirm the saved endpoints' content hash
             (or the endpoint energies and histograms), and then run
             the ensemble (p10_neighbour_ensemble_061) at larger N,
             where the GPU makes the relaxations practical.
```

## Ledger

```text
derivation:  neighbour_changes_061
satisfies:   p10_bulk_neighbour_changes_060 (one seed)
opens:       p10_neighbour_ensemble_061
depends on:  angle_energy_fixed_neighbors_060, periodic_spring_control_057
```
