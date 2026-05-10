# Candidate GR limit recovery audit
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The conservation identity requirements study found:
#
#   the sector split is disciplined but not closed.
#   closure requires a parent identity.
#
# Before inventing that parent identity, this script audits which GR-facing
# results are actually derived, which are reduced-derived, which are structural,
# which are matched, which are constrained, and which are missing.
#
# This is an audit script, not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status, TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
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


@dataclass
class GRLimitEntry:
    result: str
    gr_target: str
    current_basis: str
    status: str
    what_is_real: str
    what_is_not_yet_real: str
    risk: str
    next_needed: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="conservation_identity_requirements_generated_marker",
        upstream_script_id="11_field_equation_closure__candidate_conservation_identity_requirements_generated",
        upstream_derivation_id="conservation_identity_requirements_generated_marker",
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


def build_audit() -> List[GRLimitEntry]:
    return [
        GRLimitEntry(
            result="Static spherical exterior A",
            gr_target="Schwarzschild A = 1 - 2GM/(c^2 r)",
            current_basis="areal flux law / scalar monopole exterior integration",
            status="DERIVED_REDUCED",
            what_is_real="The exterior scalar factor is genuinely reconstructed in the reduced static spherical case.",
            what_is_not_yet_real="Full covariant derivation and nonspherical nonlinear extension.",
            risk="Overclaiming beyond reduced symmetry.",
            next_needed="parent scalar constraint identity.",
        ),
        GRLimitEntry(
            result="Exterior B = 1/A",
            gr_target="Schwarzschild radial factor",
            current_basis="AB = exp(2 kappa), exterior kappa=0",
            status="DERIVED_REDUCED",
            what_is_real="Reduced exterior reciprocal relation follows once exterior kappa is zero.",
            what_is_not_yet_real="Covariant gauge/physical meaning of kappa and B.",
            risk="Treating areal-gauge relation as full geometry.",
            next_needed="metric recombination / gauge identity.",
        ),
        GRLimitEntry(
            result="Weak scalar multipoles",
            gr_target="Newtonian potential / weak GR scalar limit",
            current_basis="A approx 1 + 2 Phi/c^2, nabla^2 Phi = 4*pi*G rho",
            status="DERIVED_REDUCED",
            what_is_real="Weak scalar/multipole structure follows from scalar constraint analogy.",
            what_is_not_yet_real="Full nonlinear nonspherical equation and conservation closure.",
            risk="Assuming weak multipole success proves complete nonspherical GR.",
            next_needed="nonspherical parent constraint.",
        ),
        GRLimitEntry(
            result="PPN gamma = 1 / spatial scalar response",
            gr_target="equal weak spatial/lapse scalar response",
            current_basis="A/B exterior reciprocal relation and weak expansion",
            status="DERIVED_REDUCED",
            what_is_real="Weak exterior reciprocal relation supports gamma=1 in the reduced regime.",
            what_is_not_yet_real="General PPN derivation with all parameters and gauges.",
            risk="Claiming full PPN success from gamma only.",
            next_needed="full weak-field PPN audit.",
        ),
        GRLimitEntry(
            result="Frame-dragging shape",
            gr_target="far-field gravitomagnetic dipole proportional to angular momentum J",
            current_basis="transverse vector W_i sourced by j_T; rotating source reduces to J",
            status="DERIVED_REDUCED",
            what_is_real="The expected far-field vector shape and angular-momentum dependence are supported.",
            what_is_not_yet_real="Absolute normalization and observable coupling beta_W.",
            risk="Shape success hiding coefficient matching.",
            next_needed="derive alpha_W/K_c and beta_W.",
        ),
        GRLimitEntry(
            result="Frame-dragging normalization",
            gr_target="Lense-Thirring coefficient",
            current_basis="not yet derived; target known from GR",
            status="MATCHED",
            what_is_real="Target normalization is known.",
            what_is_not_yet_real="Ontology-derived coefficient.",
            risk="Importing GR shift-vector coefficient.",
            next_needed="vacuum vector stiffness / source coupling derivation.",
        ),
        GRLimitEntry(
            result="Tensor wave existence",
            gr_target="two transverse-traceless gravitational wave polarizations",
            current_basis="TT sector selected as only ordinary long-range radiation",
            status="STRUCTURAL",
            what_is_real="TT-only radiation is structurally consistent and scalar/vector radiation hazards are constrained.",
            what_is_not_yet_real="Action-derived tensor wave equation and coupling.",
            risk="Assuming GR tensor dynamics because TT is selected.",
            next_needed="tensor action stiffness and source identity.",
        ),
        GRLimitEntry(
            result="Tensor wave coupling",
            gr_target="linearized GR coupling to TT stress / quadrupole",
            current_basis="Box h_TT = -C_T S_TT",
            status="MATCHED",
            what_is_real="Correct target structure is identified.",
            what_is_not_yet_real="C_T from vacuum ontology.",
            risk="C_T imported as 16*pi*G/c^4 or equivalent.",
            next_needed="derive C_T from tensor flux/stiffness.",
        ),
        GRLimitEntry(
            result="Quadrupole radiation power",
            gr_target="GR quadrupole luminosity",
            current_basis="tensor flux proportional to <dot h_TT^2>",
            status="MATCHED",
            what_is_real="Energy-flux form is structurally aligned with TT radiation.",
            what_is_not_yet_real="Absolute flux coefficient and quadrupole power coefficient.",
            risk="Copying GR radiation formula.",
            next_needed="vacuum tensor energy flux derivation.",
        ),
        GRLimitEntry(
            result="No scalar breathing radiation",
            gr_target="GR has no scalar breathing mode",
            current_basis="A_rad rejected; kappa non-inertial trace relaxation",
            status="CONSTRAINED",
            what_is_real="Scalar radiation hazards are explicitly controlled by current rules.",
            what_is_not_yet_real="Parent identity proving absence rather than imposing it.",
            risk="Suppression by rule rather than derivation.",
            next_needed="scalar constraint/radiation split identity.",
        ),
        GRLimitEntry(
            result="Kappa interior/trace behavior",
            gr_target="GR interior pressure/stress effects without exterior scalar radiation",
            current_basis="kappa_min shift and non-inertial relaxation",
            status="STRUCTURAL",
            what_is_real="Coherent control model prevents kappa from becoming scalar gravity.",
            what_is_not_yet_real="Source law, coefficients, covariant origin, boundary theorem.",
            risk="Repair knob if not parent-derived.",
            next_needed="kappa non-radiative trace identity.",
        ),
        GRLimitEntry(
            result="Near-boundary deviation",
            gr_target="possible deviation from naive GR interior/exterior matching",
            current_basis="joint minimum spline/energy diagnostic",
            status="RISK",
            what_is_real="Deviation diagnostics are defined.",
            what_is_not_yet_real="Magnitude, observable, weights, transition width, compatibility with tests.",
            risk="Overclaiming unmeasured prediction.",
            next_needed="only after closure: numerical model and observability scan.",
        ),
        GRLimitEntry(
            result="Conservation / Bianchi compatibility",
            gr_target="nabla_mu G^mu_nu = 0 and nabla_mu T^mu_nu = 0 compatibility",
            current_basis="requirements ledger only",
            status="MISSING",
            what_is_real="The required identity is now named.",
            what_is_not_yet_real="The identity itself.",
            risk="Theory remains sector ledger, not closed field equations.",
            next_needed="candidate parent identity template.",
        ),
        GRLimitEntry(
            result="Metric recombination",
            gr_target="one coherent metric field",
            current_basis="reduced bookkeeping ansatz",
            status="UNFINISHED",
            what_is_real="Sector map is explicit and no-double-counting rules are known.",
            what_is_not_yet_real="Covariant recombination map.",
            risk="Silent GR import.",
            next_needed="parent metric/recombination identity.",
        ),
    ]


def print_entry(e: GRLimitEntry) -> None:
    marks = {
        "DERIVED": "PASS",
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "MATCHED": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "REJECTED": "WARN",
        "UNFINISHED": "FAIL",
    }
    mark = marks.get(e.status, "INFO")
    print()
    print("-" * 120)
    print(e.result)
    print("-" * 120)
    print(f"GR target: {e.gr_target}")
    print(f"Current basis: {e.current_basis}")
    print(f"[{mark}] {e.result}: {e.status}")
    print(f"What is real: {e.what_is_real}")
    print(f"What is not yet real: {e.what_is_not_yet_real}")
    print(f"Risk: {e.risk}")
    print(f"Next needed: {e.next_needed}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: GR limit recovery audit problem")

    print("Question:")
    print()
    print("  Which GR-facing results are actually derived, reduced-derived, structural, matched,")
    print("  constrained, missing, or risky?")
    print()
    print("Goal:")
    print()
    print("  prevent the theory from claiming closure by inheriting GR targets")
    print()
    print("Discipline:")
    print()
    print("  targets are not derivations")
    print("  structural agreement is not coefficient derivation")
    print("  reduced reconstruction is real but limited")

    with out.governance_assessments():
        out.line("GR recovery audit problem posed", StatusMark.DEFER, "structural constraint")


def case_1_audit_inventory(entries: List[GRLimitEntry]):
    header("Case 1: GR limit audit inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[GRLimitEntry], out: ScriptOutput):
    header("Case 2: Compact GR recovery ledger")

    print("| Result | GR target | Status | Real | Not yet real |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.result.replace("|", "/")
            + " | "
            + e.gr_target.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.what_is_real.replace("|", "/")
            + " | "
            + e.what_is_not_yet_real.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact GR recovery ledger produced", StatusMark.PASS, "inventory marker")


def case_3_status_counts(entries: List[GRLimitEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The strongest results are reduced scalar/exterior results.")
    print("  Vector shape is reduced-derived but normalization is matched/missing.")
    print("  Tensor radiation is structurally correct but coupling and flux are matched.")
    print("  Conservation/Bianchi closure is missing.")

    with out.governance_assessments():
        out.line("GR audit status count produced", StatusMark.PASS, "inventory marker")


def case_4_strongest_results(out: ScriptOutput):
    header("Case 4: Strongest results")

    print("Strongest current GR-facing recoveries:")
    print()
    print("1. Static spherical exterior A.")
    print("2. Exterior B=1/A once kappa=0.")
    print("3. Weak scalar multipole / Newtonian limit.")
    print("4. Gamma=1 in the reduced exterior weak limit.")
    print("5. Frame-dragging far-field shape proportional to J.")
    print()
    print("These are real reduced/structural wins, but limited.")

    with out.governance_assessments():
        out.line("strongest GR-facing results identified", StatusMark.PASS,
                 "reduced derivations confirmed")


def case_5_weakest_results(out: ScriptOutput):
    header("Case 5: Weakest results")

    print("Weakest or most matched GR-facing pieces:")
    print()
    print("1. Frame-dragging normalization.")
    print("2. Tensor coupling C_T.")
    print("3. Tensor radiation energy flux coefficient.")
    print("4. Bianchi/conservation closure.")
    print("5. Covariant metric recombination.")
    print()
    print("These must not be advertised as derived.")

    with out.governance_assessments():
        out.line("weakest GR-facing pieces identified", StatusMark.WARN, "open risk")


def case_6_reconstruction_scorecard(out: ScriptOutput):
    header("Case 6: Reconstruction scorecard")

    print("Reconstruction scorecard:")
    print()
    print("  Reduced scalar exterior:")
    print("    real reconstruction")
    print()
    print("  Weak scalar/multipole:")
    print("    reduced/structural success")
    print()
    print("  Vector sector:")
    print("    shape success, normalization missing")
    print()
    print("  Tensor radiation:")
    print("    structural TT success, coupling/flux matched")
    print()
    print("  Kappa:")
    print("    safety/control success, not covariant derivation")
    print()
    print("  Conservation/closure:")
    print("    missing")

    with out.governance_assessments():
        out.line("reconstruction scorecard produced", StatusMark.DEFER, "structural assessment")


def case_6b_vf_reciprocal_metric_crosscheck(ns, out: ScriptOutput):
    header("Case 6b: VacuumForge reciprocal metric cross-check")

    ctx = TheoryContext("candidate_gr_limit_recovery_audit")
    ms = ctx.define_equal_response_algebraic_symbols()
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = 1 / A_value
    result = check_concrete_metric(ctx, A_value, B_value, ["reciprocal_scaling"])[0]
    product = sp.simplify(A_value * B_value)

    print(f"A_value = {A_value}")
    print(f"B_value = {B_value}")
    print(f"A_value * B_value = {product}")
    print(f"ConcreteMetricCheck status = {result.status}")
    print(f"Message = {result.message}")

    ok = result.status == "satisfied_by_construction" and product == 1

    with out.derived_results():
        out.line(
            "VacuumForge classifies reciprocal Schwarzschild metric as by-construction",
            StatusMark.PASS if ok else StatusMark.FAIL,
            f"A*B = {product}",
        )

    ns.record_derivation(
        derivation_id="gr_limit_reciprocal_metric_crosscheck",
        inputs=[A_value, B_value],
        output=product,
        method="ConcreteMetricCheck reciprocal_scaling",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
    )


def case_6_good_failure(out: ScriptOutput):
    header("Case 6c: Good failure demonstration")

    print("Controlled failure: A*B product check with non-reciprocal B.")
    print()
    print("  If B is incorrectly set to 1 (flat) instead of 1/A,")
    print("  then A*B != 1 and the reciprocal_scaling check must fail.")

    ctx = TheoryContext("candidate_gr_limit_recovery_audit__failure")
    ms = ctx.define_equal_response_algebraic_symbols()
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_wrong = sp.Integer(1)  # deliberately wrong: B should be 1/A
    product_wrong = sp.simplify(A_value * B_wrong)

    print(f"A_value = {A_value}")
    print(f"B_wrong = {B_wrong}  (flat, not 1/A)")
    print(f"A_value * B_wrong = {product_wrong}")

    detected = product_wrong != 1
    print(f"Nonzero deviation detected: {detected}")

    with out.counterexamples():
        out.line(
            "non-reciprocal B gives A*B != 1",
            StatusMark.FAIL if detected else StatusMark.WARN,
            f"A*B = {product_wrong}; deviation = {sp.simplify(product_wrong - 1)}",
        )

    print()
    if detected:
        print("[PASS] Good failure: non-reciprocal B is correctly detected as failing reciprocal scaling.")
    else:
        print("[FAIL] Failure detection did not work as expected.")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_gr_limit_recovery_audit.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_identity_template.py")
    print("   Try to write an explicit candidate parent identity.")
    print()
    print("3. candidate_field_equation_closure_failure_modes.py")
    print("   List ways full closure can fail.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_identity_template.py")
    print()
    print("Reason:")
    print("  The GR audit has separated real wins from matched gaps; now try the parent identity.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("Honest GR recovery status:")
    print()
    print("  real reduced reconstruction: static spherical exterior")
    print("  strong reduced/structural support: weak scalar limit, gamma=1, vector shape")
    print("  structural but not coefficient-derived: tensor waves")
    print("  matched: tensor coupling/flux and vector normalization")
    print("  constrained: no scalar radiation and kappa safety")
    print("  missing: Bianchi-like parent closure and covariant recombination")
    print()
    print("Possible next artifact:")
    print("  candidate_gr_limit_recovery_audit.md")
    print()
    print("Possible next script:")
    print("  candidate_parent_identity_template.py")


def record_governance(ns, entries: List[GRLimitEntry]) -> None:
    # DERIVED_REDUCED -> HEURISTIC claims
    ns.record_claim(ClaimRecord(
        claim_id="gr_static_spherical_exterior_A",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "Static spherical exterior A = 1 - 2GM/(c^2 r) is genuinely reconstructed "
            "in the reduced static spherical case via areal flux law."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="gr_exterior_B_reciprocal",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "Exterior B = 1/A follows from AB = exp(2 kappa) once exterior kappa=0. "
            "This is a reduced areal-gauge derivation, not full covariant geometry."
        ),
    ))

    # MATCHED -> PROVISIONAL_CONVENTION + obligations for coefficient origin
    ns.record_claim(ClaimRecord(
        claim_id="gr_frame_dragging_normalization_matched",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "Frame-dragging normalization (Lense-Thirring coefficient) is identified as a target. "
            "Target normalization is known from GR. Ontology-derived coefficient is missing."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_alpha_W_K_c_and_beta_W",
        script_id=SCRIPT_ID,
        title="Derive alpha_W/K_c and beta_W (vector coupling coefficients)",
        status=ObligationStatus.OPEN,
        description=(
            "The vector coupling coefficients alpha_W/K_c and observable coupling beta_W "
            "must be derived from vacuum vector stiffness / source coupling. "
            "GR Lense-Thirring coefficient must not be imported."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="gr_tensor_coupling_matched",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "Tensor wave coupling Box h_TT = -C_T S_TT has correct target structure. "
            "C_T from vacuum ontology is not yet derived. C_T must not be imported as "
            "16*pi*G/c^4 or equivalent."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_C_T_tensor_coupling_from_stiffness",
        script_id=SCRIPT_ID,
        title="Derive C_T tensor coupling from vacuum stiffness",
        status=ObligationStatus.OPEN,
        description=(
            "C_T must be derived from tensor flux/stiffness in the vacuum ontology. "
            "It must not be imported from GR radiation coupling constants."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="gr_quadrupole_radiation_power_matched",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "Quadrupole radiation power F_T ~ K_T <dot h_TT^2> has correct structural form. "
            "Absolute flux coefficient is not derived. GR radiation formula must not be copied."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_vacuum_tensor_energy_flux_coefficient",
        script_id=SCRIPT_ID,
        title="Derive vacuum tensor energy flux coefficient",
        status=ObligationStatus.OPEN,
        description=(
            "The absolute tensor radiation energy flux coefficient must be derived from "
            "vacuum tensor ontology. GR quadrupole luminosity formula must not be copied."
        ),
    ))

    # MISSING -> OPEN obligation
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_conservation_bianchi_parent_identity",
        script_id=SCRIPT_ID,
        title="Derive conservation/Bianchi-like parent identity",
        status=ObligationStatus.OPEN,
        description=(
            "A parent divergence identity compatible with nabla_mu G^mu_nu = 0 and "
            "nabla_mu T^mu_nu = 0 must be derived. Without this the theory remains "
            "a sector ledger, not a closed field equation system."
        ),
    ))

    # OPEN_RISK
    ns.record_claim(ClaimRecord(
        claim_id="gr_near_boundary_deviation_risk",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "A possible near-boundary deviation from GR interior/exterior matching is "
            "indicated by joint-minimum spline diagnostics. Magnitude, observable, weights, "
            "and transition width are not yet derived. This must not be overclaimed."
        ),
    ))

    # Audit marker (placeholder, inventory-level)
    ns.record_derivation(
        derivation_id="gr_limit_recovery_audit_marker",
        inputs=[],
        output=sp.Symbol("gr_limit_recovery_audit_completed"),
        method="gr_limit_recovery_audit_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate GR Limit Recovery Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_audit()
    case_1_audit_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_strongest_results(out)
    case_5_weakest_results(out)
    case_6_reconstruction_scorecard(out)
    case_6b_vf_reciprocal_metric_crosscheck(ns, out)
    case_6_good_failure(out)
    case_7_next_tests(out)
    final_interpretation()
    out.print_summary()
    with archive:
        record_governance(ns, entries)
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
