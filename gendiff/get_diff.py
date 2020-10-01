# -*- coding:utf-8 -*-

"""Module of 'get_diff' function."""

from gendiff import argparser, builder_diff


def get_diff():
    """Print the diff."""
    first_file_path, second_file_path = argparser.get_file_paths()
    print(builder_diff.generate_diff(first_file_path, second_file_path))
