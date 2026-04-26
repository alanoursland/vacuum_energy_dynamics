# Structure Search Higher-Dimensional Results

## What This Document Is

This document reports the second structure-search investigation conducted with VacuumForge, extending the baseline analysis (`structure_search_baseline_results.md`) from 2D mode space to 4D / 3+1-style configuration space.

The baseline established that trace-free exchange in 2D occurs only along the antisymmetric directions $(+1, -1)$ and $(-1, +1)$. Two of eight discrete sign patterns — a result that looked like a fine-tuning condition: trace-free exchange as a single special direction in a small space.

This investigation asks whether that impression survives in higher dimensions. The answer is: partly. The trace-free condition generalizes cleanly as a codimension-1 kernel — one linear constraint regardless of dimension, leaving an $(N-1)$-dimensional subspace of allowed exchange directions. In 2D the kernel is a 1D line, which looks restrictive. In 4D it is a 3D hyperplane, which is less restrictive but still a measure-zero subset of continuous direction space. The wall has been reshaped, not lowered: the framework no longer needs to explain why exchange selects one specific antisymmetric vector, but it still needs to explain why local exchange avoids the trace direction.

The investigation also identifies the physically natural trace-kernel direction in 3+1: the time channel responds oppositely to the average of the spatial channels. This is the higher-dimensional expression of reciprocal scaling, and it reduces under static spherical symmetry to the simple condition $e_t + e_s = 0$.

## Background

The Equal-Response problem asks why the weak-field spatial response equals the temporal response, equivalently $\gamma_v = 1$. In scale-factor form

$$ds^2 = -A(r)^2 c^2 dt^2 + B(r)^2 d\vec{x}^{\,2},$$

Equal-Response is equivalent at first order to the reciprocal-scale condition $A(r)B(r) = 1$. In logarithmic and mode variables — $a = \ln A$, $b = \ln B$, $\kappa = (a+b)/2$, $\sigma = (a-b)/2$ — Equal-Response becomes $\kappa = 0$.

The candidate Exchange-Creation Separation principle says local vacuum exchange should satisfy $J_\kappa = 0$ (trace-free) while vacuum creation can have $J_\kappa \neq 0$ (traceful). The baseline structure search sharpened this into a kernel condition: exchange must lie in the kernel of the trace projection $\mathcal{T}$ from configuration space to mode space.

The 2D baseline found that this kernel is a 1-dimensional subspace of a 2-dimensional space. The interpretive concern was that 2D might be small enough to overstate the constraint. This investigation tests that concern by extending to 4 variables.

## Methodology

Three scripts were run, each testing a different aspect of the higher-dimensional structure:

`e4a.py` enumerates all 80 nonzero sign patterns in $\{-1, 0, +1\}^4$ with direct projection $a = q_1$, $b = q_2$. The trace vector is $[1, 1, 0, 0]$ and the kernel condition is $\delta_1 + \delta_2 = 0$.

`e4b.py` analyzes the trace-kernel geometry in two cases. First, the general linear 4D family with symbolic projection coefficients, to extract the symbolic form of the trace-free condition. Second, a physical 3+1 projection $a = q_t$, $b = (q_x + q_y + q_z)/3$ representing time-channel and average-spatial-channel scales, with specific exchange directions tested.

`e4c.py` verifies leak detection in 4D across four cases: a tautological control (mode-basis projection with trace-free baked in), a genuine derived case (antisymmetric exchange with non-trivial projection), a null-operator case (exchange acting only on variables outside the projection), and the physical 3+1 kernel direction.

The trace projection used throughout is the Jacobian sum row: for projection $(a, b) = (f_a(\mathbf{q}), f_b(\mathbf{q}))$, the trace vector is $[\partial a/\partial q_i + \partial b/\partial q_i]$, and the trace-free condition is $J_\kappa = \sum_i s_i \, \delta q_i = 0$ where $s_i$ is the trace vector's $i$-th component.

## Results

### Sign-Pattern Enumeration

With direct projection $a = q_1$, $b = q_2$ (trace vector $[1, 1, 0, 0]$):
```
Total patterns tested: 80
Trace-free derived:  18  (22.5%)
Failed:              62
Tautological:         0
```
All 18 derived patterns satisfy $s_1 + s_2 = 0$ with the antisymmetric pair $(s_1, s_2) \in \{(+1,-1), (-1,+1)\}$ in the trace-coupled channels. The remaining two internal signs $(s_3, s_4)$ are free, giving $2 \times 3^2 = 18$ patterns.

A subtlety appears at this scale that did not arise in 2D. Eight patterns of the form $(0, 0, s_3, s_4)$ with $(s_3, s_4) \neq (0, 0)$ satisfy $s_1 + s_2 = 0$ but produce $J_a = J_b = 0$. These are *internal-only* patterns: the exchange acts on configuration variables $q_3$ and $q_4$ that don't appear in the projection, so it produces no metric response. The analyzer correctly classifies these as "failed" with classification "zero" rather than as derived trace-free exchange. An exchange invisible to the metric is not meaningfully trace-free metric exchange.

This means the structural condition is more precisely:

$$s_1 + s_2 = 0 \quad \text{and} \quad (s_1, s_2) \neq (0, 0).$$

The first clause is necessary for trace-freeness; the second clause is required for the exchange to produce any metric response at all. Both writeup-level sign-pattern fractions in this report should be read with this distinction in mind.

### General Linear 4D Family

The general linear 4D projection has $a = \sum_i \alpha_i q_i$ and $b = \sum_i \beta_i q_i$ with arbitrary symbolic coefficients. The exchange operator has direction coefficients $e_i$. The induced trace source is

$$J_\kappa = S \sum_{i=1}^{4} (\alpha_i + \beta_i) e_i.$$

The analyzer classifies this family as conditional. Trace-free exchange requires the single linear equation

$$\sum_{i=1}^{4} (\alpha_i + \beta_i) e_i = 0.$$

This is the central structural result: the trace-free condition is one linear equation regardless of the number of pre-mode variables. The kernel dimension is always $N - 1$. The codimension is always 1.

| Dimension | Kernel dim | Codimension |
|-----------|-----------|-------------|
| $N = 2$ | 1 | 1 |
| $N = 4$ | 3 | 1 |
| $N$ | $N - 1$ | 1 |

### Physical 3+1 Projection

With projection $a = q_t$, $b = (q_x + q_y + q_z)/3$, the Jacobian is

$$J = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1/3 & 1/3 & 1/3 \end{bmatrix}$$

and the trace vector is $[1, 1/3, 1/3, 1/3]$. The trace-kernel condition is

$$e_t + \frac{e_x + e_y + e_z}{3} = 0.$$

Three free spatial parameters determine the time component. Four directions were tested:

| Direction | $\delta\mathbf{q}$ | $J_\kappa$ | Status |
|-----------|-------|-----------|--------|
| Antisymmetric t-x | $(S, -S, 0, 0)$ | $2S/3$ | failed |
| Isotropic spatial | $(-S, S, S, S)$ | $0$ | derived |
| Pure spatial shear | $(0, S, -S, 0)$ | $0$ | failed (zero) |
| Non-kernel | $(S, S, 0, 0)$ | $4S/3$ | failed |

The antisymmetric t-x direction — which was trace-free in 2D — fails in 3+1 because the trace vector is no longer $[1, 1, 0, 0]$ but $[1, 1/3, 1/3, 1/3]$. The simple antisymmetric pattern doesn't transfer between projections.

The isotropic spatial direction $(-S, S, S, S)$ satisfies the kernel: $-1 + (1+1+1)/3 = 0$. This is the physically natural 3+1 trace-kernel direction: the time channel contracts while all three spatial channels expand equally (or vice versa), preserving the average of $a + b$.

The pure spatial shear $(0, S, -S, 0)$ satisfies the kernel condition $0 + (1 - 1 + 0)/3 = 0$ but produces $J_a = 0$ and $J_b = (S - S)/3 = 0$, hence $J_\sigma = 0$. It redistributes within spatial channels without affecting the two-mode metric decomposition. This reveals a subtlety not present in 2D: the trace kernel can contain directions invisible to the $(a, b)$ projection. The analyzer classifies these as zero-response failures, which is the correct default for the Equal-Response question but is worth flagging because such directions might still be physically meaningful in other contexts (gravitational wave polarization, anisotropic sources).

### Leak Detection

All four leak detection tests pass in 4D:

| Test | Expected | Got |
|------|----------|-----|
| Mode basis (tautological control) | tautological | tautological |
| Genuine antisymmetric | derived | derived |
| Null operator (zero metric response) | failed | failed |
| Physical 3+1 kernel | derived | derived |

The third test is the new case that arises only in higher dimensions: an operator that zeroes the trace-contributing variables and acts only on non-contributing variables. The analyzer correctly classifies this as zero-response (failed) rather than as tautologically trace-free (which would have triggered a leak warning). This is the right default — a metrically invisible operator is not evidence for trace-free exchange — though it does suggest a tooling improvement (see below).

The physical 3+1 kernel direction $(-S, S, S, S)$ produced $J_\kappa = 0$ and $J_\sigma = -2S$, with creation $(C, C, C, C)$ producing $J_\kappa = 2C$. Exchange is trace-free and shear-active; creation is traceful. This is the cleanest physical demonstration of the structure search's central distinction in the dimensionally correct setting.

## Interpretation

### The codimension-1 result reshapes the wall

The trace-free condition is always one linear equation. The kernel is $(N-1)$-dimensional out of $N$. In 2D this is 1 out of 2, which looks like fine-tuning. In 4D this is 3 out of 4, which looks more permissive. The constraint is the same in both cases: avoid one specific direction. The 2D presentation made the constraint look directional ("pick this special vector") when it is actually conservational ("preserve this single quantity").

The framework's question therefore reshapes from "why does local exchange take a specific direction" to "why does local exchange preserve the trace $a + b$." The latter is structurally simpler — it is a single conservation law, the kind of thing physics often derives from a symmetry, an identity, or a structural constraint. The conditional chain to Equal-Response is now:
```
trace conservation (single conservation law)
→ J_κ = 0
→ κ = 0 at energy minimum
→ AB = 1
→ γ_v = 1
```
The first step remains the open wall. What the 3+1 investigation has changed is the wall's shape:

- **Before:** Why does local exchange pick a specific direction?
- **After:** Why does local exchange preserve a single conservation law?

The new shape is more amenable to physics-style derivation — conservation laws have natural origins in symmetries, identities, and structural constraints — but the wall itself is the same height. A structural commitment is still required to put exchange in the trace kernel. The framework's three options remain:

1. Derive trace conservation from existing postulates under a strengthened interpretation.
2. Derive trace conservation from a fuller mathematical structure of the vacuum.
3. Adopt trace conservation as a new structural postulate.

Option 1 has a more concrete target now: derive $e_t + e_s = 0$ under static spherical symmetry from existing postulates. Options 2 and 3 remain available as fallbacks.

## Next Investigation

**Symmetry-reduced static spherical 3+1 search.** Impose isotropy $e_x = e_y = e_z = e_s$ on the physical 3+1 projection. The trace-kernel condition collapses to $e_t + e_s = 0$. Test whether candidate structural assumptions naturally force this relation:

1. *Isotropic exchange:* spatial components respond equally.
2. *Conformal-content conservation:* exchange preserves the trace/conformal content of the local causal cell.
3. *Volume-neutral local exchange:* local exchange redistributes vacuum shape without changing net trace content.
4. *Creation-exchange separation:* creation sources trace; exchange preserves trace.
5. *Configuration-energy minimization:* trace excitation carries positive energy and is unsourced under exchange.

Each candidate is a structural assumption that, if it implied $e_t + e_s = 0$, would close Equal-Response. The search should encode each assumption and test whether it forces the trace-kernel condition under symmetry.

**Anisotropic spatial mode tracking.** The pure spatial shear $(0, S, -S, 0)$ is invisible to the averaged-spatial $(a, b)$ projection. This is fine for Equal-Response, but the framework's gravitational-wave mode question needs the spatial sector decomposed into average spatial scale, trace-free spatial shear, and possibly tensor polarization modes. A future analyzer extension should support this decomposition and connect the Equal-Response program to the wave-modes branch.

## Reproduction

In `vacuum_energy_dynamics/vacuum_forge/src`:
```
python src/scripts/e4a.py    # 4D sign-pattern enumeration
python src/scripts/e4b.py    # Trace-kernel geometry analysis
python src/scripts/e4c.py    # 4D leak detection verification
```
