"""AST-based linting for hardcoded validation verdicts.

Implements Milestones 42-43 from the validation-hardening technical design:
- Pattern detection for verdict-emitting sites (print, status_line, dataclass).
- Trace-back analysis with bounded recursion to determine whether a verdict
  is gated on a real computation.
- Import-aware recognition of sympy and vacuumforge names.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path

VERDICT_WORDS = {
    "PASS",
    "CLOSED",
    "DERIVED",
    "DEFER",
    "BRANCH_KILLED",
    "FAIL",
    "FAILED",
}

# Well-known validation function names recognised regardless of import alias.
VALIDATION_LEAF_CALLS = {"is_zero", "check_equal", "simplify", "validate", "validate_all"}

# Maximum depth for trace-back through variable assignments.
_MAX_TRACE_DEPTH = 5


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

@dataclass
class VerdictSite:
    path: Path
    line: int
    column: int
    pattern: str  # "pass_print", "status_line", "dataclass_status"
    detail: str
    node: ast.AST = field(repr=False)


@dataclass
class VerdictClassification:
    site: VerdictSite
    severity: str  # "OK", "WARN", "FAIL"
    message: str
    rule_name: str = ""


@dataclass
class FileLintResult:
    path: Path
    classifications: list[VerdictClassification]
    has_validation_imports: bool = True
    syntax_error: str | None = None

    @property
    def severity(self) -> str:
        if self.syntax_error:
            return "FAIL"
        severities = {c.severity for c in self.classifications}
        if "FAIL" in severities:
            return "FAIL"
        if "WARN" in severities:
            return "WARN"
        return "OK"


# ---------------------------------------------------------------------------
# Import resolution
# ---------------------------------------------------------------------------

class _ImportCollector(ast.NodeVisitor):
    """Walk the AST to build a mapping from local names to their module roots."""

    def __init__(self) -> None:
        # Maps local name -> set of module root strings.
        # e.g. ``import sympy as sp`` -> {"sp": {"sympy"}}
        #      ``from vacuumforge.core.simplify import is_zero`` -> {"is_zero": {"vacuumforge"}}
        self.name_roots: dict[str, set[str]] = {}
        # Set of all imported root module names.
        self.imported_roots: set[str] = set()

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            root = alias.name.split(".")[0]
            local = alias.asname or alias.name
            self.name_roots.setdefault(local, set()).add(root)
            self.imported_roots.add(root)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module is None:
            return
        root = node.module.split(".")[0]
        self.imported_roots.add(root)
        for alias in node.names:
            local = alias.asname or alias.name
            self.name_roots.setdefault(local, set()).add(root)


def _collect_imports(tree: ast.AST) -> _ImportCollector:
    collector = _ImportCollector()
    collector.visit(tree)
    return collector


# ---------------------------------------------------------------------------
# Parent annotation
# ---------------------------------------------------------------------------

def _annotate_parents(node: ast.AST) -> None:
    """Annotate every node with a ``_parent`` attribute."""
    for child in ast.walk(node):
        for sub in ast.iter_child_nodes(child):
            sub._parent = child  # type: ignore[attr-defined]


# ---------------------------------------------------------------------------
# Scope-level assignment collection
# ---------------------------------------------------------------------------

def _collect_assignments(scope: ast.AST) -> dict[str, list[ast.AST]]:
    """Map variable names to their assignment value nodes within *scope*.

    Only collects simple ``name = value`` assignments (not augmented, tuple
    unpacking, etc.).  Returns the value side of the assignment.
    """
    assigns: dict[str, list[ast.AST]] = {}
    for node in ast.walk(scope):
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                assigns.setdefault(target.id, []).append(node.value)
    return assigns


# ---------------------------------------------------------------------------
# Pattern matchers
# ---------------------------------------------------------------------------

class _SiteFinder(ast.NodeVisitor):
    """Walk the AST and collect verdict-emitting sites."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.sites: list[VerdictSite] = []

    def visit_Call(self, node: ast.Call) -> None:
        name = _call_name(node.func)

        if name == "print" and node.args and _contains_verdict_literal(node.args[0]):
            self.sites.append(
                VerdictSite(self.path, node.lineno, node.col_offset, "pass_print",
                            "print verdict", node)
            )
        elif name == "status_line":
            self.sites.append(
                VerdictSite(self.path, node.lineno, node.col_offset, "status_line",
                            "status_line verdict", node)
            )
        elif _has_verdict_status_keyword(node):
            self.sites.append(
                VerdictSite(self.path, node.lineno, node.col_offset, "dataclass_status",
                            "literal status field", node)
            )

        self.generic_visit(node)


# ---------------------------------------------------------------------------
# Trace-back analysis
# ---------------------------------------------------------------------------

def _depends_on_validation(
    node: ast.AST,
    imports: _ImportCollector,
    assignments: dict[str, list[ast.AST]],
    depth: int = 0,
) -> bool:
    """Recursively determine whether *node* traces back to a validation call.

    Walks the expression tree looking for function calls whose root module is
    sympy or vacuumforge (resolved through actual imports).  If a bare
    ``Name`` is found, attempts to trace through variable assignments up to
    ``_MAX_TRACE_DEPTH`` levels.
    """
    if depth > _MAX_TRACE_DEPTH:
        # Exceeded recursion bound — conservatively assume OK.
        return True

    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            if _is_validation_call(child, imports):
                return True

        # Trace variable references back through assignments.
        if isinstance(child, ast.Name) and child.id in assignments:
            for value_node in assignments[child.id]:
                if _depends_on_validation(value_node, imports, assignments, depth + 1):
                    return True

    return False


def _is_validation_call(call: ast.Call, imports: _ImportCollector) -> bool:
    """Return True if *call* is a sympy or vacuumforge validation call."""
    name = _call_name(call.func)
    if name is None:
        return False

    parts = name.split(".")
    root = parts[0]
    leaf = parts[-1]

    # Check if the leaf function name is a known validation function.
    if leaf in VALIDATION_LEAF_CALLS:
        return True

    # Check if the root resolves to sympy or vacuumforge via imports.
    roots = imports.name_roots.get(root, set())
    if roots & {"sympy", "vacuumforge"}:
        return True

    return False


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

def _classify_site(
    site: VerdictSite,
    imports: _ImportCollector,
    assignments: dict[str, list[ast.AST]],
) -> VerdictClassification:
    # Pattern C: dataclass constructor with a verdict literal.
    if site.pattern == "dataclass_status":
        return VerdictClassification(
            site, "FAIL",
            "verdict-like status is a literal constructor input",
            rule_name="verdict_in_dataclass_literal",
        )

    # Pattern B: status_line(label, ok, ...).
    if site.pattern == "status_line":
        call = site.node
        assert isinstance(call, ast.Call)
        if len(call.args) < 2:
            return VerdictClassification(
                site, "WARN", "status_line has no condition argument",
                rule_name="status_line_with_no_computation",
            )
        condition = call.args[1]
        if _is_literal(condition):
            return VerdictClassification(
                site, "WARN", "status_line condition is literal",
                rule_name="status_line_with_literal",
            )
        if _depends_on_validation(condition, imports, assignments):
            return VerdictClassification(
                site, "OK", "status_line is gated on validation computation",
            )
        return VerdictClassification(
            site, "WARN",
            "status_line condition is not traceable to validation",
            rule_name="status_line_with_no_computation",
        )

    # Pattern A: print("[PASS] ...").
    enclosing = _enclosing_if(site.node)
    if enclosing is None:
        return VerdictClassification(
            site, "WARN", "verdict print is unconditional",
            rule_name="unconditional_pass_print",
        )
    if _is_literal(enclosing.test):
        return VerdictClassification(
            site, "WARN", "verdict print is gated on a literal",
            rule_name="unconditional_pass_print",
        )
    if _depends_on_validation(enclosing.test, imports, assignments):
        return VerdictClassification(
            site, "OK", "verdict print is gated on validation computation",
        )
    return VerdictClassification(
        site, "WARN",
        "verdict print gate is not traceable to validation",
        rule_name="unconditional_pass_print",
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def lint_file(path: str | Path) -> FileLintResult:
    """Analyse a single Python file and return a lint result."""
    path = Path(path)
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        return FileLintResult(path, [], syntax_error=str(exc))

    _annotate_parents(tree)
    imports = _collect_imports(tree)
    assignments = _collect_assignments(tree)

    finder = _SiteFinder(path)
    finder.visit(tree)

    classifications = [_classify_site(s, imports, assignments) for s in finder.sites]

    # INFO-level check: verdicts present but no validation imports.
    has_validation_imports = bool(imports.imported_roots & {"sympy", "vacuumforge"})
    if finder.sites and not has_validation_imports:
        classifications.append(
            VerdictClassification(
                VerdictSite(path, 0, 0, "missing_imports", "no validation imports", tree),
                "WARN",
                "Script emits verdicts but imports neither sympy nor vacuumforge.",
                rule_name="missing_validation_imports",
            )
        )

    return FileLintResult(path, classifications, has_validation_imports=has_validation_imports)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _call_name(func: ast.AST) -> str | None:
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        base = _call_name(func.value)
        return f"{base}.{func.attr}" if base else func.attr
    return None


def _contains_verdict_literal(node: ast.AST) -> bool:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return any(word in node.value for word in VERDICT_WORDS)
    if isinstance(node, ast.JoinedStr):
        return any(_contains_verdict_literal(v) for v in node.values)
    return False


def _has_verdict_status_keyword(node: ast.Call) -> bool:
    for kw in node.keywords:
        if kw.arg == "status" and isinstance(kw.value, ast.Constant):
            return isinstance(kw.value.value, str) and kw.value.value in VERDICT_WORDS
    return False


def _is_literal(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant)


def _enclosing_if(node: ast.AST) -> ast.If | None:
    current = getattr(node, "_parent", None)
    while current is not None:
        if isinstance(current, ast.If):
            return current
        current = getattr(current, "_parent", None)
    return None
