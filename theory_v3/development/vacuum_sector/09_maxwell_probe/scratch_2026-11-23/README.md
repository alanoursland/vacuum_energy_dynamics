# Scratch Scripts (2026-11-23)

Exploratory scripts from the Astra session, kept verbatim for
provenance. They are **not** forge modules: no archive records, no
governance claims. Derivation 056 is the forge port of `cell_check.py`.

```text
cell_check.py       600-cell quotient Maxwell spectrum + 1% stretch
                    control                        -> cell_output.txt
virial_check.py     051 E1 rerun: E/N, traceless extension fabric Q,
                    orientation reversal, virial W -> packing_output.txt
                    (writes Q80.npy, Q160.npy, Q320.npy)
mode_proxy.py       Q mapped to edge scales on the quotient; spectrum
                                                   -> proxy_output.txt
eval_packing.py     original packing-only variant, superseded by
                    virial_check.py
README_original.md  the scripts' own README
```

## Running

Python 3 with NumPy and SciPy. Run from this directory with a checkout
of this repository at `./ved_read` (a symlink works). The reference
commit is `dc1d7aae3393f62be761e34d90997f176ffd3c76`.

```text
python cell_check.py
OPENBLAS_NUM_THREADS=1 python virial_check.py
python mode_proxy.py
```

`OPENBLAS_NUM_THREADS=1` keeps the relaxation bit-reproducible.

## Rerun

2026-11-23: an independent rerun of all three scripts on commit
`d0c4c23` (NumPy 2.5.3, SciPy 1.18.1; `vacuum_forge/` unchanged since
`dc1d7aa`) reproduced `cell_output.txt`, `packing_output.txt` and
`proxy_output.txt` byte for byte.

## Caution

The unsigned circumcentric distances in `cell_check.py` and
`mode_proxy.py` are valid only for small perturbations of regular
tetrahedra. Do not reuse them as general signed Hodge stars on
arbitrary meshes.
