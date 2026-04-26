# VacuumForge Known Limitations

## Symbolic Engine

- **SymPy simplification**: Some symbolic identities (e.g., `exp(x)*exp(-x) = 1`) require the numerical evaluation fallback in `is_zero()`. Complex expressions may occasionally fail to simplify.
- **Chained substitutions**: The assumption `apply()` method iterates up to 10 times, which handles common chains (B=1/A, A=exp(x)) but could in theory fail for very deep chains.
- **Cross-term positivity**: The Hessian-based positivity checker can determine definiteness for diagonal quadratic forms but returns "undetermined" for cross-coupled forms with symbolic coefficients.

## Scope and Generality

- **Algebraic prototype only**: Most results are derived in the algebraic-prototype scope. Coordinate-dependent field equations (Euler-Lagrange) are available but not yet integrated into the main validation pipeline.
- **3+1 generalization is experimental**: The higher-dimensional mode decomposition is a foundation only. No validation or PPN extraction is implemented for the 3+1 case.
- **Static isotropic coordinates**: Weak-field metric construction assumes static, spherically symmetric, isotropic coordinates. Other coordinate choices are not yet supported.
- **Single radial coordinate**: Field-equation support (M33) handles one independent coordinate only.

## Validation System

- **Conservative classification**: The model classifier may label a valid model as "exploratory" if it can't determine enough about it. This is by design — VacuumForge prefers undetermined over incorrect classification.
- **Leak detection heuristic**: Leak detection checks assumption expressions against target equivalent forms via SymPy simplification. Clever rewritings may evade detection.
- **No automated derivation**: VacuumForge validates but does not automatically derive new results. The user must construct the derivation chain manually.

## Persistence

- **SymPy version sensitivity**: Session files use `sympy.srepr` for serialization. Loading sessions across different SymPy versions may fail if internal representation changes.
- **No incremental save**: Sessions are saved as complete snapshots. There is no journaling or undo.

## Display and Reporting

- **Notebook detection**: The `_in_notebook()` check may not work in all Jupyter-like environments.
- **LaTeX rendering**: Report math rendering depends on the viewer supporting LaTeX. Plain-text fallback uses SymPy's pretty-printer.

## CLI

- **Basic feature set**: The CLI supports `new`, `validate`, `report`, `compare`, and `summary`. Interactive exploration requires the Python API.

## Not Yet Implemented

- Full Jinja2 template system for reports (currently uses string building)
- Mypy/pyright strict type checking pass
- Performance profiling and optimization
- Automated counterexample generation from failed validation
- Multi-session comparison persistence
