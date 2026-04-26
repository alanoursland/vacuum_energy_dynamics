"""Notebook-friendly display helpers (M32).

Provides pretty display methods for interactive research use.
Falls back gracefully to plain text in terminal environments.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import sympy

if TYPE_CHECKING:
    from vacuumforge.core.context import TheoryContext
    from vacuumforge.requirements.validators import ValidationResult


def _in_notebook() -> bool:
    """Detect if running in a Jupyter notebook."""
    try:
        from IPython import get_ipython
        shell = get_ipython()
        if shell is None:
            return False
        return shell.__class__.__name__ == "ZMQInteractiveShell"
    except (ImportError, NameError):
        return False


def _display_html(html: str) -> None:
    """Display HTML in notebook or print plain text."""
    if _in_notebook():
        from IPython.display import HTML, display
        display(HTML(html))
    else:
        # Strip tags for terminal
        import re
        text = re.sub(r"<[^>]+>", "", html)
        text = text.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">")
        print(text)


def _display_latex(expr: sympy.Basic) -> None:
    """Display a SymPy expression as LaTeX."""
    if _in_notebook():
        from IPython.display import Math, display
        display(Math(sympy.latex(expr)))
    else:
        print(sympy.pretty(expr))


class DisplayProxy:
    """Display helper attached to a TheoryContext."""

    def __init__(self, ctx: TheoryContext) -> None:
        self._ctx = ctx

    def ledger(self) -> None:
        """Display the theory ledger."""
        entries = self._ctx.ledger.all()
        if not entries:
            print("Ledger: empty")
            return

        lines = ["<table><tr><th>ID</th><th>Status</th><th>Statement</th></tr>"]
        for e in entries:
            lines.append(
                f"<tr><td>{e.id}</td><td>{e.status.value}</td>"
                f"<td>{e.statement}</td></tr>"
            )
        lines.append("</table>")
        _display_html("\n".join(lines))

    def assumptions(self) -> None:
        """Display active assumptions."""
        records = self._ctx.assumptions.active()
        if not records:
            print("No active assumptions.")
            return

        if _in_notebook():
            from IPython.display import Latex, display
            for rec in records:
                if isinstance(rec.expression, sympy.Basic):
                    display(Latex(f"**{rec.id}**: ${sympy.latex(rec.expression)}$"))
                else:
                    print(f"  {rec.id}: {rec.expression}")
        else:
            for rec in records:
                print(f"  [{rec.id}] {sympy.pretty(rec.expression)}")

    def symbols(self, kind: str | None = None) -> None:
        """Display registered symbols."""
        records = self._ctx.symbols.list(kind)
        if not records:
            print("No symbols registered.")
            return

        for rec in records:
            desc = f" — {rec.description}" if rec.description else ""
            if _in_notebook() and hasattr(rec.sympy_object, 'free_symbols'):
                from IPython.display import Latex, display
                display(Latex(f"${sympy.latex(rec.sympy_object)}$ ({rec.kind}){desc}"))
            else:
                print(f"  {rec.name} ({rec.kind}){desc}")

    def validation_results(self, results: list[ValidationResult] | None = None) -> None:
        """Display validation results."""
        if results is None:
            results = self._ctx.requirements.validate_all(self._ctx)

        icons = {"pass": "+", "fail": "X", "assumed": "~", "undetermined": "?"}
        colors = {"pass": "green", "fail": "red", "assumed": "orange", "undetermined": "gray"}

        if _in_notebook():
            lines = ["<table><tr><th></th><th>Requirement</th><th>Status</th><th>Message</th></tr>"]
            for r in results:
                color = colors.get(r.status, "black")
                icon = icons.get(r.status, "?")
                lines.append(
                    f"<tr><td>[{icon}]</td>"
                    f"<td>{r.requirement_id}</td>"
                    f"<td style='color:{color}'><b>{r.status.upper()}</b></td>"
                    f"<td>{r.message}</td></tr>"
                )
            lines.append("</table>")
            _display_html("\n".join(lines))
        else:
            for r in results:
                icon = icons.get(r.status, "?")
                print(f"  [{icon}] {r.requirement_id}: {r.status} — {r.message}")

    def expression(self, name_or_expr: str | sympy.Basic) -> None:
        """Display a named expression or SymPy expression."""
        if isinstance(name_or_expr, str):
            rec = self._ctx.expressions.get(name_or_expr)
            expr = rec.expr
            print(f"  {name_or_expr}:")
        else:
            expr = name_or_expr
        _display_latex(expr)

    def sources(self) -> None:
        """Display source configuration."""
        source_list = self._ctx.sources.list()
        if not source_list:
            print("No sources defined.")
            return
        for s in source_list:
            print(f"  {s.id} ({s.source_type}): {s.classification.value}")
            if s.J_kappa is not None:
                print(f"    J_kappa = {sympy.pretty(s.J_kappa)}")
            if s.J_sigma is not None:
                print(f"    J_sigma = {sympy.pretty(s.J_sigma)}")

    def energy(self) -> None:
        """Display energy functionals."""
        funcs = self._ctx.energy.list()
        if not funcs:
            print("No energy functionals defined.")
            return
        for f in funcs:
            print(f"  {f.id}:")
            _display_latex(f.expression)
