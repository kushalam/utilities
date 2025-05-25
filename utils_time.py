# -*- coding: utf-8 -*-
"""
Functions commonly used for time operations. 
Internet timestamp format RFC3339 available at https://datatracker.ietf.org/doc/html/rfc3339.

Author:     Kushal Moolchandani
Created:    2025-01-30
"""

from datetime import datetime


def convert_datetime_to_RFC3339(input_datetime: datetime) -> str:
    """
    Get timestamp string in RFC3339 format given Python datetime object.
    RFC3339 format like '2025-02-28T00:00:00.00Z'
    Uses ISO 8601 format string with 'T' separator and 'Z' timezone.

    :param input_datetime: Python datetime object
    :return: RFC3339 formatted string
    """
    try:
        rfc_datetime = input_datetime.isoformat("T")
        idx = rfc_datetime.find(".")
        if idx > 0:
            return rfc_datetime[0:idx + 3] + "Z"
        elif rfc_datetime.find("Z") < 0:
            return rfc_datetime + "Z"
        return rfc_datetime
    except ValueError:
        print(f"Error! Invalid value to convert to RFC3339 datetime given {input_datetime}")
        raise
    except Exception:
        print(f"Error! Unable to convert to RFC3339 datetime given {input_datetime}")
        raise


def get_datetime_from_RFC3339(timestamp: str) -> datetime:
    """
    Get Python datetime object given string in RFC3339 timestamp format.
    RFC3339 format like '2025-02-28T00:00:00.00Z'
    Uses ISO 8601 format string with 'T' separator and 'Z' timezone

    :param timestamp: RFC3339 formatted string
    :return: Python datetime object
    """
    try:
        dt = timestamp
        idx = timestamp.find(".")
        if idx > 0:
            dt = timestamp[0:idx] + "Z"
        return datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        print(f"Error! Invalid value to convert from RFC3339 datetime given {timestamp}")
        raise
    except Exception:
        print(f"Error! Unable to convert from RFC3339 datetime given {timestamp}")
        raise
