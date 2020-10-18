#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Script of 'Difference Generator'."""

import argparse

from gendiff import generate_diff

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
args = parser.parse_args()


def main():
    """Generate and print the difference."""
    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format,
    ))


if __name__ == '__main__':
    main()
