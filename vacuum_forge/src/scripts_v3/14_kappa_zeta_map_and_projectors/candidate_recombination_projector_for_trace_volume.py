# Candidate recombination projector for trace volume
#
# Group:
#   14_kappa_zeta_map_and_projectors
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# The boundary projector audit separated P_boundary from P_trace.
#
# P_boundary owns:
#
#   exterior zeta/kappa neutrality,
#   zero boundary flux,
#   zero volume/kappa charge,
#   A-sector mass protection,
#   shell-source avoidance.
#
# The next risk is recombination double-counting:
#
#   A-sector spatial response,
#   zeta volume response,
#   kappa residual/diagnostic response,
#   h_TT trace-free response,
#   W_i vector response.
#
# This script defines what P_recombination must do so that A, zeta, and kappa
# enter the geometry once, and only once.
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
class RecombinationEntry:
    name: str
    requirement: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[RecombinationEntry]:
    return [
        RecombinationEntry(
            name="R1: A-sector time response",
            requirement="g_tt <- A",
            role="places scalar mass response in time/lapse sector",
            allowed_if="A carries exterior mass / monopole response",
            forbidden_if="A response is duplicated as zeta/kappa exterior charge",
            status="STRUCTURAL",
            missing="covariant recombination map",
        ),
        RecombinationEntry(
            name="R2: A-sector spatial companion",
            requirement="g_ij may include scalar spatial response required by A-sector geometry",
            role="accounts for spatial curvature associated with mass response",
            allowed_if="counted once and separated from zeta/kappa residual volume response",
            forbidden_if="scalar_spatial_response(A), zeta, and kappa all add the same trace volume",
            status="UNRESOLVED",
            missing="which spatial trace belongs to A versus zeta/kappa",
        ),
        RecombinationEntry(
            name="R3: zeta volume response",
            requirement="zeta enters as volume-form configuration only once",
            role="represents vacuum-spacetime volume configuration",
            allowed_if="boundary-neutral and not counted again through kappa",
            forbidden_if="zeta adds exterior scalar charge or duplicates A spatial trace",
            status="REQUIRED",
            missing="metric insertion rule for zeta",
        ),
        RecombinationEntry(
            name="R4: kappa residual/diagnostic response",
            requirement="kappa enters as projected residual, diagnostic, or relaxation coordinate",
            role="tracks trace/volume mismatch without becoming second scalar gravity",
            allowed_if="role is explicitly diagnostic, residual, or energetic",
            forbidden_if="kappa adds independent spatial trace on top of zeta",
            status="REQUIRED",
            missing="kappa-zeta map and energy convention",
        ),
        RecombinationEntry(
            name="R5: count-once trace/volume rule",
            requirement="Trace[g_ij scalar sector] = one assembled trace/volume response",
            role="core no-double-counting condition",
            allowed_if="P_recombination chooses a single scalar trace channel",
            forbidden_if="A spatial response + zeta + kappa are summed as independent trace sources",
            status="REQUIRED",
            missing="explicit projection formula",
        ),
        RecombinationEntry(
            name="R6: boundary-neutral input",
            requirement="P_recombination receives P_boundary P_trace output",
            role="ensures recombined trace/volume piece is exterior-neutral",
            allowed_if="boundary projection happens before or inside recombination",
            forbidden_if="recombination reintroduces exterior zeta/kappa tail",
            status="REQUIRED",
            missing="composition order",
        ),
        RecombinationEntry(
            name="R7: TT trace-free insertion",
            requirement="g_ij <- ... + h_ij^TT with gamma^ij h_ij^TT = 0",
            role="adds tensor radiation without changing zeta at linear order",
            allowed_if="TT remains trace-free and orthogonal to scalar trace sector",
            forbidden_if="TT contributes volume trace or scalar radiation",
            status="STRUCTURAL",
            missing="nonlinear/covariant TT recombination",
        ),
        RecombinationEntry(
            name="R8: vector insertion",
            requirement="g_0i <- W_i",
            role="places transverse current/frame response in shift/vector sector",
            allowed_if="W_i sourced by P_T j and remains transverse",
            forbidden_if="longitudinal current or scalar trace enters W_i",
            status="STRUCTURAL",
            missing="covariant vector recombination and normalization",
        ),
        RecombinationEntry(
            name="R9: no scalar wave insertion",
            requirement="no A_rad, no Box kappa, no Box zeta contribution inserted into metric",
            role="preserves TT-only ordinary radiation rule",
            allowed_if="scalar/trace response remains constraint/relaxation/volume configuration",
            forbidden_if="recombination adds breathing scalar mode",
            status="FORBIDDEN",
            missing="parent scalar-radiation exclusion",
        ),
        RecombinationEntry(
            name="R10: epsilon/e_kappa accounting compatibility",
            requirement="metric assembly must match energy accounting convention",
            role="prevents geometric count-once rule from conflicting with epsilon/e_kappa separation",
            allowed_if="zeta energy and kappa residual energy are not the same contribution",
            forbidden_if="metric count-once but energy double-counts, or vice versa",
            status="REQUIRED",
            missing="degree-of-freedom accounting",
        ),
        RecombinationEntry(
            name="R11: areal diagnostic compatibility",
            requirement="kappa = 1/2 ln(AB) remains reduced diagnostic unless promoted",
            role="prevents areal-gauge relation from silently becoming covariant physical scalar",
            allowed_if="diagnostic status is explicit",
            forbidden_if="AB diagnostic and zeta/kappa physical insertion are both counted",
            status="CONSTRAINED",
            missing="areal diagnostic versus physical variable split",
        ),
        RecombinationEntry(
            name="R12: recommended provisional recombination rule",
            requirement="g_tt<-A, g_0i<-W_i, g_ij<-A_spatial_once + boundary-neutral trace/volume residual once + h_TT",
            role="best current operational recombination bundle",
            allowed_if="declared provisional and count-once",
            forbidden_if="treated as covariant derived metric law",
            status="RECOMMENDED",
            missing="explicit covariant parent recombination",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="boundary_projector_for_volume_neutrality_marker",
        upstream_script_id="14_kappa_zeta_map_and_projectors__candidate_boundary_projector_for_volume_neutrality",
        upstream_derivation_id="boundary_projector_for_volume_neutrality_marker",
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


def print_entry(e: RecombinationEntry) -> None:
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
    header("Case 0: Recombination projector for trace/volume problem")

    print("Question:")
    print()
    print("  How do A, zeta, and kappa assemble into the metric once, and only once?")
    print()
    print("Goal:")
    print()
    print("  define P_recombination requirements for count-once trace/volume assembly")
    print()
    print("Discipline:")
    print()
    print("  A carries exterior mass")
    print("  zeta carries volume configuration")
    print("  kappa is residual/diagnostic/relaxation, not second scalar gravity")
    print("  h_TT remains trace-free")
    print("  W_i remains transverse")
    print("  no scalar breathing mode is inserted")
    print("  metric assembly must match energy accounting")


def case_1_inventory(entries: List[RecombinationEntry]):
    header("Case 1: P_recombination requirement inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[RecombinationEntry]):
    header("Case 2: Compact P_recombination ledger")

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


def case_3_status_counts(entries: List[RecombinationEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  P_recombination is the count-once gate.")
    print("  The major unresolved issue is A_spatial versus zeta/kappa trace volume response.")
    print("  Recombination must match energy accounting or the theory double-counts even if projectors look clean.")


def case_4_minimal_recombination_bundle():
    header("Case 4: Minimal P_recombination requirement bundle")

    print("Current provisional bundle:")
    print()
    print("  g_tt <- A")
    print("  g_0i <- W_i")
    print("  g_ij <- A_spatial_once + trace_volume_residual_once + h_TT")
    print()
    print("where:")
    print()
    print("  trace_volume_residual_once <- P_boundary P_trace or P_boundary P_relax P_trace")
    print()
    print("and:")
    print()
    print("  h_TT is trace-free")
    print("  W_i is transverse")
    print("  no A_rad / Box kappa / Box zeta is inserted")


def case_4b_symbolic_trace_orthogonality(ns) -> None:
    header("Case 4b: Symbolic TT trace-free and trace orthogonality sample")

    # Linear trace projector in 3D
    # P_trace h_ij = delta_ij * (1/3) * delta^{ab} h_ab
    # TT tensor satisfies delta^{ab} h_ab^{TT} = 0
    # -> P_trace h_TT = 0

    hxx, hyy, hzz, hxy, hxz, hyz = sp.symbols("hxx hyy hzz hxy hxz hyz")
    # General symmetric 3-tensor
    h = sp.Matrix([[hxx, hxy, hxz], [hxy, hyy, hyz], [hxz, hyz, hzz]])
    identity3 = sp.eye(3)
    trace_h = sp.simplify(h.trace())
    # Linear trace projection
    P_trace_h = sp.simplify(identity3 * trace_h / 3)
    # TT sample (traceless by construction)
    # hzz = -(hxx + hyy), hxz=hyz=0
    h_TT_subs = {hzz: -(hxx + hyy), hxz: 0, hyz: 0}
    trace_h_TT = sp.simplify(h.subs(h_TT_subs).trace())
    P_trace_h_TT = sp.simplify(identity3 * trace_h_TT / 3)

    print("Linear trace projector applied to general h:")
    print(f"  trace(h) = {trace_h}")
    print(f"  P_trace h = (1/3)*I*trace(h)")
    print()
    print("TT sample (hzz = -(hxx+hyy), hxz=hyz=0):")
    print(f"  trace(h_TT) = {trace_h_TT}")
    print(f"  P_trace h_TT = {P_trace_h_TT}")
    print()
    print("Interpretation: P_trace h_TT = 0. The TT sector and the trace sector are orthogonal at linear order.")

    ns.record_derivation(
        derivation_id="recombination_projector_tt_trace_orthogonality_sample",
        inputs=[h, identity3],
        output=sp.Tuple(trace_h_TT, P_trace_h_TT),
        method="linear TT / trace orthogonality projector sample",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="linear reduced 3D sample only",
    )


def case_5_failure_controls():
    header("Case 5: Failure controls")

    print("P_recombination fails if:")
    print()
    print("1. A spatial response, zeta, and kappa all add the same trace")
    print("2. kappa becomes an independent exterior scalar gravity")
    print("3. zeta creates exterior scalar charge")
    print("4. h_TT contributes trace volume")
    print("5. W_i receives longitudinal/scalar current")
    print("6. scalar breathing mode is inserted")
    print("7. boundary-neutrality is undone during metric assembly")
    print("8. metric count-once rule conflicts with epsilon/e_kappa energy accounting")
    print("9. reduced areal kappa diagnostic is treated as covariant physical scalar without derivation")


def case_6_next_tests():
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_recombination_projector_for_trace_volume.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_areal_kappa_diagnostic_vs_physical_variable.py")
    print("   Separate kappa=1/2 ln(AB) diagnostic from physical kappa/zeta response.")
    print()
    print("3. candidate_A_spatial_vs_zeta_trace_counting.py")
    print("   Focus on whether A spatial curvature and zeta volume configuration overlap.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_A_spatial_vs_zeta_trace_counting.py")
    print()
    print("Reason:")
    print("  The unresolved recombination bottleneck is whether A_spatial and zeta/kappa trace-volume response overlap.")


def final_interpretation():
    header("Final interpretation")

    print("P_recombination is the count-once gate:")
    print()
    print("  g_tt <- A")
    print("  g_0i <- W_i")
    print("  g_ij <- A_spatial_once + trace_volume_residual_once + h_TT")
    print()
    print("Main unresolved issue:")
    print()
    print("  What spatial trace belongs to A, and what remains for zeta/kappa?")
    print()
    print("Possible next artifact:")
    print("  candidate_recombination_projector_for_trace_volume.md")
    print()
    print("Possible next script:")
    print("  candidate_A_spatial_vs_zeta_trace_counting.py")


def main():
    header("Candidate Recombination Projector For Trace Volume")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_recombination_bundle()
    case_4b_symbolic_trace_orthogonality(ns)
    case_5_failure_controls()
    case_6_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.derived_results():
        out.line("TT/trace orthogonality sample", StatusMark.PASS, "P_trace h_TT = 0 at linear order in 3D sample")

    with out.governance_assessments():
        out.line("P_recombination requirement bundle stated", StatusMark.PASS, "12 requirements inventoried")
        out.line("A_spatial versus zeta/kappa trace-volume split", StatusMark.FAIL, "unresolved — obligation recorded")

    with out.unresolved_obligations():
        out.line("derive P_recombination explicit formula", StatusMark.OBLIGATION, "open proof obligation recorded")
        out.line("resolve A_spatial vs zeta/kappa trace-volume overlap", StatusMark.OBLIGATION, "open proof obligation recorded")

    with archive.with_project_namespace(SCRIPT_ID) as ns:

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_P_recombination_explicit_formula_in_14",
            script_id=SCRIPT_ID,
            title="Derive the explicit P_recombination formula for count-once metric assembly",
            status=ObligationStatus.OPEN,
            description=(
                "P_recombination must assemble g_tt <- A, g_0i <- W_i, "
                "g_ij <- A_spatial_once + trace_volume_residual_once + h_TT. "
                "The covariant parent recombination is not derived. "
                "TT trace-orthogonality is verified at linear order only."
            ),
        ))

        ns.record_obligation(ProofObligationRecord(
            obligation_id="resolve_A_spatial_vs_zeta_kappa_trace_volume_in_14",
            script_id=SCRIPT_ID,
            title="Resolve which spatial trace belongs to A versus zeta/kappa",
            status=ObligationStatus.OPEN,
            description=(
                "R2 is unresolved: it is unclear whether A-sector spatial companion trace and zeta/kappa "
                "volume residual trace overlap. This is the core double-counting risk in P_recombination."
            ),
        ))

        ns.record_claim(ClaimRecord(
            claim_id="recombination_TT_trace_orthogonal_at_linear_order",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.SAMPLE_DERIVATION,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.HEURISTIC,
            statement=(
                "At linear order in 3D, the TT sector (traceless by construction) is orthogonal to the "
                "linear trace projector P_trace. P_trace h_TT = 0. This is a diagnostic sample; "
                "the nonlinear/covariant statement is not yet derived."
            ),
        ))

        ns.record_derivation(
            derivation_id="recombination_projector_for_trace_volume_marker",
            inputs=[],
            output=sp.Symbol("recombination_projector_for_trace_volume_audited"),
            method="recombination_projector_for_trace_volume_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns.write_run_metadata()


if __name__ == "__main__":
    main()
