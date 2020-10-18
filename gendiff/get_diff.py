# -*- coding:utf-8 -*-

"""Module of 'get_diff' function."""

from gendiff.builder_diff import build_diff
from gendiff.formatters import json_like_view, json_view, plain_view
from gendiff.upload_file import get_file


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

    try:
        formatter = mapping_for_choose_render_function[output_format]
    except KeyError as key_error:
        return (
            'Invalid output format: {0}.\n'.format(key_error) +
            "Try 'json', 'plain' or 'json-like'."
        )

    try:
        before = get_file(file_path1)
        after = get_file(file_path2)
    except FileNotFoundError as file_error:
        return "File not found.\n{0}: '{1}'".format(
            file_error.args[1],
            file_error.filename,
        )

    diff = build_diff(before, after)

    return formatter(diff)
