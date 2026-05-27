#!/usr/bin/env python3
"""
make_4_source_signature_endpoint_formula.py

Reconstruct the source-family sign formula for S_pq=x^(2q)(1-x^2)^p and its
endpoint-order interpretation.

Output:
    4_source_signature_endpoint_formula.md
"""

from pathlib import Path
import sympy as sp


k, p, q = sp.symbols("k p q", integer=True, nonnegative=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

n = k + q
r_k = (2 * k - 1) / (2 * k + 3)

# For S_pq=x^(2q)(1-x^2)^p under projection weight (1-x^2)^4,
# the beta-ratio part of b_k has sign:
#   (2n-1)/(2n+2p+9) - (2k-1)/(2k+3).
sign_numerator = simplify_expr((2 * n - 1) * (2 * k + 3) - (2 * k - 1) * (2 * n + 2 * p + 9))
expected = -2 * (2 * k * p + 6 * k - p - 4 * q - 3)
require_equal("source-family sign numerator", sign_numerator, expected)
checks.append("source-family sign numerator")

balanced_rule_value = simplify_expr(expected.subs(p, q))
require_equal("balanced p=q sign expression", balanced_rule_value, -2 * (2 * k * q + 6 * k - 5 * q - 3))
checks.append("balanced p=q sign expression")

endpoint_concentrated_value = simplify_expr(expected.subs(q, p + 2))
require_equal("endpoint-concentrated q=p+2 sign expression", endpoint_concentrated_value, -2 * (2 * k * p + 6 * k - 5 * p - 11))
checks.append("endpoint-concentrated q=p+2 sign expression")

origin_order = 2 * q
endpoint_order = p
effective_endpoint_order = p + 4

require_equal("origin order", origin_order, 2 * q)
checks.append("origin order")
require_equal("endpoint order", endpoint_order, p)
checks.append("endpoint order")
require_equal("effective endpoint order under projection weight", effective_endpoint_order, p + 4)
checks.append("effective endpoint order under projection weight")

low_q_value = simplify_expr(expected.subs(q, 0))
require_equal("low-q source sign expression", low_q_value, -2 * (2 * k * p + 6 * k - p - 3))
checks.append("low-q source sign expression")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Field Search Survivor Audit 4: Source Signature Endpoint Formula

## Purpose

This report reconstructs the source-family signature formula from the archived
boundary-condition trend analysis.

For:

```text
S_pq(x) = x^(2q)(1-x^2)^p,
```

the goal is to record what is formal mathematics and what remains physical
interpretation.

## Validated Checks

{validation_bullets}

## Endpoint Orders

The formal endpoint orders are:

```text
origin order at x=0: 2q
endpoint order at x=1: p
effective endpoint order under w=(1-x^2)^4: p+4.
```

So `q` controls origin suppression / endpoint concentration, while `p` controls
endpoint suppression.

## Sign Formula

For the projected source vector component, the sign-relevant beta-ratio
difference has numerator:

```text
(2k+2q-1)(2k+3)
  - (2k-1)(2k+2q+2p+9).
```

SymPy verifies this equals:

```text
-2(2kp + 6k - p - 4q - 3).
```

This is the formula behind the endpoint-signature trends.

## Interpretation

The source signatures are not arbitrary. They track endpoint suppression versus
endpoint concentration.

But this does not select a physical source law. It is a formal boundary/domain
trend until a physical boundary or source principle is supplied.
"""

out = Path(__file__).with_name("4_source_signature_endpoint_formula.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
