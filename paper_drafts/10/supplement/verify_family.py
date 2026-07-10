"""Standalone symbolic checks for Sections 2-5 of Paper 10."""

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


def radial_laplacian(expr, radius):
    return sp.diff(radius**2 * sp.diff(expr, radius), radius) / radius**2


r, r_s = sp.symbols("r r_s", positive=True)
lam, mu = sp.symbols("lambda mu", real=True, nonzero=True)

# Constant-weight resummation and exact family.
s_fn = sp.Function("s")(r)
identity = radial_laplacian(sp.exp(mu * s_fn), r) - mu * sp.exp(mu * s_fn) * (
    radial_laplacian(s_fn, r) + mu * sp.diff(s_fn, r) ** 2
)
check("resummation identity", is_zero(identity))

s = -sp.log(1 + lam * r_s / r) / lam
A = sp.exp(s)
family_residual = radial_laplacian(s, r) - lam * sp.diff(s, r) ** 2
check("A_lambda solves the constant-weight vacuum equation", is_zero(family_residual))

A_series = sp.series(A, r_s, 0, 3).removeO().expand()
check("Newtonian coefficient is -r_s/r", is_zero(A_series.coeff(r_s, 1) + 1 / r))
check(
    "second-order areal coefficient is (1+lambda)/2",
    is_zero(A_series.coeff(r_s, 2) - (1 + lam) / (2 * r**2)),
)
check("lambda=-1 is Schwarzschild", is_zero(A.subs(lam, -1) - (1 - r_s / r)))
check("lambda=0 limit is exponential", is_zero(sp.limit(A, lam, 0) - sp.exp(-r_s / r)))
check("lambda=+1 is reciprocal", is_zero(A.subs(lam, 1) - 1 / (1 + r_s / r)))

# Horizon dichotomy.
lam_neg = sp.Symbol("lambda_minus", negative=True)
lam_pos = sp.Symbol("lambda_plus", positive=True)
A_neg = (1 + lam_neg * r_s / r) ** (-1 / lam_neg)
A_pos = (1 + lam_pos * r_s / r) ** (-1 / lam_pos)
r_h = -lam_neg * r_s
check(
    "lambda<0 gives r_h=-lambda r_s and A approaches zero",
    bool(r_h.is_positive) and is_zero(sp.limit(A_neg, r, r_h, dir="+")),
)
check("lambda=0 has no finite-radius zero", bool(sp.exp(-r_s / r).is_positive))
check("lambda>0 has no finite-radius zero", bool(A_pos.is_positive))

# Invariant two-shell assembly ledger.
G, c, m1, m2, b = sp.symbols("G c m_1 m_2 b", positive=True)
R = sp.Symbol("R", positive=True)
work = sp.integrate(G * m1 * m2 / R**2, (R, b, sp.oo))
target = -work
check("assembly interaction energy is -G m1 m2/b", is_zero(target + G * m1 * m2 / b))

s1p = 2 * G * m1 / (c**2 * r**2)
s2p = 2 * G * m2 / (c**2 * r**2)
cross_density = lam * c**4 * 2 * s1p * s2p / (8 * sp.pi * G)
field_cross = sp.simplify(
    sp.integrate(cross_density * 4 * sp.pi * r**2, (r, b, sp.oo))
)
check("gradient-local cross term is 4 lambda G m1 m2/b", is_zero(field_cross - 4 * lam * G * m1 * m2 / b))

matter_cross = -2 * G * m1 * m2 / b
lam_rest = sp.solve(sp.Eq(field_cross, target), lam)
lam_redshift = sp.solve(sp.Eq(matter_cross + field_cross, target), lam)
check("rest-energy audit gives lambda=-1/4", lam_rest == [sp.Rational(-1, 4)])
check("redshift audit gives lambda=+1/4", lam_redshift == [sp.Rational(1, 4)])

f = sp.Symbol("f", real=True)
lam_f = sp.solve(sp.Eq(f * matter_cross + field_cross, target), lam)[0]
check("audited conventions give lambda=(2f-1)/4", is_zero(lam_f - (2 * f - 1) / 4))
check("Schwarzschild would require f=-3/2", sp.solve(sp.Eq(lam_f, -1), f) == [sp.Rational(-3, 2)])

phi_p = sp.Symbol("Phi_prime", real=True)
u_minus_one = -c**4 * (2 * phi_p / c**2) ** 2 / (8 * sp.pi * G)
u_newton = -phi_p**2 / (8 * sp.pi * G)
check("Schwarzschild self-source is four times Newtonian field energy", is_zero(u_minus_one / u_newton - 4))

# Areal-to-isotropic transform and PPN dictionary.
w = sp.Symbol("w")
a2 = (1 + lam) / 2
k1 = sp.Rational(1, 2)
k2 = (1 - 4 * a2) / 16
radius_ratio = 1 + k1 * w + k2 * w**2
x_iso = sp.series(w / radius_ratio, w, 0, 3).removeO()
A_iso = sp.series(1 - x_iso + a2 * x_iso**2, w, 0, 3).removeO().expand()
B_iso = sp.series(1 / A_iso, w, 0, 3).removeO()
dr_factor = radius_ratio - w * sp.diff(radius_ratio, w)
isotropy_residual = sp.series(B_iso * dr_factor**2 - radius_ratio**2, w, 0, 3).removeO()
check("areal-to-isotropic radial condition holds through second order", is_zero(isotropy_residual))

gamma = sp.expand(radius_ratio**2).coeff(w, 1)
beta = 2 * A_iso.coeff(w, 2)
check("gamma=1 for every family member", is_zero(gamma - 1))
check("beta=lambda+2", is_zero(beta - (lam + 2)))

# Vacuum response selector on B=1/A: G^t_t=0 iff r(1-A) is constant.
flux_derivative = sp.diff(r * (1 - A), r)
selector_coefficient = sp.series(flux_derivative, r_s, 0, 3).removeO().coeff(r_s, 2)
selector = sp.solve(sp.Eq(selector_coefficient, 0), lam)
check(
    "vacuum response selects lambda=-1",
    selector == [-1] and is_zero(flux_derivative.subs(lam, -1)),
)

expected = 21
if passed != expected:
    raise AssertionError(f"expected {expected} checks, ran {passed}")
print(f"\n{passed}/{expected} checks passed")
