# -*- coding:utf-8 -*-

"""Module of Difference Builder."""

from collections import OrderedDict

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
    before_keys = set(before.keys())
    after_keys = set(after.keys())

    removed_keys = before_keys.difference(after_keys)
    for removed_key in removed_keys:
        diff[removed_key] = {
            'value': before[removed_key],
            'status': 'removed',
        }

    added_keys = after_keys.difference(before_keys)
    for added_key in added_keys:
        diff[added_key] = {
            'value': after[added_key],
            'status': 'added',
        }

    common_keys = before_keys.intersection(after_keys)
    for common_key in common_keys:
        before_value = before[common_key]
        after_value = after[common_key]
        if before_value == after_value:
            diff[common_key] = {
                'value': before_value,
                'status': 'unmodified',
            }
        elif isinstance(before_value, dict) and isinstance(after_value, dict):
            diff[common_key] = {
                'children': build_diff(before_value, after_value),
                'status': 'modified',
            }
        else:
            diff[common_key] = {
                'new_value': after_value,
                'old_value': before_value,
                'status': 'modified',
            }

    return OrderedDict(sorted(diff.items(), key=lambda pair: pair[0]))


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
