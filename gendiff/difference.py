"""Module of the difference dict builder."""

from collections import OrderedDict


def build(before_dict, after_dict):
    """Build the diff dict between before and after dicts.

    Args:
        before_dict: dict before change
        after_dict: dict after change

    Returns:
        diff dict
    """
    diff = {}
    before_keys = set(before_dict.keys())
    after_keys = set(after_dict.keys())

    for removed_key in before_keys.difference(after_keys):
        diff[removed_key] = ("removed", before_dict[removed_key])

    for added_key in after_keys.difference(before_keys):
        diff[added_key] = ("added", after_dict[added_key])

    for common_key in before_keys.intersection(after_keys):
        before_value = before_dict[common_key]
        after_value = after_dict[common_key]

        if before_value == after_value:
            diff[common_key] = ("unchanged", before_value)

        elif isinstance(before_value, dict) and isinstance(after_value, dict):
            diff[common_key] = ("nested", build(before_value, after_value))

        else:
            diff[common_key] = ("changed", (before_value, after_value))

    return OrderedDict(sorted(diff.items(), key=lambda pair: pair[0]))
