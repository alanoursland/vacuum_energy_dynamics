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
    print(); print("=" * 120); print(title); print("=" * 120)


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT); ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(dependency_id=dep_id, upstream_script_id=upstream_script_id, upstream_derivation_id=upstream_derivation_id)
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated: print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared."); return
    print("[INFO] Archive dependency check:")
    for check in checks: print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def record_claim(ns, marker_id: str, claim_id: str, status: GovernanceStatus, statement: str) -> None:
    ns.record_claim(ClaimRecord(claim_id=claim_id, script_id=SCRIPT_ID, claim_kind=RecordKind.GOVERNANCE_CLAIM, tier=ClaimTier.CONSTRAINED, status=status, statement=statement, derivation_ids=[marker_id], obligation_ids=[]))


def record_obligation(ns, obligation_id: str, statement: str, status: ObligationStatus = ObligationStatus.OPEN) -> None:
    ns.record_obligation(ProofObligationRecord(obligation_id=obligation_id, script_id=SCRIPT_ID, title=obligation_id, status=status, required_by=[SCRIPT_ID], description=statement))


DEPENDENCIES = [
    ("g73_signed_distance", "73_layer_generator_construction__candidate_signed_distance_layer_scaffold", "g73_signed_distance"),
]
MARKER_ID = "g73_measure_origin"


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES); print_archive_status(ns, invalidated)
    out = ScriptOutput()

    y, R, ell, c = sp.symbols("y R ell c", nonzero=True)
    measure = sp.expand((R + ell*y)**2)
    w = (1 - y**2)**2
    profile = w * (y - c)
    weighted_charge = sp.factor(sp.integrate(measure * profile, (y, -1, 1)))
    c_solution = sp.solve(sp.Eq(weighted_charge, 0), c)
    c_star = sp.simplify(c_solution[0]) if c_solution else sp.nan
    flat_charge_at_cstar = sp.factor(sp.integrate(profile.subs(c, c_star), (y, -1, 1)))

    header("Candidate Boundary Measure Origin Test")
    print(f"boundary/layer measure proxy mu(y) = {measure}")
    print(f"localized profile family = {sp.expand(profile)}")
    print(f"weighted charge = {weighted_charge}")
    print(f"weighted-neutral c = {c_star}")
    print(f"flat charge at weighted-neutral c = {flat_charge_at_cstar}")
    print("Interpretation:")
    print("  boundary measure can force weighted-neutral skew")
    print("  weighted neutrality is a measure constraint, not D_layer legitimacy")

    with out.derived_results():
        out.line("measure", StatusMark.PASS, str(measure))
        out.line("weighted charge", StatusMark.PASS, str(weighted_charge))
        out.line("weighted neutral skew", StatusMark.PASS, str(c_star))
    with out.governance_assessments():
        out.line("measure scaffold", StatusMark.INFO, "geometry-aware measure can constrain layer profile")
        out.line("legitimacy", StatusMark.OBLIGATION, "measure neutrality does not derive D_layer component role")
    with out.counterexamples():
        out.line("flat neutrality", StatusMark.FAIL, "flat cancellation is not the correct boundary/layer measure")
        out.line("measure as theorem", StatusMark.FAIL, "weighted neutrality is not covariant boundary-component theorem")
        out.line("old N_w promotion", StatusMark.FAIL, "neutralizer-like diagnostics remain evidence, not physical D_layer")
    with out.unresolved_obligations():
        out.line("measure origin", StatusMark.OBLIGATION, "derive boundary/layer measure covariantly")
        out.line("component origin", StatusMark.OBLIGATION, "derive why measured layer object enters D_boundary")

    ns.record_derivation(derivation_id=MARKER_ID, inputs=[], output=c_star, method="solve weighted-neutral skew under boundary/layer measure proxy", status=Status.DERIVED, record_kind=RecordKind.COMPATIBILITY_EXAMPLE, result_type="boundary_measure_neutrality_scaffold", scope="measure constraint; not D_layer theorem")
    record_claim(ns, MARKER_ID, "g73_measure_c1", GovernanceStatus.POLICY_RULE, "Weighted measure constraints can guide layer profiles but do not prove D_layer legitimacy.")
    record_claim(ns, MARKER_ID, "g73_measure_c2", GovernanceStatus.REJECTED_ROUTE, "Flat neutrality or neutralizer diagnostics cannot be promoted into D_layer.")
    record_obligation(ns, "g73_measure_o1", "Derive boundary/layer measure and component role from geometry.")
    ns.write_run_metadata()
    print("\nPossible next script:")
    print("  candidate_component_membership_origin_test.py")


if __name__ == "__main__": main()
