"""Module of rendering to JSON-like format function."""

import types

from gendiff.load_file import remove_dubleqoutes, was_string

MAPPING_FOR_CHOOSE_SIGN = types.MappingProxyType({
    'removed': '-',
    'added': '+',
    'unmodified': ' ',
    'nested': ' ',
})


def to_string(strings, nesting_lvl):
    """Generate finish string like JSON adding curly braces.

    Args:
        strings: list of strings
        nesting_lvl: nesting level

    Returns:
        string like JSON
    """
    indent = '    ' * nesting_lvl
    return '{0}\n{1}\n{2}{3}'.format('{', '\n'.join(strings), indent, '}')


def make_line(some_key, some_value, status, nesting_lvl):
    """Generate string line from parameters.

    Args:
        some_key: key
        some_value: value
        status: status for choose sign (-, +, space)
        nesting_lvl: nesting level

    Returns:
        string
    """
    sign = MAPPING_FOR_CHOOSE_SIGN[status]
    indent = '    ' * nesting_lvl
    normalize_value = value_to_string_like_json(some_value, nesting_lvl + 1)
    return '{0}  {1} {2}: {3}'.format(indent, sign, some_key, normalize_value)


def value_to_string_like_json(some_value, nesting_lvl):
    """Render the value to string like JSON.

    Args:
        some_value: value to render
        nesting_lvl: nesting level

    Returns:
        string like JSON
    """
    if isinstance(some_value, dict):
        lines = []
        for item_key, item_value in some_value.items():
            normalize_value = value_to_string_like_json(item_value, nesting_lvl + 1)
            lines.append(
                make_line(item_key, normalize_value, 'unmodified', nesting_lvl),
            )
        return to_string(lines, nesting_lvl)

    if was_string(some_value):
        return remove_dubleqoutes(some_value)

    return some_value


def diff_to_string(diff, nesting_lvl):
    """Render the diff to string like JSON.

    Args:
        diff: diff object
        nesting_lvl: nesting level

    Returns:
        string like JSON to output
    """
    lines = []

    for item_key, item_value in diff.items():
        status = item_value['status']

        if status == 'nested':
            nested_diff = diff_to_string(item_value['children'], nesting_lvl + 1)
            lines.append(make_line(item_key, nested_diff, status, nesting_lvl))

        elif status == 'modified':
            for current_status, current_value in item_value['value']:
                lines.append(
                    make_line(item_key, current_value, current_status, nesting_lvl),
                )

        else:
            lines.append(
                make_line(item_key, item_value['value'], status, nesting_lvl),
            )

    return to_string(lines, nesting_lvl)


def render(diff):
    """Start the render diff.

    Args:
        diff: diff object

    Returns:
        string to output
    """
    return diff_to_string(diff, 0)
