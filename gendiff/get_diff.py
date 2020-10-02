# -*- coding:utf-8 -*-

"""Module of 'get_diff' function."""

from gendiff.argparser import get_file_paths, get_output_format
from gendiff.builder_diff import build_diff
from gendiff.formatters import json_like_view, plain_view
from gendiff.upload_file import get_file


def get_diff():
    """Print the diff."""
    output_format = get_output_format()
    first_file_path, second_file_path = get_file_paths()
    print(generate_diff(first_file_path, second_file_path, output_format))


def generate_diff(file_path1, file_path2, output_format='JSON-like'):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        Return the formatted diff.
    """
    MAPPING_FOR_CHOOSE_RENDER_FUNCTION = {
        'plain': plain_view.render,
        'JSON-like': json_like_view.render,
    }

    before = get_file(file_path1)
    after = get_file(file_path2)
    diff = build_diff(before, after)

    return MAPPING_FOR_CHOOSE_RENDER_FUNCTION[output_format](diff)
