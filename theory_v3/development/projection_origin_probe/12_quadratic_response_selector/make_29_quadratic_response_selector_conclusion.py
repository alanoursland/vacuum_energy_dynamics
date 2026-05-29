#!/usr/bin/env python3
"""
Final conclusion for quadratic response selector.

Output:
    29_quadratic_response_selector_conclusion.md
"""
from pathlib import Path

required = [
    '5_quadratic_gate_initial_status.md',
    '10_hessian_approximation_status.md',
    '15_nonquadratic_branch_status.md',
    '20_calibration_coherence_status.md',
    '24_projection_ladder_dependency_status.md',
    '25_downstream_gr_gate_dependency.md',
    '27_quadratic_response_dependency_table.md',
    '28_hidden_quadratic_assumption_witness.md',
]
missing = [name for name in required if not Path(__file__).with_name(name).exists()]
if missing:
    raise AssertionError(f'missing prerequisite reports: {missing}')

md = """# Quadratic Response Selector 29: Conclusion

## Result

This folder isolates the central metric-origin gate:

```text
exact parallelogram/quadratic response
  <-> polarization reconstructs a symmetric bilinear metric-like form.
```

The algebraic result is strong:

```text
quadratic Q -> bilinear metric branch;
nonquadratic Q -> parallelogram failure / polarization contamination /
                  scale or direction dependent calibration.
```

## What Is Proved

This folder proves:

```text
1. exact quadratic response satisfies the parallelogram identity;
2. polarization recovers a fixed symmetric bilinear form only in the quadratic branch;
3. a Hessian gives a local quadratic approximation but not exact metric ontology;
4. quartic/Finsler-like response gives explicit obstruction witnesses;
5. downstream GR gates depend on the quadratic response selector.
```

## What Is Not Proved

This folder does not prove that the parent vacuum ontology forces exact
quadratic response. That remains the central open selector unless a later proof
excludes or routes all nonquadratic directional-response channels.

## Current Interpretation

The scalar admissibility ladder remains the first scalar projection seed. The
metric branch begins only when the directional response satisfies the
quadratic/parallelogram gate. If that gate fails, the correct continuation is
not automatic Einstein geometry but an explicit nonmetric branch.

## Next Frontier

A follow-up folder should attack the parent question directly:

```text
Does relational interval substance force exact parallelogram response,
or does it merely admit a Hessian metric approximation plus higher-order
response channels?
```
"""

out = Path(__file__).with_name('29_quadratic_response_selector_conclusion.md')
tmp = out.with_suffix(out.suffix + '.tmp')
tmp.write_text(md, encoding='utf-8')
tmp.replace(out)
print('Quadratic response selector conclusion passed.')
print(f'Wrote {out.resolve()}')
