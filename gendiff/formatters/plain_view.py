"""Module of Rendering to plain format function."""

from gendiff.builder_diff import has_children


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
        return "Property '{0}' was {1} with value: {2}".format(path, status, diff_value)
    if status == 'modified':
        old_value = diff_value['old_value']
        new_value = diff_value['new_value']
        return "Property '{0}' was updated. From {1} to {2}".format(
            path,
            '[complex value]' if isinstance(old_value, dict) else old_value,
            '[complex value]' if isinstance(new_value, dict) else new_value,
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
                output_parts.extend(render(diff_value['children'], path + key))
            else:
                output_parts.append(generate_string_diff(path + key, status, diff_value))
        else:
            output_parts.append(generate_string_diff(
                path + key,
                status,
                diff_value['value'],
            ))
    return '\n'.join(output_parts)
