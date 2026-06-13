# Appendix A. Static Bootstrap Algebra

This appendix collects the algebra behind Sec. 3.

The areal radial operator is

$$
\Delta_{\rm ar} f=\frac{1}{r^2}(r^2 f')'.
$$

For $A=e^s$,

$$
A'=e^s s',
$$

so

$$
r^2 A'=r^2 e^s s'.
$$

Applying the areal operator,

$$
\Delta_{\rm ar}(e^s)
=\frac{1}{r^2}\frac{d}{dr}(r^2 e^s s')
=e^s\left(s''+\frac{2}{r}s'+(s')^2\right).
$$

Since

$$
\Delta_{\rm ar}s=s''+\frac{2}{r}s',
$$

we obtain the identity

$$
\Delta_{\rm ar}(e^s)
=e^s\left(\Delta_{\rm ar}s+(s')^2\right).
$$

The source-free exterior flux law in the self-coupled variable is

$$
\Delta_{\rm ar}A=0.
$$

With $A=e^s$, this is

$$
\Delta_{\rm ar}s=-(s')^2.
$$

The bootstrap family is obtained by writing

$$
\Delta_{\rm ar}s=\lambda(s')^2 .
$$

Let $u=s'$. Then

$$
u'+\frac{2}{r}u=\lambda u^2 .
$$

Set $v=1/u$. Since $v'=-u'/u^2$, the equation becomes

$$
v'-\frac{2}{r}v=-\lambda .
$$

The solution is

$$
v=C r^2+\lambda r .
$$

Asymptotic normalization $s\sim-r_s/r$ fixes $C=1/r_s$, giving

$$
A_\lambda(r)
=\left(1+\lambda\frac{r_s}{r}\right)^{-1/\lambda}.
$$

The selected value $\lambda=-1$ gives

$$
A(r)=1-\frac{r_s}{r}.
$$

The sign of the field energy follows by reading the nonlinear term as
the field's own source at universal coupling:

$$
u_{\rm stat}
=\lambda\frac{c^4}{8\pi G}(s')^2.
$$

Thus the selected branch has

$$
u_{\rm stat}
=-\frac{c^4}{8\pi G}(s')^2.
$$

The corresponding verification script is
`vacuum_forge/src/field_equation_trials/002_trial_C_burden_ledger/trial_C2_self_coupling_bootstrap.py`.
