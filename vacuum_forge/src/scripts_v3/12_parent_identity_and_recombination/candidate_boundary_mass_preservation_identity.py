# Candidate boundary mass preservation identity
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# The kappa covariant relaxation audit found:
#
#   kappa relaxation is only safe if boundary/exterior mass preservation is enforced.
#
# This script asks:
#
#   Can kappa / boundary relaxation modify local trace or volume matching
#   without changing the exterior A-sector mass flux?
#
# It does not prove the theorem.
# It builds the required boundary mass preservation identity.
#
# Key target:
#
#   delta M_ext | kappa relaxation = 0
#
# and:
#
#   F_kappa(R+) = 0
#
# This is a requirement audit, not a derivation.

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


@dataclass
class BoundaryRequirement:
    name: str
    requirement: str
    candidate_form: str
    forbidden_form: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_covariant_relaxation_requirement_marker",
        upstream_script_id="12_parent_identity_and_recombination__candidate_kappa_covariant_relaxation_requirement",
        upstream_derivation_id="kappa_covariant_relaxation_requirement_marker",
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


def build_requirements() -> List[BoundaryRequirement]:
    return [
        BoundaryRequirement(
            name="B1: exterior mass is A-sector flux",
            requirement="Exterior mass must be defined by the A-sector flux / exterior 1/r coefficient.",
            candidate_form="A_ext = 1 - 2*G*M_ext/(c^2*r)",
            forbidden_form="M_ext adjusted by kappa boundary smoothing",
            status="DERIVED_REDUCED",
            risk="Measured mass becomes tunable by interface choice.",
            missing="Parent flux-charge definition.",
        ),
        BoundaryRequirement(
            name="B2: kappa boundary relaxation preserves M_ext",
            requirement="Kappa relaxation may change local trace/volume matching but not exterior mass.",
            candidate_form="delta M_ext|kappa_relaxation = 0",
            forbidden_form="delta M_ext != 0 from smoothing or kappa interface adjustment",
            status="REQUIRED",
            risk="Boundary smoothing tunes measured gravity.",
            missing="Boundary mass preservation theorem.",
        ),
        BoundaryRequirement(
            name="B3: exterior kappa charge vanishes",
            requirement="Kappa must not create an exterior 1/r scalar tail.",
            candidate_form="Q_kappa = integral S_kappa d^3x = 0",
            forbidden_form="kappa_ext ~ q_kappa/r",
            status="CONSTRAINED",
            risk="Second exterior scalar charge.",
            missing="Projection or boundary cancellation identity.",
        ),
        BoundaryRequirement(
            name="B4: exterior kappa flux vanishes",
            requirement="No kappa flux may cross into exterior vacuum as scalar charge.",
            candidate_form="F_kappa(R+) = 4*pi*R^2*kappa_prime(R+) = 0",
            forbidden_form="F_kappa(R+) != 0",
            status="CONSTRAINED",
            risk="Exterior kappa tail and scalar double-counting.",
            missing="Interface law enforcing zero flux.",
        ),
        BoundaryRequirement(
            name="B5: exterior vacuum fixed point",
            requirement="Outside ordinary matter, kappa_min=0 and kappa relaxes to zero.",
            candidate_form="S_trace_effective=0 -> kappa_min=0 -> kappa -> 0",
            forbidden_form="nonzero exterior kappa attractor",
            status="CONSTRAINED",
            risk="Persistent exterior scalar state.",
            missing="Exterior vacuum relaxation proof.",
        ),
        BoundaryRequirement(
            name="B6: A flux and kappa flux are independent charges",
            requirement="Kappa interface conditions must not modify the A-sector Gauss/flux charge.",
            candidate_form="delta integral grad A dot dS | kappa = 0",
            forbidden_form="kappa boundary condition changes integral grad A dot dS",
            status="REQUIRED",
            risk="Scalar mass double-counting through boundary coupling.",
            missing="Parent separation of A flux and kappa boundary condition.",
        ),
        BoundaryRequirement(
            name="B7: joint-minimum smoothing is diagnostic only",
            requirement="Near-boundary smoothing may be modeled, but cannot be used to claim mass change.",
            candidate_form="f_joint diagnostics with fixed exterior M_ext",
            forbidden_form="joint-minimum fit changes exterior mass coefficient",
            status="CONSTRAINED",
            risk="Near-boundary deviation overclaim or mass retuning.",
            missing="Weights, sigma, recombination, observable map.",
        ),
        BoundaryRequirement(
            name="B8: source compactness condition",
            requirement="Kappa relaxation support must be compact or compensated for ordinary isolated bodies.",
            candidate_form="support(S_kappa_eff) compact and/or integral S_kappa_eff d^3x = 0",
            forbidden_form="uncompensated trace source leaking into exterior",
            status="STRUCTURAL",
            risk="Long-range kappa scalar field.",
            missing="Definition of S_kappa_eff and compensation law.",
        ),
        BoundaryRequirement(
            name="B9: recombination preserves exterior Schwarzschild",
            requirement="Metric recombination must preserve exterior A/B result when kappa=0.",
            candidate_form="kappa_ext=0 -> recombination gives exterior Schwarzschild reduced form",
            forbidden_form="recombination reintroduces scalar trace outside",
            status="REQUIRED",
            risk="Silent GR import or scalar double-counting.",
            missing="P_recombination identity.",
        ),
        BoundaryRequirement(
            name="B10: relaxation energy does not alter M_ext by disappearance",
            requirement="Energy moved by Gamma_relax must be accounted without changing exterior mass incorrectly.",
            candidate_form="Delta E_relax -> Delta E_vac_config with total exterior charge preserved",
            forbidden_form="energy damping changes mass without source accounting",
            status="MISSING",
            risk="Energy nonconservation or hidden mass tuning.",
            missing="Vacuum configuration energy balance.",
        ),
    ]


def print_requirement(b: BoundaryRequirement) -> None:
    print()
    print("-" * 120)
    print(b.name)
    print("-" * 120)
    print(f"Requirement: {b.requirement}")
    print(f"Candidate form: {b.candidate_form}")
    print(f"Forbidden form: {b.forbidden_form}")
    print(f"[INFO] {b.name}: {b.status}")
    print(f"Risk: {b.risk}")
    print(f"Missing: {b.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Boundary mass preservation problem")

    print("Question:")
    print()
    print("  Can kappa/boundary relaxation occur without changing exterior mass?")
    print()
    print("Goal:")
    print()
    print("  formalize the boundary mass preservation requirement")
    print()
    print("Discipline:")
    print()
    print("  exterior mass belongs to A-sector flux")
    print("  kappa cannot add a second exterior scalar charge")
    print("  boundary smoothing cannot tune measured gravity")
    print("  near-boundary diagnostics are not predictions yet")

    with out.unresolved_obligations():
        out.line("boundary mass preservation problem posed", StatusMark.OBLIGATION, "boundary mass preservation theorem required")


def case_1_requirement_inventory(entries: List[BoundaryRequirement]):
    header("Case 1: Boundary requirement inventory")
    for entry in entries:
        print_requirement(entry)


def case_2_compact_table(entries: List[BoundaryRequirement], out: ScriptOutput):
    header("Case 2: Compact boundary ledger")

    print("| Requirement | Candidate form | Forbidden form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.forbidden_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact boundary ledger produced", StatusMark.INFO, "10 boundary requirements recorded")


def case_3_status_counts(entries: List[BoundaryRequirement], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Exterior A mass is reduced-derived.")
    print("  Boundary preservation is required but not proven.")
    print("  Relaxation energy accounting remains missing.")

    with out.governance_assessments():
        out.line("boundary status count produced", StatusMark.INFO, str(counts))


def case_4_candidate_boundary_identity(out: ScriptOutput):
    header("Case 4: Candidate boundary identity")

    print("Candidate boundary preservation identity:")
    print()
    print("  delta M_ext|kappa_relaxation = 0")
    print()
    print("with:")
    print()
    print("  M_ext proportional to exterior A flux")
    print("  F_kappa(R+) = 0")
    print("  Q_kappa = 0")
    print("  kappa_ext -> 0")
    print()
    print("Equivalent reduced reading:")
    print()
    print("  kappa can smooth/relax local trace-volume matching,")
    print("  but it cannot change the coefficient of 1/r in A_ext.")
    print()
    print("This is currently a requirement, not a theorem.")

    with out.unresolved_obligations():
        out.line("candidate boundary identity stated", StatusMark.OBLIGATION, "boundary mass preservation theorem not yet proved")


def case_5_failure_controls(out: ScriptOutput):
    header("Case 5: Failure controls")

    print("Boundary mass preservation fails if:")
    print()
    print("1. Kappa smoothing changes M_ext.")
    print("2. F_kappa(R+) is nonzero.")
    print("3. Q_kappa is nonzero.")
    print("4. Exterior kappa has a nonzero attractor.")
    print("5. A flux and kappa flux mix without parent identity.")
    print("6. Near-boundary diagnostics are advertised as measured predictions.")
    print("7. Relaxation energy disappears or changes exterior mass without accounting.")

    with out.governance_assessments():
        out.line("boundary failure controls stated", StatusMark.DEFER, "failure controls policy-guarded")


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_boundary_mass_preservation_identity.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_recombination_without_double_counting.py")
    print("   Try a disciplined recombination map.")
    print()
    print("3. candidate_relaxation_energy_accounting_identity.py")
    print("   Define the energy destination for Gamma_relax.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_recombination_without_double_counting.py")
    print()
    print("Reason:")
    print("  Boundary mass is protected by requirements; now recombination must avoid reintroducing scalar double-counting.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "recombination script is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("Boundary/kappa relaxation can remain safe only if:")
    print()
    print("  exterior mass is A-sector flux")
    print("  delta M_ext from kappa relaxation is zero")
    print("  Q_kappa is zero")
    print("  F_kappa(R+) is zero")
    print("  exterior kappa relaxes to zero")
    print("  recombination preserves exterior Schwarzschild")
    print("  relaxation energy is accounted")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_mass_preservation_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_recombination_without_double_counting.py")


def main():
    header("Candidate Boundary Mass Preservation Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_requirements()
    case_1_requirement_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_boundary_identity(out)
    case_5_failure_controls(out)
    case_6_next_tests(out)
    final_interpretation()

    # Proof obligations for boundary mass preservation
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_mass_preservation_theorem_B2",
        script_id=SCRIPT_ID,
        title="Derive boundary mass preservation theorem: delta M_ext|kappa_relaxation = 0 (B2)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that kappa relaxation can modify local trace/volume matching "
            "without changing the exterior A-sector mass flux. "
            "This is the key theorem required for kappa boundary safety."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_flux_neutrality_boundary_B4",
        script_id=SCRIPT_ID,
        title="Derive interface law enforcing F_kappa(R+) = 0 (B4)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that no kappa flux crosses into exterior vacuum as scalar charge. "
            "F_kappa(R+) = 4*pi*R^2*kappa_prime(R+) = 0 must follow from the parent identity."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_flux_kappa_flux_independence_B6",
        script_id=SCRIPT_ID,
        title="Derive parent separation of A flux and kappa boundary condition (B6)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that kappa interface conditions do not modify the A-sector Gauss/flux charge. "
            "delta integral(grad A dot dS)|kappa = 0 must be established from the parent identity."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_recombination_exterior_schwarzschild_B9",
        script_id=SCRIPT_ID,
        title="Derive P_recombination preserving exterior Schwarzschild when kappa=0 (B9)",
        status=ObligationStatus.OPEN,
        description=(
            "Metric recombination must preserve exterior A/B result when kappa=0. "
            "kappa_ext=0 must give the exterior Schwarzschild reduced form without "
            "reintroducing scalar trace outside."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_relaxation_energy_vac_config_balance_B10",
        script_id=SCRIPT_ID,
        title="Derive vacuum configuration energy balance for Gamma_relax (B10)",
        status=ObligationStatus.OPEN,
        description=(
            "Energy moved by Gamma_relax must be accounted as Delta E_vac_config "
            "with total exterior charge preserved. This requires defining E_vac_config."
        ),
    ))

    # Policy claim: near-boundary smoothing is diagnostic only
    ns.record_claim(ClaimRecord(
        claim_id="near_boundary_smoothing_diagnostic_only_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Near-boundary joint-minimum smoothing is diagnostic only. "
            "It may not be used to claim mass change or measurable deviation "
            "until weights, sigma, recombination, and observable map are derived."
        ),
    ))

    # Candidate route: boundary mass preservation via compact support
    ns.record_route(RouteRecord(
        route_id="boundary_mass_preservation_compact_support_route",
        script_id=SCRIPT_ID,
        name="Boundary mass preservation via compact kappa support and zero flux condition",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_boundary_mass_preservation_theorem_B2",
            "derive_kappa_flux_neutrality_boundary_B4",
            "derive_A_flux_kappa_flux_independence_B6",
        ],
        activation_conditions=[
            "support(S_kappa_eff) is compact or compensated",
            "F_kappa(R+) = 0 follows from parent identity",
            "delta(integral grad A dot dS)|kappa = 0 established",
            "exterior kappa attractor is zero",
        ],
    ))

    # Branch decision: boundary mass preservation theorem deferred
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_boundary_mass_preservation_theorem",
        script_id=SCRIPT_ID,
        branch_id="boundary_mass_preservation_theorem",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_boundary_mass_preservation_theorem_B2",
            "derive_kappa_flux_neutrality_boundary_B4",
            "derive_A_flux_kappa_flux_independence_B6",
            "derive_P_recombination_exterior_schwarzschild_B9",
            "derive_relaxation_energy_vac_config_balance_B10",
        ],
        description=(
            "Boundary mass preservation cannot be established as a theorem yet. "
            "The branch is deferred pending parent identity projection identities "
            "and vacuum configuration energy accounting."
        ),
    ))

    ns.record_derivation(
        derivation_id="boundary_mass_preservation_identity_marker",
        inputs=[],
        output=sp.Symbol("boundary_mass_preservation_identity_built"),
        method="boundary_mass_preservation_identity_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
