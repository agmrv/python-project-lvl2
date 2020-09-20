"""Module of 'get_diff' function."""

from gendiff import argparser, engine


def get_diff():
    """Print the diff."""
    first_file_path, second_file_path = argparser.get_file_paths()
    print(engine.generate_diff(first_file_path, second_file_path))
