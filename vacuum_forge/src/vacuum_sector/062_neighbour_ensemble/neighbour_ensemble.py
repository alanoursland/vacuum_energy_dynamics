#!/usr/bin/env python3
"""
neighbour_ensemble.py

Derivation 062: the neighbour-change ensemble
(09_maxwell_probe, stage 3; p10_neighbour_ensemble_061, with the
matching spring control, spring_control_ensemble_057).

The questions, across seeds and sizes:
  1. Is the energy per volume left after neighbour changes reproducible?
  2. How much survives above the floor: how much is unavoidable
     coordination cost, how much is uneven sharing?
  3. Does the directional anisotropy of the stored energy wash out with
     size, and does the angle-gap model store energy more anisotropically
     than the spring control on the same quanta?

Per sample (seeded Poisson points, periodic Delaunay, unit mean edge,
FIXED cubic box), four runs, all with the definitions of 057/060/061
(imported, not re-implemented):

  F   fixed neighbours: the weighted angle energy relaxed on the starting
      Delaunay mesh (060's setting);
  A   VED's Delaunay rule: relax, re-triangulate, repeat to a fixed point,
      a cycle, or MAX_ROUNDS (061 rule A);
  B   energy-selected 2-3 / 3-2 flips alternated with relaxation, one flip
      order (061 rule B);
  S   spring control: the 051/057 spring proxy under the same Delaunay
      rule from the same quanta.

Exact mesh checks after every round (E = V + T, sum n = 6T,
sum (6 - n) = 6V, positive volumes summing to L^3, hinge closure for
the angle runs). Anisotropy is the rotation-invariant |dev F| / tr F of
each packing's energy fabric, measured per packing BEFORE any averaging
(a preferred axis may rotate from sample to sample); the random
starting mesh's angle-energy fabric is the baseline.

Fences: TRIAL angle energy, K = 1; spring proxy for the control; small
sizes (N <= 320) on a CPU; endpoints are local results of the stated
procedures; no EM coupling.
"""

import csv
from collections import Counter
import importlib.util
import itertools as it
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
PROBE_DIR = REPO_ROOT / "theory_v3" / "development" / "vacuum_sector" / "09_maxwell_probe"
REPORT_PATH = PROBE_DIR / "neighbour_ensemble_vacuumforge.md"
PLOT_PATH = PROBE_DIR / "neighbour_ensemble_062.png"
CSV_PATH = SCRIPT_PATH.parent / "ensemble_062.csv"
SECTOR = SCRIPT_PATH.parents[1]

DEPENDENCIES = [
    ("neighbour_dep_062", "061_neighbour_changes__neighbour_changes", "neighbour_changes_061"),
    ("spring_dep_062", "057_periodic_spring_control__periodic_spring_control",
     "periodic_spring_control_057"),
]

SIZES = (80, 160, 320)
SEEDS = (1, 2, 3, 4)
BASE_SEED = 20261125
MU = 1e-3
MAX_ROUNDS = 30
FLIP_ORDER = 1
TH0 = math.acos(1 / 3)
N5_FLOOR = (2 * math.pi - 5 * TH0) ** 2 / 10   # per unit hinge length at n = 5


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M057 = _load("m057", SECTOR / "057_periodic_spring_control" / "periodic_spring_control.py")
M060 = _load("m060", SECTOR / "060_angle_energy_fixed_neighbors" / "angle_energy_fixed_neighbors.py")
M061 = _load("m061", SECTOR / "061_neighbour_changes" / "neighbour_changes.py")
AngleModel, fabric, overlap = M060.AngleModel, M060.fabric, M060.overlap


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


# =============================================================================
# Measurements
# =============================================================================


def mesh_ok(x, L, T, O, angle=True):
    model = AngleModel(L, T, O)
    n = model.coord
    V = model.volumes(x)
    ok = (model.nH == model.n + model.nT and int(n.sum()) == 6 * model.nT
          and int((6 - n).sum()) == 6 * model.n and np.all(V > 0)
          and abs(float(V.sum()) - L ** 3) < 1e-8 * L ** 3)
    if angle:
        ok = ok and float(np.abs(model.hinges(x)["sum_th"] - 2 * math.pi).max()) < 1e-8
    return bool(ok)


def angle_metrics(x, L, T, O):
    model = AngleModel(L, T, O)
    hz = model.hinges(x)
    th, le, _, _ = model.dihedrals(model.P(x))
    ew_h = np.bincount(model.hinge.ravel(), weights=(0.5 * le * (th - TH0) ** 2).ravel(),
                       minlength=model.nH)
    vol = L ** 3
    fab = fabric(ew_h, hz["dir"])
    return {
        "Ew_vol": float(ew_h.sum()) / vol,
        "unavoid_w_vol": float((hz["len"] * hz["unavoid"]).sum()) / vol,
        "extra_w_vol": float((hz["len"] * hz["extra"]).sum()) / vol,
        "floor_vol": N5_FLOOR * float(hz["len"].sum()) / vol,
        "frac5": float(np.mean(hz["n"] == 5)), "mean_n": float(np.mean(hz["n"])),
        "aniso": fab["aniso"], "fab": fab, "T": model.nT,
    }


def spring_metrics(x, L, T, O):
    I, J, OF, _ = M057.edges_and_faces(T, O)
    b = x[J] + L * OF - x[I]
    l = np.linalg.norm(b, axis=1)
    fab = fabric((l - 1) ** 2, b / l[:, None])
    return {"Es_vol": float(((l - 1) ** 2).sum()) / L ** 3, "aniso": fab["aniso"], "fab": fab}


def spring_relax(x, L, T, O):
    """057's exact-Hessian Newton; if it stalls at the floating-point floor
    (Armijo decrease below the energy's resolution), polish with full Newton
    steps that are energy-neutral to roundoff and shrink the gradient (the
    same rule 060 uses for the angle energy)."""
    I, J, OF, _ = M057.edges_and_faces(T, O)
    pk = M057.Packing(L, T, O, I, J, OF)
    x, it_, gn, status = pk.newton(x.copy(), MU)
    if status == "converged":
        return x, status
    FALLBACKS["spring roundoff polish"] += 1
    E, g, *_ = pk.total(x, MU)
    for _ in range(50):
        gn = float(np.abs(g).max())
        if gn < M057.GTOL:
            return x, "converged"
        H = pk.hessian(x, MU)
        w, Q = np.linalg.eigh(H)
        wm = np.maximum(np.abs(w), 1e-8 * max(1.0, float(np.abs(w).max())))
        d = -(Q @ ((Q.T @ g.ravel()) / wm)).reshape(x.shape)
        xn = x + d
        En, gnew, *_ = pk.total(xn, MU)
        if gnew is None or not (En <= E + 1e-4 * float(d.ravel() @ g.ravel())
                                or (abs(En - E) < 1e-12 * max(1.0, abs(E))
                                    and float(np.abs(gnew).max()) < 0.5 * gn)):
            return x, status
        x, E, g = xn, En, gnew
    return x, status


# =============================================================================
# One sample
# =============================================================================


def delaunay_rule(x, L, relax_fn, angle, failures, tag):
    T, O = M061.delaunay_unwrapped(x, L)
    seen = {M061.tet_keys(T, O): 0}
    outcome, rounds = f"max rounds ({MAX_ROUNDS})", 0
    first_relaxed = None
    for r in range(1, MAX_ROUNDS + 1):
        x, status = relax_fn(x, L, T, O)
        if first_relaxed is None:
            first_relaxed = (x.copy(), T, O)
        ok = status == "converged" and mesh_ok(x, L, T, O, angle)
        Tn, On = M061.delaunay_unwrapped(x, L)
        ok = ok and mesh_ok(x, L, Tn, On, angle)
        if not ok:
            require(f"{tag} round {r}: converged relaxation and exact mesh checks", False, failures)
        kn = M061.tet_keys(Tn, On)
        rounds = r
        if kn == M061.tet_keys(T, O):
            outcome = "fixed point"
            break
        if kn in seen:
            outcome = "cycle"
            T, O = Tn, On
            x, status = relax_fn(x, L, T, O)
            break
        seen[kn] = r
        T, O = Tn, On
    else:
        x, status = relax_fn(x, L, T, O)
    return x, T, O, outcome, rounds, first_relaxed


FALLBACKS = Counter()


def angle_relax(x, L, T, O):
    """061's relaxation (060's Newton at mu = MU). If it fails -- a sliver
    driven toward zero volume can trap the feasibility-limited steps --
    fall back to barrier continuation from the same input: mu = 1e-2, then
    warm-start at MU. Fallbacks are counted and reported."""
    x1, it_, gn, status = M061.relax(x, L, T, O)
    if status == "converged":
        return x1, status
    FALLBACKS["angle continuation"] += 1
    model = AngleModel(L, T, O)
    x2, _, _, s2 = model.newton(x.copy(), 1e-2, True)
    if s2 != "converged":
        return x1, status
    x3, _, _, s3 = model.newton(x2, MU, True)
    return x3, s3


def rule_b(x, L, T, O, failures, tag):
    rng = np.random.default_rng(FLIP_ORDER)
    flips = 0
    for r in range(1, MAX_ROUNDS + 1):
        mesh = M061.Mesh(x, L, T, O)
        n23, n32 = M061.flip_sweeps(mesh, rng)
        T, O = mesh.arrays()
        flips += n23 + n32
        if n23 + n32 == 0:
            break
        x, status = angle_relax(x, L, T, O)
        if not (status == "converged" and mesh_ok(x, L, T, O)):
            require(f"{tag} rule B round {r}: converged relaxation and exact mesh checks", False,
                    failures)
    return x, T, O, flips


def run_sample(N, seed, failures):
    rng = np.random.default_rng(BASE_SEED + 1000 * N + seed)
    L0 = N ** (1 / 3)
    pts = rng.uniform(0, L0, size=(N, 3))
    T, O = M057.periodic_delaunay(pts, L0)
    I, J, OF, _ = M057.edges_and_faces(T, O)
    m = np.linalg.norm(pts[J] + L0 * OF - pts[I], axis=1).mean()
    x0, L = pts / m, L0 / m
    T0, O0 = M061.delaunay_unwrapped(x0, L)
    tag = f"N={N} seed={seed}"
    require(f"{tag}: starting periodic Delaunay mesh passes the exact checks",
            mesh_ok(x0, L, T0, O0), failures)
    start = angle_metrics(x0, L, T0, O0)
    t0 = time.time()
    xA, TA, OA, outA, rA, first = delaunay_rule(x0.copy(), L, angle_relax, True, failures,
                                                f"{tag} rule A")
    F = angle_metrics(*first[:1], L, first[1], first[2])
    A = angle_metrics(xA, L, TA, OA)
    tA = time.time() - t0
    xB, TB, OB, flips = rule_b(first[0], L, first[1], first[2], failures, tag)
    B = angle_metrics(xB, L, TB, OB)
    xS, TS, OS, outS, rS, _ = delaunay_rule(x0.copy(), L, spring_relax, False, failures,
                                            f"{tag} spring")
    S = spring_metrics(xS, L, TS, OS)
    S_angle = angle_metrics(xS, L, TS, OS)  # angle energy carried by the spring endpoint
    ov_AS = overlap(A["fab"], S["fab"])
    ov_A_start = overlap(A["fab"], start["fab"])
    print(f"    {tag}: F {F['Ew_vol']:.3f} | A {A['Ew_vol']:.3f} ({outA}, {rA} rounds, {tA:.0f}s) | "
          f"B {B['Ew_vol']:.3f} ({flips} flips) | spring {S['Es_vol']:.4f} ({outS}, {rS} rounds); "
          f"aniso start {start['aniso']:.4f}, A {A['aniso']:.4f}, spring {S['aniso']:.4f}; "
          f"overlap A-spring {ov_AS:+.2f}, A-start {ov_A_start:+.2f}", flush=True)
    return {"N": N, "seed": seed, "L": L,
            "F_Ew_vol": F["Ew_vol"], "A_Ew_vol": A["Ew_vol"], "B_Ew_vol": B["Ew_vol"],
            "A_unavoid_vol": A["unavoid_w_vol"], "A_extra_vol": A["extra_w_vol"],
            "A_floor_vol": A["floor_vol"], "A_frac5": A["frac5"], "A_mean_n": A["mean_n"],
            "start_frac5": start["frac5"], "A_outcome": outA, "A_rounds": rA,
            "B_flips": flips, "S_Es_vol": S["Es_vol"], "S_outcome": outS, "S_rounds": rS,
            "S_angle_Ew_vol": S_angle["Ew_vol"],
            "aniso_start": start["aniso"], "aniso_F": F["aniso"], "aniso_A": A["aniso"],
            "aniso_B": B["aniso"], "aniso_S": S["aniso"],
            "ov_A_S": ov_AS, "ov_A_start": ov_A_start, "ov_S_start": overlap(S["fab"], start["fab"])}


# =============================================================================
# Experiments
# =============================================================================


def experiment_1_ensemble(failures):
    header(f"E1: the ensemble -- {len(SEEDS)} seeds x N = {SIZES}")
    rows = []
    for N in SIZES:
        for s in SEEDS:
            rows.append(run_sample(N, s, failures))
    return rows


def stats(rows, key, N):
    v = np.array([r[key] for r in rows if r["N"] == N])
    return float(v.mean()), float(v.std(ddof=1)) if len(v) > 1 else 0.0


def experiment_2_summary(rows, failures):
    header("E2: reproducibility, floor, and anisotropy by size")
    keys = ["F_Ew_vol", "A_Ew_vol", "B_Ew_vol", "A_unavoid_vol", "A_extra_vol", "A_floor_vol",
            "A_frac5", "S_Es_vol", "aniso_start", "aniso_A", "aniso_S", "ov_A_S", "ov_A_start"]
    summary = {}
    for N in SIZES:
        summary[N] = {k: stats(rows, k, N) for k in keys}
        s = summary[N]
        print(f"  N = {N}: E_w/vol fixed {s['F_Ew_vol'][0]:.3f}+-{s['F_Ew_vol'][1]:.3f}; "
              f"Delaunay rule {s['A_Ew_vol'][0]:.3f}+-{s['A_Ew_vol'][1]:.3f}; "
              f"flips {s['B_Ew_vol'][0]:.3f}+-{s['B_Ew_vol'][1]:.3f}")
        print(f"          A: unavoidable {s['A_unavoid_vol'][0]:.3f}, extra {s['A_extra_vol'][0]:.3f}, "
              f"n = 5 floor {s['A_floor_vol'][0]:.4f}; n = 5 fraction {s['A_frac5'][0]:.3f}")
        print(f"          anisotropy start {s['aniso_start'][0]:.4f}+-{s['aniso_start'][1]:.4f}, "
              f"angle A {s['aniso_A'][0]:.4f}+-{s['aniso_A'][1]:.4f}, "
              f"spring {s['aniso_S'][0]:.4f}+-{s['aniso_S'][1]:.4f}; overlap A-spring "
              f"{s['ov_A_S'][0]:+.2f}, A-start {s['ov_A_start'][0]:+.2f}")
    cv = {N: summary[N]["A_Ew_vol"][1] / summary[N]["A_Ew_vol"][0] for N in SIZES}
    print(f"    seed-to-seed coefficient of variation of the Delaunay-rule E_w/vol: "
          + ", ".join(f"N={N}: {100 * c:.1f}%" for N, c in cv.items()))
    require("every sample: the Delaunay rule releases energy relative to fixed neighbours",
            all(r["A_Ew_vol"] < r["F_Ew_vol"] for r in rows), failures)
    require("every sample: the Delaunay endpoint stays above the n = 5 floor",
            all(r["A_Ew_vol"] > r["A_floor_vol"] for r in rows), failures)
    return summary, cv


def write_csv(rows):
    with CSV_PATH.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.8f}" if isinstance(v, float) else v) for k, v in r.items()})
    print(f"[INFO] data written: {CSV_PATH}")


def write_plot(rows):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    surface, ink, ink2, grid = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3de"
    c1, c2, c3 = "#2a78d6", "#eb6834", "#1baf7a"  # validated categorical slots 1-3
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": ink2, "axes.labelcolor": ink2,
                         "xtick.color": ink2, "ytick.color": ink2, "text.color": ink})
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
    fig.patch.set_facecolor(surface)
    Ns = np.array(SIZES, float)

    def series(ax, key, color, label, jitter):
        for N in SIZES:
            v = [r[key] for r in rows if r["N"] == N]
            ax.scatter([N * jitter] * len(v), v, s=22, color=color, alpha=0.45, linewidths=0,
                       zorder=2)
        means = [np.mean([r[key] for r in rows if r["N"] == N]) for N in SIZES]
        ax.plot(Ns * jitter, means, color=color, lw=2, marker="o", ms=6, label=label, zorder=3)

    ax = axs[0]
    series(ax, "F_Ew_vol", c1, "neighbours fixed", 0.97)
    series(ax, "A_Ew_vol", c2, "Delaunay rule (VED)", 1.0)
    series(ax, "B_Ew_vol", c3, "energy-selected flips", 1.03)
    ax.set_ylabel("stored angle energy per volume  (K = 1)")
    ax.set_title("Energy left after relaxation", color=ink, fontsize=11)
    ax = axs[1]
    series(ax, "aniso_start", c1, "random starting mesh", 0.97)
    series(ax, "aniso_A", c2, "angle energy, Delaunay rule", 1.0)
    series(ax, "aniso_S", c3, "spring control, Delaunay rule", 1.03)
    ax.set_ylabel("anisotropy  |dev F| / tr F  (per packing)")
    ax.set_title("Directional anisotropy of stored energy", color=ink, fontsize=11)
    for ax in axs:
        ax.set_facecolor(surface)
        ax.set_xscale("log")
        ax.set_xticks(list(SIZES))
        ax.set_xticklabels([str(N) for N in SIZES])
        ax.set_xlabel("N (quanta per periodic box)")
        ax.set_ylim(bottom=0)
        ax.grid(True, color=grid, lw=0.8)
        ax.set_axisbelow(True)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.legend(frameon=False, loc="upper right", fontsize=9)
    fig.suptitle(f"Neighbour-change ensemble: {len(SEEDS)} seeds per size (dots), means (lines)",
                 color=ink, fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=150, bbox_inches="tight", facecolor=surface,
                metadata={"Software": None, "CreationDate": None})
    plt.close(fig)
    print(f"[INFO] plot written: {PLOT_PATH}")


def record(ns):
    ns.record_derivation(
        derivation_id="neighbour_ensemble_062",
        inputs=[sp.Symbol("seeded_periodic_delaunay"), sp.Symbol("weighted_trial_angle_energy"),
                sp.Symbol("spring_proxy"), sp.Symbol("delaunay_rule"), sp.Symbol("bistellar_flips")],
        output=sp.Symbol("ensemble_energy_per_volume_and_anisotropy"),
        method=(
            f"{len(SEEDS)} seeds x N = {SIZES}; per sample: fixed-neighbour relaxation, "
            "Delaunay-rule iteration, energy-selected flips (one order), and the spring proxy "
            "under the Delaunay rule from the same quanta; 057/060/061 code imported; exact "
            "mesh checks every round; per-packing rotation-invariant anisotropy"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_experiment",
        scope=(
            "trial angle energy, K = 1; spring proxy; N <= 320 on CPU; local endpoints of the "
            "stated procedures; no EM coupling"
        ),
    )
    for oid, title in (("p10_neighbour_ensemble_061", "Neighbour-change ensemble (first pass)"),
                       ("spring_control_ensemble_057", "Spring-control ensemble (first pass)")):
        ns.record_obligation(ProofObligationRecord(
            obligation_id=oid, script_id=SCRIPT_ID, title=title,
            status=ObligationStatus.SATISFIED, satisfied_by=["neighbour_ensemble_062"],
            description=(f"First pass at N = {SIZES} with {len(SEEDS)} seeds each; larger N and "
                         "cell shapes remain in p10_large_ensemble_062."),
        ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="p10_large_ensemble_062", script_id=SCRIPT_ID,
        title="Larger N, more seeds, other cell shapes (GPU scale)",
        status=ObligationStatus.OPEN, required_by=["neighbour_ensemble_062"],
        description=("Extend 062 to N >= 1000, more seeds, and non-cubic cells; test whether the "
                     "energy per volume converges and the anisotropy falls like a random "
                     "fluctuation; stronger searches (annealing, 4-4 flips) for rule B."),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="neighbour_ensemble_claim_062", script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=("Across seeds and N <= 320, the report records the energy per volume left after "
                   "neighbour changes, its unavoidable/extra split relative to the n = 5 floor, "
                   "and the per-packing anisotropy of the angle-gap and spring models against the "
                   "random starting mesh. Small sizes; trial energy."),
        derivation_ids=["neighbour_ensemble_062"],
        obligation_ids=["p10_neighbour_ensemble_061", "spring_control_ensemble_057"],
    ))


def write_report(rows, summary, cv):
    def ms(N, k, f=".3f"):
        m, s = summary[N][k]
        return f"{m:{f}} +- {s:{f}}"

    tab_E = "\n".join(f"    {N:4d}   {ms(N, 'F_Ew_vol')}   {ms(N, 'A_Ew_vol')}   {ms(N, 'B_Ew_vol')}   "
                      f"{100 * cv[N]:4.1f}%" for N in SIZES)
    tab_F = "\n".join(f"    {N:4d}   {ms(N, 'A_unavoid_vol')}   {ms(N, 'A_extra_vol')}   "
                      f"{ms(N, 'A_floor_vol', '.4f')}   {ms(N, 'A_frac5')}" for N in SIZES)
    tab_A = "\n".join(f"    {N:4d}   {ms(N, 'aniso_start', '.4f')}   {ms(N, 'aniso_A', '.4f')}   "
                      f"{ms(N, 'aniso_S', '.4f')}   {ms(N, 'ov_A_S', '+.2f')}   "
                      f"{ms(N, 'ov_A_start', '+.2f')}" for N in SIZES)
    outs = "\n".join(f"    N={r['N']:<4d} seed {r['seed']}: A {r['A_outcome']} ({r['A_rounds']} rounds); "
                     f"spring {r['S_outcome']} ({r['S_rounds']} rounds); B {r['B_flips']} flips"
                     for r in rows)
    m80, m320 = summary[SIZES[0]], summary[SIZES[-1]]
    ratio_start = m80["aniso_start"][0] / m320["aniso_start"][0]
    ratio_A = m80["aniso_A"][0] / m320["aniso_A"][0]
    ratio_S = m80["aniso_S"][0] / m320["aniso_S"][0]
    md = f"""# VacuumForge: The Neighbour-Change Ensemble

## Status

```text
result type:   numerical ensemble (stage 3; 2026-11-24, derivation 062);
               TRIAL angle energy, K = 1; spring proxy as control
samples:       {len(SEEDS)} seeds x N = {SIZES} (fixed cubic periodic box)
satisfies:     p10_neighbour_ensemble_061, spring_control_ensemble_057
               (first pass)
opens:         p10_large_ensemble_062 (larger N, cell shapes; GPU)
data:          vacuum_forge/src/vacuum_sector/062_neighbour_ensemble/ensemble_062.csv
verification:  vacuum_forge/src/vacuum_sector/062_neighbour_ensemble/
```

![Ensemble](neighbour_ensemble_062.png)

Left: angle energy per volume left after relaxation with neighbours
fixed, under VED's Delaunay rule, and under energy-selected flips. Right:
per-packing anisotropy of the stored energy for the random starting
mesh, the angle energy under the Delaunay rule, and the spring control
under the same rule. Dots are seeds; lines are means.

## Measured Results

```text
E_w per volume (mean +- std over seeds):
    N      fixed neighbours   Delaunay rule      flips              seed CV (Delaunay)
{tab_E}

Delaunay-rule endpoint, per volume (length-weighted):
    N      unavoidable        extra              n = 5 floor          n = 5 fraction
{tab_F}

Per-packing anisotropy |dev F| / tr F and fabric overlaps:
    N      random start       angle, Delaunay    spring, Delaunay   overlap A-spring  overlap A-start
{tab_A}
    mean anisotropy ratio N = {SIZES[0]} : {SIZES[-1]}: start {ratio_start:.2f}, angle {ratio_A:.2f},
    spring {ratio_S:.2f} (a random fluctuation would give ~{math.sqrt(SIZES[-1] / SIZES[0]):.1f})

Outcomes:
{outs}

Solver fallbacks (counted over every relaxation in the ensemble):
    {dict(FALLBACKS) if FALLBACKS else 'none'}
    angle continuation: 061's direct relaxation failed (a sliver driven
    toward zero volume trapped the feasibility-limited Newton steps);
    re-run from the same input at mu = 1e-2, then warm-started at
    mu = {MU:g}. spring roundoff polish: 057's Newton stalled at the
    floating-point floor; finished with the roundoff-aware rule of 060.
```

## Fences

```text
- TRIAL angle energy, K = 1; the spring proxy is a control, not P10.
- small sizes (N <= 320) and one cell shape; scaling claims wait for
  p10_large_ensemble_062.
- endpoints are local results: the Delaunay iteration may stop at a
  fixed point, a cycle, or the round cap; rule B is greedy (061).
- no EM coupling.
```

## Compute Environment

```text
ran on:      CPU-only cloud container (NumPy/SciPy). No GPU was
             available; attaching the theory owner's local GPU (RTX
             3080 Ti) to the cloud session was not supported.
methods:     057/060/061 code imported unchanged (periodic Delaunay,
             exact spring Hessian, exact per-tetrahedron angle Hessian
             with eigenvalue-modified Newton, incremental flips).
validation:  another Claude Code session with GPU access should rerun
             this module (ensemble_062.csv to ~1e-6) and extend it to
             N >= 1000, more seeds and non-cubic cells
             (p10_large_ensemble_062), where dense Hessians must give way
             to sparse GPU solvers.
```

## Ledger

```text
derivation:  neighbour_ensemble_062
satisfies:   p10_neighbour_ensemble_061, spring_control_ensemble_057
opens:       p10_large_ensemble_062
depends on:  neighbour_changes_061, periodic_spring_control_057
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 062: The Neighbour-Change Ensemble")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    rows = experiment_1_ensemble(failures)
    summary, cv = experiment_2_summary(rows, failures)
    write_csv(rows)
    write_plot(rows)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 062: verification failure")
    print("  Ensemble delivered: energy per volume, its floor split, and per-packing")
    print("  anisotropy recorded across seeds and sizes, with exact mesh checks.")
    record(ns)
    write_report(rows, summary, cv)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
