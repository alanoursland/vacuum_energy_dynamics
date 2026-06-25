#!/usr/bin/env python3
"""
casimir_ufft_channel_contract.py

VacuumForge-managed contract for the Casimir/UFFT non-gravitational channel.

This is not a derivation of a signal. It separates an apparatus-level
boundary/material response from a gravitational Yukawa residual and records the
missing coupling-operator obligation.

Output:
    theory_v3/development/vacuum_sector/06_non_gravitational_channels/
        casimir_ufft_channel_contract_vacuumforge.md
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
    / "06_non_gravitational_channels"
    / "casimir_ufft_channel_contract_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "non_grav_channel_quarantine_020",
        "020_non_grav_channel_quarantine__non_grav_channel_quarantine",
        "non_grav_channel_quarantine_020",
    )
]


@dataclass(frozen=True)
class ContractGate:
    gate_id: str
    requirement: str
    current_entry: str
    status: str
    next_obligation: str
    ready: int


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


def contract_gates():
    return [
        ContractGate(
            gate_id="channel_variable",
            requirement="state the apparatus-level channel variable",
            current_entry="boundary/material data B = (L, chi_m, boundary class, frequency window)",
            status="contracted",
            next_obligation="keep distinct from metric variable g_ab",
            ready=1,
        ),
        ContractGate(
            gate_id="coupling_schema",
            requirement="state the symbolic coupling schema",
            current_entry="Delta O_ch = eta_ch * chi_m / L^4 as a scaling placeholder",
            status="schema only",
            next_obligation="derive or justify the operator and coefficient eta_ch",
            ready=1,
        ),
        ContractGate(
            gate_id="operator_derivation",
            requirement="derive the channel operator before prediction",
            current_entry="not supplied",
            status="missing",
            next_obligation="casimir_ufft_operator_instantiation_required_021",
            ready=0,
        ),
        ContractGate(
            gate_id="metric_quarantine",
            requirement="show the channel does not modify the closed metric response",
            current_entry="epsilon_g = 0 unless rerouted through residual gates",
            status="contracted",
            next_obligation="do not count apparatus response as K_residual",
            ready=1,
        ),
        ContractGate(
            gate_id="source_ledger",
            requirement="separate apparatus/material exchange from T_ab insertion",
            current_entry="not supplied",
            status="missing",
            next_obligation="write source/exchange bookkeeping for any concrete apparatus claim",
            ready=0,
        ),
        ContractGate(
            gate_id="observable",
            requirement="state the observable",
            current_entry="differential response with L, material, boundary-class, or frequency dependence",
            status="contracted",
            next_obligation="turn target window into an experimental bound before prediction",
            ready=1,
        ),
        ContractGate(
            gate_id="falsifier",
            requirement="state what kills or reroutes the channel",
            current_entry="no material/boundary scaling, or only universal Yukawa-like scaling",
            status="contracted",
            next_obligation="bind to current bounds before quantitative use",
            ready=1,
        ),
    ]


def run_sympy_checks(gates):
    L, r, lambda_y, eta_ch, chi_m, alpha_y, epsilon_g = sp.symbols(
        "L r lambda_y eta_ch chi_m alpha_y epsilon_g", positive=True
    )

    channel_observable = eta_ch * chi_m / L**4
    yukawa_residual = alpha_y * sp.exp(-r / lambda_y) / r
    metric_leak = epsilon_g * channel_observable

    require_equal("channel has material dependence", sp.diff(channel_observable, chi_m), eta_ch / L**4)
    require_equal("Yukawa residual has no material dependence", sp.diff(yukawa_residual, chi_m), 0)
    require_equal("channel has boundary-scale dependence", sp.diff(channel_observable, L), -4 * eta_ch * chi_m / L**5)
    require_equal("metric quarantine sets leak to zero", metric_leak.subs(epsilon_g, 0), 0)
    require_true("channel observable depends on apparatus variables", channel_observable.has(L) and channel_observable.has(chi_m))
    require_true("Yukawa residual depends on separation variables", yukawa_residual.has(r) and yukawa_residual.has(lambda_y))

    readiness = sum(gate.ready for gate in gates)
    complete = int(readiness == len(gates))
    require_equal("Casimir/UFFT contract is not prediction-ready", complete, 0)

    return {
        "channel_observable": channel_observable,
        "yukawa_residual": yukawa_residual,
        "metric_leak": metric_leak,
        "d_channel_d_material": sp.diff(channel_observable, chi_m),
        "d_yukawa_d_material": sp.diff(yukawa_residual, chi_m),
        "readiness": readiness,
        "gate_count": len(gates),
    }


def markdown_gates(gates):
    return "\n".join(
        "| {gate_id} | {requirement} | {current_entry} | {status} | {next_obligation} | {ready} |".format(
            gate_id=gate.gate_id,
            requirement=gate.requirement,
            current_entry=gate.current_entry,
            status=gate.status,
            next_obligation=gate.next_obligation,
            ready=bool(gate.ready),
        )
        for gate in gates
    )


def write_report(gates, data):
    gates_md = markdown_gates(gates)
    md = f"""# VacuumForge Casimir/UFFT Channel Contract

## Purpose

This report writes the first concrete contract for a Casimir/UFFT-like
non-gravitational vacuum channel. It does not derive an effect.

This report depends on:

```text
non_grav_channel_quarantine_020
```

It satisfies:

```text
casimir_ufft_channel_contract_required_020
```

## Symbolic Distinction Check

Apparatus-channel placeholder:

```text
Delta O_ch = {sp.sstr(data["channel_observable"])}
d(Delta O_ch)/d chi_m = {sp.sstr(data["d_channel_d_material"])}
```

Gravitational-Yukawa residual placeholder:

```text
Delta Phi_Y = {sp.sstr(data["yukawa_residual"])}
d(Delta Phi_Y)/d chi_m = {sp.sstr(data["d_yukawa_d_material"])}
```

Metric leakage proxy:

```text
Delta_metric = {sp.sstr(data["metric_leak"])}
Delta_metric | epsilon_g = 0 -> 0
```

The distinction is only a contract-level quarantine check. Material/boundary
dependence is compatible with an apparatus channel, but it does not derive the
operator or coefficient.

## Contract Gates

| gate | requirement | current entry | status | next obligation | ready |
| --- | --- | --- | --- | --- | --- |
{gates_md}

Readiness:

```text
{data["readiness"]}/{data["gate_count"]} gates ready
```

## Current Conclusion

The Casimir/UFFT channel now has a contract shape and a symbolic quarantine
from a gravitational-Yukawa misroute. It is not prediction-ready because the
channel operator and source/exchange ledger are still missing.

## Classification

```text
result type: non-gravitational channel contract
scope: Casimir/UFFT-like boundary/material apparatus response
conclusion: contract drafted, no effect licensed
non-conclusion: no Casimir/UFFT operator, coefficient, or target window derived
```

The next technical target is:

```text
casimir_ufft_operator_instantiation_required_021
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, gates):
    marker_id = "casimir_ufft_channel_contract_021"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("non_grav_channel_quarantine_result")],
        output=sp.Symbol("casimir_ufft_channel_contract_result"),
        method="SymPy apparatus-channel versus Yukawa-dependence quarantine check",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Casimir/UFFT channel contract and operator-instantiation handoff",
    )

    for gate in gates:
        status = (
            GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
            if gate.ready
            else GovernanceStatus.UNRESOLVED_PROOF_OBLIGATION
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"casimir_ufft_gate_{gate.gate_id}_021",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{gate.gate_id}: {gate.status}",
                derivation_ids=[marker_id],
                obligation_ids=["casimir_ufft_operator_instantiation_required_021"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="casimir_ufft_channel_contract_required_020",
            script_id=SCRIPT_ID,
            title="Write the first concrete Casimir/UFFT channel contract",
            status=ObligationStatus.SATISFIED,
            required_by=["020_non_grav_channel_quarantine__non_grav_channel_quarantine"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by defining the channel variable, coupling schema, "
                "observable, falsifier, metric quarantine, and missing source "
                "and operator obligations."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="casimir_ufft_operator_instantiation_required_021",
            script_id=SCRIPT_ID,
            title="Instantiate or reject the Casimir/UFFT channel operator",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Derive, justify, or reject the apparatus channel operator and "
                "coefficient before any quantitative Casimir/UFFT prediction "
                "or bound is used."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 021: Casimir/UFFT Channel Contract")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    gates = contract_gates()
    data = run_sympy_checks(gates)

    out = ScriptOutput()
    for gate in gates:
        status = StatusMark.PASS if gate.ready else StatusMark.OBLIGATION
        with out.governance_assessments():
            out.line(gate.gate_id, status, gate.status)
    with out.unresolved_obligations():
        out.line(
            "Casimir/UFFT operator instantiation required",
            StatusMark.OBLIGATION,
            "derive or reject the channel operator and source/exchange ledger",
        )

    record_archive(ns, gates)
    ns.write_run_metadata()
    write_report(gates, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
