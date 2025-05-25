# -*- coding: utf-8 -*-
"""
Functions to create GeoJSON files. 
GeoJSON specification available at https://datatracker.ietf.org/doc/html/rfc7946.

Author:     Kushal Moolchandani
Created:    2025-02-26
"""

from .. import utils_file
from typing import Optional


def create_geojson_geometry(geometry_type: str, 
                            coordinates: Optional[list] = None):
    """
    Create a GeoJSON Geometry.

    :param geometry_type: Type of geometry (Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon)
    :param coordinates: List of coordinates
    :return: GeoJSON Geometry
    """
    if coordinates is None:
        coordinates = []
    if geometry_type == "Point":
        return {
            "type": "Point",
            "coordinates": coordinates
        }
    elif geometry_type == "LineString":
        return {
            "type": "LineString",
            "coordinates": coordinates
        }
    elif geometry_type == "Polygon":
        return {
            "type": "Polygon",
            "coordinates": coordinates
        }
    elif geometry_type == "MultiPoint":
        return {
            "type": "MultiPoint",
            "coordinates": coordinates
        }
    elif geometry_type == "MultiLineString":
        return {
            "type": "MultiLineString",
            "coordinates": coordinates
        }
    elif geometry_type == "MultiPolygon":
        return {
            "type": "MultiPolygon",
            "coordinates": coordinates
        }
    else:
        return None


def create_geojson_geometry_collection(geometries: Optional[list] = None):
    """
    Create a GeoJSON Geometry Collection.

    :param geometries: List of GeoJSON Geometries
    :return: GeoJSON Geometry Collection
    """
    if geometries is None:
        geometries = []
    return {
        "type": "GeometryCollection",
        "geometries": geometries
    }


def create_geojson_feature(geometry_type: str, 
                           properties: Optional[dict] = None, 
                           coordinates: Optional[list] = None):
    """
    Create a GeoJSON Feature.

    :param geometry_type: Type of geometry (Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon)
    :param coordinates: List of coordinates
    :return: GeoJSON Feature
    """
    if properties is None:
        properties = {}
    if coordinates is None:
        coordinates = []
    return {
        "type": "Feature",
        "properties": properties,
        "geometry": create_geojson_geometry(geometry_type, coordinates)
    }


def create_geojson_feature_collection(features: Optional[list] = None):
    """
    Create a GeoJSON Feature Collection.

    :param features: List of GeoJSON Features
    :return: GeoJSON Feature Collection
    """
    if features is None:
        features = []
    return {
        "type": "FeatureCollection",
        "features": features
    }


def add_geojson_feature_to_feature_collection(feature_collection: dict, 
                                              feature: dict):
    """
    Add a GeoJSON Feature to a GeoJSON Feature Collection.

    :param feature_collection: GeoJSON Feature Collection
    :param feature: GeoJSON Feature
    :return: GeoJSON Feature Collection
    """
    feature_collection["features"].append(feature)
    return feature_collection


def write_geojson_file(file_path: str, 
                       geojson: dict):
    """
    Write GeoJSON to a file.
    
    :param file_path: File path
    :param geojson: GeoJSON
    """
    utils_file.write_json_file(file_path, geojson)