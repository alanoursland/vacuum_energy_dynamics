"""Candidate equation search via coefficient constraint solving.

Given a parameterized energy family and a set of requirements,
derives coefficient constraints that satisfy those requirements.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import sympy


@dataclass
class CandidateSolution:
    """A set of coefficient constraints satisfying requirements."""

    substitutions: dict[sympy.Symbol, sympy.Basic] = field(default_factory=dict)
    conditions: list[sympy.Basic] = field(default_factory=list)
    passes: list[str] = field(default_factory=list)
    fails: list[str] = field(default_factory=list)
    undetermined: list[str] = field(default_factory=list)
    reasoning: list[str] = field(default_factory=list)


def search_energy_coefficients(
    energy_expr: sympy.Basic,
    variables: list[sympy.Basic],
    coefficients: list[sympy.Symbol],
    requirements: dict[str, dict],
) -> CandidateSolution:
    """Search for coefficient constraints satisfying requirements.

    Requirements dict maps requirement names to specs:
      {
        "unsourced_kappa_zero": {
            "type": "equilibrium_zero",
            "variable": kappa,
            "source_zero": J_kappa,
        },
        "nonzero_sigma": {
            "type": "equilibrium_nonzero",
            "variable": sigma,
            "source_symbol": J_sigma,
        },
        "positive_energy": {
            "type": "positivity",
        },
      }
    """
    result = CandidateSolution()

    # Derive stationary equations
    stat_eqs = [sympy.diff(energy_expr, var) for var in variables]
    solutions = sympy.solve(stat_eqs, variables, dict=True)

    if not solutions:
        result.fails.append("No stationary solution found")
        result.reasoning.append("sympy.solve returned no solutions for stationary conditions")
        return result

    sol = solutions[0]
    result.reasoning.append(f"Stationary solution: {sol}")

    for req_name, spec in requirements.items():
        req_type = spec.get("type", "")

        if req_type == "equilibrium_zero":
            var = spec["variable"]
            source_zero = spec.get("source_zero")
            eq_val = sol.get(var)
            if eq_val is None:
                result.undetermined.append(req_name)
                continue

            if source_zero is not None:
                eq_val_sourced = eq_val.subs(source_zero, 0)
            else:
                eq_val_sourced = eq_val

            if sympy.simplify(eq_val_sourced) == 0:
                result.passes.append(req_name)
                result.reasoning.append(
                    f"{req_name}: {var} = {eq_val}, with {source_zero}=0 gives {var}=0"
                )
            else:
                result.fails.append(req_name)
                result.reasoning.append(
                    f"{req_name}: {var} = {eq_val_sourced} (nonzero)"
                )

        elif req_type == "equilibrium_nonzero":
            var = spec["variable"]
            source_sym = spec.get("source_symbol")
            eq_val = sol.get(var)
            if eq_val is None:
                result.undetermined.append(req_name)
                continue

            if eq_val == 0:
                result.fails.append(req_name)
                result.reasoning.append(f"{req_name}: {var} = 0 (should be nonzero)")
            elif source_sym and eq_val.has(source_sym):
                result.passes.append(req_name)
                result.reasoning.append(
                    f"{req_name}: {var} = {eq_val} (depends on {source_sym})"
                )
            else:
                result.undetermined.append(req_name)
                result.reasoning.append(f"{req_name}: {var} = {eq_val} (cannot determine)")

        elif req_type == "positivity":
            from vacuumforge.energy.positivity import check_quadratic_positivity
            pos = check_quadratic_positivity(energy_expr, variables)
            if pos.status == "positive":
                result.passes.append(req_name)
            elif pos.status == "indefinite":
                result.fails.append(req_name)
                result.conditions.extend(pos.conditions)
            else:
                result.undetermined.append(req_name)
                result.conditions.extend(pos.conditions)
            result.reasoning.append(f"{req_name}: positivity status = {pos.status}")

    return result
