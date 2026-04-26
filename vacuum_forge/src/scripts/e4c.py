# Leak detection verification in 4D: ensure the analyzer correctly
# distinguishes derived from tautological trace-free exchange in 3+1.
#
# The baseline (e1) showed that leak detection works in 2D:
#   - direct_mode_basis: flagged as TAUTOLOGICAL (leak)
#   - two_channel_exchange: correctly DERIVED (no leak)
#
# This script tests the same distinction in 4D, plus a subtle new case
# that only arises in higher dimensions: exchange that zeros out the
# trace-contributing variables while acting on non-contributing ones.
#
# Test cases:
#   1. Direct 4D mode basis (kappa, sigma, nu, mu) — should be TAUTOLOGICAL
#   2. Antisymmetric 4D exchange with direct projection — should be DERIVED
#   3. Subtle case: exchange zeroes q_1 and q_2 (trace contributors) but
#      acts on q_3 and q_4 (non-contributors) — should be FAILED as "zero"
#      because the operator produces NO metric response at all (J_a = J_b = 0).
#      This is correctly handled: an operator invisible to the metric is not
#      "trace-free exchange" — it's a null operator from the metric's perspective
#   4. Genuine 4D kernel direction — should be DERIVED

import sympy

from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)

analyzer = StructureAnalyzer()
S, C = sympy.symbols("S C")

# -----------------------------------------------------------------------
# Test 1: Direct 4D mode basis — should be TAUTOLOGICAL
# -----------------------------------------------------------------------
print("=" * 70)
print("Test 1: Direct 4D mode basis (tautological control)")
print("=" * 70)

kappa, sigma, nu, mu = sympy.symbols("kappa sigma nu mu", real=True)

# Projection: a = kappa + sigma, b = kappa - sigma
# (nu and mu don't affect a or b — they're internal DOF)
proj_mode = ProjectionMap(
    id="mode_basis_4d",
    variables=[kappa, sigma, nu, mu],
    a_expr=kappa + sigma,
    b_expr=kappa - sigma,
    description="a = kappa + sigma, b = kappa - sigma (nu, mu internal)",
)

# Exchange: delta kappa = 0 (bakes in trace-free), acts on sigma, nu, mu
exchange_mode = SourceOperator(
    id="mode_exchange_4d",
    kind="exchange",
    deltas={kappa: sympy.Integer(0), sigma: S, nu: S, mu: S},
    source_symbols=[S],
    description="Exchange in mode basis: delta kappa = 0, delta sigma = delta nu = delta mu = S",
)

creation_mode = SourceOperator(
    id="mode_creation_4d",
    kind="creation",
    deltas={kappa: C, sigma: sympy.Integer(0), nu: sympy.Integer(0), mu: sympy.Integer(0)},
    source_symbols=[C],
)

struct_1 = VacuumStructure(
    id="mode_basis_4d",
    variables=[kappa, sigma, nu, mu],
    projection=proj_mode,
    exchange_operators=[exchange_mode],
    creation_operators=[creation_mode],
    description="4D mode basis — tautological control",
)

result_1 = analyzer.analyze(struct_1)
print(f"Status: {result_1.summary_status.value}")
print(f"Trace-free exchange derived: {result_1.derived_trace_free_exchange}")
if result_1.leak_warnings:
    for w in result_1.leak_warnings:
        print(f"LEAK: {w}")
else:
    print("No leak warnings (UNEXPECTED — should detect leak)")
ex1 = result_1.exchange_results[0]
print(f"J_kappa = {ex1.J_kappa}")
print(f"Classification: {ex1.classification}")

# -----------------------------------------------------------------------
# Test 2: Genuine antisymmetric 4D exchange — should be DERIVED
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Test 2: Antisymmetric 4D exchange (should be DERIVED)")
print("=" * 70)

q1, q2, q3, q4 = sympy.symbols("q_1 q_2 q_3 q_4", real=True)

proj_direct = ProjectionMap(
    id="direct_4d",
    variables=[q1, q2, q3, q4],
    a_expr=q1,
    b_expr=q2,
)

# Exchange: delta q_1 = S, delta q_2 = -S, delta q_3 = S, delta q_4 = 0
# Trace check: s1 + s2 = 1 + (-1) = 0 => in kernel
exchange_genuine = SourceOperator(
    id="antisymmetric_4d",
    kind="exchange",
    deltas={q1: S, q2: -S, q3: S, q4: sympy.Integer(0)},
    source_symbols=[S],
    description="Antisymmetric exchange: s1+s2=0, with nonzero s3",
)

creation_4d = SourceOperator(
    id="symmetric_creation_4d",
    kind="creation",
    deltas={q1: C, q2: C, q3: C, q4: C},
    source_symbols=[C],
)

struct_2 = VacuumStructure(
    id="genuine_antisym_4d",
    variables=[q1, q2, q3, q4],
    projection=proj_direct,
    exchange_operators=[exchange_genuine],
    creation_operators=[creation_4d],
    description="Genuine antisymmetric 4D exchange — should derive trace-free",
)

result_2 = analyzer.analyze(struct_2)
print(f"Status: {result_2.summary_status.value}")
print(f"Trace-free exchange derived: {result_2.derived_trace_free_exchange}")
if result_2.leak_warnings:
    for w in result_2.leak_warnings:
        print(f"LEAK (UNEXPECTED): {w}")
else:
    print("No leak warnings (correct — trace-free is structurally derived)")
ex2 = result_2.exchange_results[0]
print(f"J_kappa = {ex2.J_kappa}")
print(f"J_sigma = {ex2.J_sigma}")

# -----------------------------------------------------------------------
# Test 3: Subtle leak — zeros trace contributors, acts on non-contributors
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Test 3: Subtle 4D leak (zeros trace vars, acts on non-trace vars)")
print("=" * 70)
print("Projection: a = q_1, b = q_2  (trace vector = [1, 1, 0, 0])")
print("Exchange: delta q_1 = 0, delta q_2 = 0, delta q_3 = S, delta q_4 = S")
print("This is trace-free because q_3 and q_4 don't contribute to a or b.")
print("The classifier should mark this as 'zero' (no metric response)")
print("and the status should be FAILED — a null operator is not meaningful")
print("trace-free exchange.")
print()

exchange_subtle = SourceOperator(
    id="subtle_leak_4d",
    kind="exchange",
    deltas={q1: sympy.Integer(0), q2: sympy.Integer(0), q3: S, q4: S},
    source_symbols=[S],
    description="Only acts on non-trace variables q_3, q_4",
)

struct_3 = VacuumStructure(
    id="subtle_leak_4d",
    variables=[q1, q2, q3, q4],
    projection=proj_direct,
    exchange_operators=[exchange_subtle],
    creation_operators=[creation_4d],
    description="Subtle leak: exchange avoids trace-contributing variables",
)

result_3 = analyzer.analyze(struct_3)
print(f"Status: {result_3.summary_status.value}")
print(f"Trace-free exchange derived: {result_3.derived_trace_free_exchange}")
if result_3.leak_warnings:
    for w in result_3.leak_warnings:
        print(f"LEAK: {w}")
else:
    print("No leak warnings (correct — classified as zero source, not as trace-free)")
ex3 = result_3.exchange_results[0]
print(f"J_kappa = {ex3.J_kappa}")
print(f"J_sigma = {ex3.J_sigma}")
print(f"Classification: {ex3.classification}")

# -----------------------------------------------------------------------
# Test 4: Physical 3+1 kernel direction — should be DERIVED
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Test 4: Physical 3+1 trace-kernel direction (should be DERIVED)")
print("=" * 70)

q_t, q_x, q_y, q_z = sympy.symbols("q_t q_x q_y q_z", real=True)

proj_31 = ProjectionMap(
    id="physical_31",
    variables=[q_t, q_x, q_y, q_z],
    a_expr=q_t,
    b_expr=(q_x + q_y + q_z) / 3,
    description="a = q_t, b = (q_x + q_y + q_z)/3",
)

# Exchange in the trace kernel: e_t + (e_x + e_y + e_z)/3 = 0
# Choose: e_t = -1, e_x = 1, e_y = 1, e_z = 1
# Check: -1 + (1+1+1)/3 = -1 + 1 = 0 ✓
exchange_31_kernel = SourceOperator(
    id="kernel_exchange_31",
    kind="exchange",
    deltas={q_t: -S, q_x: S, q_y: S, q_z: S},
    source_symbols=[S],
    description="In trace kernel: -1 + (1+1+1)/3 = 0",
)

creation_31 = SourceOperator(
    id="creation_31",
    kind="creation",
    deltas={q_t: C, q_x: C, q_y: C, q_z: C},
    source_symbols=[C],
)

struct_4 = VacuumStructure(
    id="physical_31_kernel",
    variables=[q_t, q_x, q_y, q_z],
    projection=proj_31,
    exchange_operators=[exchange_31_kernel],
    creation_operators=[creation_31],
    description="Physical 3+1 with exchange in the trace kernel",
)

result_4 = analyzer.analyze(struct_4)
print(f"Trace vector: {(proj_31.jacobian().row(0) + proj_31.jacobian().row(1)).tolist()}")
print(f"Status: {result_4.summary_status.value}")
print(f"Trace-free exchange derived: {result_4.derived_trace_free_exchange}")
if result_4.leak_warnings:
    for w in result_4.leak_warnings:
        print(f"LEAK (UNEXPECTED): {w}")
else:
    print("No leak warnings (correct)")
ex4 = result_4.exchange_results[0]
print(f"J_kappa = {ex4.J_kappa}")
print(f"J_sigma = {ex4.J_sigma}")
cr4 = result_4.creation_results[0]
print(f"Creation J_kappa = {cr4.J_kappa}  (should be nonzero)")

# -----------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Leak Detection Summary (4D)")
print("=" * 70)
print()
results = [
    ("Mode basis (tautological control)", result_1, "tautological"),
    ("Genuine antisymmetric", result_2, "derived"),
    ("Null operator (zero metric response)", result_3, "failed"),
    ("Physical 3+1 kernel", result_4, "derived"),
]

all_correct = True
for name, r, expected in results:
    actual = r.summary_status.value
    match = "OK" if actual == expected else "FAIL"
    if actual != expected:
        all_correct = False
    print(f"  [{match}] {name}: expected {expected}, got {actual}")

print()
if all_correct:
    print("All leak detection tests passed in 4D.")
else:
    print("SOME TESTS FAILED -- investigate leak detection for higher dimensions.")
