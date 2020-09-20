#!/usr/bin/env python3
"""Agrparser of 'Difference Generator."""

import argparse


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
        metavar='FORMAT',
        help='set format of output',
        )
    return parser.parse_args()


ARGS = get_args()


def get_file_paths():
    """Get the file paths.

    Returns:
        The file paths.
    """
    return ARGS.first_file, ARGS.second_file
