#!/usr/bin/env python3
"""
perturb_and_relax.py

Derivation 063: is 062's relaxed energy density characteristic of the
model, or of the first configuration the quanta settled into?
(09_maxwell_probe, stage 3; p10_preparation_dependence_063.)

062 found a reproducible stored angle energy per volume (5.18-5.25 at
N = 80-320) under VED's Delaunay rule, with declining anisotropy. Two
questions remain about that number:

  E1. PATH SENSITIVITY. The energy is non-convex, and 062 needed a
      barrier-continuation fallback once. Replay an ordinary successful
      sample (N = 160, seed 1, no fallback in 062) with continuation
      FORCED in every relaxation (mu = 1e-2, then warm-started at
      mu = 1e-3) and compare endpoints: energy per volume, anisotropy,
      fabric overlap, and the fraction of tetrahedra shared. Does the
      fallback only help the solver arrive, or can it steer it?

  E2. PERTURB AND RELAX at N = 320. Regenerate the four Delaunay-rule
      endpoints of 062 (checked against its recorded energies). Kick
      every quantum by an isotropic Gaussian displacement of rms
      amplitude sigma (in units of the mean edge; sigma = 0.10 and 0.25,
      two kicks each), which changes many neighbours; relax back under
      the same Delaunay rule, box and energy law to a fixed point. Do
      the quanta shed more strain once they escape the first
      configuration, or return to the same band?

All definitions are imported from 057/060/061/062 unchanged. Exact mesh
checks after every round (through 062's Delaunay-rule driver).

Fences: TRIAL angle energy, K = 1; four endpoints, two amplitudes, two
kicks each; endpoints are local results; no EM coupling.
"""

import csv
import importlib.util
import math
import time
from pathlib import Path

import numpy as np

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (REPO_ROOT / "theory_v3" / "development" / "vacuum_sector"
               / "09_maxwell_probe" / "perturb_and_relax_vacuumforge.md")
CSV_PATH = SCRIPT_PATH.parent / "perturb_063.csv"
SECTOR = SCRIPT_PATH.parents[1]

DEPENDENCIES = [
    ("ensemble_dep_063", "062_neighbour_ensemble__neighbour_ensemble", "neighbour_ensemble_062"),
]

PATH_SAMPLE = (160, 1)
KICK_N = 320
KICK_SEEDS = (1, 2, 3, 4)
SIGMAS = (0.10, 0.25)
KICKS_PER_SIGMA = 2
KICK_BASE = 20261126


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M062 = _load("m062", SECTOR / "062_neighbour_ensemble" / "neighbour_ensemble.py")
M057, M061 = M062.M057, M062.M061
AngleModel = M062.AngleModel


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
        )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def start_state(N, seed):
    """Exactly 062's starting state for (N, seed)."""
    rng = np.random.default_rng(M062.BASE_SEED + 1000 * N + seed)
    L0 = N ** (1 / 3)
    pts = rng.uniform(0, L0, size=(N, 3))
    T, O = M057.periodic_delaunay(pts, L0)
    I, J, OF, _ = M057.edges_and_faces(T, O)
    m = np.linalg.norm(pts[J] + L0 * OF - pts[I], axis=1).mean()
    return pts / m, L0 / m


def forced_continuation(x, L, T, O):
    model = AngleModel(L, T, O)
    x2, _, _, s2 = model.newton(x.copy(), 1e-2, True)
    if s2 != "converged":
        return x2, s2
    x3, _, _, s3 = model.newton(x2, M062.MU, True)
    return x3, s3


def ensemble_row(N, seed):
    with M062.CSV_PATH.open() as fh:
        for r in csv.DictReader(fh):
            if int(r["N"]) == N and int(r["seed"]) == seed:
                return r
    raise KeyError((N, seed))


def shared_fraction(TA, OA, TB, OB):
    ka, kb = M061.tet_keys(TA, OA), M061.tet_keys(TB, OB)
    return len(ka & kb) / max(len(ka), len(kb))


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_path(failures):
    header("E1: path sensitivity -- standard relaxation vs forced barrier continuation")
    N, seed = PATH_SAMPLE
    x0, L = start_state(N, seed)
    ref = float(ensemble_row(N, seed)["A_Ew_vol"])
    xs, Ts, Os, outs, rs, _ = M062.delaunay_rule(x0.copy(), L, M062.angle_relax, True, failures,
                                                 "standard")
    xc, Tc, Oc, outc, rc, _ = M062.delaunay_rule(x0.copy(), L, forced_continuation, True, failures,
                                                 "forced continuation")
    ms, mc = M062.angle_metrics(xs, L, Ts, Os), M062.angle_metrics(xc, L, Tc, Oc)
    shared = shared_fraction(Ts, Os, Tc, Oc)
    ov = M062.overlap(ms["fab"], mc["fab"])
    print(f"    standard:   E_w/vol {ms['Ew_vol']:.4f} ({outs}, {rs} rounds); aniso {ms['aniso']:.4f}; "
          f"n=5 fraction {ms['frac5']:.3f}   (062 recorded {ref:.4f})")
    print(f"    continued:  E_w/vol {mc['Ew_vol']:.4f} ({outc}, {rc} rounds); aniso {mc['aniso']:.4f}; "
          f"n=5 fraction {mc['frac5']:.3f}")
    print(f"    shared tetrahedra {100 * shared:.1f}%; fabric overlap {ov:+.3f}")
    require("standard replay reproduces 062's recorded endpoint (to 1e-6)",
            abs(ms["Ew_vol"] - ref) < 1e-6, failures)
    require("both procedures reach a Delaunay fixed point",
            outs == "fixed point" and outc == "fixed point", failures)
    return {"std": ms, "cont": mc, "out_s": (outs, rs), "out_c": (outc, rc), "shared": shared,
            "ov": ov, "ref": ref}


def experiment_2_kicks(failures):
    header(f"E2: perturb and relax at N = {KICK_N} -- sigma = {SIGMAS}, {KICKS_PER_SIGMA} kicks each")
    rows = []
    for seed in KICK_SEEDS:
        x0, L = start_state(KICK_N, seed)
        ref = float(ensemble_row(KICK_N, seed)["A_Ew_vol"])
        t0 = time.time()
        xA, TA, OA, outA, rA, _ = M062.delaunay_rule(x0.copy(), L, M062.angle_relax, True, failures,
                                                     f"N={KICK_N} seed={seed} endpoint")
        base = M062.angle_metrics(xA, L, TA, OA)
        require(f"seed {seed}: regenerated endpoint matches 062 ({base['Ew_vol']:.4f} vs {ref:.4f})",
                abs(base["Ew_vol"] - ref) < 1e-6 and outA == "fixed point", failures)
        print(f"  seed {seed}: endpoint E_w/vol {base['Ew_vol']:.4f} ({time.time() - t0:.0f}s)", flush=True)
        for sigma in SIGMAS:
            for k in range(KICKS_PER_SIGMA):
                rng = np.random.default_rng(KICK_BASE + 100 * seed + 10 * int(100 * sigma) + k)
                xk = xA + sigma * rng.normal(size=xA.shape) / math.sqrt(3)
                Tk0, Ok0 = M061.delaunay_unwrapped(xk, L)
                changed = 1 - shared_fraction(TA, OA, Tk0, Ok0)
                t1 = time.time()
                xr, Tr, Or, outr, rr, _ = M062.delaunay_rule(xk, L, M062.angle_relax, True, failures,
                                                             f"seed {seed} sigma {sigma} kick {k}")
                m = M062.angle_metrics(xr, L, Tr, Or)
                back = shared_fraction(TA, OA, Tr, Or)
                row = {"seed": seed, "sigma": sigma, "kick": k, "base_Ew_vol": base["Ew_vol"],
                       "Ew_vol": m["Ew_vol"], "delta": m["Ew_vol"] - base["Ew_vol"],
                       "frac5": m["frac5"], "base_frac5": base["frac5"], "aniso": m["aniso"],
                       "base_aniso": base["aniso"], "kick_changed": changed,
                       "shared_with_base": back, "outcome": outr, "rounds": rr,
                       "ov_base": M062.overlap(m["fab"], base["fab"])}
                rows.append(row)
                print(f"    sigma {sigma:.2f} kick {k}: kick changes {100 * changed:.0f}% of tetrahedra; "
                      f"relaxed E_w/vol {m['Ew_vol']:.4f} ({row['delta']:+.4f}; {outr}, {rr} rounds, "
                      f"{time.time() - t1:.0f}s); shares {100 * back:.0f}% with the original; "
                      f"aniso {m['aniso']:.4f}", flush=True)
                require(f"seed {seed} sigma {sigma} kick {k}: relaxes to a Delaunay fixed point",
                        outr == "fixed point", failures)
    return rows


def write_csv(rows):
    with CSV_PATH.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.8f}" if isinstance(v, float) else v) for k, v in r.items()})
    print(f"[INFO] data written: {CSV_PATH}")


def record(ns):
    ns.record_derivation(
        derivation_id="perturb_and_relax_063",
        inputs=[sp.Symbol("ensemble_062"), sp.Symbol("barrier_continuation"),
                sp.Symbol("gaussian_kicks")],
        output=sp.Symbol("preparation_dependence_of_energy_density"),
        method=(
            "062 code imported; path replay of N = 160 seed 1 with forced continuation; four "
            f"N = {KICK_N} Delaunay endpoints regenerated and kicked (sigma = {SIGMAS}, "
            f"{KICKS_PER_SIGMA} kicks each) then relaxed under the Delaunay rule to fixed points"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_experiment",
        scope="trial angle energy, K = 1; small numbers of kicks; local endpoints; no EM coupling",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_preparation_dependence_063", script_id=SCRIPT_ID,
        title="Is the relaxed energy density characteristic or preparation-dependent? (first pass)",
        status=ObligationStatus.SATISFIED, satisfied_by=["perturb_and_relax_063"],
        description=("Path replay with forced continuation and perturb-and-relax from four N = 320 "
                     "endpoints; energies, neighbour turnover, anisotropy recorded."),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="perturb_and_relax_claim_063", script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=("The report records whether forced barrier continuation changes a relaxed "
                   "endpoint, and whether kicked N = 320 packings relax back to the 062 energy band "
                   "or shed more strain. Small sample; trial energy."),
        derivation_ids=["perturb_and_relax_063"],
        obligation_ids=["p10_preparation_dependence_063"],
    ))


def write_report(path, rows):
    sigma_stats = {}
    for s in SIGMAS:
        d = np.array([r["delta"] for r in rows if r["sigma"] == s])
        e = np.array([r["Ew_vol"] for r in rows if r["sigma"] == s])
        sh = np.array([r["shared_with_base"] for r in rows if r["sigma"] == s])
        ch = np.array([r["kick_changed"] for r in rows if r["sigma"] == s])
        an = np.array([r["aniso"] for r in rows if r["sigma"] == s])
        sigma_stats[s] = (d, e, sh, ch, an)
    base = sorted({(r["seed"], r["base_Ew_vol"]) for r in rows})
    base_vals = np.array([b[1] for b in base])
    all_e = np.array([r["Ew_vol"] for r in rows])
    lower = sum(r["delta"] < -0.05 * r["base_Ew_vol"] for r in rows)
    tab = "\n".join(
        f"    seed {r['seed']}  sigma {r['sigma']:.2f}  kick {r['kick']}:  {r['base_Ew_vol']:.4f} -> "
        f"{r['Ew_vol']:.4f} ({r['delta']:+.4f})   kick changed {100 * r['kick_changed']:3.0f}%   "
        f"shared after {100 * r['shared_with_base']:3.0f}%   n=5 {r['frac5']:.3f}   aniso {r['aniso']:.4f}"
        for r in rows)
    st = "\n".join(
        f"    sigma {s:.2f}: change {sigma_stats[s][0].mean():+.4f} +- {sigma_stats[s][0].std(ddof=1):.4f}; "
        f"kick changes {100 * sigma_stats[s][3].mean():.0f}% of tetrahedra; relaxed packings share "
        f"{100 * sigma_stats[s][2].mean():.0f}% with the original; anisotropy {sigma_stats[s][4].mean():.4f}"
        for s in SIGMAS)
    p = path
    md = f"""# VacuumForge: Perturb and Relax -- Is the Energy Density Characteristic?

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
E1. PATH SENSITIVITY (N = {PATH_SAMPLE[0]}, seed {PATH_SAMPLE[1]}; no fallback was needed in 062):
    standard relaxation:     E_w/vol {p['std']['Ew_vol']:.4f} ({p['out_s'][0]}, {p['out_s'][1]} rounds), anisotropy {p['std']['aniso']:.4f}
                             (062 recorded {p['ref']:.4f})
    forced continuation:     E_w/vol {p['cont']['Ew_vol']:.4f} ({p['out_c'][0]}, {p['out_c'][1]} rounds), anisotropy {p['cont']['aniso']:.4f}
    shared tetrahedra {100 * p['shared']:.1f}%; fabric overlap {p['ov']:+.3f}

E2. PERTURB AND RELAX (N = {KICK_N}; endpoints regenerated and matched
    to 062; Gaussian kicks of rms sigma x mean edge; Delaunay rule):
{tab}

    by amplitude:
{st}
    original endpoints {base_vals.min():.4f} .. {base_vals.max():.4f}; all relaxed kicks
    {all_e.min():.4f} .. {all_e.max():.4f}; kicks ending >5% below their origin: {lower} of {len(rows)}
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
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 063: Perturb and Relax")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    failures: list = []
    path = experiment_1_path(failures)
    rows = experiment_2_kicks(failures)
    write_csv(rows)
    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 063: verification failure")
    print("  Path replay and perturb-and-relax recorded.")
    record(ns)
    write_report(path, rows)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
