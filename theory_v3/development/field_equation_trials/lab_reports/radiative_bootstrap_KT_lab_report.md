# Lab Report: Radiative Bootstrap -- K_T Derived (the Last Matched Coefficient)

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/008_radiative_bootstrap/radiative_bootstrap_KT.py`
**Experiment type:** Derivation / coefficient closure (armchair, reduced level)
**Route:** `radiative_bootstrap_route_g03` (registered at G03)
**Status:** SUCCESS -- K_T derived; **zero MATCHED coefficients remain in the reduced theory**
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/008_radiative_bootstrap/radiative_bootstrap_KT.py`
**Run date:** 2026-06-12
**Dependencies verified:** C2 bootstrap selector; G03 TT positivity; P9 adoption record.

## Purpose

After C2/C3/G02/G03, exactly one coefficient in the reduced theory was
MATCHED to GR rather than derived: the radiative normalization (the
far-field amplitude coefficient $2G/c^4$ in
$h_{ij}=(2G/c^4 r)\ddot Q_{ij}$, equivalently the TT kinetic constant
$K_T$). Repeat the C2 move -- the field's own energy gravitates at the
universal coupling, counted once (P9) -- in the radiative sector.

## Results

**T1 (underdetermination lemma).** In the linear TT theory with the
matter coupling fixed kinematically (h is metric strain, P2), the
radiated amplitude scales as $1/K_T$ and the work-flux balance holds
identically for *every* $K_T$ (verified with an explicit harmonic
source). The linear sector's only physical combination is
$(\text{coupling})^2/K_T$. The MATCHED status was structural, not an
omission -- fixing $K_T$ *requires* the self-coupling.

**T2 (static anchor).** The conditional response $N\,G_{ab}=T_{ab}$
(same gates as C3) must reproduce the *derived* static law
$\Delta\phi = 4\pi G\rho$ (from C2+P9+P7', not from GR). Weak-field
$G_{tt}^{(1)} = 2\Delta\phi$ computed from scratch; this forces
$$N = \frac{c^4}{8\pi G}, \qquad\text{corollary: } \Box\bar h_{ab} = -\frac{16\pi G}{c^4}T_{ab}.$$

**T3 (the bootstrap).** Exact Einstein tensor of the TT metric expanded
to second order:

* $O(\epsilon)$: the TT wave equation, with $G_{tt}^{(1)}=0$ -- wave
  energy first appears at second order, exactly where P9 bites.
* $O(\epsilon^2)$ on the null solution: $\langle G_{tt}^{(2)}\rangle =
  -\epsilon^2\omega^2/4$ per linear polarization (period average), and
  $-\epsilon^2\omega^2/2$ *exactly, no averaging* for circular
  polarization; null transport $|G^{(2)}_{tz}| = |G^{(2)}_{tt}|/c$
  confirmed (flux = c x density, as G03 required).
* Bootstrap reading $t_{ab} \equiv -N\,G^{(2)}$: the wave's own energy
  sources the background at the universal coupling -- **P9 realized in
  the radiative sector**, geometry-side, counted once (C3's placement).
  Reading off against the G03 quadratic form:
$$\boxed{\;K_T = \frac{c^4}{16\pi G}\ \text{ per polarization}\;}
\qquad\Longleftrightarrow\qquad
\langle u\rangle = \frac{c^2}{32\pi G}\langle\dot h_{ij}\dot h_{ij}\rangle.$$
  Positivity (G03) reconfirmed with the derived sign.

**T4 (the payoff -- no free constants).** Retarded Green identity,
tensor-virial step (compact 1D witness), and the angular projector
average $\frac{1}{4\pi}\oint \Lambda_{ij,kl}Q_{ij}Q_{kl}\,d\Omega =
\frac{2}{5}Q_{ij}Q_{ij}$ all verified exactly. Assembly:
$$h_{ij}^{TT} = \frac{2G}{c^4 r}\,\ddot Q_{ij}^{TT}(t-r/c)
\qquad\text{(the previously MATCHED $2G/c^4$ -- now derived)},$$
$$P = \frac{G}{5c^5}\,\langle\dddot Q_{ij}\dddot Q_{ij}\rangle.$$

## Verdict

```text
RADIATIVE BOOTSTRAP: SUCCESS (reduced level, conditional).
K_T = c^4/(16 pi G) derived from the static sector's own
normalization + P9 self-sourcing. Quadrupole power closes with
no free constants. ZERO MATCHED COEFFICIENTS REMAIN.
```

**Kill condition confronted, not dodged:** the quadrupole power now has
no adjustable constant. Had the bootstrap produced any other $K_T$, the
predicted binary-pulsar spin-down would differ from GR's by that factor
and be excluded by the Hulse-Taylor agreement (~0.2%). The derived
coefficients reproduce GR's exactly: the anchor PASSES as a genuine
falsification test, not a calibration.

**K_strain constraint exported:** the covariant parent functional must
have quadratic TT expansion with $K_T = c^4/(16\pi G)$ given the static
normalization $N = c^4/(8\pi G)$ -- the relative weight of the shear
and TT sectors of $K_{\text{strain}}$ is no longer a free choice.

## Honesty ledger (open obligations, all coefficient-free)

1. **Closure uniqueness** cited to Deser (1970), not rederived in-house
   (recorded as handoff import with status ASSUMPTION).
2. **Averaging rigor:** short-wave (Isaacson) averaging used at reduced
   level; the circular-polarization cross-check is exact (no averaging)
   and agrees, but secular/gauge questions belong to the covariant lift.
3. **Tensor-virial identity** verified on a compact 1D witness, not in
   generality (it is a standard conservation identity).

None of these carries a number: every coefficient came from the trials'
own static sector plus P9.

## Relation to the program

This is C2's bootstrap completing its second sector. The pattern is now
established twice: *the field's own energy, admitted once at the
universal coupling, fixes the coefficient the linear theory provably
cannot.* G03's obligation `derive_tensor_coupling_g03` is discharged
(SATISFIED record in the trial archive). The recovery ledger now reads:
postulates P1-P6, P7', P9; everything else in the reduced theory --
including both sector couplings -- is derived or theorem-shaped.

## Next steps

1. The covariant $K_{\text{strain}}$ parent, now carrying one more
   derived constraint (relative shear/TT normalization).
2. Trial D2 (excess equation of state) and Trial B2 (physical identity
   of the measure bridge), both feeding the same parent.
3. In-house closure-uniqueness proof (retire the Deser citation).
