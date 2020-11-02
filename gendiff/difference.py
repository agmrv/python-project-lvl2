"""Module of the difference structure builder."""

from collections import OrderedDict


def build(before, after):
    """Build the diff structure between before and after files.

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
            diff[common_key] = ('nested', build(before_value, after_value))

        else:
            diff[common_key] = ('changed', (before_value, after_value))

    return OrderedDict(sorted(diff.items(), key=lambda pair: pair[0]))
