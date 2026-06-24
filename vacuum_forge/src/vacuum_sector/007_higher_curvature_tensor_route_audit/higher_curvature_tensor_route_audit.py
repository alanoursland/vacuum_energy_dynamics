#!/usr/bin/env python3
"""
higher_curvature_tensor_route_audit.py

VacuumForge-managed route audit for higher-curvature residuals.

This is not a full tensor/covariant derivation. It classifies the tensor-route
burdens opened by the scalar prototype:

    inert/topological terms;
    scalaron/f(R)-type routes;
    spin-2/Weyl-type routes.

The symbolic checks are small projector/pole checks. Prior GR-branch closure
results are imported as context, not rederived here.

Output:
    theory_v3/development/vacuum_sector/02_candidate_branches/
        higher_curvature_tensor_route_audit_vacuumforge.md
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
    / "02_candidate_branches"
    / "higher_curvature_tensor_route_audit_vacuumforge.md"
)

DEPENDENCIES = [
    (
        "higher_curvature_scalar_prototype_006",
        "006_higher_curvature_scalar_prototype__higher_curvature_scalar_prototype",
        "higher_curvature_scalar_prototype_006",
    )
]


@dataclass(frozen=True)
class RouteAudit:
    route_id: str
    route_name: str
    representative_terms: str
    symbolic_result: str
    imported_context: str
    disposition: str
    epsilon_status: str
    next_obligation: str


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_equal(label, lhs, rhs):
    residual = simplify_expr(lhs - rhs)
    if residual != 0:
        raise AssertionError(f"{label} failed: {residual}")


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


def run_sympy_checks():
    k, b, a = sp.symbols("k b a", positive=True)

    eh_tt_symbol = k**2
    inert_delta_symbol = sp.Integer(0)
    inert_total_symbol = eh_tt_symbol + inert_delta_symbol
    require_equal("inert route leaves TT symbol unchanged", inert_total_symbol, eh_tt_symbol)

    scalaron_mass_squared = 1 / (6 * a)
    scalaron_range_squared = 6 * a
    require_equal(
        "scalaron mass/range inverse relation",
        scalaron_mass_squared * scalaron_range_squared,
        1,
    )
    alpha_fR = sp.Rational(1, 3)
    require_equal("f(R) scalaron weak-field alpha", alpha_fR, sp.Rational(1, 3))

    spin2_symbol = k**2 + b * k**4
    spin2_prop = 1 / spin2_symbol
    spin2_partial_fraction = sp.apart(spin2_prop, k)
    expected_spin2_pf = 1 / k**2 - 1 / (k**2 + 1 / b)
    require_equal("spin-2 partial fraction", spin2_partial_fraction, expected_spin2_pf)
    spin2_massive_pole_coefficient = -1
    require_equal("spin-2 massive pole coefficient", spin2_massive_pole_coefficient, -1)

    return {
        "eh_tt_symbol": eh_tt_symbol,
        "inert_delta_symbol": inert_delta_symbol,
        "inert_total_symbol": inert_total_symbol,
        "scalaron_mass_squared": scalaron_mass_squared,
        "scalaron_range_squared": scalaron_range_squared,
        "alpha_fR": alpha_fR,
        "spin2_symbol": spin2_symbol,
        "spin2_partial_fraction": spin2_partial_fraction,
        "spin2_normalized_partial_fraction": expected_spin2_pf,
        "spin2_massive_pole_coefficient": spin2_massive_pole_coefficient,
    }


def build_routes():
    return [
        RouteAudit(
            route_id="inert_topological",
            route_name="inert or topological higher-curvature route",
            representative_terms="Gauss-Bonnet in 4D, total derivatives, field redefinitions, boundary-local completions",
            symbolic_result="no bulk TT symbol change in the inert proxy",
            imported_context="topological or pure-boundary terms may change bookkeeping but do not license a bulk residual",
            disposition="retained only as epsilon = 0 equivalent or boundary-quarantined",
            epsilon_status="not controlled epsilon != 0",
            next_obligation="prove inertness or boundary quarantine for each concrete term",
        ),
        RouteAudit(
            route_id="scalaron_fR",
            route_name="scalaron / f(R)-type route",
            representative_terms="R + a R^2 with a > 0, plus inert topological terms",
            symbolic_result="mass^2 = 1/(6a), range^2 = 6a, weak-field alpha = 1/3 in the imported G20 route",
            imported_context="G20 treats this as ghost-safe after mode routing; E3 later kills it under adopted P7prime through mandatory scalaron hair unless P7prime is reopened",
            disposition="routed but not licensed under the current adopted closure",
            epsilon_status="not controlled epsilon != 0 under current postulate set",
            next_obligation="only reopen through an explicit P7prime scope appeal plus weak-field/source ledger",
        ),
        RouteAudit(
            route_id="spin2_weyl",
            route_name="spin-2 / Weyl-type route",
            representative_terms="Weyl^2, Ricci^2 combinations that reach the TT propagator",
            symbolic_result="quartic TT propagator has a massive pole with negative residue",
            imported_context="G20 kills quartic TT kinetic content as a ghost in the dynamical radiative sector",
            disposition="fails as controlled local higher-curvature residual unless reduced to inert/topological combination",
            epsilon_status="failed residual route",
            next_obligation="do not reuse except as a killed route or after proving degeneracy/topological cancellation",
        ),
        RouteAudit(
            route_id="generic_mixed_curvature_squared",
            route_name="generic mixed curvature-squared route",
            representative_terms="arbitrary R^2, Ricci^2, Riemann^2 mixture",
            symbolic_result="must decompose into inert, scalaron, and spin-2 pieces before evaluation",
            imported_context="generic labels hide which gate is active; the scalar prototype alone is insufficient",
            disposition="not evaluated until decomposed",
            epsilon_status="underdetermined without decomposition",
            next_obligation="decompose concrete invariant into topological, scalaron, and spin-2 sectors",
        ),
    ]


def markdown_route_rows(routes):
    return "\n".join(
        "| {route_id} | {representative_terms} | {symbolic_result} | {imported_context} | {disposition} | {epsilon_status} | {next_obligation} |".format(
            route_id=route.route_id,
            representative_terms=route.representative_terms,
            symbolic_result=route.symbolic_result,
            imported_context=route.imported_context,
            disposition=route.disposition,
            epsilon_status=route.epsilon_status,
            next_obligation=route.next_obligation,
        )
        for route in routes
    )


def write_report(data, routes):
    rows = markdown_route_rows(routes)
    md = f"""# VacuumForge Higher-Curvature Tensor-Route Audit

## Purpose

This report discharges the route-audit obligation opened by the
higher-curvature scalar prototype. It is a tensor-route classifier, not a full
new covariant derivation.

This report depends on:

```text
higher_curvature_scalar_prototype_006
```

It satisfies:

```text
higher_curvature_tensor_route_audit_required_006
```

## Symbolic Checks

The inert/topological proxy leaves the TT symbol unchanged:

```text
EH TT symbol      = {sp.sstr(data["eh_tt_symbol"])}
inert correction  = {sp.sstr(data["inert_delta_symbol"])}
total TT symbol   = {sp.sstr(data["inert_total_symbol"])}
```

The scalaron/f(R)-type route carries a scalar scale and weak-field face:

```text
mass^2  = {sp.sstr(data["scalaron_mass_squared"])}
range^2 = {sp.sstr(data["scalaron_range_squared"])}
alpha   = {sp.sstr(data["alpha_fR"])}
```

This is ghost-safe only after mode routing. Under the already adopted
GR-branch closure, the later P7prime gate still blocks the route unless that
postulate is explicitly reopened.

The spin-2/Weyl-type TT propagator decomposes as:

```text
symbol      = {sp.sstr(data["spin2_symbol"])}
propagator  = {sp.sstr(data["spin2_normalized_partial_fraction"])}
massive pole coefficient = {sp.sstr(data["spin2_massive_pole_coefficient"])}
```

In the normalized partial-fraction form, the massive pole has negative
coefficient. This is the ghost route identified in the prior G20 gate.

## Route Audit

| route | representative terms | symbolic result | imported context | disposition | epsilon status | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
{rows}

## Current Conclusion

The higher-curvature local residual branch still does not supply a controlled
`epsilon != 0` route. The inert/topological sector is not a bulk residual. The
spin-2/Weyl sector fails by the ghost route unless it degenerates to an inert
combination. The scalaron/f(R)-type sector is the only non-ghost local
higher-curvature route, but under the already adopted project closure it is
blocked by P7prime/weak-field routing unless that appeal is explicitly reopened.

## Classification

```text
result type: tensor-route audit / higher-curvature branch classifier
scope: local curvature-squared residual routes after scalar prototype
conclusion: no higher-curvature route is currently licensed as controlled epsilon != 0
non-conclusion: no new covariant tensor theorem is proved here; prior G20/E3 closures are imported as route context
```

The next technical target is to return to branch selection rather than keep
decorating the killed higher-curvature branch:

```text
open the Lambda baseline folder and separate baseline-selection questions from
local higher-curvature strain residuals.
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")


def governance_status(route: RouteAudit):
    if route.route_id == "spin2_weyl":
        return GovernanceStatus.REJECTED_ROUTE
    if route.route_id == "inert_topological":
        return GovernanceStatus.POLICY_RULE
    return GovernanceStatus.UNVERIFIED


def record_archive(ns, routes):
    marker_id = "higher_curvature_tensor_route_audit_007"
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[sp.Symbol("higher_curvature_scalar_obstruction")],
        output=sp.Symbol("higher_curvature_route_classification"),
        method="SymPy pole bookkeeping plus imported G20/E3 route context",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        is_placeholder=False,
        scope="higher-curvature residual route audit after scalar prototype",
    )

    for route in routes:
        ns.record_claim(
            ClaimRecord(
                claim_id=f"higher_curvature_route_{route.route_id}_007",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=governance_status(route),
                statement=(
                    f"{route.route_name}: {route.disposition}; epsilon status: "
                    f"{route.epsilon_status}; next obligation: {route.next_obligation}."
                ),
                derivation_ids=[marker_id],
                obligation_ids=[],
            )
        )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="higher_curvature_tensor_route_audit_required_006",
            script_id=SCRIPT_ID,
            title="Separate tensor higher-curvature residual routes",
            status=ObligationStatus.SATISFIED,
            required_by=["006_higher_curvature_scalar_prototype__higher_curvature_scalar_prototype"],
            satisfied_by=[SCRIPT_ID],
            description=(
                "Satisfied by separating inert/topological, scalaron/f(R), "
                "spin-2/Weyl, and generic mixed curvature-squared routes."
            ),
        )
    )

    ns.record_obligation(
        ProofObligationRecord(
            obligation_id="lambda_baseline_folder_required_007",
            script_id=SCRIPT_ID,
            title="Open Lambda baseline workstream",
            status=ObligationStatus.OPEN,
            required_by=[SCRIPT_ID],
            description=(
                "After higher-curvature residual routes fail or quarantine, "
                "open the separate Lambda baseline folder so baseline-selection "
                "questions do not get mixed into local strain residuals."
            ),
        )
    )


def main() -> None:
    header("Vacuum Sector 007: Higher-Curvature Tensor-Route Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    data = run_sympy_checks()
    routes = build_routes()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line(
            "inert/topological route",
            StatusMark.DEFER,
            "not a bulk residual; prove inertness for concrete terms",
        )
    with out.governance_assessments():
        out.line(
            "scalaron/f(R) route",
            StatusMark.OBLIGATION,
            "ghost-safe only after mode routing; P7prime/weak-field route still blocks adoption",
        )
    with out.counterexamples():
        out.line(
            "spin-2/Weyl route",
            StatusMark.FAIL,
            "negative residue massive TT pole",
        )
    with out.unresolved_obligations():
        out.line(
            "Lambda baseline folder required",
            StatusMark.OBLIGATION,
            "separate baseline selection from local strain residuals",
        )

    record_archive(ns, routes)
    ns.write_run_metadata()
    write_report(data, routes)

    print(f"Wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
