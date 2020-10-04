# -*- coding:utf-8 -*-

"""Agrparser of 'Difference Generator."""

import argparse
from os.path import abspath


def get_args():
    """Parse and return the args from CLI.

    Returns:
        return the arguments from CLI.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        default='json-like',
        help='set format of output',
        metavar='FORMAT',
    )
    return parser.parse_args()


def get_output_format():
    """Get the ouput format.

    Returns:
        format
    """
    return get_args().format


def get_file_paths():
    """Get the file paths.

    Returns:
        The file paths
    """
    return abspath(get_args().first_file), abspath(get_args().second_file)
