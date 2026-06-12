# Postulate adoption record: P9 and P7'
#
# Group:
#   005_postulate_adoptions
#
# Script type:
#   GOVERNANCE RECORD / HANDOFF IMPORT
#
# Purpose
# -------
# Import the theory-owner postulate adoptions of 2026-06-11 into the trial
# archive as dependable records, and discharge the corresponding open
# obligations from Trials C2 and C3.
#
#   P9  (Configuration Energy Gravitates), with its fence:
#       theory_v3/01_postulates/p9_configuration_energy_gravitates.md
#   P7' (Static Frame Indifference), defined at the limit:
#       theory_v3/01_postulates/p7_prime_static_frame_indifference.md
#
# After this script, downstream trial scripts may declare dependencies on:
#
#   postulate_P9_record_005
#   postulate_P7prime_record_005
#
# This script performs no derivation. It records decisions and the updated
# postulate-set status.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    HandoffImportRecord,
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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="c2_selector_dependency_005",
        upstream_script_id="002_trial_C_burden_ledger__trial_C2_self_coupling_bootstrap",
        upstream_derivation_id="bootstrap_selector_lamda_minus_one_c2",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="c3_equivalence_dependency_005",
        upstream_script_id="002_trial_C_burden_ledger__trial_C3_spatial_bootstrap",
        upstream_derivation_id="tr_block_identity_c3",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


def main() -> None:
    header("Postulate Adoption Record: P9 and P7'")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()

    header("Adoptions")
    print("P9 (Configuration Energy Gravitates), adopted 2026-06-11:")
    print("  'The vacuum's configuration energy gravitates with the same")
    print("   universal per-unit-energy coupling as every other energy.'")
    print("  Fence: source status is earned by presence in the adopted")
    print("  dynamical law, counted exactly once; diagnostic energies do not")
    print("  become sources; no gate is bypassed.")
    print()
    print("P7' (Static Frame Indifference), adopted 2026-06-11, at the limit:")
    print("  'A strictly static vacuum configuration carries no energy")
    print("   current and no preferred frame in the t-r plane.'")
    print("  Limit scoping: exact at H -> 0; real exteriors carry the")
    print("  expansion correction AB - 1 = O(H_0 r/c).")

    # ----- archive records future scripts can depend on -----
    ns.record_derivation(
        derivation_id="postulate_P9_record_005",
        inputs=[],
        output=sp.Symbol("P9_configuration_energy_gravitates"),
        method="theory-owner adoption 2026-06-11; statement and fence in "
               "theory_v3/01_postulates/p9_configuration_energy_gravitates.md",
        status=Status.POSTULATE,
        record_kind=RecordKind.UNARCHIVED_FOUNDATION,
        result_type="adopted_postulate",
        scope="configuration energy sources gravity at the universal P6 coupling; "
              "admission rule: presence in the adopted dynamical law, counted once",
    )
    ns.record_derivation(
        derivation_id="postulate_P7prime_record_005",
        inputs=[],
        output=sp.Symbol("P7prime_static_frame_indifference"),
        method="theory-owner adoption 2026-06-11; statement and limit scoping in "
               "theory_v3/01_postulates/p7_prime_static_frame_indifference.md",
        status=Status.POSTULATE,
        record_kind=RecordKind.UNARCHIVED_FOUNDATION,
        result_type="adopted_postulate",
        scope="strictly static vacuum: no t-r energy current / preferred frame; "
              "AB = 1 as shadow; expansion correction AB - 1 = O(H_0 r/c)",
    )

    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="p9_adoption_import_005",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.UNARCHIVED_FOUNDATION,
        status=Status.POSTULATE,
        source_record_ref="theory_v3/01_postulates/p9_configuration_energy_gravitates.md",
        description="P9 adoption imported; discharges C2 obligation bootstrap_postulate_adoption_c2.",
    ))
    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="p7prime_adoption_import_005",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.UNARCHIVED_FOUNDATION,
        status=Status.POSTULATE,
        source_record_ref="theory_v3/01_postulates/p7_prime_static_frame_indifference.md",
        description="P7' adoption imported; discharges C3 obligation p7_prime_adoption_c3.",
    ))

    # ----- obligation discharge records -----
    ns.record_obligation(ProofObligationRecord(
        obligation_id="discharge_bootstrap_postulate_adoption_005",
        script_id=SCRIPT_ID,
        title="C2 obligation bootstrap_postulate_adoption_c2: SATISFIED by P9 adoption",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["postulate_P9_record_005"],
        description="Theory-owner decision 2026-06-11 adopted P9 with fence.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="discharge_p7_prime_adoption_005",
        script_id=SCRIPT_ID,
        title="C3 obligation p7_prime_adoption_c3: SATISFIED by P7' adoption",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["postulate_P7prime_record_005"],
        description="Theory-owner decision 2026-06-11 adopted P7' with limit scoping.",
    ))

    # ----- the updated postulate-set status claim -----
    ns.record_claim(ClaimRecord(
        claim_id="postulate_set_status_005",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Postulate set after 2026-06-11: P1-P6 (ontology), P7' (static frame "
            "indifference, limit-scoped), P9 (configuration energy gravitates, "
            "fenced). P7 retained as P7''s metric shadow; P8 a 1PN theorem under "
            "P9 (formal rewrite pending). No recovery-shaped postulates remain. "
            "Open sector obligations: G03 radiative positivity; spatial bootstrap "
            "covariant lift; interior behavior."
        ),
        derivation_ids=["postulate_P9_record_005", "postulate_P7prime_record_005"],
    ))

    with out.governance_assessments():
        out.line("P9 recorded as dependable archive object", StatusMark.PASS,
                 "postulate_P9_record_005 (UNARCHIVED_FOUNDATION)")
        out.line("P7' recorded as dependable archive object", StatusMark.PASS,
                 "postulate_P7prime_record_005 (UNARCHIVED_FOUNDATION)")
        out.line("C2/C3 adoption obligations discharged", StatusMark.PASS,
                 "SATISFIED records reference the adoption imports")
        out.line("postulate-set status claim recorded", StatusMark.PASS,
                 "no recovery-shaped postulates remain")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
