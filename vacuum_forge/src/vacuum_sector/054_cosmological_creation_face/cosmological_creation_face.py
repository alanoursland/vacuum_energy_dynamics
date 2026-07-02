#!/usr/bin/env python3
"""
cosmological_creation_face.py

Derivation 054: the cosmological-creation observable face -- the 045
seam is DECIDED. Expansion is creation of new cells, not stretching
of old ones.

Derivation 045 left an underdetermination: does cosmic expansion mean
(a) STRETCH -- a fixed graph whose cells dilate with the scale factor
    (edge length l(t) = l_0 a(t), cell count N fixed), or
(b) GROWTH -- new cells created at fixed packing scale
    (l = const, N proportional to a^3)?

Register C3 hoped the readings would differ someday in the perturbed
kappa-leak profile. This derivation finds they differ TODAY, twice,
and existing data executes both kills against the stretch reading:

  KILL 1 (G DRIFT). The floor-Newton lock (039) ties Newton's G to
  the packing scale: G proportional to 1/(f'(Delta_0) l). Under
  stretch, l grows with a(t), so
      Gdot/G = -ldot/l = -H(t) ~ -7.2e-11 / yr,
  while lunar laser ranging bounds |Gdot/G| < ~1.5e-13 / yr.
  EXCLUDED BY A FACTOR ~480. A stretched packing drags Newton's
  constant at the Hubble rate; nature says G does not drift.

  KILL 2 (THE FLOOR TURNS TO DUST). Wedge energies are exactly
  dilation-invariant (038; measured many-body in 041 E3). Under
  stretch the total floor energy E = const while V grows: the floor's
  pressure is p = -dE/dV = 0 -- it becomes DUSTLIKE (w = 0) at
  ~Planck density. A w = 0 component is NOT sequestered (P3
  sequesters constant DENSITY, not constant total energy): the floor
  would gravitate as dark matter at ~1e122 times closure density.
  Instantly excluded; also destroys the sequestering architecture
  A1/B1 rest on.

  THE SURVIVOR IS SELF-CONSISTENT AND SELF-FUNDING. Under growth,
  l = const: G is exactly constant (kill 1 inverted into a
  commitment), and the floor is intensive -- u = const, which 051
  MEASURED. Intensivity is the substance-level equation of state:
  E = uV gives p = -dE/dV = -u, i.e. w = -1 EXACTLY. The energy
  that funds new frustrated cells is exactly the negative-pressure
  work of the floor itself (dE = u dV = -p dV): creation pays for
  itself through w = -1. The 045 seam's "where does creation's
  energy come from" closes: the first law closes it, term by term.

  THE SUPPRESSION CLAUSE (the owner's vacuum-flow intuition: mass
  constrains creation; new space appears preferentially outside
  wells). Writing the creation rate C = 3H(1 - alpha delta) with
  delta the density contrast: since <delta> = 0, the background is
  EXACTLY unchanged for any alpha -- the clause lives entirely in
  the perturbation/substance sector, invisible to everything derived
  so far. It survives as the recorded watch item for O-P10-4's
  Lorentzian dynamics (the packing's initial-value problem is where
  alpha would become computable).

NEW REGISTER COMMITMENT (A6): Gdot = 0, exactly, forever. The
surviving reading has no mechanism for G drift at all -- any
confirmed nonzero Gdot/G now falsifies the graph-growth reading and
with it P10's account of expansion. The barrel is pointed before the
next LLR/ephemeris improvement lands.

Fence: the metric sector is untouched throughout (both readings
source the same dust stress; the closed equations never cared which
bookkeeping the substance uses). What is decided is the SUBSTANCE
ontology's reading of expansion -- decided by its two side effects
(G drift, floor equation of state), not by any new metric term.
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
               / "08_packing_microphysics" / "cosmological_creation_face_vacuumforge.md")

DEPENDENCIES = [
    ("seam_dep_054", "045_p6_p10_consistency__p6_p10_consistency",
     "p6_p10_consistency_045"),
    ("intensivity_dep_054", "051_bulk_relaxation_phase2__bulk_relaxation_phase2",
     "bulk_relaxation_phase2_051"),
    ("lock_dep_054", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
]

H0_PER_YR = 7.16e-11          # H0 = 70 km/s/Mpc in 1/yr
LLR_GDOT_BOUND_PER_YR = 1.5e-13  # lunar laser ranging |Gdot/G| bound
RHO_CRIT_J_M3 = 8.6e-10       # critical density, J/m^3
U_FLOOR_PLANCK = 5.07e112     # 053's locked floor density at Planck packing


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


def check_1_dichotomy(failures):
    header("Check 1: the dichotomy, formalized -- both readings give V ~ a^3")
    t = sp.Symbol("t", positive=True)
    a = sp.Function("a", positive=True)(t)
    l0, N0, v0 = sp.symbols("l0 N0 v0", positive=True)
    # cell volume ~ v0 * l^3; stretch: l = l0 a, N = N0; growth: l = l0, N = N0 a^3
    V_stretch = N0 * v0 * (l0 * a) ** 3
    V_growth = (N0 * a**3) * v0 * l0**3
    require("V_stretch = V_growth = N0 v0 l0^3 a^3 (same background volume history)",
            sp.simplify(V_stretch - V_growth) == 0, failures)
    # both readings carry the same dust stress: rho_m ~ M/V ~ a^-3 either way
    M = sp.Symbol("M", positive=True)
    require("both readings give identical dust dilution rho_m ~ a^-3 "
            "(the metric face cannot tell them apart)",
            sp.simplify(M / V_stretch - M / V_growth) == 0, failures)
    print("  The closed equations see the same T_ab under both readings: the")
    print("  metric sector is silent on the seam, exactly as 045 recorded.")
    print("  The discriminators are the SIDE EFFECTS on locked quantities.")


def check_2_stretch_kill_g_drift(failures):
    header("Check 2: KILL 1 -- stretch drags Newton's G at the Hubble rate")
    t = sp.Symbol("t", positive=True)
    a = sp.Function("a", positive=True)(t)
    l0, K = sp.symbols("l0 K", positive=True)
    ell = l0 * a                       # stretch reading
    G = K / ell                        # floor-Newton lock: G ~ 1/(f'(Delta_0) l)
    gdot_over_g = sp.simplify(sp.diff(G, t) / G)
    H = sp.diff(a, t) / a
    require("lock consequence: Gdot/G = -ldot/l = -H(t) exactly",
            sp.simplify(gdot_over_g + H) == 0, failures)
    margin = H0_PER_YR / LLR_GDOT_BOUND_PER_YR
    print(f"  |Gdot/G|_stretch = H0 = {H0_PER_YR:.2e}/yr")
    print(f"  LLR bound:              {LLR_GDOT_BOUND_PER_YR:.2e}/yr")
    print(f"  exclusion margin: {margin:.0f}x")
    require("stretch reading excluded by lunar laser ranging (margin > 100x)",
            margin > 100, failures)
    print("  A packing whose cells dilate with the scale factor cannot keep")
    print("  Newton's constant fixed: the same lock that derives G from the")
    print("  wedge stiffness forces it to drift at H. Nature's G does not")
    print("  drift. The stretch reading is DEAD on existing data.")


def check_3_stretch_kill_floor_dust(failures):
    header("Check 3: KILL 2 -- under stretch, the floor turns to gravitating dust")
    V, E0 = sp.symbols("V E0", positive=True)
    # Dilation invariance (038, 041 E3): wedge energies unchanged by uniform
    # dilation => total floor energy CONSTANT under stretch while V grows.
    E_stretch = E0
    p_stretch = -sp.diff(E_stretch, V)
    require("dilation-invariant wedges: p_floor = -dE/dV = 0 under stretch (w = 0, dust)",
            sp.simplify(p_stretch) == 0, failures)
    # A w = 0 floor is NOT sequestered: P3 sequesters constant density.
    # Density under stretch: u = E0/V ~ a^-3 -- NOT constant => visible.
    u_stretch = E_stretch / V
    require("floor density dilutes (u ~ 1/V): not a constant density -- "
            "sequestering does not protect it",
            sp.simplify(sp.diff(u_stretch, V)) != 0, failures)
    overclosure = U_FLOOR_PLANCK / RHO_CRIT_J_M3
    print(f"  the unsequestered dustlike floor would weigh in at "
          f"~{overclosure:.1e} x closure density")
    require("stretch floor overcloses the universe by > 1e100 (instant kill)",
            overclosure > 1e100, failures)
    print("  Under stretch the floor stops being a constant density (the one")
    print("  thing P3 sequesters) and becomes Planck-density dark matter --")
    print("  excluded by ~122 orders, and it would also demolish the")
    print("  sequestering architecture A1/B1 stand on. Second, independent")
    print("  kill: the stretch reading dies twice.")


def check_4_growth_self_consistency(failures):
    header("Check 4: the survivor -- growth is self-consistent and SELF-FUNDING")
    V = sp.Symbol("V", positive=True)
    u = sp.Symbol("u_floor", positive=True)   # intensive: constant, as 051 measured
    E_growth = u * V
    p_growth = -sp.diff(E_growth, V)
    require("intensive floor: p = -dE/dV = -u exactly (w = -1, the substance-level "
            "equation of state)", sp.simplify(p_growth + u) == 0, failures)
    # Self-funding: energy cost of new cells = negative-pressure work.
    dV = sp.Symbol("dV", positive=True)
    creation_cost = u * dV
    pressure_work = -p_growth * dV
    require("creation is self-funding: u dV = -p dV term by term (first law closes)",
            sp.simplify(creation_cost - pressure_work) == 0, failures)
    # G constancy under growth: l = const => G = const.
    t = sp.Symbol("t", positive=True)
    l0, K = sp.symbols("l0 K", positive=True)
    G_growth = K / l0
    require("growth reading: Gdot = 0 exactly (l constant)",
            sp.diff(G_growth, t) == 0, failures)
    print("  Everything locks together: 051's MEASURED intensivity is w = -1")
    print("  at the substance level; the floor's negative-pressure work pays")
    print("  for each new frustrated cell exactly; G never moves. The 045")
    print("  seam's energy-budget worry closes by the first law. Expansion IS")
    print("  creation -- and the reading now carries a falsifier: any")
    print("  confirmed Gdot != 0 kills it (register A6, new).")


def check_5_suppression_clause(failures):
    header("Check 5: the suppression clause (vacuum flow) -- background-invisible")
    H, alpha = sp.symbols("H alpha", positive=True)
    delta = sp.Symbol("delta", real=True)
    C = 3 * H * (1 - alpha * delta)     # creation rate with well-suppression
    C_background = C.subs(delta, 0)     # <delta> = 0 over the background
    require("<C> = 3H for ANY alpha: the clause is exactly invisible to the "
            "background", sp.simplify(C_background - 3 * H) == 0, failures)
    require("first-order response is pure perturbation: dC/d delta = -3 H alpha "
            "(lives in the substance/perturbation sector)",
            sp.simplify(sp.diff(C, delta) + 3 * H * alpha) == 0, failures)
    print("  The owner's flow intuition -- mass suppresses creation, new space")
    print("  appears preferentially outside wells and is 'pushed out' -- is")
    print("  formalized as C = 3H(1 - alpha delta). It changes NOTHING derived")
    print("  so far (background exact for any alpha; metric face independent of")
    print("  the bookkeeping) and becomes computable only when O-P10-4's")
    print("  Lorentzian dynamics supplies alpha. Recorded as the watch item")
    print("  creation_suppression_dynamics_054.")


def record(ns):
    ns.record_derivation(
        derivation_id="cosmological_creation_face_054",
        inputs=[sp.Symbol("floor_newton_lock_039"), sp.Symbol("dilation_invariance_038_041"),
                sp.Symbol("intensivity_051"), sp.Symbol("llr_gdot_bound")],
        output=sp.Symbol("expansion_is_creation_stretch_killed_twice_gdot_zero_commitment"),
        method=(
            "dichotomy formalized (same a^3 volume and dust stress both "
            "readings); stretch kill 1: lock gives Gdot/G = -H, excluded ~480x "
            "by LLR; stretch kill 2: dilation-invariant wedges make the floor "
            "dustlike (w = 0) at ~1e122 x closure, unsequestered; growth "
            "survivor: intensivity <=> w = -1 exactly, creation self-funded by "
            "negative-pressure work, G exactly constant; suppression clause "
            "C = 3H(1 - alpha delta) background-invisible for any alpha"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="ontology_reading_decision_theorem",
        scope=(
            "decides the substance ontology's reading of expansion by its side "
            "effects on locked quantities; the metric sector untouched (both "
            "readings source identical dust); alpha (the suppression "
            "coefficient) awaits O-P10-4 dynamics"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="creation_seam_decided_054",
        script_id=SCRIPT_ID,
        title="The 045 creation seam DECIDED: expansion is graph growth, not stretch",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["cosmological_creation_face_054"],
        description=(
            "Resolves p6_p10_cosmological_creation_045 / register C3: the "
            "stretch reading is killed twice on existing data (G drift at H "
            "vs LLR, margin ~480; floor turned to Planck-density dust, "
            "~1e122 x closure). The growth reading survives, is self-funding "
            "(intensivity <=> w = -1; first law closes creation's budget), "
            "and commits to Gdot = 0 exactly (new register entry A6)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="creation_suppression_dynamics_054",
        script_id=SCRIPT_ID,
        title="Derive alpha: the creation-suppression coefficient (vacuum flow)",
        status=ObligationStatus.OPEN,
        required_by=["cosmological_creation_face_054"],
        description=(
            "The owner's flow intuition formalized as C = 3H(1 - alpha "
            "delta): background-invisible for any alpha, so nothing derived "
            "constrains it. O-P10-4's Lorentzian/initial-value dynamics is "
            "where alpha becomes computable (creation rate as a functional "
            "of local strain). Until then: substance-sector watch item; no "
            "observable claimed."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="creation_face_claim_054",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Cosmic expansion, read through P10, is the CREATION of new "
            "packing cells at fixed scale -- not the stretching of existing "
            "ones. The stretch reading is excluded twice by existing data: "
            "the floor-Newton lock would drag G at the Hubble rate (LLR "
            "excludes by ~480x), and dilation-invariant wedge energies would "
            "turn the floor into unsequestered Planck-density dust (~1e122 x "
            "closure). The surviving growth reading is exactly self-funding: "
            "the measured intensivity of the floor IS w = -1 at the "
            "substance level, and the floor's negative-pressure work pays "
            "for each new cell term by term. New standing commitment: "
            "Gdot = 0 exactly (A6). The well-suppression clause (vacuum "
            "flow) is formalized and background-invisible; its coefficient "
            "awaits O-P10-4 dynamics."
        ),
        derivation_ids=["cosmological_creation_face_054"],
        obligation_ids=["creation_seam_decided_054"],
    ))


def write_report():
    md = f"""# The Cosmological-Creation Face (the 045 Seam, Decided) -- VacuumForge Record

## Status

```text
result type:   ontology-reading decision theorem (2026-07-02,
               derivation 054)
conclusion:    EXPANSION IS CREATION. The stretch reading (fixed graph,
               dilating cells) is killed TWICE on existing data; the
               growth reading (new cells at fixed packing scale)
               survives, is exactly self-funding, and commits the
               theory to Gdot = 0 forever (new register entry A6).
resolves:      p6_p10_cosmological_creation_045; register C3
opens:         creation_suppression_dynamics_054 (the vacuum-flow
               coefficient alpha; O-P10-4 territory)
verification:  vacuum_forge/src/vacuum_sector/054_cosmological_creation_face/
```

## The Seam

045 proved P6 and P10 consistent but left expansion's reading open:
stretch (l = l_0 a(t), N fixed) vs growth (l fixed, N ~ a^3). Both
give the same a^3 volume history and the same dust stress -- the
closed metric sector cannot tell them apart, and never will. The
discriminators are the readings' side effects on LOCKED quantities.

## Kill 1: Stretch Drags Newton's Constant

```text
floor-Newton lock (039):  G ~ 1/(f'(Delta_0) l)
stretch:                  l = l_0 a(t)  =>  Gdot/G = -H ~ -7.2e-11/yr
lunar laser ranging:      |Gdot/G| < 1.5e-13/yr
EXCLUDED, margin ~480x.
```

## Kill 2: Stretch Turns the Floor into Planck-Density Dark Matter

```text
wedge energies are exactly dilation-invariant (038; measured in 041 E3)
=> under stretch, E_floor = const while V grows
=> p_floor = -dE/dV = 0: DUSTLIKE (w = 0)
=> density u = E/V ~ a^-3 is NOT constant => NOT sequestered (P3
   protects constant density only)
=> a w = 0 component at ~5e112 J/m^3 gravitates: ~1e122 x closure.
EXCLUDED instantly; would also demolish the sequestering architecture
(A1, B1). The stretch reading dies twice, independently.
```

## The Survivor: Creation, Exactly Self-Funding

```text
growth: l = const  =>  G = const EXACTLY (kill 1 inverts into a
                       standing commitment, register A6)
floor intensive (u = const -- MEASURED, 051 E1)
   =>  p = -dE/dV = -u:  w = -1 EXACTLY at the substance level
   =>  creation cost u dV = negative-pressure work -p dV, term by term:
       THE FIRST LAW FUNDS CREATION. The 045 energy-budget seam closes.
```

The chain is tight: 051's measured intensivity IS the w = -1 equation
of state; w = -1 is what makes creation free-standing; and the same
constancy of l that funds it keeps G fixed. One reading, three locks,
zero tuning.

## The Vacuum-Flow Clause (the owner's founding intuition, formalized)

```text
C = 3H(1 - alpha delta):  mass suppresses local creation; new space
appears preferentially outside wells ("pushed out").
<delta> = 0  =>  <C> = 3H for ANY alpha: exactly invisible to the
background and to everything so far derived. alpha becomes computable
only with O-P10-4's Lorentzian dynamics (creation as a functional of
local strain). Watch item: creation_suppression_dynamics_054. No
observable is claimed for it -- yet.
```

## New Register Entry (A6)

```text
commitment:  Gdot = 0. Exactly. Forever.
forced by:   the surviving creation reading (l = const) + the
             floor-Newton lock. There is NO mechanism for G drift
             left in the theory.
kills it:    any confirmed nonzero Gdot/G (LLR, ephemerides, pulsar
             timing, BBN consistency). Current bounds ~1.5e-13/yr and
             tightening.
distinctive: scalar-tensor/varying-G rivals generically predict
             drift; VED now forbids it outright -- pre-registered
             BEFORE the next data release, as the register requires.
```

## Ledger

```text
derivation:  cosmological_creation_face_054
satisfies:   creation_seam_decided_054 (045 seam; register C3)
opens:       creation_suppression_dynamics_054 (alpha; O-P10-4)
depends on:  p6_p10_consistency_045, bulk_relaxation_phase2_051,
             regge_delaunay_bridge_039
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 054: The Cosmological-Creation Face -- the Seam Decided")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_dichotomy(failures)
    check_2_stretch_kill_g_drift(failures)
    check_3_stretch_kill_floor_dust(failures)
    check_4_growth_self_consistency(failures)
    check_5_suppression_clause(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 054: FAILED")
    print("  EXPANSION IS CREATION. Stretch killed twice on existing data")
    print("  (G drift ~480x over LLR; floor-turned-dust ~1e122 x closure).")
    print("  Growth survives, self-funded by the floor's w = -1 (051's")
    print("  measured intensivity), with G exactly constant. New standing")
    print("  falsifier: Gdot = 0 (register A6). The vacuum-flow clause is")
    print("  formalized, background-invisible, and waits on O-P10-4 for its")
    print("  coefficient.")

    record(ns)
    write_report()
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
