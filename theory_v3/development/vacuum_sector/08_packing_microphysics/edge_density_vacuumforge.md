# The Edge Density c_e (O-P10-1, partial) -- VacuumForge Record

## Status

```text
result type:   microphysics-constant derivation (2026-07-02,
               derivation 052)
conclusion:    c_e = 36 arccos(1/3)/(sqrt(2) pi) = 9.974276 edges
               per a^3 -- EXACT, pure geometry of the flat
               near-regular ground packing. O-P10-1 reduces to one
               unknown: the packing scale a.
fence:         mean-field near-regular (the 050 class); the exact
               values are claims about the energy-relaxed packing --
               phase 3 (periodic_energy_relaxation_051) tests them.
               NO value of a is proposed.
verification:  vacuum_forge/src/vacuum_sector/052_edge_density/
```

## The Derivation

```text
1. THE 3D GROUND MIXTURE (050's logic, one dimension down).
   delta(5) = +7.36 deg, delta(6) = -63.17 deg: a flat ground state
   must mix, and zero mean deficit fixes
       x_6 = 2 pi/arccos(1/3) - 5 = 0.104299
   with mean edge coordination
       n_bar = 2 pi/arccos(1/3) = 5.104299
   (the hinge identity: independent of WHICH coordinations mix).

2. THE EDGE DENSITY. 6 edges per near-regular tetrahedron (edge a),
   each shared by n_bar cells, cell volume sqrt(2) a^3/12:
       c_e = 6/(V_tet n_bar) = 36 arccos(1/3)/(sqrt(2) pi)
           = 9.974276 per a^3.
   A function of arccos(1/3) alone -- the same sole input as
   Delta_0, the relief function (037), and the mixtures (050, here).

3. BULK CROSS-CHECK (seeded, smoothed 3D Delaunay, N = 600):
   mean interior edge coordination 5.2158 vs predicted
   5.1043 (within 10%); edge density 11.7361 vs predicted
   9.9743 (tens-of-percent level on the PROXY complex -- the
   smoothed random complex is not the ground packing; direction and
   window are the meaningful signals pre-phase-3).

4. THE REDUCTION. rho_v = (c_e Delta_0/2) f'(Delta_0)/a^3
            = 0.640290 f'(Delta_0)/a^3.
   c_e: derived here. f'(Delta_0): eliminated by the floor-Newton
   lock (039). Remaining free microphysics constant: a, alone.
```

## What Sharpens

Register C4 (the discreteness consistency battery) now reads: G,
rho_v, and a are locked into a ONE-parameter family with every
coefficient an exact function of arccos(1/3). If any independent
probe ever measures a discreteness scale, the system is
overdetermined twice over -- the floor-Newton lock must produce the
observed G, AND the 048 scalaron must appear at range sqrt(6) a.
Parameter-free consistency tests waiting on a measurement nobody yet
knows how to make: recorded as exactly that.

## What Stays Open

```text
o_p10_1_packing_scale_052: the packing scale a -- the sole remaining
microphysics constant; same thread as "is space discrete." No
derivation route on the books; Planck-scale a remains an assumption
wherever used, and is recorded as such.
```

## Ledger

```text
derivation:  edge_density_052
satisfies:   o_p10_1_ce_derived_052 (O-P10-1, c_e face)
opens:       o_p10_1_packing_scale_052 (the remainder, explicit)
depends on:  regge_delaunay_bridge_039, ground_coordination_4d_050,
             bulk_relaxation_phase2_051
```
