"""Module of Rendering to plain format function."""

from gendiff.builder_diff import has_children
from gendiff.upload_file import remove_dubleqoutes, was_string


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
        old_value = formatting(diff_value['old_value'])
        new_value = formatting(diff_value['new_value'])
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
    output_parts = []
    for key, diff_value in sorted(diff.items(), key=lambda pair: pair[0]):
        status = diff_value['status']
        if status == 'unmodified':
            continue
        if status == 'modified':
            if has_children(diff_value):
                new_path = '{0}{1}.'.format(path, key)
                output_parts.append(render(diff_value['children'], new_path))
            else:
                output_parts.append(generate_string_diff(path + key, status, diff_value))
        else:
            output_parts.append(generate_string_diff(
                path + key,
                status,
                diff_value['value'],
            ))
    return '\n'.join(output_parts)
