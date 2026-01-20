import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Configure plot style for publication-quality figures
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False
os.makedirs('figures', exist_ok=True)

def save_plot(fig, filename):
    """Save figure in high-resolution PNG and vector PDF formats."""
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
    plt.close(fig)

def add_calendar_year_axis(ax):
    """Add secondary x-axis showing calendar years and annotate policy milestones."""
    ax.set_xlabel('Time Step')

    secax = ax.secondary_xaxis('top')
    secax.set_xlabel('Calendar Year', color='darkred')
    
    year_ticks = np.arange(0, 501, 60)
    year_labels = [str(2018 + int(t // 12)) for t in year_ticks]
    secax.set_ticks(year_ticks)
    secax.set_xticklabels(year_labels, color='darkred', fontsize=14)

    milestones = {144: '2030\nCarbon Peak', 504: '2060\nCarbon Neutrality'}
    for tick, label in milestones.items():
        if tick <= 500:
            ax.axvline(x=tick, color='gray', linestyle='--', linewidth=1.5, alpha=0.8)
            ax.text(
                tick, ax.get_ylim()[1] * 0.96, label,
                ha='center', va='top', color='gray', fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9)
            )

def figure_8_market_responsiveness():
    """Generate revised Figure 8 comparing high vs. low market responsiveness (β)."""
    # Load simulation data from local directory
    df_high = pd.read_csv('data_β_high.csv')
    df_low = pd.read_csv('data_β_low.csv')

    # Ensure numeric data
    df_high = df_high.apply(pd.to_numeric, errors='coerce').fillna(0)
    df_low = df_low.apply(pd.to_numeric, errors='coerce').fillna(0)

    fig, axes = plt.subplots(1, 3, figsize=(21, 6.5))
    fig.suptitle(
        'Impact of Market Responsiveness to Systemic Value (β) on Smart Manufacturing Transformation',
        fontsize=20, y=0.98
    )

    # (a) Market Demand
    ax0 = axes[0]
    ax0.plot(df_high['tick'], df_high['Demand'], label=r'High Responsiveness ($\beta=2.0$)', color='red', linewidth=3)
    ax0.plot(df_low['tick'], df_low['Demand'], label=r'Low Responsiveness ($\beta=1.0$)', color='blue', linewidth=3)
    ax0.set_title('(a) Market Demand Trajectory')
    ax0.set_ylabel('Market Demand')
    ax0.legend(fontsize=14)
    add_calendar_year_axis(ax0)

    # (b) Average AI Generation Level
    ax1 = axes[1]
    ax1.plot(df_high['tick'], df_high['AvgAIGen'], label=r'High Responsiveness ($\beta=2.0$)', color='red', linewidth=3)
    ax1.plot(df_low['tick'], df_low['AvgAIGen'], label=r'Low Responsiveness ($\beta=1.0$)', color='blue', linewidth=3)
    ax1.set_title('(b) Average AI Generation Level')
    ax1.set_ylabel('Average AI Generation')
    ax1.legend(fontsize=14)
    add_calendar_year_axis(ax1)

    # (c) Price-Supply Scatter
    ax2 = axes[2]
    ax2.scatter(df_high['Supply'], df_high['MarketPrice'], alpha=0.7, s=15, color='red', label=r'High $\beta$')
    ax2.scatter(df_low['Supply'], df_low['MarketPrice'], alpha=0.7, s=15, color='blue', label=r'Low $\beta$')
    ax2.set_title('(c) Price–Supply Dynamics')
    ax2.set_xlabel('Total Supply')
    ax2.set_ylabel('Market Price')
    ax2.legend(fontsize=14)

    plt.tight_layout(rect=[0, 0.02, 1, 0.94])
    save_plot(fig, 'fig8_market_responsiveness_revised')

if __name__ == "__main__":
    figure_8_market_responsiveness()

