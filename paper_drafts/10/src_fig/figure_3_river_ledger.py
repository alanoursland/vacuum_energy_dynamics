"""Figure 3: the Painleve-Gullstrand river profiles v(r)/c for the
family, against the Newtonian free-fall profile.

v_lambda(r) = c sqrt(1 - A_lambda(r)) family-wide. The Newtonian
profile sqrt(r_s/r) is drawn as a wide light underlay; the
lambda = -1 curve rides it exactly at every radius — that coincidence
is the figure's point. Members with lambda < 0 reach v = c at their
horizons (dots); members with lambda >= 0 never do.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "md" / "figure_3_river_ledger.png"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.linewidth": 0.6,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.top": True,
    "ytick.right": True,
})


def A(lam, x):
    if lam == 0.0:
        return np.exp(-x)
    return (1.0 + lam * x) ** (-1.0 / lam)


def v(lam, r):
    return np.sqrt(1.0 - A(lam, 1.0 / r))


fig, ax = plt.subplots(figsize=(3.4, 2.55), dpi=300)

R_MAX = 6.0

# Newtonian profile, continued past v = c to show Michell's premise
r = np.linspace(0.62, R_MAX, 600)
ax.plot(r, np.sqrt(1.0 / r), color="0.8", lw=3.2, solid_capstyle="round",
        zorder=1, label=r"Newtonian $\sqrt{2GM/c^2 r}$")

# lambda = -1 rides the Newtonian curve exactly; ends at its horizon
r = np.linspace(1.0, R_MAX, 400)
ax.plot(r, v(-1.0, r), "k-", lw=1.2, zorder=3,
        label=r"$\lambda=-1$ (Schwarzschild)")
ax.plot(1.0, 1.0, "ko", ms=4.5, zorder=6)

r = np.linspace(0.25, R_MAX, 500)
ax.plot(r, v(-0.25, r), color="0.25", ls="--", lw=1.1, zorder=3,
        label=r"$\lambda=-1/4$")
ax.plot(0.25, 1.0, "o", ms=4.5, mfc="white", mec="k", mew=0.9, zorder=6)

r = np.linspace(0.12, R_MAX, 600)
ax.plot(r, v(0.0, r), color="0.35", ls="-.", lw=1.1, zorder=3,
        label=r"$\lambda=0$ (exponential)")
ax.plot(r, v(1.0, r), color="0.45", ls=":", lw=1.3, zorder=3,
        label=r"$\lambda=+1$ (reciprocal)")

# v = c line
ax.axhline(1.0, color="0.6", lw=0.6, ls=(0, (5, 3)), zorder=2)

ax.annotate(r"$v=c$ at $r_s$", xy=(1.0, 1.0), xytext=(1.55, 1.10),
            fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))

ax.set_xlim(0.0, R_MAX)
ax.set_ylim(0.0, 1.28)
ax.set_xlabel(r"$r/r_s$")
ax.set_ylabel(r"river speed $v(r)/c$")
leg = ax.legend(loc="upper right", frameon=True, fontsize=7,
                handlelength=2.4, borderaxespad=0.4, framealpha=1.0,
                edgecolor="none", facecolor="white")
leg.set_zorder(10)

fig.tight_layout(pad=0.3)
fig.savefig(OUT)
print(f"wrote {OUT}")
