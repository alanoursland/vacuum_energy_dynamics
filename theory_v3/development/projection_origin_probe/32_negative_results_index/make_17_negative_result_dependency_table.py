import os
os.chdir(os.path.dirname(__file__))

from pathlib import Path
md="""# 17. Negative Result Dependency Table

| Negative result | Eliminates | Depends on |
|---|---|---|
| Scalar trace cannot see traceless data | scalar-as-full-tensor | tensor trace split |
| Scalar monopole cannot see multipoles | monopole-as-angular-data | angular projection |
| Scalar nonlinear PN no-go | scalar-only GR completion | PN tensor requirements |
| Stress coupling not matter ontology | stress-as-microphysics | matter-action variation |
| Finite flux not R | flux-as-projection-chart | compactified moment ladder |
| Nonquadratic hidden metric no-go | Finsler-inside-metric | parallelogram gate |
| EH from r_k no-go | coefficient-to-GR leap | action assumption ledger |

## Closed result

The negative results are not all independent, but they eliminate distinct
failure modes.
"""
Path('17_negative_result_dependency_table.md').write_text(md)
