# -*- coding: utf-8 -*-
"""
Functions to parse or write csv and json files. 

Author:     Kushal Moolchandani
Created:    2025-02-19
"""

from pathlib import Path
import csv
import json


def make_dir_at_path(path: str):
    """
    Create directory if it does not exist
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def open_file_at_path(file_path: str, mode: str):
    """
    Open file at given path with given mode, creating any parent directories as needed.
    """
    make_dir_at_path(Path(file_path).parent)
    return open(file_path, mode)


def write_json_file(out_file_w_path: str, json_data: dict):
    """
    Write JSON data to file at given path. Append '.json' if not present.

    :param out_file_w_path: Path to write JSON data to
    :param json_data: JSON data to write
    """
    if not out_file_w_path.endswith('.json'):
        out_file_w_path += '.json'
    with open_file_at_path(out_file_w_path, 'w') as out_file:
        json.dump(json_data, out_file, indent=4)


def read_json_file(in_file_w_path: str):
    """
    Read JSON data from file at given path. Append '.json' if not present.

    :param in_file_w_path: Path to read JSON data from
    :return: JSON data read from file
    """
    if not in_file_w_path.endswith('.json'):
        in_file_w_path += '.json'
    with open_file_at_path(in_file_w_path, 'r') as in_file:
        return json.load(in_file)


def write_csv_file(out_file_w_path: str, csv_data: list, delimiter: str = ','):
    """
    Write CSV data to file at given path. Append '.csv' if not present.

    :param out_file_w_path: Path to write CSV data to
    :param csv_data: CSV data to write
    :param delimiter: Delimiter to use for CSV data
    """
    if not out_file_w_path.endswith('.csv'):
        out_file_w_path += '.csv'
    with open_file_at_path(out_file_w_path, 'w') as out_file:
        for row in csv_data:
            writer = csv.writer(out_file, delimiter=delimiter)
            writer.writerow(row)


def read_csv_file(in_file_w_path: str, delimiter: str = ','):
    """
    Read CSV data from file at given path. Append '.csv' if not present.
    
    :param in_file_w_path: Path to read CSV data from
    :param delimiter: Delimiter to use for CSV data
    :return: CSV data read from file
    """
    if not in_file_w_path.endswith('.csv'):
        in_file_w_path += '.csv'
    with open_file_at_path(in_file_w_path, 'r') as in_file:
        reader = csv.reader(in_file, delimiter=delimiter)
        return [row for row in reader]