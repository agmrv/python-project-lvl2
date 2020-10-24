"""Module of rendering to JSON-like format function."""

from gendiff.value_converter import remove_doubleqoutes


def generate_string(some_key, some_value, status, depth):
    """Generate string from parameters.

    Args:
        some_key: key
        some_value: value
        status: status for choose sign (-, +, space)
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
    sign = signs[status]
    normalize_value = some_value

    if isinstance(some_value, dict):
        normalize_value = render(some_value, depth + 1)

    elif some_value.startswith('"') and some_value.endswith('"'):
        normalize_value = remove_doubleqoutes(some_value)

    return '  {0} {1}: {2}'.format(sign, some_key, normalize_value)


def render(diff, depth=0):
    """Render the diff and dict to stylish string.

    Args:
        diff: diff object or some dict
        depth: nesting level

    Returns:
        string stylish to output
    """
    lines = []

    for item_key, item_value in diff.items():

        if isinstance(item_value, tuple):
            status = item_value[0]
            current_value = item_value[1]

        else:
            status = 'unchanged'
            current_value = item_value

        if status == 'nested':
            nested_diff = render(current_value, depth + 1)
            lines.append(generate_string(item_key, nested_diff, status, depth))

        elif status == 'changed':
            lines.append(generate_string(item_key, current_value[0], 'removed', depth))
            lines.append(generate_string(item_key, current_value[1], 'added', depth))

        else:
            lines.append(generate_string(item_key, current_value, status, depth))

    indent = '{0}{1}'.format('\n', '    ' * depth)
    return '{0}{1}{2}{3}{4}'.format('{', indent, indent.join(lines), indent, '}')