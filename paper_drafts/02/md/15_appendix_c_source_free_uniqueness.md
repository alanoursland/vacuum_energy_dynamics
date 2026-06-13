# Appendix C. Source-Free Uniqueness

The source-free static constraint equation is

$$
\Delta_{\rm ar}A=0,
$$

or

$$
(r^2 A')'=0.
$$

Integrating once,

$$
r^2 A'=C_1.
$$

Then

$$
A'=\frac{C_1}{r^2},
$$

and hence

$$
A(r)=C_0-\frac{C_1}{r}.
$$

Asymptotic flatness gives

$$
\lim_{r\to\infty}A(r)=1,
$$

so

$$
C_0=1.
$$

If there is no source at the origin, regularity excludes the $1/r$ term,
so

$$
C_1=0.
$$

Therefore

$$
A(r)\equiv1.
$$

The zero-source regular asymptotically flat static solution is unique.
This proves the source-slavery statement used in Sec. 5: the negative
static sector is not an independent reservoir. It exists only as a
response to sources or boundary data that represent sources.

The corresponding verification appears as the G02 result in
`vacuum_forge/src/field_equation_trials/006_gate_G03_radiative_positivity/gate_G03_radiative_positivity.py`.
