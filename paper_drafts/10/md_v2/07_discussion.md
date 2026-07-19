# 7. Discussion

The central result of this paper is that the stated static assumptions determine a complete one-parameter family rather than a unique exterior metric:

[
A_\lambda(r)
============

\left(
1+\lambda\frac{r_s}{r}
\right)^{-1/\lambda},
\qquad
B_\lambda(r)=A_\lambda(r)^{-1},
]

with

[
r_s=\frac{2GM}{c^2}.
]

This reframes the disagreement over simple derivations of the Schwarzschild metric. The assumptions are strong enough to recover the Schwarzschild scale and to include Schwarzschild as the member

[
\lambda=-1,
]

but they do not by themselves select that value.

The possibility, impossibility, and family viewpoints can therefore be understood as emphasizing different parts of the same result. Schwarzschild is possible within the assumptions; its unique derivation is impossible without further input; and the residual freedom is represented by the parameter (\lambda).

## 7.1 Additional inputs in simple derivations

The family makes it possible to distinguish the assumptions that construct the candidate class from the additional conditions that select a particular member. Several familiar derivations may be organized in this way.

| Route                                 | Additional input                                                  | Role relative to the family                                                     |
| ------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Michell and Laplace                   | Newtonian escape condition                                        | Identifies the scale (2GM/c^2), but does not determine a metric                 |
| Lenz–Sommerfeld and related arguments | Relativistic reinterpretation of Newtonian motion                 | Supplies additional kinematic or metric assumptions                             |
| Visser; Czerniawski                   | Exact Newtonian infall profile in a flat-slice representation     | Selects the Schwarzschild member                                                |
| Kassner                               | Exact force, orbital, or dust-ball condition                      | Adds dynamical or observational information beyond the base assumptions         |
| Shuler; Kassner                       | Reduction of a broader metric family by additional physical tests | Constrains or selects the admissible member                                     |
| Bootstrapped Newtonian models         | Nonlinear coupling calibrated to a desired exterior response      | Fixes the otherwise free nonlinear coefficient                                  |
| Deser; Duff                           | Consistent field self-coupling                                    | Supplies full dynamical equations whose static vacuum solution is Schwarzschild |

The table does not imply that these approaches are equivalent. Their assumptions, purposes, and levels of generality differ substantially. Their common structural feature is that each introduces information not contained in the assumptions of Sec. 2.

The relevant question is therefore not whether a derivation uses an assumption. Every derivation does. The relevant question is which assumptions determine the family and which additional condition selects the member.

## 7.2 Static accounting and observational selection

Section 4 examined whether a static gravitational-energy ledger could supply the missing selection condition. Within the gradient-local bookkeeping class defined there, the two-shell assembly calculation gives

[
\lambda=\frac{2f-1}{4},
\qquad
0\leq f\leq1,
]

and hence

[
-\frac14\leq\lambda\leq\frac14.
]

That interval excludes the Schwarzschild value (\lambda=-1).

The PPN calculation supplies a different kind of information. For the entire family,

[
\gamma=1,
\qquad
\beta=\lambda+2.
]

Thus the leading spatial PPN coefficient is common to all members, while the nonlinear temporal coefficient identifies the member:

[
\lambda=\beta-2.
]

The family is therefore underdetermined by the static construction but distinguishable by post-Newtonian measurement. Standard tests selecting (\beta\simeq1) select

[
\lambda\simeq-1.
]

The comparison between Secs. 4 and 5 is consequently direct:

[
\text{the specified static ledger does not select Schwarzschild,}
]

whereas

[
\text{the measured nonlinear metric coefficient does.}
]

## 7.3 Michell’s result

The Painlevé–Gullstrand representation provides a precise interpretation of Michell’s calculation.

For any member of the family, the static exterior may be written locally in the form

[
ds^2
====

-c^2dT^2
+
\left(dr+v_\lambda(r)dT\right)^2
+
r^2d\Omega^2,
]

with

[
v_\lambda^2(r)
==============

c^2\left[1-A_\lambda(r)\right].
]

The exact Newtonian infall relation

[
\frac12v^2=\frac{GM}{r}
]

requires

[
A(r)=1-\frac{r_s}{r},
]

which is precisely the Schwarzschild member (\lambda=-1).

For that selected member,

[
v^2=\frac{2GM}{r}
]

holds exactly in Painlevé–Gullstrand coordinates, and the condition

[
v=c
]

occurs at

[
r=r_s.
]

Michell’s calculation therefore identifies the correct scale, while the Schwarzschild geometry explains why the Newtonian-looking relation becomes exact in this representation.
