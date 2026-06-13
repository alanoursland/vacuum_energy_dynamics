# 10. Verification and Reproducibility

The derivations in this note are short enough to check by hand, but each
nontrivial algebraic step also has a companion script in the project
archive. The scripts are not substitutes for mathematical judgment. Their
role is narrower and useful: they rederive the symbolic identities from
scratch and verify declared dependencies on upstream archived results.

| claim | script | role |
|---|---|---|
| static self-coupling identity and `lambda = -1` selector | `002_trial_C_burden_ledger/trial_C2_self_coupling_bootstrap.py` | derives `Delta_ar(e^s)` identity, bootstrap family, negative static energy |
| static placement / `AB = 1` compatibility | `002_trial_C_burden_ledger/trial_C3_spatial_bootstrap.py` | verifies the t-r block identity and excludes explicit scalar-source placement |
| TT positivity, ghost exclusion, source slavery | `006_gate_G03_radiative_positivity/gate_G03_radiative_positivity.py` | proves the sector-sign architecture at reduced level |
| linear underdetermination and `K_T` bootstrap | `008_radiative_bootstrap/radiative_bootstrap_KT.py` | shows linear work-flux balance cannot fix `K_T`, then fixes it by second-order self-coupling |

For a public version of the paper, the scripts should be archived with a
versioned DOI. The paper should cite the archive but remain readable
without running it. A reader should be able to follow the proof from the
main text and use the scripts only to audit algebra, signs, and dependency
claims.

The minimal reproducibility standard is:

1. the source file name and theorem label are listed;
2. the script can be run from a clean checkout;
3. the script reports dependency status;
4. the script prints or records the symbolic residuals it claims vanish;
5. the paper states which claims are script-verified and which are
   interpretive or literature-dependent.
