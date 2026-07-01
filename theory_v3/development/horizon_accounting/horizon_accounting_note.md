# The Horizon as an Accounting Corollary
## (and why this is not Michell's coincidence)

## Status

```text
result type:    supporting theorem, forge-verified (trial 021)
scope:          static spherical exterior of the closed parent; the
                interior cap obligation is untouched
conclusion:     the horizon's existence and location are corollaries of
                P9's count-once accounting; the Michell radius agreement
                is explained, not inherited
non-conclusion: nothing here claims the interior, changes any closed
                result, or adds a prediction beyond GR's
```

## The Claim Being Made Precise

The bookkeeping exterior of `04_field_equations/proof.md` §2 derives

$$A(r) = 1 - \frac{2GM}{c^2 r}$$

from three commitments — the flux law (P3a/P6 + Newton anchor), the
P9-selected distortion variable ($A = e^s$, count-once), and the P7′
compensation ($B = 1/A$) — with no tensor response law. The Schwarzschild
radius $r_s = 2GM/c^2$ is then simply the zero of the derived $A$. This
looks like "energy accounting gives the horizon easily," and it does.
The purpose of this note is to state exactly what that ease is worth,
because there is a famous trap here.

## The Trap: Michell's Coincidence

Michell (1784) and Laplace (1799) obtained the same radius from
Newtonian escape velocity: $\tfrac12 v^2 = GM/r$ with $v = c$ gives
$r = 2GM/c^2$. The agreement is exact — and accidental. The Newtonian
route uses the wrong kinetic energy (nonrelativistic) and the wrong
potential (Newtonian), and the errors cancel. The standard warning is
correct: getting $r_s$ from naive energy accounting is not evidence of
anything.

If VED's claim were "our ledger reproduces Michell," it would inherit
the coincidence. It does not. Three forge-verified discriminators
separate the routes.

## Theorem (horizon as accounting corollary)

**Within the C2 bootstrap family**
$A_\lambda = (1 + \lambda\, r_s/r)^{-1/\lambda}$ — the complete family of
accountings consistent with the flux law at first order — **a horizon
exists at finite radius if and only if $\lambda = -1$, the P9-selected
member, and it sits exactly at $r = r_s$.**

- $\lambda = -1$ (count-once): $A = 1 - r_s/r$, zero at $r = r_s$.
- $\lambda \to 0$ (log-linear counting, no self-energy):
  $A = e^{-r_s/r} > 0$ everywhere — **no horizon at any radius**.
- $\lambda = +1$ (wrong-weight counting): $A = (1+r_s/r)^{-1} > 0$
  everywhere — **no horizon at any radius**.

All three members agree at first post-Newtonian order; Michell-grade
accounting cannot distinguish them. The *existence* of the horizon —
not merely its location — is therefore a corollary of counting the
configuration energy exactly once at the universal coupling. Wrong
accounting does not move the horizon; it deletes it.

## Discriminator Table

| observable | Michell route | bookkeeping route (§2) |
|---|---|---|
| horizon radius | $2GM/c^2$ ✓ (by cancellation) | $2GM/c^2$ ✓ (zero of derived $A$) |
| horizon existence | asserted, not derived | P9 corollary (family selection) |
| spatial response | $B = 1$, $\gamma = 0$ — **half** the observed light deflection (0.875″; falsified 1919, excluded at $10^{-5}$ by Cassini) | $B = 1/A$, $\gamma = 1$ ✓ |
| second order | fails ($\beta$ undefined/wrong) | $\beta = 1$ (P9+C2 theorem) |
| full metric | none | exact, all orders |

A coincidence hands you a number. It cannot hand you a function.

## Why the Coincidence Happens (the river ledger)

The deepest part, forge-verified in trial 021: the derived exterior
admits the Painlevé–Gullstrand slicing

$$ds^2 = -c^2\,dT^2 + \big(dr + v(r)\,dT\big)^2 + r^2 d\Omega^2,
\qquad v(r) = c\sqrt{r_s/r},$$

verified from scratch to be exactly vacuum with Schwarzschild's
Kretschmann invariant $12 r_s^2/r^6$ (hence, by the 019 Birkhoff lift,
a relabeling of the derived exterior). In this slicing the infall
velocity satisfies

$$\tfrac12 v^2 = \frac{GM}{r} \quad\text{exactly, at every } r,
\qquad v(r_s) = c \quad\text{exactly}.$$

In GR pedagogy this exactness is the "river model" curiosity
(Hamilton–Lisle): the metric *happens* to admit a chart where Newtonian
bookkeeping is exact. In VED it is not a curiosity — it is the P6
kinetic-exchange ledger, and the *reason* it closes exactly at all
orders is the P9 resummation (the flux law is linear in $A = e^s$; the
self-energy corrections at every order are exactly absorbed). The same
mechanism explains Michell: the "two cancelling errors" cancel *because*
the exact theory's ledger is Newtonian-formed in this slicing. The
naive argument lands on the right number for a reason the naive
argument cannot state.

So the horizon acquires a ledger reading: it is the radius at which the
P6 exchange rate saturates the causal bound, $v = c$ — a statement
about the substance's bookkeeping, exactly coincident with the metric
statement $A = 0$.

## Honest Boundaries

1. **Exterior only.** The same ledger that finds the horizon announces
   its own breakdown at the horizon: the binding entry diverges as
   $-2GM^2/(R - r_s)$ at the doorstep
   (`04_field_equations/01_the_field_equations.md`). What happens at and
   inside $r_s$ is the interior-cap obligation, open.
2. **No new prediction.** Everything here is GR-exact; the content is
   *explanatory* (why naive accounting works at all, why the horizon is
   an accounting object) and *structural* (horizon existence as a P9
   selection witness), not predictive.
3. **Supersedes the exploratory language.** The old
   `notes/black_holes.md` "vacuum furnace / voracious consumption"
   framing predates the closure: the static ledger closes without a
   funding current (C2/C3), so static masses do not consume vacuum. The
   fence-compatible statement is the one above: the *dynamic* P6
   exchange of infalling matter saturates at the horizon; nothing is
   consumed by standing still.

## Verification

```text
vacuum_forge/src/field_equation_trials/021_horizon_accounting/horizon_accounting.py
```

Eleven checks: Michell/derived radius agreement; the zero-set of all
three family members; the $\gamma$ discriminator; PG vacuum, Kretschmann,
ledger exactness, and horizon saturation. Archive record:
`horizon_accounting_021`, with dependencies on
`bootstrap_family_exact_solution_c2` and `covariant_statics_lift_019`.

## References

Michell, J. (1784). *Phil. Trans. R. Soc.* 74, 35–57.
Laplace, P.-S. (1799). *Allgemeine geographische Ephemeriden* 4, 1.
Painlevé, P. (1921). *C. R. Acad. Sci.* 173, 677–680.
Gullstrand, A. (1922). *Ark. Mat. Astron. Fys.* 16, 1–15.
Hamilton, A. J. S., & Lisle, J. P. (2008). The river model of black
holes. *Am. J. Phys.* 76, 519–532.
