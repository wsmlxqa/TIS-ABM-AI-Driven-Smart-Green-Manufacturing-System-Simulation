# -*- coding: utf-8 -*-
"""
Title: AI-driven Transformation in Smart Manufacturing Systems
Description: Replication code for Figure \label{fig:e1-nonlinear-comparison}
Comparison of Linear vs Exponential Upgrade Costs (Patterns P1–P4)
Data Sources: linear_cost.csv, exponential_cost.csv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==================== Global Settings for Journal Publication ====================
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 3.0
plt.rcParams['lines.dash_capstyle'] = 'round'

# CSV File Paths
LINEAR_CSV = "linear_cost.csv"
EXP_CSV    = "exponential_cost.csv"

TOTAL_PATCHES = 1089

# ==================== Helper Functions ====================
def load_data():
    """Load and preprocess simulation results."""
    df_linear = pd.read_csv(LINEAR_CSV)
    df_exp    = pd.read_csv(EXP_CSV)
    for df in [df_linear, df_exp]:
        df[:] = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    return df_linear, df_exp


def add_year_axis(ax):
    """Add Time Step and secondary Calendar Year axis to the plot."""
    ax.set_xlabel('Time Step', fontsize=18)
    
    secax = ax.secondary_xaxis('top')
    secax.set_xlabel('Calendar Year', fontsize=18, color='darkred')
    year_ticks = np.arange(0, 501, 60)
    year_labels = [str(2018 + int(t // 12)) for t in year_ticks]
    secax.set_ticks(year_ticks)
    secax.set_xticklabels(year_labels, color='darkred', fontsize=15)
    
    # 2030 & 2060 Policy Milestones
    for tick, label in {144: '2030 Carbon Peak', 504: '2060 Carbon Neutrality'}.items():
        if tick <= 500:
            ax.axvline(x=tick, color='gray', linestyle='--', lw=1.4, alpha=0.75)
            ax.text(tick, ax.get_ylim()[1]*0.92, label,
                    ha='center', va='top', color='gray', fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.85))


# ==================== Main Plotting Function ====================
def plot_all_patterns_combined():
    """Generates the unified 4-panel figure comparing Linear and Exponential cost regimes."""
    print("Loading data and generating Figure E.1...")
    df_linear, df_exp = load_data()
    
    fig = plt.figure(figsize=(20, 14))
    
    # 2x2 Grid Layout
    gs = fig.add_gridspec(2, 2, hspace=0.38, wspace=0.32)
    
    # ---------------- (a) P1: Average AI Generation ----------------
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(df_linear['tick'], df_linear['AvgAIGen'], color='#6a0dad', label='Linear', solid_capstyle='round')
    ax1.plot(df_exp['tick'],    df_exp['AvgAIGen'],    color='#ba55d3', linestyle='--', dashes=(6,3), label='Exponential')
    ax1.fill_between(df_linear['tick'], df_linear['AvgAIGen'], alpha=0.08, color='#6a0dad')
    ax1.fill_between(df_exp['tick'],    df_exp['AvgAIGen'],    alpha=0.05, color='#ba55d3')
    ax1.set_ylabel('Average AI Generation', fontsize=18)
    ax1.set_ylim(0.9, 4.5)
    ax1.set_title('(a) P1: Firm-level Efficiency Optimization', fontsize=20, pad=18)
    ax1.legend(loc='lower right', frameon=True, fancybox=True, shadow=True, fontsize=14)
    add_year_axis(ax1)
    
    # ---------------- (b) P2: Number of AI Manufacturers ----------------
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(df_linear['tick'], df_linear['NumAIFactories'], color='#1f77b4', label='Linear')
    ax2.plot(df_exp['tick'],    df_exp['NumAIFactories'],    color='#4c8bf5', linestyle='--', dashes=(6,3), label='Exponential')
    ax2.fill_between(df_linear['tick'], df_linear['NumAIFactories'], alpha=0.08, color='#1f77b4')
    ax2.set_ylabel('Number of AI Manufacturers', fontsize=18)
    ax2.set_title('(b) P2: Knowledge Diffusion & Spatial Clustering', fontsize=20, pad=18)
    ax2.legend(loc='lower right', frameon=True, fancybox=True, shadow=True, fontsize=14)
    add_year_axis(ax2)
    
    # ---------------- (c) P3: Market Demand ----------------
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.plot(df_linear['tick'], df_linear['Demand'], color='#d62728', label='Linear')
    ax3.plot(df_exp['tick'],    df_exp['Demand'],    color='#ff7f7f', linestyle='--', dashes=(6,3), label='Exponential')
    ax3.fill_between(df_linear['tick'], df_linear['Demand'], alpha=0.08, color='#d62728')
    ax3.set_ylabel('Market Demand', fontsize=18)
    ax3.set_title('(c) P3: System-level Value Creation & Demand Takeoff', fontsize=20, pad=18)
    ax3.legend(loc='upper left', bbox_to_anchor=(0, 0.85), frameon=True, fancybox=True, shadow=True, fontsize=14)
    add_year_axis(ax3)
    
    # ---------------- (d) P4: Institutional Feedback & Resilience ----------------
    ax4 = fig.add_subplot(gs[1, 1])
    # Gov Budget
    ax4.plot(df_linear['tick'], df_linear['GovBudget'], color='#6a0dad', lw=3.2, label='Linear (Gov Budget)')
    ax4.plot(df_exp['tick'],    df_exp['GovBudget'],    color='#ba55d3', linestyle='--', dashes=(8,4), lw=3.8, label='Exponential (Gov Budget)')
    ax4.fill_between(df_linear['tick'], df_linear['GovBudget'], alpha=0.06, color='#6a0dad')
    
    ax4_2 = ax4.twinx()
    # Green Coverage
    ax4_2.plot(df_linear['tick'], df_linear['GreenZones']/TOTAL_PATCHES, color='#2ca02c', lw=2.8, alpha=0.9, label='Linear (Green Coverage)')
    ax4_2.plot(df_exp['tick'],    df_exp['GreenZones']/TOTAL_PATCHES,    color='#66c266', linestyle='--', dashes=(6,3), lw=2.8, alpha=0.9, label='Exponential (Green Coverage)')
    ax4_2.fill_between(df_linear['tick'], df_linear['GreenZones']/TOTAL_PATCHES, alpha=0.05, color='#2ca02c')
    
    ax4.set_ylabel('Government Budget Balance', fontsize=18, color='#6a0dad')
    ax4_2.set_ylabel('Green Coverage Ratio', fontsize=18, color='#2ca02c')
    ax4.set_title('(d) P4: Institutional Feedback & Resilience', fontsize=20, pad=18)
    
    # Combined legend for the dual-axis plot
    lines1, labels1 = ax4.get_legend_handles_labels()
    lines2, labels2 = ax4_2.get_legend_handles_labels()
    ax4.legend(lines1 + lines2, labels1 + labels2, loc='lower center', 
               bbox_to_anchor=(0.5, -0.22), ncol=2, frameon=True, fancybox=True, shadow=True, fontsize=13)
    
    add_year_axis(ax4)
    
    # Final Adjustments
    plt.tight_layout(rect=[0, 0.03, 1, 0.94])
    
    # Exporting
    filename = "fig_e1_comparison_results"
    plt.savefig(f'{filename}.png', bbox_inches='tight', dpi=300)
    plt.savefig(f'{filename}.pdf', bbox_inches='tight')
    print(f"Success: Figure saved as {filename}.png and {filename}.pdf")
    plt.show()

if __name__ == "__main__":
    plot_all_patterns_combined()