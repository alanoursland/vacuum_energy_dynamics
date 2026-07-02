# The Gravitational Response

**Claim (licensed by P10).** The vacuum's gravitational response is
Einstein–Hilbert *because* the ground state is frustrated. The
expansion-point theorem is the selector the strain-functional program
sought; the sector architecture of the closed theory is the packing's
own mode structure; and the higher-derivative corrections the packing
generically produces are Planck-suppressed and quarantined.

## 1. The Expansion-Point Theorem

Expand the wedge energy about the frustrated ground state
$\delta_h = \Delta_0$ (derivation 039):

$$E \;=\; \underbrace{\sum_h V_h\, f(\Delta_0)}_{\text{floor: substance,
sequestered}}
\;+\; \underbrace{f'(\Delta_0)\sum_h V_h(\delta_h - \Delta_0)}_{\text{Regge
action}\;\to\;\text{Einstein--Hilbert}}
\;+\; \underbrace{\tfrac12 f''(\Delta_0)\sum_h V_h(\delta_h-\Delta_0)^2}_{
R^2\text{-class},\; a^2K\text{-suppressed}}.$$

The linear term is generic **because the expansion point is
frustrated**: at nonzero deficit, $f'(\Delta_0) \neq 0$ for generic
smooth $f$. An unfrustrated packing would sit at its energy minimum
$\delta = 0$, where $f'(0) = 0$ *necessarily* — its leading response
would be curvature-squared.

> **Geometric frustration is why gravity is Einstein–Hilbert.**

The physical body of the theorem: a pre-strained cell is a loaded
spring, and loaded springs respond at first order (force ∝ preload).
Newton's constant is the preload — $G^{-1} \propto f'(\Delta_0)$, the
floor–Newton lock. *Things fall because space is pre-tensioned.*

## 2. The Linear Term Is Einstein–Hilbert, Exactly in the Limit

The Regge action's convergence to $\tfrac12\int R\sqrt{g}$ is closed at
the standard of the rest of the program (derivations 039, 040, 043):

- **2D is exact at every refinement**: $\sum_v \delta_v = 2\pi\chi$
  combinatorially, and the local encoding has exact relative error
  $\tfrac18 s^2$.
- **3D, complete regular family** (the only three that exist):
  5-cell 0.6916 → 16-cell 0.7791 → 600-cell 0.9648, quadratic rate,
  coefficient stabilizing at ~0.089.
- **4D, complete regular family** (the only two): 0.3065 → 0.4434,
  matching rate coefficients (0.221, 0.226). Hinges are triangles;
  the regular 4-simplex dihedral is $\arccos\tfrac14$; every integer
  coordination is frustrated in 4D, so the theorem lifts.
- Arbitrary triangulations: Cheeger–Müller–Schrader 1984, declared
  import, Fierz–Pauli class.

## 3. The Sector Architecture, Bottom-Up

The closed theory's sector signature — trace mode constrained and
non-dynamical, shear mode carrying the gravitating energy, TT modes the
only propagating ones — was derived top-down in `04_field_equations/`
(Theorems 2–4, P7′, G02/G03). The packing reproduces it bottom-up:

```text
volume/trace mode   dihedrals exactly dilation-invariant => zero
                    restoring force => must be constrained => P3
                    (unimodular). Exact (038); measured (041).
shear mode          first-order angle sensitivity; quadratic energy
                    about equilibrium (the discrete stationarity).
                    Exact (038); measured (041).
gauge directions    vertex displacements (K3's relabelings) are exact
                    zero modes; Schlafli closes the Regge variation
                    (discrete Bianchi). Exact (042, 043).
propagating modes   massless spin-2, TT only (Rocek-Williams 1981,
                    declared import; gauge structure in-house).
boundary            Hartle-Sorkin hinge term, exactly additive under
                    gluing -- the defining GHY property (042).
```

Top-down and bottom-up meet at the same architecture. This convergence
— structure derived in June for field-equation reasons, reproduced in
July by the microphysics — is the strongest single piece of P10's
adoption evidence.

## 4. What the Packing Adds Beyond GR's Response

At observable scales: **nothing** — by design and by theorem. The
corrections are:

- the $R^2$-class quadratic term, suppressed by $a^2 K$
  (Planck-suppressed for Planck packing). Its coexistence with exact
  P7′ is the recorded tension O-P10-3: either the $f''$ contribution
  cancels/routes into the constraint sector, or P7′ is the $a \to 0$
  idealization of an observationally inert scalaron. No closed
  coefficient moves either way; the P7′ null test (no Yukawa at any
  range) remains the standing discriminator.
- $O(s^2)$ discretization corrections to the EH coefficient — absorbed
  into the Newton anchor at any fixed packing scale.

The honest summary stands as it did in the README: the closed sector
predicts no accessible deviation from GR. What P10 changes is not the
predictions of the metric response but their *explanation* — and it
relocates the novelty budget to the substance and excursion ledgers.

## Verification Pointers

```text
039  expansion-point theorem; floor-Newton lock (regge_delaunay_bridge)
040  convergence, complete 3D family, rates     (regge_refinement_convergence)
042  Schlafli, Hartle-Sorkin                    (discrete_conservation_boundary)
043  4D lift, Wick foundation, gauge modes      (lorentzian_4d_lift)
038, 041  sector signature, exact + measured
```
