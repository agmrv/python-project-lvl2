"""Module of Rendering to plain format function."""

from gendiff.load_file import remove_dubleqoutes, was_string


def formatting(element):
    """Convert the value to the desired output format.

    Args:
        element: value to convert

    Returns:
        formatted string
    """
    if isinstance(element, dict):
        return '[complex value]'

    if was_string(element):
        return "'{0}'".format(remove_dubleqoutes(element))

    return element


def generate_string_diff(path, status, diff_value):
    """Generate the text string.

    Args:
        path: current path
        status: element status
        diff_value: current element

    Returns:
        string
    """
    if status == 'removed':
        return "Property '{0}' was {1}".format(path, status)

    if status == 'added':
        return "Property '{0}' was {1} with value: {2}".format(
            path,
            status,
            formatting(diff_value),
        )

    if status == 'modified':
        old_value = formatting(diff_value[0][1])
        new_value = formatting(diff_value[1][1])
        return "Property '{0}' was updated. From {1} to {2}".format(
            path,
            old_value,
            new_value,
        )


def render(diff, path=''):
    """Render the diff to string.

    Args:
        diff: diff object
        path: current path

    Returns:
        string
    """
    lines = []

    for item_key, item_value in diff.items():
        status = item_value['status']

        if status == 'nested':
            lines.append(render(
                item_value.get('children'),
                '{0}{1}.'.format(path, item_key),
            ))

        elif status != 'unmodified':
            lines.append(generate_string_diff(
                path + item_key,
                status,
                item_value['value'],
            ))

    return '\n'.join(lines)
