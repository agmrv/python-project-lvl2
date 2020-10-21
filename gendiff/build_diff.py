# -*- coding:utf-8 -*-

"""Module of the difference builder."""

from collections import OrderedDict

from gendiff.formatters import json_like_view, json_view, plain_view
from gendiff.load_file import load_file


def get_key_sets(before, after):
    """Generate a dictionary of key sets from files.

    Args:
        before: file before change
        after: file after change

    Returns:
        dict of key sets
    """
    before_keys = set(before.keys())
    after_keys = set(after.keys())
    return {
        'added': after_keys.difference(before_keys),
        'removed':  before_keys.difference(after_keys),
        'common': before_keys.intersection(after_keys),
    }


def build_diff(before, after):
    """Build the diff between before and after files.

    Args:
        before: file before change
        after: file after change

    Returns:
        diff
    """
    diff = {}
    key_sets = get_key_sets(before, after)

    for removed_key in key_sets['removed']:
        diff[removed_key] = {
            'value': before[removed_key],
            'status': 'removed',
        }

    for added_key in key_sets['added']:
        diff[added_key] = {
            'value': after[added_key],
            'status': 'added',
        }

    for common_key in key_sets['common']:
        before_value, after_value = before[common_key], after[common_key]
        if before_value == after_value:
            diff[common_key] = {
                'value': before_value,
                'status': 'unmodified',
            }
        elif isinstance(before_value, dict) and isinstance(after_value, dict):
            diff[common_key] = {
                'children': build_diff(before_value, after_value),
                'status': 'nested',
            }
        else:
            diff[common_key] = {
                'value': [('removed', before_value), ('added', after_value)],
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
        formatted diff
    """
    mapping_for_choose_render_function = {
        'plain': plain_view.render,
        'json-like': json_like_view.render,
        'json': json_view.render,
    }

    formatter = mapping_for_choose_render_function.get(output_format)
    if not formatter:
        return (
            "Invalid output format: '{0}'.\n".format(output_format)
            +
            "Try 'json', 'plain' or 'json-like'."
        )

    try:
        before = load_file(file_path1)
        after = load_file(file_path2)
    except FileNotFoundError as file_error:
        return "File not found.\n{0}: '{1}'".format(
            file_error.args[1],
            file_error.filename,
        )

    diff = build_diff(before, after)

    return formatter(diff)
