import matplotlib.pyplot as plt
import numpy as np

# Example data
ranks = ["1-rank", "2-rank", "4-rank"]
cpu_cores = ["Banana Pi", "Rocket", "MILK-V", "BOOM"]

# Ume Runtimes
values = np.array([
    # ["Banana Pi", "Rocket", "MILK-V", "BOOM"]
    [0.7328, 1.0030, 0.1537, 0.4890],   # 1-rank
    [0.4017, 0.5550, 0.0272, 0.2763],   # 2-rank
    [0.2147, 0.3142, 0.0158, 0.1502]    # 4-rank
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
