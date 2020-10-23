# -*- coding:utf-8 -*-

"""Module of the difference builder."""

from collections import OrderedDict

from gendiff.file_loader import load_file
from gendiff.formatters import json, plain, stylish


def build_diff(before, after):
    """Build the diff between before and after files.

    Args:
        before: file before change
        after: file after change

    Returns:
        diff
    """
    diff = {}
    before_keys = set(before.keys())
    after_keys = set(after.keys())

    for removed_key in before_keys.difference(after_keys):
        diff[removed_key] = ('removed', before[removed_key])

    for added_key in after_keys.difference(before_keys):
        diff[added_key] = ('added', after[added_key])

    for common_key in before_keys.intersection(after_keys):
        before_value, after_value = before[common_key], after[common_key]

        if before_value == after_value:
            diff[common_key] = ('unchanged', before_value)

        elif isinstance(before_value, dict) and isinstance(after_value, dict):
            diff[common_key] = ('nested', build_diff(before_value, after_value))

        else:
            diff[common_key] = ('changed', (before_value, after_value))

    return OrderedDict(sorted(diff.items(), key=lambda pair: pair[0]))


def generate_diff(file_path1, file_path2, output_format='stylish'):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        output_format: output format (json, plain or stylish)

    Returns:
        formatted diff
    """
    mapping_for_choose_render_function = {
        'json': json.render,
        'plain': plain.render,
        'stylish': stylish.render,
    }

    formatter = mapping_for_choose_render_function.get(output_format)
    if not formatter:
        return (
            "Invalid output format: '{0}'.\n".format(output_format)
            + "Try 'json', 'plain' or 'stylish'."
        )

    try:
        before = load_file(file_path1)
        after = load_file(file_path2)
    except ValueError as extension_error:
        return (
            "Unsupported file extension: '{0}'\n".format(extension_error)
            + "'.json' and '.yaml' are supported."
        )
    except FileNotFoundError as file_error:
        return "File not found.\n{0}: '{1}'".format(
            file_error.args[1],
            file_error.filename,
        )

    diff = build_diff(before, after)

    return formatter(diff)
