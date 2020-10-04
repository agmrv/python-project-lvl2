"""Module of Rendering to JSON-like format function."""

import types

from gendiff.builder_diff import has_children
from gendiff.upload_file import was_string, remove_dubleqoutes

MAPPING_FOR_CHOOSE_SIGN = types.MappingProxyType({
    'removed': '-',
    'added': '+',
    'unmodified': ' ',
})


def generate_string_diff(indent, sign, key, some_value):
    """Generate string representation from parameters.

    Args:
        indent: indent from spaces
        sign: sign (-, +, space)
        key: key
        some_value: value

    Returns:
        string
    """
    return '{0}  {1} {2}: {3}'.format(indent, sign, key, some_value)


def value_to_str_like_json(value_data, nesting_lvl):
    """Render the value to string like JSON.

    Args:
        value_data: value to render
        nesting_lvl: nesting level

    Returns:
        string like JSON.
    """
    indent = '    ' * nesting_lvl
    if isinstance(value_data, dict):
        formatted_value_parts = []
        for data_key, data_value in value_data.items():
            formatted_value_parts.append(
                '{0}{1}: {2}'.format(
                    indent,
                    data_key,
                    value_to_str_like_json(data_value, nesting_lvl + 1),
                    ),
                )
        return '{0}{1}\n{2}{3}'.format(
            '{\n',
            '\n'.join(formatted_value_parts),
            '    ' * (nesting_lvl - 1),
            '}',
            )
    if was_string(value_data):
        return remove_dubleqoutes(value_data)
    return value_data


def diff_to_str_like_json(diff_data, nesting_lvl):
    """Render the diff to string like JSON.

    Args:
        diff_data: diff object
        nesting_lvl: nesting level

    Returns:
        String like JSON to output.
    """
    output_parts = []
    for data_key, data_value in sorted(diff_data.items(), key=lambda pair: pair[0]):
        status = data_value['status']
        indent = '    ' * nesting_lvl
        if status == 'modified':
            if has_children(data_value):
                output_parts.append(generate_string_diff(
                    indent,
                    ' ',
                    data_key,
                    diff_to_str_like_json(data_value['children'], nesting_lvl + 1),
                    ),
                )
            else:
                output_parts.append(generate_string_diff(
                    indent,
                    MAPPING_FOR_CHOOSE_SIGN['removed'],
                    data_key,
                    value_to_str_like_json(data_value['old_value'], nesting_lvl + 2),
                    ),
                )
                output_parts.append(generate_string_diff(
                    indent,
                    MAPPING_FOR_CHOOSE_SIGN['added'],
                    data_key,
                    value_to_str_like_json(data_value['new_value'], nesting_lvl + 2),
                    ),
                )
        else:
            output_parts.append(generate_string_diff(
                indent,
                MAPPING_FOR_CHOOSE_SIGN[status],
                data_key,
                value_to_str_like_json(data_value['value'], nesting_lvl + 2),
                ),
            )
    return '{0}\n{1}\n{2}{3}'.format('{', '\n'.join(output_parts), indent, '}')


def render(diff):
    """Start the render diff.

    Args:
        diff: diff object

    Returns:
        String to output
    """
    return diff_to_str_like_json(diff, 0)
