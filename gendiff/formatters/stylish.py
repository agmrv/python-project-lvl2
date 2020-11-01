"""Module of rendering to JSON-like format function."""

from gendiff.converter_to_initial_format import remove_doubleqoutes


def make_line(some_key, some_value, type_, depth):
    """Generate string from parameters.

    Args:
        some_key: key
        some_value: value
        type_: type for choose sign (-, +, space)
        depth: nesting level

    Returns:
        string
    """
    signs = {
        'removed': '-',
        'added': '+',
        'unchanged': ' ',
        'nested': ' ',
    }
    sign = signs[type_]
    normalize_value = some_value

    if isinstance(some_value, dict):
        normalize_value = generate_string(some_value, depth + 1)

    elif some_value.startswith('"') and some_value.endswith('"'):
        normalize_value = remove_doubleqoutes(some_value)

    return '  {0} {1}: {2}'.format(sign, some_key, normalize_value)


def generate_string(diff, depth):
    """Generate string diff and dict to stylish format.

    Args:
        diff: diff object or some dict
        depth: nesting level

    Returns:
        stylish format string
    """
    lines = []

    for item_key, item_value in diff.items():

        if isinstance(item_value, tuple):
            type_ = item_value[0]
            current_value = item_value[1]

        else:
            type_ = 'unchanged'
            current_value = item_value

        if type_ == 'nested':
            nested_diff = generate_string(current_value, depth + 1)
            lines.append(make_line(item_key, nested_diff, type_, depth))

        elif type_ == 'changed':
            lines.append(make_line(item_key, current_value[0], 'removed', depth))
            lines.append(make_line(item_key, current_value[1], 'added', depth))

        else:
            lines.append(make_line(item_key, current_value, type_, depth))

    indent = '{0}{1}'.format('\n', '    ' * depth)
    return '{{{0}{1}{2}}}'.format(indent, indent.join(lines), indent)


def render(diff):
    """Start render the diff to stylish format string with depth=0.

    Args:
        diff: diff object or some dict

    Returns:
        stylish format string
    """
    return generate_string(diff, 0)
