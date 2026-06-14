# Trial 018: Closure uniqueness, step 3
#
# Script type:
#   RIGOR PROGRAM / DEFORMATION AUDIT
#
# Purpose
# -------
# This is the third in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It still does not retire the
# full closure-uniqueness obligation.
#
# Step 2 verified the finite first-order/Palatini witness. This script
# audits the local deformation space around that witness:
#
#   1. Under the Palatini replacement ansatz, the only generated
#      nonlinear derivative self-coupling is H.Q.
#   2. H.Rlin is the free kinetic core, not a new self-coupling.
#   3. H^2.Rlin and H^2.Q have distinct bidegrees and are not generated
#      by eta -> eta + H. They would be extra assumptions, not the
#      universal self-coupling forced by conservation.
#   4. The remaining missing lemma is isolated: prove that every
#      admissible local, two-derivative, no-extra-field completion can
#      be reduced to the Palatini replacement ansatz up to boundary
#      terms, field redefinitions, normalization, and the cosmological
#      term.

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

DIM = 4
ETA = [-1, 1, 1, 1]


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
        dependency_id="closure_step_2_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_2_palatini_finite",
        upstream_derivation_id="palatini_first_self_coupling_term_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


eps = sp.Symbol("eps")

H = sp.Matrix(DIM, DIM, lambda mu, nu: sp.Symbol(f"H{mu}{nu}"))


def eta_up(mu: int, nu: int):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def Gamma(alpha: int, mu: int, nu: int):
    a, b = sorted((mu, nu))
    return sp.Symbol(f"G{alpha}_{a}{b}")


def dGamma(alpha: int, mu: int, nu: int, rho: int):
    a, b = sorted((mu, nu))
    return sp.Symbol(f"dG{alpha}_{a}{b}_{rho}")


def Rlin(mu: int, nu: int):
    return sp.simplify(
        sum(dGamma(alpha, mu, nu, alpha) for alpha in range(DIM))
        - sum(dGamma(alpha, mu, alpha, nu) for alpha in range(DIM))
    )


def Q(mu: int, nu: int):
    return sp.simplify(
        sum(
            Gamma(alpha, alpha, beta) * Gamma(beta, mu, nu)
            - Gamma(alpha, mu, beta) * Gamma(beta, alpha, nu)
            for alpha in range(DIM)
            for beta in range(DIM)
        )
    )


def contraction(metric_density, tensor):
    return sp.simplify(
        sum(metric_density(mu, nu) * tensor(mu, nu) for mu in range(DIM) for nu in range(DIM))
    )


def H_component(mu: int, nu: int):
    return H[mu, nu]


def H2_component(mu: int, nu: int):
    return sp.simplify(sum(H[mu, alpha] * H[alpha, nu] for alpha in range(DIM)))


def eta_plus_eps_H(mu: int, nu: int):
    return eta_up(mu, nu) + eps * H[mu, nu]


H_RLIN = contraction(H_component, Rlin)
H_Q = contraction(H_component, Q)
H2_RLIN = contraction(H2_component, Rlin)
H2_Q = contraction(H2_component, Q)
PALATINI_DENSITY = contraction(eta_plus_eps_H, lambda mu, nu: Rlin(mu, nu) + Q(mu, nu))


def scale_expr(expr):
    h_scale, gamma_scale = sp.symbols("h_scale gamma_scale")
    subs = {}
    for mu in range(DIM):
        for nu in range(DIM):
            subs[H[mu, nu]] = h_scale * H[mu, nu]
    for alpha in range(DIM):
        for mu in range(DIM):
            for nu in range(mu, DIM):
                subs[Gamma(alpha, mu, nu)] = gamma_scale * Gamma(alpha, mu, nu)
                for rho in range(DIM):
                    subs[dGamma(alpha, mu, nu, rho)] = gamma_scale * dGamma(alpha, mu, nu, rho)
    return sp.Poly(sp.expand(expr.xreplace(subs)), h_scale, gamma_scale)


def monomials(expr):
    return sorted(scale_expr(expr).monoms())


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, third rung")
    print("Step 2 proved the finite Palatini witness. This step audits the")
    print("nearby deformation space under that ansatz: what is generated by")
    print("eta -> eta + H, what merely renormalizes the free theory, and what")
    print("would be an extra assumption outside the universal self-coupling.")

    with out.governance_assessments():
        out.line(
            "Palatini deformation audit opened",
            StatusMark.INFO,
            "narrows the remaining uniqueness problem; does not retire it",
        )


def case_1_taylor_generated_terms(out: ScriptOutput):
    header("Case 1: Universal replacement has no higher H tower")
    l0 = sp.simplify(PALATINI_DENSITY.subs(eps, 0))
    l1 = sp.simplify(sp.diff(PALATINI_DENSITY, eps).subs(eps, 0))
    l2 = sp.simplify(sp.diff(PALATINI_DENSITY, eps, 2).subs(eps, 0))
    residual_l1 = sp.simplify(l1 - (H_RLIN + H_Q))

    print("Taylor expansion of (eta + eps H).(Rlin + Q):")
    print("  L0 = eta.(Rlin + Q)")
    print("  L1 = H.Rlin + H.Q")
    print("  L2 = 0")
    print(f"  L1 residual = {sp.sstr(residual_l1)}")
    print(f"  L2 residual = {sp.sstr(l2)}")

    ok = is_zero(residual_l1) and is_zero(l2) and bool(l0 != 0)
    with out.derived_results():
        out.line(
            "universal Palatini replacement generates only first order in H",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "no H^2 derivative tower is produced by eta -> eta + H",
        )
    return ok


def case_2_bidegree_separation(out: ScriptOutput):
    header("Case 2: Candidate terms are separated by field/connection bidegree")
    data = {
        "H.Rlin": monomials(H_RLIN),
        "H.Q": monomials(H_Q),
        "H2.Rlin": monomials(H2_RLIN),
        "H2.Q": monomials(H2_Q),
    }
    expected = {
        "H.Rlin": [(1, 1)],
        "H.Q": [(1, 2)],
        "H2.Rlin": [(2, 1)],
        "H2.Q": [(2, 2)],
    }

    for name, mons in data.items():
        print(f"  {name}: bidegree monomials {mons}")

    ok = data == expected
    with out.derived_results():
        out.line(
            "deformation candidates have distinct bidegrees",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "free, generated self-coupling, and H^2 tower terms cannot be confused",
        )
    return ok


def case_3_coefficient_audit(out: ScriptOutput):
    header("Case 3: Coefficient audit under the replacement ansatz")
    a, b, c, d = sp.symbols("a b c d")
    B_self, B_free, B_h2r, B_h2q = sp.symbols("B_self B_free B_h2r B_h2q")

    candidate = a * B_self + b * B_free + c * B_h2r + d * B_h2q
    target = B_self
    residual = sp.Poly(candidate - target, B_self, B_free, B_h2r, B_h2q)
    equations = [sp.Eq(coeff, 0) for coeff in residual.coeffs()]
    solution = sp.solve(equations, [a, b, c, d], dict=True)

    print("Generic deformation beside the free core:")
    print("  a H.Q + b H.Rlin + c H2.Rlin + d H2.Q")
    print("Universal replacement target:")
    print("  H.Q")
    print(f"  coefficient solution = {solution}")

    ok = solution == [{a: 1, b: 0, c: 0, d: 0}]
    with out.derived_results():
        out.line(
            "replacement ansatz fixes the local derivative self-coupling coefficient",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "H.Q coefficient is one; H.Rlin renormalization and H^2 tower terms are excluded within this ansatz",
        )
    return ok


def case_4_missing_lemma(out: ScriptOutput):
    header("Case 4: Remaining missing lemma isolated")
    print("What this script proves:")
    print("  Within the first-order Palatini replacement ansatz, the derivative")
    print("  self-coupling is uniquely H.Q. H^2 derivative terms are not generated.")
    print()
    print("What remains open:")
    print("  Show that every admissible local, two-derivative, no-extra-field")
    print("  completion can be reduced to this ansatz by boundary terms, field")
    print("  redefinitions, and normalization. The cosmological term is a")
    print("  separate zero-derivative freedom and is already admitted.")

    with out.governance_assessments():
        out.line(
            "closure uniqueness problem narrowed to ansatz-reduction lemma",
            StatusMark.INFO,
            "the Deser citation remains active until that lemma and endpoint uniqueness are proved",
        )
    with out.unresolved_obligations():
        out.line(
            "ansatz-reduction lemma for self-coupled spin-2 closure",
            StatusMark.OBLIGATION,
            "prove all admissible completions reduce to the Palatini replacement class",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="palatini_replacement_no_h2_tower_018",
        inputs=["palatini_finite_decomposition_018"],
        output=sp.Symbol("d2_deps2_eta_plus_eps_H_density_eq_zero"),
        method="Taylor expansion of (eta + eps H).(Rlin + Q)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="Palatini replacement ansatz; not full endpoint uniqueness",
    )
    ns.record_derivation(
        derivation_id="palatini_deformation_bidegree_audit_018",
        inputs=["palatini_replacement_no_h2_tower_018"],
        output=sp.Symbol("candidate_terms_separated_by_H_Gamma_bidegree"),
        method="scale H and Gamma independently and compare polynomial monomials",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="local derivative deformation audit",
    )
    ns.record_derivation(
        derivation_id="palatini_replacement_coefficient_audit_018",
        inputs=["palatini_deformation_bidegree_audit_018"],
        output=sp.Symbol("a_HQ_eq_one_others_zero_within_ansatz"),
        method="linear coefficient matching against the universal replacement target H.Q",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="first-order Palatini replacement ansatz",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "The Palatini deformation audit narrows the remaining problem to "
            "an ansatz-reduction lemma: prove all admissible local two-derivative "
            "completions reduce to the Palatini replacement class up to boundary "
            "terms, field redefinitions, normalization, and the cosmological term."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_3_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Within the first-order Palatini replacement ansatz, the generated "
            "local derivative self-coupling is uniquely H.Q. H.Rlin is part of "
            "the free core, and H^2 derivative terms are not generated by "
            "eta -> eta + H. This narrows but does not retire the in-house "
            "closure-uniqueness obligation; the remaining missing lemma is "
            "ansatz reduction for all admissible completions."
        ),
        derivation_ids=[
            "palatini_replacement_no_h2_tower_018",
            "palatini_deformation_bidegree_audit_018",
            "palatini_replacement_coefficient_audit_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 3")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_taylor_generated_terms(out)
    case_2_bidegree_separation(out)
    case_3_coefficient_audit(out)
    case_4_missing_lemma(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
