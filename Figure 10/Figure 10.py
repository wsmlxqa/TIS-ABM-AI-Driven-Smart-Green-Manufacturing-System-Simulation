import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Publication-quality plot settings
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False
os.makedirs('figures', exist_ok=True)

def save_plot(fig, filename):
    """Save figure in both high-resolution PNG and vector PDF formats."""
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
    plt.close(fig)

def add_year_axis_and_milestones(ax):
    """Add top calendar-year axis and annotate 2030/2060 policy milestones."""
    ax.set_xlabel('Time Step')

    secax = ax.secondary_xaxis('top')
    secax.set_xlabel('Calendar Year', color='darkred')
    year_ticks = np.arange(0, 501, 60)
    year_labels = [str(2018 + int(t // 12)) for t in year_ticks]
    secax.set_ticks(year_ticks)
    secax.set_xticklabels(year_labels, color='darkred', fontsize=14)

    # Annotate policy targets
    milestones = {144: '2030\nCarbon Peak', 504: '2060\nCarbon Neutrality'}
    for tick, label in milestones.items():
        if tick <= 500:
            ax.axvline(x=tick, color='gray', linestyle='--', linewidth=1.5, alpha=0.8)
            ax.text(
                tick, ax.get_ylim()[1] * 0.96, label,
                ha='center', va='top', color='gray', fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.9)
            )

def figure_10_policy_comparison():
    """Generate final version of Figure 10 for journal submission."""
    # Load data from current working directory
    df_static = pd.read_csv('data_policy_static.csv')
    df_dynamic = pd.read_csv('data_policy_dynamic.csv')
    df_mixed = pd.read_csv('data_policy_mixed.csv')

    # Ensure all data are numeric
    for df in [df_static, df_dynamic, df_mixed]:
        df[:] = df.apply(pd.to_numeric, errors='coerce').fillna(0)

    total_patches = 1089

    fig = plt.figure(figsize=(21, 7))
    fig.suptitle(
        'Figure 10: Comparison of Governance Effectiveness under Different Policy Regimes\n'
        'Note: Each time step = 1 month (Jan 2018 – Aug 2059); dashed lines indicate 2030 Carbon Peak and 2060 Carbon Neutrality targets',
        fontsize=19, y=0.98, color='darkred', weight='bold'
    )

    axes = fig.subplots(1, 3)

    # (a) Green Coverage Ratio
    ax0 = axes[0]
    ax0.plot(df_static['tick'], df_static['GreenZones'] / total_patches, label='Static Subsidy', color='orange', linestyle='--', linewidth=2.5)
    ax0.plot(df_dynamic['tick'], df_dynamic['GreenZones'] / total_patches, label='Dynamic Fund', color='green', linewidth=3.5)
    ax0.plot(df_mixed['tick'], df_mixed['GreenZones'] / total_patches, label='Mixed Policy', color='purple', linestyle='-.', linewidth=3)
    ax0.set_title('(a) Evolution of Green Coverage Rate', fontsize=17, pad=15)
    ax0.set_ylabel('Green Coverage Ratio')
    ax0.set_ylim(0, 1)
    ax0.legend(fontsize=14)
    add_year_axis_and_milestones(ax0)

    # (b) Government Budget Dynamics
    ax1 = axes[1]
    ax1.plot(df_static['tick'], df_static['GovBudget'], label='Static Subsidy', color='orange', linestyle='--', linewidth=2.5)
    ax1.plot(df_dynamic['tick'], df_dynamic['GovBudget'], label='Dynamic Fund', color='green', linewidth=3.5)
    ax1.plot(df_mixed['tick'], df_mixed['GovBudget'], label='Mixed Policy', color='purple', linestyle='-.', linewidth=3)
    ax1.set_title('(b) Government Budget Dynamics', fontsize=17, pad=15)
    ax1.set_ylabel('Budget Balance')
    ax1.legend(fontsize=14)
    add_year_axis_and_milestones(ax1)

    # (c) Technology Upgrade Speed (Average AI Generation)
    ax2 = axes[2]
    ax2.plot(df_static['tick'], df_static['AvgAIGen'], label='Static Subsidy', color='orange', linestyle='--', linewidth=2.5)
    ax2.plot(df_dynamic['tick'], df_dynamic['AvgAIGen'], label='Dynamic Fund', color='green', linewidth=3.5)
    ax2.plot(df_mixed['tick'], df_mixed['AvgAIGen'], label='Mixed Policy', color='purple', linestyle='-.', linewidth=3)
    ax2.set_title('(c) Technology Upgrade Speed', fontsize=17, pad=15)
    ax2.set_ylabel('Average AI Generation')
    ax2.legend(fontsize=14)
    add_year_axis_and_milestones(ax2)

    plt.tight_layout(rect=[0, 0.02, 1, 0.90])
    save_plot(fig, 'fig10_policy_comparison_final')

if __name__ == "__main__":

    figure_10_policy_comparison()
