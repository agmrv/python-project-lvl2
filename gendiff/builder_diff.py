# -*- coding:utf-8 -*-

"""Module of Difference Builder."""

from gendiff.rendering import render
from gendiff.upload_file import get_file


def build_diff(before, after):
    """Build the diif between before and after files.

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


def generate_diff(file_path1, file_path2):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        Return the diff.
    """
    before = get_file(file_path1)
    after = get_file(file_path2)
    return render(build_diff(before, after))
