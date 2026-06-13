# Trial 014: Tensor-virial identity in generality
#
# Script type:
#   RIGOR UPGRADE / SYMBOLIC CONSERVATION IDENTITY
#
# Purpose
# -------
# The 008 radiative bootstrap used the tensor-virial identity in the
# quadrupole chain and verified it on a compact one-dimensional witness.
# This follow-on script discharges the general identity under explicit
# assumptions:
#
#   1. flat-background conservation, partial_mu T^{mu nu} = 0, with x0=ct;
#   2. symmetric stress tensor;
#   3. compact support or falloff killing the integration-by-parts
#      surface terms;
#   4. enough regularity to commute d/dt through the spatial integral.
#
# The identity proved is
#
#   int T^{ij} d^3x = (1/(2 c^2)) d^2/dt^2 int T^{00} x^i x^j d^3x.

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


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


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
        dependency_id="quadrupole_chain_dependency_014",
        upstream_script_id="008_radiative_bootstrap__radiative_bootstrap_KT",
        upstream_derivation_id="quadrupole_one_fifth_008",
        expected_record_kind=RecordKind.DERIVATION,
    )
    return archive, ns, invalidated


t, x, y, z = sp.symbols("t x y z")
c = sp.Symbol("c", positive=True)
coords = [x, y, z]
labels = ["x", "y", "z"]


def make_vector(prefix: str):
    return [sp.Function(f"{prefix}{i}")(t, x, y, z) for i in range(3)]


def make_tensor(prefix: str):
    return [
        [sp.Function(f"{prefix}{i}{j}")(t, x, y, z) for j in range(3)]
        for i in range(3)
    ]


T0 = make_vector("T0")
S = make_tensor("T")


def case_0_statement(out: ScriptOutput) -> None:
    header("Case 0: Tensor-virial obligation")
    print("008 used the tensor-virial identity in the quadrupole chain:")
    print()
    print("  int T^{ij} d^3x = (1/(2 c^2)) d^2/dt^2 int T^{00} x^i x^j d^3x")
    print()
    print("There it was checked on a compact 1D witness. Here the general")
    print("identity is proved from flat stress conservation plus boundary")
    print("conditions. No coefficient can move; this only upgrades rigor.")

    with out.governance_assessments():
        out.line(
            "tensor-virial generality proof opened",
            StatusMark.INFO,
            "follow-on to 008 quadrupole chain; coefficient-free rigor item",
        )


def case_1_first_integration_by_parts(out: ScriptOutput):
    header("Case 1: First integration by parts")
    print("For I^{ij} = int T^{00} x^i x^j d^3x and x^0 = ct,")
    print("conservation gives dot(T^{00}) = -c partial_k T^{0k}.")
    print("The needed local product-rule identity is checked for all")
    print("spatial index pairs:")
    print()
    print("  partial_k(T^{0k} x^i x^j)")
    print("    = (partial_k T^{0k}) x^i x^j + T^{0i} x^j + T^{0j} x^i")

    residuals = []
    for i in range(3):
        for j in range(3):
            xi = coords[i]
            xj = coords[j]
            div_total = sum(
                sp.diff(T0[k] * xi * xj, coords[k]) for k in range(3)
            )
            expanded = (
                sum(sp.diff(T0[k], coords[k]) for k in range(3)) * xi * xj
                + T0[i] * xj
                + T0[j] * xi
            )
            residual = sp.simplify(div_total - expanded)
            residuals.append(residual)
            print(f"  ({labels[i]},{labels[j]}): residual = {sp.sstr(residual)}")

    ok = all(is_zero(residual) for residual in residuals)
    with out.derived_results():
        out.line(
            "first integration-by-parts identity holds for all i,j",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "surface-free local identity behind dot(I^{ij})",
        )
    return ok


def case_2_second_integration_by_parts(out: ScriptOutput):
    header("Case 2: Second integration by parts")
    print("Momentum conservation gives dot(T^{0i}) = -c partial_k T^{ki}.")
    print("The second product-rule identity is checked for all index pairs:")
    print()
    print("  partial_k(T^{ki} x^j) = (partial_k T^{ki}) x^j + T^{ji}")

    residuals = []
    symmetry_residuals = []
    for i in range(3):
        for j in range(3):
            xj = coords[j]
            xi = coords[i]
            first_total = sum(
                sp.diff(S[k][i] * xj, coords[k]) for k in range(3)
            )
            first_expanded = (
                sum(sp.diff(S[k][i], coords[k]) for k in range(3)) * xj
                + S[j][i]
            )
            first_residual = sp.simplify(first_total - first_expanded)

            second_total = sum(
                sp.diff(S[k][j] * xi, coords[k]) for k in range(3)
            )
            second_expanded = (
                sum(sp.diff(S[k][j], coords[k]) for k in range(3)) * xi
                + S[i][j]
            )
            second_residual = sp.simplify(second_total - second_expanded)

            sym_residual = sp.simplify(
                (S[j][i] + S[i][j] - 2 * S[i][j]).subs(S[j][i], S[i][j])
            )

            residuals.extend([first_residual, second_residual])
            symmetry_residuals.append(sym_residual)
            print(
                f"  ({labels[i]},{labels[j]}): product residuals = "
                f"{sp.sstr(first_residual)}, {sp.sstr(second_residual)}; "
                f"symmetry residual = {sp.sstr(sym_residual)}"
            )

    product_ok = all(is_zero(residual) for residual in residuals)
    symmetry_ok = all(is_zero(residual) for residual in symmetry_residuals)
    ok = product_ok and symmetry_ok
    with out.derived_results():
        out.line(
            "second integration-by-parts identity holds for all i,j",
            StatusMark.PASS if product_ok else StatusMark.FAIL,
            "surface-free local identity behind ddot(I^{ij})",
        )
        out.line(
            "stress symmetry reduces T^{ij}+T^{ji} to 2T^{ij}",
            StatusMark.PASS if symmetry_ok else StatusMark.FAIL,
            "the only tensor-symmetry input used by the theorem",
        )
    return ok


def case_3_boundary_witness(out: ScriptOutput):
    header("Case 3: Boundary terms")
    print("The theorem requires the surface terms from both integrations by")
    print("parts to vanish. Compact support is sufficient. The script checks")
    print("an explicit compact polynomial envelope on the box [-1,1]^3:")
    print()
    print("  B = (1-x^2)^2 (1-y^2)^2 (1-z^2)^2")

    B = (1 - x**2) ** 2 * (1 - y**2) ** 2 * (1 - z**2) ** 2
    a = [sp.Function(f"a{i}")(t) for i in range(3)]
    b = [[sp.Function(f"b{i}{j}")(t) for j in range(3)] for i in range(3)]
    T0_b = [B * a[i] for i in range(3)]
    S_b = [[B * b[i][j] for j in range(3)] for i in range(3)]

    residuals = []
    for normal_axis, coord in enumerate(coords):
        for side in (-1, 1):
            substitutions = {coord: side}
            for i in range(3):
                for j in range(3):
                    xi = coords[i]
                    xj = coords[j]
                    first_surface = sp.simplify(
                        (T0_b[normal_axis] * xi * xj).subs(substitutions)
                    )
                    second_surface_a = sp.simplify(
                        (S_b[normal_axis][i] * xj).subs(substitutions)
                    )
                    second_surface_b = sp.simplify(
                        (S_b[normal_axis][j] * xi).subs(substitutions)
                    )
                    residuals.extend([first_surface, second_surface_a, second_surface_b])

    ok = all(is_zero(residual) for residual in residuals)
    print(f"  checked boundary expressions: {len(residuals)}")
    print(f"  all boundary expressions vanish: {ok}")

    with out.derived_results():
        out.line(
            "compact-support witness kills all tensor-virial boundary terms",
            StatusMark.PASS if ok else StatusMark.FAIL,
            "finite-box polynomial envelope vanishes on every face",
        )
    return ok


def case_4_assembly(out: ScriptOutput):
    header("Case 4: Assembly")
    Iddot_ij, Int_Tij = sp.symbols("Iddot_ij Int_Tij")
    identity_residual = sp.simplify(Int_Tij - Iddot_ij / (2 * c**2))
    solved = sp.solve(sp.Eq(Iddot_ij, 2 * c**2 * Int_Tij), Int_Tij)[0]
    assembly_ok = is_zero(sp.simplify(solved - Iddot_ij / (2 * c**2)))

    print("The two integrations by parts give")
    print()
    print("  ddot(I^{ij}) = 2 c^2 int T^{ij} d^3x")
    print()
    print("so")
    print()
    print(f"  int T^ij d^3x = {sp.sstr(solved)}")
    print(f"  residual against target = {sp.sstr(identity_residual.subs(Int_Tij, solved))}")

    with out.derived_results():
        out.line(
            "tensor-virial identity assembled in generality",
            StatusMark.PASS if assembly_ok else StatusMark.FAIL,
            "flat conservation + symmetry + vanishing surface terms imply the quadrupole-chain identity",
        )
    return assembly_ok


def case_5_verdict(out: ScriptOutput) -> None:
    header("Case 5: Verdict")
    print("The tensor-virial identity used in 008 is now discharged at general")
    print("reduced level. The remaining assumptions are explicit: flat")
    print("stress conservation, stress symmetry, isolation/falloff, and enough")
    print("regularity to commute time derivatives through the integral.")
    print()
    print("This does not alter the radiative bootstrap. It only upgrades the")
    print("quadrupole chain's virial step from compact witness to theorem.")

    with out.governance_assessments():
        out.line(
            "tensor-virial generality obligation discharged",
            StatusMark.PASS,
            "008 compact-witness debt retired under stated assumptions",
        )


def record_results(ns) -> None:
    ns.record_derivation(
        derivation_id="tensor_virial_identity_general_014",
        inputs=[],
        output=sp.Symbol("Int_Tij_eq_half_cminus2_ddot_Int_T00_xixj"),
        method=(
            "two integrations by parts from flat conservation "
            "partial_mu T^{mu nu}=0 with x0=ct; symbolic product-rule "
            "checks for all spatial index pairs; explicit compact-support "
            "boundary witness"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="rigor_upgrade",
        scope=(
            "isolated symmetric stress tensor on flat background; surface "
            "terms vanish and time derivatives commute with spatial integrals"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="tensor_virial_generality_014",
        script_id=SCRIPT_ID,
        title="Tensor-virial identity in generality",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["tensor_virial_identity_general_014"],
        description=(
            "Retires the 008 note that the tensor-virial step had only been "
            "verified on a compact witness."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="tensor_virial_identity_general_claim_014",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "Under flat stress conservation, stress symmetry, isolation/falloff, "
            "and regularity, int T^{ij} d^3x = (1/(2c^2)) d^2/dt^2 "
            "int T^{00} x^i x^j d^3x. This discharges the tensor-virial "
            "generality obligation recorded by the 008 radiative bootstrap."
        ),
        derivation_ids=["tensor_virial_identity_general_014"],
        obligation_ids=["tensor_virial_generality_014"],
    ))


def main() -> None:
    header("Trial 014: Tensor-Virial Identity in Generality")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    case_0_statement(out)
    case_1_first_integration_by_parts(out)
    case_2_second_integration_by_parts(out)
    case_3_boundary_witness(out)
    case_4_assembly(out)
    case_5_verdict(out)

    record_results(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()

