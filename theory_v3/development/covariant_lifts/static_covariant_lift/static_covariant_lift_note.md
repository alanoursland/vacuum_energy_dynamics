# Covariant Lift of the C2/C3 Static Bookkeeping Sector

## Statement

Trials C2 and C3 proved the static sector in reduced variables: areal
gauge $ds^2 = -c^2 A(r)\,dt^2 + B(r)\,dr^2 + r^2 d\Omega^2$, staticity
assumed, ODEs in $r$. This note lifts each reduced statement to a
covariant statement about the closed parent
$G_{ab} + \Lambda g_{ab} = (8\pi G/c^4) T_{ab}$ (at $\Lambda = 0$ for
the asymptotically flat statics; the SdS extension is in trial F1).

## 1. The flux law is the covariant tt-equation (Lemma 1 lift)

For a general static spherical metric,

$$
\boxed{\;G^t{}_t = -\frac{1}{r^2}\frac{d}{dr}\Big[r\Big(1-\tfrac1B\Big)\Big]\;}
$$

identically. With the **Misner–Sharp mass**

$$
m(r) \equiv \frac{c^2 r}{2G}\Big(1-(\nabla r)^2\Big),
\qquad (\nabla r)^2 = g^{rr} = \tfrac1B ,
$$

the covariant equation $N\,G^t{}_t = T^t{}_t = -\rho c^2$ with
$N = c^4/8\pi G$ reads

$$
m'(r) = \frac{4\pi r^2}{c^2}\,\rho .
$$

This is Lemma 1's areal flux law, with the enclosed mass now a
quasilocal geometric invariant: $r$ is defined by the orbit area
$4\pi r^2$ and $(\nabla r)^2$ is a scalar. No gauge choice remains in
the statement.

## 2. The P7′ shadow is chart-invariant (Lemma 2 lift)

In an arbitrary radial chart
$ds^2 = -c^2 a(\rho)\,dt^2 + b(\rho)\,d\rho^2 + R(\rho)^2 d\Omega^2$,

$$
G^t{}_t - G^\rho{}_\rho
= -\frac{R'}{R\,b}\,\frac{d}{d\rho}\ln\!\frac{a\,b}{R'^2},
$$

verified from scratch. The shadow variable is the invariant combination
$a b/R'^2$ — exactly the areal-gauge product $AB$ after the relabeling
$r = R(\rho)$. Since $(\nabla r)^2 = R'^2/b$ and the static Killing
norm is $-\xi^2/c^2 = a$, the shadow $AB=1$ is the chart-free statement

$$
\boxed{\;(\nabla r)^2 = -\xi^2/c^2\;}
$$

P7′ constrains geometry, not coordinates. Witness: Schwarzschild
rewritten with $r = \rho + r_s e^{-\rho/r_s}$ still satisfies both the
vacuum equations and the invariant shadow.

## 3. The C2 bootstrap equation is the covariant vacuum tt-equation (Theorem 1 lift)

On the compensated branch $B = 1/A$:

$$
G^t{}_t = \frac{rA' + A - 1}{r^2},
\qquad
\frac{d}{dr}\big[r^2\,G^t{}_t\big] = r\,\Delta_{\rm areal} A .
$$

With the exponential identity
$\Delta_{\rm areal} e^s = e^s(\Delta_{\rm areal}s + (s')^2)$, the C2
self-coupling equation $\Delta_{\rm areal}s = -(s')^2$ is the covariant
vacuum tt-equation's content. The solution families coincide under
asymptotic flatness:

$$
\{\Delta_{\rm areal}A = 0,\ A\to1\} \;=\; \{G^t{}_t = 0,\ B=1/A\}
\;=\; \{A = 1 + C/r\}.
$$

The angular equation is then implied: all $G^a{}_b$ vanish on the
selected solution (the Bianchi identity in static spherical form).
The bookkeeping route and the covariant route are one route, seen in
two variable sets.

## 4. Staticity is derived, not assumed (Birkhoff-type lift)

For time-dependent spherical $A(t,r)$, $B(t,r)$ in the areal chart:

$$
G_{tr} = \frac{\dot B}{r B}
\;\Rightarrow\;
\text{vacuum forces } B = B(r);
$$

$G^t{}_t$ then depends only on $B$ and gives $B = (1 + C_1/r)^{-1}$;
the t–r identity forces $A = h(t)/B$; and $h(t)$ is pure relabeling —
the Kretschmann invariant equals $12\,r_s^2/r^6$ for arbitrary
$h(t) > 0$, so $d\tau = \sqrt{h}\,dt$ (a K3 gauge move) lands on the
static solution. The static assumption of C2/C3 is therefore a theorem
of the spherical vacuum sector of the closed parent.

## What This Retires

This retires the "covariant lift of the C2/C3 static bookkeeping
sector" rigor debt of `04_field_equations/06_rigor_closures.md`. It
moves no coefficient and changes no equation. Nonlinear stability is
handled separately (020).

## Verification

```text
vacuum_forge/src/field_equation_trials/019_static_covariant_lift/static_covariant_lift.py
```

Archive record: `covariant_statics_lift_019`, with declared
dependencies on `bootstrap_family_exact_solution_c2` and
`tr_block_identity_c3`.
