#!/usr/bin/env python3
"""
non_grav_channel_quarantine.py

VacuumForge-managed quarantine ledger for non-gravitational vacuum channels.

This is not a derivation of a Casimir/UFFT or preferred-frame signal. It checks
whether a proposed channel has the minimum bookkeeping needed to remain outside
the closed metric-response sector.

Output:
    theory_v3/development/vacuum_sector/06_non_gravitational_channels/
        non_grav_channel_quarantine_vacuumforge.md
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
    / "non_grav_channel_quarantine_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "dark_excess_abundance_production_probe_019",
        "019_dark_excess_abundance_production__dark_excess_abundance_production",
        "dark_excess_abundance_production_probe_019",
    )
]


@dataclass(frozen=True)
class ChannelRow:
    row_id: str
    channel: str
    coupling_object: str
    metric_quarantine: str
    source_ledger: str
    observable: str
    falsifier: str
    disposition: str
    next_obligation: str
    channel_variable: int
    coupling_ready: int
    metric_quarantine_ready: int
    source_ledger_ready: int
    observable_ready: int
    falsifier_ready: int
    rejected: int = 0


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


def channel_rows():
    return [
        ChannelRow(
            row_id="casimir_ufft_channel",
            channel="boundary/material vacuum channel such as Casimir or UFFT",
            coupling_object="not yet written; must be a channel operator, not a metric residual",
            metric_quarantine="closed metric response unchanged unless a residual gate is explicitly reopened",
            source_ledger="not yet supplied; cannot be inserted into T_ab without bookkeeping",
            observable="geometry/material/frequency dependence in a nongravitational apparatus channel",
            falsifier="null target-window dependence or scaling incompatible with the channel operator",
            disposition="quarantined candidate only",
            next_obligation="write casimir_ufft_channel_contract",
            channel_variable=1,
            coupling_ready=0,
            metric_quarantine_ready=1,
            source_ledger_ready=0,
            observable_ready=1,
            falsifier_ready=1,
        ),
        ChannelRow(
            row_id="substance_frame_channel",
            channel="preferred-substance-frame observable channel",
            coupling_object="not yet written; must state the frame-sensitive operator",
            metric_quarantine="frame velocity cannot modify the closed metric sector by assumption",
            source_ledger="not yet supplied; matter-calibration effects need their own ledger",
            observable="anisotropy, calibration drift, or Lorentz/preferred-frame target window",
            falsifier="existing or proposed null bounds on preferred-frame/calibration response",
            disposition="quarantined candidate only",
            next_obligation="write substance_frame_coupling_contract",
            channel_variable=1,
            coupling_ready=0,
            metric_quarantine_ready=1,
            source_ledger_ready=0,
            observable_ready=1,
            falsifier_ready=1,
        ),
        ChannelRow(
            row_id="material_boundary_channel",
            channel="material or boundary vacuum-response channel",
            coupling_object="not yet written; needs boundary/material state variables",
            metric_quarantine="boundary response is not a universal gravitational potential",
            source_ledger="not yet supplied; material energy exchange must be separated",
            observable="material, geometry, or boundary-condition dependence",
            falsifier="loss of material/boundary dependence after controls",
            disposition="quarantined candidate only",
            next_obligation="route through a concrete channel contract before use",
            channel_variable=1,
            coupling_ready=0,
            metric_quarantine_ready=1,
            source_ledger_ready=0,
            observable_ready=1,
            falsifier_ready=1,
        ),
        ChannelRow(
            row_id="gravitational_yukawa_misroute",
            channel="reinterpret channel effect as local gravitational Yukawa residual",
            coupling_object="metric residual coefficient without residual gates",
            metric_quarantine="fails: changes closed metric response",
            source_ledger="fails: bypasses epsilon residual ledger",
            observable="short-range force fit",
            falsifier="already belongs in gravitational residual tests, not this folder",
            disposition="rejected as wrong ledger",
            next_obligation="route through residual gates before any gravitational use",
            channel_variable=0,
            coupling_ready=0,
            metric_quarantine_ready=0,
            source_ledger_ready=0,
            observable_ready=1,
            falsifier_ready=1,
            rejected=1,
        ),
        ChannelRow(
            row_id="stress_tensor_insertion_misroute",
            channel="insert channel energy into T_ab as unexplained source",
            coupling_object="source term without production, exchange, or conservation route",
            metric_quarantine="fails: becomes gravitational source bookkeeping",
            source_ledger="fails: double-counting risk is unresolved",
            observable="whatever source fit is desired",
            falsifier="not operational until the source ledger is stated",
            disposition="rejected as unbooked source insertion",
            next_obligation="return to source ledger before any metric coupling",
            channel_variable=0,
            coupling_ready=0,
            metric_quarantine_ready=0,
            source_ledger_ready=0,
            observable_ready=0,
            falsifier_ready=0,
            rejected=1,
        ),
    ]


def run_sympy_checks(rows):
    eps_g, delta_o, c_channel = sp.symbols("epsilon_g delta_O c_channel")
    metric_leak = eps_g * c_channel
    nongrav_observable = delta_o * c_channel

    require_equal("metric quarantine requires zero metric leak", metric_leak.subs(eps_g, 0), 0)
    require_true("observable may depend on channel coupling", nongrav_observable.has(c_channel))
    require_true("observable can remain nonzero when metric leak is zero", nongrav_observable.subs(eps_g, 0) == nongrav_observable)

    readiness = []
    for row in rows:
        gate_sum = (
            row.channel_variable
            + row.coupling_ready
            + row.metric_quarantine_ready
            + row.source_ledger_ready
            + row.observable_ready
            + row.falsifier_ready
        )
        complete = int(gate_sum == 6 and not row.rejected)
        readiness.append((row.row_id, gate_sum, complete))

    require_equal("no complete non-grav channel is live", sum(item[2] for item in readiness), 0)
    require_true("at least one candidate row is carried forward", any(row.rejected == 0 for row in rows))
    require_true("at least one misroute is explicitly rejected", any(row.rejected == 1 for row in rows))

    return {
        "metric_leak": metric_leak,
        "nongrav_observable": nongrav_observable,
        "readiness": readiness,
    }


def markdown_rows(rows):
    return "\n".join(
        (
            "| {row_id} | {channel} | {coupling_object} | {metric_quarantine} | "
            "{source_ledger} | {observable} | {falsifier} | {disposition} | {next_obligation} |"
        ).format(
            row_id=row.row_id,
            channel=row.channel,
            coupling_object=row.coupling_object,
            metric_quarantine=row.metric_quarantine,
            source_ledger=row.source_ledger,
            observable=row.observable,
            falsifier=row.falsifier,
            disposition=row.disposition,
            next_obligation=row.next_obligation,
        )
        for row in rows
    )


def readiness_rows(readiness):
    return "\n".join(
        f"| {row_id} | {gate_sum}/6 | {bool(complete)} |"
        for row_id, gate_sum, complete in readiness
    )


def write_report(rows, data):
    rows_md = markdown_rows(rows)
    readiness_md = readiness_rows(data["readiness"])
    md = f"""# VacuumForge Non-Gravitational Channel Quarantine

## Purpose

This report opens the non-gravitational vacuum-channel workstream. It does not
derive a Casimir/UFFT signal, preferred-frame coupling, or material-boundary
effect.

This report depends on:

```text
dark_excess_abundance_production_probe_019
```

It satisfies:

```text
non_grav_channel_quarantine_required_019
```

## Symbolic Checks

Metric leakage proxy:

```text
Delta_metric = {sp.sstr(data["metric_leak"])}
Delta_metric | epsilon_g = 0 -> 0
```

Non-gravitational observable proxy:

```text
Delta_observable = {sp.sstr(data["nongrav_observable"])}
```

The check is intentionally narrow: a non-gravitational channel may carry an
observable coupling only if its metric-leak coefficient is quarantined at zero
or routed through the residual-gate ledger.

## Channel Quarantine Ledger

| row | channel | coupling object | metric quarantine | source ledger | observable | falsifier | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{rows_md}

## Readiness Check

| row | minimum gates ready | live channel |
| --- | ---: | --- |
{readiness_md}

## Current Conclusion

No non-gravitational vacuum channel is live yet. Casimir/UFFT,
substance-frame, and material-boundary routes are carried forward only as
quarantined candidates. They need a channel variable, coupling object, source
ledger, observable, falsifier, and explicit metric quarantine before they can
be used.

Direct gravitational-Yukawa reinterpretation and unbooked stress-tensor
insertion are rejected as wrong-ledger moves.

## Classification

```text
result type: non-gravitational channel quarantine ledger
scope: vacuum channels outside the closed metric response
conclusion: no non-grav channel is live until its coupling and falsifier are written
non-conclusion: no Casimir/UFFT or preferred-frame mechanism has been killed
```

The next technical target is:

```text
casimir_ufft_channel_contract_required_020
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def record_archive(ns, rows):
    marker_id = "non_grav_channel_quarantine_020"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("dark_excess_abundance_production_result")],
        output=sp.Symbol("non_grav_channel_quarantine_result"),
        method="SymPy metric-leak quarantine proxy plus channel readiness ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="Non-gravitational vacuum channel quarantine and misroute rejection",
    )

    for row in rows:
        status = (
            GovernanceStatus.REJECTED_ROUTE
            if row.rejected
            else GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        )
        ns.record_claim(
            ClaimRecord(
                claim_id=f"non_grav_channel_row_{row.row_id}_020",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=status,
                statement=f"{row.row_id}: {row.disposition}",
                derivation_ids=[marker_id],
                obligation_ids=["casimir_ufft_channel_contract_required_020"],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="non_grav_channel_quarantine_required_019",
            script_id=SCRIPT_ID,
            title="Open non-gravitational vacuum channel quarantine",
            status=ObligationStatus.SATISFIED,
            required_by=["019_dark_excess_abundance_production__dark_excess_abundance_production"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating quarantined non-gravitational channel "
                "candidates from wrong-ledger gravitational residual and "
                "stress-tensor insertion routes."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="casimir_ufft_channel_contract_required_020",
            script_id=SCRIPT_ID,
            title="Write the first concrete Casimir/UFFT channel contract",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "Define the Casimir/UFFT observable, channel coupling object, "
                "metric quarantine, source ledger, falsifier, and failure route "
                "before treating it as a vacuum-sector signal."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 020: Non-Gravitational Channel Quarantine")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    rows = channel_rows()
    data = run_sympy_checks(rows)

    out = ScriptOutput()
    for row in rows:
        status = StatusMark.FAIL if row.rejected else StatusMark.DEFER
        with out.governance_assessments():
            out.line(row.row_id, status, row.disposition)
    with out.unresolved_obligations():
        out.line(
            "Casimir/UFFT channel contract required",
            StatusMark.OBLIGATION,
            "write concrete coupling, observable, falsifier, and quarantine contract",
        )

    record_archive(ns, rows)
    ns.write_run_metadata()
    write_report(rows, data)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
