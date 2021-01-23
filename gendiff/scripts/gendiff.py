#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Script of the 'Difference Generator'."""

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """Print the difference."""
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
