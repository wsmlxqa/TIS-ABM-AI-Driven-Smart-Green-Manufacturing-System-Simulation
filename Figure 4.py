# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==================== Global Settings for Journal-Ready Plots ====================
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False
os.makedirs('figures', exist_ok=True)  # Create folder to store figures

# ==================== Helper Function: Save Plot in Journal Format ====================
def save_plot(fig, filename):
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')  # PDF format for submission
    plt.show()
    plt.close(fig)

# ==================== Helper Function: Add Calendar Year Axis + Policy Nodes ====================
def add_calendar_year_axis(ax):
    ax.set_xlabel('Time Step', fontsize=16)
    
    # Top red axis: mapping time steps to real calendar years
    secax = ax.secondary_xaxis('top')
    secax.set_xlabel('Calendar Year', fontsize=16, color='darkred')
    year_ticks = np.arange(0, 501, 60)  # Tick every 5 years
    year_labels = [str(2018 + int(t // 12)) for t in year_ticks]  # 1 time step = 1 month
    secax.set_ticks(year_ticks)
    secax.set_xticklabels(year_labels, color='darkred', fontsize=14)
    
    # Highlight policy milestones: Carbon Peak (2030) and Carbon Neutrality (2060)
    policy_nodes = {144: '2030\nCarbon Peak', 504: '2060\nCarbon Neutrality'}
    for tick, label in policy_nodes.items():
        if tick <= 500:  # Only show if within simulation range
            ax.axvline(x=tick, color='gray', linestyle='--', linewidth=1.5, alpha=0.8)
            ax.text(tick, ax.get_ylim()[1]*0.96, label,
                    ha='center', va='top', color='gray', fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9))

# ==================== Core Function: Generate Figure 1 with Pathway 1 Highlights ====================
def figure_1_baseline_evolution_optimized():
    print("Generating Optimized Figure 1 with Pathway 1 Highlights...")

    # 1. Load dataset (assumed to be in the same directory)
    df = pd.read_csv('smart-green-manufacturing-data-v8.0.csv')

    # 2. Create 2×3 subplot layout
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle('Figure 1: Baseline Evolution of Key Indicators (Pathway 1 Focus)\n'
                 'Note: Each time step = 1 month (Jan 2018 – Aug 2059); Core indicators of Pathway 1 highlighted',
                 fontsize=20, y=0.98, color='darkred', weight='bold')

    # (a) Manufacturer Count — S-Curve Adoption (Pathway 1 Core)
    axes[0,0].plot(df['tick'], df['NumAIFactories'], color='#1f77b4', linewidth=3.5, label='Manufacturers')
    axes[0,0].fill_between(df['tick'], df['NumAIFactories'], alpha=0.3, color='#1f77b4')
    axes[0,0].set_title('(a) Manufacturer Count (S-curve Adoption)', fontweight='bold')
    axes[0,0].set_ylabel('Number of Manufacturers')
    axes[0,0].legend(loc='center left', bbox_to_anchor=(0.02, 0.5), fontsize=14, frameon=True, fancybox=True, shadow=True)
    add_calendar_year_axis(axes[0,0])

    # (b) Supplier Count — Pathway 1 Spillover Effect
    axes[0,1].plot(df['tick'], df['NumSuppliers'], color='#ff7f0e', linewidth=3.5, label='Suppliers')
    axes[0,1].fill_between(df['tick'], df['NumSuppliers'], alpha=0.3, color='#ff7f0e')
    axes[0,1].set_title('(b) Supplier Count', fontweight='bold')
    axes[0,1].set_ylabel('Number of Suppliers')
    axes[0,1].legend(loc='center left', bbox_to_anchor=(0.02, 0.5), fontsize=14, frameon=True, fancybox=True, shadow=True)
    add_calendar_year_axis(axes[0,1])

    # (c) Green Coverage Ratio — Pathway 1 Acceleration
    green_ratio = df['GreenZones'] / 1089  # 33×33 grid patches = 1089
    axes[0,2].plot(df['tick'], green_ratio, color='#2ca02c', linewidth=3.5, label='Green Coverage')
    axes[0,2].fill_between(df['tick'], green_ratio, alpha=0.3, color='#2ca02c')
    axes[0,2].set_title('(c) Green Coverage Rate (Pathway 1 Core)', fontweight='bold', color='#2ca02c')
    axes[0,2].set_ylabel('Green Coverage Ratio')
    axes[0,2].set_ylim(0, 1.05)
    axes[0,2].legend(loc='lower right', bbox_to_anchor=(0.98, 0.02), fontsize=14, frameon=True, fancybox=True, shadow=True)
    axes[0,2].text(0.02, 0.78, 'Pathway 1\nGreen Acceleration', transform=axes[0,2].transAxes, 
                   ha='left', va='top', fontsize=12, color='red',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))
    add_calendar_year_axis(axes[0,2])

    # (d) Average AI Generation — Efficiency Driver
    axes[1,0].plot(df['tick'], df['AvgAIGen'], color='#9467bd', linewidth=3.5, label='Average AI Generation')
    axes[1,0].fill_between(df['tick'], df['AvgAIGen'], alpha=0.3, color='#9467bd')
    axes[1,0].set_title('(d) Average AI Generation (Efficiency Driver)', fontweight='bold', color='#9467bd')
    axes[1,0].set_ylabel('AI Generation')
    axes[1,0].legend(loc='center left', bbox_to_anchor=(0.02, 0.6), fontsize=14, frameon=True, fancybox=True, shadow=True)
    axes[1,0].text(0.45, 0.95, 'Pathway 1\nEfficiency Optimization', transform=axes[1,0].transAxes, 
                   ha='left', va='top', fontsize=12, color='red',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))
    add_calendar_year_axis(axes[1,0])

    # (e) Relative Energy Intensity — Efficiency Proxy
    energy_intensity = 1 / (df['AvgAIGen'] + 0.1)
    axes[1,1].plot(df['tick'], energy_intensity, color='#d62728', linewidth=3.5, label='Relative Energy Intensity')
    axes[1,1].fill_between(df['tick'], energy_intensity, alpha=0.3, color='#d62728')
    axes[1,1].set_title('(e) Relative Energy Intensity (Efficiency Proxy)', fontweight='bold', color='#d62728')
    axes[1,1].set_ylabel('Relative Energy Intensity')
    axes[1,1].legend(fontsize=14, frameon=True, fancybox=True, shadow=True)
    add_calendar_year_axis(axes[1,1])

    # (f) Market Price — Cost Efficiency Reflection
    axes[1,2].plot(df['tick'], df['MarketPrice'], color='#8c564b', linewidth=3.5, label='Market Price')
    axes[1,2].fill_between(df['tick'], df['MarketPrice'], alpha=0.3, color='#8c564b')
    axes[1,2].set_title('(f) Market Price (Cost Efficiency Reflection)', fontweight='bold')
    axes[1,2].set_ylabel('Market Price')
    axes[1,2].legend(loc='upper right', bbox_to_anchor=(0.88, 0.98), fontsize=14, frameon=True, fancybox=True, shadow=True)
    add_calendar_year_axis(axes[1,2])

    # Final layout adjustment to prevent overlap
    plt.tight_layout(rect=[0, 0.02, 1, 0.93])

    # Save as high-quality PNG and PDF
    save_plot(fig, 'fig1_baseline_evolution_pathway1_optimized')
    print("Optimized Figure 1 generated and saved to 'figures' folder.")

# ==================== Main Execution ====================
if __name__ == "__main__":
    figure_1_baseline_evolution_optimized()
