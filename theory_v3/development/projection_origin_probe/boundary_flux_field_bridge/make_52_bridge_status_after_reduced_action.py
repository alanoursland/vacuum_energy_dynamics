#!/usr/bin/env python3
"""
make_52_bridge_status_after_reduced_action.py

Generate a status report after proofs 46-51.

Output:
    52_bridge_status_after_reduced_action.md
"""

from pathlib import Path


md = """# Boundary Flux Field Bridge: Status After Proofs 46-51

## Main Update

Proof `46` resolves the scalar sign bookkeeping at the level of the
source-coupled reduced action.

The positive stored strain cross term is:

```text
E_strain,cross = +Q1*Q2/(4*pi*d).
```

By itself, this is repulsive for same-sign positive sources.

But the stationary source-coupled action:

```text
E[u] = 1/2 <u,Au> - <J,u>
```

reduces to:

```text
E_red[J] = -1/2 <J,A^-1J>.
```

For two sources, the separation-dependent reduced interaction is:

```text
E_red,cross = -Q1*Q2/(4*pi*d).
```

This gives attractive same-sign separation force under the convention:

```text
F_d = -dE/dd.
```

## What This Means

The earlier sign problem was partly a bookkeeping problem:

```text
stored strain energy != effective reduced interaction energy.
```

The scalar boundary-flux bridge can produce attractive same-sign interaction if
the physical interaction is read from the source-coupled reduced action.

## What Still Needs To Be Justified

The proof does not by itself prove that nature uses this scalar action. It
proves a conditional:

```text
if the vacuum field is eliminated from a positive quadratic source-coupled
action, then same-sign positive sources have negative reduced interaction.
```

The remaining physical question is:

```text
why the reduced source-coupled action is the correct physical bookkeeping for
mass interaction.
```

## Other Results In This Batch

Proof `47` shows:

```text
compact spherical bulk source
```

and:

```text
enclosing boundary flux
```

are equivalent for the exterior field.

Proof `48` packages the bridge as a radial Gauss-law theorem:

```text
Q'(r) = -4*pi*r^2 Delta u.
```

Proof `49` shows inverse-square field strength is specifically the
three-dimensional member of the `n`-dimensional flux family:

```text
|u'| proportional to r^(1-n).
```

Proof `50` shows a screened exterior equation gives Yukawa behavior and fails
to preserve exact long-range inverse-square scaling unless the screening mass
vanishes.

Proof `51` classifies nonlinear scalar strain corrections:

```text
Phi_p(z)=1/2 z + alpha/(2p) z^p
```

predicts:

```text
u(r)=Q/(4*pi*r)
     - alpha (Q/(4*pi))^(2p-1)/[(4p-3)r^(4p-3)]
     + O(alpha^2).
```

## Current Bridge Status

The scalar bridge now has:

```text
1. boundary flux source strength;
2. source-free exterior Laplace equation;
3. finite-sphere monopole stability;
4. bulk-source / boundary-flux equivalence;
5. Gauss-law form;
6. 3D inverse-square dependence;
7. attractive same-sign reduced interaction under source-coupled action;
8. nonlinear correction classifier.
```

## Next Proof Targets

The next useful targets are:

```text
1. induced multipoles for fixed-potential spheres;
2. exact two-sphere capacitance/interaction expansion;
3. source-coupled action with boundary integrals rather than point sources;
4. deriving the reduced action sign from a minimum-burden principle;
5. identifying the first geometry/tensor lift candidate.
```

The bridge has become a controlled scalar weak-field model. The next hard step
is no longer inverse-square scaling; it is deriving the action/source
bookkeeping from the proposed vacuum ontology.
"""

out = Path(__file__).with_name("52_bridge_status_after_reduced_action.md")
out.write_text(md, encoding="utf-8")

print(f"Wrote {out.resolve()}")
