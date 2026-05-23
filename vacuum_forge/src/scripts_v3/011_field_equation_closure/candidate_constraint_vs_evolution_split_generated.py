# Candidate constraint versus evolution split
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# The no-double-counting constraints identified which sources must not be
# counted twice.
#
# The next closure question is:
#
#   which fields are constraints?
#   which fields relax?
#   which fields propagate?
#
# This script classifies:
#
#   A       -> scalar constraint / monopole field
#   W_i     -> transverse vector constraint / stationary response, possibly retarded in dynamics
#   h_TT    -> true propagating tensor radiation
#   kappa   -> non-inertial trace relaxation / constrained variable
#   A_rad   -> rejected ordinary scalar radiation
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
class DynamicsEntry:
    field: str
    sector: str
    classification: str
    schematic_equation: str
    propagates: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="no_double_counting_constraints_marker",
        upstream_script_id="11_field_equation_closure__candidate_no_double_counting_constraints",
        upstream_derivation_id="no_double_counting_constraints_marker",
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


def build_entries() -> List[DynamicsEntry]:
    return [
        DynamicsEntry(
            field="A",
            sector="scalar monopole / areal flux",
            classification="constraint / elliptic-like scalar sector",
            schematic_equation="Delta_areal A = 8*pi*G*rho/c^2",
            propagates="No ordinary long-range scalar radiation; static/constraint field.",
            status="DERIVED_REDUCED",
            risk="Turning static scalar constraint into a propagating scalar wave.",
            missing="Full nonlinear nonspherical constraint propagation.",
        ),
        DynamicsEntry(
            field="B",
            sector="radial reciprocal scalar metric piece",
            classification="gauge-conditioned companion to A in exterior",
            schematic_equation="AB = exp(2*kappa); exterior kappa=0 -> B=1/A",
            propagates="No independent propagation in current reduced exterior.",
            status="DERIVED_REDUCED",
            risk="Treating gauge relation as independent dynamics.",
            missing="Covariant gauge/physical split.",
        ),
        DynamicsEntry(
            field="W_i",
            sector="transverse vector / frame dragging",
            classification="transverse vector constraint in stationary limit; possible retarded response dynamically",
            schematic_equation="curl curl W = -(alpha_W/(2K_c)) j_T",
            propagates="Not currently a free radiation sector; source-tied vector response.",
            status="STRUCTURAL",
            risk="Importing electromagnetic-like vector waves or GR shift dynamics by hand.",
            missing="Dynamic propagation/retardation law and normalization.",
        ),
        DynamicsEntry(
            field="h_ij^TT",
            sector="tensor radiation",
            classification="true propagating radiative degree of freedom",
            schematic_equation="Box h_ij^TT = -C_T S_ij^TT",
            propagates="Yes: ordinary long-range gravitational radiation.",
            status="STRUCTURAL",
            risk="Correct form but coefficient/source identity matched to GR.",
            missing="C_T and action stiffness derivation.",
        ),
        DynamicsEntry(
            field="kappa",
            sector="trace / volume relaxation",
            classification="non-inertial relaxation / constrained trace response",
            schematic_equation="dot kappa = -mu_kappa K_kappa (kappa-kappa_min)",
            propagates="No: no independent momentum channel; no ordinary breathing wave.",
            status="STRUCTURAL",
            risk="Becoming a hidden scalar wave or repair knob.",
            missing="K_kappa, mu_kappa, chi_kappa, S_trace_effective, covariant origin.",
        ),
        DynamicsEntry(
            field="A_rad",
            sector="scalar radiation hazard",
            classification="rejected ordinary massless scalar radiation sector",
            schematic_equation="source(A_rad ordinary massless) = 0",
            propagates="No; rejected unless separately derived and controlled.",
            status="REJECTED",
            risk="Breathing/scalar radiation contradicts safety constraints.",
            missing="Parent identity proving absence/suppression.",
        ),
        DynamicsEntry(
            field="Sigma_creation",
            sector="active regimes",
            classification="excluded from ordinary closed-gravity evolution",
            schematic_equation="Sigma_creation = 0 in ordinary closed regime",
            propagates="Not a field; source/regime switch.",
            status="CONSTRAINED",
            risk="Nonconservative source contaminates ordinary closure.",
            missing="Active-regime trigger and accounting.",
        ),
        DynamicsEntry(
            field="Gamma_relax",
            sector="vacuum relaxation / kappa equilibration",
            classification="energy-transfer / restoration term, not propagating mode",
            schematic_equation="Gamma_relax acts on trace imbalance, not A_mass_flux",
            propagates="No; local restoration/accounting term.",
            status="STRUCTURAL",
            risk="Cosmetic damping or energy disappearance.",
            missing="Vacuum energy destination / parent balance.",
        ),
    ]


def print_entry(e: DynamicsEntry) -> None:
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
    print(f"Field: {e.field}")
    print("-" * 120)
    print(f"Sector: {e.sector}")
    print(f"Classification: {e.classification}")
    print(f"Schematic equation: {e.schematic_equation}")
    print(f"Propagates? {e.propagates}")
    print(f"[{mark}] {e.field}: {e.status}")
    print(f"Risk: {e.risk}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Constraint versus evolution split problem")

    print("Question:")
    print()
    print("  Which fields are constraints, which relax, and which propagate?")
    print()
    print("Goal:")
    print()
    print("  avoid accidentally turning constraint sectors into radiative fields")
    print()
    print("Discipline:")
    print()
    print("  A is not scalar radiation")
    print("  kappa is not breathing radiation")
    print("  W_i is not automatically a free vector wave")
    print("  h_ij^TT is the true long-range radiation sector")

    with out.governance_assessments():
        out.line("constraint/evolution split problem posed", StatusMark.DEFER,
                 "structural constraint")


def case_1_dynamics_inventory(entries: List[DynamicsEntry]):
    header("Case 1: Dynamics inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[DynamicsEntry], out: ScriptOutput):
    header("Case 2: Compact dynamics ledger")

    print("| Field | Classification | Propagates? | Status |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.field.replace("|", "/")
            + " | "
            + e.classification.replace("|", "/")
            + " | "
            + e.propagates.replace("|", "/")
            + " | "
            + e.status
            + " |"
        )

    with out.governance_assessments():
        out.line("compact dynamics ledger produced", StatusMark.PASS, "inventory marker")


def case_3_true_radiation_rule(out: ScriptOutput):
    header("Case 3: True radiation rule")

    print("Current radiation rule:")
    print()
    print("  ordinary long-range gravitational radiation is TT-only.")
    print()
    print("Allowed:")
    print("  h_ij^TT propagates.")
    print()
    print("Constrained/rejected:")
    print("  A_rad ordinary scalar radiation is rejected.")
    print("  kappa breathing radiation is rejected.")
    print("  W_i free vector radiation is not currently derived.")
    print()
    print("This rule can be changed only by a separate derivation and observational control.")

    with out.governance_assessments():
        out.line("TT-only ordinary radiation rule stated", StatusMark.DEFER,
                 "structural constraint")


def case_4_constraint_fields(out: ScriptOutput):
    header("Case 4: Constraint fields")

    print("Constraint-like fields:")
    print()
    print("  A:")
    print("    scalar mass/monopole constraint")
    print()
    print("  B:")
    print("    reduced gauge-conditioned reciprocal companion to A")
    print()
    print("  W_i:")
    print("    transverse vector response in stationary/current sector")
    print()
    print("  kappa:")
    print("    non-inertial trace/volume relaxation constraint")
    print()
    print("These may have time-dependent source response, but they are not currently")
    print("ordinary free radiative degrees of freedom.")

    with out.governance_assessments():
        out.line("constraint-like fields listed", StatusMark.DEFER, "structural constraint")


def case_5_evolution_fields(out: ScriptOutput):
    header("Case 5: Evolution fields")

    print("Evolving/radiating fields:")
    print()
    print("  h_ij^TT:")
    print("    propagating tensor radiation")
    print()
    print("Possibly dynamic but not yet radiative:")
    print("  W_i:")
    print("    may require retardation/dynamic source response")
    print()
    print("  kappa:")
    print("    first-order relaxation toward local minimum")
    print()
    print("Rejected as ordinary radiative fields:")
    print("  A_rad")
    print("  kappa breathing wave")

    with out.governance_assessments():
        out.line("evolution fields classified", StatusMark.DEFER, "structural")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Constraint/evolution split fails if:")
    print()
    print("1. A is promoted to a free scalar radiation field.")
    print("2. kappa gains a second-order Box equation and momentum channel.")
    print("3. W_i is treated as a free vector radiation field without derivation.")
    print("4. h_ij^TT coupling is copied from GR while claimed derived.")
    print("5. Gamma_relax hides energy loss rather than vacuum exchange.")
    print("6. Sigma_creation appears in ordinary closed gravity.")
    print("7. constraint propagation is not compatible with source conservation.")

    with out.governance_assessments():
        out.line("constraint/evolution failure controls stated", StatusMark.WARN,
                 "open risk")


def case_7_parent_identity_requirements(out: ScriptOutput):
    header("Case 7: Parent identity requirements")

    print("The parent identity must explain:")
    print()
    print("  how constraints propagate consistently")
    print("  why TT modes alone carry ordinary radiation")
    print("  why scalar trace relaxes but does not radiate")
    print("  why vector current response is transverse")
    print("  how energy/source conservation is maintained")
    print()
    print("Without this, the split is disciplined but not derived.")

    with out.unresolved_obligations():
        out.line("parent identity for constraint/evolution split", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_constraint_vs_evolution_split.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_conservation_identity_requirements.py")
    print("   List the parent identities needed to justify the constraints.")
    print()
    print("3. candidate_gr_limit_recovery_audit.py")
    print("   Audit where GR recovery is derived versus matched.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_conservation_identity_requirements.py")
    print()
    print("Reason:")
    print("  The split is now clear; the next gap is the identity that enforces it.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("Current split:")
    print()
    print("  A: constraint")
    print("  B: reduced gauge-conditioned companion")
    print("  W_i: transverse vector response, not free radiation")
    print("  h_ij^TT: true propagating radiation")
    print("  kappa: non-inertial trace relaxation, not breathing radiation")
    print("  A_rad: rejected ordinary scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_constraint_vs_evolution_split.md")
    print()
    print("Possible next script:")
    print("  candidate_conservation_identity_requirements.py")


def record_governance(ns, entries: List[DynamicsEntry]) -> None:
    # DERIVED_REDUCED -> HEURISTIC
    ns.record_claim(ClaimRecord(
        claim_id="dyn_A_constraint_derived_reduced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "A is a scalar constraint/elliptic-like sector. "
            "Delta_areal A = 8*pi*G*rho/c^2 is derived in the reduced static spherical case. "
            "A is not a propagating scalar radiation field."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="dyn_B_gauge_conditioned_derived_reduced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "B is a gauge-conditioned companion to A in the reduced areal exterior. "
            "AB = exp(2*kappa); exterior kappa=0 -> B=1/A. No independent propagation."
        ),
    ))

    # STRUCTURAL -> CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="dyn_h_TT_true_propagating",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "h_ij^TT is the true propagating tensor radiation sector. "
            "Box h_ij^TT = -C_T S_ij^TT. C_T and action stiffness are not yet derived."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="dyn_kappa_non_inertial_relaxation",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "kappa is a non-inertial relaxation / constrained trace response. "
            "dot kappa = -mu_kappa K_kappa (kappa-kappa_min). "
            "No independent momentum channel. No ordinary breathing wave."
        ),
    ))

    # TT-only radiation rule -> PROVISIONAL_CONVENTION (usable as explicit convention)
    ns.record_claim(ClaimRecord(
        claim_id="dyn_TT_only_radiation_rule",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "Ordinary long-range gravitational radiation is TT-only. "
            "A_rad ordinary scalar radiation and kappa breathing radiation are rejected. "
            "W_i free vector radiation is not currently derived. "
            "This rule may be changed only by a separate derivation and observational control."
        ),
    ))

    # Parent identity needed -> OPEN
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_parent_identity_for_constraint_evolution_split",
        script_id=SCRIPT_ID,
        title="Derive parent identity enforcing constraint/evolution split",
        status=ObligationStatus.OPEN,
        description=(
            "A parent identity is required to explain how constraints propagate consistently, "
            "why TT modes alone carry ordinary radiation, why scalar trace relaxes but does "
            "not radiate, why vector current response is transverse, and how energy/source "
            "conservation is maintained. Without this, the split is disciplined but not derived."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="constraint_vs_evolution_split_generated_marker",
        inputs=[],
        output=sp.Symbol("constraint_vs_evolution_split_generated"),
        method="constraint_vs_evolution_split_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate Constraint Versus Evolution Split")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_dynamics_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_true_radiation_rule(out)
    case_4_constraint_fields(out)
    case_5_evolution_fields(out)
    case_6_failure_controls(out)
    case_7_parent_identity_requirements(out)
    case_8_next_tests(out)
    final_interpretation()
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
