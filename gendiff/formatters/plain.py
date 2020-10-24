"""Module of rendering to plain format function."""

from gendiff.value_converter import remove_doubleqoutes


def formatting(element):
    """Convert the value to the desired output format.

    Args:
        element: value to convert

    Returns:
        formatted string
    """
    if isinstance(element, dict):
        return '[complex value]'

    if element.startswith('"') and element.endswith('"'):
        return "'{0}'".format(remove_doubleqoutes(element))

    return element


def render(diff, path=''):
    """Render the diff to plain format string.

    Args:
        diff: diff object
        path: current path

    Returns:
        string
    """
    lines = []

    for item_key, item_value in diff.items():
        type_ = item_value[0]
        current_value = item_value[1]
        current_path = path + item_key

        if type_ == 'removed':
            lines.append("Property '{0}' was removed".format(current_path))

        elif type_ == 'added':
            lines.append("Property '{0}' was added with value: {1}".format(
                current_path,
                formatting(current_value),
            ))

        elif type_ == 'changed':
            lines.append("Property '{0}' was updated. From {1} to {2}".format(
                current_path,
                formatting(current_value[0]),
                formatting(current_value[1]),
            ))

        elif type_ == 'nested':
            lines.append(render(
                current_value,
                '{0}.'.format(current_path),
            ))

    return '\n'.join(lines)
