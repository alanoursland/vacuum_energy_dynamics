"""Figure 1: the family A_lambda(r), with horizon zeros marked.

Grayscale-safe: identity is carried by line style and direct labels,
never by color alone. Members with lambda < 0 terminate at A = 0
(horizons, at r = -lambda r_s); members with lambda >= 0 stay positive
for all r > 0.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "md" / "figure_1_family.png"

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


fig, ax = plt.subplots(figsize=(3.4, 2.55), dpi=300)

R_MAX = 4.0

# lambda < 0: draw down to the horizon r_h = -lambda (in units of r_s).
r = np.linspace(1.0, R_MAX, 400)
ax.plot(r, A(-1.0, 1.0 / r), "k-", lw=1.4, label=r"$\lambda=-1$ (Schwarzschild)")
ax.plot(1.0, 0.0, "ko", ms=4.5, zorder=5)

r = np.linspace(0.25, R_MAX, 400)
ax.plot(r, A(-0.25, 1.0 / r), color="0.25", ls="--", lw=1.1,
        label=r"$\lambda=-1/4$")
ax.plot(0.25, 0.0, "o", ms=4.5, mfc="white", mec="k", mew=0.9, zorder=5)

# lambda >= 0: positive for all r > 0.
r = np.linspace(0.02, R_MAX, 600)
ax.plot(r, A(0.0, 1.0 / r), color="0.35", ls="-.", lw=1.1,
        label=r"$\lambda=0$ (exponential)")
ax.plot(r, A(1.0, 1.0 / r), color="0.45", ls=":", lw=1.3,
        label=r"$\lambda=+1$ (reciprocal)")

# horizon annotations
ax.annotate("horizon at $r_s$", xy=(1.0, 0.0), xytext=(1.45, 0.035),
            fontsize=7, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))
ax.annotate(r"horizon at $r_s/4$", xy=(0.25, 0.0), xytext=(0.52, 0.115),
            fontsize=7, ha="left",
            arrowprops=dict(arrowstyle="-", lw=0.6, color="0.2"))

ax.axhline(0.0, color="0.75", lw=0.5, zorder=0)

ax.set_xlim(0.0, R_MAX + 0.06)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_ylim(-0.04, 1.04)
ax.set_xlabel(r"$r/r_s$")
ax.set_ylabel(r"$A_\lambda(r)$")
ax.legend(loc="upper left", frameon=False, fontsize=7, handlelength=2.4,
          borderaxespad=0.4)

fig.tight_layout(pad=0.3)
fig.savefig(OUT)
print(f"wrote {OUT}")
