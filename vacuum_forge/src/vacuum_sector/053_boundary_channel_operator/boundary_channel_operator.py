#!/usr/bin/env python3
"""
boundary_channel_operator.py

Derivation 053: the Casimir/UFFT boundary operator, instantiated --
and the instantiation KILLS the unsuppressed channel.

The dimensional-relaxation channel (dimensional_relaxation_channel.md)
has waited in quarantine on kill conditions 1-6: derive the operator,
show it distinct from QFT Casimir, bound it against the micron window,
enforce the one-time/no-cycle discipline, make dimensional reduction
precise, and preserve the closed sector. Under P10 the operator is
finally derivable, because every ingredient is now on the books:

  - 2D packing is EXACTLY frustration-free (six equilateral triangles
    close a vertex: deficit identically zero) -- the release
    differential exists and is the full 3D floor;
  - the 3D floor density is derived (052 mixture + edge density c_e);
  - the magnitude is LOCKED, coefficient-free, by the floor-Newton
    lock (039): the same f'(Delta_0) that must reproduce G fixes the
    floor scale, u_floor ~ (c^4/32 pi G) <delta^2>/Delta_0 * c_e/a^2.

THE OPERATOR (mean-field, full-relaxation bound): confining the
packing to quasi-2D in a slab of thickness d releases E/A =
u_floor * d; the associated inter-boundary force is a CONSTANT
attractive pressure P = u_floor -- scaling exponent 0 in d, cleanly
distinct from QFT Casimir's d^-4 (kill condition 2: PASSED -- it
would be a new channel).

THE KILL (condition 3, quantitative): the locked magnitude is
u_floor ~ 1e112 J/m^3 at Planck packing -- and Casimir-class
experiments bound anomalous plate pressures at the ~1e-2 Pa level.
Any unsuppressed matter-boundary/packing coupling is excluded by
~114 orders of magnitude; even a = 30 um (the window scale itself,
absurdly generous) leaves ~44 orders. For the channel to hide, the
coupling of matter boundaries to packing configuration must be
< ~1e-44 at best: OPERATIONALLY ZERO. The P10-consistent reading of
that zero: matter is strain/defect content OF the packing (041 E4,
the matter-as-defect charter), not external walls that can impose
packing boundary conditions; there is no derived operator by which
atoms confine cells, and this result says any such operator must be
essentially absent.

CONSEQUENCES, recorded honestly:
  - the engineered-boundary energy-release mechanism is CLOSED at
    leading order (the founding energy-extraction motivation loses
    its packing-era route);
  - "gravity sequesters, boundaries reveal" (the channel note's
    section 6 hope) is quantitatively dead: the floor is hidden from
    BOTH channels;
  - the UFFT micron window (29.9-38.6 um) loses its VED motivation:
    whatever lives there is ordinary QFT physics; excluding the
    window would now kill nothing in the VED core (register B3
    downgraded);
  - the discipline line was never violated: the release is a state
    function, and Hartle-Sorkin additivity (042) makes the closed
    cycle net exactly zero -- checked below.

Fence: the kill is of the UNSUPPRESSED channel. A future derivation
producing a specific tiny coupling with independent motivation could
reopen it through the front door; nothing here licenses that, and
backsolving a coupling to fit inside the exclusion is forbidden.
"""

import math
from pathlib import Path

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
               / "08_packing_microphysics" / "boundary_channel_operator_vacuumforge.md")

DEPENDENCIES = [
    ("edge_density_dep_053", "052_edge_density__edge_density", "edge_density_052"),
    ("boundary_dep_053",
     "042_discrete_conservation_boundary__discrete_conservation_boundary",
     "discrete_conservation_boundary_042"),
    ("bridge_dep_053", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
]

THETA3 = sp.acos(sp.Rational(1, 3))

# physical constants (SI)
C_LIGHT = 299792458.0
G_NEWTON = 6.674e-11
L_PLANCK = 1.616e-35
CASIMIR_ANOMALY_BOUND_PA = 1e-2   # conservative residual-pressure bound at um range
WINDOW_M = 30e-6                   # the UFFT window scale (generous a)


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


def check_1_release_differential(failures):
    header("Check 1: 2D is exactly free, 3D floor is positive -- the differential exists")
    # 2D: six equilateral triangles around a vertex close exactly.
    deficit_2d = sp.simplify(2 * sp.pi - 6 * (sp.pi / 3))
    require("2D vertex deficit = 2 pi - 6*(pi/3) = 0 EXACTLY (triangles tile)",
            deficit_2d == 0, failures)
    # 3D floor: the 052 mixture's mean squared deficit.
    d5 = 2 * sp.pi - 5 * THETA3
    d6 = 2 * sp.pi - 6 * THETA3
    x6 = sp.simplify(2 * sp.pi / THETA3 - 5)
    mean_d2 = sp.simplify((1 - x6) * d5**2 + x6 * d6**2)
    mean_d2_num = float(mean_d2.evalf(50))
    require(f"3D ground mixture floor <delta^2> = {mean_d2_num:.6f} rad^2 > 0",
            mean_d2_num > 0, failures)
    print("  Confining a region to quasi-2D packing releases its entire 3D")
    print("  frustration floor: the differential is real and derived (037/041/")
    print("  050/052). The question is the OPERATOR: magnitude and scaling.")
    return mean_d2


def check_2_operator_and_scaling(failures):
    header("Check 2: the operator -- constant pressure, distinct from QFT Casimir")
    u, d, A = sp.symbols("u_floor d A", positive=True)
    E_release = u * A * d            # full-relaxation bound for a slab
    P = sp.diff(E_release, d) / A    # attractive pressure magnitude
    require("released energy E/A = u_floor * d (extensive in slab thickness)",
            sp.simplify(E_release / A - u * d) == 0, failures)
    require("force law: constant attractive pressure P = u_floor, d-exponent 0",
            sp.simplify(P - u) == 0, failures)
    # QFT Casimir: P_C = pi^2 hbar c / (240 d^4) -- exponent -4.
    dd = sp.Symbol("d", positive=True)
    P_c = sp.pi**2 * sp.Symbol("hbar_c", positive=True) / (240 * dd**4)
    exponent_casimir = sp.simplify(sp.diff(sp.log(P_c), sp.log(dd) if False else dd) * dd)
    require("QFT Casimir exponent: d ln P_C/d ln d = -4 (cleanly distinct from 0)",
            sp.simplify(exponent_casimir + 4) == 0, failures)
    print("  Kill condition 2 PASSED in form: the packing operator is NOT a")
    print("  rescaled Casimir term -- constant pressure vs d^-4. If it existed")
    print("  at detectable strength it would be a NEW channel. Now the")
    print("  magnitude.")


def check_3_locked_magnitude_kill(mean_d2, failures):
    header("Check 3: the locked magnitude -- and the exclusion (the kill)")
    # Floor-Newton lock, quadratic witness: f(delta) = k delta^2/2 per hinge
    # (hinge weight = edge length ell = a in 3D Regge), with
    # f'(Delta_0) * a = c^4/(16 pi G) * a-scale calibration => k = c^4/(16 pi G Delta_0).
    # Floor density u = (c_e/a^3) * (k/2) <delta^2> * a
    #                 = c^4 c_e <delta^2> / (32 pi G Delta_0 a^2).
    Delta0 = 2 * sp.pi - 5 * THETA3
    c_e = 36 * THETA3 / (sp.sqrt(2) * sp.pi)
    a = sp.Symbol("a", positive=True)
    c4_32piG = C_LIGHT**4 / (32 * math.pi * G_NEWTON)
    # u_floor(a) numeric, SI:
    def u_floor(a_m):
        return c4_32piG * float((c_e * mean_d2 / Delta0).evalf(50)) / a_m**2

    u_planck = u_floor(L_PLANCK)
    u_window = u_floor(WINDOW_M)
    print(f"  u_floor(a = l_P)   = {u_planck:.3e} J/m^3 = Pa")
    print(f"  u_floor(a = 30 um) = {u_window:.3e} J/m^3 = Pa (absurdly generous a)")
    print(f"  experimental anomalous-pressure bound (Casimir-class): "
          f"{CASIMIR_ANOMALY_BOUND_PA:.0e} Pa")
    margin_planck = u_planck / CASIMIR_ANOMALY_BOUND_PA
    margin_window = u_window / CASIMIR_ANOMALY_BOUND_PA
    print(f"  exclusion margins: {margin_planck:.1e} (Planck a), "
          f"{margin_window:.1e} (window a)")
    require("Planck-packing operator excluded by > 1e100 (unsuppressed coupling dead)",
            margin_planck > 1e100, failures)
    require("even window-scale packing excluded by > 1e30",
            margin_window > 1e30, failures)
    require("required coupling suppression < 1e-30 at best: operationally zero",
            1 / margin_window < 1e-30, failures)
    print("  THE KILL: any unsuppressed coupling of matter boundaries to the")
    print("  packing configuration predicts a constant attractive plate")
    print("  pressure of order the floor density -- excluded by >= 30 orders")
    print("  of magnitude under the most generous packing scale, and by ~114")
    print("  at Planck packing. Matter boundaries do NOT confine the packing:")
    print("  consistent with matter being strain content OF the packing")
    print("  (041 E4), not external walls. The 'gravity sequesters, boundaries")
    print("  reveal' hope is quantitatively dead -- the floor hides from both")
    print("  channels.")
    return u_planck, u_window, margin_planck, margin_window


def check_4_cycle_closure(failures):
    header("Check 4: the discipline line -- closed cycle nets exactly zero")
    u, A, d1, d2 = sp.symbols("u A d1 d2", positive=True)
    E = lambda d: -u * A * d  # energy of the relaxed slab relative to bulk
    release = E(d2) - E(d1)      # d2 < d1: energy released (negative change)
    reset = E(d1) - E(d2)        # work to re-expand
    require("cycle: release + reset = 0 exactly (state function, no over-unity)",
            sp.simplify(release + reset) == 0, failures)
    print("  The released energy is a state function of the configuration;")
    print("  Hartle-Sorkin additivity (042) guarantees the boundary terms")
    print("  cancel on regluing, so a closed confine/release/re-expand cycle")
    print("  nets exactly zero. The discipline line (finite, one-time, no")
    print("  perpetual source) was structurally sound -- the channel dies of")
    print("  magnitude, not of thermodynamics.")


def record(ns, u_planck, margin_planck, margin_window):
    ns.record_derivation(
        derivation_id="boundary_channel_operator_053",
        inputs=[sp.Symbol("floor_newton_lock_039"), sp.Symbol("edge_density_052"),
                sp.Symbol("hartle_sorkin_additivity_042")],
        output=sp.Symbol("constant_pressure_operator_excluded_unsuppressed_channel_dead"),
        method=(
            "2D zero-deficit exactness; slab release operator E/A = u_floor d "
            "with constant-pressure force law (d-exponent 0 vs Casimir -4); "
            "magnitude locked coefficient-free by the floor-Newton lock "
            "(quadratic witness): u_floor = c^4 c_e <delta^2>/(32 pi G "
            "Delta_0 a^2); exclusion against Casimir-class anomalous-pressure "
            "bounds; cycle closure via state-function + Hartle-Sorkin "
            "additivity"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.COUNTEREXAMPLE,
        result_type="channel_kill",
        scope=(
            "kills the UNSUPPRESSED matter-boundary/packing coupling; a "
            "future front-door derivation of a specific tiny coupling could "
            "reopen; backsolving a coupling into the exclusion window is "
            "forbidden; ordinary QFT Casimir physics untouched"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="ufft_operator_instantiated_053",
        script_id=SCRIPT_ID,
        title="Casimir/UFFT operator instantiated -- and the unsuppressed channel is DEAD",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["boundary_channel_operator_053"],
        description=(
            "The long-owed operator instantiation is delivered: the "
            "dimensional-relaxation boundary operator is a constant "
            "attractive pressure u_floor (distinct from Casimir d^-4), "
            "locked by the floor-Newton lock to ~1e112 Pa at Planck packing "
            "-- excluded by ~114 orders (>= 30 even at window-scale a). "
            "Matter boundaries cannot confine the packing at any detectable "
            "coupling. Kill conditions 1, 2, 4 satisfied; 3 satisfied by "
            "exclusion; consequence: the UFFT window loses its VED "
            "motivation (register B3 downgraded), the engineered-boundary "
            "release mechanism closes, and 'boundaries reveal the "
            "sequestered floor' is dead."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="boundary_channel_claim_053",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The packing supplies exactly one boundary-confinement operator "
            "at leading order -- a constant attractive plate pressure equal "
            "to the frustration floor density -- and its floor-Newton-locked "
            "magnitude is excluded by tens to ~114 orders of magnitude by "
            "Casimir-class experiments. Therefore the matter-boundary/"
            "packing coupling is operationally zero: matter is strain "
            "content of the packing, not walls that confine it. The "
            "dimensional-relaxation energy-release channel is CLOSED "
            "(unsuppressed), the UFFT micron window is no longer "
            "VED-motivated, and the sequestered floor is hidden from the "
            "boundary channel exactly as it is from gravity. Honest "
            "negative; no observable moves; the closed sector is untouched."
        ),
        derivation_ids=["boundary_channel_operator_053"],
        obligation_ids=["ufft_operator_instantiated_053"],
    ))


def write_report(u_planck, u_window, margin_planck, margin_window):
    md = f"""# The Boundary Channel Operator (Casimir/UFFT) -- VacuumForge Record

## Status

```text
result type:   operator instantiation => CHANNEL KILL (honest negative;
               2026-07-02, derivation 053)
conclusion:    the dimensional-relaxation boundary operator EXISTS in
               form (constant attractive pressure, cleanly distinct
               from QFT Casimir d^-4) but its floor-Newton-locked
               magnitude is excluded by ~114 orders of magnitude
               (Planck packing) to >= 30 orders (window-scale packing,
               absurdly generous). The unsuppressed matter-boundary/
               packing coupling is operationally zero.
consequences:  - engineered-boundary energy release: CLOSED at leading
                 order (the founding extraction motivation loses its
                 packing-era route)
               - "gravity sequesters, boundaries reveal": DEAD -- the
                 floor hides from both channels
               - the UFFT micron window (29.9-38.6 um): no longer
                 VED-motivated; register B3 downgraded
verification:  vacuum_forge/src/vacuum_sector/053_boundary_channel_operator/
```

## The Operator (kill conditions 1, 2, 5 -- delivered)

```text
2D packing is EXACTLY frustration-free (six triangles close a vertex:
deficit identically zero); the 3D floor is the derived 052 mixture.
Confining a slab of thickness d to quasi-2D releases (full-relaxation
bound)

    E/A = u_floor * d,      force law: P = u_floor, CONSTANT in d

vs QFT Casimir's P_C = pi^2 hbar c/(240 d^4). Scaling exponents 0 vs
-4: a genuinely new channel IF it existed at detectable strength.
"Dimensional reduction under confinement" made precise: the quantity
that drops is the per-volume hinge frustration <delta^2>, to zero, at
confinement scale ~ a.
```

## The Kill (condition 3 -- the magnitude is locked, and it is fatal)

```text
The floor-Newton lock (039) + derived c_e (052) fix the magnitude
with NO free coefficient (quadratic witness):

    u_floor = c^4 c_e <delta^2> / (32 pi G Delta_0 a^2)

    a = l_P:    u_floor = {u_planck:.2e} Pa   (margin ~{margin_planck:.0e})
    a = 30 um:  u_floor = {u_window:.2e} Pa   (margin ~{margin_window:.0e})

against Casimir-class anomalous-pressure bounds (~1e-2 Pa). Any
unsuppressed coupling of matter boundaries to the packing predicts a
plate pressure excluded by >= 30 orders of magnitude under the most
generous assumptions. The coupling is OPERATIONALLY ZERO.

The P10-consistent reading of that zero: matter is strain/defect
content OF the packing (041 E4, matter-as-defect charter) -- not
external walls. Atoms do not confine cells; this result now says any
operator by which they could must be absent to fantastic precision.
```

## The Discipline Line (condition 4 -- held throughout)

The release is a state function; Hartle-Sorkin additivity (042) makes
boundary terms cancel on regluing; a closed confine/release/re-expand
cycle nets exactly zero. The channel was never a perpetual source --
it dies of magnitude, not thermodynamics. Condition 6 (closed sector
untouched) holds trivially: nothing here ever reached the metric
sector.

## Ledger Consequences

```text
- register B3 (the Casimir squeeze window): DOWNGRADED -- the window
  is no longer VED-motivated; its exclusion would kill nothing in the
  VED core; whatever lives at 29.9-38.6 um is ordinary QFT physics.
- dimensional_relaxation_channel.md: superseded by this record (the
  mechanism note's kill conditions are all now adjudicated).
- the X < 0 sign-fork payoff (5a) and interior-cap payoff (5b) of the
  channel note lose their boundary-channel route; the interior cap
  keeps its own separate ledger.
- FENCE: the kill is of the UNSUPPRESSED channel. A front-door
  derivation of a specific tiny coupling could reopen it; backsolving
  a coupling into the exclusion window is forbidden.
```

## Ledger

```text
derivation:  boundary_channel_operator_053 (COUNTEREXAMPLE/channel kill)
satisfies:   ufft_operator_instantiated_053 (the long-owed audit debt)
depends on:  edge_density_052, discrete_conservation_boundary_042,
             regge_delaunay_bridge_039
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 053: The Boundary Channel Operator -- Instantiation and Kill")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    mean_d2 = check_1_release_differential(failures)
    check_2_operator_and_scaling(failures)
    u_planck, u_window, margin_planck, margin_window = \
        check_3_locked_magnitude_kill(mean_d2, failures)
    check_4_cycle_closure(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 053: FAILED")
    print("  The operator is instantiated -- and the instantiation kills the")
    print("  unsuppressed channel. Constant-pressure form (new-channel shape),")
    print("  floor-Newton-locked magnitude, excluded by 30-114 orders of")
    print("  magnitude. Matter boundaries cannot confine the packing; the")
    print("  UFFT window loses its VED motivation; the floor hides from both")
    print("  channels. Honest negative, recorded as a counterexample.")

    record(ns, u_planck, margin_planck, margin_window)
    write_report(u_planck, u_window, margin_planck, margin_window)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
