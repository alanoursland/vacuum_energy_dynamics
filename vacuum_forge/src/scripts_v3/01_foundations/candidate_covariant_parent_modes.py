# Candidate covariant parent modes
#
# Purpose
# -------
# This script starts the transition from reduced exterior variables
# to possible full metric/geometric parent structures.
#
# Reduced variables from the exterior program:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
#   A = exp(kappa + s)
#   B = exp(kappa - s)
#   AB = exp(2*kappa)
#
# In static spherical symmetry with kappa=0:
#
#   A = exp(s)
#   B = exp(-s)
#   AB = 1
#
# Question:
#   What are kappa and s shadows of in the full metric?
#
# This script explores reduced candidates:
#
#   1. kappa as a trace/conformal/volume-like mode.
#   2. s as a trace-free or compensated temporal-radial shear mode.
#   3. the relation between reduced 2-sector modes and 3+1 trace splitting.
#   4. the danger that kappa/s are coordinate-gauge artifacts unless their
#      parent quantities are defined carefully.
#
# IMPORTANT:
# This is exploratory. It does not identify the final covariant parent.
# It only tests candidate reductions and normalization conventions.
#
# Case 2 now exercises StructureSearch to ground the claim that kappa is a
# trace-like parent mode via structural derivation (the exchange lies in
# the projection's trace kernel), not merely via a hand-substitution that
# happens to vanish. Case 2b extends this with an anisotropic perturbation
# that could fail, providing a test whose outcome is not guaranteed by
# construction.
#
# Suggested location:
#   scripts_v3/candidate_covariant_parent_modes.py

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def mat_trace(M):
    return sp.simplify(sum(M[i, i] for i in range(M.shape[0])))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
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
# Case 0: Reduced log-scale algebra recap
# =============================================================================

def case_0_reduced_log_scale_recap():
    header("Case 0: Reduced log-scale algebra recap")

    kappa, s = sp.symbols("kappa s", real=True)

    a = kappa + s
    b = kappa - s

    A = sp.exp(a)
    B = sp.exp(b)
    AB = sp.simplify(A * B)

    print(f"a = ln A = {a}")
    print(f"b = ln B = {b}")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"AB = {AB}")

    status_line("AB = exp(2*kappa)", is_zero(AB - sp.exp(2*kappa)))
    status_line("kappa=0 gives reciprocal scaling", is_zero(AB.subs(kappa, 0) - 1))


# =============================================================================
# Case 1: 2-sector trace and shear decomposition
# =============================================================================

def case_1_two_sector_trace_shear():
    header("Case 1: 2-sector trace/shear decomposition")

    a, b = sp.symbols("a b", real=True)

    # Reduced 2-vector of log metric coefficients.
    v = sp.Matrix([a, b])

    # Trace-like direction and shear-like direction in the temporal-radial
    # two-sector.
    trace_basis = sp.Matrix([1, 1])
    shear_basis = sp.Matrix([1, -1])

    kappa = sp.simplify((a + b) / 2)
    s = sp.simplify((a - b) / 2)

    v_reconstructed = sp.simplify(kappa * trace_basis + s * shear_basis)

    print(f"v = [a,b] = {v.T}")
    print(f"kappa = (a+b)/2 = {kappa}")
    print(f"s = (a-b)/2 = {s}")
    print(f"kappa*[1,1] + s*[1,-1] = {v_reconstructed.T}")

    status_line("2-sector decomposition reconstructs [a,b]", v_reconstructed == v)

    # Dot products in Euclidean mode space, only as an algebraic toy.
    dot_trace_shear = sp.simplify(trace_basis.dot(shear_basis))
    print(f"[1,1]·[1,-1] = {dot_trace_shear}")
    status_line("trace and shear basis are orthogonal in toy mode space", is_zero(dot_trace_shear))


# =============================================================================
# Case 2: 3+1 isotropic spatial reduction — structural derivation
# =============================================================================

def case_2_physical_3plus1_trace_split(ns=None):
    header("Case 2: 3+1 isotropic spatial trace split (structural)")

    q_t, q_x, q_y, q_z = sp.symbols("q_t q_x q_y q_z", real=True)
    S = sp.symbols("S", real=True)
    C = sp.symbols("C", real=True)

    # --- Primary check: StructureAnalyzer derivation ---
    #
    # The claim "kappa is the trace-like parent mode" depends on the exchange
    # lying in the trace kernel of the projection *structurally*, not merely on
    # a substitution that happens to zero out delta_kappa. The StructureAnalyzer
    # distinguishes these two readings.

    projection = ProjectionMap(
        id="physical_3plus1_log_projection",
        variables=[q_t, q_x, q_y, q_z],
        a_expr=q_t,
        b_expr=(q_x + q_y + q_z) / 3,
        description="a = q_t, b = average spatial log scale.",
    )

    exchange = SourceOperator(
        id="isotropic_time_vs_space_exchange",
        kind="exchange",
        deltas={q_t: -S, q_x: S, q_y: S, q_z: S},
        source_symbols=[S],
        description="Isotropic time-vs-space: -1 + (1+1+1)/3 = 0.",
    )

    creation = SourceOperator(
        id="symmetric_creation_31",
        kind="creation",
        deltas={q_t: C, q_x: C, q_y: C, q_z: C},
        source_symbols=[C],
        description="Symmetric creation sources the trace.",
    )

    structure = VacuumStructure(
        id="case_2_physical_31_trace_kernel",
        variables=[q_t, q_x, q_y, q_z],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="3+1 projection with isotropic exchange in trace kernel.",
    )

    analyzer = StructureAnalyzer()
    result = analyzer.analyze(structure)

    print(result.summary())

    ex = result.exchange_results[0]
    print()
    print(f"J_kappa        = {ex.J_kappa}")
    print(f"J_sigma        = {ex.J_sigma}")
    print(f"Status         = {ex.status}")
    print(f"Classification = {ex.classification}")
    print(f"Summary status = {result.summary_status.value}")

    case_2_derived = result.summary_status.value == "derived"
    status_line(
        "trace-kernel exchange is structurally derived (not tautological)",
        case_2_derived,
        detail=result.summary_status.value,
    )

    # --- Secondary check: direct sympy substitution ---
    #
    # This should agree with the analyzer. If it disagrees, that's a bug in
    # either the analyzer or the hand calculation.

    print()
    print("Secondary check (direct sympy substitution):")

    a_expr = q_t
    b_expr = (q_x + q_y + q_z) / 3

    dq = {q_t: -S, q_x: S, q_y: S, q_z: S}
    zero = {q_t: 0, q_x: 0, q_y: 0, q_z: 0}

    delta_a = sp.simplify(a_expr.subs(dq) - a_expr.subs(zero))
    delta_b = sp.simplify(b_expr.subs(dq) - b_expr.subs(zero))
    delta_kappa = sp.simplify((delta_a + delta_b) / 2)
    delta_s = sp.simplify((delta_a - delta_b) / 2)

    print(f"  delta a     = {delta_a}")
    print(f"  delta b     = {delta_b}")
    print(f"  delta kappa = {delta_kappa}")
    print(f"  delta s     = {delta_s}")

    hand_kappa_zero = is_zero(delta_kappa)
    hand_s_nonzero = not is_zero(delta_s)
    status_line("hand calc: exchange lies in kappa-kernel", hand_kappa_zero)
    status_line("hand calc: exchange excites shear s", hand_s_nonzero)

    # Cross-check: both methods should agree.
    if case_2_derived and hand_kappa_zero:
        print()
        print("  Analyzer and hand calculation agree: J_kappa = 0 structurally.")
    elif not case_2_derived and hand_kappa_zero:
        print()
        print("  DISAGREEMENT: hand calc shows delta_kappa=0 but analyzer did not")
        print("  classify as derived. Inspect analyzer behavior.")
    elif case_2_derived and not hand_kappa_zero:
        print()
        print("  DISAGREEMENT: analyzer says derived but hand calc gives delta_kappa != 0.")
        print("  This is a bug — investigate.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="kappa_trace_kernel_exchange",
            inputs=[q_t, q_x, q_y, q_z, S],
            output=sp.Eq(ex.J_kappa, 0),
            method="structure_search_trace_kernel",
            status=Status.DERIVED if case_2_derived else Status.CANDIDATE,
            metadata={
                "classification": ex.classification,
                "summary_status": result.summary_status.value,
            },
        )

    return case_2_derived


# =============================================================================
# Case 2b: Anisotropic perturbation — extension test that could fail
# =============================================================================

def case_2b_anisotropic_perturbation(ns=None):
    header("Case 2b: Anisotropic spatial exchange — extension test")

    # This tests whether the trace-kernel structure depends on spatial isotropy
    # or only on the trace condition itself.
    #
    # Anisotropic exchange: (-S, 2S, S/2, S/2)
    # Trace-kernel sum: -1 + (2 + 1/2 + 1/2)/3 = -1 + 1 = 0
    #
    # If the analyzer classifies this as "derived" with J_kappa = 0, the
    # trace-kernel interpretation is robust against isotropy breaking.
    # If it classifies differently, the original Case 2's vanishing was partly
    # an artifact of the isotropic substitution.

    q_t, q_x, q_y, q_z = sp.symbols("q_t q_x q_y q_z", real=True)
    S = sp.symbols("S", real=True)
    C = sp.symbols("C", real=True)

    projection = ProjectionMap(
        id="physical_3plus1_log_projection_aniso",
        variables=[q_t, q_x, q_y, q_z],
        a_expr=q_t,
        b_expr=(q_x + q_y + q_z) / 3,
        description="a = q_t, b = average spatial log scale.",
    )

    exchange = SourceOperator(
        id="anisotropic_time_vs_space_exchange",
        kind="exchange",
        deltas={q_t: -S, q_x: 2*S, q_y: S/2, q_z: S/2},
        source_symbols=[S],
        description="Anisotropic: -1 + (2 + 1/2 + 1/2)/3 = 0.",
    )

    creation = SourceOperator(
        id="symmetric_creation_31_aniso",
        kind="creation",
        deltas={q_t: C, q_x: C, q_y: C, q_z: C},
        source_symbols=[C],
        description="Symmetric creation sources the trace.",
    )

    structure = VacuumStructure(
        id="case_2b_anisotropic_trace_kernel",
        variables=[q_t, q_x, q_y, q_z],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="3+1 projection with anisotropic exchange in trace kernel.",
    )

    analyzer = StructureAnalyzer()
    result = analyzer.analyze(structure)

    print(result.summary())

    ex = result.exchange_results[0]
    print()
    print(f"J_kappa        = {ex.J_kappa}")
    print(f"J_sigma        = {ex.J_sigma}")
    print(f"Status         = {ex.status}")
    print(f"Classification = {ex.classification}")
    print(f"Summary status = {result.summary_status.value}")

    case_2b_derived = result.summary_status.value == "derived"

    if case_2b_derived:
        status_line(
            "anisotropic exchange also structurally derived",
            True,
            detail="trace-kernel interpretation does not depend on isotropy",
        )
    else:
        status_line(
            "anisotropic exchange NOT classified as derived",
            False,
            detail=(
                f"got '{result.summary_status.value}'; "
                "original Case 2 vanishing may depend on isotropy"
            ),
        )

    # Secondary hand-calc cross-check.
    print()
    print("Secondary check (direct sympy substitution):")

    a_expr = q_t
    b_expr = (q_x + q_y + q_z) / 3

    dq = {q_t: -S, q_x: 2*S, q_y: S/2, q_z: S/2}
    zero = {q_t: 0, q_x: 0, q_y: 0, q_z: 0}

    delta_a = sp.simplify(a_expr.subs(dq) - a_expr.subs(zero))
    delta_b = sp.simplify(b_expr.subs(dq) - b_expr.subs(zero))
    delta_kappa = sp.simplify((delta_a + delta_b) / 2)
    delta_s = sp.simplify((delta_a - delta_b) / 2)

    print(f"  delta a     = {delta_a}")
    print(f"  delta b     = {delta_b}")
    print(f"  delta kappa = {delta_kappa}")
    print(f"  delta s     = {delta_s}")

    hand_kappa_zero = is_zero(delta_kappa)
    status_line("hand calc: anisotropic exchange in kappa-kernel", hand_kappa_zero)

    if case_2b_derived and not hand_kappa_zero:
        print("  DISAGREEMENT: analyzer says derived but hand calc gives delta_kappa != 0.")
    elif not case_2b_derived and hand_kappa_zero:
        print("  DISAGREEMENT: hand calc shows delta_kappa=0 but analyzer did not derive.")

    if ns is not None:
        ns.record_derivation(
            derivation_id="anisotropic_kappa_trace_kernel_exchange",
            inputs=[q_t, q_x, q_y, q_z, S],
            output=sp.Eq(ex.J_kappa, 0),
            method="structure_search_trace_kernel",
            status=Status.DERIVED if case_2b_derived else Status.CANDIDATE,
            metadata={
                "classification": ex.classification,
                "summary_status": result.summary_status.value,
            },
        )

    return case_2b_derived


# =============================================================================
# Case 3: Linearized metric perturbation trace comparison
# =============================================================================

def case_3_linearized_trace_comparison():
    header("Case 3: Linearized metric perturbation trace comparison")

    # This case compares the reduced log modes with a simple linearized metric
    # perturbation around Minkowski.
    #
    # Use signature (-,+,+,+).
    #
    # Toy diagonal metric:
    #   g_tt = -exp(a)
    #   g_rr =  exp(b)
    #
    # In weak field:
    #   h_tt ~ -(A-1)
    #   h_rr ~  B-1
    #
    # Reduced log modes are cleaner than raw h components, but the linear trace
    # hints at parent trace/shear structure.

    a, b = sp.symbols("a b", real=True)
    eps = sp.symbols("eps", real=True)

    # Substitute a=eps*a1, b=eps*b1 for first-order expansion.
    a1, b1 = sp.symbols("a1 b1", real=True)
    A = sp.exp(eps * a1)
    B = sp.exp(eps * b1)

    # Linear perturbations in diagonal tt and rr components.
    # g_tt = -A = -1 + h_tt => h_tt = -(A-1)
    # g_rr = B = 1 + h_rr => h_rr = B-1
    h_tt = sp.series(-(A - 1), eps, 0, 2).removeO()
    h_rr = sp.series(B - 1, eps, 0, 2).removeO()

    # Minkowski inverse trace contribution for tt and rr:
    # h = eta^{tt} h_tt + eta^{rr} h_rr = -h_tt + h_rr
    trace_2 = sp.simplify(-h_tt + h_rr)

    kappa_linear = sp.simplify((eps*a1 + eps*b1) / 2)
    s_linear = sp.simplify((eps*a1 - eps*b1) / 2)

    print(f"A = exp(eps*a1), B = exp(eps*b1)")
    print(f"h_tt first order = {h_tt}")
    print(f"h_rr first order = {h_rr}")
    print(f"2-sector Minkowski trace contribution -h_tt+h_rr = {trace_2}")
    print(f"kappa linear = {kappa_linear}")
    print(f"s linear = {s_linear}")

    # trace_2 = eps*(a1+b1) = 2*kappa_linear
    status_line("linearized 2-sector trace is 2*kappa", is_zero(trace_2 - 2*kappa_linear))

    print()
    print("Interpretation:")
    print("  In this reduced diagonal sector, kappa matches half of the")
    print("  linearized temporal-radial trace contribution.")
    print("  This supports kappa as a trace/conformal-like parent candidate,")
    print("  but it is not yet a covariant definition.")


# =============================================================================
# Case 4: Trace-free shear in the reduced 2-sector
# =============================================================================

def case_4_trace_free_shear_linearized():
    header("Case 4: Trace-free shear in reduced linearized sector")

    eps, s = sp.symbols("eps s", real=True)

    # Pure shear/compensated mode:
    #   kappa = 0
    #   a = s
    #   b = -s
    a = eps * s
    b = -eps * s

    A = sp.exp(a)
    B = sp.exp(b)

    h_tt = sp.series(-(A - 1), eps, 0, 2).removeO()
    h_rr = sp.series(B - 1, eps, 0, 2).removeO()
    trace_2 = sp.simplify(-h_tt + h_rr)

    print("Pure reduced shear:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  A = {A}")
    print(f"  B = {B}")
    print(f"  h_tt first order = {h_tt}")
    print(f"  h_rr first order = {h_rr}")
    print(f"  reduced trace contribution = {trace_2}")

    status_line("pure reduced shear is trace-free to first order", is_zero(trace_2))


# =============================================================================
# Case 5: Determinant / volume caution
# =============================================================================

def case_5_determinant_volume_caution():
    header("Case 5: Determinant / volume caution")

    a, b, r, theta = sp.symbols("a b r theta", real=True, positive=True)

    # Static spherical metric in areal radius:
    #   ds² = -A dt² + B dr² + r² dΩ²
    # determinant magnitude:
    #   |g| = A B r^4 sin²θ
    # sqrt(|g|) = sqrt(A B) r² sinθ = exp(kappa) r² sinθ
    A = sp.exp(a)
    B = sp.exp(b)
    sqrt_abs_g = sp.sqrt(A * B) * r**2 * sp.sin(theta)

    kappa = sp.simplify((a + b) / 2)
    sqrt_abs_g_k = sp.simplify(sp.exp(kappa) * r**2 * sp.sin(theta))

    print("Areal-radius static spherical determinant:")
    print(f"  sqrt(|g|) = {sqrt_abs_g}")
    print(f"  exp(kappa) r² sin(theta) = {sqrt_abs_g_k}")

    status_line("sqrt(|g|) temporal-radial factor is exp(kappa)", is_zero(sqrt_abs_g - sqrt_abs_g_k))

    print()
    print("Caution:")
    print("  In areal-radius coordinates, the angular sector is fixed as r²dΩ².")
    print("  Therefore kappa controls the temporal-radial determinant factor,")
    print("  not a fully coordinate-independent volume mode by itself.")
    print("  A covariant parent must handle gauge/coordinate dependence carefully.")


# =============================================================================
# Case 6: Candidate parent classification
# =============================================================================

def case_6_candidate_parent_classification():
    header("Case 6: Candidate parent classification")

    print("Candidate parent interpretation:")
    print()
    print("  kappa:")
    print("    reduced trace / conformal / determinant-like mode")
    print("    controls AB = exp(2*kappa)")
    print("    equals half the temporal-radial linearized trace contribution")
    print("    controls sqrt(|g|)'s temporal-radial factor in areal gauge")
    print()
    print("  s:")
    print("    reduced trace-free temporal-radial shear mode")
    print("    preserves AB when kappa=0")
    print("    carries compensated exterior distortion")
    print()
    print("Main caution:")
    print("  These are reduced static spherical sector variables.")
    print("  They are not yet covariant fields.")
    print("  A full theory must identify gauge-aware or covariant parent structures.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(case_2_ok: bool, case_2b_ok: bool):
    header("Final interpretation")

    print("This exploratory script supports the following working hypothesis:")
    print()
    print("  kappa is the reduced trace/conformal/determinant-like mode")
    print("  of the temporal-radial exterior sector.")
    print()
    print("  s is the reduced trace-free/shear mode that remains when")
    print("  the source-free exterior suppresses kappa.")
    print()
    print("In the reduced sector:")
    print("  kappa = 0 -> AB = 1")
    print("  s != 0 carries compensated exterior distortion")
    print()

    if case_2_ok and case_2b_ok:
        print("Structural grounding (Cases 2 and 2b both derived):")
        print("  The trace-like classification of kappa is grounded structurally")
        print("  in the projection kernel via StructureAnalyzer derivation, not")
        print("  merely in a substitution that happens to vanish.")
        print("  The anisotropic perturbation (Case 2b) confirms the trace-kernel")
        print("  structure does not depend on spatial isotropy.")
    elif case_2_ok and not case_2b_ok:
        print("Partial structural grounding (Case 2 derived, Case 2b did not):")
        print("  The isotropic exchange is structurally derived, but the anisotropic")
        print("  perturbation was not classified as derived. This means the")
        print("  trace-kernel interpretation may depend on isotropy or the analyzer")
        print("  handles anisotropic operators differently. This discrepancy must")
        print("  be resolved before the strengthened claim can be made.")
    else:
        print("Structural grounding NOT confirmed:")
        print("  The StructureAnalyzer did not classify the isotropic exchange as")
        print("  structurally derived. The trace-like interpretation of kappa rests")
        print("  only on the algebraic substitution, not on structural derivation.")
        print("  Investigate why the analyzer disagrees before proceeding.")

    print()
    print("Caveat (unchanged):")
    print("  kappa and s are not yet covariant objects.")
    print("  They are reduced variables extracted in a static spherical setting.")
    print()
    print("Next theoretical target:")
    print("  Find a gauge-aware or covariant decomposition of metric variations")
    print("  whose static spherical reduction gives kappa and s.")
    print()
    print("Possible next artifact:")
    print("  candidate_covariant_parent_modes.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Covariant Parent Modes")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_reduced_log_scale_recap()
    case_1_two_sector_trace_shear()
    case_2_ok = case_2_physical_3plus1_trace_split(ns)
    case_2b_ok = case_2b_anisotropic_perturbation(ns)
    case_3_linearized_trace_comparison()
    case_4_trace_free_shear_linearized()
    case_5_determinant_volume_caution()
    case_6_candidate_parent_classification()
    final_interpretation(case_2_ok, case_2b_ok)
    ns.write_run_metadata(case_2_ok=case_2_ok, case_2b_ok=case_2b_ok)


if __name__ == "__main__":
    main()
