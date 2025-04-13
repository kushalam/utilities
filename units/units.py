# -*- coding: utf-8 -*-
"""
Constants, units, and conversions.

Author:     Kushal Moolchandani
Created:    2025-04-06
"""

import csv
from importlib import resources

# Load constants and conversion factors from CSV files
with resources.open_text('utilities.units', 'constants_codata.csv') as f:
    for i in range(4):
        next(f)
    rows = csv.DictReader(f)
    constants_codata = {row['constant_name']: float(row['value']) for row in rows}

with resources.open_text('utilities.units', 'conversion_factors.csv') as f:
    for i in range(2):
        next(f)
    rows = csv.DictReader(f)
    conversion_factors = {row['source_unit']: row['conversion_factor'] for row in rows}

with resources.open_text('utilities.units', 'constants_physical.csv') as f:
    rows = csv.DictReader(f)
    constants_physical = {row['constant_name']: float(row['value']) for row in rows}

constants = {**constants_codata, **constants_physical}

#-------------------------------------------------------------------------------
def get_constant(constant_name: str) -> float:
    """
    Get the value of a constant by its name.

    Parameters
    ----------
    constant_name : str
        The name of the constant.

    Returns
    -------
    float
        The value of the constant.
    """
    try:
        # return constants.loc[constants['constant_name'] == constant_name, 'value'].values[0]
        return constants[constant_name]
    except:
        raise KeyError(f"Constant '{constant_name}' not found.")

#-------------------------------------------------------------------------------
def to_metric(customary_value: float, 
               customary_unit: str,
               metric_unit: str) -> float:
    """
    Convert a value from customary units to metric units.

    Parameters
    ----------
    customary_value : float
        The value in customary units.
    customary_unit : str
        The unit of the value in customary units.
    metric_unit : str
        The unit to convert to in metric units.

    Returns
    -------
    float
        The value in metric units.
    """
    try:
        factor = conversion_factors.loc[(conversion_factors['source_unit'] == customary_unit) & 
                                        (conversion_factors['metric_unit'] == metric_unit), 
                                        'conversion_factor'].values[0]
    except:
        raise ValueError(f"Conversion from '{customary_unit}' to '{metric_unit}' not found.")
    
    return customary_value * factor

#-------------------------------------------------------------------------------
def to_customary(metric_value: float,
                  metric_unit: str,
                  customary_unit: str) -> float:
    """
    Convert a value from metric units to customary units.

    Parameters
    ----------
    metric_value : float
        The value in metric units.
    metric_unit : str
        The unit of the value in metric units.
    customary_unit : str
        The unit to convert to in customary units.

    Returns
    -------
    float
        The value in customary units.
    """
    try:
        factor = conversion_factors.loc[(conversion_factors['metric_unit'] == metric_unit) & 
                                        (conversion_factors['source_unit'] == customary_unit), 
                                        'conversion_factor'].values[0]
    except:
        raise ValueError(f"Conversion from '{metric_unit}' to '{customary_unit}' not found.")
    
    return metric_value / factor

#-------------------------------------------------------------------------------
def format_unit(unit: str) -> str:
    """
    Format a unit string to a standard format.

    Parameters
    ----------
    unit : str
        The unit string to format.

    Returns
    -------
    str
        The formatted unit string.
    """
    return unit.lower().rstrip('s')