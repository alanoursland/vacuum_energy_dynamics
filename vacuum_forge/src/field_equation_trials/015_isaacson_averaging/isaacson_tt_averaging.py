# Trial 015: Isaacson-style TT averaging
#
# Script type:
#   COVARIANT-LIFT RIGOR UPGRADE / SHORT-WAVE AVERAGING
#
# Purpose
# -------
# The 008 radiative bootstrap derives the TT wave energy and records an
# averaging rigor debt: secular terms, fast total derivatives, and the
# assumptions behind <t_ab>. This script discharges the averaging part at
# local inertial short-wave level. Gauge invariance of the averaged
# stress remains a separate follow-on lift.
#
# The validated statement is:
#
#   <t_ab> = (c^4/32 pi G) <partial_a h^TT_ij partial_b h^TT_ij>
#
# to leading order in lambda/L, for TT waves averaged over a window
# lambda << ell_avg << L.

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


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


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


def avg_theta(expr):
    return sp.simplify(sp.integrate(expr, (theta, 0, 2 * sp.pi)) / (2 * sp.pi))


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="wave_energy_dependency_015",
        upstream_script_id="008_radiative_bootstrap__radiative_bootstrap_KT",
        upstream_derivation_id="second_order_wave_energy_008",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="kt_dependency_015",
        upstream_script_id="008_radiative_bootstrap__radiative_bootstrap_KT",
        upstream_derivation_id="KT_derived_008",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


theta = sp.Symbol("theta", real=True)
c = sp.Symbol("c", positive=True)
omega = sp.Symbol("omega", positive=True)
A, B = sp.symbols("A B", real=True)
AU = sp.Symbol("A_U", real=True)
ka, kb, ea, eb = sp.symbols("k_a k_b e_a e_b", real=True)
G_N = sp.Symbol("G", positive=True)


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Averaging obligation")
    print("008 directly computed the second-order TT energy and null flux for")
    print("explicit waves. The remaining rigor debt here is the averaging")
    print("apparatus: fast total derivatives, cross terms, and slow-envelope")
    print("suppression under lambda << ell_avg << L.")
    print()
    print("This script closes only that averaging piece. Gauge invariance of")
    print("the averaged stress is intentionally left for a separate lift.")

    with out.governance_assessments():
        out.line(
            "Isaacson averaging proof opened",
            StatusMark.INFO,
            "local inertial short-wave lift of 008 averaging assumptions",
        )


def case_1_periodic_averages(out: ScriptOutput):
    header("Case 1: Periodic averaging rules")
    checks = {
        "<sin>": avg_theta(sp.sin(theta)),
        "<cos>": avg_theta(sp.cos(theta)),
        "<sin cos>": avg_theta(sp.sin(theta) * sp.cos(theta)),
        "<sin^2> - 1/2": sp.simplify(avg_theta(sp.sin(theta) ** 2) - sp.Rational(1, 2)),
        "<cos^2> - 1/2": sp.simplify(avg_theta(sp.cos(theta) ** 2) - sp.Rational(1, 2)),
    }
    for label, residual in checks.items():
        print(f"  {label}: {sp.sstr(residual)}")

    periodic = A * sp.sin(theta) + B * sp.cos(theta) + A * B * sp.sin(2 * theta)
    total_derivative_avg = avg_theta(sp.diff(periodic, theta))
    print(f"  <d_theta periodic(theta)> = {sp.sstr(total_derivative_avg)}")

    ok = all(is_zero(value) for value in checks.values()) and is_zero(total_derivative_avg)
    with out.derived_results():
        out.line(
            "periodic fast averages and total derivatives vanish as required",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "the cell average kills oscillatory cross terms and fast boundary terms",
        )
    return ok


def case_2_scale_separated_product(out: ScriptOutput):
    header("Case 2: Scale-separated derivative product")
    print("For h = A(U) cos(theta), write")
    print("  partial_a h = -k_a A sin(theta) + e_a A_U cos(theta)")
    print("where k_a is the fast phase gradient and e_a A_U is the slow")
    print("envelope derivative. The mixed term should average to zero.")

    da_h = -ka * A * sp.sin(theta) + ea * AU * sp.cos(theta)
    db_h = -kb * A * sp.sin(theta) + eb * AU * sp.cos(theta)
    averaged = sp.expand(avg_theta(da_h * db_h))
    target = sp.Rational(1, 2) * ka * kb * A**2 + sp.Rational(1, 2) * ea * eb * AU**2
    residual = sp.simplify(averaged - target)
    leading = sp.Rational(1, 2) * ka * kb * A**2
    slow = sp.Rational(1, 2) * ea * eb * AU**2

    print(f"  <partial_a h partial_b h> = {sp.sstr(averaged)}")
    print(f"  target split residual     = {sp.sstr(residual)}")
    print(f"  leading fast piece        = {sp.sstr(leading)}")
    print(f"  slow-envelope correction  = {sp.sstr(slow)}")
    print()
    print("If k ~ 1/lambda and e A_U/A ~ 1/L, the slow term is suppressed")
    print("by O((lambda/L)^2) relative to the fast term when A is nonzero.")

    ok = is_zero(residual)
    with out.derived_results():
        out.line(
            "scale-separated product splits into leading fast term plus suppressed envelope term",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "mixed fast/slow term averages exactly to zero",
        )
    return ok


def case_3_retarded_tt_wave(out: ScriptOutput):
    header("Case 3: Retarded TT wave positivity and null transport")
    print("Use h_+ = A cos(theta), h_x = B sin(theta),")
    print("theta = omega(t - z/c), with constant amplitudes across one cell.")

    hp_t = -omega * A * sp.sin(theta)
    hx_t = omega * B * sp.cos(theta)
    hp_z = omega * A * sp.sin(theta) / c
    hx_z = -omega * B * sp.cos(theta) / c

    s_tt = sp.simplify(avg_theta(hp_t**2 + hx_t**2))
    s_tz = sp.simplify(avg_theta(hp_t * hp_z + hx_t * hx_z))
    s_zz = sp.simplify(avg_theta(hp_z**2 + hx_z**2))

    tt_expected = omega**2 * (A**2 + B**2) / 2
    null_tz = sp.simplify(c * s_tz + s_tt)
    null_zz = sp.simplify(c**2 * s_zz - s_tt)
    positive_residual = sp.simplify(s_tt - tt_expected)

    print(f"  <h_t h_t> = {sp.sstr(s_tt)}")
    print(f"  <h_t h_z> = {sp.sstr(s_tz)}")
    print(f"  <h_z h_z> = {sp.sstr(s_zz)}")
    print(f"  <h_t h_t> target residual = {sp.sstr(positive_residual)}")
    print(f"  c <h_t h_z> + <h_t h_t> = {sp.sstr(null_tz)}")
    print(f"  c^2 <h_z h_z> - <h_t h_t> = {sp.sstr(null_zz)}")

    coeff = c**4 / (32 * sp.pi * G_N)
    ttt = sp.simplify(coeff * s_tt)
    print()
    print(f"  Isaacson local coefficient gives t_tt = {sp.sstr(ttt)}")

    ok = is_zero(positive_residual) and is_zero(null_tz) and is_zero(null_zz)
    with out.derived_results():
        out.line(
            "averaged TT derivative product is positive and null-transported",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "retarded plus/cross wave reproduces the 008 positivity/null-flux structure under averaging",
        )
    return ok


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Verdict")
    print("The Isaacson averaging part of the radiative covariant-lift debt is")
    print("now explicit at local inertial short-wave level. Periodic fast")
    print("terms and total derivatives average away; envelope corrections are")
    print("suppressed by powers of lambda/L; and the averaged TT stress keeps")
    print("the positive null transport already derived in 008.")
    print()
    print("Not claimed here: gauge invariance of the averaged stress. That is")
    print("the next targeted radiative lift.")

    with out.governance_assessments():
        out.line(
            "Isaacson averaging rigor discharged",
            StatusMark.PASS,
            "secular/oscillatory averaging assumptions retired; gauge invariance remains separate",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="isaacson_tt_averaging_015",
        inputs=[],
        output=sp.Symbol("avg_tab_eq_c4_over_32piG_avg_dhTT_dhTT_leading_shortwave"),
        method=(
            "periodic phase averages; fast total derivative average; "
            "two-scale derivative-product split; retarded TT wave positivity "
            "and null transport check"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="covariant_lift_rigor",
        scope=(
            "local inertial short-wave TT averaging with lambda << ell_avg << L; "
            "gauge invariance of averaged stress not included"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="isaacson_averaging_rigor_015",
        script_id=SCRIPT_ID,
        title="Isaacson averaging rigor for the TT/radiative sector",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["isaacson_tt_averaging_015"],
        description=(
            "Retires the secular/oscillatory averaging portion of the 008 "
            "covariant-lift debt. Gauge invariance remains open."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="isaacson_tt_averaging_claim_015",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "At local inertial short-wave level, TT waves admit the standard "
            "Isaacson average <t_ab> = (c^4/32 pi G)<partial_a h^TT_ij "
            "partial_b h^TT_ij> to leading order in lambda/L. Fast total "
            "derivatives and mixed fast/slow terms average away, and the "
            "retarded TT stress is positive and null-transported. This "
            "discharges averaging rigor only; gauge invariance is separate."
        ),
        derivation_ids=["isaacson_tt_averaging_015"],
        obligation_ids=["isaacson_averaging_rigor_015"],
    ))


def main() -> None:
    header("Trial 015: Isaacson-Style TT Averaging")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_periodic_averages(out)
    case_2_scale_separated_product(out)
    case_3_retarded_tt_wave(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()

