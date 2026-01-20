import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Publication-ready plotting configuration
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False
os.makedirs('figures', exist_ok=True)

def save_plot(fig, filename):
    """Save figure in both high-resolution PNG and vector PDF formats."""
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
    plt.close(fig)

def add_year_axis_and_milestones(ax, shock_tick=200):
    """Add top calendar-year axis, policy milestones, and shock annotation."""
    ax.set_xlabel('Time Step')

    # Secondary x-axis: Calendar Year
    secax = ax.secondary_xaxis('top')
    secax.set_xlabel('Calendar Year', color='darkred')
    year_ticks = np.arange(0, 501, 60)
    year_labels = [str(2018 + int(t // 12)) for t in year_ticks]
    secax.set_ticks(year_ticks)
    secax.set_xticklabels(year_labels, color='darkred', fontsize=14)

    # Policy milestones: 2030 (t=144), 2060 (t=504)
    milestones = {144: '2030\nCarbon Peak', 504: '2060\nCarbon Neutrality'}
    for tick, label in milestones.items():
        if tick <= 500:
            ax.axvline(x=tick, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
            ax.text(
                tick, ax.get_ylim()[1] * 0.56, label,
                ha='center', va='top', color='gray', fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9)
            )

    # External shock annotation (t=200 ≈ 2034)
    ax.axvline(x=shock_tick, color='black', linestyle='-', linewidth=2.5, alpha=0.9)
    ax.text(
        shock_tick + 10, ax.get_ylim()[1] * 0.92, 'External Shock\n(≈2034)',
        ha='left', va='top', color='black', fontsize=13, weight='bold',
        bbox=dict(boxstyle="round,pad=0.4", facecolor="yellow", edgecolor="black", alpha=0.3)
    )

def figure_9_shock_response():
    """Generate final version of Figure 9 for journal submission."""
    # Load data from current directory
    df_normal = pd.read_csv('data_normal.csv')
    df_shock = pd.read_csv('data_with_shock.csv')

    # Ensure numeric data
    df_normal = df_normal.apply(pd.to_numeric, errors='coerce').fillna(0)
    df_shock = df_shock.apply(pd.to_numeric, errors='coerce').fillna(0)

    total_patches = 1089

    fig = plt.figure(figsize=(16, 11))
    fig.suptitle(
        'Figure 9: System Resilience and Recovery Capability under External Shock\n'
        'Note: Each time step = 1 month (Jan 2018 – Aug 2059); Major external shock occurs at t=200 (≈2034)',
        fontsize=19, y=0.97, color='darkred', weight='bold'
    )

    axes = fig.subplots(2, 2)

    # (a) Manufacturer Recovery Capability
    ax0 = axes[0, 0]
    ax0.plot(df_normal['tick'], df_normal['NumAIFactories'], label='Without Shock', color='blue', linewidth=3)
    ax0.plot(df_shock['tick'], df_shock['NumAIFactories'], label='With Shock', color='red', linewidth=3)
    ax0.set_title('(a) Manufacturer Recovery Capability', fontsize=17, pad=12)
    ax0.set_ylabel('Number of Manufacturers')
    ax0.legend(fontsize=13)
    add_year_axis_and_milestones(ax0, shock_tick=200)

    # (b) Green Area Stability
    ax1 = axes[0, 1]
    ax1.plot(df_normal['tick'], df_normal['GreenZones'] / total_patches, label='Without Shock', color='blue', linewidth=3)
    ax1.plot(df_shock['tick'], df_shock['GreenZones'] / total_patches, label='With Shock', color='red', linewidth=3)
    ax1.set_title('(b) Green Area Stability', fontsize=17, pad=12)
    ax1.set_ylabel('Green Coverage Ratio')
    ax1.set_ylim(0, 1)
    ax1.legend(fontsize=13)
    add_year_axis_and_milestones(ax1, shock_tick=200)

    # (c) Market Price Fluctuation
    ax2 = axes[1, 0]
    ax2.plot(df_normal['tick'], df_normal['MarketPrice'], label='Without Shock', color='blue', linewidth=3, alpha=0.9)
    ax2.plot(df_shock['tick'], df_shock['MarketPrice'], label='With Shock', color='red', linewidth=3, alpha=0.9)
    ax2.set_title('(c) Market Price Fluctuation', fontsize=17, pad=12)
    ax2.set_ylabel('Market Price')
    ax2.legend(fontsize=13)
    add_year_axis_and_milestones(ax2, shock_tick=200)

    # (d) Government Budget Response
    ax3 = axes[1, 1]
    ax3.plot(df_normal['tick'], df_normal['GovBudget'], label='Without Shock', color='blue', linewidth=3)
    ax3.plot(df_shock['tick'], df_shock['GovBudget'], label='With Shock', color='red', linewidth=3)
    ax3.set_title('(d) Government Budget Response', fontsize=17, pad=12)
    ax3.set_ylabel('Budget Balance')
    ax3.legend(fontsize=13)
    add_year_axis_and_milestones(ax3, shock_tick=200)

    plt.tight_layout(rect=[0, 0.02, 1, 0.91])
    save_plot(fig, 'fig9_shock_response_final')

if __name__ == "__main__":
    figure_9_shock_response()

