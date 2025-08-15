import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def create_heatmap(df, configs, normalized_key, plot_cols, fig_name):
    df_normalized = df.copy(deep=True)
    for config in configs:
        df_normalized[config] = df_normalized[normalized_key] / df_normalized[config]

    df_normalized.set_index('Benchmark', inplace=True)
    df_normalized.drop(normalized_key, axis=1, inplace=True)
    df_normalized.drop('Description', axis=1, inplace=True)
    df_normalized.drop('Category', axis=1, inplace=True)

    for column_name in df_normalized.columns:
        if (column_name not in plot_cols):
            df_normalized.drop(column_name, axis=1, inplace=True)

    df_normalized = df_normalized.T

    fig, ax = plt.subplots(figsize=(18, 8))
    cax = ax.imshow(df_normalized.values, aspect='auto', cmap='viridis')

    ax.set_xticks(np.arange(len(df_normalized.columns)))
    ax.set_yticks(np.arange(len(df_normalized.index)))
    ax.set_xticklabels(df_normalized.columns, rotation=90)
    ax.set_yticklabels(df_normalized.index)


    fig.colorbar(cax, ax=ax)

    ax.set_xlabel('Benchmark')

    plt.tight_layout()

    plt.savefig(fig_name, bbox_inches='tight')
    plt.show() 

def create_split_plot(df, color_dict, configs, normalized_key, plot_cols, y_label, fig_name):
    df_normalized = df.copy(deep=True)
    for config in configs:
        df_normalized[config] = df_normalized[normalized_key] / df_normalized[config]

    df_normalized.drop(normalized_key, axis=1, inplace=True)

    color_dict_filtered = {key: color_dict[key] for key in plot_cols}

    df_normalized_top = df_normalized[(df_normalized['Category'] == '\n\n\n\n\n\nControl Flow') | (df_normalized['Category'] == '\n\n\n\n\n\nData') | (df_normalized['Category'] == '\n\n\n\n\n\nExecution')]
    df_normalized_bottom = df_normalized[(df_normalized['Category'] == '\n\n\n\n\n\nCache') | (df_normalized['Category'] == '\n\n\n\n\n\nMemory')]

    df_normalized_top['Category'] = df['Category'].str.replace(r'^\n', '', n=1, regex=True)

    fig, axes = plt.subplots(2, 1, figsize=(25, 12), sharey=True, constrained_layout=True)
    fig.suptitle('Microbenchmark Relative Performance to ' + normalized_key, fontsize=28, fontweight='bold')
    fig.supylabel(y_label, va='center', rotation='vertical', fontsize=20, fontweight='bold')

    ax1 = df_normalized_top.plot.bar(x='Benchmark', y=plot_cols, color=color_dict_filtered, width=0.9, ax=axes[0])
    ax1.axhline(y=1.0, color='k', linestyle='--', label=normalized_key)

    handles, labels = ax1.get_legend_handles_labels()
    reordered_handles = handles[1:] + [handles[0]]
    reordered_labels = labels[1:] + [labels[0]]
    ax1.legend(reordered_handles, reordered_labels, fontsize=18, ncol=len(reordered_labels))

    #if ax1.get_legend():
    #    ax1.get_legend().remove()

    ylim_cutoff = 2.0

    ax1.set(xlabel=None)
    ax1.set_ylim(0, ylim_cutoff)
    ax1.tick_params(axis='x', labelsize=18)
    ax1.tick_params(axis='y', labelsize=18)

    for container in ax1.containers:
        for bar in container.patches:
            height = bar.get_height()
            if height > ylim_cutoff:
                ax1.text(bar.get_x() + bar.get_width() / 2,
                        ylim_cutoff,
                        f'{height:.2f}  ',
                        ha='center', va='bottom',
                        color='black', fontsize=16, rotation=270)

    sec = ax1.secondary_xaxis(location=0)
    sec.set_xticks([4.5, 13, 18], labels=df_normalized_top['Category'].unique())

    sec2 = ax1.secondary_xaxis(location=0)
    sec2.set_xticks([-0.5, 10.5, 15.5, 20.5], labels=[])
    sec2.tick_params('x', length=150, width=1.5)

    for label in sec.get_xticklabels():
        label.set_fontsize(18)
        label.set_fontweight('bold')

    ax2 = df_normalized_bottom.plot.bar(x='Benchmark', y=plot_cols, color=color_dict_filtered, width=0.9, ax=axes[1])
    ax2.axhline(y=1.0, color='k', linestyle='--', label=normalized_key)

    if ax2.get_legend():
        ax2.get_legend().remove()

    ax2.set(xlabel=None)
    ax2.set_ylim(0, ylim_cutoff)
    ax2.tick_params(axis='x', labelsize=18)
    ax2.tick_params(axis='y', labelsize=18)

    for container in ax2.containers:
        for bar in container.patches:
            height = bar.get_height()
            if height > ylim_cutoff:
                ax2.text(bar.get_x() + bar.get_width() / 2,
                        ylim_cutoff,
                        f'{height:.2f}  ',
                        ha='center', va='bottom',
                        color='black', fontsize=16, rotation=270)

    ax2.legend
    sec3 = ax2.secondary_xaxis(location=0)
    sec3.set_xticks([8, 16.5], labels=df_normalized_bottom['Category'].unique())

    sec4 = ax2.secondary_xaxis(location=0)
    sec4.set_xticks([-0.5, 15.5, 17.5], labels=[])
    sec4.tick_params('x', length=150, width=1.5)

    for label in sec3.get_xticklabels():
        label.set_fontsize(18)
        label.set_fontweight('bold')

    plt.savefig(fig_name, bbox_inches='tight')
    plt.show()


def create_plot(df, color_dict, configs, normalized_key, plot_cols, y_label, fig_name):
    df_normalized = df.copy(deep=True)

    for config in configs:
        df_normalized[config] = df_normalized[normalized_key] / df_normalized[config]

    df_normalized.drop(normalized_key, axis=1, inplace=True)

    color_dict_filtered = {key: color_dict[key] for key in plot_cols}

    ax1 = df_normalized.plot.bar(x='Benchmark', y=plot_cols, figsize=(25, 6), color=color_dict_filtered, width=0.9)
    ax1.axhline(y=1.0, color='k', linestyle='--', label=normalized_key)

    ax1.legend()

    handles, labels = plt.gca().get_legend_handles_labels()
    reordered_handles = handles[1:] + [handles[0]]
    reordered_labels = labels[1:] + [labels[0]]
    plt.legend(reordered_handles, reordered_labels)

    ylim_cutoff = 2.0

    ax1.set(xlabel=None)
    ax1.set_ylim(0, ylim_cutoff)

    for container in ax1.containers:
        for bar in container.patches:
            height = bar.get_height()
            if height > ylim_cutoff:
                ax1.text(bar.get_x() + bar.get_width() / 2,
                        ylim_cutoff,
                        f'{height:.2f}  ',
                        ha='center', va='bottom',
                        color='black', fontsize=6, rotation=270)

    sec = ax1.secondary_xaxis(location=0)
    sec.set_xticks([4.5, 13, 18, 30, 37.5], labels=df_normalized['Category'].unique())

    sec2 = ax1.secondary_xaxis(location=0)
    sec2.set_xticks([-0.5, 10.5, 15.5, 20.5, 36.5, 38.5], labels=[])
    sec2.tick_params('x', length=100, width=1.5)

    for label in sec.get_xticklabels():
        label.set_fontsize(14)
        label.set_fontweight('bold')

    ax1.set_ylabel(y_label, fontsize=14, fontweight='bold')
    ax1.set_title('Microbenchmark Relative Performance', fontsize=18, fontweight='bold', pad=20)

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
                    '#B03A48',  # Rich Dark Rose
                    '#731F2A']  # Deep Crimson / Burnt Rose

    bench_labels = ['Small BOOM',  
                    'Medium BOOM', 
                    'Large BOOM',  
                    'MILK-V Hardware',  
                    'Rocket 1',
                    'Rocket 2', 
                    'Rocket 3',  
                    'Banana Pi Hardware',
                    'MILK-V Sim Model',
                    'Banana Pi Sim Model',
                    'Fast Banana Pi Sim Model']  

    color_dict = dict(zip(bench_labels, bench_colors))

    df = pd.read_csv('microbench.csv')
    df = df[df['Benchmark'] != 'CRm']

    df['Category'] = '\n\n\n\n\n\n' + df['Category'].astype(str)

    configs = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi Sim Model', 'Fast Banana Pi Sim Model', 'MILK-V Sim Model', 'Banana Pi Hardware', 'MILK-V Hardware']

    plot_cols =  ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi Sim Model', 'Fast Banana Pi Sim Model', 'MILK-V Sim Model', 'Banana Pi Hardware'] 
    create_plot(df, color_dict, configs, 'MILK-V Hardware', plot_cols, 'Relative Performance to MILK-V Hardware', 'Micro-All.png')

    plot_cols = ['Banana Pi Sim Model', 'Fast Banana Pi Sim Model']
    create_plot(df, color_dict, configs, 'Banana Pi Hardware', plot_cols, 'Relative Performance to Banana Pi Hardware', 'Micro-BPi.png')

    plot_cols = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'MILK-V Sim Model']
    create_plot(df, color_dict, configs, 'MILK-V Hardware', plot_cols, 'Relative Performance to MILK-V Hardware', 'Micro-MILK-V.png')


    plot_cols =  ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi Sim Model', 'Fast Banana Pi Sim Model', 'MILK-V Sim Model', 'Banana Pi Hardware'] 
    create_split_plot(df, color_dict, configs, 'MILK-V Hardware', plot_cols, 'Relative Performance to MILK-V Hardware', 'Micro-All-Split.png')

    plot_cols = ['Banana Pi Sim Model', 'Fast Banana Pi Sim Model']
    create_split_plot(df, color_dict, configs, 'Banana Pi Hardware', plot_cols, 'Relative Performance to Banana Pi Hardware', 'Micro-BPi-Split.png')

    plot_cols = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'MILK-V Sim Model']
    create_split_plot(df, color_dict, configs, 'MILK-V Hardware', plot_cols, 'Relative Performance to MILK-V Hardware', 'Micro-MILK-V-Split.png')

    plot_cols =  ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'Banana Pi Sim Model', 'Fast Banana Pi Sim Model', 'MILK-V Sim Model', 'Banana Pi Hardware']  
    create_heatmap(df, configs, 'MILK-V Hardware', plot_cols, 'Micro-MILK-V-Heatmap.png')

    plot_cols = ['Banana Pi Sim Model', 'Fast Banana Pi Sim Model']
    create_heatmap(df, configs, 'Banana Pi Hardware', plot_cols, 'Micro-BPi-Heatmap.png')

    plot_cols = ['Small BOOM', 'Medium BOOM', 'Large BOOM', 'MILK-V Sim Model']
    create_heatmap(df, configs, 'MILK-V Hardware', plot_cols, 'Micro-MILK-V-Heatmap.png')



main()

