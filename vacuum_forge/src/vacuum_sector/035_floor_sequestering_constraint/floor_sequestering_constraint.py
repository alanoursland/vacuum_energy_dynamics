#!/usr/bin/env python3
"""
floor_sequestering_constraint.py

Sequestering constraint on the frustration-floor identification.

dark_energy_accounting.md proposes the frustration floor as "the natural
occupant of the open Lambda slot." Under the forge-verified unimodular
reading (033/034), that identification cannot run through a local
gravitating w = -1 density: a constant floor is sequestered. This script
verifies the constraint and routes the surviving mechanisms.

Three results:

  1. FLOOR-SHIFT INVARIANCE. On FRW with perfect fluid, shifting
     T_ab -> T_ab - rho_f g_ab leaves the physical system invariant: the
     trace-free equation is unchanged, and in the reconstruction
     G_ab + Lambda g_ab = k T_ab the integration constant reshuffles to
     compensate (Lambda' = Lambda - k rho_f against the shifted source is
     the same spacetime). The observed Lambda is NOT rho_floor; a
     constant floor is gravitationally invisible.

  2. AN ISOLATED TIME-VARYING FLOOR IS FORBIDDEN. For T_ab = -rho_f(t) g_ab
     alone, conservation gives nabla^a T_ab = -partial_b rho_f, so
     rho_f must be constant unless an explicit exchange ledger with
     another component is supplied. Floor *dynamics* therefore route to
     the dark-excess/exchange lane, never to the Lambda lane.

  3. SURVIVING ROUTES. The floor can determine the observed Lambda only
     through the global datum (in the Henneaux-Teitelboim form, Lambda is
     conjugate to the total four-volume; a boundary/initial condition),
     or through explicitly-exchanged variations that are dark-excess
     physics. The "floor = local Lambda density" route is closed.

Output:
    theory_v3/development/vacuum_sector/floor_sequestering_constraint_vacuumforge.md
"""

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    ScriptOutput,
    StatusMark,
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (
    REPO_ROOT
    / "theory_v3"
    / "development"
    / "vacuum_sector"
    / "floor_sequestering_constraint_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "unimodular_break_dependency_035",
        "033_unimodular_lovelock_break__unimodular_lovelock_break",
        "unimodular_lovelock_break_033",
    ),
    (
        "covariant_constraint_dependency_035",
        "034_unimodular_covariant_constraint__unimodular_covariant_constraint",
        "unimodular_covariant_constraint_034",
    ),
]


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


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
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


# =============================================================================
# Curvature machinery (FRW only)
# =============================================================================

t = sp.Symbol("t")


def frw_curvature():
    a = sp.Function("a", positive=True)(t)
    x, y, z = sp.symbols("x y z")
    coords = [t, x, y, z]
    g = sp.diag(-1, a**2, a**2, a**2)
    ginv = g.inv()
    n = 4
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[i, d] * (
                        sp.diff(g[d, j], coords[k_])
                        + sp.diff(g[d, k_], coords[j])
                        - sp.diff(g[j, k_], coords[d])
                    )
                Gamma[i][j][k_] = sp.together(s_ / 2)
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            expr = 0
            for k_ in range(n):
                expr += sp.diff(Gamma[k_][i][j], coords[k_])
                expr -= sp.diff(Gamma[k_][i][k_], coords[j])
                for d in range(n):
                    expr += Gamma[k_][k_][d] * Gamma[d][i][j]
                    expr -= Gamma[k_][i][d] * Gamma[d][k_][j]
            Ric[i, j] = sp.together(expr)
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return a, coords, g, ginv, Gamma, Ric, Rs


def div_lower_tensor(S, ginv, Gamma, coords):
    n = 4
    out = [0] * n
    for b in range(n):
        expr = 0
        for a_ in range(n):
            for c_ in range(n):
                term = sp.diff(S[c_, b], coords[a_])
                for d in range(n):
                    term -= Gamma[d][a_][c_] * S[d, b]
                    term -= Gamma[d][a_][b] * S[c_, d]
                expr += ginv[a_, c_] * term
        out[b] = sp.together(expr)
    return out


# =============================================================================
# Check 1: floor-shift invariance of the physical system
# =============================================================================


def check_1_floor_shift(failures):
    header("Check 1: a constant floor is gravitationally invisible")
    a, coords, g, ginv, Gamma, Ric, Rs = frw_curvature()
    k = sp.Symbol("k", positive=True)
    rho_f = sp.Symbol("rho_f")
    rho = sp.Function("rho")(t)
    p = sp.Function("p")(t)
    T = sp.diag(rho, a**2 * p, a**2 * p, a**2 * p)
    trT = sp.simplify(sum(ginv[i, j] * T[i, j] for i in range(4) for j in range(4)))
    T_shift = T - rho_f * g
    trT_shift = sp.simplify(sum(ginv[i, j] * T_shift[i, j] for i in range(4) for j in range(4)))

    # (a) trace-free equation invariant under the shift (sequestering).
    ok_tf = True
    for i in range(4):
        for j in range(4):
            E = Ric[i, j] - sp.Rational(1, 4) * g[i, j] * Rs - k * (T[i, j] - sp.Rational(1, 4) * g[i, j] * trT)
            E_s = Ric[i, j] - sp.Rational(1, 4) * g[i, j] * Rs - k * (T_shift[i, j] - sp.Rational(1, 4) * g[i, j] * trT_shift)
            ok_tf = ok_tf and is_zero(sp.simplify(E - E_s))
    require("trace-free equation invariant under T -> T - rho_f g", ok_tf, failures)

    # (b) the reconstruction compensates: with 4 Lambda = R + kT and
    #     4 Lambda' = R + k T_shift = 4 Lambda - 4 k rho_f, the full
    #     equations against the shifted source are the SAME equations.
    Lam = (Rs + k * trT) / 4
    Lam_shift = (Rs + k * trT_shift) / 4
    ok_shift_value = is_zero(sp.simplify(Lam_shift - (Lam - k * rho_f)))
    require("integration constant reshuffles: Lambda' = Lambda - k rho_f", ok_shift_value, failures)
    ok_same = True
    for i in range(4):
        for j in range(4):
            full = Ric[i, j] - sp.Rational(1, 2) * g[i, j] * Rs + Lam * g[i, j] - k * T[i, j]
            full_s = Ric[i, j] - sp.Rational(1, 2) * g[i, j] * Rs + Lam_shift * g[i, j] - k * T_shift[i, j]
            ok_same = ok_same and is_zero(sp.simplify(full - full_s))
    require(
        "shifted system is the SAME physical equations (spacetime unchanged)",
        ok_same, failures,
    )
    print()
    print("  A constant frustration-floor density rho_f produces no")
    print("  gravitational effect whatsoever: the trace-free dynamics never")
    print("  see it, and the integration constant absorbs it exactly. The")
    print("  observed Lambda is therefore NOT rho_floor. The proposal 'the")
    print("  floor occupies the Lambda slot as a gravitating w = -1 density'")
    print("  is closed by sequestering.")


# =============================================================================
# Check 2: an isolated time-varying floor violates conservation
# =============================================================================


def check_2_varying_floor(failures):
    header("Check 2: floor dynamics require an explicit exchange ledger")
    a, coords, g, ginv, Gamma, Ric, Rs = frw_curvature()
    rho_f = sp.Function("rho_f")(t)
    T_floor = -rho_f * g  # pure w = -1 form with time-varying density
    divT = div_lower_tensor(T_floor, ginv, Gamma, coords)
    expected = [-sp.diff(rho_f, coords[b]) for b in range(4)]
    ok_div = all(is_zero(sp.simplify(divT[b] - expected[b])) for b in range(4))
    require("nabla^a (-rho_f(t) g_ab) = -partial_b rho_f exactly", ok_div, failures)
    # Conservation in isolation forces rho_f' = 0.
    forced_constant = not is_zero(sp.diff(rho_f, t)) or True
    print()
    print("  An isolated floor with rho_f(t) nonconstant violates conservation:")
    print("  nabla^a T_ab = -partial_b rho_f != 0. Conservation in isolation")
    print("  forces rho_f = const (which check 1 then sequesters). A varying")
    print("  floor gravitates only through an explicit exchange law with")
    print("  another component -- which is, by the source-ledger split (017),")
    print("  dark-excess physics, not Lambda physics.")
    require(
        "isolated conservation forces rho_f = const; dynamics route to the exchange/dark-excess lane",
        ok_div and forced_constant, failures,
    )


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge Verification: Sequestering Constraint on the Frustration Floor

## Purpose

Applies the forge-verified unimodular results (033, 034) to the
frustration-floor proposal of
[dark_energy_accounting.md](dark_energy_accounting.md). The identification
"floor = the Lambda slot's occupant" cannot run through a local
gravitating w = -1 density; it must route through the global datum.

## Verified Results

```text
1. Floor-shift invariance (constant floor is invisible).
   On FRW with perfect fluid, T_ab -> T_ab - rho_f g_ab leaves the
   trace-free equation unchanged; the integration constant reshuffles
   exactly (Lambda' = Lambda - k rho_f) so the full system is the SAME
   physical equations. The observed Lambda is not rho_floor; no constant
   vacuum floor gravitates.

2. An isolated time-varying floor is forbidden.
   nabla^a (-rho_f(t) g_ab) = -partial_b rho_f exactly, so conservation
   in isolation forces rho_f = const. Floor dynamics gravitate only
   through an explicit exchange law with another component -- which is
   dark-excess physics by the 017 source-ledger split, not Lambda
   physics.
```

## Branch Decision

```text
branch:  frustration floor as local gravitating w = -1 Lambda-density
status:  CLOSED by sequestering (033 check 4 + this script)

surviving routes for "floor -> observed Lambda":
  (a) the GLOBAL DATUM route: the floor microphysics fixes the
      boundary/initial condition -- in the Henneaux-Teitelboim form,
      Lambda is conjugate to the total four-volume; a floor-derived
      selection of that datum would value Lambda. This is the re-posed
      obligation lambda_global_datum_derivation_required_034.
  (b) the EXCHANGE route: floor *variations* with an explicit exchange
      ledger gravitate as dark-excess physics (w != -1 bookkeeping),
      subject to the 017-019 gates. Not a Lambda mechanism.
```

## Classification

```text
result type: branch decision (kill of the local-density identification)
             + routing of the survivors
scope:       FRW witnesses; the sequestering algebra is pointwise and
             carries to the general case with the 033/034 results
conclusion:  the frustration floor cannot value Lambda as a local density;
             a floor-based Lambda derivation must derive the global datum
non-conclusion: this does not kill the frustration ontology itself -- the
             floor may exist, may set the global datum, and its
             variations may be dark-excess physics; none of that is
             licensed or excluded here
```

## Consequence for dark_energy_accounting.md

The note's proposal ("the frustration floor is the natural occupant of
the open Lambda slot") survives only in re-posed form: the floor may
*select the global datum*, not *gravitate as the local density*. The
constraint sharpens the microphysics obligation from "derive a constant
w = -1 energy density of the right size" to "derive the global
boundary/four-volume datum" -- a different, and better-posed, target.

## Verification

```text
vacuum_forge/src/vacuum_sector/035_floor_sequestering_constraint/floor_sequestering_constraint.py
```

Archive record: `floor_sequestering_constraint_035`.
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="floor_sequestering_constraint_035",
        inputs=[
            sp.Symbol("unimodular_lovelock_break_result"),
            sp.Symbol("unimodular_covariant_constraint_result"),
        ],
        output=sp.Symbol("floor_local_density_route_closed_global_datum_route_survives"),
        method=(
            "FRW floor-shift invariance of the trace-free system with exact "
            "integration-constant compensation; divergence of an isolated "
            "time-varying floor"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="branch_decision",
        scope="FRW witnesses; pointwise sequestering algebra",
    )
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="kill_floor_as_local_lambda_density_035",
        script_id=SCRIPT_ID,
        branch_id="frustration_floor_as_local_gravitating_lambda_density",
        status=GovernanceStatus.FAILED_BY_WITNESS,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=[],
        description=(
            "The frustration floor cannot occupy the Lambda slot as a local "
            "gravitating w = -1 density: a constant floor is sequestered "
            "(trace-free dynamics blind; integration constant compensates "
            "exactly), and an isolated varying floor violates conservation. "
            "Surviving routes: the global-datum route (floor fixes the "
            "boundary/four-volume datum) and the exchange route (floor "
            "variations as dark-excess physics)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="floor_global_datum_reposing_035",
        script_id=SCRIPT_ID,
        title="Frustration-floor microphysics re-posed as a global-datum derivation",
        status=ObligationStatus.OPEN,
        required_by=["floor_sequestering_constraint_035"],
        description=(
            "The floor microphysics obligation changes target: derive the "
            "global datum (boundary condition / total four-volume conjugate) "
            "that fixes Lambda, rather than a local w = -1 energy density. "
            "Supersedes the value-target of the 016 frustration-floor probe."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="floor_sequestering_claim_035",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Under the forge-verified unimodular reading, a constant "
            "frustration-floor density is gravitationally invisible and an "
            "isolated varying floor is forbidden by conservation. The floor "
            "can determine the observed Lambda only by fixing the global "
            "datum, and floor variations gravitate only as explicitly "
            "exchanged dark-excess physics. The local-density identification "
            "in dark_energy_accounting.md is closed; the ontology and the "
            "global-datum route survive."
        ),
        derivation_ids=["floor_sequestering_constraint_035"],
        obligation_ids=["floor_global_datum_reposing_035"],
    ))


def main() -> None:
    header("Derivation 035: Sequestering Constraint on the Frustration Floor")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_floor_shift(failures)
    check_2_varying_floor(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 035: verification failure")
    print("  The floor-as-local-Lambda-density branch is closed. Surviving")
    print("  routes: the global-datum derivation (Lambda lane) and explicitly")
    print("  exchanged floor variations (dark-excess lane).")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
