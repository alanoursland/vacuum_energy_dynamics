# Lab Report: Gates G03 and G02 -- Sector Signature Completed

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/006_gate_G03_radiative_positivity/gate_G03_radiative_positivity.py`
**Experiment type:** Gate derivation (armchair, reduced level)
**Gates:** G03 (gravitational-wave energy sign), G02 (flat-vacuum stability)
**Status:** BOTH GATES PASS; sector-indefinite signature theorem-shaped
**Run environment:** `cd vacuum_forge/src; PYTHONPATH=. ; python field_equation_trials/006_gate_G03_radiative_positivity/gate_G03_radiative_positivity.py`
**Run date:** 2026-06-11
**Dependencies verified:** C2 negative-energy derivation; P9 and P7' adoption records (first use of the postulate archive objects).

## Purpose

Complete the sector-indefinite signature. C2/C3 + P9 + P7' fixed the static
temporal sector NEGATIVE. Observed gravitational radiation carries positive
energy. Owed: proof that the propagating sector is positive and that the
negative sector can neither propagate nor be mined.

## Results

**T1 (G03).** The reduced TT action's energy density is a sum of squares,
$T^{00}=\tfrac{K_T}{2}[h_t^2/c^2+h_z^2]$ per polarization -- positive
definite for $K_T>0$. For outgoing waves $h=F(z-ct)$ the flux is
$c^3K_TF'^2>0$ outward, with density = flux/c (null transport). The binary
pulsar's spin-down anchors $\mathrm{sign}(K_T)=+$ (observational anchor,
not a fit). The charter's quadrupole power $P\sim(G/c^5)\langle\dddot
Q^2\rangle$ is manifestly a square.

**T2 (ghost exclusion).** Promoting the negative-energy temporal sector to
a propagating (hyperbolic) mode gives a Hamiltonian density that is
negative definite with $H[\lambda s]=\lambda^2H[s]\to-\infty$: a ghost,
draining without bound into the positive TT sector. EXCLUDED by stability.
Consequence: the elliptic/constraint assignment of the scalar sector --
the old FEC-007 "A is constraint, not radiation" *policy* -- is now a
*theorem* (reduced level, conditional on the C2 sign).

**T3 (G02).** The source-free constraint sector $(r^2A')'=0$ with
asymptotic flatness and regularity at the origin has the unique solution
$A\equiv1$: flat vacuum is the unique zero-source static state. The
negative sector is therefore source-slaved -- a functional of the sources,
not an independent reservoir. Nothing to decay into; mining it requires
moving sources (P6 dynamics), radiated through the positive channel.

## Verdict

```text
G03 PASS: everything that propagates is positive; sign anchored.
G02 PASS: flat vacuum unique at zero source; no runaway.

Sector-indefinite signature, complete (reduced level):
  temporal sector: negative, non-propagating (forced), source-slaved
  radiative sector: positive definite, outward flux
```

This is the architecture by which GR survives its conformal-factor
problem (wrong-sign conformal mode caged by the Hamiltonian constraint;
TT positive). The framework reproduces the stable arrangement from its
own adopted laws -- and, via T2, can now say WHY the scalar sector had to
be a constraint: the alternative is a ghost.

## Open obligations

- Covariant lift of T1-T3; nonlinear stability.
- $K_T$ magnitude (still MATCHED to $2G/c^4$): the radiative-bootstrap
  route is registered -- derive the tensor coupling from the same
  self-consistency that fixed the temporal sector.

## Relation to the program

With G02/G03 closed, the P4 sign fork that opened this session's theory
work is fully resolved at the reduced level: sector-indefinite, with each
sign derived or anchored, and stability proven rather than hoped. The
remaining sign-related work is covariant, not conceptual.
