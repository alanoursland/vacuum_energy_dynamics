# Candidate correction tensor boundary and mass neutrality
#
# Group:
#   19_parent_correction_tensor_audit
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The correction tensor source-separation audit found:
#
#   Source separation is required but not derived.
#   Ordinary matter must stay in ordinary source routing.
#   A-sector mass accounting must remain protected.
#   e_curv cannot become H_curv source reservoir.
#   Sigma/R cannot become H_exch tuning knobs.
#   J_sub/J_exch cannot become ordinary matter channels.
#   Dark sector cannot relabel ordinary matter or ordinary exchange failure.
#   zeta/B_s insertion and residual trace cannot be reopened by correction tensor.
#   Boundary failure cannot be reclassified as correction tensor source.
#
# This script audits whether H_curv/H_exch avoid boundary repair and exterior mass shift.
#
# Locked-door question:
#
#   Can H_curv/H_exch avoid boundary repair and exterior mass shift?
#
# This is a boundary/mass neutrality audit, not a boundary theorem.


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
class BoundaryMassEntry:
    name: str
    rule: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="correction_tensor_source_separation_marker",
        upstream_script_id="19_parent_correction_tensor_audit__candidate_correction_tensor_source_separation",
        upstream_derivation_id="correction_tensor_source_separation_marker",
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


def build_entries() -> List[BoundaryMassEntry]:
    return [
        BoundaryMassEntry(
            name="BM1: boundary/mass neutrality target",
            rule="H_curv/H_exch must avoid boundary repair, exterior mass shift, scalar charge leakage, hidden flux, and shell-source hiding",
            role="core boundary/mass theorem target",
            allowed_if="neutrality is structural and derived before insertion",
            forbidden_if="boundary/mass behavior is repaired by tensor choice",
            status="THEOREM_TARGET",
            missing="boundary/mass neutrality theorem",
            consequence="decides whether correction tensors can be inserted without corrupting exterior sector",
        ),
        BoundaryMassEntry(
            name="BM2: no M_ext shift independent of A",
            rule="delta M_ext|H_curv/H_exch = 0 unless derived through established A-sector source law",
            role="mass neutrality guard",
            allowed_if="correction tensor is exterior-mass-neutral by theorem",
            forbidden_if="H_curv/H_exch changes measured exterior mass",
            status="REQUIRED",
            missing="mass neutrality theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        BoundaryMassEntry(
            name="BM3: no boundary counterterm",
            rule="H_curv/H_exch is not a counterterm chosen to cancel boundary leakage or mismatch",
            role="boundary repair guard",
            allowed_if="boundary behavior follows from source/tensor law",
            forbidden_if="correction tensor exists because boundary behavior failed",
            status="REQUIRED",
            missing="boundary law",
            consequence="prevents painted boundary closure",
        ),
        BoundaryMassEntry(
            name="BM4: no exterior scalar charge",
            rule="H_curv/H_exch does not generate exterior B_s/zeta/kappa scalar charge or tail",
            role="scalar exterior guard",
            allowed_if="scalar trace neutrality and no-overlap are preserved",
            forbidden_if="correction tensor leaks scalar charge outside",
            status="REQUIRED",
            missing="scalar trace / exterior charge theorem",
            consequence="preserves Group 16 guardrails",
        ),
        BoundaryMassEntry(
            name="BM5: no far-zone hidden flux",
            rule="H_curv/H_exch does not carry hidden far-zone flux of mass, scalar charge, curvature, or exchange",
            role="far-zone neutrality guard",
            allowed_if="flux neutrality follows structurally",
            forbidden_if="hidden flux is used to balance interior correction",
            status="REQUIRED",
            missing="far-zone flux theorem",
            consequence="protects exterior recovery and mass accounting",
        ),
        BoundaryMassEntry(
            name="BM6: no shell source by support",
            rule="compact/boundary support does not create an unaccounted shell source",
            role="support regularity guard",
            allowed_if="support is smooth/structural and shell-neutral",
            forbidden_if="support discontinuity hides source layer",
            status="REQUIRED",
            missing="support regularity theorem",
            consequence="prevents support-shaped source smuggling",
        ),
        BoundaryMassEntry(
            name="BM7: no recovery-tuned boundary smoothing",
            rule="boundary behavior is not chosen to pass gamma_like, AB, exterior matching, or PPN behavior",
            role="recovery-smuggling guard",
            allowed_if="boundary law is derived before recovery tests",
            forbidden_if="boundary smoothing is recovery-fit",
            status="REQUIRED",
            missing="boundary coefficient/origin theorem",
            consequence="keeps recovery downstream",
        ),
        BoundaryMassEntry(
            name="BM8: no dark boundary patch",
            rule="dark-sector label is not used to absorb boundary mismatch, exterior mass shift, or scalar tail",
            role="dark boundary guard",
            allowed_if="dark branch remains absent/deferred or independently sourced",
            forbidden_if="dark sector patches ordinary boundary failure",
            status="REQUIRED",
            missing="dark boundary separation theorem if reopened",
            consequence="preserves no-dark-patch rule",
        ),
        BoundaryMassEntry(
            name="BM9: no anti-singularity by boundary tensor",
            rule="H_curv/H_exch does not claim bounce, regular core, or finite admissibility by boundary behavior",
            role="anti-overclaim guard",
            allowed_if="anti-singularity claims remain theorem targets with equations/solutions",
            forbidden_if="boundary tensor is used as singularity cure",
            status="REQUIRED",
            missing="anti-singularity theorem if stronger claim is wanted",
            consequence="preserves Group 17 claim limits",
        ),
        BoundaryMassEntry(
            name="BM10: ordinary matter boundary decoupling",
            rule="boundary behavior does not reroute ordinary matter or modify ordinary source coupling",
            role="ordinary matter boundary guard",
            allowed_if="ordinary matter remains in established source routing",
            forbidden_if="boundary tensor fixes matter coupling or source discontinuity",
            status="REQUIRED",
            missing="ordinary matter boundary decoupling theorem",
            consequence="protects ordinary matter coupling",
        ),
        BoundaryMassEntry(
            name="BM11: diagnostic-only correction tensor",
            rule="H-like object remains diagnostic-only and therefore has no boundary or mass effect",
            role="safe fallback",
            allowed_if="not inserted into field equation",
            forbidden_if="diagnostic object becomes boundary/mass correction",
            status="SAFE_IF",
            missing="none if kept diagnostic",
            consequence="safe route if correction tensors remain audit objects",
        ),
        BoundaryMassEntry(
            name="BM12: interior-only branch filter",
            rule="correction object acts as interior diagnostic / branch filter only",
            role="candidate safe route",
            allowed_if="does not alter exterior mass, boundary conditions, or field equations",
            forbidden_if="branch filter is promoted to dynamics",
            status="CANDIDATE",
            missing="branch-filter theorem and interior domain",
            consequence="possible non-inserted curvature/admissibility route",
        ),
        BoundaryMassEntry(
            name="BM13: compact support with structural zero-flux",
            rule="correction tensor has compact support and structural zero exterior flux",
            role="candidate boundary-safe tensor class",
            allowed_if="support and zero-flux are derived, smooth, and not solution-tailored",
            forbidden_if="compact support is chosen to hide exterior effects",
            status="CANDIDATE",
            missing="support and zero-flux theorem",
            consequence="possible safe route if support is real",
        ),
        BoundaryMassEntry(
            name="BM14: identically divergence-free interior tensor",
            rule="interior tensor is divergence-free by identity and has neutral boundary behavior",
            role="candidate divergence/boundary class",
            allowed_if="identity and boundary neutrality are both derived",
            forbidden_if="identity is Bianchi smoke or boundary behavior is patched",
            status="CANDIDATE",
            missing="identity plus boundary neutrality theorem",
            consequence="possible insertable class if all other source guards hold",
        ),
        BoundaryMassEntry(
            name="BM15: source-balanced tensor with neutral boundary",
            rule="tensor divergence balances an independent source while boundary remains neutral",
            role="candidate source/boundary class",
            allowed_if="source partner is independent and boundary flux is neutral",
            forbidden_if="boundary flux balances source failure",
            status="CANDIDATE",
            missing="source partner and neutral boundary theorem",
            consequence="possible route if source/boundary are both real",
        ),
        BoundaryMassEntry(
            name="BM16: boundary-supported tensor risk",
            rule="correction tensor lives at boundary/interface",
            role="high-risk tensor class",
            allowed_if="boundary support is structural, shell-neutral, mass-neutral, scalar-neutral",
            forbidden_if="support repairs leakage or hides shell source",
            status="RISK",
            missing="boundary support theorem",
            consequence="dangerous because boundary repair is recurring failure mode",
        ),
        BoundaryMassEntry(
            name="BM17: boundary repair tensor rejection",
            rule="H_curv/H_exch cancels boundary leakage, scalar tail, shell source, or exterior mismatch",
            role="forbidden boundary repair",
            allowed_if="never as mechanism",
            forbidden_if="accepted as boundary behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents boundary patch tensor",
        ),
        BoundaryMassEntry(
            name="BM18: M_ext correction tensor rejection",
            rule="H_curv/H_exch changes M_ext to fix exterior behavior",
            role="forbidden mass correction",
            allowed_if="never without A-sector source theorem",
            forbidden_if="accepted as mass effect",
            status="REJECTED",
            missing="not pursued",
            consequence="protects exterior mass",
        ),
        BoundaryMassEntry(
            name="BM19: scalar tail cancellation tensor rejection",
            rule="H_curv/H_exch cancels or hides exterior scalar tail",
            role="forbidden scalar repair",
            allowed_if="never as mechanism",
            forbidden_if="accepted as scalar neutrality",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents scalar charge cover-up",
        ),
        BoundaryMassEntry(
            name="BM20: shell-source hiding tensor rejection",
            rule="support or boundary behavior hides an unaccounted shell source",
            role="forbidden support trick",
            allowed_if="never as mechanism",
            forbidden_if="accepted as compact/boundary support",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents source layer smuggling",
        ),
        BoundaryMassEntry(
            name="BM21: recovery boundary fit rejection",
            rule="boundary behavior is selected to recover gamma_like, AB, exterior matching, or PPN behavior",
            role="forbidden recovery construction",
            allowed_if="never as origin",
            forbidden_if="accepted as boundary law",
            status="REJECTED",
            missing="not pursued",
            consequence="keeps recovery downstream",
        ),
        BoundaryMassEntry(
            name="BM22: boundary/mass neutrality failure",
            rule="correction tensors cannot avoid boundary repair or exterior mass shift",
            role="branch failure condition",
            allowed_if="used to keep correction tensors deferred or diagnostic-only",
            forbidden_if="patched with support choices, counterterms, or dark labels",
            status="BRANCH_KILLED",
            missing="applies if failure demonstrated",
            consequence="correction tensors cannot be inserted",
        ),
        BoundaryMassEntry(
            name="BM23: recommended next move",
            rule="after boundary/mass neutrality, audit parent equation insertability",
            role="next local bottleneck",
            allowed_if="boundary/mass neutrality remains theorem-targeted",
            forbidden_if="jumping to parent equation before insertability audit",
            status="RECOMMENDED",
            missing="parent equation insertability audit",
            consequence="next script should be candidate_parent_equation_insertability_audit.py",
        ),
    ]


def print_entry(e: BoundaryMassEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    out = ScriptOutput()
    with out.governance_assessments():
        out.line(e.name, StatusMark.from_string(e.status), e.status)

    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Correction tensor boundary/mass neutrality problem")

    print("Question:")
    print()
    print("  Can H_curv/H_exch avoid boundary repair and exterior mass shift?")
    print()
    print("Goal:")
    print()
    print("  prevent correction tensors from repairing boundary behavior or changing exterior mass")
    print()
    print("Discipline:")
    print()
    print("  no M_ext shift independent of A")
    print("  no boundary counterterm")
    print("  no exterior scalar charge")
    print("  no far-zone hidden flux")
    print("  no shell source by support")
    print("  no recovery-tuned boundary smoothing")
    print("  no dark boundary patch")
    print("  no anti-singularity by boundary tensor")

    with out.unresolved_obligations():
        out.line("correction tensor boundary/mass neutrality problem posed", StatusMark.OBLIGATION, "boundary/mass neutrality audit required before any H insertion")


def case_1_inventory(entries: List[BoundaryMassEntry]):
    header("Case 1: Correction tensor boundary/mass neutrality inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[BoundaryMassEntry], out: ScriptOutput):
    header("Case 2: Compact boundary/mass neutrality ledger")

    print("| Entry | Rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact boundary/mass neutrality ledger produced", StatusMark.INFO, "STRUCTURAL")


def case_3_status_counts(entries: List[BoundaryMassEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Boundary/mass neutrality is required but not derived.")
    print("  H_curv/H_exch must not shift M_ext, act as boundary counterterms, generate exterior scalar charge, hide far-zone flux, create shell sources, or tune boundary recovery.")
    print("  Diagnostic-only remains safest.")
    print("  Interior-only branch filter, compact support with structural zero-flux, identically divergence-free interior tensor, and source-balanced neutral-boundary tensor remain candidate routes only if derived.")
    print("  Boundary-supported tensors are risky.")
    print("  Boundary repair tensor, M_ext correction tensor, scalar tail cancellation tensor, shell-source hiding tensor, and recovery boundary fit are rejected.")
    print("  Next gate is parent equation insertability.")

    with out.governance_assessments():
        out.line("boundary/mass neutrality status count produced", StatusMark.INFO, "STRUCTURAL")


def case_4_candidate_safe_routes(out: ScriptOutput):
    header("Case 4: Candidate safe routes")

    print("Candidate safe routes:")
    print()
    print("1. diagnostic-only correction tensor")
    print("2. interior-only branch filter")
    print("3. compact support with structural zero-flux")
    print("4. identically divergence-free interior tensor")
    print("5. source-balanced tensor with neutral boundary")
    print()
    print("High risk:")
    print()
    print("1. boundary-supported tensor")
    print()
    print("Rejected:")
    print()
    print("1. boundary repair tensor")
    print("2. M_ext correction tensor")
    print("3. scalar tail cancellation tensor")
    print("4. shell-source hiding tensor")
    print("5. recovery boundary fit")

    with out.governance_assessments():
        out.line("boundary/mass safe routes listed", StatusMark.PASS, "RECOMMENDED")


def case_4b_compact_support_sample(ns, out: ScriptOutput):
    header("Case 4b: Sample compact-support neutral-boundary profile")

    r, R, a = sp.symbols("r R a", positive=True)
    profile = a * (1 - r / R) ** 4
    profile_at_boundary = sp.simplify(profile.subs(r, R))
    slope_at_boundary = sp.simplify(sp.diff(profile, r).subs(r, R))

    print("Sample profile:")
    print(f"  h(r) = {profile}")
    print()
    print(f"h(R) = {profile_at_boundary}")
    print(f"h'(R) = {slope_at_boundary}")
    print()
    print("Interpretation:")
    print("  this is a compatibility example for a smooth compact-support profile")
    print("  with zero boundary value and zero first derivative at the support edge.")
    print("  It is not a real correction-tensor boundary theorem.")

    if profile_at_boundary == 0 and slope_at_boundary == 0:
        with out.sample_results():
            out.line(
                "sample neutral-boundary support witness",
                StatusMark.PASS,
                "compact-support sample has h(R)=0 and h'(R)=0",
            )
    else:
        with out.sample_results():
            out.line(
                "sample neutral-boundary support witness",
                StatusMark.FAIL,
                "compact-support sample failed boundary neutrality conditions",
            )

    ns.record_derivation(
        derivation_id="compact_support_neutral_boundary_sample",
        inputs=[profile],
        output=sp.Tuple(profile_at_boundary, slope_at_boundary),
        method="toy_compact_support_boundary_compatibility",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
        scope="toy 1D radial profile; not a real correction-tensor boundary theorem",
    )


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Boundary/mass neutrality decision tree")

    print("Decision tree:")
    print()
    print("1. H is diagnostic-only:")
    print("   safe if never inserted.")
    print()
    print("2. H is interior-only branch filter:")
    print("   candidate if no field-equation/boundary effect.")
    print()
    print("3. H has compact support with structural zero-flux:")
    print("   candidate if support is not solution-tailored.")
    print()
    print("4. H is divergence-free/source-balanced and boundary-neutral:")
    print("   candidate if source separation also holds.")
    print()
    print("5. H repairs boundary, mass, scalar tail, shell, or recovery:")
    print("   rejected.")
    print()
    print("6. Neutrality cannot be shown:")
    print("   keep correction tensors deferred.")

    with out.governance_assessments():
        out.line("boundary/mass neutrality decision tree stated", StatusMark.PASS, "RECOMMENDED")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  correction tensors cannot avoid boundary repair or exterior mass shift.")
    print()
    print("Consequence:")
    print()
    print("  keep H_curv/H_exch deferred or diagnostic-only.")
    print("  do not insert correction tensors into parent equation.")
    print()
    print("Bad failure:")
    print()
    print("  hide boundary/mass failure inside support choices, counterterms, or dark labels.")

    with out.governance_assessments():
        out.line("boundary/mass neutrality good failure stated", StatusMark.DEFER, "DEFERRED_PENDING_PREREQUISITES")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("Boundary/mass neutrality fails if:")
    print()
    print("1. M_ext shifts independently of A")
    print("2. boundary counterterm is introduced")
    print("3. exterior scalar charge appears")
    print("4. far-zone hidden flux appears")
    print("5. shell source appears by support")
    print("6. boundary smoothing is recovery-tuned")
    print("7. dark sector patches boundary")
    print("8. boundary tensor claims anti-singularity")
    print("9. ordinary matter boundary coupling changes")
    print("10. compact support is solution-tailored")
    print("11. boundary-supported tensor repairs leakage")
    print("12. diagnostic-only object is inserted")

    with out.governance_assessments():
        out.line("boundary/mass neutrality failure controls stated", StatusMark.WARN, "RISK")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_correction_tensor_boundary_and_mass_neutrality.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_equation_insertability_audit.py")
    print("   Decide whether any correction tensor can be inserted into a parent equation yet.")
    print()
    print("3. candidate_boundary_mass_neutrality_failure_summary.py")
    print("   Use if all boundary/mass routes collapse into repair.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_equation_insertability_audit.py")
    print()
    print("Reason:")
    print("  H_curv/H_exch have now been audited for role, definition requirements, divergence safety, source separation, and boundary/mass neutrality.")
    print("  The next gate is whether any correction tensor is insertable at all.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "STRUCTURAL")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("Boundary/mass neutrality is required but not derived.")
    print()
    print("Required:")
    print()
    print("  no M_ext shift independent of A")
    print("  no boundary counterterm")
    print("  no exterior scalar charge")
    print("  no far-zone hidden flux")
    print("  no shell source by support")
    print("  no recovery-tuned boundary smoothing")
    print("  no dark boundary patch")
    print("  no anti-singularity by boundary tensor")
    print()
    print("Candidate routes:")
    print()
    print("  diagnostic-only")
    print("  interior-only branch filter")
    print("  compact support with structural zero-flux")
    print("  divergence-free interior tensor with neutral boundary")
    print("  source-balanced tensor with neutral boundary")
    print()
    print("Best next script:")
    print()
    print("  candidate_parent_equation_insertability_audit.py")

    with out.governance_assessments():
        out.line("correction tensor boundary/mass neutrality audit complete", StatusMark.PASS, "CLOSED")



def record_governance(ns) -> None:
    required_obligations = [
        ("derive_H_mass_neutrality_theorem_19",
         "Derive correction tensor exterior mass neutrality theorem",
         "delta M_ext|H_curv/H_exch = 0 unless derived through A-sector source law (BM2)."),
        ("derive_H_no_boundary_counterterm_19",
         "Derive that H_curv/H_exch is not a boundary counterterm",
         "H_curv/H_exch must not be chosen to cancel boundary leakage or mismatch (BM3)."),
        ("derive_H_no_exterior_scalar_charge_19",
         "Derive no exterior scalar charge theorem for correction tensors",
         "H_curv/H_exch must not generate exterior B_s/zeta/kappa scalar charge or tail (BM4)."),
        ("derive_H_no_far_zone_flux_19",
         "Derive no far-zone hidden flux theorem for correction tensors",
         "H_curv/H_exch must not carry hidden far-zone flux of mass, scalar charge, curvature, or exchange (BM5)."),
        ("derive_H_no_shell_source_19",
         "Derive no shell source by support theorem",
         "Compact/boundary support must not create an unaccounted shell source (BM6)."),
        ("derive_H_boundary_coefficient_origin_19",
         "Derive H boundary behavior coefficient origin",
         "Boundary behavior must not be chosen to pass recovery targets (BM7)."),
        ("guard_H_no_dark_boundary_patch_19",
         "Guard no dark boundary patch in correction tensors",
         "Dark-sector label must not be used to absorb boundary mismatch or exterior mass shift (BM8)."),
        ("guard_H_no_antisingularity_boundary_claim_19",
         "Guard no anti-singularity by boundary tensor claim",
         "H_curv/H_exch must not claim bounce, regular core, or finite admissibility by boundary behavior (BM9)."),
        ("derive_H_ordinary_matter_boundary_decoupling_19",
         "Derive ordinary matter boundary decoupling for correction tensors",
         "Boundary behavior must not reroute ordinary matter or modify ordinary source coupling (BM10)."),
    ]

    for obligation_id, title, description in required_obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["correction_tensor_insertability_route"],
            description=description,
        ))

    all_obligation_ids = [o[0] for o in required_obligations]

    # Candidate routes
    ns.record_route(RouteRecord(
        route_id="compact_support_zero_flux_candidate_route_19",
        script_id=SCRIPT_ID,
        name="Compact support with structural zero exterior flux",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=all_obligation_ids,
        activation_conditions=[
            "support is derived, smooth, and not solution-tailored",
            "zero-flux follows from tensor/source law",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="divergence_free_interior_neutral_boundary_route_19",
        script_id=SCRIPT_ID,
        name="Identically divergence-free interior tensor with neutral boundary",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=all_obligation_ids,
        activation_conditions=[
            "identity and boundary neutrality both derived",
            "not Bianchi smoke",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="diagnostic_only_boundary_safe_route_19",
        script_id=SCRIPT_ID,
        name="Diagnostic-only correction tensor (no boundary/mass effect)",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=["not inserted into field equation"],
    ))

    # BM22 BRANCH_KILLED -> DEFERRED_PENDING_PREREQUISITES per governance rule 5
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_boundary_mass_neutrality_failure_branch_19",
        script_id=SCRIPT_ID,
        branch_id="correction_tensor_boundary_mass_neutrality_failure",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=all_obligation_ids,
        description=(
            "BM22 failure condition: if correction tensors cannot avoid boundary repair or exterior mass shift, "
            "they remain deferred or diagnostic-only. Mapped to DEFERRED_PENDING_PREREQUISITES because "
            "no contradiction has been demonstrated — boundary/mass neutrality prerequisites are simply absent."
        ),
    ))

    # Rejected routes
    for decision_id, branch_id, description in [
        ("reject_H_boundary_repair_tensor_19", "H_boundary_repair_tensor", "BM17: boundary repair tensor rejected by policy."),
        ("reject_H_M_ext_correction_19", "H_M_ext_correction_tensor", "BM18: M_ext correction tensor rejected by policy."),
        ("reject_H_scalar_tail_cancellation_19", "H_scalar_tail_cancellation_tensor", "BM19: scalar tail cancellation tensor rejected by policy."),
        ("reject_H_shell_source_hiding_19", "H_shell_source_hiding_tensor", "BM20: shell-source hiding tensor rejected by policy."),
        ("reject_H_recovery_boundary_fit_19", "H_recovery_boundary_fit", "BM21: recovery boundary fit rejected by policy."),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    # Summary claim
    ns.record_claim(ClaimRecord(
        claim_id="boundary_mass_neutrality_not_derived_19",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.NOT_INSERTABLE_YET,
        statement=(
            "Boundary/mass neutrality for correction tensors is required but not derived. "
            "All nine neutrality obligations remain open."
        ),
        obligation_ids=all_obligation_ids,
    ))


def main():
    header("Candidate Correction Tensor Boundary And Mass Neutrality")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_safe_routes(out)
    case_4b_compact_support_sample(ns, out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

        record_governance(ns)
        ns.record_derivation(
            derivation_id="correction_tensor_boundary_and_mass_neutrality_marker",
            inputs=[],
            output=sp.Symbol("correction_tensor_boundary_and_mass_neutrality_complete"),
            method="correction_tensor_boundary_and_mass_neutrality",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
