# The Field Equations of Vacuum Energy Dynamics

## Covariant statement

$$G_{ab} + \Lambda g_{ab} = \frac{8\pi G}{c^4}\,T_{ab}$$

equivalently, from the action (the strain functional, closed at
≤ 4-derivative order):

$$S \;=\; \frac{c^4}{16\pi G}\int\!\sqrt{-g}\,\big(R - 2\Lambda\big)\,d^4x
\;+\; S_{\text{matter}}
\qquad (+\ \text{Gauss-Bonnet, topological})$$

There is no other local gravitational freedom: the four-derivative
coefficient is exactly zero (forced by P7′ — see
`04_divergences_from_gr.md` for what that kill means physically), and
the Gauss-Bonnet term is inert in 4D.

## The reduced (working) forms

In the static spherical sector, with reduced variables
$\kappa=\tfrac12\ln(AB)$, $s=\tfrac12\ln(A/B)$ and P7′ setting
$\kappa=0$, $A=e^s$:

**Areal-flux law (statics):**
$$\Delta_{\text{areal}}\,A = \frac{8\pi G}{c^2}\rho
\qquad\Longrightarrow\qquad
F_A = 4\pi r^2 A' = \frac{8\pi G}{c^2}M_{\text{enc}},
\quad A_{\text{ext}} = 1-\frac{2GM}{c^2 r}$$

**Self-coupling content (the C2 bootstrap):**
$$\Delta_{\text{areal}}\,s = -(s')^2 + \text{source},
\qquad u_{\text{field}} = -\frac{c^4 (s')^2}{8\pi G}$$

**Radiative sector (TT), per polarization:**
$$K_T\,\Box h = \text{source},\qquad K_T = \frac{c^4}{16\pi G},
\qquad \langle u\rangle = \frac{c^2}{32\pi G}\langle\dot h_{ij}\dot h_{ij}\rangle$$

**Vector sector (stationary, divergence-free gauge):**
$$\Delta w_i = \frac{16\pi G}{c^2}\,\rho v_i
\qquad\Longrightarrow\qquad
w = -\frac{2G}{c^2}\,\frac{\mathbf S\times\mathbf r}{r^3}
\ \ \text{(Lense-Thirring)}$$

**Cosmological trace correction (quasi-static patch):**
$$AB-1 = \tfrac{3}{2}\,\Omega_m\Big(\frac{H_0 r}{c}\Big)^2
\qquad(\text{exactly } 0 \text{ in any pure-Λ epoch})$$

## Every coefficient, and where it was derived

| coefficient | value | derived by | anchor that could have killed it |
|---|---|---|---|
| static response $N$ | $c^4/8\pi G$ | C2+C3+P9+P7′ → 008 T2 | Newtonian limit (input anchor) |
| source law | $8\pi G/c^2$ | areal-flux derivation (C2) | Schwarzschild exterior, exact |
| TT kinetic $K_T$ | $c^4/16\pi G$ | radiative bootstrap (008) | binary-pulsar spin-down (~0.2%) |
| quadrupole power | $G/5c^5$ | 008 T4 (projector 2/5 exact) | same |
| wave amplitude | $2G/c^4$ | 008 T4 | same |
| four-derivative $a$ | $0$ | P7′ contradiction (E3) | bench-top Yukawa null (54 μm at α=⅓) |
| vector normalization | $16\pi G/c^2$ | parent closure (012) | GPB (~19%), LAGEOS (~few %) |
| κ-leak coefficient | $\tfrac32\Omega_m(H_0r/c)^2$ | F1 | (unobservably small; honesty entry) |
| Λ | **not derived** | — | the vacuum-sector program's problem |

**Zero matched coefficients.** Each anchor above was confronted as a
kill condition after derivation, not used as a fit before it.

## Boundary behavior

Identical to GR (Trial E, resolved): curvature at matter boundaries
transcribes the source profile exactly — jumps for sharp edges, smooth
for smooth profiles — with finite field energy in all cases. The
energy ledger diverges only with compactness ($E_{\rm ext} =
-2GM^2/(R-r_s)$), at the doorstep of the interior cap.
