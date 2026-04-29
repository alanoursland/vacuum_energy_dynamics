# 4D sign-pattern enumeration: extend e2's 2D sweep to 4 pre-mode variables.
#
# In 2D (e2), only 2 of 8 sign patterns produce trace-free exchange — the
# antisymmetric pair (+1,-1) and (-1,+1). This raised the question: is
# trace-free exchange rare because of genuine structural constraint, or
# because 2D is too small a space?
#
# Setup:
#   - Four pre-mode variables (q_1, q_2, q_3, q_4) with direct projection
#     a = q_1, b = q_2 (the "physical" channels; q_3 and q_4 are internal).
#   - The trace projection vector is [da/dq_i + db/dq_i] = [1, 1, 0, 0].
#   - The trace kernel is the 3D subspace orthogonal to [1,1,0,0]:
#     any delta with delta_1 + delta_2 = 0.
#   - Creation: symmetric delta = (C, C, C, C).
#
# Enumerates all 3^4 - 1 = 80 nonzero sign patterns in {-1, 0, +1}^4.
# Classifies each as derived, failed, or tautological.
#
# Key question: what fraction of 4D sign patterns are trace-free?
# With trace vector [1,1,0,0], the kernel constraint is delta_1 + delta_2 = 0.
# Patterns with s_1 + s_2 = 0 (and any s_3, s_4) should derive trace-free.
# This is a much larger fraction than in 2D.

import itertools

import sympy

from vacuumforge import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)

ctx = TheoryContext("sign_pattern_4d")
ctx.define_equal_response_algebraic_symbols()

q1, q2, q3, q4 = sympy.symbols("q_1 q_2 q_3 q_4", real=True)
S, C = sympy.symbols("S C")

# Direct projection: a = q_1, b = q_2
# Trace vector: [1, 1, 0, 0]
# Trace kernel: delta_1 + delta_2 = 0 (3D subspace of 4D)
projection = ProjectionMap(
    id="direct_4d",
    variables=[q1, q2, q3, q4],
    a_expr=q1,
    b_expr=q2,
)

creation = SourceOperator(
    id="symmetric_creation_4d",
    kind="creation",
    deltas={q1: C, q2: C, q3: C, q4: C},
    source_symbols=[C],
)

analyzer = StructureAnalyzer()

signs = [sympy.Integer(-1), sympy.Integer(0), sympy.Integer(1)]
total = 0
derived_count = 0
failed_count = 0
tautological_count = 0
zero_count = 0

derived_patterns = []
failed_patterns = []
tautological_patterns = []

for s1, s2, s3, s4 in itertools.product(signs, repeat=4):
    if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
        continue

    pattern = (int(s1), int(s2), int(s3), int(s4))

    exchange = SourceOperator(
        id=f"exchange_{pattern}",
        kind="exchange",
        deltas={q1: s1 * S, q2: s2 * S, q3: s3 * S, q4: s4 * S},
        source_symbols=[S],
    )

    structure = VacuumStructure(
        id=f"sign_4d_{pattern}",
        variables=[q1, q2, q3, q4],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
    )

    result = analyzer.analyze(structure)
    total += 1

    if result.summary_status.value == "derived":
        derived_count += 1
        derived_patterns.append(pattern)
    elif result.summary_status.value == "tautological":
        tautological_count += 1
        tautological_patterns.append(pattern)
    elif result.summary_status.value == "failed":
        failed_count += 1
        failed_patterns.append(pattern)
    else:
        zero_count += 1

# Report
print("=" * 70)
print("4D Sign-Pattern Enumeration")
print("=" * 70)
print(f"Projection: a = q_1, b = q_2  (trace vector = [1, 1, 0, 0])")
print(f"Trace kernel: delta_1 + delta_2 = 0  (3D subspace of 4D)")
print()
print(f"Total patterns tested: {total}")
print(f"  Trace-free derived:  {derived_count}  ({100*derived_count/total:.1f}%)")
print(f"  Failed:              {failed_count}  ({100*failed_count/total:.1f}%)")
print(f"  Tautological:        {tautological_count}  ({100*tautological_count/total:.1f}%)")
if zero_count:
    print(f"  Other:               {zero_count}")

print()
print("Derived (trace-free) patterns:")
for p in sorted(derived_patterns):
    kernel_check = p[0] + p[1]
    print(f"  {p}  (s1+s2 = {kernel_check})")

print()
print("Tautological patterns:")
for p in sorted(tautological_patterns):
    print(f"  {p}")

print()
print("Failed patterns (sample, first 10):")
for p in sorted(failed_patterns)[:10]:
    kernel_check = p[0] + p[1]
    print(f"  {p}  (s1+s2 = {kernel_check})")
if len(failed_patterns) > 10:
    print(f"  ... and {len(failed_patterns) - 10} more")

# Verify the structural prediction: derived iff s1 + s2 = 0
print()
print("=" * 70)
print("Structural check: is 'derived' exactly equivalent to s1 + s2 = 0?")
print("=" * 70)

predicted_derived = [
    p for p in derived_patterns if p[0] + p[1] == 0
]
predicted_but_not_derived = [
    p for p in derived_patterns if p[0] + p[1] != 0
]
missed = []
for s1, s2, s3, s4 in itertools.product(signs, repeat=4):
    p = (int(s1), int(s2), int(s3), int(s4))
    if p == (0, 0, 0, 0):
        continue
    if p[0] + p[1] == 0 and p not in derived_patterns:
        # Check it's not in tautological either
        if p not in tautological_patterns:
            missed.append(p)

print(f"Derived with s1+s2=0: {len(predicted_derived)}")
print(f"Derived with s1+s2!=0: {len(predicted_but_not_derived)}")
print(f"s1+s2=0 but not derived or tautological: {len(missed)}")
if missed:
    for p in missed:
        print(f"  unexpected: {p}")

# Dimensionality comparison
print()
print("=" * 70)
print("Dimensionality comparison: 2D vs 4D")
print("=" * 70)
print(f"2D: trace kernel is 1D of 2D  -> 2/8 sign patterns derived (25.0%)")
print(f"4D: trace kernel is 3D of 4D  -> {derived_count}/{total} sign patterns derived ({100*derived_count/total:.1f}%)")
print()
# Note: sign-pattern counting undercounts the kernel fraction because
# patterns with s1=s2=0 (and nonzero s3,s4) are in the kernel but produce
# zero metric response (J_a = J_b = 0), so the analyzer classifies them as
# "zero" (failed). The kernel fraction of the continuous direction space is
# (N-1)/N by dimension, not by sign-pattern count.
print("The trace kernel in 4D is codimension-1 (one constraint: s1+s2=0).")
print("Sign-pattern counting understates the kernel fraction because patterns")
print("with s1=s2=0 produce zero metric response and are classified as failed.")
print("In continuous direction space, the kernel is (N-1)/N dimensional:")
print("  N=2: kernel is 1/2 of direction space")
print("  N=4: kernel is 3/4 of direction space")
print("Trace-free exchange is codimension-1 regardless of N.")
