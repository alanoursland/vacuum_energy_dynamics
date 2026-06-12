# Trial C3: spatial-sector bootstrap -- what P7 actually is
#
# Group:
#   002_trial_C_burden_ledger
#
# Script type:
#   DERIVATION / EQUIVALENCE THEOREMS / PLACEMENT RESOLUTION
#
# Purpose
# -------
# Trial C2 + P9 left one recovery postulate standing: P7 (AB = 1 in the
# static source-free exterior). This script asks whether the bootstrap
# principle forces it.
#
# Honest answer found: P9 alone does NOT force P7. Instead, conditional on
# the probe's gates (second-order, divergence-free, D = 4 response =
# Einstein tensor up to Lambda; gates G15/G16/G20, the conditional GR
# branch), three statements are EQUIVALENT:
#
#   (i)   AB = const in the static spherical exterior          (P7)
#   (ii)  the effective source stress satisfies T^t_t = T^r_r
#         (radial-boost invariance of the t-r block)
#   (iii) configuration energy is counted INSIDE the nonlinear
#         geometric response (geometry-side placement), not as an
#         explicit scalar-field-like source
#
# and the explicit-source placement is RULED OUT: a static scalar-type
# configuration source has T^t_t - T^r_r = -(phi')^2/B != 0, which breaks
# AB = 1 wherever the field has a gradient -- contradicting P7.
#
# So C3 resolves the count-once placement question P9's fence left open,
# and upgrades P7 from arbitrary recovery postulate to a placement
# selector with an ontological restatement candidate:
#
#   P7' (candidate): static vacuum configurations carry no energy
#   current and no preferred frame in the t-r plane (radial-boost
#   invariance). AB = 1 is its metric shadow.
#
# Conditionality is explicit throughout: the Einstein tensor is used as
# the unique conditional response under the probe's gates, not as an
# import of GR-as-truth (no recovery-as-construction: P7 is never
# inserted; it EMERGES from (ii)/(iii) and is CONTRASTED with (explicit
# source) which kills it).

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
    RouteRecord,
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
        dependency_id="c2_bootstrap_family_dependency_c3",
        upstream_script_id="002_trial_C_burden_ledger__trial_C2_self_coupling_bootstrap",
        upstream_derivation_id="bootstrap_family_exact_solution_c2",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


# =============================================================================
# Curvature machinery (hand-rolled, diagonal static spherical metric)
# =============================================================================

t, r, th, ph = sp.symbols("t r theta phi")
A = sp.Function("A")(r)
B = sp.Function("B")(r)
COORDS = [t, r, th, ph]


def metric(Afun, Bfun):
    return sp.diag(-Afun, Bfun, r**2, r**2 * sp.sin(th) ** 2)


def christoffel(g):
    ginv = g.inv()
    n = 4
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s_ = 0
                for d in range(n):
                    s_ += ginv[a, d] * (sp.diff(g[d, b], COORDS[c])
                                        + sp.diff(g[d, c], COORDS[b])
                                        - sp.diff(g[b, c], COORDS[d]))
                Gamma[a][b][c] = sp.simplify(s_ / 2)
    return Gamma


def ricci(Gamma):
    n = 4
    R = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c in range(n):
                expr += sp.diff(Gamma[c][a][b], COORDS[c])
                expr -= sp.diff(Gamma[c][a][c], COORDS[b])
                for d in range(n):
                    expr += Gamma[c][c][d] * Gamma[d][a][b]
                    expr -= Gamma[c][a][d] * Gamma[d][c][b]
            R[a, b] = sp.simplify(expr)
    return R


def einstein_mixed(g):
    Gamma = christoffel(g)
    Ric = ricci(Gamma)
    ginv = g.inv()
    Rs = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(4) for j in range(4)))
    G_mixed = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            G_ab = Ric[a, b] - sp.Rational(1, 2) * g[a, b] * Rs
            # mixed component G^a_b = g^{ac} G_cb
            G_mixed[a, b] = sp.simplify(sum(ginv[a, c] * (Ric[c, b] - sp.Rational(1, 2) * g[c, b] * Rs)
                                            for c in range(4)))
    return G_mixed


# =============================================================================
# Case 0
# =============================================================================


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Does the bootstrap force P7?")
    print("After C2 + P9, P7 (AB = 1 static source-free exterior) is the last")
    print("recovery postulate. Question: does requiring configuration energy")
    print("to gravitate universally (P9) force the reciprocal spatial response?")
    print()
    print("Conditional apparatus, stated openly: the probe's gates G15/G16/G20")
    print("(second-order, divergence-free, D=4) make the Einstein tensor the")
    print("unique geometric response of the conditional branch. We use G^a_b")
    print("in that conditional role only -- never as an import of GR-as-truth,")
    print("and P7 is never inserted as a target.")

    with out.governance_assessments():
        out.line("Trial C3 opened", StatusMark.INFO,
                 "spatial-sector bootstrap; equivalence-theorem strategy; conditionality explicit")


# =============================================================================
# Case 1: the t-r block identity
# =============================================================================


def case_1_tr_identity(out: ScriptOutput):
    header("Case 1: G^t_t - G^r_r is proportional to (ln AB)'")
    g = metric(A, B)
    G = einstein_mixed(g)
    diff_tr = sp.simplify(G[0, 0] - G[1, 1])
    target = -(sp.diff(A, r) / A + sp.diff(B, r) / B) / (r * B)
    residual = sp.simplify(diff_tr - target)
    print(f"  G^t_t - G^r_r = {sp.sstr(diff_tr)}")
    print(f"  target  -(lnAB)'/(rB) = {sp.sstr(target)}")
    print(f"  residual = {sp.sstr(residual)}")
    print()
    print("  THEOREM C3-1 (conditional): with a divergence-free second-order")
    print("  response, T^t_t = T^r_r  <=>  (AB)' = 0  <=>  P7.")
    print("  P7 is exactly the statement that the effective source stress is")
    print("  invariant under boosts in the t-r plane (no radial energy current,")
    print("  no preferred radial frame).")

    with out.derived_results():
        out.line("G^t_t - G^r_r = -(ln AB)'/(r B)",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 "P7 <=> radial-boost invariance of the effective stress (conditional theorem)")
    return diff_tr


# =============================================================================
# Case 2: explicit-source placement is ruled out
# =============================================================================


def case_2_explicit_source(out: ScriptOutput):
    header("Case 2: Explicit scalar-type configuration source breaks P7")
    phi = sp.Function("phi")(r)
    g = metric(A, B)
    ginv = g.inv()
    # T_ab = d_a phi d_b phi - (1/2) g_ab (d phi)^2 ; static radial phi
    dphi = [0, sp.diff(phi, r), 0, 0]
    grad_sq = sp.simplify(sum(ginv[i, j] * dphi[i] * dphi[j] for i in range(4) for j in range(4)))
    T = sp.zeros(4, 4)
    for a_ in range(4):
        for b_ in range(4):
            T[a_, b_] = dphi[a_] * dphi[b_] - sp.Rational(1, 2) * g[a_, b_] * grad_sq
    T_mixed_tt = sp.simplify(sum(ginv[0, c] * T[c, 0] for c in range(4)))
    T_mixed_rr = sp.simplify(sum(ginv[1, c] * T[c, 1] for c in range(4)))
    diff_T = sp.simplify(T_mixed_tt - T_mixed_rr)
    expected = -sp.diff(phi, r) ** 2 / B
    residual = sp.simplify(diff_T - expected)

    print(f"  T^t_t - T^r_r = {sp.sstr(diff_T)}   (expected -(phi')^2/B)")
    print(f"  residual = {sp.sstr(residual)}")
    print()
    print("  THEOREM C3-2: a static, radial, scalar-field-type stress is NOT")
    print("  radial-boost invariant: T^t_t - T^r_r = -(phi')^2/B < 0 wherever")
    print("  the field has a gradient. By C3-1, sourcing the response with an")
    print("  EXPLICIT configuration-energy field of this type forces AB != 1")
    print("  in the exterior -- contradicting P7.")
    print()
    print("  Consequence: P9's count-once placement question is ANSWERED by P7.")
    print("  Configuration energy must be counted INSIDE the nonlinear response")
    print("  (the C2 pattern: self-coupling as the nonlinearity that linearizes")
    print("  in A), not as an explicit external scalar source. The framework's")
    print("  exact branch already uses the only placement P7 allows.")

    with out.derived_results():
        out.line("scalar-type stress violates radial-boost invariance",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 "T^t_t - T^r_r = -(phi')^2/B != 0")
    with out.counterexamples():
        out.line("explicit-source placement of configuration energy",
                 StatusMark.FAIL,
                 "breaks AB = 1 wherever the field has a gradient; contradicts P7 (kill by C3-1 + C3-2)")
    return diff_T


# =============================================================================
# Case 3: the C2 family meets the spatial sector
# =============================================================================


def case_3_family_consistency(out: ScriptOutput):
    header("Case 3: Conditional vacuum equations re-select lamda = -1")
    print("Under geometry-side placement, the conditional exterior equations are")
    print("G^a_b = 0. Take the C2 family A_lamda = (1 + lamda r_s/r)^(-1/lamda)")
    print("with the compensated ansatz B = 1/A (P7 form), and ask which family")
    print("members actually solve the conditional vacuum equations:")
    print()

    r_s = sp.Symbol("r_s", positive=True)
    results = []
    for lam_val, name in [(-1, "lamda = -1 (Schwarzschild)"),
                          (sp.Rational(1, 1), "lamda = +1 (reciprocal)")]:
        if lam_val == -1:
            A_l = 1 - r_s / r
        else:
            A_l = 1 / (1 + r_s / r)
        g = metric(A_l, 1 / A_l)
        G = einstein_mixed(g)
        Gtt = sp.simplify(G[0, 0])
        results.append((name, Gtt))
        print(f"  {name}:  G^t_t = {sp.sstr(Gtt)}")

    # exponential member lamda -> 0
    A_e = sp.exp(-r_s / r)
    g = metric(A_e, 1 / A_e)
    G = einstein_mixed(g)
    Gtt_exp = sp.simplify(G[0, 0])
    print(f"  lamda -> 0 (exponential):  G^t_t = {sp.sstr(Gtt_exp)}")
    print()
    print("  Only lamda = -1 solves the conditional vacuum equations. The")
    print("  temporal bootstrap selector (C2) and the spatial conditional")
    print("  response select the SAME member independently -- the consistency")
    print("  loop closes.")

    ok_m1 = is_zero(results[0][1])
    ok_p1_nonzero = not is_zero(results[1][1])
    ok_exp_nonzero = not is_zero(Gtt_exp)

    with out.derived_results():
        out.line("lamda = -1 solves conditional vacuum equations",
                 StatusMark.PASS if ok_m1 else StatusMark.FAIL,
                 "G^a_b = 0 exactly for Schwarzschild with B = 1/A")
        out.line("lamda = +1 and exponential members fail the spatial sector",
                 StatusMark.PASS if (ok_p1_nonzero and ok_exp_nonzero) else StatusMark.FAIL,
                 "independent re-selection of the C2 winner by the conditional response")


# =============================================================================
# Case 4: verdict
# =============================================================================


def case_4_verdict(out: ScriptOutput) -> None:
    header("Case 4: Trial C3 verdict")
    print("ANSWER to the locked-door question: P9 alone does NOT force P7.")
    print("What was derived instead (conditional on gates G15/G16/G20):")
    print()
    print("  EQUIVALENCE (C3-1):   P7  <=>  T^t_t = T^r_r  <=>  no radial")
    print("    energy current / no preferred frame in the t-r plane.")
    print("  EXCLUSION  (C3-2):    explicit-source placement of configuration")
    print("    energy is killed: scalar-type stress is not radial-boost")
    print("    invariant, so it breaks P7. Geometry-side placement is the only")
    print("    survivor: P9's count-once placement question is RESOLVED.")
    print("  CONSISTENCY (C3-3):   the conditional vacuum equations re-select")
    print("    the C2 winner lamda = -1 independently.")
    print()
    print("STATUS SHIFT for P7: from arbitrary recovery postulate to a")
    print("placement selector with an ontological restatement candidate:")
    print()
    print("  P7' (candidate, for theory-owner review):")
    print("    'Static vacuum configurations carry no energy current and no")
    print("     preferred frame in the t-r plane.'")
    print("  AB = 1 is then P7''s metric shadow, and P7' + P9 + the conditional")
    print("  gates yield the full static exterior recovery with no remaining")
    print("  recovery-shaped postulates.")
    print()
    print("NOT DERIVED: P7' itself from P1-P6 (it is a new candidate ontology")
    print("statement, like P9 was); the radiative-sector positivity (G03);")
    print("the unconditional (gate-free) versions of all three theorems.")

    with out.governance_assessments():
        out.line("Trial C3 verdict: P7 not forced, but transformed",
                 StatusMark.PASS,
                 "equivalence + exclusion + consistency; placement question resolved; P7' candidate named")
    with out.unresolved_obligations():
        out.line("P7' adoption decision (theory owner): no preferred t-r frame for static vacuum",
                 StatusMark.OBLIGATION,
                 "would retire the last recovery-shaped postulate in favor of an ontology statement")
        out.line("derive P7' or P7 from P1-P6 + P9, or record as primitive",
                 StatusMark.OBLIGATION,
                 "the bootstrap program's remaining static-sector gap")


# =============================================================================
# Archive recording
# =============================================================================


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="tr_block_identity_c3",
        inputs=[],
        output=sp.Symbol("Gtt_minus_Grr_eq_minus_lnAB_prime_over_rB"),
        method="full Einstein tensor for diag(-A, B, r^2, r^2 sin^2) computed from scratch",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="equivalence_theorem",
        scope="conditional on G15/G16/G20: P7 <=> T^t_t = T^r_r (radial-boost invariance)",
    )
    ns.record_derivation(
        derivation_id="scalar_stress_violates_boost_invariance_c3",
        inputs=[],
        output=sp.Symbol("Ttt_minus_Trr_eq_minus_phiprime_sq_over_B"),
        method="stress of static radial scalar field, mixed components",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="exclusion_theorem",
        scope="explicit-source placement of configuration energy breaks P7; geometry-side placement forced",
    )
    ns.record_derivation(
        derivation_id="family_spatial_reselection_c3",
        inputs=[],
        output=sp.Symbol("only_lamda_minus_one_solves_vacuum"),
        method="G^t_t evaluated for C2 family members with B = 1/A",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="consistency_check",
        scope="conditional vacuum equations independently re-select lamda = -1",
    )

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="kill_explicit_source_placement_c3",
        script_id=SCRIPT_ID,
        branch_id="configuration_energy_as_explicit_scalar_source",
        status=GovernanceStatus.FAILED_BY_WITNESS,
        tier=ClaimTier.EXCLUSION,
        obligation_ids=[],
        description=(
            "Counting configuration energy as an explicit static scalar-type source "
            "is killed: its stress satisfies T^t_t - T^r_r = -(phi')^2/B != 0, which "
            "by the t-r block identity forces AB != 1, contradicting P7. The "
            "geometry-side (nonlinear-response) placement is the unique survivor; "
            "P9's count-once placement question is resolved."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="p7_prime_adoption_c3",
        script_id=SCRIPT_ID,
        title="Theory-owner decision: adopt P7' (no preferred t-r frame for static vacuum)",
        status=ObligationStatus.OPEN,
        required_by=["trial_C_verdict"],
        description=(
            "P7' restates P7 ontologically: static vacuum configurations carry no "
            "energy current and no preferred frame in the t-r plane; AB = 1 is its "
            "metric shadow. Adoption would retire the last recovery-shaped postulate."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="trial_C4_p7_prime_route_c3",
        script_id=SCRIPT_ID,
        name="Trial C4: derive or adopt P7' (static t-r frame indifference)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["p7_prime_adoption_c3"],
        activation_conditions=[
            "C3 equivalences carried as conditional theorems (gates G15/G16/G20)",
            "geometry-side placement of configuration energy is settled (C3-2)",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="spatial_bootstrap_resolution_c3",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Conditional on the probe's gates: P7 is equivalent to radial-boost "
            "invariance of the effective stress (no static energy current in the "
            "t-r plane), explicit-source placement of configuration energy is "
            "excluded (scalar-type stress breaks the invariance), geometry-side "
            "counting is forced -- resolving P9's placement question -- and the "
            "conditional vacuum equations independently re-select the C2 bootstrap "
            "winner lamda = -1. P9 alone does not force P7; P7' (static t-r frame "
            "indifference) is the candidate ontological replacement."
        ),
        derivation_ids=[
            "tr_block_identity_c3",
            "scalar_stress_violates_boost_invariance_c3",
            "family_spatial_reselection_c3",
        ],
        obligation_ids=["p7_prime_adoption_c3"],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Trial C3: Spatial-Sector Bootstrap -- What P7 Actually Is")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_problem(out)
    case_1_tr_identity(out)
    case_2_explicit_source(out)
    case_3_family_consistency(out)
    case_4_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
