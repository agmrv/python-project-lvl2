# -*- coding:utf-8 -*-

"""Module of 'get_diff' function."""

from gendiff.argparser import get_file_paths, get_output_format
from gendiff.builder_diff import build_diff
from gendiff.formatters import json_like_view, json_view, plain_view
from gendiff.upload_file import get_file


def get_diff():
    """Start getting diff.

    Returns:
        the diff string to output
    """
    output_format = get_output_format()
    first_file_path, second_file_path = get_file_paths()
    return generate_diff(first_file_path, second_file_path, output_format)


def generate_diff(file_path1, file_path2, output_format='json-like'):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        output_format: output format: plain or json-like

    Returns:
        Return the formatted diff.
    """
    mapping_for_choose_render_function = {
        'plain': plain_view.render,
        'json-like': json_like_view.render,
        'json': json_view.render,
    }

    before = get_file(file_path1)
    after = get_file(file_path2)
    diff = build_diff(before, after)

    return mapping_for_choose_render_function[output_format](diff)
