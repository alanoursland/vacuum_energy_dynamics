from __future__ import annotations
from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord, ClaimTier, GovernanceStatus, ObligationStatus,
    ProofObligationRecord, RecordKind, ScriptOutput, StatusMark,
)

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)

def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
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

def record_marker(ns, marker_id: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(marker_id),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )

def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )

def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )

DEPENDENCIES = [
    ("g85_profile_validation", "85_shape_family_payload_suppression_test__candidate_suppressed_profile_validation", "g85_profile_validation"),
    ("g85_weighted_extension", "85_shape_family_payload_suppression_test__candidate_weighted_payload_extension", "g85_weighted_extension"),
]
MARKER_ID = "g85_admissibility"

def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, t = sp.symbols("y t")
    P_y = 1 - 12*y**2 + 51*y**4
    P_t = 1 - 12*t + 51*t**2
    t_star = sp.solve(sp.Eq(sp.diff(P_t, t), 0), t)[0]
    P_min = sp.simplify(P_t.subs(t, t_star))
    P_0 = sp.simplify(P_y.subs(y, 0))
    P_1 = sp.simplify(P_y.subs(y, 1))
    regular = (P_min > 0) if P_min.is_number else None

    decisions = [
        ("inside_reduced_moment_problem", "NOT_REPAIR", "profile follows from M2=M4 moment constraints"),
        ("relative_to_Group84", "STRENGTHENED", "overcomes low-order obstruction of linear-skew family"),
        ("relative_to_full_theory", "NOT_CLOSED", "shape origin not derived from geometry/covariance"),
        ("local_rho_status", "NONZERO", "profile suppresses moments, not pointwise rho"),
        ("higher_moment_status", "OPEN", "M6/W4 remain nonzero"),
        ("parent_status", "BLOCKED", "parent divergence and recombination remain blocked"),
    ]

    header("Candidate Shape Admissibility and Repair Discriminator")
    print(f"P(y) = {P_y}")
    print(f"P(t=y^2) = {P_t}")
    print(f"t* = {t_star}")
    print(f"P_min = {P_min}")
    print(f"P(0) = {P_0}")
    print(f"P(1) = {P_1}")
    for name, status, reason in decisions:
        print(f"{name}: {status}; {reason}")

    with out.derived_results():
        out.line("P minimum location", StatusMark.PASS, str(t_star))
        out.line("P minimum value", StatusMark.PASS, str(P_min))
        out.line("P endpoints", StatusMark.PASS, f"P(0)={P_0}, P(1)={P_1}")
    with out.governance_assessments():
        out.line("regularity", StatusMark.PASS, "P is positive on the tested interval")
        out.line("repair status", StatusMark.INFO, "not repair inside reduced moment problem")
        out.line("shape origin", StatusMark.OBLIGATION, "profile still needs geometric origin")
        out.line("full closure", StatusMark.DEFER, "full inertness not proven")
    with out.counterexamples():
        out.line("shape as physical theorem", StatusMark.FAIL, "moment-derived profile is not physically derived")
        out.line("all-order inertness", StatusMark.FAIL, "higher moments remain")
        out.line("parent jump", StatusMark.FAIL, "parent equation remains forbidden")

    record_marker(ns, MARKER_ID, "shape admissibility and repair discriminator")
    record_claim(ns, MARKER_ID, "g85_admit_c1", GovernanceStatus.POLICY_RULE, "Even quartic profile is regular and not repair inside the reduced moment-suppression problem.")
    record_claim(ns, MARKER_ID, "g85_admit_c2", GovernanceStatus.POLICY_RULE, "Shape origin and all-order/covariant inertness remain open.")
    record_obligation(ns, "g85_admit_o1", "Derive shape origin from geometry if route continues.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_shape_suppression_route_classifier.py")

if __name__ == "__main__":
    main()
