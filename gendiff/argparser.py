"""Agrparser of 'Difference Generator'."""

import argparse


def get_args():
    """Parse and return the args from CLI.

    Returns:
        the arguments from CLI
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output',
        metavar='FORMAT',
        dest='format',
    )

    return parser.parse_args()
