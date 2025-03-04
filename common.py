# -*- coding: utf-8 -*-
"""
Functions commonly used and considered utilities. 

Author:     Kushal Moolchandani
Created:    2025-01-23
"""

import sys


def query_yes_no(question, default='no'):
    """
    Ask for user input and get a True (for yes) or False (for no) response to question
    """
    if default is None:
        prompt = " [y/n] "
    elif default == 'yes':
        prompt = " [Y/n] "
    elif default == 'no':
        prompt = " [y/N] "
    else:
        raise ValueError(f"Unknown setting '{default}' for default.")

    while True:
        try:
            resp = input(question + prompt).strip().lower()
            if default is not None and resp == '':
                print("Using default response: " + default, file=sys.stdout)
                return convert_yes_no_to_bool(default)
            else:
                return convert_yes_no_to_bool(resp)
        except ValueError:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def convert_yes_no_to_bool(yes_no: str):
    if yes_no and len(yes_no) > 0:
        if yes_no.lower() == "y":
            return True
        if yes_no.lower() == "yes":
            return True
        if yes_no.lower() == "n":
            return False
        if yes_no.lower() == "no":
            return False
        print("\nError! Expected 'y', 'Y', 'n', 'N', 'yes', 'no' but not", yes_no, "Assume False", file=sys.stderr)
    print("\nError! Invalid yes or no given! Assume False!", file=sys.stderr)

    return False
