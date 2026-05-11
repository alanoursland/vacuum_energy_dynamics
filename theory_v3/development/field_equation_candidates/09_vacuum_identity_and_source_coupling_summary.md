# Vacuum Identity and Source Coupling Summary

## Purpose

This document summarizes the `09_vacuum_identity_and_source_coupling/` development group.

This group marks the transition from treating gravitational sectors as independent "reduced toys" to deriving them from a unified **vacuum-substance ontology**. It seeks to answer how matter density, current, and stress act as different "projections" of a single vacuum-exchange balance law.

The central conclusion is:

> The vacuum-substance picture provides the structural reason for the vector sector ($W_i$) and the exact shape of frame dragging, but the final normalization coefficients remain "reconstruction-incomplete".

---

## The Vacuum-Substance Continuity Identity

The foundation of this group is a candidate ontology-native balance law:

$$\partial_t q_v + \nabla \cdot J_v = \Sigma_{\text{exchange}} + \Sigma_{\text{creation}} - \Gamma_{\text{relax}}$$

* **$q_v$ and $J_v$**: Scalar vacuum-substance density and flow proxies.
* **$\Sigma_{\text{exchange}}$**: Matter density ($\rho$) is interpreted as a scalar exchange term that sources $A_{\text{constraint}}$.
* **$J_v$ (Transport)**: Matter current ($j_i = \rho v_i$) is interpreted as vacuum transport that sources the vector response $W_i$.
* **$\Gamma_{\text{relax}}$**: Encodes the vacuum absorption mechanism that suppresses scalar radiative hazards ($A_{\text{rad}}$).

This identity moves the theory beyond "analogies" to General Relativity and toward a system where source coupling is demanded by mass-continuity bookkeeping.

---

## The Vector Sector ($W_i$) Reconstruction

The group achieves its most significant progress in the vector/current sector, moving through three stages:

### 1. Source Identification via Continuity

If mass density sources the scalar field, then the continuity equation ($\partial_t \rho + \nabla \cdot j = 0$) demands that current $j_i$ sources a vector response. The sector allocation policy is refined via a formal **transverse projector** ($P_T = I - \frac{kk^T}{k^2}$):

* **$j_T$ (Transverse)**: Sources the $W_i$ vector/curl sector.
* **$j_L$ (Longitudinal)**: Allocates to scalar continuity and $A_{\text{constraint}}$.

### 2. The Curl-Energy Field Equation

The theory derives the vector equation form from a gauge-aware **curl-energy action** ($E_W \sim \int | \nabla \times W |^2$):

$$\nabla \times (\nabla \times W) = -\frac{\alpha_W}{2K_c} j_T$$

This operator is "safe" because it ignores pure-gradient gauge-like pieces ($W = \nabla \phi$).

### 3. Structural Recovery of Frame Dragging

By treating global rotation as boundary data fixed by total angular momentum ($J$), the theory recovers the exact far-field shape observed in the Lense-Thirring effect:

* **Ansatz**: $W_\phi \sim \frac{J \sin \theta}{r^2}$.
* **Diagnostic**: $B_W = \nabla \times W \sim \frac{J}{r^3}$.

---

## Normalization and "Coefficient Discipline"

A core theme of Group 09 is the strict prohibition of "hand-matching". The study categorizes the state of all coefficients to maintain theoretical integrity:

| Item | Status | Result |
| --- | --- | --- |
| **Source Objects ($\rho, j_i$)** | **Constrained** | Fixed by mass continuity. |
| **Scalar $A$ Coefficient** | **Derived** | Inherited from the areal-flux normalization. |
| **Vector Action Ratio ($\frac{\alpha_W}{K_c}$)** | **Missing** | The "vacuum stiffness" for vector transport is not yet derived. |
| **Precession Coupling ($\beta_W$)** | **Missing** | The link between the $B_W$ field and gyroscopic motion is symbolic. |
| **Lense-Thirring Match** | **Hand-Assigned** | Forbidden as an input; must remain a future target. |

---

## Status of Source Couplings

The group's audit provides a clear map of what is ontology-native vs. what is still matched:

* **$A_{\text{constraint}}$**: Strongly supported as a scalar exchange projection of mass density.
* **$W_i$**: Structurally supported by current continuity, though normalization is missing.
* **$A_{\text{rad}}$**: Controlled by a relaxation term ($\Gamma_{\text{relax}}$) that represents vacuum absorption.
* **$\kappa$ (Trace/Interior)**: Currently labeled as **Missing**; no source identity yet links it to pressure or stress trace.
* **$h_{ij}^{TT}$ (Tensor)**: Structurally strong but currently **Hand-Assigned** regarding its $2G/c^4$ coupling.

---

## Closing Summary

Group 09 transforms the "reduced sector bundle" into a **Vacuum Response Theory**. It identifies the vacuum-substance balance law as the parent of both static gravity and frame dragging.

While it successfully recovers the **dipole-like shape** ($1/r^3$) of rotational fields, it identifies a major frontier: deriving the **vector stiffness** ($K_c$) from the vacuum ontology rather than fitting it to match General Relativity. The project has mapped the "tunnels" of frame-dragging plumbing, but the "castle" of a fully normalized covariant derivation remains the next objective.

**Next Recommended Target:** `09_vector_sector_status_summary.md` to consolidate the vector line before moving to the $\kappa$ or tensor coupling challenges.