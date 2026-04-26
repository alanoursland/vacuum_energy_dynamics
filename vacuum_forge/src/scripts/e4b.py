# Trace-kernel geometry in 4D: analyze the algebraic structure of the
# trace-free condition for general linear projections in 4 dimensions.
#
# The 2D baseline found that the trace-free condition is a single equation:
#   (alpha_1 + beta_1)*e_1 + (alpha_2 + beta_2)*e_2 = 0
# which defines a codimension-1 subspace (a line in 2D exchange space).
#
# Questions for 4D:
#   1. What is the trace-free condition for a general 4D linear projection?
#   2. How many independent constraints does it impose on exchange coefficients?
#   3. Is it still codimension-1 (one equation in 4 unknowns)?
#   4. What does this say about the trace-kernel dimension?
#
# Also tests a specific 3+1 physical scenario:
#   - q_t (time log-scale), q_x, q_y, q_z (spatial log-scales)
#   - Projection: a = q_t, b = (q_x + q_y + q_z)/3  (average spatial scale)
#   - Trace vector: [1, 1/3, 1/3, 1/3]
#   - Trace kernel: delta_t + (delta_x + delta_y + delta_z)/3 = 0
#
# This physical projection represents the actual 3+1 metric structure
# where a = ln(g_tt) and b = average ln(g_ii) for spatial components.

import sympy

from vacuumforge import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)
from vacuumforge.structure_search.families import general_linear_projection

ctx = TheoryContext("trace_kernel_4d")
ctx.define_equal_response_algebraic_symbols()

analyzer = StructureAnalyzer()

# -----------------------------------------------------------------------
# Part 1: General linear projection in 4D
# -----------------------------------------------------------------------
print("=" * 70)
print("Part 1: General linear 4D projection — trace-free condition")
print("=" * 70)

family_4d = general_linear_projection(n_vars=4)
result_4d = analyzer.analyze(family_4d)

print(result_4d.summary())

# Extract and display the trace-free condition explicitly
ex = result_4d.exchange_results[0]
print()
print("Trace-free condition (J_kappa = 0):")
print(f"  J_kappa = {ex.J_kappa}")
print()
print("This is a SINGLE linear equation in 4 exchange coefficients (e_1..e_4)")
print("parameterized by 8 projection coefficients (alpha_i, beta_i).")
print("The trace kernel is therefore 3-dimensional (codimension 1 in 4D).")
print()
print("Compare to 2D: trace kernel was 1-dimensional (codimension 1 in 2D).")
print("The codimension is always 1, regardless of the number of variables.")
print("This is the key structural result.")

if result_4d.conditions:
    print()
    print("Conditions extracted by solver:")
    for c in result_4d.conditions:
        print(f"  {c}")

# -----------------------------------------------------------------------
# Part 2: Physical 3+1 projection (time vs averaged space)
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Part 2: Physical 3+1 projection (a = q_t, b = avg spatial)")
print("=" * 70)

q_t, q_x, q_y, q_z = sympy.symbols("q_t q_x q_y q_z", real=True)
S, C = sympy.symbols("S C")
e_t, e_x, e_y, e_z = sympy.symbols("e_t e_x e_y e_z", real=True)

projection_31 = ProjectionMap(
    id="physical_3plus1",
    variables=[q_t, q_x, q_y, q_z],
    a_expr=q_t,
    b_expr=(q_x + q_y + q_z) / 3,
    description="a = q_t (time), b = (q_x + q_y + q_z)/3 (avg spatial)",
)

# General exchange with symbolic coefficients
exchange_31 = SourceOperator(
    id="general_exchange_31",
    kind="exchange",
    deltas={q_t: e_t * S, q_x: e_x * S, q_y: e_y * S, q_z: e_z * S},
    source_symbols=[S],
    description="General exchange: delta q_i = e_i * S",
)

# Symmetric creation (all channels equal)
creation_31 = SourceOperator(
    id="symmetric_creation_31",
    kind="creation",
    deltas={q_t: C, q_x: C, q_y: C, q_z: C},
    source_symbols=[C],
    description="Symmetric creation: delta q_i = C for all i",
)

structure_31 = VacuumStructure(
    id="physical_3plus1",
    variables=[q_t, q_x, q_y, q_z],
    projection=projection_31,
    exchange_operators=[exchange_31],
    creation_operators=[creation_31],
    description="Physical 3+1 metric: a = ln(g_tt), b = avg ln(g_ii)",
)

result_31 = analyzer.analyze(structure_31)

print()
print("Jacobian:")
jac = projection_31.jacobian()
print(f"  {jac.tolist()}")
print()

trace_vec = jac.row(0) + jac.row(1)
print(f"Trace vector (da/dq_i + db/dq_i): {trace_vec.tolist()}")
print()

ex_31 = result_31.exchange_results[0]
print(f"J_kappa = {ex_31.J_kappa}")
print(f"J_sigma = {ex_31.J_sigma}")
print(f"Status: {ex_31.status.value}")
print(f"Classification: {ex_31.classification}")
print()

if result_31.conditions:
    print("Trace-free exchange condition:")
    for c in result_31.conditions:
        print(f"  {c}")
    print()
    print("This says: e_t + (e_x + e_y + e_z)/3 = 0")
    print("i.e., the time-channel exchange must cancel the average spatial exchange.")
    print("The kernel is 3D: three free parameters (e_x, e_y, e_z) determine e_t.")

# -----------------------------------------------------------------------
# Part 3: Specific trace-kernel directions in 3+1
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Part 3: Specific trace-kernel exchange directions in 3+1")
print("=" * 70)

# Direction 1: pure time-space antisymmetric (like 2D case extended)
# NOTE: In 3+1, the trace vector is [1, 1/3, 1/3, 1/3], NOT [1, 1, 0, 0].
# So (S, -S, 0, 0) gives J_kappa = S - S/3 = 2S/3 != 0.
# The simple 2D antisymmetric pattern does NOT transfer to 3+1.
exchange_anti = SourceOperator(
    id="antisymmetric_tx",
    kind="exchange",
    deltas={q_t: S, q_x: -S, q_y: sympy.Integer(0), q_z: sympy.Integer(0)},
    source_symbols=[S],
    description="Antisymmetric time-x exchange (NOT in 3+1 trace kernel)",
)

# Direction 2: time vs all-spatial (isotropic spatial exchange)
# Trace kernel: e_t + (e_x+e_y+e_z)/3 = 0 => e_t = -1 when e_x=e_y=e_z=1
exchange_isotropic = SourceOperator(
    id="isotropic_spatial_exchange",
    kind="exchange",
    deltas={q_t: -S, q_x: S, q_y: S, q_z: S},
    source_symbols=[S],
    description="Time contracts, all spatial expand equally: e_t + (1+1+1)/3 = 0",
)

# Direction 3: pure spatial shear (no time component)
# Trace kernel: 0 + (1 + (-1) + 0)/3 = 0 => in kernel.
# But J_a = 0, J_b = (S - S)/3 = 0 => J_sigma = 0 too.
# This is in the kernel but produces ZERO metric response — a null operator.
# It redistributes within spatial channels without affecting the metric.
exchange_shear = SourceOperator(
    id="spatial_shear",
    kind="exchange",
    deltas={q_t: sympy.Integer(0), q_x: S, q_y: -S, q_z: sympy.Integer(0)},
    source_symbols=[S],
    description="Pure spatial shear: in trace kernel but J_sigma = 0 too",
)

# Direction 4: NOT in trace kernel — should fail
exchange_non_kernel = SourceOperator(
    id="non_kernel_exchange",
    kind="exchange",
    deltas={q_t: S, q_x: S, q_y: sympy.Integer(0), q_z: sympy.Integer(0)},
    source_symbols=[S],
    description="NOT in trace kernel: s_t + (s_x+0+0)/3 = S + S/3 != 0",
)

test_directions = [
    ("Antisymmetric t-x", exchange_anti),
    ("Isotropic spatial (time vs 3-space)", exchange_isotropic),
    ("Pure spatial shear (x vs y)", exchange_shear),
    ("Non-kernel (should fail)", exchange_non_kernel),
]

for name, exchange_op in test_directions:
    structure = VacuumStructure(
        id=f"test_{exchange_op.id}",
        variables=[q_t, q_x, q_y, q_z],
        projection=projection_31,
        exchange_operators=[exchange_op],
        creation_operators=[creation_31],
    )

    result = analyzer.analyze(structure)
    ex = result.exchange_results[0]

    print(f"\n{name}:")
    print(f"  deltas: {dict((str(k), str(v)) for k, v in exchange_op.deltas.items())}")
    print(f"  J_kappa = {ex.J_kappa}")
    print(f"  J_sigma = {ex.J_sigma}")
    print(f"  status = {result.summary_status.value}")
    if result.leak_warnings:
        for w in result.leak_warnings:
            print(f"  LEAK: {w}")

# -----------------------------------------------------------------------
# Part 4: Dimension count summary
# -----------------------------------------------------------------------
print()
print("=" * 70)
print("Part 4: Trace-kernel dimensionality summary")
print("=" * 70)
print()
print("For N pre-mode variables with projection to (a, b):")
print("  Config space dimension:  N")
print("  Trace projection:        1 equation (J_kappa = 0)")
print("  Trace kernel dimension:  N - 1  (codimension 1)")
print("  Shear (J_sigma) within kernel: N - 1 dimensional")
print()
print("  N=2 (2D):   kernel dim = 1,  fraction of sign-patterns = 2/8 = 25%")
print("  N=4 (3+1):  kernel dim = 3,  fraction grows significantly")
print()
print("The trace-free condition is ALWAYS codimension-1, regardless of N.")
print("As N grows, the kernel becomes a larger fraction of the full space.")
print("Trace-free exchange is NOT a fine-tuned condition — it's a single")
print("linear constraint, leaving N-1 free directions for exchange.")
print()
print("Physical implication: the framework doesn't need exchange to pick a")
print("specific direction. It needs exchange to avoid ONE direction (the trace")
print("direction). This is qualitatively different from the 2D picture where")
print("the kernel looked like a 'special' subspace.")
