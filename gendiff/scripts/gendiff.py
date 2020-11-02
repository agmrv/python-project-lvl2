#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Script of the 'Difference Generator'."""

from gendiff import generate_diff
from gendiff.cli import get_args


def main():
    """Print the difference."""
    args = get_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
