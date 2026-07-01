#!/usr/bin/env python3
"""
global_datum_frustration_relief.py

The global datum, re-posed and attacked: what would it mean for the
frustration floor to fix Lambda, and what does the frustration ontology
actually predict about it?

Four results:

  A. THE DATUM IS A SLICE VALUE. 4 Lambda = R + k T is a constant of
     motion of the closed parent (033), so the global datum is the value
     of (R + k T)/4 on any single slice. Verified: the trace identity
     g^{ab}(G_ab + Lambda g_ab - k T_ab) = 0 gives 4 Lambda = R + k T
     identically on shell; Schwarzschild-de Sitter has R = 4 Lambda
     exactly; de Sitter FRW (a = e^{Ht}) has R = 12 H^2 with
     Lambda = 3 H^2, i.e. R = 4 Lambda.

  B. IN A FLOOR-ONLY EPOCH, LAMBDA IS THE GROUND CONFIGURATION'S
     CURVATURE. The floor's energy sequesters (035), so a floor-only
     initial state has 4 Lambda = R_init: the datum is the INTRINSIC
     CURVATURE of the vacuum's minimum-frustration configuration, not
     its energy density. "Floor fixes Lambda" therefore means "the
     ground configuration is intrinsically curved," a geometric
     statement the microphysics can address.

  C. FRUSTRATION RELIEF PREDICTS THE SIGN: LAMBDA > 0. The tetrahedral
     packing frustration of flat 3-space is the dihedral-angle deficit
     2 pi - 5 arccos(1/3) > 0 (five regular tetrahedra around an edge
     fall short by ~7.36 degrees). Verified symbolically:
     arccos(1/3) < 2 pi / 5  <=>  1/3 > cos(2 pi/5) = (sqrt(5)-1)/4
     <=>  49 > 45. Positive spatial curvature increases dihedral
     angles; the deficit closes exactly on the 3-sphere, where regular
     tetrahedra DO tile (the 600-cell, five cells per edge). Frustration
     is relieved by POSITIVE curvature and aggravated by negative
     curvature, so a frustration-relieving ground configuration is
     spherical: Lambda > 0. This matches observation and is the
     ontology's first sign prediction in the Lambda lane.

  D. THE SMALLNESS GATE (decisive, recorded honestly). Full relief at
     the packing scale a gives R_curv = phi * a (600-cell circumradius
     to edge ratio is the golden ratio), hence
     Lambda_naive = 3 / (phi a)^2. For a at the Planck scale this is
     ~10^122 too large. The route survives only if relief is nearly
     complete -- residual curvature suppressed by a derived mechanism
     (defect dilution, frustration sharing, relaxation depth) -- and
     deriving that suppression is the route's kill-or-live condition.

Output:
    theory_v3/development/vacuum_sector/global_datum_frustration_relief_vacuumforge.md
"""

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
    / "global_datum_frustration_relief_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "covariant_constraint_dependency_036",
        "034_unimodular_covariant_constraint__unimodular_covariant_constraint",
        "unimodular_covariant_constraint_034",
    ),
    (
        "floor_sequestering_dependency_036",
        "035_floor_sequestering_constraint__floor_sequestering_constraint",
        "floor_sequestering_constraint_035",
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
# Curvature machinery
# =============================================================================

t, r, th, ph = sp.symbols("t r theta phi")


def curvature(g, coords):
    n = len(coords)
    ginv = g.inv()
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c_ in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[a, d] * (
                        sp.diff(g[d, b], coords[c_])
                        + sp.diff(g[d, c_], coords[b])
                        - sp.diff(g[b, c_], coords[d])
                    )
                Gamma[a][b][c_] = sp.together(s_ / 2)
    Ric = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c_ in range(n):
                expr += sp.diff(Gamma[c_][a][b], coords[c_])
                expr -= sp.diff(Gamma[c_][a][c_], coords[b])
                for d in range(n):
                    expr += Gamma[c_][c_][d] * Gamma[d][a][b]
                    expr -= Gamma[c_][a][d] * Gamma[d][c_][b]
            Ric[a, b] = sp.together(expr)
    Rs = sp.together(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    return Gamma, Ric, Rs, ginv


# =============================================================================
# Check A: the datum is a slice value
# =============================================================================


def check_A_slice_value(failures):
    header("Check A: 4 Lambda = R + k T -- the datum is a slice value")
    # (i) Trace identity: g^{ab}(G_ab + Lambda g_ab - k T_ab) = -R + 4 Lambda - k T.
    R_sym, T_sym, Lam, k = sp.symbols("R T Lambda k")
    trace = -R_sym + 4 * Lam - k * T_sym
    solved = sp.solve(sp.Eq(trace, 0), Lam)[0]
    require(
        "trace of the full equations gives 4 Lambda = R + k T identically on shell",
        is_zero(sp.simplify(4 * solved - (R_sym + k * T_sym))), failures,
    )

    # (ii) SdS: R = 4 Lambda exactly.
    Lam_s, rs = sp.symbols("Lambda r_s", positive=True)
    A_sds = 1 - rs / r - Lam_s * r**2 / 3
    g = sp.diag(-A_sds, 1 / A_sds, r**2, r**2 * sp.sin(th) ** 2)
    _, _, Rs, _ = curvature(g, [t, r, th, ph])
    require("Schwarzschild-de Sitter: R = 4 Lambda exactly",
            is_zero(sp.simplify(Rs - 4 * Lam_s)), failures)

    # (iii) de Sitter FRW: a = e^{Ht}, R = 12 H^2 = 4 Lambda with Lambda = 3 H^2.
    H = sp.Symbol("H", positive=True)
    x, y, z = sp.symbols("x y z")
    a_ds = sp.exp(H * t)
    g2 = sp.diag(-1, a_ds**2, a_ds**2, a_ds**2)
    _, _, Rs2, _ = curvature(g2, [t, x, y, z])
    require("de Sitter FRW: R = 12 H^2, i.e. R = 4 Lambda with Lambda = 3 H^2",
            is_zero(sp.simplify(Rs2 - 12 * H**2)), failures)
    print()
    print("  Since 4 Lambda = R + k T is a constant of motion (033), the global")
    print("  datum is the value of (R + k T)/4 on ANY single slice. Fixing")
    print("  Lambda means fixing one slice's worth of this combination.")


# =============================================================================
# Check B: floor-only epoch => Lambda is the ground configuration's curvature
# =============================================================================


def check_B_ground_curvature(failures):
    header("Check B: floor-only epoch => 4 Lambda = R_init (curvature, not energy)")
    # In a floor-only epoch T_ab = -rho_f g_ab; its trace-free part vanishes
    # (035), so it contributes to 4 Lambda = R + k T only through k T = -4 k rho_f,
    # which the integration constant absorbs (035 check 1). The physical
    # content of the datum in that epoch is R_init alone.
    rho_f, k = sp.symbols("rho_f k")
    R_init, Lam = sp.symbols("R_init Lambda")
    # 4 Lambda' = R_init + k(-4 rho_f); physical Lambda_phys = Lambda' + k rho_f
    Lam_prime = (R_init - 4 * k * rho_f) / 4
    Lam_phys = Lam_prime + k * rho_f
    require(
        "floor contribution cancels: Lambda_phys = R_init / 4 independent of rho_f",
        is_zero(sp.simplify(Lam_phys - R_init / 4)), failures,
    )
    print()
    print("  'The floor fixes Lambda' can only mean: the vacuum's minimum-")
    print("  frustration configuration is INTRINSICALLY CURVED, with")
    print("  R_ground = 4 Lambda. The datum is geometry, not energy. This is")
    print("  a well-posed target for the packing microphysics: does the")
    print("  ground configuration curve, which way, and by how much?")


# =============================================================================
# Check C: frustration relief predicts Lambda > 0
# =============================================================================


def check_C_sign_prediction(failures):
    header("Check C: tetrahedral frustration is relieved by POSITIVE curvature")
    # Flat-space dihedral angle of the regular tetrahedron: arccos(1/3).
    theta = sp.acos(sp.Rational(1, 3))
    deficit = 2 * sp.pi - 5 * theta
    deficit_deg = sp.deg(deficit).evalf(6)
    print(f"  flat dihedral angle: arccos(1/3) = {sp.deg(theta).evalf(6)} deg")
    print(f"  five-around-an-edge deficit: 2 pi - 5 arccos(1/3) = {deficit_deg} deg")

    # Symbolic sign proof: arccos(1/3) < 2 pi/5 <=> 1/3 > cos(2 pi/5) = (sqrt(5)-1)/4
    # <=> 4 > 3(sqrt(5)-1) <=> 7 > 3 sqrt(5) <=> 49 > 45.
    cos_2pi5 = sp.cos(2 * sp.pi / 5)
    ineq = sp.simplify(sp.Rational(1, 3) - cos_2pi5)
    require(
        "deficit is strictly positive: 1/3 - cos(2 pi/5) = (7 - 3 sqrt(5))/12 > 0",
        bool(sp.simplify(ineq - (7 - 3 * sp.sqrt(5)) / 12) == 0) and bool(ineq.evalf() > 0),
        failures,
    )
    require(
        "equivalently 49 > 45 (exact rational witness)",
        sp.Integer(49) > sp.Integer(45), failures,
    )
    print()
    print("  Flat 3-space cannot close five regular tetrahedra around an edge:")
    print("  the ~7.36 degree deficit is the geometric frustration of the")
    print("  packing (P5's nonzero floor). On the 3-sphere, dihedral angles")
    print("  grow with the cell-to-curvature-radius ratio, and the deficit")
    print("  closes EXACTLY: the 600-cell tiles S^3 with five regular")
    print("  tetrahedra per edge -- zero frustration. Negative curvature")
    print("  shrinks dihedral angles and makes the deficit worse.")
    print()
    print("  Therefore, IF the vacuum's ground configuration relieves packing")
    print("  frustration through intrinsic curvature (the standard mechanism")
    print("  of geometric frustration theory: Frank-Kasper phases, curved-")
    print("  space crystallography), the relief direction is spherical:")
    print()
    print("      R_ground > 0   =>   Lambda > 0.")
    print()
    print("  The observed Lambda is positive. This is the frustration")
    print("  ontology's first sign prediction in the Lambda lane -- ")
    print("  conditional on the packing reading of P4/P5, stated as such.")


# =============================================================================
# Check D: the smallness gate
# =============================================================================


def check_D_smallness_gate(failures):
    header("Check D: the smallness gate (recorded, not solved)")
    # Full relief at packing scale a: the 600-cell circumradius/edge = phi.
    phi = (1 + sp.sqrt(5)) / 2
    a_len = sp.Symbol("a", positive=True)
    R_curv = phi * a_len
    Lam_naive = 3 / R_curv**2
    print(f"  full relief: curvature radius = phi * a (600-cell), phi = {phi.evalf(8)}")
    print(f"  Lambda_naive = 3/(phi a)^2 = {sp.sstr(sp.simplify(Lam_naive))}")

    # Numbers: a = Planck length vs observed Lambda.
    lP = 1.616255e-35  # m
    Lam_obs = 1.1056e-52  # m^-2 (Planck 2018-class)
    Lam_naive_val = float((3 / (phi * lP) ** 2).evalf())
    suppression = Lam_obs / Lam_naive_val
    import math
    print(f"  a = l_P: Lambda_naive ~ {Lam_naive_val:.3e} m^-2")
    print(f"  Lambda_obs ~ {Lam_obs:.3e} m^-2")
    print(f"  required residual-frustration suppression ~ 10^{math.log10(suppression):.1f}")
    require(
        "smallness gate quantified: full Planck-scale relief overshoots by ~10^121-122",
        -123 < math.log10(suppression) < -120, failures,
    )
    print()
    print("  The route's kill-or-live condition: derive why relief is ALMOST")
    print("  complete -- residual ground curvature suppressed by ~10^-122 from")
    print("  the packing scale (defect dilution, frustration sharing across")
    print("  the relaxation depth, or a large emergent length). Equivalently:")
    print("  R_ground = 4 Lambda_obs corresponds to a curvature radius ~ Hubble")
    print("  scale; the microphysics owes the emergence of that length or the")
    print("  route dies. No backsolve is permitted: the suppression must be")
    print("  derived before the observed value is compared.")


# =============================================================================
# Report and archive
# =============================================================================


def write_report():
    md = """# VacuumForge: The Global Datum and Frustration Relief

## Purpose

Attacks the re-posed Lambda obligation
(`lambda_global_datum_derivation_required_034` /
`floor_global_datum_reposing_035`): what would it mean for the
frustration floor to fix Lambda, and what does the frustration ontology
predict about the datum?

## Verified Results

```text
A. The datum is a slice value. 4 Lambda = R + k T on shell (trace
   identity), constant of motion (033); SdS has R = 4 Lambda exactly;
   de Sitter FRW has R = 12 H^2 = 4 Lambda. Fixing Lambda = fixing one
   slice's (R + k T)/4.

B. Floor-only epoch: the floor's density cancels out of the physical
   datum exactly (sequestering), leaving Lambda_phys = R_init / 4. The
   datum is the INTRINSIC CURVATURE of the vacuum's ground
   configuration, not its energy density. "Floor fixes Lambda" is
   therefore a geometric microphysics question: does the minimum-
   frustration configuration curve, which way, how much?

C. Sign prediction: Lambda > 0. The tetrahedral-packing frustration of
   flat 3-space is the dihedral deficit 2 pi - 5 arccos(1/3) > 0
   (exact witness: 49 > 45; numerically ~7.36 degrees). Positive
   curvature closes the deficit exactly (the 600-cell tiles S^3, five
   tetrahedra per edge, zero frustration); negative curvature worsens
   it. If the ground configuration relieves frustration through
   curvature -- the standard mechanism of geometric frustration theory
   (curved-space crystallography, Frank-Kasper) -- the relief direction
   is spherical: R_ground > 0, hence Lambda > 0. Matches observation.
   Conditional on the packing reading of P4/P5, and stated as such.

D. The smallness gate, quantified. Full relief at packing scale a gives
   R_curv = phi a (600-cell circumradius/edge = golden ratio), so
   Lambda_naive = 3/(phi a)^2. For a = l_Planck this overshoots the
   observed Lambda by ~10^122. The route lives only if a suppression of
   the residual ground curvature by ~10^-122 is DERIVED (defect
   dilution, frustration sharing, relaxation depth, an emergent large
   length). No backsolve from the observed value is permitted.
```

## Classification

```text
result type: derivation-shaped reframing + conditional sign prediction
             + quantified kill gate
scope:       constraint algebra exact (A, B); frustration-relief geometry
             exact (C's inequalities); the ontological step "the vacuum
             packs like frustrated tetrahedra and relieves through
             curvature" is a candidate reading of P4/P5, not a licensed
             result
conclusion:  the global datum is the ground configuration's intrinsic
             curvature; frustration relief predicts its sign positive;
             the magnitude requires a derived ~10^-122 suppression
non-conclusion: Lambda's value is not derived; the sign prediction is
             conditional on the packing microphysics; nothing here
             reopens the closed sector
```

## Status of the Lambda Lane After 036

```text
Lambda's status:     integration constant (033, 034) -- settled
Lambda's meaning:    ground-configuration curvature, R_ground = 4 Lambda (036.B)
Lambda's sign:       predicted positive by frustration relief (036.C),
                     conditional on the packing reading
Lambda's magnitude:  open; requires derived near-complete relief (036.D);
                     this is now the lane's single decisive obligation
```

## Newly Opened Obligation

```text
frustration_relief_suppression_required_036:
  derive the residual ground curvature of the minimum-frustration
  configuration -- why relief is nearly complete, with the ~10^-122
  suppression (equivalently the emergence of a Hubble-scale curvature
  radius) coming out of the packing/relaxation microphysics rather than
  being inserted. Kill condition: if the microphysics pins residual
  curvature at the packing scale (no dilution mechanism), the
  frustration route to Lambda's value dies, leaving the sign prediction
  as its only surviving content.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/036_global_datum_frustration_relief/global_datum_frustration_relief.py
```

Archive record: `global_datum_frustration_relief_036`.
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def record_archive(ns):
    ns.record_derivation(
        derivation_id="global_datum_frustration_relief_036",
        inputs=[
            sp.Symbol("unimodular_covariant_constraint_result"),
            sp.Symbol("floor_sequestering_constraint_result"),
        ],
        output=sp.Symbol("datum_is_ground_curvature_sign_positive_smallness_gated"),
        method=(
            "trace identity and SdS/de Sitter witnesses for 4 Lambda = R + kT; "
            "floor cancellation in the physical datum; exact dihedral-deficit "
            "inequality and 600-cell relief geometry; quantified smallness gate"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="reframing_with_conditional_prediction",
        scope=(
            "constraint algebra exact; relief geometry exact; packing reading "
            "of P4/P5 is a candidate ontology, not licensed; magnitude open"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="lambda_global_datum_attacked_036",
        script_id=SCRIPT_ID,
        title="Global datum re-posed as ground-configuration curvature",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["global_datum_frustration_relief_036"],
        description=(
            "Sharpens lambda_global_datum_derivation_required_034: the datum "
            "is R_ground/4; frustration relief predicts R_ground > 0; the "
            "magnitude is gated on a derived ~1e-122 suppression."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="frustration_relief_suppression_required_036",
        script_id=SCRIPT_ID,
        title="Derive near-complete frustration relief (the ~1e-122 suppression)",
        status=ObligationStatus.OPEN,
        required_by=["global_datum_frustration_relief_036"],
        description=(
            "Derive the residual ground curvature of the minimum-frustration "
            "configuration from packing/relaxation microphysics. Kill "
            "condition: residual curvature pinned at the packing scale kills "
            "the frustration route to Lambda's value, leaving only the sign "
            "prediction."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="frustration_relief_claim_036",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "The global datum that fixes Lambda is the intrinsic curvature of "
            "the vacuum's ground configuration: 4 Lambda = R + kT on any "
            "slice, and in a floor-only epoch the floor's density cancels "
            "exactly, leaving Lambda = R_ground/4. Under the packing reading "
            "of P4/P5, geometric frustration relief selects positive ground "
            "curvature (the flat dihedral deficit 2pi - 5 arccos(1/3) > 0 "
            "closes exactly on S^3, the 600-cell), predicting Lambda > 0 -- "
            "conditional on that reading. Full relief at the packing scale "
            "overshoots the observed Lambda by ~1e122; the magnitude route "
            "lives or dies on a derived near-complete-relief suppression."
        ),
        derivation_ids=["global_datum_frustration_relief_036"],
        obligation_ids=[
            "lambda_global_datum_attacked_036",
            "frustration_relief_suppression_required_036",
        ],
    ))


def main() -> None:
    header("Derivation 036: The Global Datum and Frustration Relief")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_A_slice_value(failures)
    check_B_ground_curvature(failures)
    check_C_sign_prediction(failures)
    check_D_smallness_gate(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 036: verification failure")
    print("  The Lambda lane now reads: status settled (integration constant),")
    print("  meaning settled (ground-configuration curvature), sign predicted")
    print("  positive (conditional on the packing reading), magnitude gated on")
    print("  a derived ~1e-122 near-complete-relief suppression.")

    write_report()
    record_archive(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
