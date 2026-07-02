#!/usr/bin/env python3
"""
quadratic_selector_closure.py

Derivation 049: P10 supplies the quadratic selector -- the
metric-vs-Finsler audit closes.

The projection-origin probe's GR-branch capstone (34) recorded two
imported assumptions at the root of the metric branch:

    "exact quadratic response"  -- not derived from the vacuum functional
    "epsilon = 0"               -- Finsler/constitutive residuals removed
                                   by hand, not computed

The whole probe treated quadratic interval response as a GATE (tested,
not derived): if response is quadratic, polarization gives a metric; if
not, the structure is Finsler-class and must be routed explicitly. The
selector itself was never computed from the ontology.

Under adopted P10 both imports become theorems, because the axiom's
cells are FLAT:

  (1) a flat cell's interval response is exactly the quadratic form of
      its Gram matrix -- the parallelogram identity holds identically
      and the fundamental tensor is direction-independent;
  (2) the packing's state space is edge lengths ONLY, and for an
      n-simplex the edge count C(n+1, 2) equals exactly the dimension
      n(n+1)/2 of a symmetric quadratic form in a vertex frame: the
      ontology has precisely enough numbers to store a metric and NO
      ROOM to store Finsler data (a quartic response in 4D needs 35
      coefficients; the 4-simplex carries 10 edges);
  (3) the edge lengths reconstruct the full quadratic form uniquely
      (the Gram/law-of-cosines inversion, verified symbolically for a
      generic form), so the stored data IS metric data;
  (4) the probe's own Finsler witness (the quartic eps-deformation)
      fails the parallelogram gate with the recorded residual 12 eps
      and carries a direction-dependent fundamental tensor -- such a
      response is not expressible in the packing's state space at all.

Consequence: epsilon = 0 for interval response is not an assumption
under P10; it is the flatness clause. Finsler deviation is impossible
WITHIN a cell by (1) and unstorable BY the ontology by (2)+(3). The
only place direction dependence can live is at hinges -- and that is
curvature (the deficit), already the theory's subject, not a hidden
norm. The two capstone rows close against this derivation.

Scope fence: this closes the INTERVAL-RESPONSE selector (the
metric-vs-Finsler audit). The other capstone imports (matter action,
shared interval ownership, quantum structure, ...) are untouched and
remain on their own ledger.
"""

from itertools import combinations
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
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"

DEPENDENCIES = [
    ("bridge_dep_049", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
    ("adoption_dep_049", "044_p10_adoption__p10_adoption",
     "p10_adoption_record_044"),
]


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


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
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def generic_form(n: int, name: str = "G"):
    """Generic symmetric quadratic form (signature-agnostic symbols)."""
    entries = {}
    G = sp.zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            s = sp.Symbol(f"{name}_{i}{j}", real=True)
            G[i, j] = s
            G[j, i] = s
            entries[(i, j)] = s
    return G


def Q_of(G, v):
    return sp.expand((v.T * G * v)[0, 0])


def check_1_flat_cell_quadratic(failures):
    header("Check 1: a flat cell's response passes every metric gate IDENTICALLY (generic form, n = 4)")
    n = 4
    G = generic_form(n)
    u = sp.Matrix(sp.symbols(f"u0:{n}", real=True))
    v = sp.Matrix(sp.symbols(f"v0:{n}", real=True))

    # Parallelogram identity: Q(u+v) + Q(u-v) = 2Q(u) + 2Q(v), identically.
    resid = sp.expand(Q_of(G, u + v) + Q_of(G, u - v) - 2 * Q_of(G, u) - 2 * Q_of(G, v))
    require("parallelogram identity: Q(u+v) + Q(u-v) - 2Q(u) - 2Q(v) = 0 identically",
            resid == 0, failures)

    # Polarization recovers an exactly bilinear object.
    B = sp.expand(sp.Rational(1, 4) * (Q_of(G, u + v) - Q_of(G, u - v)))
    require("polarization: (1/4)[Q(u+v) - Q(u-v)] = u.G.v exactly (bilinear)",
            sp.expand(B - (u.T * G * v)[0, 0]) == 0, failures)

    # Fundamental tensor g_ij(v) = (1/2) d^2 Q / dv_i dv_j is v-INDEPENDENT.
    Qv = Q_of(G, v)
    fund = sp.Matrix(n, n, lambda i, j: sp.Rational(1, 2) * sp.diff(Qv, v[i], v[j]))
    require("fundamental tensor (1/2) Hess Q = G, direction-independent",
            sp.simplify(fund - G) == sp.zeros(n, n), failures)
    print("  Flat means quadratic: signature plays no role (generic symmetric G).")


def check_2_dof_count(failures):
    header("Check 2: the ontology's storage exactly matches a metric and cannot hold Finsler data")
    print("  edges of an n-simplex: C(n+1, 2); quadratic form: n(n+1)/2;")
    print("  quartic (Finsler-class) form: C(n+3, 4) independent coefficients")
    print()
    print("    n   edges   quadratic   quartic   verdict")
    ok_all = True
    for n in range(2, 6):
        edges = sp.binomial(n + 1, 2)
        quad = sp.Rational(n * (n + 1), 2)
        quart = sp.binomial(n + 3, 4)
        match = (edges == quad)
        deficit = quart - edges
        ok_all = ok_all and match and (deficit > 0)
        print(f"    {n}   {int(edges):5d}   {int(quad):9d}   {int(quart):7d}   "
              f"metric exact, Finsler deficit {int(deficit)}")
    require("edge count = quadratic-form dimension exactly, for every n (2..5)",
            ok_all, failures)
    require("4D case: 10 edges vs 35 quartic coefficients (deficit 25)",
            int(sp.binomial(5, 2)) == 10 and int(sp.binomial(7, 4)) == 35, failures)
    print()
    print("  The packing's state space (edge lengths only, P10) has EXACTLY the")
    print("  degrees of freedom of a quadratic form per cell -- and 25 fewer than")
    print("  the smallest Finsler deformation class in 4D. Finsler data is not")
    print("  suppressed by the ontology; it is UNSTORABLE.")


def check_3_gram_reconstruction(failures):
    header("Check 3: edge lengths reconstruct the full quadratic form uniquely (generic G, n = 4)")
    n = 4
    G = generic_form(n)
    # Simplex with vertex 0 at origin, edge vectors e_i = basis vectors of the frame.
    # Squared lengths: l_{0i}^2 = G_ii ; l_{ij}^2 = Q(e_i - e_j) = G_ii + G_jj - 2 G_ij.
    basis = [sp.Matrix([1 if k == i else 0 for k in range(n)]) for i in range(n)]
    l0 = {i: Q_of(G, basis[i]) for i in range(n)}
    lij = {(i, j): Q_of(G, basis[i] - basis[j]) for i, j in combinations(range(n), 2)}
    # Law-of-cosines inversion.
    G_rec = sp.zeros(n, n)
    for i in range(n):
        G_rec[i, i] = l0[i]
    for i, j in combinations(range(n), 2):
        G_rec[i, j] = sp.Rational(1, 2) * (l0[i] + l0[j] - lij[(i, j)])
        G_rec[j, i] = G_rec[i, j]
    require("law-of-cosines inversion: G reconstructed from edge data exactly",
            sp.expand(G_rec - G) == sp.zeros(n, n), failures)
    print("  The C(n+1,2) squared edge lengths of one cell ARE the metric, bijectively:")
    print("  P10's stored data is metric data -- nothing else is in the cell.")


def check_4_finsler_witness_excluded(failures):
    header("Check 4: the probe's Finsler witness fails the gates and cannot enter a cell")
    # The probe's recorded witness (12_quadratic_response_selector/11):
    # Q(v) = a v1^2 + c v2^2 + eps (v1^2 + v2^2)^2, residual 12 eps at u=v=(1,0).
    a, c, eps = sp.symbols("a c epsilon", real=True)
    v1, v2, u1, u2 = sp.symbols("v1 v2 u1 u2", real=True)

    def Qf(x, y):
        return a * x**2 + c * y**2 + eps * (x**2 + y**2) ** 2

    resid = sp.expand(Qf(u1 + v1, u2 + v2) + Qf(u1 - v1, u2 - v2)
                      - 2 * Qf(u1, u2) - 2 * Qf(v1, v2))
    resid_at = resid.subs({u1: 1, u2: 0, v1: 1, v2: 0})
    require("probe witness reproduced: parallelogram residual = 12 eps at u=v=(1,0)",
            sp.simplify(resid_at - 12 * eps) == 0, failures)

    # Direction-dependent fundamental tensor: g_11(v) differs between directions.
    Qv = Qf(v1, v2)
    g11 = sp.Rational(1, 2) * sp.diff(Qv, v1, v1)
    dir_diff = sp.simplify(g11.subs({v1: 1, v2: 0}) - g11.subs({v1: 0, v2: 1}))
    require("fundamental tensor is direction-dependent: g_11(e1) - g_11(e2) = 4 eps != 0",
            sp.simplify(dir_diff - 4 * eps) == 0, failures)

    print("  For eps != 0 the witness fails the parallelogram gate (residual 12 eps)")
    print("  and has no single Gram matrix (fundamental tensor varies with direction).")
    print("  By check 3 a cell's geometry is exhausted by its Gram matrix; by check 2")
    print("  the eps coefficient has no storage slot. The witness is not a small")
    print("  perturbation of a P10 cell -- it is outside the axiom's state space.")


def record(ns):
    ns.record_derivation(
        derivation_id="quadratic_selector_closure_049",
        inputs=[sp.Symbol("P10_flat_cells"), sp.Symbol("edge_length_state_space"),
                sp.Symbol("probe_parallelogram_gate")],
        output=sp.Symbol("quadratic_selector_derived_epsilon_finsler_unstorable"),
        method=(
            "generic-form symbolic verification: parallelogram/polarization/"
            "fundamental-tensor identities for arbitrary symmetric G (n = 4); "
            "degree-of-freedom count edges = dim(quadratic) exactly for all n, "
            "with strict quartic deficit; law-of-cosines inversion reconstructs "
            "G from edge data exactly; the probe's quartic Finsler witness "
            "reproduced (residual 12 eps) and shown unstorable"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="selector_closure_theorem",
        scope=(
            "closes the interval-response quadratic gate under P10 (the "
            "metric-vs-Finsler audit); other capstone imports untouched; "
            "hinge direction-dependence is curvature, not a norm, and is "
            "the theory's existing subject"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="quadratic_gate_import_closed_049",
        script_id=SCRIPT_ID,
        title="Capstone imports 'exact quadratic response' and 'epsilon = 0' DERIVED under P10",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["quadratic_selector_closure_049"],
        description=(
            "The projection-origin probe's two root imports of the metric "
            "branch (34_gr_branch_closure_capstone, imported-assumption table "
            "rows 1-2) are theorems of P10's flatness clause: flat cells are "
            "exactly quadratic (parallelogram/polarization/fundamental-tensor "
            "identities, generic form), and the packing's edge-length state "
            "space stores exactly a metric per cell (C(n+1,2) = n(n+1)/2) "
            "with no slot for Finsler coefficients (quartic deficit 25 in 4D). "
            "Finsler interval response is unstorable, not merely unlicensed."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="quadratic_selector_claim_049",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Under P10 the quadratic interval-response selector is DERIVED: "
            "piecewise flatness makes every cell's response exactly the "
            "quadratic form of its Gram matrix, the edge-length ontology "
            "stores exactly that Gram matrix and nothing else (bijectively, "
            "by the law-of-cosines inversion), and Finsler-class deviations "
            "are unstorable in the axiom's state space. The only direction "
            "dependence the packing can express lives at hinges as deficit "
            "-- i.e. curvature, the theory's subject. The metric-vs-Finsler "
            "audit is closed; epsilon_Finsler = 0 is a theorem, not an import."
        ),
        derivation_ids=["quadratic_selector_closure_049"],
        obligation_ids=["quadratic_gate_import_closed_049"],
    ))


def write_report() -> Path:
    repo_root = SCRIPT_PATH.parents[4]
    report_path = (repo_root / "theory_v3" / "development" / "vacuum_sector"
                   / "08_packing_microphysics"
                   / "quadratic_selector_closure_vacuumforge.md")
    report = """# The Quadratic Selector Closure (Metric vs Finsler) -- VacuumForge Record

## Status

```text
result type:   selector-closure theorem (2026-07-02, derivation 049)
conclusion:    under P10 the quadratic interval-response gate is DERIVED,
               not imported: flat cells are exactly quadratic, and the
               edge-length ontology has no storage for Finsler data.
               The metric-vs-Finsler audit is CLOSED.
closes:        the two root rows of the GR-branch capstone's imported-
               assumption table ("exact quadratic response", "epsilon = 0"
               for interval response) --
               development/projection_origin_probe/34_gr_branch_closure_capstone/
non-conclusion: the OTHER capstone imports (matter action, shared interval
               ownership, second-order locality, quantum structure, ...)
               are untouched and remain on their own ledger.
verification:  vacuum_forge/src/vacuum_sector/049_quadratic_selector_closure/
```

## The Question

The projection-origin probe established that IF interval response is
exactly quadratic, polarization produces a pseudo-Riemannian metric and
the GR branch follows; if not, the structure is Finsler-class and must
be routed as explicit extra structure (`K_strain = K_metric + eps
K_Finsler`). The probe built gates and witnesses -- notably the
parallelogram gate and the quartic obstruction witness with residual
`12 eps` -- but the selector itself was an import: nothing in the
pre-P10 ontology said WHY response is quadratic.

## The Theorem (four verified parts)

```text
1. FLAT IS QUADRATIC. For a generic symmetric form G (n = 4, any
   signature), the cell response Q(v) = v.G.v satisfies the
   parallelogram identity IDENTICALLY, polarization returns an exactly
   bilinear object, and the fundamental tensor (1/2)Hess(Q) = G is
   direction-independent. P10's flatness clause is the quadratic gate.

2. THE ONTOLOGY CANNOT STORE FINSLER DATA. Per n-cell the packing
   stores C(n+1,2) edge lengths; a quadratic form in a vertex frame
   has n(n+1)/2 = C(n+1,2) components -- EXACT match, every n. The
   smallest Finsler deformation class (quartic) needs C(n+3,4)
   coefficients: 35 in 4D against 10 edges. Deficit 25: Finsler
   structure is not suppressed, it is UNSTORABLE.

3. EDGE DATA IS METRIC DATA, BIJECTIVELY. The law-of-cosines
   inversion G_ij = (l_0i^2 + l_0j^2 - l_ij^2)/2 reconstructs the
   full generic form from the edge lengths exactly (verified
   symbolically). The stored numbers ARE the metric.

4. THE WITNESS IS OUTSIDE THE STATE SPACE. The probe's own quartic
   witness reproduces (parallelogram residual 12 eps at u=v=(1,0));
   its fundamental tensor is direction-dependent (g_11 differs by
   4 eps between axes), so it has no Gram matrix -- and by (2)+(3)
   no P10 cell can hold it, even perturbatively.
```

## Where Direction Dependence Actually Lives

The packing is not globally quadratic -- and that is the point. The
only place the axiom can express direction dependence is ACROSS cells,
at hinges, as deficit angle. Deficit is curvature: the very thing the
theory is about. What P10 forbids is direction dependence WITHIN the
interval response -- a hidden norm -- and it forbids it structurally.
The old routing rule ("nonquadratic response must be routed explicitly
as Finsler/medium/constitutive structure") is now a theorem of the
form: under P10 there is nothing to route; the epsilon branch of
`K_metric + eps K_Finsler` has an empty state space.

## Ledger

```text
derivation:  quadratic_selector_closure_049
satisfies:   quadratic_gate_import_closed_049 (capstone rows 1-2)
depends on:  regge_delaunay_bridge_039, p10_adoption_record_044
kill face:   any demonstration that the packing's effective long-
             wavelength interval response develops a direction-
             dependent norm (e.g. from anisotropic ground order)
             would reopen the audit -- flagged as the watch item:
             the ground state's isotropy is O-P10-2/O-P10-5 territory.
```
"""
    report_path.write_text(report)
    return report_path


def main() -> None:
    header("Derivation 049: Quadratic Selector Closure (Metric vs Finsler under P10)")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    check_1_flat_cell_quadratic(failures)
    check_2_dof_count(failures)
    check_3_gram_reconstruction(failures)
    check_4_finsler_witness_excluded(failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 049: FAILED")
    print("  The metric-vs-Finsler audit CLOSES under P10: flat cells are exactly")
    print("  quadratic, the edge-length ontology stores exactly a metric per cell,")
    print("  and Finsler-class response is unstorable. 'epsilon = 0' and 'exact")
    print("  quadratic response' convert from capstone imports to theorems.")
    print("  Watch item: ground-state isotropy (O-P10-2/O-P10-5) guards the")
    print("  long-wavelength face.")

    record(ns)
    report_path = write_report()
    print(f"[INFO] report written: {report_path}")
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
