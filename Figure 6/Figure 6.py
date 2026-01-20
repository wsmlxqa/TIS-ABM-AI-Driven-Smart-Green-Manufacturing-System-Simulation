import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Matplotlib global settings
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['axes.unicode_minus'] = False

# Create output directory
os.makedirs('figures', exist_ok=True)

def save_plot(fig, filename):
    fig.savefig(f'figures/{filename}.png', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
    plt.show()
    plt.close(fig)

def figure_6_spatial_evolution_from_csv():
    print("Generating Figure 6 from CSV spatial data files...")

    # Define year labels and file mapping with updated filenames
    years = [2018, 2026, 2043, 2059]
    file_map = {
        2018: 'spatial_data_2018 1=green 0=non-green.csv',
        2026: 'spatial_data_2026 1=green 0=non-green.csv',
        2043: 'spatial_data_2043 1=green 0=non-green.csv',
        2059: 'spatial_data_2059 1=green 0=non-green.csv'
    }

    # Set up 2×2 grid for subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 12), constrained_layout=True)
    fig.suptitle('Figure 6: Spatial Evolution of Manufacturing Systems', fontsize=18)

    # Plot each spatial grid
    for i, year in enumerate(years):
        ax = axes[i // 2, i % 2]
        file_path = file_map[year]

        # Load spatial data from CSV
        spatial_data = pd.read_csv(file_path, header=None).values

        im = ax.imshow(spatial_data, cmap='Greens', interpolation='nearest')
        ax.set_title(f'Year = {year}', fontsize=14)
        ax.set_xticks([])
        ax.set_yticks([])

    # Shared colorbar
    cbar = plt.colorbar(im, ax=axes.ravel().tolist(), shrink=0.8, aspect=20)
    cbar.set_label('Region Attribute (Darker = Greener)', fontsize=14)

    save_plot(fig, 'fig6_spatial_evolution')

if __name__ == "__main__":
    figure_6_spatial_evolution_from_csv()

