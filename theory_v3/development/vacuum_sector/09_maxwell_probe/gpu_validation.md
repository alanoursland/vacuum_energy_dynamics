# GPU Validation of Forges 056–061

## Status

```text
result type:   independent rerun + GPU cross-check (2026-11-24); a
               validation record, not a derivation
conclusion:    every recorded number in 056-061 reproduces on independent
               hardware. One verification check fails here (057 E4,
               mu = 1e-3: Newton stop test at the roundoff floor; same
               minimum). Saved-packing hashes differ only by a rigid
               translation of all vertices (~1e-3), the periodic
               energy's exact zero mode. Independent GPU optimizers and a
               sparse GPU eigensolver reach the same minima and the same
               phase speeds. At N = 160 the GPU is SLOWER than the CPU.
scope:         one seed, N = 160, as in the forges; capacity numbers
               below are measured kernel costs plus stated assumptions
code:          vacuum_forge/src/vacuum_sector/gpu_validation/
```

## Hardware and Software

```text
GPU        NVIDIA GeForce RTX 3080 Ti, 12 GB (WDDM; ~1.7 GB held by the
           desktop), driver 610.88, CUDA (driver) 13.3
           measured fp64 dense matmul ~0.45 TFLOPS (consumer GA102)
CPU path   Windows 11, Anaconda Python 3.11.7, NumPy 1.26.4 (OpenBLAS
           0.3.23), SciPy 1.10.1, SymPy 1.12, NetworkX 3.1, pydantic
           2.11.7; OPENBLAS_NUM_THREADS=1
GPU path   PyTorch 2.3.0 (CUDA 11.8 build), float64 / complex128
repo       main at 6436e84e (pull request 26 merged)
```

## Step 1: Independent CPU Rerun

All nine modules ran in order from `vacuum_forge/src/vacuum_sector/`
(upstream 039, 041 and 051 first, to populate the local archive).

```text
module   wall    verification   recorded numbers
039      2.8 s   pass           (upstream)
041      2.3 s   pass           (upstream)
051     10.5 s   pass           (upstream)
056      7.4 s   pass           triplets 2.10292445 (x3), 8.90813092 (x3);
                                1% stretch 2.08334853 (x2), 2.13210754:
                                identical (checks at 1e-8)
057     20.3 s   1 FAIL         see below; every printed number identical
058     78.7 s   pass           G3a-G3c pass; report text identical; CSV
                                phase speeds within 1.0e-10 of committed
059      3.2 s   pass           identity to 1e-12; spring ring 0.000649;
                                all-dihedral minimum 0.00197300: identical
060     30.6 s   pass           E_u 976.709, E_w 948.548, unavoidable
                                441.129, overlaps: identical; report
                                differs only in the hash and one virial
                                trace (-1.1e-07 vs -5.7e-08; check is
                                |trace| < 1e-5)
061     59.0 s   pass           rule A: fixed point after 18 rounds, E_w
                                368.8176; rule B orders 1-3: 363.824,
                                359.023, 376.209; every round, flip count,
                                histogram and 2-3 census line identical;
                                report differs only in the hash
```

Reports regenerated on Windows also change line endings (CRLF). None of
the regenerated reports or data files were committed; the committed ones
are kept.

**057 discrepancy (explained).** E4's warm-started Newton at
mu = 1e-3 stops at 500 iterations with max|g| = 1.15e-9 against the
1e-11 stop test. Trace: |g| reaches 9e-8 at step 16, where the energy is
flat to ~1e-15 relative; the Armijo test cannot see a decrease below the
energy's floating-point resolution, the damping grows, and |g| stalls.
The cloud run happened to cross 1e-11; this machine's BLAS rounding does
not. It is the same minimum: the warm-started mu = 1e-4 packing from the
stalled point equals the committed `x_weak` to 8.6e-12, and E/N, minimum
volume, anisotropy and axis rotations print identically. (A full Newton
step from the stalled point converges to 5e-14 but moves every vertex by
the same vector, max 0.017: a rigid translation, non-rigid part 1.5e-9.)
Forge 062 already carries a roundoff-aware polish for the same stall;
057 itself was not changed.

**Hash differences (explained).** 057 (regenerated), 060 and 061
packings get new content hashes here. In every case the coordinate
difference from the committed file is a rigid translation:

```text
packing   array                max |dx|    non-rigid part
060       x_weighted(_weak)    9.75e-04    2.8e-15, 1.5e-15
060       x_unweighted(_weak)  1.73e-04    1.2e-14, 4.2e-14
061       x_delaunay           9.66e-04    7.8e-16
061       x_flips_1..3         9.8e-04     5.1e-16 .. 7.3e-16
061       T_*, O_* (ints)      identical
```

The periodic energies are invariant under translating every vertex,
so their Hessians have three exact zero modes. The forges'
eigenvalue-modified Newton floors |lambda|, so the step along those
modes is set by roundoff and differs between machines. Geometry,
connectivity and every reported quantity are unaffected. 058–061 were
then run against the committed (hash-verified) 057/060 inputs.

## Step 2: GPU Validation

The GPU scripts read the forges' saved packings but share no numerical
code with them (`gpu_common.py`, `gpu_maxwell.py`). Gradients come from
autograd. Hessians are assembled sparse on the GPU from per-term local
Hessians (`torch.func.vmap(hessian)`). The optimizer is trust-region
Newton-CG (Steihaug, 3x3 block-Jacobi preconditioner, translations
projected out), plus FIRE as a descent-path reference. The Maxwell
operators are sparse Bloch-twisted Whitney matrices assembled per
tetrahedron, with a complex LOBPCG.

### 057: spring control — PASS (with a basin note)

```text
committed x (mu = 1e-2): GPU autograd max|g| = 8.48e-12 (report 8.5e-12);
  Hessian: 3 translation zeros, next eigenvalue 0.4531 (strict minimum)
FIRE then TR, from x_initial, warm-started in mu:
  mu      E/N        min V/V_ref  aniso     vs committed (non-rigid |dx|, axes)
  1e-2    0.288856   0.014865     0.03289   2.0e-11, <= 8.5e-07 deg
  1e-3    0.286968   0.001641     0.03173   (no committed coordinates)
  1e-4    0.286769   0.000165     0.03223   1.2e-14, <= 1.7e-06 deg
  all match the report to printed precision; dE/E <= 5e-14
```

**Basin note.** Trust-region Newton-CG run directly from `x_initial`, at
any of three initial radii, converges (max|g| 1e-14) to a different
strict local minimum: E/N = 0.289260 (+0.14%), min V 0.014196,
anisotropy 0.03031 (−8%), principal axes rotated 4–7 deg, non-rigid
|dx| = 0.49. FIRE, a damped-dynamics method close to gradient flow,
drains `x_initial` into the committed minimum. 057's endpoint is
therefore the descent-path minimum, but a different second-order path
reaches a neighbouring basin. For `spring_control_ensemble_057`, this
gives a scale for optimizer-path variation within one seed. That
variation should be separated from seed-to-seed variation. This is
recorded only; nothing in 057 is changed.

### 058: ordinary Maxwell (fork (a)) — phase speeds PASS; 1 solver check FAIL

```text
operators   Whitney commuting property curl W1 = W2 d1: 1.0e-15;
            d1 d0 = 0: 2.7e-16; local C^T M2 C assembly = global
            d1^H M2 d1: 2.5e-16
G3a         M1 min eig 6.2291e-02, M2 min eig 2.8341e-01 (report 6.229e-02,
            2.834e-01); rank d0 = 159, nullity d1 = 162, 3 harmonic dims
G3b         |d1 U| 8.9e-16, |d0^T M1 U| 4.6e-15, energy/Vol = I,
            principal cosines 1, 1, 1
G3c         ka 0.05 / 0.1 [111]: rank d0(k) = 160, 160 zero modes; LOBPCG
            omega^2 = 0.002574, 0.002574, 1.98255 / 0.010292, 0.010293,
            1.918653 (= report)
dispersion  27 points x 2 polarizations vs dispersion_058.csv:
            max |dv| = 6.7e-11; gap ratios to 1e-6 relative
```

The eigensolver removes gradients by a spectral shift,
K + s·M1 G A0⁻¹ Gᴴ M1 with s = 10. This puts every gradient mode at
ω² = s exactly and leaves the divergence-free spectrum unchanged. A
first version that only projected the search directions converged to
spurious ω² ≈ −1e-14: roundoff leaks gradient components, which are
exact zero modes of K, and LOBPCG amplifies them. That failure is not
in the forge.

**Failing check, recorded.** LOBPCG reached its 3000-iteration cap at
the 9 dispersion points with ka ≤ 0.1 and in both G3c solves. At
ka = 0.2 it took 559–1982 iterations; elsewhere it took 114–142. The
1e-10 relative-residual target is too tight for these small ω². At the
capped points the final residuals are 3e-9 to 1.5e-5, and the
divergence of the returned vectors, |GᴴM1x|/|M1x|, is 1e-9 to 2.5e-5.
The divergence check, with a 1e-10 threshold, therefore fails. The
eigenvalues are second-order in the residual and still match the CSV
to 7e-11 in v. A looser residual target or a better preconditioner
would avoid the cap; neither was rerun.

### 060: angle energy, neighbours fixed — PASS (1 convergence flag)

```text
committed x_unweighted / x_weighted (mu = 1e-3): GPU max|g| 2.1e-12 /
  7.4e-12; Hessians positive beyond translations
TR from 057 x_initial (warm-started in mu):
               mu      E_angle    unavoidable  extra      non-rigid |dx|
  unweighted   1e-3    976.7102   441.1291     535.5811   1.5e-13
               1e-4    976.7091   441.1291     535.5801
               1e-5    976.7090   441.1291     535.5800   5.7e-14
  weighted     1e-3    948.5497   441.1291     553.0394   1.1e-15
               1e-4    948.5485   441.1291     553.1142
               1e-5    948.5484   441.1291     553.1220   1.9e-15
fabric anisotropies (GPU = committed = report to 4 digits):
  0.02476 / 0.02754 / 0.02687 / 0.02869 / 0.03223 / 0.02024
overlaps (GPU, report): w-spring +0.9057 (+0.906); u-spring +0.9017
  (+0.902); w-u +0.9897 (+0.990); w-start +0.8839 (+0.884);
  spring-start +0.9160 (+0.916); extra_w-spring +0.6539 (+0.654)
```

FIRE followed by TR reaches the same minima, non-rigid |dx| ≤ 6e-13
(`diag_060_basins.py`). **Flag:** at weighted mu = 1e-5 the trust region
stopped at max|g| = 2.1e-10 against a 1e-10 target. This is a
roundoff-floor stop like 057's. The point equals the committed one to
1.9e-15.

### 061: neighbour changes — PASS (endpoint level)

```text
endpoint   T     E_w       histogram   max|g| saved   perturbed 1e-3 -> |dx|
A          993   368.8176  = report    7.9e-14        8.0e-14
B order 1  958   363.8241  = report    5.3e-14        3.5e-14
B order 2  953   359.0234  = report    1.1e-12        1.8e-14
B order 3  956   376.2093  = report    5.2e-14        6.5e-14
all four: exact mesh identities (E = V + T, sum n = 6T, sum(6 - n) = 6V,
volumes positive and summing to L^3, every hinge closed)
rule A: an independent periodic Delaunay of the saved coordinates
reproduces the saved tetrahedra exactly (the fixed point)
```

The full rule-A iteration and the rule-B flip search were not rerun on
the GPU. Their re-triangulation and flip bookkeeping are CPU work, the
CPU rerun already reproduces them line for line, and at this size GPU
relaxations are slower.

## Timings

```text
               CPU (this machine; report)          GPU (this work)
057 relax      0.7 s at mu = 1e-2 (< 1 s)          FIRE+TR 2.0 / 1.3 / 36.5 s
                                                   (1e-2 / 1e-3 / 1e-4; FIRE is
                                                   slow at weak barriers; TR alone
                                                   ~0.6 s per warm start)
058 per k      ~1.5 s dense (report)               0.8-1.5 s converged points;
               module 78.7 s                       ~20 s at the 9 capped points;
                                                   mean 9.6 s
060 relax      module 30.6 s ("seconds per run")   TR 0.6-5.5 s per mu; ~13 s
                                                   for all six
061            module 59.0 s                       endpoint checks ~2 s
```

At N = 160 every GPU kernel is latency-bound (gradient 3 ms, sparse
Hessian 17 ms, regardless of size), and consumer fp64 is slow. The GPU
offers nothing for the forges as they stand. Its value is at larger N.

## Capacity of the 12 GB Card (measured kernels, `gpu_capacity.py`)

Synthetic Poisson packings: periodic Delaunay, unit mean edge, no
relaxation.

```text
N        T        sparse Hessian (assembly peak, time)   gradient    SpMV
1000     6771     spring 115 MB / 11 ms;  angle 226 MB / 17 ms    2-4 ms   0.03 ms
4000     27062    spring 452 MB / 16 ms;  angle 853 MB / 30 ms    4-6 ms   0.03 ms
16000    108308   spring 1.8 GB / 46 ms;  angle 3.4 GB / 102 ms   6-40 ms  0.08 ms
Maxwell (k along [111], ka = 0.1; CG gradient projector):
1000     nE 7771    LOBPCG 0.28 s/iteration (~150 CG its/projection), 38 MB
4000     nE 31062   LOBPCG 1.16 s/iteration (~237 CG its/projection), 156 MB
```

Memory scales linearly: about 113 kB (spring) and 213 kB (angle) per
vertex. Almost all of it is the unchunked COO staging of the per-term
Hessians. With ~10 GB usable:

```text
obligation                     limit (single sample)        estimate
spring_control_ensemble_057    N ~ 8e4 by memory            seeds run sequentially;
                                                            ensemble size is time-
                                                            limited, not memory-limited
p10_neighbour_ensemble_061     N ~ 4.5e4 by memory          GPU relaxation per round is
                                                            not the bottleneck: scipy
                                                            Delaunay (27 images) and the
                                                            Python flip bookkeeping are
                                                            CPU-bound and need porting
                                                            first (062 runs N <= 320 on
                                                            CPU)
maxwell_packing_sweep          memory not limiting          time-limited by the gradient
                               (N = 4000: 156 MB)           projector: ~1.2 s per LOBPCG
                                                            iteration at N = 4000; ~130
                                                            iterations per converged k
                                                            at N = 160 => ~2.5 min per k
                                                            at N = 4000 if counts hold
```

**Assumptions, not measured.** Iteration counts to convergence at large
N are taken from the N = 160 runs: TR 20–250 iterations, LOBPCG ~130.
They will grow, since the barrier contact sets get larger and the
folded-mode gap narrows as the box grows. Per-sample time at N ~ 1e4 is
therefore estimated at minutes, not measured. Chunked Hessian assembly
would raise the memory limits several-fold. A multigrid or sparse-direct
vertex-Laplacian solve would cut the Maxwell projector cost, which
dominates. Recommended next step: a pilot at N = 4000 (one seed,
spring and angle relaxation to convergence, one Maxwell direction) to
replace these assumptions with measurements.

## How to Run

```text
cd vacuum_forge/src/vacuum_sector/gpu_validation
python gpu_057_spring.py      # ~45 s
python gpu_058_maxwell.py     # ~4.5 min (11 solves hit the LOBPCG cap)
python gpu_060_angle.py       # ~15 s
python gpu_061_endpoints.py   # ~10 s
python gpu_capacity.py        # ~1 min
diag_057_basins.py, diag_060_basins.py: the basin diagnostics above
results/*.json: the numbers quoted here
```

## Fences

```text
- a validation record: no new physics claim; every forge's own fences
  stand unchanged.
- one seed, N = 160; the basin note is one optimizer comparison on one
  seed.
- forge code, reports and saved packings are unchanged; regenerated
  files were not committed.
- capacity estimates combine measured kernel costs with iteration
  counts assumed from N = 160.
```
