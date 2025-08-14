import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def create_plot(df, color_dict, configs, normalized_key, plot_cols, y_label, fig_name):

    df_normalized = df.copy(deep=True)
    for config in configs:
        df_normalized[config] = df_normalized[normalized_key] / df_normalized[config]

    color_dict_filtered = {key: color_dict[key] for key in plot_cols}

    ax1 = df_normalized.plot.bar(x='Benchmark', y=plot_cols, figsize=(25, 6), color=color_dict_filtered, width=0.9)

    ylim_cutoff = 2.0

    ax1.set(xlabel=None)
    ax1.set_ylim(0, ylim_cutoff)

    for container in ax1.containers:
        for bar in container.patches:
            height = bar.get_height()
            if height > ylim_cutoff:
                ax1.text(bar.get_x() + bar.get_width() / 2, # x position
                        ylim_cutoff,                      # y position (at the cutoff)
                        f'{height:.2f}  ',                   # text label (actual value)
                        ha='center', va='bottom',          # alignment
                        color='red', fontsize=6, rotation=270)

    sec = ax1.secondary_xaxis(location=0)
    sec.set_xticks([4.5, 13, 18, 28, 37], labels=df['Category'].unique())

    sec2 = ax1.secondary_xaxis(location=0)
    sec2.set_xticks([-0.5, 10.5, 15.5, 20.5, 35.5, 38.5], labels=[])
    sec2.tick_params('x', length=100, width=1.5)

    for label in sec.get_xticklabels():
        label.set_fontsize(14)
        label.set_fontweight('bold')

    ax1.set_ylabel(y_label, fontsize=14, fontweight='bold')
    ax1.set_title('Microbenchmark Relative Performance', fontsize=18, fontweight='bold')

    plt.tight_layout()

    plt.savefig(fig_name, bbox_inches='tight')
    plt.show()



def main():
    plt.rcParams['figure.dpi'] = 60  # For inline display in notebooks
    plt.rcParams['savefig.dpi'] = 300  # For saved figures

    bench_colors = ['#4E79A7',  # Blue
                    '#F28E2B',  # Orange
                    '#E15759',  # Red
                    '#76B7B2',  # Teal
                    '#59A14F',  # Green
                    '#EDC948',  # Yellow
                    '#AF7AA1',  # Violet
                    '#FF9DA7',  # Soft Pink/Coral
                    '#3B5D5C',  # Dark Slate Teal
                    '#B03A48']  # Rich Dark Rose

    bench_labels = ['Small BOOM',  
                    'Medium BOOM', 
                    'Large BOOM',  
                    'MILK-V',  
                    'Rocket 1',  
                    'Rocket 2', 
                    'Rocket 3',  
                    'Banana Pi',
                    'MILK-V FireSim',
                    'Banana Pi FireSim']  

    color_dict = dict(zip(bench_labels, bench_colors))

    df = pd.read_csv('microbench.csv')
    df = df[df['Benchmark'] != 'CRm']

    df['Category'] = '\n\n\n\n\n' + df['Category'].astype(str)

    configs = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi FireSim', 'MILK-V FireSim', 'Banana Pi', 'MILK-V']
    plot_cols =  ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi FireSim', 'MILK-V FireSim', 'Banana Pi', 'MILK-V'] 

    create_plot(df, color_dict, configs, 'MILK-V', plot_cols, 'Relative Performance to MILK-V', 'Micro-All.png')

    plot_cols = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi FireSim', 'Banana Pi']
    create_plot(df, color_dict, configs, 'Banana Pi', plot_cols, 'Relative Performance to Banana Pi', 'Micro-BPi.png')

    plot_cols = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'MILK-V FireSim', 'MILK-V']
    create_plot(df, color_dict, configs, 'MILK-V', plot_cols, 'Relative Performance to MILK-V', 'Micro-MILK-V.png')

main()

