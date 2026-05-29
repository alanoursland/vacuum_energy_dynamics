#!/usr/bin/env python3
"""
make_102_eh_origin_initial_status.py

Generate the initial status report for the Einstein-Hilbert origin tests.

Output:
    102_eh_origin_initial_status.md
"""

from pathlib import Path


md = """# Einstein-Hilbert Origin Tests: Initial Status

## Purpose

This folder tests whether the Einstein-Hilbert / Gamma-Gamma action is the
nonlinear geometric completion of the scalar boundary-flux and linearized
Fierz-Pauli bridge.

This is not an attempt to derive GR from nothing. It is an origin test:

```text
Does the standard nonlinear geometric action contain the structures already
proved in the scalar and linearized folders?
```

## What This First Batch Proved

Proof `98` validated the Levi-Civita connection identities:

```text
Gamma^a_bc = Gamma^a_cb
nabla_c g_ab = 0
Gamma^a_ac = partial_c log(sqrt(g)).
```

Proof `99` validated a controlled nonlinear EH split:

```text
sqrt(g)R
  =
  sqrt(g)g^ab(
    Gamma^c_ad Gamma^d_bc
    - Gamma^c_ab Gamma^d_cd
  )
  + partial_c V^c.
```

This is the first nonlinear connection-strain bridge.

Proof `100` showed that the nonlinear Christoffel and Ricci definitions
linearize to the expressions used in `geometric_field_lift`.

Proof `101` showed that the Einstein-Hilbert field equation recovers:

```text
Delta Phi = 4*pi*G rho
```

and the boundary mass flux:

```text
M = (1/(4*pi*G)) integral partial_n Phi dA.
```

## Current Interpretation

The Einstein-Hilbert action passes the first consistency tests:

```text
nonlinear metric connection
  -> Gamma-Gamma quadratic strain plus boundary term
  -> linearized Ricci/Fierz-Pauli layer
  -> Newtonian scalar boundary-flux sector.
```

## What Is Not Yet Proven

This batch does not prove:

```text
the full EH variation;
the GHY boundary variation;
that EH is uniquely selected by the vacuum ontology;
that the original projection ladder forces EH;
that no additional nonlinear vacuum terms are allowed.
```

## Next Proof Targets

The next useful scripts should test:

```text
make_103_palatini_variation_identity.py
104_ghy_boundary_term_variation_toy_model.py
105_eh_linearizes_to_fierz_pauli_action.py
106_adm_or_komar_mass_boundary_flux.py
107_lovelock_uniqueness_gate_summary.py
```

The next hard question is not whether EH has the right weak-field limit. It
does. The next hard question is whether the vacuum-energy ontology selects the
Einstein-Hilbert action rather than another diffeomorphism-invariant nonlinear
completion.
"""

out = Path(__file__).with_name("102_eh_origin_initial_status.md")
out.write_text(md, encoding="utf-8")

print(f"Wrote {out.resolve()}")
