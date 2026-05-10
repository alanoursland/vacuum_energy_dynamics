# Candidate conservation identity requirements
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   REQUIREMENTS
#
# Purpose
# -------
# The constraint-versus-evolution split established:
#
#   A is a constraint, not scalar radiation.
#   B is a reduced gauge-conditioned companion.
#   W_i is a transverse vector response, not free radiation.
#   h_ij^TT is true propagating radiation.
#   kappa is non-inertial trace relaxation, not breathing radiation.
#   A_rad is rejected ordinary scalar radiation.
#
# The next closure gap is the parent identity that enforces this split.
#
# This script lists the identities required for closure:
#
#   scalar constraint propagation,
#   current decomposition,
#   TT source conservation,
#   kappa non-radiative trace relaxation,
#   boundary mass preservation,
#   exclusion of Sigma_creation in ordinary closure,
#   energy/source accounting.
#
# This is a requirements script, not a derivation.

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
class IdentityRequirement:
    name: str
    required_identity: str
    what_it_enforces: str
    current_status: str
    failure_if_missing: str
    next_needed: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="constraint_vs_evolution_split_generated_marker",
        upstream_script_id="11_field_equation_closure__candidate_constraint_vs_evolution_split_generated",
        upstream_derivation_id="constraint_vs_evolution_split_generated_marker",
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


def build_requirements() -> List[IdentityRequirement]:
    return [
        IdentityRequirement(
            name="I1: scalar constraint propagation",
            required_identity="time evolution of A constraint is compatible with continuity of rho",
            what_it_enforces="A remains a constraint rather than scalar radiation.",
            current_status="UNFINISHED",
            failure_if_missing="A may need a wave equation or violate source conservation.",
            next_needed="derive reduced continuity-compatible A update law.",
        ),
        IdentityRequirement(
            name="I2: mass flux preservation",
            required_identity="exterior A flux / M_ext is invariant under kappa boundary relaxation",
            what_it_enforces="kappa smoothing cannot change measured exterior mass.",
            current_status="CONSTRAINED",
            failure_if_missing="boundary smoothing tunes gravity by hand.",
            next_needed="boundary/interface mass theorem.",
        ),
        IdentityRequirement(
            name="I3: current decomposition identity",
            required_identity="j = P_T j + P_L j with W_i sourced only by P_T j",
            what_it_enforces="transverse current sources W_i; longitudinal current remains scalar continuity.",
            current_status="STRUCTURAL",
            failure_if_missing="vector and scalar sectors double-count current.",
            next_needed="covariant current split or gauge-fixed reduced proof.",
        ),
        IdentityRequirement(
            name="I4: TT source conservation",
            required_identity="TT projection of stress source is compatible with conserved total stress-energy",
            what_it_enforces="h_ij^TT carries tensor radiation without trace contamination.",
            current_status="STRUCTURAL",
            failure_if_missing="tensor radiation source may be imported from GR or double-count trace.",
            next_needed="derive TT source from vacuum stress/shear identity.",
        ),
        IdentityRequirement(
            name="I5: kappa non-radiative trace identity",
            required_identity="trace/pressure shifts kappa_min but does not source Box kappa",
            what_it_enforces="kappa relaxes locally and does not radiate breathing modes.",
            current_status="CONSTRAINED",
            failure_if_missing="scalar breathing radiation or hidden kappa wave.",
            next_needed="derive kappa_min source and first-order relaxation from vacuum minimum.",
        ),
        IdentityRequirement(
            name="I6: scalar radiation exclusion",
            required_identity="source(A_rad ordinary massless) = 0 in ordinary closed regime",
            what_it_enforces="ordinary long-range radiation is TT-only.",
            current_status="CONSTRAINED",
            failure_if_missing="unwanted scalar radiation channel.",
            next_needed="parent scalar constraint/radiation split.",
        ),
        IdentityRequirement(
            name="I7: ordinary closure excludes creation",
            required_identity="Sigma_creation = 0 outside active creation/exchange regimes",
            what_it_enforces="ordinary gravity remains conservative/closed.",
            current_status="CONSTRAINED",
            failure_if_missing="nonconservative field equations.",
            next_needed="active-regime trigger and conservation accounting.",
        ),
        IdentityRequirement(
            name="I8: relaxation energy accounting",
            required_identity="Gamma_relax transfers imbalance into vacuum configuration, not energy loss",
            what_it_enforces="kappa relaxation is exchange/restoration, not dissipation from total system.",
            current_status="STRUCTURAL",
            failure_if_missing="cosmetic damping or energy disappearance.",
            next_needed="vacuum configuration energy variable.",
        ),
        IdentityRequirement(
            name="I9: metric recombination compatibility",
            required_identity="sector recombination preserves source split and avoids duplicate scalar response",
            what_it_enforces="A, W_i, h_TT, and kappa combine without double-counting.",
            current_status="UNFINISHED",
            failure_if_missing="GR metric imported by hand or scalar trace duplicated.",
            next_needed="recombination identity / parent metric map.",
        ),
        IdentityRequirement(
            name="I10: Bianchi-like closure target",
            required_identity="parent divergence identity implies source conservation and sector constraints",
            what_it_enforces="full field system is compatible with conservation.",
            current_status="MISSING",
            failure_if_missing="theory remains a sector ledger, not a closed field equation system.",
            next_needed="derive or state candidate parent identity.",
        ),
    ]


def print_requirement(req: IdentityRequirement) -> None:
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
    mark = marks.get(req.current_status, "INFO")
    print()
    print("-" * 120)
    print(req.name)
    print("-" * 120)
    print(f"Required identity: {req.required_identity}")
    print(f"Enforces: {req.what_it_enforces}")
    print(f"[{mark}] {req.name}: {req.current_status}")
    print(f"Failure if missing: {req.failure_if_missing}")
    print(f"Next needed: {req.next_needed}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Conservation identity requirements problem")

    print("Question:")
    print()
    print("  What parent identities are required to justify the constraint/evolution split?")
    print()
    print("Goal:")
    print()
    print("  make the missing identities explicit")
    print()
    print("Discipline:")
    print()
    print("  do not claim closure just because the sector split is organized")
    print("  identify what must be derived before the system is closed")

    with out.unresolved_obligations():
        out.line("conservation identity requirements", StatusMark.OBLIGATION,
                 "system not closed; parent identities required")


def case_1_requirement_inventory(entries: List[IdentityRequirement]):
    header("Case 1: Identity requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[IdentityRequirement], out: ScriptOutput):
    header("Case 2: Compact identity ledger")

    print("| Identity | Enforces | Status | Failure if missing |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.what_it_enforces.replace("|", "/")
            + " | "
            + e.current_status
            + " | "
            + e.failure_if_missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact identity ledger produced", StatusMark.PASS, "inventory marker")


def case_3_status_counts(entries: List[IdentityRequirement], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.current_status] = counts.get(e.current_status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Most identities are constrained or structural requirements.")
    print("  The Bianchi-like closure identity remains missing.")

    with out.governance_assessments():
        out.line("identity status count produced", StatusMark.PASS, "inventory marker")


def case_4_minimal_parent_identity_template(out: ScriptOutput):
    header("Case 4: Minimal parent identity template")

    print("A minimal parent identity must look something like:")
    print()
    print("  divergence(parent field equation) = source balance identity")
    print()
    print("and in reduced sector language it must imply:")
    print()
    print("  A constraint propagation")
    print("  W_i transverse current sourcing")
    print("  h_ij^TT TT radiation sourcing")
    print("  kappa trace relaxation without scalar radiation")
    print("  exterior mass preservation")
    print("  ordinary Sigma_creation = 0")
    print()
    print("This is a requirement template, not a derivation.")

    with out.unresolved_obligations():
        out.line("minimal parent identity template", StatusMark.OBLIGATION,
                 "template only; parent identity not derived")


def case_5_hardest_requirements(out: ScriptOutput):
    header("Case 5: Hardest requirements")

    print("Hardest requirements:")
    print()
    print("1. Bianchi-like closure target.")
    print("2. Metric recombination compatibility.")
    print("3. Kappa non-radiative trace identity.")
    print("4. Tensor coupling/source conservation.")
    print("5. Boundary mass preservation.")
    print()
    print("These are where the reconstruction can still fail.")

    with out.governance_assessments():
        out.line("hardest requirements identified", StatusMark.WARN, "open risk")


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_conservation_identity_requirements.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_gr_limit_recovery_audit.py")
    print("   Audit where GR recovery is derived versus matched.")
    print()
    print("3. candidate_parent_identity_template.py")
    print("   Try to write an explicit candidate parent identity.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_gr_limit_recovery_audit.py")
    print()
    print("Reason:")
    print("  Before inventing the parent identity, audit which GR limits are actually derived.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("The sector split is disciplined but not closed.")
    print()
    print("Closure requires a parent identity that explains:")
    print("  constraint propagation")
    print("  source conservation")
    print("  TT-only radiation")
    print("  non-radiative kappa trace relaxation")
    print("  mass preservation")
    print("  ordinary exclusion of Sigma_creation")
    print()
    print("Possible next artifact:")
    print("  candidate_conservation_identity_requirements.md")
    print()
    print("Possible next script:")
    print("  candidate_gr_limit_recovery_audit.py")


def record_governance(ns, entries: List[IdentityRequirement]) -> None:
    # UNFINISHED -> OPEN obligation
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_I1_scalar_constraint_propagation",
        script_id=SCRIPT_ID,
        title="Derive scalar constraint propagation identity (I1)",
        status=ObligationStatus.OPEN,
        description=(
            "Time evolution of the A constraint must be shown compatible with continuity of rho. "
            "Without this A may need a wave equation or violate source conservation."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_I9_metric_recombination_compatibility",
        script_id=SCRIPT_ID,
        title="Derive metric recombination compatibility identity (I9)",
        status=ObligationStatus.OPEN,
        description=(
            "Sector recombination must be shown to preserve source split and avoid duplicate "
            "scalar response. Without this GR metric is imported by hand or scalar trace is duplicated."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_I10_bianchi_like_closure",
        script_id=SCRIPT_ID,
        title="Derive Bianchi-like closure identity (I10)",
        status=ObligationStatus.OPEN,
        description=(
            "A parent divergence identity must be derived that implies source conservation "
            "and sector constraints. Without this the theory remains a sector ledger, "
            "not a closed field equation system."
        ),
    ))

    # CONSTRAINED -> ClaimRecord CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="req_I2_mass_flux_preservation",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "I2: exterior A flux / M_ext must be invariant under kappa boundary relaxation. "
            "Boundary/interface mass theorem is not yet derived."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="req_I5_kappa_non_radiative",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "I5: trace/pressure shifts kappa_min but does not source Box kappa. "
            "kappa must relax locally and not radiate breathing modes."
        ),
    ))

    # STRUCTURAL -> CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="req_I3_current_decomposition",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "I3: j = P_T j + P_L j with W_i sourced only by P_T j. "
            "A covariant current split or gauge-fixed reduced proof is missing."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="conservation_identity_requirements_generated_marker",
        inputs=[],
        output=sp.Symbol("conservation_identity_requirements_generated"),
        method="conservation_identity_requirements_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate Conservation Identity Requirements")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_minimal_parent_identity_template(out)
    case_5_hardest_requirements(out)
    case_6_next_tests(out)
    final_interpretation()
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
