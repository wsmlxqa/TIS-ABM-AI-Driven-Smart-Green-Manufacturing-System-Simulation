import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================== Global Figure Settings ====================
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

def normalize(series):
    """Normalize series to [0, 1] range for SVI calculation."""
    return (series - series.min()) / (series.max() - series.min() + 1e-8)

def plot_svi_sensitivity(csv_path):
    # 1. Load Data
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
        return

    # 2. Data Transformation
    # Green Coverage is calculated relative to total patches (1089)
    df['GreenCoverage'] = df['GreenZones'] / 1089
    
    # Normalize key indicators for weighted SVI
    q = normalize(df['AvgAIGen'])       # Quality proxy
    g = normalize(df['GreenCoverage'])  # Greenness proxy
    r = normalize(df['NumSuppliers'])   # Resilience proxy

    # Define scenarios from Table: Impact of SVI Weighting Configurations
    # Format: {Scenario_Name: (w_q, w_g, w_r)}
    scenarios = {
        'S1: Balanced (Baseline)': (1.0, 1.0, 1.0),
        'S2: Quality-Led (High-tech)': (2.0, 0.5, 0.5),
        'S3: Green-Led (Process industries)': (0.5, 2.0, 0.5),
        'S4: Resilience-Led (Assembly)': (0.5, 0.5, 2.0)
    }

    # 3. Plotting
    fig, ax = plt.subplots(figsize=(8, 6))

    colors = ['#d62728', '#1f77b4', '#2ca02c', '#ff7f0e']
    styles = ['-', '--', '-.', ':']

    for (name, weights), color, style in zip(scenarios.items(), colors, styles):
        w_q, w_g, w_r = weights
        # Calculate Weighted SVI
        weighted_svi = (w_q * q + w_g * g + w_r * r) / (w_q + w_g + w_r)
        
        ax.plot(weighted_svi, df['Demand'], label=name, color=color, 
                linestyle=style, linewidth=2, marker='o', markersize=3, alpha=0.8)

    # 4. Critical Threshold Zone Highlighting (0.55 - 0.85)
    v_start, v_end = 0.55, 0.85
    ax.axvspan(v_start, v_end, color='gray', alpha=0.15, label='Critical Threshold Zone')
    
    # Add vertical boundary lines and text labels
    ax.axvline(x=v_start, color='black', linestyle=':', linewidth=1, alpha=0.6)
    ax.axvline(x=v_end, color='black', linestyle=':', linewidth=1, alpha=0.6)
    
    y_top = ax.get_ylim()[1]
    ax.text(v_start, y_top * 0.9, f'{v_start}', ha='center', fontweight='bold')
    ax.text(v_end, y_top * 0.9, f'{v_end}', ha='center', fontweight='bold')

    # 5. Aesthetics
    ax.set_xlabel('Perceived System Value Index (Weighted SVI)')
    ax.set_ylabel('Market Demand')
    ax.set_title('Robustness of Phase Transition across Market Weighting Scenarios')
    ax.legend(loc='upper left', fontsize=10, frameon=True)
    ax.grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()
    
    # Save outputs
    output_filename = 'fig_svi_sensitivity'
    plt.savefig(f'{output_filename}.pdf', format='pdf', dpi=300)
    plt.savefig(f'{output_filename}.png', format='png', dpi=300)
    print(f"Success: Plots saved as {output_filename}.pdf and .png")
    plt.show()

if __name__ == "__main__":
    plot_svi_sensitivity('SVI_Sensitivity_Analysis_Data.csv')