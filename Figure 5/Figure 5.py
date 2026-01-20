# -*- coding: utf-8 -*-
"""
Figure for Pathway 2: Knowledge Diffusion & Spatial Clustering (Macro Evidence)
This figure illustrates the "point → cluster → network" evolution based on aggregate indicators.

Author: [Your Name]
Date: 2025-12-10
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import os

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
os.makedirs('figures', exist_ok=True)

def save_plot(fig, filename):
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
    plt.show()
    plt.close(fig)

def add_calendar_year_axis(ax):
    ax.set_xlabel('Time Step', fontsize=16)
    secax = ax.secondary_xaxis('top')
    secax.set_xlabel('Calendar Year', fontsize=16, color='darkred')
    year_ticks = np.arange(0, 501, 100)
    year_labels = [str(2018 + int(t // 12)) for t in year_ticks]
    secax.set_ticks(year_ticks)
    secax.set_xticklabels(year_labels, color='darkred', fontsize=14)

# Load data from local CSV file in the same directory
df = pd.read_csv('smart-green-manufacturing-data-v8.0.csv')

df['GreenCoverage'] = df['GreenZones'] / 1089

stages = {
    0: ('Initial\n(20% green)', 'black'),
    100: ('Preliminary\n(40% green)', 'blue'),
    300: ('Island Formation\n(60% green)', 'green'),
    500: ('Network Ubiquity\n(>80% green)', 'red')
}

fig, axes = plt.subplots(1, 3, figsize=(21, 8))
fig.suptitle('Figure X: Macro Evidence of Pathway 2 – Knowledge Diffusion and Cluster Proliferation\n'
             r'(Point $\rightarrow$ Cluster $\rightarrow$ Network Evolution)', 
             fontsize=20, y=0.98, weight='bold')

# (a) Green Coverage Ratio over Time
ax0 = axes[0]
ax0.plot(df['tick'], df['GreenCoverage'], color='#2ca02c', linewidth=3, label='Green Coverage')
ax0.set_ylabel('Green Coverage Ratio')
ax0.set_ylim(0, 1.05)
ax0.set_title('(a) Green Transformation Progression')
for t, (label, color) in stages.items():
    idx = df.index[df['tick'] == t][0]
    y_val = df.loc[idx, 'GreenCoverage']
    ax0.plot(t, y_val, 'o', color=color, markersize=10)

    x_offset, y_offset = 0, 0
    va_align, ha_align = 'bottom', 'center'

    if t == 0:
        x_offset, y_offset = 20, 0.08
    elif t == 100:
        y_offset = 0.04
    elif t == 300:
        x_offset, y_offset, va_align = -20, -0.06, 'top'
    elif t == 500:
        x_offset, y_offset, va_align = -35, -0.07, 'top'

    ax0.text(t + x_offset, y_val + y_offset, label,
             ha=ha_align, va=va_align, color=color, fontweight='bold',
             fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=color, alpha=0.8))
add_calendar_year_axis(ax0)

# (b) Average AI Generation vs. Green Coverage Ratio
ax1 = axes[1]
ax1.scatter(df['GreenCoverage'], df['AvgAIGen'], c=df['tick'], cmap='viridis', s=60, alpha=0.8)
ax1.set_xlabel('Green Coverage Ratio')
ax1.set_ylabel('Average AI Generation')
ax1.set_title('(b) AI–Green Co-evolution')
z = np.polyfit(df['GreenCoverage'], df['AvgAIGen'], 2)
p = np.poly1d(z)
ax1.plot(df['GreenCoverage'], p(df['GreenCoverage']), "r--", linewidth=2, label='Trend')
ax1.legend()

# (c) AI Manufacturer Count over Time
ax2 = axes[2]
ax2.plot(df['tick'], df['NumAIFactories'], color='#1f77b4', linewidth=3, label='AI Manufacturers')
ax2.set_ylabel('Number of AI Manufacturers')
ax2.set_title('(c) S-curve Adoption Reflecting Cluster Growth')
for t, (label, color) in stages.items():
    idx = df.index[df['tick'] == t][0]
    y_val = df.loc[idx, 'NumAIFactories']
    ax2.plot(t, y_val, 'o', color=color, markersize=10)

    x_offset, y_offset = 0, 0
    va_align = 'bottom'

    if t == 0:
        x_offset, y_offset = 20, 35
    elif t == 100:
        x_offset, y_offset = 20, 30
    elif t == 300:
        x_offset, y_offset = 20, 30
    elif t == 500:
        x_offset, y_offset, va_align = -35, -35, 'top'

    ax2.text(t + x_offset, y_val + y_offset, label,
             ha='center', va=va_align, color=color, fontweight='bold',
             fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=color, alpha=0.8))
add_calendar_year_axis(ax2)

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
save_plot(fig, 'fig_pathway2_macro_evidence')
print("Figure for Pathway 2 successfully generated and saved.")
