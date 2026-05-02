"""
candidate_p3_volume_preservation_test.py

Move 1 experiment: Does P3 (constant local vacuum energy density) force local
exchange operators to preserve volume on configuration space?

Background:
-----------
The structure search baseline established that volume-preserving exchange
operators automatically lie in the trace kernel of the projection map, which
gives J_kappa = 0 and therefore reciprocal scaling AB = 1 in the static
spherical exterior, which gives gamma_v = 1.

The remaining link to be tested: does P3 (vacuum energy density is finite and
locally constant) force exchange operators to preserve volume? If yes, the
trace-kernel constraint is a derived consequence of P3 rather than a separate
postulate, and the equal-response problem is closed at the postulate level.

Hypothesis:
-----------
P3 says rho_v (energy per unit vacuum volume) is locally constant. If exchange
between matter and vacuum changes the configuration but does not change the
local density, then the local volume of vacuum exchanged must equal the local
volume of vacuum displaced. This is volume preservation as a consequence of
density constancy.

Failure mode to test:
---------------------
A non-volume-preserving exchange would produce different vacuum volumes on
each side of the exchange while density stays constant. Total vacuum energy
would not balance unless density itself changed, contradicting P3.

So the test is: is there an exchange operator that violates volume preservation
while still satisfying P3's density constancy? If such an operator exists in
the space of allowed structures, P3 alone does not force volume preservation.
If no such operator exists, P3 forces volume preservation.

Method:
-------
1. Define a configuration space with explicit volume form.
2. Define candidate exchange operators parameterized by direction.
3. For each operator, compute:
   a. Whether it preserves the volume form (Jacobian determinant = 1 to leading
      order in the exchange amplitude).
   b. Whether it preserves local energy density (rho_v constant before and
      after exchange).
4. Identify operators that satisfy (b) without satisfying (a). If any exist,
   P3 does not force volume preservation. If none exist, P3 forces it.
"""

import sympy as sp
from sympy import symbols, Matrix, simplify, det, eye, Symbol

# I'M GUESSING AT THE FORGE API HERE. Real imports might look like:
# from vacuumforge import TheoryContext
# from vacuumforge.structure_search import StructureSearch, StructureFamily
# from vacuumforge.modes import StandardModes
# from vacuumforge.requirements import LeakDetector
#
# I'll write the experiment in pure SymPy first, then note where forge
# integration would replace ad-hoc symbolic manipulation.


# ---------------------------------------------------------------------------
# Setup: configuration space and projection
# ---------------------------------------------------------------------------

# Pre-mode configuration variables for static spherical 3+1
# q_t: time channel scale
# q_r: radial channel scale
# q_theta, q_phi: angular channel scales (held isotropic for spherical symmetry)

q_t, q_r, q_theta, q_phi = symbols('q_t q_r q_theta q_phi', real=True)
S = Symbol('S', positive=True)  # exchange amplitude

# Projection to mode variables a = ln A, b = ln B
# Standard 3+1 projection: a = q_t, b = (q_r + q_theta + q_phi) / 3
# For static spherical symmetry, set q_theta = q_phi = q_r (isotropic spatial)

# Volume form on configuration space:
# dV = dq_t ∧ dq_r ∧ dq_theta ∧ dq_phi
# An exchange operator δq is volume-preserving to first order in S if
# div(δq) = 0, equivalently the Jacobian determinant of the flow is 1
# to first order.


# ---------------------------------------------------------------------------
# Exchange operator family
# ---------------------------------------------------------------------------

# General linear exchange operator: each component is a linear function
# of the configuration variables, parameterized by coefficients.

# For simplicity, start with constant-direction exchange:
# δq_i = e_i * S  (constant direction in configuration space)

e_t, e_r, e_theta, e_phi = symbols('e_t e_r e_theta e_phi', real=True)

exchange_direction = Matrix([e_t, e_r, e_theta, e_phi])


# ---------------------------------------------------------------------------
# Volume preservation test
# ---------------------------------------------------------------------------

def is_volume_preserving(direction):
    """
    For a constant-direction exchange δq = e*S, the flow is x -> x + e*S.
    The Jacobian is the identity matrix (since direction doesn't depend on q),
    so determinant is 1 trivially. This is the wrong test.

    The correct test for volume preservation under a general field δq(q) is
    that the divergence of the field vanishes:
        div(δq) = ∂(δq_t)/∂q_t + ∂(δq_r)/∂q_r + ... = 0

    For constant direction, divergence is zero trivially (each ∂ = 0).
    To make the test meaningful, we need to consider direction fields that
    depend on q.
    """
    # For now, return tautological pass for constant direction.
    # See discussion below for what a proper test would look like.
    return True


# ---------------------------------------------------------------------------
# Density preservation test
# ---------------------------------------------------------------------------

def preserves_density(direction):
    """
    P3 says rho_v is locally constant. An exchange operator preserves rho_v
    if the local energy density is unchanged before and after exchange.

    But here's the issue: rho_v is energy per unit vacuum volume. If exchange
    changes the amount of vacuum in a region, does it also change the energy
    in that region in lockstep?

    P1 says vacuum is energy. So vacuum amount and vacuum energy are the same
    quantity. Exchanging vacuum at constant rho_v means exchanging some amount
    of vacuum (= some amount of energy) at the local density rate.

    For the exchange to preserve rho_v, the energy added to the region must
    equal rho_v times the volume added. Equivalently: the amount of vacuum
    energy exchanged equals rho_v times the amount of vacuum volume exchanged.

    This is automatically true *if* exchange preserves the rho_v identity.
    It is automatically false otherwise.

    So this test is not informative as stated. The question reduces to:
    is there a notion of "exchange" that doesn't preserve rho_v?
    """
    # Same problem: this is tautological as stated.
    return True


# ---------------------------------------------------------------------------
# WHERE I'M STUCK
# ---------------------------------------------------------------------------

# Writing this script has revealed that "P3 forces volume preservation" might
# not be the right framing of the question.
#
# P3 says rho_v is constant. P1 says vacuum is energy. Together, these imply
# that vacuum energy = rho_v * vacuum volume, and rho_v is a fixed constant.
#
# So "exchange of vacuum" is automatically "exchange of energy at fixed
# density rate," which means exchanging volume of vacuum equals exchanging
# energy. There is no degree of freedom for "exchange that doesn't preserve
# volume" because volume IS the energy under P1+P3.
#
# This makes "volume preservation under P3" tautological in a way I didn't
# see when I proposed Move 1. P3+P1 don't force volume preservation as a
# separate condition; they identify volume with energy, making volume
# preservation automatic for any exchange that conserves energy.
#
# So the real question moves up a level: what does "local exchange" actually
# mean, and what does it conserve?
#
# If exchange means "matter ↔ vacuum redistribution at constant local energy
# density," then by P1+P3, it preserves volume by construction. The
# trace-kernel constraint then follows from the volume-trace-kernel link
# the structure search already established.
#
# But this argument has a hidden step: the assumption that local exchange
# is local energy redistribution. Is that an additional commitment, or is
# it forced by something in P1-P5?
#
# I think it's forced by P5's minimum-energy-seeking interpretation:
# exchange that doesn't conserve local energy would either inject or extract
# energy, which in the framework's ontology means creating or destroying
# vacuum substance — which is creation/destruction, not exchange.


# ---------------------------------------------------------------------------
# Reformulated test
# ---------------------------------------------------------------------------

# The test that's actually meaningful: separate "exchange" (no net energy
# change) from "creation" (net energy change), and check whether exchange
# defined this way automatically satisfies the trace-kernel constraint.
#
# Exchange: δ(rho_v * V) = 0  where V is local vacuum volume
# Since rho_v is constant by P3: δV = 0
# This is volume preservation by definition.
#
# Then by the structure search baseline, volume preservation forces the
# direction to lie in the trace kernel: e_t + (e_r + e_theta + e_phi)/3 = 0
# under the standard 3+1 projection.
#
# So the trace-kernel constraint follows from:
#   - Definition: exchange = no net local energy change
#   - P3: rho_v constant
#   - Algebraic result: volume preservation → trace-kernel direction
#
# The wall is now: why is "no net local energy change" the right definition
# of exchange? Why couldn't local matter-vacuum interaction involve net
# energy change in a region (i.e., creation or destruction at the location
# of the matter)?
#
# This is the actual remaining gap. P5's minimum-energy-seeking can be
# interpreted to forbid local energy injection in static configurations,
# but P5 as written doesn't directly say this.


# ---------------------------------------------------------------------------
# Diagnostic output
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("Move 1 experiment: P3 → volume preservation → trace-kernel?")
    print("=" * 70)
    print()
    print("Result: The question reformulates rather than resolves.")
    print()
    print("P1 (vacuum is energy) + P3 (rho_v constant) together imply that")
    print("vacuum volume and vacuum energy are the same quantity, related by")
    print("the constant rho_v. So 'exchange that preserves volume' and")
    print("'exchange that preserves local energy' are the same thing.")
    print()
    print("The trace-kernel constraint follows IF exchange is defined as")
    print("'no net local energy change.' But this definition is not forced")
    print("by P1-P5 as currently stated. It would require a strengthened")
    print("interpretation of P5 (or a new postulate) saying that local")
    print("matter-vacuum interaction in static configurations cannot inject")
    print("or extract net energy at the matter's location.")
    print()
    print("So Move 1 does NOT close the equal-response gap from P3 alone.")
    print("It identifies that the gap is in the definition of 'exchange'")
    print("vs 'creation,' which P1-P5 currently does not pin down.")
    print()
    print("Suggested next move: examine whether 'exchange = no local net")
    print("energy change' follows from P5 under any natural strengthening,")
    print("or whether it must be adopted as a separate postulate.")
