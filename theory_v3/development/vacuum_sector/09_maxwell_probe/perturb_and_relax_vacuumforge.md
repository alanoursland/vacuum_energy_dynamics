# VacuumForge: Perturb and Relax -- Is the Energy Density Characteristic?

## Status

```text
result type:   numerical experiment (stage 3; 2026-11-24, derivation 063);
               TRIAL angle energy, K = 1
questions:     does forced barrier continuation steer the relaxation
               to a different endpoint? Once kicked out of the first
               configuration they settled into, do the quanta shed more
               strain or return to 062's band?
satisfies:     p10_preparation_dependence_063 (first pass)
data:          vacuum_forge/src/vacuum_sector/063_perturb_and_relax/perturb_063.csv
verification:  vacuum_forge/src/vacuum_sector/063_perturb_and_relax/
```

## Measured Results

```text
E1. PATH SENSITIVITY (N = 160, seed 1; no fallback was needed in 062):
    standard relaxation:     E_w/vol 4.3452 (fixed point, 21 rounds), anisotropy 0.0207
                             (062 recorded 4.3452)
    forced continuation:     E_w/vol 4.3452 (fixed point, 21 rounds), anisotropy 0.0207
    shared tetrahedra 100.0%; fabric overlap +1.000

E2. PERTURB AND RELAX (N = 320; endpoints regenerated and matched
    to 062; Gaussian kicks of rms sigma x mean edge; Delaunay rule):
    seed 1  sigma 0.10  kick 0:  5.2597 -> 4.9129 (-0.3468)   kick changed  14%   shared after  81%   n=5 0.363   aniso 0.0118
    seed 1  sigma 0.10  kick 1:  5.2597 -> 4.9270 (-0.3327)   kick changed  14%   shared after  81%   n=5 0.365   aniso 0.0102
    seed 1  sigma 0.25  kick 0:  5.2597 -> 5.1975 (-0.0621)   kick changed  60%   shared after  40%   n=5 0.360   aniso 0.0141
    seed 1  sigma 0.25  kick 1:  5.2597 -> 5.2741 (+0.0144)   kick changed  59%   shared after  35%   n=5 0.354   aniso 0.0051
    seed 2  sigma 0.10  kick 0:  5.3144 -> 4.7228 (-0.5916)   kick changed  15%   shared after  80%   n=5 0.380   aniso 0.0114
    seed 2  sigma 0.10  kick 1:  5.3144 -> 4.7622 (-0.5522)   kick changed  13%   shared after  83%   n=5 0.361   aniso 0.0138
    seed 2  sigma 0.25  kick 0:  5.3144 -> 5.0639 (-0.2505)   kick changed  60%   shared after  38%   n=5 0.367   aniso 0.0164
    seed 2  sigma 0.25  kick 1:  5.3144 -> 5.3744 (+0.0600)   kick changed  57%   shared after  42%   n=5 0.345   aniso 0.0096
    seed 3  sigma 0.10  kick 0:  4.8854 -> 4.9345 (+0.0491)   kick changed  14%   shared after  81%   n=5 0.395   aniso 0.0117
    seed 3  sigma 0.10  kick 1:  4.8854 -> 4.9524 (+0.0670)   kick changed  17%   shared after  79%   n=5 0.383   aniso 0.0069
    seed 3  sigma 0.25  kick 0:  4.8854 -> 5.1080 (+0.2226)   kick changed  57%   shared after  42%   n=5 0.360   aniso 0.0041
    seed 3  sigma 0.25  kick 1:  4.8854 -> 4.7125 (-0.1729)   kick changed  54%   shared after  46%   n=5 0.391   aniso 0.0128
    seed 4  sigma 0.10  kick 0:  5.2430 -> 4.8968 (-0.3462)   kick changed  14%   shared after  80%   n=5 0.367   aniso 0.0156
    seed 4  sigma 0.10  kick 1:  5.2430 -> 4.9897 (-0.2534)   kick changed  16%   shared after  77%   n=5 0.370   aniso 0.0088
    seed 4  sigma 0.25  kick 0:  5.2430 -> 5.4887 (+0.2457)   kick changed  60%   shared after  41%   n=5 0.343   aniso 0.0142
    seed 4  sigma 0.25  kick 1:  5.2430 -> 4.8511 (-0.3919)   kick changed  58%   shared after  37%   n=5 0.378   aniso 0.0087

    by amplitude:
    sigma 0.10: change -0.2884 +- 0.2425; kick changes 15% of tetrahedra; relaxed packings share 80% with the original; anisotropy 0.0113
    sigma 0.25: change -0.0418 +- 0.2236; kick changes 58% of tetrahedra; relaxed packings share 40% with the original; anisotropy 0.0106
    original endpoints 4.8854 .. 5.3144; all relaxed kicks
    4.7125 .. 5.4887; kicks ending >5% below their origin: 6 of 16
```

## Fences

```text
- TRIAL angle energy, K = 1.
- four endpoints, two amplitudes, two kicks each: a first look at
  preparation dependence, not a search for the global minimum.
- endpoints are local results of the Delaunay-rule iteration.
- no EM coupling.
```

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     062's Delaunay-rule driver and relaxations imported
             unchanged; continuation as in 062's fallback.
validation:  another Claude Code session with GPU access should rerun
             this module (perturb_063.csv to ~1e-6) and extend it:
             more kicks, annealing schedules, and larger N.
```

## Ledger

```text
derivation:  perturb_and_relax_063
satisfies:   p10_preparation_dependence_063
depends on:  neighbour_ensemble_062
```
