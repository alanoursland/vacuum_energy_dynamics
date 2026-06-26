#!/usr/bin/env python3
"""
strain_axiom_candidate_sieve.py

VacuumForge-managed sieve for currently named strain-axiom routes.

This does not adopt an axiom. It checks whether any currently named route
satisfies the minimal strain axiom contract.

Output:
    theory_v3/development/vacuum_sector/01_strain_functional/
        strain_axiom_candidate_sieve_vacuumforge.md
"""

from dataclasses import dataclass
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
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (
    REPO_ROOT
    / "theory_v3"
    / "development"
    / "vacuum_sector"
    / "01_strain_functional"
    / "strain_axiom_candidate_sieve_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "minimal_strain_axiom_contract_031",
        "031_minimal_strain_axiom_contract__minimal_strain_axiom_contract",
        "minimal_strain_axiom_contract_031",
    )
]


@dataclass(frozen=True)
class CandidateAxiom:
    candidate_id: str
    candidate: str
    x_variable: int
    metric_response_map: int
    neighboring_mismatch: int
    strain_invariant: int
    boundary_variation: int
    conservation_identity: int
    mode_hyperbolicity: int
    epsilon_classification: int
    falsifier: int
    nonbaseline: int
    rejected: int
    decision: str
    next_obligation: str
    governance_status: GovernanceStatus

    @property
    def field_count(self) -> int:
        return (
            self.x_variable
            + self.metric_response_map
            + self.neighboring_mismatch
            + self.strain_invariant
            + self.boundary_variation
            + self.conservation_identity
            + self.mode_hyperbolicity
            + self.epsilon_classification
            + self.falsifier
        )

    @property
    def satisfies_contract(self) -> bool:
        return self.field_count == 9 and not self.rejected

    @property
    def licenses_nonbaseline(self) -> bool:
        return bool(self.satisfies_contract and self.nonbaseline)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_equal(label, lhs, rhs) -> None:
    residual = simplify_expr(lhs - rhs)
    if residual != 0:
        raise AssertionError(f"{label} failed: {residual}")


def require_true(label, condition) -> None:
    if not bool(condition):
        raise AssertionError(f"{label} failed")


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def candidates():
    return [
        CandidateAxiom(
            candidate_id="no_new_axiom_baseline",
            candidate="retain accumulated-gate EH/GHY baseline",
            x_variable=1,
            metric_response_map=1,
            neighboring_mismatch=1,
            strain_invariant=1,
            boundary_variation=1,
            conservation_identity=1,
            mode_hyperbolicity=1,
            epsilon_classification=1,
            falsifier=1,
            nonbaseline=0,
            rejected=0,
            decision="passes only as epsilon = 0 baseline",
            next_obligation="do not claim nonbaseline physics",
            governance_status=GovernanceStatus.LICENSED_CLAIM,
        ),
        CandidateAxiom(
            candidate_id="primitive_nonmetric_x_axiom",
            candidate="postulate deeper nonmetric X",
            x_variable=1,
            metric_response_map=0,
            neighboring_mismatch=0,
            strain_invariant=0,
            boundary_variation=0,
            conservation_identity=0,
            mode_hyperbolicity=0,
            epsilon_classification=0,
            falsifier=0,
            nonbaseline=1,
            rejected=0,
            decision="fails current sieve; X name alone is not a strain axiom",
            next_obligation="supply response map, mismatch, invariant, boundary, modes, and falsifier",
            governance_status=GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
        ),
        CandidateAxiom(
            candidate_id="primitive_mismatch_axiom",
            candidate="postulate non-Levi-Civita neighboring mismatch",
            x_variable=0,
            metric_response_map=0,
            neighboring_mismatch=1,
            strain_invariant=0,
            boundary_variation=0,
            conservation_identity=0,
            mode_hyperbolicity=0,
            epsilon_classification=0,
            falsifier=0,
            nonbaseline=1,
            rejected=0,
            decision="fails current sieve; mismatch name alone is not a variational branch",
            next_obligation="supply X, invariant, boundary, conservation, modes, and epsilon route",
            governance_status=GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION,
        ),
        CandidateAxiom(
            candidate_id="nonlocal_relaxation_axiom",
            candidate="postulate nonlocal relaxation/history selector",
            x_variable=0,
            metric_response_map=0,
            neighboring_mismatch=1,
            strain_invariant=0,
            boundary_variation=0,
            conservation_identity=0,
            mode_hyperbolicity=0,
            epsilon_classification=0,
            falsifier=0,
            nonbaseline=1,
            rejected=0,
            decision="deferred; not local strain physics without local GR limit and source quarantine",
            next_obligation="route through nonlocal/large-scale ledger before local branch claims",
            governance_status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        ),
        CandidateAxiom(
            candidate_id="boundary_global_axiom",
            candidate="postulate boundary/topology/admissibility strain-class selector",
            x_variable=0,
            metric_response_map=0,
            neighboring_mismatch=0,
            strain_invariant=0,
            boundary_variation=1,
            conservation_identity=0,
            mode_hyperbolicity=0,
            epsilon_classification=0,
            falsifier=0,
            nonbaseline=1,
            rejected=0,
            decision="deferred; class restriction is not K_strain selection",
            next_obligation="derive local variational object and scale before action claims",
            governance_status=GovernanceStatus.POLICY_RULE,
        ),
        CandidateAxiom(
            candidate_id="metric_relabeling_axiom",
            candidate="declare X = g_ab and call EH/GHY ontology",
            x_variable=1,
            metric_response_map=1,
            neighboring_mismatch=1,
            strain_invariant=1,
            boundary_variation=1,
            conservation_identity=1,
            mode_hyperbolicity=1,
            epsilon_classification=1,
            falsifier=0,
            nonbaseline=0,
            rejected=1,
            decision="rejected as derivation; baseline use is allowed, relabeling is not selection",
            next_obligation="keep as baseline comparison only",
            governance_status=GovernanceStatus.REJECTED_ROUTE,
        ),
        CandidateAxiom(
            candidate_id="mechanism_fit_axiom",
            candidate="choose axiom to fit Lambda, dark, channel, or interior target",
            x_variable=0,
            metric_response_map=0,
            neighboring_mismatch=0,
            strain_invariant=0,
            boundary_variation=0,
            conservation_identity=0,
            mode_hyperbolicity=0,
            epsilon_classification=0,
            falsifier=0,
            nonbaseline=1,
            rejected=1,
            decision="rejected as post-hoc mechanism rescue",
            next_obligation="do not use as derivation",
            governance_status=GovernanceStatus.REJECTED_ROUTE,
        ),
    ]


def run_sympy_checks(rows):
    licensed_nonbaseline = sum(1 for row in rows if row.licenses_nonbaseline)
    adopted_candidates = [row.candidate_id for row in rows if row.licenses_nonbaseline]
    baseline_passes = [row.candidate_id for row in rows if row.satisfies_contract and not row.nonbaseline]
    open_nonbaseline = [
        row.candidate_id
        for row in rows
        if row.nonbaseline and not row.rejected and not row.satisfies_contract
    ]
    rejected = sum(row.rejected for row in rows)

    require_equal("no nonbaseline candidate axiom passes", licensed_nonbaseline, 0)
    require_true("baseline still passes as null route", baseline_passes == ["no_new_axiom_baseline"])
    require_true("open nonbaseline candidates remain incomplete", len(open_nonbaseline) >= 1)
    require_true("bad candidate routes are rejected", rejected >= 1)

    return {
        "licensed_nonbaseline": licensed_nonbaseline,
        "adopted_candidates": adopted_candidates,
        "baseline_passes": baseline_passes,
        "open_nonbaseline": open_nonbaseline,
        "rejected": rejected,
    }


def markdown_candidates(rows):
    return "\n".join(
        (
            "| {candidate_id} | {candidate} | {field_count}/9 | {satisfies} | "
            "{nonbaseline} | {rejected} | {decision} | {next_obligation} |"
        ).format(
            candidate_id=row.candidate_id,
            candidate=row.candidate,
            field_count=row.field_count,
            satisfies=row.satisfies_contract,
            nonbaseline=bool(row.nonbaseline),
            rejected=bool(row.rejected),
            decision=row.decision,
            next_obligation=row.next_obligation,
        )
        for row in rows
    )


def field_rows(rows):
    return "\n".join(
        (
            "| {candidate_id} | {x} | {metric} | {mismatch} | {invariant} | "
            "{boundary} | {conservation} | {modes} | {epsilon} | {falsifier} |"
        ).format(
            candidate_id=row.candidate_id,
            x=bool(row.x_variable),
            metric=bool(row.metric_response_map),
            mismatch=bool(row.neighboring_mismatch),
            invariant=bool(row.strain_invariant),
            boundary=bool(row.boundary_variation),
            conservation=bool(row.conservation_identity),
            modes=bool(row.mode_hyperbolicity),
            epsilon=bool(row.epsilon_classification),
            falsifier=bool(row.falsifier),
        )
        for row in rows
    )


def write_report(rows, data):
    candidates_md = markdown_candidates(rows)
    fields_md = field_rows(rows)
    adopted = ", ".join(data["adopted_candidates"]) or "none"
    open_nonbaseline = ", ".join(data["open_nonbaseline"]) or "none"
    baseline = ", ".join(data["baseline_passes"]) or "none"
    md = f"""# VacuumForge Strain Axiom Candidate Sieve

## Purpose

This report applies the minimal strain axiom contract to the currently named
axiom routes. It does not adopt an axiom.

It depends on:

```text
minimal_strain_axiom_contract_031
```

It satisfies:

```text
strain_axiom_candidate_sieve_required_031
```

## Sieve Result

```text
licensed nonbaseline candidate axioms = {data["licensed_nonbaseline"]}
adopted nonbaseline candidates = {adopted}
baseline/null pass route = {baseline}
open incomplete nonbaseline routes = {open_nonbaseline}
rejected routes = {data["rejected"]}
```

## Candidate Summary

| candidate id | candidate | fields present | satisfies contract | nonbaseline | rejected | decision | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
{candidates_md}

## Field Coverage

| candidate id | X | metric map | mismatch | invariant | boundary | conservation | modes | epsilon | falsifier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{fields_md}

## Current Conclusion

No currently named nonbaseline strain axiom satisfies the minimal contract.
The only passing route is the baseline/null route: keep the accumulated-gate
EH/GHY baseline at `epsilon = 0`. This is not a new strain axiom.

Primitive nonmetric-X and primitive-mismatch routes remain open only as
incomplete axiom candidates. Nonlocal and boundary/global routes are deferred.
Metric relabeling and mechanism-fit axioms are rejected.

## Classification

```text
result type: strain axiom candidate sieve
scope: currently named axiom routes
conclusion: no nonbaseline axiom candidate passes
non-conclusion: no no-go theorem against a future fully specified axiom
```

The next technical target is:

```text
strain_axiom_adoption_decision_required_032
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, rows):
    marker_id = "strain_axiom_candidate_sieve_032"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("minimal_strain_axiom_contract_result")],
        output=sp.Symbol("strain_axiom_candidate_sieve_result"),
        method="VacuumForge candidate-field sieve with SymPy count checks",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Sieve currently named strain axiom routes against the minimal contract",
    )

    for row in rows:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"strain_axiom_candidate_{row.candidate_id}_032",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=row.governance_status,
                statement=f"{row.candidate_id}: {row.decision}",
                derivation_ids=[marker_id],
                obligation_ids=["strain_axiom_adoption_decision_required_032"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="strain_axiom_candidate_sieve_required_031",
            script_id=SCRIPT_ID,
            title="Apply a candidate sieve to possible strain axiom routes",
            status=ObligationStatus.SATISFIED,
            required_by=["031_minimal_strain_axiom_contract__minimal_strain_axiom_contract"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by checking each currently named candidate route "
                "against the required axiom fields and confirming no "
                "nonbaseline route passes."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="strain_axiom_adoption_decision_required_032",
            script_id=SCRIPT_ID,
            title="Decide whether to adopt a new strain axiom or freeze nonbaseline branch work",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "After the candidate sieve finds no passing nonbaseline axiom, "
                "the program must either adopt a fully specified explicit "
                "axiom or keep nonbaseline mechanisms quarantined."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 032: Strain Axiom Candidate Sieve")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    rows = candidates()
    data = run_sympy_checks(rows)

    out = ScriptOutput()
    for row in rows:
        if row.rejected:
            status = StatusMark.FAIL
        elif row.governance_status == GovernanceStatus.LICENSED_CLAIM:
            status = StatusMark.PASS
        elif row.governance_status == GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION:
            status = StatusMark.OBLIGATION
        else:
            status = StatusMark.DEFER
        with out.governance_assessments():
            out.line(row.candidate_id, status, row.decision)
    with out.unresolved_obligations():
        out.line(
            "Strain axiom adoption decision required",
            StatusMark.OBLIGATION,
            "adopt a full axiom or keep nonbaseline mechanisms quarantined",
        )

    record_archive(ns, rows)
    ns.write_run_metadata()
    write_report(rows, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
