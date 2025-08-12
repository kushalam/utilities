# -*- coding: utf-8 -*-
"""
Generator functions for cycling through colors. 

Created:    2025-04-24  Kushal Moolchandani
"""

#-------------------------------------------------------------------------------
def ccycle():
    """
    Returns a generator function that yields base colors.
    """
    colorlist = ['b','g','r','c','m','y','k']
    
    while True:
        for col in colorlist:
            yield col

#-------------------------------------------------------------------------------
def ccycle_tab():
    """
    Returns a generator function that yields tableau palette colors.
    """
    colorlist = [
                 'tab:blue',
                 'tab:orange',
                 'tab:green',
                 'tab:red',
                 'tab:purple',
                 'tab:brown',
                 'tab:pink',
                 'tab:gray',
                 'tab:olive',
                 'tab:cyan',
                ]
    
    while True:
        for col in colorlist:
            yield col

#-------------------------------------------------------------------------------
def ccycle_css():
    """
    Returns a generator function that yields selected CSS colors as hex codes.
    """
    colorlist = [
                 "#4682B4", #steelblue
                 "#E9967A", #darksalmon
                 "#228B22", #forestgreen
                 "#BDB76B", #darkkhaki
                 "#00CED1", #darkturquoise
                 "#9400D3", #darkviolet
                 "#808080"  #gray
                ]
    
    while True:
        for col in colorlist:
            yield col

#-------------------------------------------------------------------------------
def ccycle_pairs():
    """
    Returns a generator function that yields pairs of named CSS colors.
    """
    colorlist = [
                 ['skyblue','steelblue'], 
                 ['lightsalmon','darksalmon'], 
                 ['lightgreen','forestgreen'], 
                 ['khaki','darkkhaki'],
                 ['paleturquoise','darkturquoise'], 
                 ['violet','darkviolet'],
                 ['lightgray','gray']
                ]

    while True:
        for col in colorlist:
            yield col