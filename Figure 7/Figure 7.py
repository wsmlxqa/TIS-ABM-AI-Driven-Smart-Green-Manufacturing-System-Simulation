import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==================== Journal-quality settings ====================
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False
os.makedirs('figures', exist_ok=True)

def save_plot(fig, filename):
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
    plt.show()
    plt.close(fig)

# Load data
df = pd.read_csv('pathway3_svi_demand_data.csv')

# Sort by SVI
df = df.sort_values('SVI').reset_index(drop=True)
x = df['SVI'].values
y = df['Demand'].values

# Compute first derivative (local slope)
d_y = np.diff(y)
d_x = np.diff(x)
d_x = np.where(d_x == 0, 1e-8, d_x)
slope = d_y / d_x  # ΔDemand / ΔSVI

# Compute second derivative (change in slope)
acc = np.diff(slope) / np.diff(x[:-1])  # Δslope / ΔSVI
acc = np.where(acc == 0, 1e-8, acc)  # avoid division by zero

# Find index where acceleration is maximum (most positive)
max_acc_idx = np.argmax(acc)

# Threshold is the SVI value at that point
threshold_svi = x[max_acc_idx + 1]  # +1 because acc[i] corresponds to change between i and i+1

print(f"🔍 Automatically detected critical threshold at SVI = {threshold_svi:.4f}")
print(f"   Max acceleration: {acc[max_acc_idx]:.2f}")

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(df['SVI'], df['Demand'], 'o-', color='#d62728', linewidth=2.5, markersize=6, label='Market Demand')
ax.fill_between(df['SVI'], df['Demand'], color='#d62728', alpha=0.15)

# Vertical line at inferred threshold
ax.axvline(x=threshold_svi, color='gray', linestyle='--', linewidth=1.8, alpha=0.8)

# Annotate threshold
y_pos = ax.get_ylim()[1] * 0.65
ax.text(threshold_svi + 0.015, y_pos, 'Critical\nThreshold',
        rotation=90, va='center', color='gray', fontsize=13,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.8))

# Labels and title
ax.set_xlabel('System Value Index (SVI)', fontsize=16)
ax.set_ylabel('Market Demand', fontsize=16)
ax.set_title('Nonlinear Demand Response to Systemic Value\n(Pattern P2: Value-Driven Demand Emergence)',
             fontsize=16, fontweight='bold', pad=15)

ax.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

fig.tight_layout()
save_plot(fig, 'fig_pathway3_svi_demand')

print("✅ Figure 7 generated with data-driven threshold.")

