# VacuumForge: The Angle-Gap Energy in Bulk, Neighbours Fixed

## Status

```text
result type:   numerical experiment (stage 3 step 1; 2026-11-24,
               derivation 060); TRIAL angle energy, K = 1 units
question:      with the 057 quanta, box and neighbour list fixed, does
               the angle-gap energy store strain in a different pattern
               from the spring proxy?
satisfies:     p10_bulk_fixed_neighbours_060
opens:         p10_bulk_neighbour_changes_060 (step 2)
packings:      vacuum_forge/src/vacuum_sector/060_angle_energy_fixed_neighbors/
               packing_060.npz (content sha256 9168ad36b4c76cbe...)
verification:  vacuum_forge/src/vacuum_sector/060_angle_energy_fixed_neighbors/
```

## The Two Energies

```text
P10 candidate:  E_w = sum over (tet, edge) of l_e (1/2)(theta - arccos(1/3))^2
control:        E_u = sum over (tet, edge) of     (1/2)(theta - arccos(1/3))^2
per hinge (closed, flat, n tetrahedra):
  (1/2) sum x_i^2 = (2 pi - n theta0)^2 / (2 n)  +  (1/2) sum (theta_i - 2 pi/n)^2
                    unavoidable at n                 extra: uneven sharing
```

## Measured Results

```text
E1. START (057 pre-relaxation coordinates; hash verified). Coordination
    histogram {3: 160, 4: 309, 5: 273, 6: 239, 7: 143, 8: 85, 9: 20, 10: 7, 11: 2}. Every hinge closes (deficit 0); per-hinge
    identity exact. E_u = 1229.778 = unavoidable 441.129 + extra
    788.649.

E2. CONTROL (unweighted):
    mu      E_angle     unavoidable  extra      angle res max/rms   min V/V_ref  min edge  mean edge
    0.001     976.7102    441.1291   535.5811  2.783/0.3055   1.99e-04   0.2251   0.9860
    0.0001    976.7091    441.1291   535.5801  2.774/0.3041   2.00e-05   0.2244   0.9860
    1e-05     976.7090    441.1291   535.5800  2.773/0.3040   2.00e-06   0.2244   0.9860
    With neighbours fixed the unavoidable part is frozen; relaxation
    removes 32.1% of the starting extra. At the relaxed state the
    unavoidable coordination cost is 45.2% of E_u.

E3. P10 CANDIDATE (length-weighted):
    mu      E_angle     unavoidable  extra      angle res max/rms   min V/V_ref  min edge  mean edge
    0.001     948.5497    441.1291   553.0394  6.822/0.6633   6.84e-05   0.2798   0.9809
    0.0001    948.5485    441.1291   553.1142  6.827/0.6627   6.84e-06   0.2794   0.9809
    1e-05     948.5484    441.1291   553.1220  6.827/0.6627   6.84e-07   0.2793   0.9809
    (unavoidable and extra columns are unweighted per-hinge sums)
    E_w 1247.6316 -> 948.5497: angle redistribution at starting lengths
    -244.5030; hinge-length change -54.5789 (exact split).
    Mean hinge length by coordination, start -> relaxed:
    n =  3 ( 160 hinges; unavoidable 1.1183 each): 1.1985 -> 1.1105 weighted, 1.1727 unweighted
    n =  4 ( 309 hinges; unavoidable 0.2310 each): 1.1074 -> 1.1005 weighted, 1.0965 unweighted
    n =  5 ( 273 hinges; unavoidable 0.0016 each): 1.0145 -> 1.0128 weighted, 0.9939 unweighted
    n =  6 ( 239 hinges; unavoidable 0.1013 each): 0.8971 -> 0.9277 weighted, 0.9136 unweighted
    n =  7 ( 143 hinges; unavoidable 0.3890 each): 0.8179 -> 0.8220 weighted, 0.8258 unweighted
    n =  8 (  85 hinges; unavoidable 0.7941 each): 0.8624 -> 0.7519 weighted, 0.7941 unweighted
    n =  9 (  20 hinges; unavoidable 1.2776 each): 0.7769 -> 0.5593 weighted, 0.6332 unweighted
    n = 10 (   7 hinges; unavoidable 1.8159 each): 0.6804 -> 0.5939 weighted, 0.6232 unweighted
    n = 11 (   2 hinges; unavoidable 2.3941 each): 1.0598 -> 0.8099 weighted, 0.9501 unweighted
    Correlation of hinge-length ratio with unavoidable cost: weighted
    -0.151, unweighted -0.089.

E4. BARRIER SENSITIVITY (mu 1e-3 -> 1e-5): angle energy change
    0.0001% (unweighted), 0.0001% (weighted); contact sets
    1 and 1 tetrahedra (volume tracks mu); min edge drift
    0.32% and 0.19%: no edge collapses.

E5. DIRECTIONAL FABRICS (per-hinge energy x hinge direction; weakest
    barrier; spring fabric = 057's (l-1)^2 on the same neighbours):
    fabric                   anisotropy  dev eigenvalues / tr
    angle, unweighted        0.0248    [-0.0155, -0.0036, 0.019]
    angle, weighted          0.0275    [-0.0177, -0.0032, 0.0209]
    extra only, unweighted   0.0269    [-0.0125, -0.0094, 0.0219]
    extra only, weighted     0.0287    [-0.0161, -0.0066, 0.0228]
    spring (057)             0.0322    [-0.0218, -0.0018, 0.0237]
    angle at start           0.0202    [-0.0153, 0.0021, 0.0131]
    deviatoric overlaps (cosine; +1 = same pattern, 0 = unrelated):
    angle, weighted          vs spring (057)             +0.906
    angle, unweighted        vs spring (057)             +0.902
    angle, weighted          vs angle, unweighted        +0.990
    angle, weighted          vs angle at start           +0.884
    spring (057)             vs angle at start           +0.916
    extra only, weighted     vs spring (057)             +0.654

E6. STRESS (affine virial, fixed box): unweighted trace -5.7e-08
    (dilation flat, exact 0); weighted trace 948.5484 = E_w 948.5484
    (degree-one homogeneity). Deviatoric eigenvalues: unweighted
    [-40.6301, 12.4119, 28.2182], weighted
    [-54.3041, 2.8472, 51.4569].
```

## Reading

- **What fixed neighbours leave behind.** In the control, the
  unavoidable coordination cost (441.1) is frozen by the 057
  triangulation. Relaxation removes 32% of the uneven-sharing extra,
  but 535.6 remains (55% of E_u): neighbouring tetrahedra cannot all
  reach their individual hinge minima at once, because each
  tetrahedron's six dihedrals are coupled.
- **How the weighted model relieves frustration.** Of its energy drop,
  82% comes from redistributing angles at the starting lengths
  and 18% from changing hinge lengths. Relative to the unweighted
  control, the extra shortening falls on the most frustrated hinges
  (n = 3 and n >= 8; see the coordination table); across all hinges
  the correlation with unavoidable cost is weak (-0.15).
- **Directional pattern.** With neighbours fixed, all three energies
  store their strain along similar directions: the angle fabrics
  overlap the spring fabric at +0.91 (weighted) and
  +0.90 (unweighted), and every fabric overlaps the starting
  mesh's (+0.92 for the spring). The pattern is largely
  inherited from the triangulation. The part the angle energy adds,
  the uneven-sharing extra, is less aligned with the spring fabric
  (+0.65). Anisotropy magnitudes are similar
  (0.028 weighted, 0.032 spring).
- **Validity.** Each model holds one tetrahedron against the
  zero-volume constraint (volume tracks mu); energies change by about
  1e-6 relative as mu drops 100x, and no edge collapses. The 057 spring
  control held 34.
- At fixed neighbours, then, the angle-gap energy does not produce a
  markedly different directional pattern from the spring model on the
  same quanta. Whether a different pattern, or a frustration floor,
  emerges when neighbours can change is step 2's question.

## Fences

```text
- TRIAL angle energy (059), K explicit; both weightings are models.
- neighbours fixed: the unavoidable coordination cost is frozen by the
  057 triangulation; whether any of it survives neighbour changes is
  step 2 (p10_bulk_neighbour_changes_060).
- one seed, one size, one cubic box.
- no EM coupling.
```

## Ledger

```text
derivation:  angle_energy_fixed_neighbors_060
satisfies:   p10_bulk_fixed_neighbours_060
opens:       p10_bulk_neighbour_changes_060
depends on:  periodic_spring_control_057, wedge_strain_definition_059
```
