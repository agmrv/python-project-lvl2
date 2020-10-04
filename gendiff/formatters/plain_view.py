"""Module of Rendering to plain format function."""

from gendiff.builder_diff import has_children
from gendiff.upload_file import was_string, remove_dubleqoutes


def formatting(data):
    """Converts the value to the desired output format.

    Args:
        data: value to convert

    Returns:
        formatted string
    """
    if isinstance(data, dict):
        return '[complex value]'
    if was_string(data):
        return f"'{remove_dubleqoutes(data)}'"
    return data


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
        return f"Property '{path}' was {status}"
    if status == 'added':
        return f"Property '{path}' was {status} with value: {formatting(diff_value)}"
    if status == 'modified':
        old_value = formatting(diff_value['old_value'])
        new_value = formatting(diff_value['new_value'])
        return f"Property '{path}' was updated. From {old_value} to {new_value}"


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
                output_parts.append(render(diff_value['children'], path + f'{key}.'))
            else:
                output_parts.append(generate_string_diff(path + key, status, diff_value))
        else:
            output_parts.append(generate_string_diff(
                path + key,
                status,
                diff_value['value'],
            ))
    return '\n'.join(output_parts)
