"""Tests for VacuumForge governance-validation support."""

from __future__ import annotations

import json

import sympy as sp

from vacuumforge import TheoryContext
from vacuumforge.archive import ProjectArchive
from vacuumforge.core.status import Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    HandoffImportRecord,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
    RouteRecord,
    classify_derivation_record,
)
from vacuumforge.governance.order_check import check_group_order
from vacuumforge.governance.summaries import GovernanceSummaryBuilder, check_claim_strength_upgrade
from vacuumforge.governance.kinds import DerivationRecordQuality
from vacuumforge.governance.output import ScriptOutput


def test_governance_enums_round_trip_values():
    assert RecordKind.SAMPLE_DERIVATION.value == "sample_derivation"
    assert ClaimTier.EXCLUSION.value == "exclusion"
    assert GovernanceStatus.UNPROVEN_EXCLUSION.value == "unproven_exclusion"
    assert EvidenceType.OVERLAP_WITNESS.value == "overlap_witness"
    assert ReasonCode.RECOVERY_SELECTED_PARAMETER.value == "recovery_selected_parameter"


def test_archive_records_evidence_and_obligation(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")
    x = sp.Symbol("x")

    ev = ns.record_evidence(
        EvidenceRecord(
            evidence_id="bad_overlap",
            evidence_type=EvidenceType.OVERLAP_WITNESS,
            script_id="script",
            observed=x + 1,
            expected=sp.Integer(0),
            residual=x + 1,
        )
    )
    obligation = ns.record_obligation(
        ProofObligationRecord(
            obligation_id="derive_boundary_neutrality",
            script_id="script",
            title="Derive boundary neutrality",
            status=ObligationStatus.OPEN,
        )
    )

    assert ns.get_evidence(ev.evidence_id).residual == x + 1
    assert ns.get_obligation(obligation.obligation_id).status == ObligationStatus.OPEN

    updated = ns.update_obligation_status(
        "derive_boundary_neutrality",
        ObligationStatus.SATISFIED,
        by="script:derivation",
    )
    assert updated.status == ObligationStatus.SATISFIED
    assert "script:derivation" in updated.satisfied_by


def test_unsupported_branch_kill_is_downgraded(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")

    decision = ns.record_branch_decision(
        BranchDecisionRecord(
            decision_id="kill_route",
            script_id="script",
            branch_id="route",
            status=GovernanceStatus.KILLED_BY_CONTRADICTION,
            tier=ClaimTier.EXCLUSION,
        )
    )

    assert decision.status == GovernanceStatus.UNPROVEN_EXCLUSION
    assert decision.metadata["validation"]["requested_status"] == "killed_by_contradiction"
    assert decision.metadata["validation"]["effective_status"] == "unproven_exclusion"


def test_supported_branch_kill_remains_strong(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")
    ns.record_evidence(
        EvidenceRecord(
            evidence_id="scalar_charge",
            evidence_type=EvidenceType.EXTERIOR_SCALAR_CHARGE_WITNESS,
            script_id="script",
            reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
        )
    )

    decision = ns.record_branch_decision(
        BranchDecisionRecord(
            decision_id="kill_route",
            script_id="script",
            branch_id="route",
            status=GovernanceStatus.FAILED_BY_WITNESS,
            tier=ClaimTier.EXCLUSION,
            reason_code=ReasonCode.EXTERIOR_SCALAR_CHARGE,
            evidence_ids=["scalar_charge"],
        )
    )

    assert decision.status == GovernanceStatus.FAILED_BY_WITNESS
    assert decision.metadata["validation"]["supported"] is True


def test_licensed_route_with_only_sample_support_downgrades(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")

    route = ns.record_route(
        RouteRecord(
            route_id="safe_route",
            script_id="script",
            name="Safe route",
            status=GovernanceStatus.LICENSED_CLAIM,
            tier=ClaimTier.LICENSING,
        )
    )

    assert route.status == GovernanceStatus.CANDIDATE_ROUTE


def test_claim_tier_two_without_reason_downgrades_to_heuristic(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")

    claim = ns.record_claim(
        ClaimRecord(
            claim_id="risk",
            script_id="script",
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.OPEN_RISK,
            statement="Route has unresolved overlap.",
        )
    )

    assert claim.status == "heuristic"


def test_expected_dependency_status_kind_and_supersession(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sp.Symbol("x")

    upstream = archive.script_namespace("upstream")
    upstream.record_derivation(
        "sample",
        [x],
        x,
        "sample",
        Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
    )
    upstream.record_derivation(
        "old",
        [x],
        x,
        "algebraic",
        Status.DERIVED,
        superseded_by="new",
    )

    downstream = archive.script_namespace("downstream")
    downstream.declare_dependency(
        "expects_real_derivation",
        "upstream",
        "sample",
        expected_record_kind=RecordKind.DERIVATION,
    )
    downstream.declare_dependency("uses_superseded", "upstream", "old")
    results = {r.dependency.dependency_id: r for r in downstream.verify_dependencies()}

    assert results["expects_real_derivation"].status == "dependency_kind_mismatch"
    assert results["uses_superseded"].status == "dependency_superseded"


def test_derivation_quality_classification(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")
    x = sp.Symbol("x")
    placeholder = ns.record_derivation(
        "marker",
        [],
        sp.Symbol("marker_stated"),
        "script_marker",
        Status.DERIVED,
    )
    contentful = ns.record_derivation("identity", [x], sp.simplify(x - x), "simplify", Status.DERIVED)
    sample = ns.record_derivation(
        "sample",
        [x],
        x,
        "toy",
        Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
    )

    assert classify_derivation_record(placeholder) == DerivationRecordQuality.PLACEHOLDER
    assert classify_derivation_record(contentful) == DerivationRecordQuality.CONTENTFUL
    assert classify_derivation_record(sample) == DerivationRecordQuality.SAMPLE


def test_context_has_governance_manager():
    ctx = TheoryContext("gov")
    ctx.governance.record_evidence(
        EvidenceRecord(
            evidence_id="counter",
            evidence_type=EvidenceType.COUNTEREXAMPLE,
            script_id="notebook",
        )
    )
    assert ctx.governance.has_evidence("counter")


def test_archive_cli_list_shows_governance_counts(tmp_path, capsys):
    from vacuumforge.archive.cli import _cmd_list

    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")
    ns.record_evidence(
        EvidenceRecord(
            evidence_id="ev",
            evidence_type=EvidenceType.COUNTEREXAMPLE,
            script_id="script",
        )
    )

    _cmd_list(ns)
    out = capsys.readouterr().out
    assert "Governance records" in out
    assert "Evidence: 1" in out


def test_governance_records_are_json(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="open",
            script_id="script",
            title="Open thing",
            status=ObligationStatus.OPEN,
        )
    )
    data = json.loads((ns.obligations_path / "open.json").read_text(encoding="utf-8"))
    assert data["status"] == "open"


def test_archive_queries_and_summary_builder(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("script")
    x = sp.Symbol("x")
    ns.record_derivation("derived", [x], x, "algebraic", Status.DERIVED)
    ns.record_derivation(
        "sample",
        [x],
        x,
        "toy",
        Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
    )
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="open",
            script_id="script",
            title="Open proof",
            status=ObligationStatus.OPEN,
        )
    )
    ns.record_evidence(
        EvidenceRecord(
            evidence_id="counter",
            evidence_type=EvidenceType.COUNTEREXAMPLE,
            script_id="script",
        )
    )
    ns.record_handoff_import(
        HandoffImportRecord(
            handoff_id="handoff",
            script_id="script",
            imported_as=RecordKind.DERIVATION,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            imported_record_refs=["script:derived", "script:sample"],
        )
    )

    assert len(archive.query_obligations(status="open")) == 1
    summary = GovernanceSummaryBuilder(archive).build(["script"])
    assert summary.derived_results == ["script:derived"]
    assert summary.sample_results == ["script:sample"]
    assert len(summary.open_obligations) == 1
    assert len(summary.counterexamples) == 1
    assert len(summary.handoff_imports) == 1
    assert "Derived results: 1" in summary.to_markdown()
    assert "Counterexamples: 1" in summary.to_markdown()


def test_claim_strength_upgrade_detection():
    upstream = ClaimRecord(
        claim_id="candidate",
        script_id="upstream",
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement="Candidate route.",
    )
    summary = ClaimRecord(
        claim_id="licensed",
        script_id="summary",
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement="Licensed route.",
        source_claim_ids=["candidate"],
    )
    result = check_claim_strength_upgrade(summary, [upstream])
    assert result.upgraded is True


def test_provisional_convention_upgrade_from_candidate_is_detected():
    upstream = ClaimRecord(
        claim_id="candidate",
        script_id="upstream",
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement="Candidate route.",
    )
    summary = ClaimRecord(
        claim_id="provisional",
        script_id="summary",
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement="Provisional convention.",
        source_claim_ids=["candidate"],
    )
    result = check_claim_strength_upgrade(summary, [upstream])
    assert result.upgraded is True


def test_script_output_blocks(capsys):
    out = ScriptOutput()
    with out.derived_results():
        out.line("identity", "PASS", "residual zero")
    with out.unresolved_obligations():
        out.line("derive theorem", "OPEN")
    text = capsys.readouterr().out
    assert "[derived_results]" in text
    assert "[unresolved_obligations]" in text
    assert out.events[0].block == "derived_results"
    assert out.events[1].block == "unresolved_obligations"


def test_handoff_import_record_supports_multiple_refs():
    record = HandoffImportRecord(
        handoff_id="h",
        script_id="s",
        imported_as=RecordKind.DERIVATION,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        source_record_ref="s:a",
        imported_record_refs=["s:b"],
    )
    assert record.imported_record_refs == ["s:b", "s:a"]


def test_script_metadata_and_order_check(tmp_path):
    group = tmp_path / "01_group"
    group.mkdir()
    (group / "a.py").write_text(
        "# Group: 01_group\n# Script type: DERIVATION\nprint('a')\n",
        encoding="utf-8",
    )
    (group / "b_summary.py").write_text(
        "# Group: 01_group\n# Script type: SUMMARY\nprint('b')\n",
        encoding="utf-8",
    )
    (group / "order.txt").write_text("a.py\nb_summary.py\n", encoding="utf-8")
    result = check_group_order(group)
    assert result.ok
    assert result.warnings == []


def test_order_check_catches_missing_and_duplicate(tmp_path):
    group = tmp_path / "bad_group"
    group.mkdir()
    (group / "a.py").write_text("print('a')\n", encoding="utf-8")
    (group / "order.txt").write_text("a.py\na.py\nmissing.py\n", encoding="utf-8")
    result = check_group_order(group)
    assert not result.ok
    assert any("missing file" in e for e in result.errors)
    assert any("more than once" in e for e in result.errors)
