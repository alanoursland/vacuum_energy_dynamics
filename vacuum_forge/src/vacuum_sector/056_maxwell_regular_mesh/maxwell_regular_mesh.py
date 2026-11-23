#!/usr/bin/env python3
"""
maxwell_regular_mesh.py

Derivation 056: the Maxwell probe's regular-mesh benchmark
(09_maxwell_probe, stage 1; maxwell_regular_mesh_reproduction_056).

Discrete Maxwell theory is an added PROBE of the packing geometry. This
module calibrates the instrument on a geometry VED already uses: the
600-cell (039, result 3), whose 120 vertices form the binary
icosahedral group I*. Its quotient by the LEFT action of I* is the
Poincare homology sphere I*\\S^3, on which a smooth Maxwell mode is
known exactly (Anonymous [@WhatMathMeans], "The Intrinsic Geometry of
Electromagnetism Is the Poincare Homology Sphere", manuscript
circulated as page images on X, 23 November 2026). The discrete
calculation was first done in exploratory scratch work
(09_maxwell_probe/scratch_2026-11-23/cell_check.py); this module is its
forge port, with acceptance checks.

Five experiments:

  E1. THE GROUP AND THE MESH. The 120 vertices are unit quaternions
      closed under multiplication (they ARE I*). 720 edges of chord
      1/phi, 1200 triangles, 600 tetrahedra. Left multiplication acts
      freely and maps the mesh to itself, so the quotient is a
      one-vertex triangulation with face identifications: 1 vertex,
      6 edges (all loops), 10 triangles, 5 tetrahedra, chi = 0. The
      edge label Im(conj(q_i) q_j) is invariant under simultaneous
      left multiplication.

  E2. THE SMOOTH BENCHMARK. The left-invariant frames X_a(q) = q e_a / R
      descend to the quotient. Their curl is measured by Stokes
      circulation on small loops: curl X_a = -2 X_a / R in the
      orientation where (X_1, X_2, X_3) is right-handed (the
      manuscript's sign). Maxwell's equations for the rotating pair
      E = A(X1 cos wt + X2 sin wt), cB = A(X1 sin wt - X2 cos wt) are
      solved symbolically: omega = 2c/R. Poynting flux along -X_3.
      The edge samples of the dual frame one-forms are a common factor
      times Im(conj(q_i) q_j).

  E3. THE DISCRETE SPECTRUM. d1^T *2 d1 e = (omega/c)^2 *1 e on the
      quotient, circumcentric Hodge weights from the flat chord
      tetrahedra (R = 1 circumradius). Lowest triplet 2.10292445, second
      triplet 8.90813092; the sampled frame patterns span the lowest
      eigenspace. With one vertex d0 = 0, and H^1 = 0 gives ker d1 = 0:
      no exact-gradient or harmonic zero modes in this edge problem.

  E4. WHY THE TRIPLETS (symmetry). Right multiplication by I* commutes
      with the left action and acts on the six oriented edge classes by
      signed permutations; +1 and -1 act identically, so the action
      factors through A5. Its character is (6, -2, 0, 1, 1) =
      chi_3 + chi_3'. The Maxwell operator commutes with the action, so
      each irreducible triplet carries a single eigenvalue. The frame
      samples carry the rotation representation 3 (character phi at the
      72-degree class), and that is the LOWER triplet. Symmetry explains
      the triplets; the calculation fixes which is lower and its
      frequency.

  E5. THE STRETCH CONTROL. Lengthening one edge class by 1% splits the
      low triplet into 2.08334853 (x2) and 2.13210754: the solver
      responds to anisotropic geometry.

Fences: Maxwell is a probe; no claim that spatial quanta produce
electromagnetism; no observable channel (06 quarantine). The discrete
operator measures omega^2 and cannot see helicity (E2 tests the sign
smoothly). One coarse mesh is a benchmark, not a convergence result.
H^1 = 0 here, so this module cannot validate harmonic modes: the torus
gates G3a-G3c are a separate obligation. The unsigned circumcentric
weights used here are valid for the regular mesh and small
perturbations of it only.
"""

import itertools as it
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.spatial.distance import cdist

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_ID = f"{SCRIPT_PATH.parent.name}__{SCRIPT_PATH.stem}"
ARCHIVE_ROOT = SCRIPT_PATH.parents[1] / ".vacuumforge_archive"
REPO_ROOT = SCRIPT_PATH.parents[4]
REPORT_PATH = (REPO_ROOT / "theory_v3" / "development" / "vacuum_sector"
               / "09_maxwell_probe" / "maxwell_regular_mesh_vacuumforge.md")

DEPENDENCIES = [
    ("regge_dep_056", "039_regge_delaunay_bridge__regge_delaunay_bridge",
     "regge_delaunay_bridge_039"),
]

PHI = (1 + 5 ** 0.5) / 2
TOL_EIG = 1e-8          # acceptance tolerance on reference frequencies
TOL_EXACT = 1e-10       # tolerance on identities that hold exactly

REF_LOW = 2.10292445
REF_HIGH = 8.90813092
REF_STRETCH = (2.08334853, 2.08334853, 2.13210754)


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def require(label: str, condition: bool, failures: list) -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"  [{mark}] {label}")
    if not condition:
        failures.append(label)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in DEPENDENCIES:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
        )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


# =============================================================================
# Quaternions (w, x, y, z); vectorized over leading axes
# =============================================================================


def qmul(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    w1, x1, y1, z1 = np.moveaxis(a, -1, 0)
    w2, x2, y2, z2 = np.moveaxis(b, -1, 0)
    return np.stack([
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    ], axis=-1)


def qconj(a):
    return np.asarray(a, dtype=float) * np.array([1.0, -1.0, -1.0, -1.0])


def qexp_imag(v):
    """exp of a pure-imaginary quaternion given by its 3-vector v."""
    t = float(np.linalg.norm(v))
    if t == 0.0:
        return np.array([1.0, 0.0, 0.0, 0.0])
    return np.concatenate([[math.cos(t)], math.sin(t) * np.asarray(v) / t])


def key(q, nd=9):
    return tuple(np.round(q, nd) + 0.0)


UNITS = np.eye(4)[1:]   # e_1 = i, e_2 = j, e_3 = k as quaternions


# =============================================================================
# The 600-cell
# =============================================================================


def six_hundred_cell_vertices():
    v = [s * x for x in np.eye(4) for s in (-1, 1)]
    v += [np.array(t) / 2 for t in it.product([-1, 1], repeat=4)]
    for perm in it.permutations(range(4)):
        if sum(i > j for i, j in it.combinations(perm, 2)) % 2:
            continue  # even permutations only
        for a, b, c in it.product([-1, 1], repeat=3):
            v.append(np.array([0, a, b * PHI, c / PHI])[list(perm)] / 2)
    return np.array(v, dtype=float)


def build_mesh(v):
    adj = np.isclose(cdist(v, v), 1 / PHI)
    n = len(v)
    edges = list(zip(*np.where(np.triu(adj, 1))))
    faces = [(i, j, k) for i, j in edges
             for k in np.where(adj[i] & adj[j] & (np.arange(n) > j))[0]]
    tets = [(i, j, k, l) for i, j, k in faces
            for l in np.where(adj[i] & adj[j] & adj[k] & (np.arange(n) > k))[0]]
    return adj, edges, faces, tets


def edge_label(v, i, j):
    """Im(conj(q_i) q_j): invariant under simultaneous left multiplication."""
    return qmul(qconj(v[i]), v[j])[1:]


def classify_edges(v, edges):
    """Six unoriented classes; em[(i, j)] = (class, sign) for the oriented edge."""
    dirs, em = [], {}
    for i, j in edges:
        d = edge_label(v, i, j)
        s = np.sign(d[np.where(np.abs(d) > 1e-7)[0][0]])
        d = d * s
        k = next((k for k, x in enumerate(dirs) if np.allclose(d, x)), len(dirs))
        if k == len(dirs):
            dirs.append(d)
        em[(i, j)] = (k, s)
        em[(j, i)] = (k, -s)
    return np.array(dirs), em


def left_orbit_count(v, cells):
    """Number of left-I* orbits of a list of vertex-index cells."""
    vk = {key(q): idx for idx, q in enumerate(v)}
    seen = set()
    for cell in cells:
        reps = []
        for base in cell:  # translate each vertex of the cell to 1
            hb = qconj(v[base])
            img = sorted(vk[key(qmul(hb, v[c]))] for c in cell)
            reps.append(tuple(img))
        seen.add(min(reps))
    return len(seen)


# =============================================================================
# E1: the group and the mesh
# =============================================================================


def experiment_1_group_and_mesh(failures):
    header("E1: the binary icosahedral group, the 600-cell, and its left quotient")
    v = six_hundred_cell_vertices()
    adj, edges, faces, tets = build_mesh(v)
    vk = {key(q): idx for idx, q in enumerate(v)}

    norms_ok = np.allclose(np.linalg.norm(v, axis=1), 1.0)
    prods = qmul(v[:, None, :], v[None, :, :]).reshape(-1, 4)
    closed = all(key(p) in vk for p in prods)
    print(f"    vertices = {len(v)}, edges = {len(edges)}, triangles = {len(faces)}, "
          f"tetrahedra = {len(tets)}")
    require("120 unit quaternions, closed under multiplication (the group I*)",
            len(v) == 120 and norms_ok and closed, failures)
    require("600-cell counts 720 / 1200 / 600, edge chord 1/phi",
            (len(edges), len(faces), len(tets)) == (720, 1200, 600), failures)

    # Left action is an isometry mapping the mesh to itself
    eset = set(edges)
    maps_mesh = True
    for h in v:
        hv = qmul(h[None, :], v)
        perm = np.array([vk[key(q)] for q in hv])
        for i, j in edges:
            a, b = sorted((perm[i], perm[j]))
            if (a, b) not in eset:
                maps_mesh = False
                break
        if not maps_mesh:
            break
    require("left multiplication by every h in I* maps the edge set to itself",
            maps_mesh, failures)

    # Label invariance under simultaneous left multiplication
    ii = np.array([e[0] for e in edges])
    jj = np.array([e[1] for e in edges])
    base = qmul(qconj(v[ii]), v[jj])
    inv_err = 0.0
    for h in v:
        hi = qmul(h[None, :], v[ii])
        hj = qmul(h[None, :], v[jj])
        inv_err = max(inv_err, float(np.max(np.abs(qmul(qconj(hi), hj) - base))))
    require(f"edge label Im(conj(q_i) q_j) is left-invariant (max err {inv_err:.1e})",
            inv_err < TOL_EXACT, failures)

    dirs, em = classify_edges(v, edges)
    counts = (1, len(dirs), left_orbit_count(v, faces), left_orbit_count(v, tets))
    chi = counts[0] - counts[1] + counts[2] - counts[3]
    print(f"    quotient: vertices = {counts[0]}, edges = {counts[1]}, "
          f"triangles = {counts[2]}, tetrahedra = {counts[3]}, chi = {chi}")
    require("left action is free: quotient counts = upstairs / 120 = 1 / 6 / 10 / 5",
            counts == (1, 6, 10, 5) and len(faces) == 120 * 10 and len(tets) == 120 * 5,
            failures)
    require("Euler characteristic 0 (closed 3-manifold)", chi == 0, failures)

    # Neighbors of 1 come in inverse pairs g, g^-1 with opposite imaginary parts
    one = vk[key(np.array([1.0, 0, 0, 0]))]
    nbrs = np.where(adj[one])[0]
    inv_pairs = all(vk[key(qconj(v[n]))] in set(nbrs) for n in nbrs)
    not_antipodal = all(vk.get(key(-v[n])) not in set(nbrs) for n in nbrs)
    require("the 12 neighbors of 1 come in inverse pairs g, g^-1 (not antipodes)",
            len(nbrs) == 12 and inv_pairs and not_antipodal, failures)
    print("  The 600-cell descends to a one-vertex quotient triangulation of the")
    print("  Poincare homology sphere; its six edges are loops.")
    return v, adj, edges, faces, tets, dirs, em


# =============================================================================
# E2: the smooth benchmark
# =============================================================================


def stokes_curl(q0, a, eps=1e-3, n=4000):
    """Circulation of X_a around a small loop in the (X_b, X_c) plane / area."""
    b, c = [(1, 2), (2, 0), (0, 1)][a]
    s = np.linspace(0, 2 * np.pi, n, endpoint=False)
    ds = 2 * np.pi / n
    h = 1e-6
    circ = 0.0
    for si in s:
        u = eps * (math.cos(si) * UNITS[b][1:] + math.sin(si) * UNITS[c][1:])
        du = eps * (-math.sin(si) * UNITS[b][1:] + math.cos(si) * UNITS[c][1:])
        g = qmul(q0, qexp_imag(u))
        gp = (qmul(q0, qexp_imag(u + h * du / eps))
              - qmul(q0, qexp_imag(u - h * du / eps))) / (2 * h) * eps
        xa = qmul(g, UNITS[a])
        circ += float(np.dot(xa, gp)) * ds
    return circ / (math.pi * eps ** 2)


def experiment_2_smooth(v, edges, failures):
    header("E2: the smooth benchmark on I*\\S^3 (manuscript field)")
    rng = np.random.default_rng(20261123)

    # Frames descend: X_a(hq) = h X_a(q)
    qs = v[rng.integers(0, 120, 5)]
    descend = all(np.allclose(qmul(qmul(h, q), UNITS[a]), qmul(h, qmul(q, UNITS[a])))
                  for h in v[:12] for q in qs for a in range(3))
    require("left-invariant frames descend: X_a(hq) = h X_a(q)", descend, failures)

    # Curl sign by Stokes circulation at random points (unit radius)
    q0s = rng.normal(size=(2, 4))
    q0s /= np.linalg.norm(q0s, axis=1)[:, None]
    curls = [stokes_curl(q0, a) for q0 in q0s for a in range(3)]
    print(f"    Stokes curl components (X_a . curl X_a): "
          + ", ".join(f"{c:+.6f}" for c in curls))
    require("curl X_a = -2 X_a / R (right-handed (X1,X2,X3); |err| < 1e-5)",
            all(abs(c + 2.0) < 1e-5 for c in curls), failures)

    # Maxwell for the rotating pair, symbolically
    A, w, t, c, R = sp.symbols("A omega t c R", positive=True)
    lam = -2 / R
    E = sp.Matrix([A * sp.cos(w * t), A * sp.sin(w * t), 0])          # in frame X_a
    cB = sp.Matrix([A * sp.sin(w * t), -A * sp.cos(w * t), 0])
    ampere = sp.simplify(E.diff(t) - c * lam * cB)
    faraday = sp.simplify(cB.diff(t) + c * lam * E)
    sol = sp.solve([ampere[0], faraday[0]], w, dict=True)
    omegas = {s[w] for s in sol}
    print(f"    Ampere/Faraday solved for omega: {omegas}")
    require("Maxwell's equations hold iff omega = 2 c / R",
            omegas == {2 * c / R}
            and all(sp.simplify(x.subs(w, 2 * c / R)) == 0 for x in list(ampere) + list(faraday)),
            failures)
    poynting = E.subs(t, 0).cross(cB.subs(t, 0))
    require("Poynting flux at t = 0 is along -X_3 (E x cB = -A^2 X_3)",
            sp.simplify(poynting - sp.Matrix([0, 0, -A ** 2])) == sp.zeros(3, 1), failures)

    # Edge samples of the dual frame one-forms vs Im(conj(q_i) q_j)
    theta = math.pi / 5
    common = theta / math.sin(theta)
    errs = []
    for i, j in edges[:40]:
        d = edge_label(v, i, j)
        n_hat = d / np.linalg.norm(d)
        m = 400
        integral = np.zeros(3)
        for s in (np.arange(m) + 0.5) / m:
            g = qmul(v[i], qexp_imag(theta * s * n_hat))
            gdot = qmul(g, np.concatenate([[0.0], theta * n_hat]))
            integral += np.array([np.dot(qmul(g, UNITS[a]), gdot) for a in range(3)]) / m
        errs.append(float(np.max(np.abs(integral - common * d))))
    print(f"    edge angular length theta = pi/5 (chord 2 sin(pi/10) = 1/phi); "
          f"max |sample - (theta/sin theta) Im(conj(q_i) q_j)| = {max(errs):.1e} "
          f"(theta/sin theta = {common:.10f})")
    require("edge samples = (theta / sin theta) Im(conj(q_i) q_j), common to all edges",
            max(errs) < 1e-9
            and math.isclose(2 * math.sin(theta / 2), 1 / PHI, abs_tol=1e-12), failures)
    print("  The smooth target is exact: omega R / c = 2, a single helicity, its")
    print("  edge pattern given by Im(conj(q_i) q_j).")
    return 2.0


# =============================================================================
# E3 / E5: the discrete spectrum and the stretch control
# =============================================================================


def incidence(faces, em):
    rows = []
    for i, j, k in faces:
        row = np.zeros(6)
        for e, s in (((i, j), 1), ((j, k), 1), ((i, k), -1)):
            h, t = em[e]
            row[h] += s * t
        rows.append(row)
    return np.array(rows)


def hodge_weights(faces, tets, em, scale):
    """Unsigned circumcentric *1 (per edge class) and *2 (per upstairs face).

    Valid for the regular mesh and small perturbations of it only.
    Both sides are summed over all 120 copies; the factor cancels.
    """
    fid = {f: n for n, f in enumerate(faces)}
    m1 = np.zeros(6)
    m2 = np.zeros(len(faces))
    for t in tets:
        g = np.zeros((4, 4))
        for i, j in it.combinations(range(4), 2):
            g[i, j] = g[j, i] = (scale[em[(t[i], t[j])][0]] / PHI) ** 2
        G = (g[0, 1:, None] + g[0, None, 1:] - g[1:, 1:]) / 2
        x = np.vstack((np.zeros(3), np.linalg.cholesky(G)))
        ct = np.linalg.solve(2 * x[1:], np.diag(G))
        for f in it.combinations(range(4), 3):
            a, b, c = x[list(f)]
            T = np.stack((b - a, c - a))
            cf = a + T.T @ np.linalg.solve(2 * T @ T.T, np.diag(T @ T.T))
            height = np.linalg.norm(ct - cf)
            m2[fid[tuple(t[i] for i in f)]] += height / (np.linalg.norm(np.cross(*T)) / 2)
            for i, j in it.combinations(f, 2):
                m1[em[(t[i], t[j])][0]] += (0.5 * height * np.linalg.norm(cf - (x[i] + x[j]) / 2)
                                            / np.linalg.norm(x[i] - x[j]))
    return m1, m2


def spectrum(B, faces, tets, em, scale):
    m1, m2 = hodge_weights(faces, tets, em, scale)
    K = B.T @ (m2[:, None] * B)
    M = np.diag(m1)
    w2, vecs = eigh(K, M)
    return np.sqrt(w2), vecs, K, M


def experiment_3_discrete(v, edges, faces, tets, dirs, em, failures):
    header("E3: the discrete Maxwell spectrum on the quotient")
    B = incidence(faces, em)
    gram = B.T @ B / 120
    gram_eigs = np.linalg.eigvalsh(gram)
    print(f"    B^T B / 120 eigenvalues: {np.round(gram_eigs, 8)}")
    require("d1 injective on the six edge classes (ker d1 = 0; d0 = 0 with one vertex)",
            np.min(gram_eigs) > 1e-6 and np.linalg.matrix_rank(B) == 6, failures)

    omega, vecs, K, M = spectrum(B, faces, tets, em, np.ones(6))
    print(f"    omega R / c: {np.array2string(omega, precision=8)}")
    require(f"lowest triplet = {REF_LOW} (tol {TOL_EIG})",
            np.allclose(omega[:3], REF_LOW, atol=TOL_EIG), failures)
    require(f"second triplet = {REF_HIGH} (tol {TOL_EIG})",
            np.allclose(omega[3:], REF_HIGH, atol=TOL_EIG), failures)

    low = vecs[:, :3]
    D = dirs  # 6 x 3: the frame samples Im(conj(q_i) q_j) per class
    proj = low @ np.linalg.solve(low.T @ M @ low, low.T @ M @ D)
    span_res = float(np.max(np.abs(proj - D)))
    print(f"    frame samples vs lowest eigenspace: residual {span_res:.1e}")
    require("the sampled frame patterns span the lowest eigenspace",
            span_res < TOL_EXACT and np.linalg.matrix_rank(D) == 3, failures)
    rel = omega[0] / 2.0 - 1.0
    print(f"    discrete / smooth = {omega[0] / 2.0:.8f} ({100 * rel:+.3f}%)")
    return B, omega, K, M


def experiment_5_stretch(B, faces, tets, em, failures):
    header("E5: the stretch control (class 0 lengthened by 1%)")
    scale = np.ones(6)
    scale[0] = 1.01
    omega, _, _, _ = spectrum(B, faces, tets, em, scale)
    print(f"    omega R / c: {np.array2string(omega, precision=8)}")
    require("low triplet splits to 2.08334853 (x2), 2.13210754 (tol 1e-8)",
            np.allclose(omega[:3], REF_STRETCH, atol=TOL_EIG), failures)
    mean_shift = omega[:3].mean() / REF_LOW - 1.0
    print(f"    mean of the low triplet shifts by {100 * mean_shift:+.4f}% "
          "(one sixth of the edges lengthened by 1%)")
    require("mean shift ~ -1/6 % (within 0.02%)", abs(mean_shift + 1 / 600) < 2e-4, failures)
    return omega


# =============================================================================
# E4: why the triplets
# =============================================================================


def right_action_matrices(v, dirs):
    """Signed permutation of the six edge classes under q -> q g."""
    mats = []
    for g in v:
        P = np.zeros((6, 6))
        for k, d in enumerate(dirs):
            rot = qmul(qmul(qconj(g), np.concatenate([[0.0], d])), g)[1:]
            for k2, d2 in enumerate(dirs):
                if np.allclose(rot, d2):
                    P[k2, k] = 1
                elif np.allclose(rot, -d2):
                    P[k2, k] = -1
        mats.append(P)
    return mats


def conjugacy_class(g):
    """A5 class of the image of g in I*/{+-1}, read off |Re g|."""
    r = abs(g[0])
    for name, val in (("1", 1.0), ("(12)(34)", 0.0), ("(123)", 0.5),
                      ("5A", PHI / 2), ("5B", 1 / (2 * PHI))):
        if abs(r - val) < 1e-9:
            return name
    raise ValueError(g)


def experiment_4_symmetry(v, dirs, K, M, omega, failures):
    header("E4: why the triplets -- the residual A5 symmetry")
    mats = right_action_matrices(v, dirs)
    vk = {key(q): idx for idx, q in enumerate(v)}
    signed_perm = all(np.all(np.abs(P).sum(axis=0) == 1) for P in mats)
    central = all(np.allclose(mats[n], mats[vk[key(-g)]]) for n, g in enumerate(v))
    require("right action = signed permutations of the 6 classes; +1 and -1 act identically",
            signed_perm and central, failures)

    classes = ("1", "(12)(34)", "(123)", "5A", "5B")
    sizes = {c: 0 for c in classes}
    chars = {c: set() for c in classes}
    for g, P in zip(v, mats):
        c = conjugacy_class(g)
        sizes[c] += 1
        chars[c].add(round(float(np.trace(P)), 9))
    sizes = {c: n // 2 for c, n in sizes.items()}  # I* -> A5 is 2:1
    print(f"    A5 class sizes: {sizes}")
    print(f"    character of the signed edge representation: "
          f"{ {c: sorted(s) for c, s in chars.items()} }")
    chi_edges = tuple(next(iter(chars[c])) for c in classes)
    chi_3 = (3, -1, 0, PHI, 1 - PHI)
    chi_3p = (3, -1, 0, 1 - PHI, PHI)
    require("character is a class function equal to (6, -2, 0, 1, 1) = chi_3 + chi_3'",
            all(len(chars[c]) == 1 for c in classes)
            and np.allclose(chi_edges, (6, -2, 0, 1, 1))
            and np.allclose(np.add(chi_3, chi_3p), chi_edges)
            and sizes == {"1": 1, "(12)(34)": 15, "(123)": 20, "5A": 12, "5B": 12},
            failures)

    comm = max(max(float(np.max(np.abs(P @ K - K @ P))), float(np.max(np.abs(P @ M - M @ P))))
               for P in mats)
    require(f"Maxwell operator commutes with the action (max |[P, K]|, |[P, M]| = {comm:.1e})",
            comm < 1e-9, failures)

    def projector(chi):
        Pr = np.zeros((6, 6))
        for g, P in zip(v, mats):
            Pr += chi[classes.index(conjugacy_class(g))] * P
        return 3 * Pr / 120  # |A5| = 60, each element counted twice in I*

    P3, P3p = projector(chi_3), projector(chi_3p)
    ranks = (np.linalg.matrix_rank(P3, tol=1e-8), np.linalg.matrix_rank(P3p, tol=1e-8))
    require(f"isotypic projectors have ranks (3, 3): got {ranks}", ranks == (3, 3), failures)
    frames_in_3 = np.allclose(P3 @ dirs, dirs, atol=1e-9)
    require("frame samples carry the rotation representation 3 (chi = phi at 72 deg)",
            frames_in_3, failures)

    w2_3 = np.linalg.eigvals(np.linalg.pinv(M) @ K @ P3)
    w2_3 = np.sort(np.real(w2_3))[-3:]
    require("the 3 isotypic block carries the LOWER triplet; 3' carries the upper",
            np.allclose(np.sqrt(w2_3), omega[0], atol=1e-8), failures)
    print("  Symmetry forces two triplets and puts the frame pattern in one of")
    print("  them. The calculation decides that the frame triplet is the lower")
    print("  one and fixes its frequency.")
    return chi_edges


# =============================================================================
# Record + report
# =============================================================================


def record(ns):
    ns.record_derivation(
        derivation_id="maxwell_regular_mesh_056",
        inputs=[sp.Symbol("six_hundred_cell_039"), sp.Symbol("left_quotient_poincare_sphere"),
                sp.Symbol("circumcentric_dec_maxwell")],
        output=sp.Symbol("regular_mesh_maxwell_benchmark"),
        method=(
            "600-cell vertices as I*; left-orbit counts of edges/faces/tets; Stokes "
            "circulation of left-invariant frames for the curl sign; symbolic "
            "Ampere/Faraday for omega; quadrature of frame one-forms along edges; "
            "circumcentric DEC generalized eigenproblem on the quotient (unsigned "
            "weights, regular mesh); signed-permutation character of the right A5 "
            "action with isotypic projectors; 1% class stretch control"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="numerical_benchmark",
        scope=(
            "one coarse regular mesh (benchmark, not convergence); H^1 = 0 so no "
            "harmonic-mode validation; omega^2 operator blind to helicity (sign tested "
            "smoothly only); Maxwell is a probe, no EM-from-quanta claim, no channel"
        ),
    )
    ns.record_obligation(ProofObligationRecord(
        obligation_id="maxwell_regular_mesh_reproduction_056",
        script_id=SCRIPT_ID,
        title="Regular-mesh Maxwell benchmark reproduced with acceptance checks",
        status=ObligationStatus.SATISFIED,
        satisfied_by=["maxwell_regular_mesh_056"],
        description=(
            "Stage 1 of 09_maxwell_probe: quotient counts 1/6/10/5, left-action "
            "convention, smooth omega R/c = 2 with curl sign -2/R, discrete triplets "
            "2.10292445 and 8.90813092, frame-pattern span, A5 character "
            "(6,-2,0,1,1), 1% stretch control."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="maxwell_torus_calibration_056",
        script_id=SCRIPT_ID,
        title="Periodic-solver calibration: torus gates G3a-G3c",
        status=ObligationStatus.OPEN,
        required_by=["maxwell_regular_mesh_056"],
        description=(
            "The regular quotient has H^1 = 0 and cannot validate harmonic modes. "
            "A periodic solver must pass G3a (nullity V - 1 + 3, three dimensions "
            "after removing gradients), G3b (fork (a): they span the uniform E "
            "fields), and G3c (twisted: V gradient zero modes; two small positive "
            "transverse frequencies) before the stage-4 sweep."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="maxwell_regular_mesh_claim_056",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.INFORMATIONAL,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "On the 600-cell quotient of the Poincare homology sphere, circumcentric "
            "discrete Maxwell gives a lowest triplet at omega R/c = 2.10292445 vs the "
            "smooth 2 (curl X_a = -2 X_a/R, left action). The residual A5 symmetry "
            "splits the six edge classes as 3 + 3', which forces the triplets; the "
            "frame pattern carries 3 and is the lower triplet. A 1% stretch of one "
            "class splits it. Instrument calibration only."
        ),
        derivation_ids=["maxwell_regular_mesh_056"],
        obligation_ids=["maxwell_regular_mesh_reproduction_056"],
    ))


def write_report(omega, omega_stretch, chi_edges):
    om = " ".join(f"{x:.8f}" for x in omega)
    st = " ".join(f"{x:.8f}" for x in omega_stretch)
    md = f"""# VacuumForge: The Maxwell Probe's Regular-Mesh Benchmark

## Status

```text
result type:   numerical benchmark (instrument calibration; 2026-11-23,
               derivation 056)
conclusion:    the solver recovers the known smooth mode's pattern and
               its frequency to {100 * (omega[0] / 2 - 1):.2f}% on the coarsest mesh;
               icosahedral symmetry protects the triplet; a controlled
               deformation splits it.
satisfies:     maxwell_regular_mesh_reproduction_056 (09 charter,
               stage 1)
opens:         maxwell_torus_calibration_056 (gates G3a-G3c)
verification:  vacuum_forge/src/vacuum_sector/056_maxwell_regular_mesh/
```

## Measured Results

```text
E1. GROUP AND MESH. 120 unit quaternions closed under multiplication
    (I*); 720 / 1200 / 600 edges / triangles / tetrahedra. Left
    multiplication acts freely and maps the mesh to itself; quotient
    1 / 6 / 10 / 5, chi = 0, all six edges loops. Edge label
    Im(conj(q_i) q_j) left-invariant. Neighbors of 1 in inverse pairs.

E2. SMOOTH BENCHMARK. Frames X_a(q) = q e_a / R descend. Stokes
    circulation gives curl X_a = -2 X_a / R (right-handed frame).
    Ampere + Faraday hold iff omega = 2c/R. Poynting flux along -X_3.
    Edge samples = (theta / sin theta) Im(conj(q_i) q_j), theta = pi/5.

E3. DISCRETE SPECTRUM (circumcentric, R = 1, chord edges 1/phi):
    omega R / c = {om}
    ker d1 = 0 (no gradient or harmonic zero modes). The frame samples
    span the lowest eigenspace.

E4. SYMMETRY. Right A5 action on the signed edge classes: character
    {tuple(round(x, 6) + 0.0 for x in chi_edges)} = chi_3 + chi_3'. The operator commutes
    with it; the frame pattern carries 3 and sits in the LOWER triplet.

E5. STRETCH CONTROL (one class +1%):
    omega R / c = {st}
```

## Fences

```text
- Maxwell is a probe: no claim that spatial quanta produce EM; no
  observable channel (06 quarantine applies to any future one).
- omega^2 is helicity-blind; the curl sign is tested smoothly (E2) only.
- one coarse mesh: a benchmark, not a convergence result.
- H^1 = 0: harmonic modes are not validated here; the periodic solver
  owes gates G3a-G3c (maxwell_torus_calibration_056).
- unsigned circumcentric weights: valid for the regular mesh and small
  perturbations only.
```

## Ledger

```text
derivation:  maxwell_regular_mesh_056
satisfies:   maxwell_regular_mesh_reproduction_056
opens:       maxwell_torus_calibration_056
depends on:  regge_delaunay_bridge_039
smooth field: Anonymous [@WhatMathMeans], manuscript circulated as page
             images on X, 23 November 2026 (pp. 1, 25-26)
discrete calc first done in: 09_maxwell_probe/scratch_2026-11-23/
             cell_check.py (Astra session)
```
"""
    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[INFO] report written: {REPORT_PATH}")


def main() -> None:
    header("Derivation 056: The Maxwell Probe's Regular-Mesh Benchmark")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    failures: list = []
    v, adj, edges, faces, tets, dirs, em = experiment_1_group_and_mesh(failures)
    experiment_2_smooth(v, edges, failures)
    B, omega, K, M = experiment_3_discrete(v, edges, faces, tets, dirs, em, failures)
    chi_edges = experiment_4_symmetry(v, dirs, K, M, omega, failures)
    omega_stretch = experiment_5_stretch(B, faces, tets, em, failures)

    header("Verdict")
    if failures:
        for f in failures:
            print(f"  FAILED: {f}")
        raise SystemExit("Derivation 056: verification failure")
    print("  Benchmark delivered: the instrument recovers the known mode's")
    print("  pattern and frequency on the regular reference mesh, symmetry")
    print("  accounts for the triplets, and a controlled deformation splits")
    print("  them. Periodic calibration (torus gates G3a-G3c) opened.")

    record(ns)
    write_report(omega, omega_stretch, chi_edges)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
