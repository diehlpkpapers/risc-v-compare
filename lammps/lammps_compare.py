bench_colors = ['#4E79A7',  # Blue
                '#F28E2B',  # Orange
                '#E15759',  # Red
                '#76B7B2',  # Teal
                '#59A14F',  # Green
                '#EDC948',  # Yellow
                '#AF7AA1',  # Violet
                '#FF9DA7',  # Soft Pink/Coral
                '#3B5D5C',  # Dark Slate Teal
                '#B03A48']  # Rich Dark Rose

import matplotlib.pyplot as plt
import numpy as np

# Example data
ranks = ["1-rank", "2-rank", "4-rank"]
cpu_cores = ["Banana Pi", "Rocket", "MILK-V", "BOOM"]

# Lammps Runtimes for LJ benchmark
values = np.array([
    # Chain["Banana Pi", "Rocket", "MILK-V", "BOOM"],
    [100, 55, 4, 21],   # 1-rank
    [100, 28, 2, 11],   # 2-rank
    [100, 15, 1, 5]    # 4-rank
])

# Lammps Runtimes for Chain benchmark
values = np.array([
    # Chain["Banana Pi", "Rocket", "MILK-V", "BOOM"],
    [100, 28, 4, 13],   # 1-rank
    [100, 18, 2, 9],   # 2-rank
    [100, 12, 1, 7]    # 4-rank
])

# Parameters
n_ranks = len(ranks)
n_cpu_cores = len(cpu_cores)
bar_width = 0.2
x = np.arange(n_ranks)

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
for i in range(n_cpu_cores):
    offsets = x + (i - (n_cpu_cores - 1) / 2) * bar_width
    bars = ax.bar(offsets, values[:, i], width=bar_width, label=cpu_cores[i])   
    # Label each bar
    # for bar, val in zip(bars, values[:, i]):
    #     ax.text(bar.get_x() + bar.get_width()/2, val + 1, f"{val}",
    #             ha='center', va='bottom', fontsize=8)

# Styling
ax.set_title("UME runtimes for different MPI ranks on FireSim simulation, Banana Pi, and MILK-V")
ax.set_ylabel("Runtime (Seconds)")
ax.set_xticks(x)
ax.set_xticklabels(ranks)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('UME_results.pdf', format='pdf')
# plt.savefig('Lammps_results.pdf', format='pdf')
plt.show()
