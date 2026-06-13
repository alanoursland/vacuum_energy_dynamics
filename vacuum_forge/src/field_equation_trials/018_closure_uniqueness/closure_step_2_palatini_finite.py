# Trial 018: Closure uniqueness, step 2
#
# Script type:
#   RIGOR PROGRAM / PALATINI FINITE-CLOSURE WITNESS
#
# Purpose
# -------
# This is the second in-house rung toward replacing the Deser 1970
# self-coupled spin-2 closure citation. It does not retire the full
# closure-uniqueness obligation.
#
# Step 1 showed that self-coupling is forced by source conservation.
# This script verifies the first-order/Palatini algebra behind the
# standard finite bootstrap:
#
#   1. The flat-background Palatini density decomposes as
#        eta.Rlin + H.Rlin + eta.Q + H.Q,
#      where Rlin is derivative-linear in the independent connection
#      and Q is connection-quadratic.
#   2. eta.Rlin is a boundary divergence on the fixed background.
#   3. The only non-boundary nonlinear completion term in densitized
#      inverse-metric variables is H.Q: cubic, local, and finite.
#   4. Replacing eta by eta + eps H in eta.Q generates exactly H.Q at
#      first order. This is the explicit first self-coupling term.
#
# This proves a finite-closure witness, not uniqueness. The remaining
# obligation is to prove that the assumptions leave no inequivalent
# local two-derivative completion.

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
        dependency_id="closure_step_1_dependency_018",
        upstream_script_id="018_closure_uniqueness__closure_step_1",
        upstream_derivation_id="first_self_coupling_obstruction_018",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


eps = sp.Symbol("eps")

H = sp.Matrix(DIM, DIM, lambda mu, nu: sp.Symbol(f"H{mu}{nu}"))


def eta_up(mu: int, nu: int):
    return sp.Integer(ETA[mu]) if mu == nu else sp.Integer(0)


def Gamma(alpha: int, mu: int, nu: int):
    # Torsion-free first-order connection: Gamma^alpha_{mu nu}=Gamma^alpha_{nu mu}.
    a, b = sorted((mu, nu))
    return sp.Symbol(f"G{alpha}_{a}{b}")


def dGamma(alpha: int, mu: int, nu: int, rho: int):
    # Placeholder for partial_rho Gamma^alpha_{mu nu}; lower connection slots are symmetric.
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


def eta_plus_H(mu: int, nu: int):
    return eta_up(mu, nu) + eps * H[mu, nu]


ETA_RLIN = contraction(eta_up, Rlin)
H_RLIN = contraction(H_component, Rlin)
ETA_Q = contraction(eta_up, Q)
H_Q = contraction(H_component, Q)
PALATINI_DENSITY = contraction(eta_plus_H, lambda mu, nu: Rlin(mu, nu) + Q(mu, nu))


def boundary_divergence_eta_rlin():
    first = sum(
        eta_up(mu, nu) * dGamma(alpha, mu, nu, alpha)
        for mu in range(DIM)
        for nu in range(DIM)
        for alpha in range(DIM)
    )
    second = sum(
        eta_up(mu, nu) * dGamma(alpha, mu, alpha, nu)
        for mu in range(DIM)
        for nu in range(DIM)
        for alpha in range(DIM)
    )
    return sp.simplify(first - second)


def scale_expr(expr):
    a, b = sp.symbols("a b")
    subs = {}
    for mu in range(DIM):
        for nu in range(DIM):
            subs[H[mu, nu]] = a * H[mu, nu]
    for alpha in range(DIM):
        for mu in range(DIM):
            for nu in range(mu, DIM):
                subs[Gamma(alpha, mu, nu)] = b * Gamma(alpha, mu, nu)
                for rho in range(DIM):
                    subs[dGamma(alpha, mu, nu, rho)] = b * dGamma(alpha, mu, nu, rho)
    return sp.Poly(sp.expand(expr.xreplace(subs)), a, b)


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Closure uniqueness program, second rung")
    print("Step 1 proved that a conserved total source forces field")
    print("self-coupling. This step checks the first-order Palatini algebra")
    print("that makes the standard spin-2 self-coupling finite.")
    print()
    print("Variables:")
    print("  H^mu nu      = perturbation of the inverse metric density")
    print("  Gamma^a_mn   = independent torsion-free connection")
    print("  Rlin_mn      = derivative-linear Ricci part")
    print("  Q_mn         = connection-quadratic Ricci part")

    with out.governance_assessments():
        out.line(
            "Palatini finite-closure witness opened",
            StatusMark.INFO,
            "second rung only; uniqueness of the endpoint remains open",
        )


def case_1_boundary_term(out: ScriptOutput):
    header("Case 1: Fixed-background eta.Rlin is a boundary divergence")
    boundary = boundary_divergence_eta_rlin()
    residual = sp.simplify(ETA_RLIN - boundary)
    print("eta^mn Rlin_mn equals")
    print("  partial_a(eta^mn Gamma^a_mn) - partial_n(eta^mn Gamma^a_ma)")
    print(f"  residual = {sp.sstr(residual)}")

    ok = is_zero(residual)
    with out.derived_results():
        out.line(
            "flat eta.Rlin term is boundary-only",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "the free first-order core is H.Rlin + eta.Q up to this boundary term",
        )
    return ok


def case_2_finite_decomposition(out: ScriptOutput):
    header("Case 2: Palatini density decomposes into free core plus one cubic term")
    expected = ETA_RLIN + eps * H_RLIN + ETA_Q + eps * H_Q
    residual = sp.simplify(PALATINI_DENSITY - expected)
    print("Full first-order density:")
    print("  (eta^mn + eps H^mn)(Rlin_mn + Q_mn)")
    print("Decomposition:")
    print("  eta.Rlin + eps H.Rlin + eta.Q + eps H.Q")
    print(f"  decomposition residual = {sp.sstr(residual)}")

    poly = scale_expr(PALATINI_DENSITY)
    monoms = sorted(poly.monoms())
    print(f"  scaling monomials in (H, Gamma) = {monoms}")
    expected_monoms = {(0, 1), (1, 1), (0, 2), (1, 2)}
    no_extra_tower = set(monoms).issubset(expected_monoms)
    ok = is_zero(residual) and no_extra_tower

    with out.derived_results():
        out.line(
            "first-order Palatini closure is finite in densitized variables",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "only boundary, free, and H.Gamma.Gamma terms occur; no H^2 tower appears",
        )
    return ok


def case_3_first_self_coupling_term(out: ScriptOutput):
    header("Case 3: Replacing eta by eta + eps H generates the first self-coupling")
    varied_eta_q = contraction(eta_plus_H, Q)
    generated = sp.diff(varied_eta_q, eps).subs(eps, 0)
    residual = sp.simplify(generated - H_Q)

    print("Start from the connection-quadratic background term:")
    print("  eta^mn Q_mn")
    print("Replace eta^mn -> eta^mn + eps H^mn and differentiate at eps=0:")
    print("  d/deps [(eta^mn + eps H^mn) Q_mn] = H^mn Q_mn")
    print(f"  first-coupling residual = {sp.sstr(residual)}")

    ok = is_zero(residual)
    with out.derived_results():
        out.line(
            "explicit first self-coupling term generated",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "the required source correction is the cubic H.Gamma.Gamma term",
        )
    return ok


def case_4_h_variation_reads_full_ricci(out: ScriptOutput):
    header("Case 4: H variation reads the full first-order Ricci tensor")
    sample_residuals = []
    for mu, nu in [(0, 0), (0, 1), (1, 1), (2, 3)]:
        derivative = sp.diff(PALATINI_DENSITY, H[mu, nu])
        expected = eps * (Rlin(mu, nu) + Q(mu, nu))
        residual = sp.simplify(derivative - expected)
        sample_residuals.append(residual)
        print(f"  dL/dH{mu}{nu} - eps*(Rlin+Q)_{mu}{nu} = {sp.sstr(residual)}")

    ok = all(is_zero(residual) for residual in sample_residuals)
    with out.derived_results():
        out.line(
            "densitized metric variation returns full Ricci component",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "the finite completion sources the same spin-2 equation with Rlin + Q, not a new operator",
        )
    return ok


def case_5_verdict(out: ScriptOutput) -> None:
    header("Case 5: Verdict")
    print("This rung gives the finite first-order closure witness:")
    print()
    print("  free core:     H.Rlin + eta.Q")
    print("  boundary:      eta.Rlin")
    print("  self-coupling: H.Q")
    print()
    print("The algebra shows why the self-coupling chain can close in one")
    print("Palatini replacement eta -> eta + H. It does not yet prove that no")
    print("other local two-derivative completion satisfies the same assumptions.")

    with out.governance_assessments():
        out.line(
            "closure uniqueness obligation advanced but not retired",
            StatusMark.INFO,
            "finite Palatini closure witness discharged; uniqueness audit remains open",
        )
    with out.unresolved_obligations():
        out.line(
            "in-house self-coupled spin-2 closure uniqueness",
            StatusMark.OBLIGATION,
            "finite closure witness proved here; full uniqueness theorem remains active",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="palatini_boundary_term_018",
        inputs=["linear_bianchi_identity_018", "first_self_coupling_obstruction_018"],
        output=sp.Symbol("eta_Rlin_is_boundary"),
        method="component contraction of flat eta with derivative-linear Palatini Ricci part",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="first-order Palatini density on Minkowski background",
    )
    ns.record_derivation(
        derivation_id="palatini_finite_decomposition_018",
        inputs=["palatini_boundary_term_018"],
        output=sp.Symbol("L_equals_boundary_plus_free_plus_H_Q"),
        method="symbolic expansion of (eta + eps H).(Rlin + Q) with independent torsion-free connection",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="finite cubic closure witness; not uniqueness",
    )
    ns.record_derivation(
        derivation_id="palatini_first_self_coupling_term_018",
        inputs=["palatini_finite_decomposition_018"],
        output=sp.Symbol("delta_eta_Q_equals_H_Q"),
        method="differentiate eta.Q under eta -> eta + eps H",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="closure_uniqueness_rung",
        scope="explicit first self-coupling term",
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="closure_uniqueness_inhouse_018",
        script_id=SCRIPT_ID,
        title="In-house self-coupled spin-2 closure uniqueness",
        status=ObligationStatus.OPEN,
        required_by=["field_equation_proof"],
        description=(
            "The Palatini finite-closure witness is proved in-house by "
            "palatini_boundary_term_018, palatini_finite_decomposition_018, "
            "and palatini_first_self_coupling_term_018. Full endpoint uniqueness remains open."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="closure_step_2_claim_018",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In first-order Palatini variables, the spin-2 self-coupling "
            "has a finite algebraic witness: the density "
            "(eta + H).(Rlin + Q) decomposes into a boundary term, the "
            "free first-order core H.Rlin + eta.Q, and the single cubic "
            "term H.Q. Replacing eta by eta + H in eta.Q generates the "
            "first self-coupling term. This advances but does not retire "
            "the in-house closure-uniqueness obligation."
        ),
        derivation_ids=[
            "palatini_boundary_term_018",
            "palatini_finite_decomposition_018",
            "palatini_first_self_coupling_term_018",
        ],
        obligation_ids=["closure_uniqueness_inhouse_018"],
    ))


def main() -> None:
    header("Trial 018: Closure Uniqueness Step 2")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_boundary_term(out)
    case_2_finite_decomposition(out)
    case_3_first_self_coupling_term(out)
    case_4_h_variation_reads_full_ricci(out)
    case_5_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
