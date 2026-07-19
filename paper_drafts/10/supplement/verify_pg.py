"""Standalone symbolic checks for finite-radius zeros and river coordinates."""

import sympy as sp


passed = 0


def check(label, condition):
    global passed
    ok = bool(condition)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        raise AssertionError(label)
    passed += 1


def is_zero(expr):
    return sp.simplify(expr) == 0


def curvature(metric, coords):
    n = len(coords)
    inverse = metric.inv()
    christoffel = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                christoffel[a][b][c] = sp.together(
                    sum(
                        inverse[a, d]
                        * (
                            sp.diff(metric[d, b], coords[c])
                            + sp.diff(metric[d, c], coords[b])
                            - sp.diff(metric[b, c], coords[d])
                        )
                        for d in range(n)
                    )
                    / 2
                )
    ricci = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c in range(n):
                expr += sp.diff(christoffel[c][a][b], coords[c])
                expr -= sp.diff(christoffel[c][a][c], coords[b])
                for d in range(n):
                    expr += christoffel[c][c][d] * christoffel[d][a][b]
                    expr -= christoffel[c][a][d] * christoffel[d][c][b]
            ricci[a, b] = sp.together(expr)
    scalar = sp.together(
        sum(inverse[i, j] * ricci[i, j] for i in range(n) for j in range(n))
    )
    return christoffel, ricci, scalar


def riemann_lower(metric, coords):
    n = len(coords)
    christoffel, _, _ = curvature(metric, coords)
    upper = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    expr = sp.diff(christoffel[a][b][d], coords[c])
                    expr -= sp.diff(christoffel[a][b][c], coords[d])
                    for e in range(n):
                        expr += christoffel[a][c][e] * christoffel[e][b][d]
                        expr -= christoffel[a][d][e] * christoffel[e][b][c]
                    upper[a][b][c][d] = sp.together(expr)
    lower = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    lower[a][b][c][d] = sp.together(
                        sum(metric[a, e] * upper[e][b][c][d] for e in range(n))
                    )
    return lower


def kretschmann(metric, coords):
    n = len(coords)
    lower = riemann_lower(metric, coords)
    inverse = metric.inv()
    result = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    raised = 0
                    for e in range(n):
                        for f in range(n):
                            for g in range(n):
                                for h in range(n):
                                    raised += (
                                        inverse[a, e]
                                        * inverse[b, f]
                                        * inverse[c, g]
                                        * inverse[d, h]
                                        * lower[e][f][g][h]
                                    )
                    result += lower[a][b][c][d] * raised
    return sp.simplify(result)


G, M, c, r_s = sp.symbols("G M c r_s", positive=True)
r = sp.Symbol("r", positive=True)

# Michell radius and family-wide finite-radius zero dichotomy.
r_michell = sp.solve(sp.Eq(c**2 / 2, G * M / r), r)[0]
check("Michell radius is 2GM/c^2", is_zero(r_michell - 2 * G * M / c**2))

lam_neg = sp.Symbol("lambda_minus", negative=True)
lam_pos = sp.Symbol("lambda_plus", positive=True)
r_0 = -lam_neg * r_s
A_neg = (1 + lam_neg * r_s / r) ** (-1 / lam_neg)
A_pos = (1 + lam_pos * r_s / r) ** (-1 / lam_pos)
check(
    "lambda<0 gives a finite-radius zero at -lambda r_s",
    bool(r_0.is_positive) and is_zero(sp.limit(A_neg, r, r_0, dir="+")),
)
check("lambda=-1 puts the Schwarzschild horizon at r_s", is_zero(r_0.subs(lam_neg, -1) - r_s))
check("lambda=0 exponential member has no finite-radius zero", bool(sp.exp(-r_s / r).is_positive))
check("lambda>0 members have no finite-radius zero", bool(A_pos.is_positive))

# The Michell route has no spatial response; AB=1 gives gamma=1.
u = sp.Symbol("u", positive=True)
gamma_michell = sp.series(sp.Integer(1), u, 0, 2).removeO().coeff(u, 1) / 2
gamma_compensated = sp.series(1 / (1 - 2 * u), u, 0, 2).removeO().coeff(u, 1) / 2
check("Michell route has gamma=0", is_zero(gamma_michell))
check("compensated branch has gamma=1", is_zero(gamma_compensated - 1))

# Painleve-Gullstrand metric with inward river speed v=c sqrt(r_s/r).
t, theta, phi = sp.symbols("t theta phi")
v = c * sp.sqrt(r_s / r)
metric = sp.Matrix(
    [
        [-(c**2 - v**2), v, 0, 0],
        [v, 1, 0, 0],
        [0, 0, r**2, 0],
        [0, 0, 0, r**2 * sp.sin(theta) ** 2],
    ]
)
coords = [t, r, theta, phi]
_, ricci, scalar = curvature(metric, coords)
einstein = ricci - scalar * metric / 2
vacuum = all(is_zero(einstein[i, j]) for i in range(4) for j in range(4))
check("river metric is vacuum", vacuum)

K = kretschmann(metric, coords)
check("Kretschmann scalar is 12 r_s^2/r^6", is_zero(K - 12 * r_s**2 / r**6))
check(
    "river kinetic profile is GM/r",
    is_zero((v**2 / 2 - G * M / r).subs(r_s, 2 * G * M / c**2)),
)
check("river speed reaches c at r_s", is_zero(v.subs(r, r_s) - c))

expected = 11
if passed != expected:
    raise AssertionError(f"expected {expected} checks, ran {passed}")
print(f"\n{passed}/{expected} checks passed")
