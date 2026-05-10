# Candidate scalar constraint not radiation identity
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# The projector audit found that P_scalar is the hardest immediate gate.
#
# The parent identity must explain:
#
#   A is a scalar constraint / mass-flux response,
#   not an ordinary propagating scalar radiation field.
#
# This script focuses on the scalar sector:
#
#   Why does rho feed A?
#   Why does rho not feed A_rad?
#   Why does rho not feed long-range kappa?
#   How can A update with source continuity without becoming Box A?
#
# This is not a derivation.
# It is an identity-requirement and failure audit.
#
# The central finding is a policy rule:
#   "scalar constraint is not radiation identity"

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
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
class ScalarRequirement:
    name: str
    requirement: str
    target_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="projector_structure_for_parent_identity_marker",
        upstream_script_id="12_parent_identity_and_recombination__candidate_projector_structure_for_parent_identity",
        upstream_derivation_id="projector_structure_for_parent_identity_marker",
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


def build_requirements() -> List[ScalarRequirement]:
    return [
        ScalarRequirement(
            name="S1: scalar source routes to A",
            requirement="rho / scalar charge feeds the A-sector constraint.",
            target_form="P_scalar[T] -> rho_eff -> Delta_areal A = 8*pi*G*rho/c^2",
            forbidden_form="rho feeds A_rad or independent kappa charge.",
            status="DERIVED_REDUCED",
            risk="Scalar source leaks into forbidden scalar sectors.",
            missing="Parent definition of rho_eff and P_scalar.",
        ),
        ScalarRequirement(
            name="S2: A is constraint, not Box A",
            requirement="A must remain elliptic/constraint-like in ordinary gravity.",
            target_form="C_A[A,rho]=0 with constraint propagation from continuity",
            forbidden_form="Box A = alpha*rho",
            status="CONSTRAINED",
            risk="Ordinary scalar gravitational radiation appears.",
            missing="Continuity-compatible constraint propagation identity.",
        ),
        ScalarRequirement(
            name="S3: A_rad ordinary massless source vanishes",
            requirement="The ordinary long-range scalar radiative channel is absent.",
            target_form="source(A_rad ordinary massless)=0",
            forbidden_form="Box A_rad = source",
            status="REJECTED",
            risk="Breathing radiation channel.",
            missing="Parent mechanism proving scalar radiation exclusion.",
        ),
        ScalarRequirement(
            name="S4: rho does not source long-range kappa",
            requirement="rho must not create independent exterior kappa charge.",
            target_form="S_kappa[rho]=0 and Q_kappa=0",
            forbidden_form="kappa_ext ~ 1/r from rho",
            status="CONSTRAINED",
            risk="Scalar double-counting and second exterior scalar field.",
            missing="Parent projection or boundary cancellation identity.",
        ),
        ScalarRequirement(
            name="S5: trace does not become scalar radiation",
            requirement="Trace/pressure may shift kappa_min but must not source Box kappa or A_rad.",
            target_form="trace -> kappa_min; dot kappa = -mu*K*(kappa-kappa_min)",
            forbidden_form="Box kappa = alpha*trace",
            status="STRUCTURAL",
            risk="Hidden breathing mode.",
            missing="P_trace/P_relax parent identity.",
        ),
        ScalarRequirement(
            name="S6: scalar continuity drives constraint update",
            requirement="Time-dependent rho updates A through continuity, not through scalar radiation.",
            target_form="partial_t C_A[A,rho] implied by partial_t rho + div j_L = 0",
            forbidden_form="add scalar wave dynamics to make A causal by hand",
            status="MISSING",
            risk="Constraint becomes inconsistent for moving sources.",
            missing="Reduced or parent constraint-propagation equation.",
        ),
        ScalarRequirement(
            name="S7: exterior scalar charge equals A-sector mass",
            requirement="The only ordinary exterior scalar charge is M_ext in A.",
            target_form="A_ext = 1 - 2*G*M_ext/(c^2*r)",
            forbidden_form="additional scalar 1/r tails from A_rad or kappa",
            status="DERIVED_REDUCED",
            risk="Multiple scalar charges in exterior vacuum.",
            missing="Parent mass-flux charge conservation.",
        ),
        ScalarRequirement(
            name="S8: scalar projector survives weak multipoles",
            requirement="P_scalar must support weak nonspherical Newtonian multipoles without scalar radiation.",
            target_form="A ~= 1 + 2*Phi/c^2; nabla^2 Phi = 4*pi*G*rho",
            forbidden_form="weak scalar waves sourced by ordinary matter",
            status="DERIVED_REDUCED",
            risk="Static weak multipoles confused with scalar radiation.",
            missing="Full nonspherical parent constraint.",
        ),
        ScalarRequirement(
            name="S9: scalar sector recombination counted once",
            requirement="A's scalar response must not be duplicated in kappa or spatial metric trace.",
            target_form="P_recombination counts scalar response exactly once",
            forbidden_form="A and kappa both represent the same scalar mass response",
            status="UNRESOLVED",
            risk="Silent scalar double-counting in metric map.",
            missing="Recombination projector.",
        ),
    ]


def print_requirement(r: ScalarRequirement) -> None:
    print()
    print("-" * 120)
    print(r.name)
    print("-" * 120)
    print(f"Requirement: {r.requirement}")
    print(f"Target form: {r.target_form}")
    print(f"Forbidden form: {r.forbidden_form}")
    print(f"[INFO] {r.name}: {r.status}")
    print(f"Risk: {r.risk}")
    print(f"Missing: {r.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Scalar constraint-not-radiation problem")

    print("Question:")
    print()
    print("  Why does scalar source produce A as a constraint, rather than scalar radiation?")
    print()
    print("Goal:")
    print()
    print("  isolate the scalar-sector identity requirements")
    print()
    print("Discipline:")
    print()
    print("  do not allow Box A")
    print("  do not allow A_rad")
    print("  do not allow rho-sourced kappa")
    print("  do not confuse static multipoles with scalar radiation")

    with out.unresolved_obligations():
        out.line("scalar constraint-not-radiation problem posed", StatusMark.OBLIGATION, "scalar sector requirements open")


def case_1_requirement_inventory(entries: List[ScalarRequirement]):
    header("Case 1: Scalar requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[ScalarRequirement], out: ScriptOutput):
    header("Case 2: Compact scalar constraint ledger")

    print("| Requirement | Target form | Forbidden form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.target_form.replace("|", "/")
            + " | "
            + e.forbidden_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact scalar ledger produced", StatusMark.INFO, "9 scalar sector requirements recorded")


def case_3_status_counts(entries: List[ScalarRequirement], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The static/reduced scalar sector is strong.")
    print("  The missing piece is scalar constraint propagation for time-dependent sources.")
    print("  Recombination remains unresolved.")

    with out.governance_assessments():
        out.line("scalar status count produced", StatusMark.INFO, str(counts))


def case_4_candidate_identity_shape(out: ScriptOutput):
    header("Case 4: Candidate scalar identity shape")

    print("A useful scalar parent implication would have the shape:")
    print()
    print("  P_scalar Div(E_parent) -> constraint propagation")
    print()
    print("with reduced content:")
    print()
    print("  C_A[A,rho] = 0")
    print("  partial_t C_A[A,rho] follows from partial_t rho + div j_L = 0")
    print("  source(A_rad ordinary massless) = 0")
    print("  S_kappa[rho] = 0")
    print()
    print("This would make scalar non-radiation structural rather than imposed.")
    print()
    print("This is currently a target, not a derivation.")

    with out.unresolved_obligations():
        out.line("candidate scalar identity shape stated", StatusMark.OBLIGATION, "scalar identity shape remains a theorem target")


def case_5_failure_controls(out: ScriptOutput):
    header("Case 5: Failure controls")

    print("The scalar sector fails if:")
    print()
    print("1. Box A appears as an ordinary matter-sourced wave equation.")
    print("2. A_rad becomes active ordinary radiation.")
    print("3. rho sources long-range kappa.")
    print("4. trace/pressure creates Box kappa.")
    print("5. scalar constraint cannot update with moving sources.")
    print("6. weak static multipoles are used to justify scalar waves.")
    print("7. recombination counts scalar response twice.")

    with out.governance_assessments():
        out.line("scalar failure controls stated", StatusMark.DEFER, "failure controls policy-guarded")


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_scalar_constraint_not_radiation_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_kappa_covariant_relaxation_requirement.py")
    print("   Focus on kappa relaxation and frame/covariance issue.")
    print()
    print("3. candidate_scalar_constraint_propagation_toy_model.py")
    print("   Try a reduced continuity-compatible scalar constraint update.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_covariant_relaxation_requirement.py")
    print()
    print("Reason:")
    print("  Scalar A is protected by constraints; now kappa's first-order relaxation must be frame/covariance audited.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "kappa covariant relaxation script is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("The scalar sector can remain safe if:")
    print()
    print("  rho routes only to A")
    print("  A remains a constraint")
    print("  A_rad has no ordinary massless source")
    print("  rho does not source long-range kappa")
    print("  trace shifts kappa_min without Box kappa")
    print("  moving sources update A through continuity")
    print("  recombination counts scalar response once")
    print()
    print("The missing scalar piece is:")
    print("  continuity-compatible scalar constraint propagation.")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_constraint_not_radiation_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_covariant_relaxation_requirement.py")


def main():
    header("Candidate Scalar Constraint Not Radiation Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_identity_shape(out)
    case_5_failure_controls(out)
    case_6_next_tests(out)
    final_interpretation()

    # Central policy rule: scalar constraint is not radiation identity
    ns.record_claim(ClaimRecord(
        claim_id="scalar_constraint_is_not_radiation_identity",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The scalar field A is a mass-flux constraint, not an ordinary propagating scalar radiation field. "
            "Box A = alpha*rho is forbidden. A_rad ordinary massless source must vanish. "
            "Rho must route to the A-sector constraint and must not source independent long-range kappa charge. "
            "This separation is a construction rule for the parent identity, not a downstream recovery target."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="scalar_radiation_channel_absent_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "source(A_rad ordinary massless) = 0 is a policy rule for this theory. "
            "The ordinary scalar radiative channel does not exist in this construction."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="box_kappa_from_trace_forbidden_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Box kappa = alpha*trace is forbidden. Trace/pressure shifts kappa_min only; "
            "kappa relaxes first-order. This policy prevents the trace from becoming a breathing mode."
        ),
    ))

    # Proof obligations for missing scalar items
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_constraint_propagation_from_continuity_S6",
        script_id=SCRIPT_ID,
        title="Derive continuity-compatible scalar constraint propagation (S6)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that partial_t C_A[A,rho] follows from partial_t rho + div j_L = 0 "
            "without introducing Box A scalar radiation. This is the key missing scalar piece."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_scalar_rho_eff_definition",
        script_id=SCRIPT_ID,
        title="Define rho_eff and P_scalar from parent identity",
        status=ObligationStatus.OPEN,
        description=(
            "The parent identity must define rho_eff and P_scalar such that "
            "P_scalar routes scalar charge to the A-sector areal constraint."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_scalar_recombination_count_once_S9",
        script_id=SCRIPT_ID,
        title="Derive recombination projector preventing scalar double-counting (S9)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that A's scalar response is not duplicated in kappa or spatial metric trace "
            "when P_recombination maps sectors to the geometry-like object."
        ),
    ))

    # Branch decision: scalar radiation branch is deferred/excluded
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_scalar_radiation_A_rad_branch",
        script_id=SCRIPT_ID,
        branch_id="scalar_radiation_A_rad",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_scalar_constraint_propagation_from_continuity_S6"],
        description=(
            "The A_rad ordinary scalar radiation branch is not licensed. "
            "The parent identity must derive constraint propagation before any scalar "
            "radiation form can be considered."
        ),
    ))

    ns.record_derivation(
        derivation_id="scalar_constraint_not_radiation_identity_marker",
        inputs=[],
        output=sp.Symbol("scalar_constraint_not_radiation_identity_built"),
        method="scalar_constraint_not_radiation_identity_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
