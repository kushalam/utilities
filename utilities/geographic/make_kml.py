# -*- coding: utf-8 -*-
"""
Functions to create KML files. 

Author:     Kushal Moolchandani
Created:    2025-08-01
"""

def placemark(coordinates, 
              name = None,
              description = None, 
              extrude = False, 
              altitudeMode = None):
    """
    Add a placemark to given KML file.
    """
    placemark_str = f'\t\t\t<Placemark>\n'

    if name:
        placemark_str += f'\t\t\t\t<name>{name}</name>\n'
    if description:
        placemark_str += f'\t\t\t\t<description>{description}</description>\n'
    
    placemark_str += f'\t\t\t\t<Point>\n'
    if extrude:
        placemark_str += f'\t\t\t\t\t<extrude>1</extrude>\n'
    if altitudeMode:
        placemark_str += f'\t\t\t\t\t<altitudeMode>{altitudeMode}</altitudeMode>\n'
    placemark_str += f'\t\t\t\t\t<coordinates>'
    placemark_str += f'{coordinates[0]},{coordinates[1]},{coordinates[2]}'
    placemark_str += f'</coordinates>\n'
    placemark_str += f'\t\t\t\t</Point>\n'
    
    placemark_str += f'\t\t\t</Placemark>\n'

    return placemark_str


def path(coordinates, 
         name = None,
         description = None, 
         tessellate = False, 
         extrude = False, 
         altitudeMode = None):
    """
    Add a path to the KML file.
    """
    placemark_str = f'\t\t\t<Placemark>\n'

    if name:
        placemark_str += f'\t\t\t\t<name>{name}</name>\n'
    if description:
        placemark_str += f'\t\t\t\t<description>{description}</description>\n'
    
    placemark_str += f'\t\t\t\t<LineString>\n'
    if tessellate:
        placemark_str += f'\t\t\t\t\t<tessellate>1</tessellate>\n'
    if extrude:
        placemark_str += f'\t\t\t\t\t<extrude>1</extrude>\n'
    if altitudeMode:
        placemark_str += f'\t\t\t\t\t<altitudeMode>{altitudeMode}</altitudeMode>\n'
    placemark_str += f'\t\t\t\t\t<coordinates>\n'
    for i in range(len(coordinates)):
        placemark_str += f'\t\t\t\t\t{coordinates[i][0]},{coordinates[i][1]},{coordinates[i][2]}\n'
    placemark_str += f'\t\t\t\t\t</coordinates>\n'
    placemark_str += f'\t\t\t\t</LineString>\n'

    placemark_str += f'\t\t\t</Placemark>\n'

    return placemark_str


def polygon(coordinates, 
            name = None,
            description = None,
            tessellate = False, 
            extrude = False, 
            altitudeMode = None):
    """
    Add a path to the KML file.
    """
    placemark_str = f'\t\t\t<Placemark>\n'

    if name:
        placemark_str += f'\t\t\t\t<name>{name}</name>\n'
    if description:
        placemark_str += f'\t\t\t\t<description>{description}</description>\n'
    
    placemark_str += f'\t\t\t\t<Polygon>\n'
    if tessellate:
        placemark_str += f'\t\t\t\t\t<tessellate>1</tessellate>\n'
    if extrude:
        placemark_str += f'\t\t\t\t\t<extrude>1</extrude>\n'
    if altitudeMode:
        placemark_str += f'\t\t\t\t\t<altitudeMode>{altitudeMode}</altitudeMode>\n'
    placemark_str += f'\t\t\t\t\t<outerBoundaryIs>\n'
    placemark_str += f'\t\t\t\t\t\t<LinearRing>\n'
    placemark_str += f'\t\t\t\t\t\t\t<coordinates>\n'
    for i in range(len(coordinates)):
        placemark_str += f'\t\t\t\t\t\t\t{coordinates[i][0]},{coordinates[i][1]},{coordinates[i][2]}\n'
    placemark_str += f'\t\t\t\t\t\t\t</coordinates>\n'
    placemark_str += f'\t\t\t\t\t\t</LinearRing>\n'
    placemark_str += f'\t\t\t\t\t</outerBoundaryIs>\n'
    placemark_str += f'\t\t\t\t</Polygon>\n'

    placemark_str += f'\t\t\t</Placemark>\n'

    return placemark_str


def create_kml(filename: str, 
               kml_strings: list[str]):
    """
    Creates and saves a KML file.
    
    Parameters
    ----------
    filename : str
        Name of the output KML file.
    kml_strings: list[str]
        A list of strings, where each string is a feature to be added to the KML file.
    """
    if not filename.endswith('.kml'):
        filename += '.kml'
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(f'<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        f.write(f'\t<Document>\n')
        f.write(f'\t\t<name>{filename}</name>\n')

        for kml_str in kml_strings:
            f.write(f'\n')
            f.write(kml_str)
            f.write(f'\n')

        f.write(f'\t</Document>\n')
        f.write(f'</kml>')
