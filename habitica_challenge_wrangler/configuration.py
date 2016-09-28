# -*- coding: utf-8 -*-
""" Configuration and command-line arguments
"""

# Ensure backwards compatibility with Python 2
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *
import os
import shutil
from string import Template

import argparse


def get_options():
    """Parses and returns the program configuration options.

    Returns:
        The options object.
    """
    parser = argparse.ArgumentParser()

    # input challenge data file
    parser.add_argument(
        '-f',
        '--input-file',
        required=True,
        metavar='FILE',
        help='Input challenge data CSV file')

    # number of leaderboard entries to display
    parser.add_argument(
        '-n',
        '--leaderboard-rows',
        required=False,
        type=int,
        default=10,
        help='The number of leaderboard entries to display')

    # option to output intermediate data tables to Excel
    parser.add_argument(
        '-x',
        '--to-excel',
        required=False,
        action='store_true',
        help='Outputs intermediate data tables to an Excel file')

    return parser.parse_args()
