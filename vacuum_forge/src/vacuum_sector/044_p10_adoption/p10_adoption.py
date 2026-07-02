#!/usr/bin/env python3
"""
p10_adoption.py

Adoption record for P10, the packing axiom.

Theory-owner decision, 2026-07-01: the Regge/Delaunay packing model is
ADOPTED as the vacuum's strain microphysics, closing the strain-axiom
question opened at derivation 001 and formalized by the 031 contract.
This script records the adoption with its fence, falsifiers, and
obligations, and re-verifies (as lightweight adoption-time witnesses)
the two exact numbers the axiom is anchored to.

The adoption's epistemic record, stated honestly in the postulate file:
unlike P7'/P9 (adopted before consequences), P10 is adopted AFTER the
037-043 verification campaign, on coherence evidence, with falsifiers
pre-registered. Forward evidential weight must come from consequences
not yet checked.
"""

from pathlib import Path

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


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"

DEPENDENCIES = [
    ("bridge_dep_044", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
    ("convergence_dep_044", "040_regge_refinement_convergence__regge_refinement_convergence",
     "regge_refinement_convergence_040"),
    ("lab_dep_044", "041_frustration_relaxation_lab__frustration_relaxation_lab",
     "frustration_relaxation_lab_041"),
    ("contract_dep_044", "042_discrete_conservation_boundary__discrete_conservation_boundary",
     "discrete_conservation_boundary_042"),
    ("lift_dep_044", "043_lorentzian_4d_lift__lorentzian_4d_lift",
     "lorentzian_4d_lift_043"),
]


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
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
    print("[INFO] Archive dependency check (the adoption's evidentiary base):")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def adoption_witnesses(failures):
    header("Adoption-time witnesses (the axiom's two anchor numbers)")
    Delta0 = 2 * sp.pi - 5 * sp.acos(sp.Rational(1, 3))
    require("the frustration deficit is positive: Delta_0 = 2 pi - 5 arccos(1/3) > 0",
            bool(sp.simplify(Delta0).evalf() > 0), failures)
    phi = (1 + sp.sqrt(5)) / 2
    ratio = 120 * Delta0 / (sp.pi**2 * phi)
    require("the 600-cell Regge/EH anchor: 120 Delta_0/(pi^2 phi) in (0.96, 0.97)",
            0.96 < float(ratio) < 0.97, failures)
    print(f"  Delta_0 = {float(Delta0):.6f} rad; EH anchor ratio = {float(ratio):.4f}")


def record_adoption(ns):
    ns.record_derivation(
        derivation_id="p10_adoption_record_044",
        inputs=[sp.Symbol(f"derivation_{n}") for n in
                ("039", "040", "041", "042", "043")],
        output=sp.Symbol("P10_adopted_2026_07_01_fenced_falsifiers_preregistered"),
        method=(
            "theory-owner adoption decision following the completed nine-field "
            "strain-axiom contract and the adoption briefing; anchor witnesses "
            "re-verified at adoption time"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="postulate_adoption_record",
        scope=(
            "adoption record; the postulate's content lives in "
            "theory_v3/01_postulates/p10_packing_axiom.md; the implied theory "
            "in theory_v3/05_vacuum_sector/"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="strain_axiom_adoption_decided_044",
        script_id=SCRIPT_ID,
        title="Strain-axiom adoption decision: ADOPTED (P10)",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["p10_adoption_record_044"],
        description=(
            "Resolves strain_axiom_adoption_decision_required_032 / _live_042: "
            "the packing axiom is adopted as P10, theory-owner decision, "
            "2026-07-01, with fence and pre-registered falsifiers "
            "(F-P10-1 volume-mode restoring force; F-P10-2 floor/conversion-"
            "factor split; F-P10-3 inherited P7' null test)."
        ),
    ))
    for oid, title, desc in [
        ("O_P10_1_microphysics_constants_044",
         "Derive/reduce a and c_e (conversion-factor derivation)",
         "The floor-Newton lock leaves two constants; same thread as discreteness."),
        ("O_P10_2_4d_ground_coordination_044",
         "4D ground coordination (opposite-sign deficits at n = 4 vs 5)",
         "Euclidean-4D vs (3+1) spatial packing relationship included."),
        ("O_P10_3_p7prime_tension_044",
         "Resolve the a^2-suppressed R^2 term against exact P7'",
         "Cancellation/routing into the constraint sector, or scoped idealization."),
        ("O_P10_4_lorentzian_dynamics_044",
         "Lorentzian dynamics beyond kinematic + linearized (043 scope)",
         "Initial-value formulation; the CDT-adjacent frontier."),
        ("O_P10_5_bulk_relaxation_phase2_044",
         "Bulk relaxation phase 2 (intensivity, disclination networks, spectrum)",
         "The experimental arm; feeder for the dark-excess gates."),
    ]:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=oid, script_id=SCRIPT_ID, title=title,
            status=ObligationStatus.OPEN,
            required_by=["p10_adoption_record_044"],
            description=desc,
        ))
    ns.record_claim(ClaimRecord(
        claim_id="p10_adoption_claim_044",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "P10 (the packing axiom) is adopted, 2026-07-01, by theory-owner "
            "decision, closing the strain-axiom question: the vacuum substance "
            "is a packing whose frustrated flat ground state realizes P1/P3's "
            "substance energy as uniform strain and whose generic leading "
            "response is Einstein-Hilbert (the expansion-point theorem). The "
            "fence excludes dark-excess abundance, non-gravitational channels, "
            "interior scales, and matter-as-defect; the falsifiers are "
            "pre-registered; obligations O-P10-1..5 are on the books. The "
            "adoption is on coherence evidence (post-verification), stated "
            "honestly in the postulate file; forward weight comes from "
            "consequences not yet checked."
        ),
        derivation_ids=["p10_adoption_record_044"],
        obligation_ids=["strain_axiom_adoption_decided_044"],
    ))


def main() -> None:
    header("Derivation 044: P10 Adoption Record")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    adoption_witnesses(failures)

    header("Record")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 044: witness failure -- adoption NOT recorded")
    print("  P10 adopted (theory owner, 2026-07-01). Fence, falsifiers, and")
    print("  obligations recorded. The strain-axiom question is closed; the")
    print("  section of record is theory_v3/05_vacuum_sector/.")

    record_adoption(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
