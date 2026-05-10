# Candidate boundary projector for volume neutrality
#
# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The trace projector definition audit found:
#
#   P_trace is currently a requirement bundle:
#     trace extraction,
#     A-sector exclusion,
#     compensation / zero monopole,
#     TT annihilation,
#     boundary cooperation.
#
# The next likely split is:
#
#   P_trace versus P_boundary versus P_recombination.
#
# This script splits off the boundary/exterior-neutrality duties into
# P_boundary.
#
# It is not a derivation.

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
class BoundaryProjectorEntry:
    name: str
    requirement: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[BoundaryProjectorEntry]:
    return [
        BoundaryProjectorEntry(
            name="B1: exterior zeta neutrality",
            requirement="zeta_ext -> 0",
            role="prevents vacuum-volume configuration from becoming an exterior scalar field",
            allowed_if="ordinary exterior vacuum is fixed point of volume sector",
            forbidden_if="zeta_ext ~ 1/r or persistent exterior volume pressure",
            status="REQUIRED",
            missing="exterior stability theorem",
        ),
        BoundaryProjectorEntry(
            name="B2: exterior kappa neutrality",
            requirement="kappa_ext -> 0",
            role="prevents kappa from becoming a second scalar gravity",
            allowed_if="kappa is residual/projected/boundary-neutral",
            forbidden_if="kappa_ext ~ 1/r",
            status="REQUIRED",
            missing="kappa-zeta boundary relation",
        ),
        BoundaryProjectorEntry(
            name="B3: zero zeta boundary flux",
            requirement="F_zeta(R+) = 0",
            role="prevents exterior zeta tail from boundary leakage",
            allowed_if="P_boundary enforces zero flux or compact support",
            forbidden_if="nonzero F_zeta seeds exterior charge",
            status="REQUIRED",
            missing="interface law",
        ),
        BoundaryProjectorEntry(
            name="B4: zero kappa boundary flux",
            requirement="F_kappa(R+) = 0",
            role="prevents exterior kappa tail from boundary leakage",
            allowed_if="P_boundary enforces zero flux or compact support",
            forbidden_if="nonzero F_kappa seeds exterior charge",
            status="REQUIRED",
            missing="interface law",
        ),
        BoundaryProjectorEntry(
            name="B5: zero volume charge",
            requirement="Q_volume = 0",
            role="removes exterior volume monopole",
            allowed_if="compact support, compensation, or parent constraint enforces it",
            forbidden_if="Q_volume nonzero sources exterior scalar",
            status="REQUIRED",
            missing="S_volume definition and compensation origin",
        ),
        BoundaryProjectorEntry(
            name="B6: zero kappa charge",
            requirement="Q_kappa = 0",
            role="removes exterior kappa monopole",
            allowed_if="kappa is projected residual with compensation",
            forbidden_if="Q_kappa nonzero creates kappa_ext ~ 1/r",
            status="REQUIRED",
            missing="Q_kappa definition and relation to Q_volume",
        ),
        BoundaryProjectorEntry(
            name="B7: A-sector mass protection",
            requirement="delta M_ext|boundary zeta/kappa = 0",
            role="keeps boundary smoothing from tuning measured mass",
            allowed_if="P_boundary preserves A_flux",
            forbidden_if="boundary volume mode changes A-sector 1/r coefficient",
            status="REQUIRED",
            missing="boundary mass preservation theorem",
        ),
        BoundaryProjectorEntry(
            name="B8: compact-support profile compatibility",
            requirement="zeta(R)=zeta'(R)=0 and/or kappa(R)=kappa'(R)=0",
            role="toy diagnostic for no boundary flux and no shell source",
            allowed_if="used as profile test, not physical derivation",
            forbidden_if="toy compact profile is mistaken for parent law",
            status="STRUCTURAL",
            missing="physical interface law",
        ),
        BoundaryProjectorEntry(
            name="B9: shell-source avoidance",
            requirement="sufficient smoothness at boundary, possibly C2 or distribution-safe matching",
            role="prevents hidden delta-function source at interface",
            allowed_if="smoothness is derived or explicitly diagnostic",
            forbidden_if="zero field but nonzero distributional curvature sneaks in",
            status="CANDIDATE",
            missing="required differentiability from action/field equations",
        ),
        BoundaryProjectorEntry(
            name="B10: cooperation with P_trace",
            requirement="P_boundary P_trace maps trace/volume residual to exterior-neutral support",
            role="splits trace extraction from boundary neutrality",
            allowed_if="P_trace and P_boundary are separate but compatible",
            forbidden_if="P_trace hides boundary conditions internally",
            status="RECOMMENDED",
            missing="composition law P_boundary P_trace",
        ),
        BoundaryProjectorEntry(
            name="B11: cooperation with P_recombination",
            requirement="boundary-neutral zeta/kappa inserted into g_ij once",
            role="prevents boundary correction from duplicating recombination trace response",
            allowed_if="P_recombination receives already-neutral trace/volume contribution",
            forbidden_if="boundary projector and recombination each add separate trace corrections",
            status="REQUIRED",
            missing="P_recombination definition",
        ),
        BoundaryProjectorEntry(
            name="B12: no scalar radiation at boundary",
            requirement="boundary projector is not a radiative outgoing condition for scalar mode",
            role="keeps boundary neutralization from becoming scalar wave leakage",
            allowed_if="boundary condition is constraint/interface, not radiation channel",
            forbidden_if="boundary emits zeta/kappa scalar waves",
            status="FORBIDDEN",
            missing="parent scalar-radiation exclusion",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="trace_projector_definition_marker",
        upstream_script_id="14_kappa_zeta_map_and_projectors__candidate_trace_projector_definition",
        upstream_derivation_id="trace_projector_definition_marker",
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


def print_entry(e: BoundaryProjectorEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Requirement: {e.requirement}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement():
    header("Case 0: Boundary projector for volume neutrality problem")

    print("Question:")
    print()
    print("  What exactly belongs to P_boundary for zeta/kappa exterior neutrality?")
    print()
    print("Goal:")
    print()
    print("  split boundary/exterior-neutrality duties away from P_trace")
    print()
    print("Discipline:")
    print()
    print("  no exterior zeta charge")
    print("  no exterior kappa charge")
    print("  no boundary flux leakage")
    print("  no A-sector mass change")
    print("  no hidden shell source")
    print("  no scalar radiation at boundary")


def case_1_inventory(entries: List[BoundaryProjectorEntry]):
    header("Case 1: P_boundary requirement inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[BoundaryProjectorEntry]):
    header("Case 2: Compact P_boundary ledger")

    print("| Entry | Requirement | Status | Missing |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.requirement.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )


def case_3_status_counts(entries: List[BoundaryProjectorEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  P_boundary has a clearer job than P_trace:")
    print("    enforce exterior neutrality, zero flux, zero charge, and mass preservation.")
    print("  Compact profiles are useful diagnostics but not derivations.")
    print("  P_boundary must cooperate with P_trace and P_recombination.")


def case_4_minimal_boundary_bundle():
    header("Case 4: Minimal P_boundary requirement bundle")

    print("Current operational bundle:")
    print()
    print("  P_boundary =")
    print("    exterior zeta/kappa neutrality")
    print("    + zero boundary flux")
    print("    + zero volume/kappa charge")
    print("    + A-sector mass protection")
    print("    + shell-source avoidance")
    print()
    print("Composition target:")
    print()
    print("  P_boundary P_trace")
    print()
    print("Meaning:")
    print("  trace/volume residual is projected into a boundary-neutral sector.")


def case_4b_symbolic_boundary_flux(ns) -> None:
    header("Case 4b: Symbolic boundary-flux check")

    r, R, zeta0 = sp.symbols("r R zeta0", positive=True)
    profile = sp.simplify(zeta0 * (1 - r**2 / R**2) ** 2)
    value_at_boundary = sp.simplify(profile.subs(r, R))
    derivative_at_boundary = sp.simplify(sp.diff(profile, r).subs(r, R))
    flux_at_boundary = sp.simplify(4 * sp.pi * R**2 * derivative_at_boundary)

    print("Compact profile sample:")
    print()
    print(f"  zeta(r) = {profile}")
    print(f"  zeta(R) = {value_at_boundary}")
    print(f"  zeta'(R) = {derivative_at_boundary}")
    print(f"  F_zeta(R+) = {flux_at_boundary}")
    print()
    print("Interpretation:")
    print("  compact support profile zeta0*(1-r^2/R^2)^2 satisfies zeta(R)=0 and zeta'(R)=0,")
    print("  yielding zero boundary flux F_zeta(R+)=0.")

    ns.record_derivation(
        derivation_id="boundary_projector_zero_flux_sample",
        inputs=[profile],
        output=sp.Tuple(value_at_boundary, derivative_at_boundary, flux_at_boundary),
        method="compact-profile boundary neutrality sample",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="compact profile diagnostic only, not a physical derivation",
    )


def case_5_failure_controls():
    header("Case 5: Failure controls")

    print("P_boundary fails if:")
    print()
    print("1. zeta_ext has a 1/r tail")
    print("2. kappa_ext has a 1/r tail")
    print("3. F_zeta(R+) or F_kappa(R+) is nonzero")
    print("4. Q_volume or Q_kappa is nonzero")
    print("5. delta M_ext changes")
    print("6. a hidden shell source appears")
    print("7. compact profile tests are mistaken for derivation")
    print("8. boundary neutralization becomes scalar radiation")
    print("9. P_boundary and P_recombination both add trace corrections")


def case_6_next_tests():
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_boundary_projector_for_volume_neutrality.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_recombination_projector_for_trace_volume.py")
    print("   Define how A, zeta, and kappa assemble without double-counting.")
    print()
    print("3. candidate_boundary_mass_preservation_theorem.py")
    print("   Focus specifically on delta M_ext = 0 under boundary-neutral volume modes.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_recombination_projector_for_trace_volume.py")
    print()
    print("Reason:")
    print("  P_boundary is now separated. The next risk is recombination double-counting of A, zeta, and kappa.")


def final_interpretation():
    header("Final interpretation")

    print("P_boundary is responsible for:")
    print()
    print("  exterior zeta/kappa neutrality")
    print("  zero boundary flux")
    print("  zero volume/kappa charge")
    print("  A-sector mass protection")
    print("  shell-source avoidance")
    print()
    print("It should compose with P_trace:")
    print()
    print("  P_boundary P_trace")
    print()
    print("Possible next artifact:")
    print("  candidate_boundary_projector_for_volume_neutrality.md")
    print()
    print("Possible next script:")
    print("  candidate_recombination_projector_for_trace_volume.py")


def main():
    header("Candidate Boundary Projector For Volume Neutrality")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_boundary_bundle()
    case_4b_symbolic_boundary_flux(ns)
    case_5_failure_controls()
    case_6_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.derived_results():
        out.line("compact boundary flux sample", StatusMark.PASS, "zeta0*(1-r^2/R^2)^2 gives F_zeta(R+)=0")

    with out.governance_assessments():
        out.line("P_boundary requirement bundle stated", StatusMark.PASS, "12 requirements inventoried")
        out.line("P_boundary as derived projector", StatusMark.DEFER, "requirement bundle, not yet a derived operator")

    with out.unresolved_obligations():
        out.line("derive P_boundary composition law", StatusMark.OBLIGATION, "open proof obligation recorded")
        out.line("derive exterior stability theorem", StatusMark.OBLIGATION, "open proof obligation recorded")
        out.line("derive P_recombination definition", StatusMark.OBLIGATION, "open proof obligation recorded")

    with archive.with_project_namespace(SCRIPT_ID) as ns:

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_P_boundary_composition_law_in_14",
            script_id=SCRIPT_ID,
            title="Derive P_boundary composition law P_boundary P_trace",
            status=ObligationStatus.OPEN,
            description=(
                "The composition P_boundary P_trace maps trace/volume residual into an exterior-neutral "
                "sector. The composition law is not derived. Requires: interface law, mass preservation, "
                "shell-source avoidance, scalar-radiation exclusion."
            ),
        ))

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_P_recombination_definition_in_14",
            script_id=SCRIPT_ID,
            title="Derive P_recombination definition for count-once metric assembly",
            status=ObligationStatus.OPEN,
            description=(
                "P_recombination must assemble A, zeta, kappa, h_TT, and W_i into the metric once "
                "and only once. A_spatial versus zeta/kappa trace volume is unresolved."
            ),
        ))

        ns.record_claim(ClaimRecord(
            claim_id="boundary_flux_sample_C2_profile",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.SAMPLE_DERIVATION,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.HEURISTIC,
            statement=(
                "The compact profile zeta(r)=zeta0*(1-r^2/R^2)^2 is a diagnostic sample showing "
                "that zeta(R)=0, zeta'(R)=0, and F_zeta(R+)=0. This is a diagnostic only, not a "
                "physical boundary law derivation."
            ),
        ))

        ns.record_derivation(
            derivation_id="boundary_projector_for_volume_neutrality_marker",
            inputs=[],
            output=sp.Symbol("boundary_projector_for_volume_neutrality_audited"),
            method="boundary_projector_for_volume_neutrality_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns.write_run_metadata()


if __name__ == "__main__":
    main()
