# -*- coding: utf-8 -*-
"""
Basic plotting functions.

Created:    2025-07-30  Kushal Moolchandani
"""

import matplotlib.pyplot as plt
import numpy as np
import os

from numpy.typing import ArrayLike

from utilities.plotting.colorutils import *

#-----------------------------------------------------------------------------------------------------------------------
# Line plot
def line(x: ArrayLike, 
         y: ArrayLike, 
         xlabel: str = '',
         ylabel: str = '', 
         title: str = '', 
         legend = None, 
         output_path: str = ''):
    """
    Plot line charts of number of simultaneously airborne flights, i.e., 
    traffic density versus time. 
    """
    fontsize = 14

    _, ax = plt.subplots()

    ax.plot(x, y)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)
    if legend:
        ax.legend(legend)

    plt.savefig(os.path.join(output_path, title))
    plt.close()

#-----------------------------------------------------------------------------------------------------------------------
# Histograms
def histogram(data: list, 
              bin_size: int = 1, 
              xlabel: str = 'Value', 
              ylabel: str = 'Frequency', 
              title: str = 'Distribution', 
              legend: list = ['Data'], 
              output_path: str = ''):
    
    fontsize = 14
    col = ccycle_pairs()
    
    _, ax = plt.subplots()
    
    for i in range(len(data)):
        colorlist = col.__next__()
        
        try:
            bins = np.arange(min(data[i], default=0), max(data[i])+bin_size, bin_size)
        except:
            bins = bin_size
        
        n, _, _ = ax.hist(data[i], bins=bins, rwidth=0.9, alpha=0.5, 
                           color=colorlist[0], edgecolor=colorlist[1])
    
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.legend(legend, loc='best', fontsize='large')
    ax.set_title(title, fontsize=fontsize)
    
    try: # Set a clean upper y-axis limit.
        maxfreq = n.max()   #type: ignore
        ax.set_ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    except:
        pass

    ax.grid(axis='y')
    plt.savefig(os.path.join(output_path, title))
    plt.close()

#-----------------------------------------------------------------------------------------------------------------------
# Bar plots
def stacked_bars(data: dict, 
                 groups: list, 
                 xlabel: str = 'Groups',
                 ylabel: str = 'Count',
                 title: str = 'Stacked Bar Chart',
                 output_path: str = ''):
    
    fontsize = 14
    colors = ccycle_tab()

    # Create the bar chart
    bar_width = 1 / len(groups)

    _, ax = plt.subplots()
    bottom = np.zeros(len(groups))

    for key, values in data.items():
        ax.bar(groups, values, bar_width, label=key, color=colors.__next__(), bottom=bottom)
        bottom += values
    
    x = np.arange(len(groups))
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize)
    ax.legend(loc='best', fontsize=fontsize)
    ax.set_xticks(x, groups, fontsize=fontsize)

    ax.grid(axis='y')

    plt.savefig(os.path.join(output_path, title))
    plt.close()

#-----------------------------------------------------------------------------------------------------------------------
# Box Plot
def box(data, 
        category: str, 
        value: str, 
        xlabel: str = 'Category',
        ylabel: str = 'Value',
        title: str = 'Boxplot',
        output_path: str = ''):
    
    colors = ccycle_tab()

    grouped = data.groupby(category)[value]

    _, ax = plt.subplots()

    # Create the plot with different colors for each group
    boxplot = ax.boxplot(x=[group.values for _, group in grouped],
                        tick_labels=grouped.groups.keys(),
                        patch_artist=True,
                        medianprops={'color': 'black'}
                        ) 

    # Assign colors to each box in the boxplot
    cols = [colors.__next__() for i in range(len(category))]
    for box, color in zip(boxplot['boxes'], cols):
        box.set_facecolor(color)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(axis='y')
        
    plt.savefig(os.path.join(output_path, title))
    plt.close()