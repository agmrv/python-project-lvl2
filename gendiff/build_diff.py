# -*- coding:utf-8 -*-

"""Module of Difference Builder."""

from gendiff.formatters import json_like_view, json_view, plain_view
from gendiff.upload_file import get_file


def build_diff(before, after):
    """Build the diff between before and after files.

    Args:
        before: file before change
        after: file after change

    Returns:
        diff.
    """
    diff = {}
    common = before.copy()
    common.update(after)
    for key, some_data in common.items():
        if key not in after:
            diff[key] = {
                'value': some_data,
                'status': 'removed',
            }
        elif key not in before:
            diff[key] = {
                'value': some_data,
                'status': 'added',
            }
        elif some_data == before[key]:
            diff[key] = {
                'value': some_data,
                'status': 'unmodified',
            }
        elif isinstance(some_data, dict) and isinstance(before[key], dict):
            diff[key] = {
                'children': build_diff(before[key], some_data),
                'status': 'modified',
            }
        else:
            diff[key] = {
                'new_value': some_data,
                'old_value': before[key],
                'status': 'modified',
            }
    return diff


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
