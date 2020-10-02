# -*- coding:utf-8 -*-

"""Module of Difference Builder."""


def has_children(element):
    """Сhecks if the element has children.

    Args:
        element: value to check

    Returns:
        Bool
    """
    return 'children' in element


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
