# Candidate no-double-counting constraints
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# The source decomposition ledger identified source-sector roles:
#
#   rho -> A
#   j_T -> W_i
#   trace/pressure -> kappa_min shift
#   TT stress/quadrupole -> h_ij^TT
#   A_rad ordinary long-range scalar source -> rejected
#
# This script formalizes the no-double-counting constraints.
#
# It asks:
#
#   which source-sector overlaps must vanish?
#   which overlaps are allowed only through a parent identity?
#   which overlaps are permitted as consistency couplings, not independent sources?
#
# This is an audit script, not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

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


@dataclass
class ConstraintEntry:
    name: str
    expression: str
    meaning: str
    status: str
    risk_if_violated: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="source_decomposition_ledger_marker",
        upstream_script_id="11_field_equation_closure__candidate_source_decomposition_ledger",
        upstream_derivation_id="source_decomposition_ledger_marker",
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


def build_constraints() -> List[ConstraintEntry]:
    return [
        ConstraintEntry(
            name="C1: rho not double-sourced into kappa",
            expression="S_kappa[rho] = 0 as independent long-range scalar source",
            meaning="rho sources A; kappa may not carry a second rho-sourced 1/r field.",
            status="CONSTRAINED",
            risk_if_violated="Double-counted scalar gravity and exterior kappa tail.",
            missing="Parent source decomposition proving rho role.",
        ),
        ConstraintEntry(
            name="C2: exterior kappa charge vanishes",
            expression="Q_kappa = integral S_kappa d^3x = 0",
            meaning="No massless exterior kappa monopole.",
            status="CONSTRAINED",
            risk_if_violated="kappa_ext ~ 1/r scalar gravity.",
            missing="Projection/boundary identity deriving Q_kappa=0.",
        ),
        ConstraintEntry(
            name="C3: pressure/trace shifts minimum, not wave source",
            expression="trace,p -> kappa_min; not Box kappa = alpha trace",
            meaning="Trace response is non-inertial local relaxation, not scalar radiation.",
            status="CONSTRAINED",
            risk_if_violated="Breathing radiation or massless scalar tail.",
            missing="S_trace_effective and chi_kappa derivation.",
        ),
        ConstraintEntry(
            name="C4: transverse current only sources W_i",
            expression="source(W_i) = P_T j; P_L j excluded",
            meaning="Frame-dragging/vector response is sourced only by transverse current.",
            status="STRUCTURAL",
            risk_if_violated="Longitudinal/gauge current contaminates vector sector.",
            missing="Covariant current decomposition.",
        ),
        ConstraintEntry(
            name="C5: longitudinal current belongs to scalar continuity",
            expression="P_L j -> continuity/dot rho, not curl W",
            meaning="Longitudinal current updates density distribution rather than vector curl field.",
            status="DERIVED_REDUCED",
            risk_if_violated="Scalar/vector source mixing.",
            missing="Full dynamic source continuity closure.",
        ),
        ConstraintEntry(
            name="C6: TT stress remains trace-free tensor source",
            expression="source(h_TT) = P_TT S_ij; trace(S) excluded",
            meaning="Tensor radiation uses TT projection, not scalar trace.",
            status="STRUCTURAL",
            risk_if_violated="Trace stress double-counted as tensor radiation.",
            missing="TT source identity and coupling derivation.",
        ),
        ConstraintEntry(
            name="C7: scalar radiation source rejected",
            expression="source(A_rad ordinary massless) = 0",
            meaning="No ordinary long-range scalar radiation sector.",
            status="REJECTED",
            risk_if_violated="Observable breathing mode / scalar radiation.",
            missing="Parent mechanism proving rejection.",
        ),
        ConstraintEntry(
            name="C8: kappa relaxation cannot erase A",
            expression="Gamma_relax[A_mass_flux] = 0",
            meaning="Relaxation may restore trace imbalance but must not damp the A-sector mass field.",
            status="CONSTRAINED",
            risk_if_violated="Gravity mass flux disappears or is tuned by relaxation.",
            missing="Energy/vacuum balance identity.",
        ),
        ConstraintEntry(
            name="C9: boundary smoothing preserves exterior mass",
            expression="delta M_ext from kappa boundary smoothing = 0",
            meaning="Near-boundary kappa smoothing may not change total exterior A flux by hand.",
            status="CONSTRAINED",
            risk_if_violated="Surface smoothing changes measured mass.",
            missing="Interface law and matching theorem.",
        ),
        ConstraintEntry(
            name="C10: creation term excluded from ordinary closure",
            expression="Sigma_creation = 0 in ordinary closed gravity regime",
            meaning="Creation/exchange active-regime terms must not enter ordinary field equations by default.",
            status="CONSTRAINED",
            risk_if_violated="Nonconservative source breaks closure.",
            missing="Active-regime trigger conditions.",
        ),
    ]


def print_constraint(c: ConstraintEntry) -> None:
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
    mark = marks.get(c.status, "INFO")
    print()
    print("-" * 120)
    print(c.name)
    print("-" * 120)
    print(f"Expression: {c.expression}")
    print(f"Meaning: {c.meaning}")
    print(f"[{mark}] {c.name}: {c.status}")
    print(f"Risk if violated: {c.risk_if_violated}")
    print(f"Missing: {c.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: No-double-counting constraint problem")

    print("Question:")
    print()
    print("  Which overlaps between sources and sectors are forbidden or constrained?")
    print()
    print("Goal:")
    print()
    print("  turn the source ledger into explicit constraints")
    print()
    print("Discipline:")
    print()
    print("  one source may contribute to total stress-energy")
    print("  but it must not become multiple independent gravity sources")
    print("  unless a parent identity forces the split")

    with out.governance_assessments():
        out.line("no-double-counting problem posed", StatusMark.DEFER, "structural constraint")


def case_1_constraint_inventory(entries: List[ConstraintEntry]):
    header("Case 1: Constraint inventory")
    for entry in entries:
        print_constraint(entry)


def case_2_compact_table(entries: List[ConstraintEntry], out: ScriptOutput):
    header("Case 2: Compact constraint ledger")

    print("| Constraint | Expression | Status | Risk if violated |")
    print("|---|---|---|---|")
    for c in entries:
        print(
            "| "
            + c.name.replace("|", "/")
            + " | "
            + c.expression.replace("|", "/")
            + " | "
            + c.status
            + " | "
            + c.risk_if_violated.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact no-double-counting ledger produced", StatusMark.PASS, "inventory marker")


def case_3_status_counts(entries: List[ConstraintEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for c in entries:
        counts[c.status] = counts.get(c.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    with out.governance_assessments():
        out.line("constraint status count produced", StatusMark.PASS, "inventory marker")


def case_4_most_dangerous_violations(out: ScriptOutput):
    header("Case 4: Most dangerous violations")

    print("Most dangerous violations:")
    print()
    print("1. rho also sources long-range kappa.")
    print("2. pressure trace creates Box kappa scalar waves.")
    print("3. kappa smoothing changes exterior mass flux.")
    print("4. TT coupling is matched but claimed derived.")
    print("5. Sigma_creation enters ordinary closure.")
    print("6. recombination duplicates scalar spatial response.")
    print()
    print("These are the goblin traps.")

    with out.governance_assessments():
        out.line("dangerous violations identified", StatusMark.WARN, "open risk")


def case_5_parent_identity_requirements(out: ScriptOutput):
    header("Case 5: Parent identity requirements")

    print("The constraints require a parent identity that can explain:")
    print()
    print("  why rho sources A and not long-range kappa")
    print("  why trace shifts kappa_min but does not radiate")
    print("  why TT stress sources only TT radiation")
    print("  why transverse and longitudinal currents split cleanly")
    print("  why boundary smoothing preserves exterior mass")
    print("  why ordinary closed gravity has Sigma_creation = 0")
    print()
    print("Without that parent identity, these are safety constraints, not derivations.")

    with out.unresolved_obligations():
        out.line("parent identity for no-double-counting rules", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_no_double_counting_constraints.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_constraint_vs_evolution_split.py")
    print("   Separate constraint fields from propagating fields.")
    print()
    print("3. candidate_conservation_identity_requirements.py")
    print("   List the parent identities required to justify these constraints.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_constraint_vs_evolution_split.py")
    print()
    print("Reason:")
    print("  Source double-counting is controlled; next we must separate constraints from evolution.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("The current no-double-counting rule is:")
    print()
    print("  rho -> A, not long-range kappa")
    print("  trace -> kappa_min, not scalar wave")
    print("  j_T -> W_i, not scalar continuity")
    print("  TT stress -> h_ij^TT, not scalar trace")
    print("  relaxation -> vacuum restoration, not A damping")
    print()
    print("These are currently constraints, not full derivations.")
    print()
    print("Possible next artifact:")
    print("  candidate_no_double_counting_constraints.md")
    print()
    print("Possible next script:")
    print("  candidate_constraint_vs_evolution_split.py")


def record_governance(ns, entries: List[ConstraintEntry]) -> None:
    # CONSTRAINED entries -> ClaimRecord CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="ndc_rho_not_double_sourced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "C1: S_kappa[rho] = 0 as independent long-range scalar source. "
            "rho sources A; kappa may not carry a second rho-sourced 1/r field."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="ndc_exterior_kappa_charge_zero",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "C2: Q_kappa = integral S_kappa d^3x = 0. "
            "No massless exterior kappa monopole. Projection/boundary identity is missing."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="ndc_pressure_trace_shifts_minimum",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "C3: trace/pressure shifts kappa_min only; it must not source Box kappa = alpha trace. "
            "Trace response is non-inertial local relaxation, not scalar radiation."
        ),
    ))

    # STRUCTURAL -> CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="ndc_transverse_current_sources_W",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "C4: source(W_i) = P_T j; P_L j excluded. "
            "Frame-dragging/vector response is sourced only by transverse current. "
            "Covariant current decomposition is missing."
        ),
    ))

    # DERIVED_REDUCED -> HEURISTIC
    ns.record_claim(ClaimRecord(
        claim_id="ndc_longitudinal_current_scalar_continuity",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "C5: P_L j -> continuity/dot rho, not curl W. "
            "Longitudinal current updates density distribution, not vector curl field."
        ),
    ))

    # Missing parent identity for all constraints -> ProofObligationRecord
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_parent_identity_for_no_double_counting",
        script_id=SCRIPT_ID,
        title="Derive parent identity enforcing no-double-counting rules",
        status=ObligationStatus.OPEN,
        description=(
            "The no-double-counting constraints C1-C10 require a parent identity explaining "
            "why rho sources only A, why trace shifts kappa_min without radiating, "
            "why TT stress sources only TT radiation, why currents split cleanly, "
            "why boundary smoothing preserves exterior mass, and why Sigma_creation=0 in "
            "ordinary closed gravity. Without this, they are safety constraints, not derivations."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_Q_kappa_zero_boundary_identity",
        script_id=SCRIPT_ID,
        title="Derive Q_kappa=0 boundary identity",
        status=ObligationStatus.OPEN,
        description=(
            "A projection/boundary identity proving Q_kappa = integral S_kappa d^3x = 0 "
            "is required to prevent exterior kappa ~ 1/r scalar gravity."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_active_regime_trigger_conditions",
        script_id=SCRIPT_ID,
        title="Derive active-regime trigger conditions for Sigma_creation",
        status=ObligationStatus.OPEN,
        description=(
            "Active-regime conditions that gate Sigma_creation must be derived. "
            "In ordinary closed gravity Sigma_creation = 0 must follow from the trigger, "
            "not be assumed."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="no_double_counting_constraints_marker",
        inputs=[],
        output=sp.Symbol("no_double_counting_constraints_built"),
        method="no_double_counting_constraints_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate No-Double-Counting Constraints")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_constraints()
    case_1_constraint_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_most_dangerous_violations(out)
    case_5_parent_identity_requirements(out)
    case_6_next_tests(out)
    final_interpretation()
    out.print_summary()
    with archive:
        record_governance(ns, entries)
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
