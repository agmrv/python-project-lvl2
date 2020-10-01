# -*- coding:utf-8 -*-

"""Module of Rendering function."""


def has_children(element):
    return 'children' in element


def to_str_like_json(data, nesting_lvl):
    indent = '    ' * nesting_lvl
    if isinstance(data, dict):
        formatted_value_parts = []
        for data_key, data_value in data.items():
            formatted_value_parts.append(
                '{0}{1}: {2}'.format(
                    indent,
                    data_key,
                    to_str_like_json(data_value, nesting_lvl + 1),
                    ),
                )
        return '{0}{1}\n{2}{3}'.format(
            '{\n',
            '\n'.join(formatted_value_parts),
            '    ' * (nesting_lvl - 1),
            '}',
            )
    else:
        return data


    # old_value = isinstance(old_value, dict) ? 

    # new_line = '{0}  {1} {2}: {3}'.format(indent, sign, key, value)


def diff_to_str_like_json(data, nesting_lvl):
    """Render the diff to string like JSON.

    Args:
        diff: diff object
        nesting_lvl: nesting level

    Returns:
        String to output.
    """
    output_parts = []
    for key, data in data.items():
        status = data['status']
        indent = '    ' * nesting_lvl
        if status == 'removed':
            output_parts.append('{0}  - {1}: {2}'.format(
                indent,
                key,
                to_str_like_json(data['value'], nesting_lvl + 2),
                )
            )
        if status == 'added':
            output_parts.append('{0}  + {1}: {2}'.format(
                indent,
                key,
                to_str_like_json(data['value'], nesting_lvl + 2),
                )
            )
        if status == 'unmodified':
            output_parts.append('{0}    {1}: {2}'.format(
                indent,
                key,
                to_str_like_json(data['value'], nesting_lvl + 2),
                )
            )
        if status == 'modified':
            if has_children(data):
                output_parts.append('{0}    {1}: {2}'.format(
                    indent,
                    key,
                    diff_to_str_like_json(data['children'], nesting_lvl + 1),
                    ),
                )
            else:
                output_parts.append('{0}  - {1}: {2}'.format(
                    indent,
                    key,
                    to_str_like_json(data['old_value'], nesting_lvl + 2),
                    )
                )
                output_parts.append('{0}  + {1}: {2}'.format(
                    indent,
                    key,
                    to_str_like_json(data['new_value'], nesting_lvl + 2),
                    )
                )
    return '{0}\n{1}\n{2}{3}'.format('{', '\n'.join(output_parts), indent, '}')


def render(diff):
    return diff_to_str_like_json(diff, 0)


# def render(diff):
#     """Render the diff to string like JSON.

#     Args:
#         diff: diff object

#     Returns:
#         String to output.
#     """
#     output_parts = []
#     nesting_lvl = 2
#     for key, data in diff.items():
#         status = data['status']
#         if status == 'removed':
#             output_parts.append('  - {0}: {1}'.format(
#                 key,
#                 to_str_like_json(data['value'], nesting_lvl),
#                 )
#             )
#         if status == 'added':
#             output_parts.append('  + {0}: {1}'.format(
#                 key,
#                 to_str_like_json(data['value'], nesting_lvl),
#                 )
#             )
#         if status == 'unmodified':
#             output_parts.append('    {0}: {1}'.format(
#                 key,
#                 to_str_like_json(data['value'], nesting_lvl),
#                 )
#             )
#         if status == 'modified':
#             if has_children(data):
#                 output_parts.append('    {0}: {1}'.format(key, render(data['children'])))
#             else:
#                 output_parts.append('  - {0}: {1}'.format(
#                     key,
#                     to_str_like_json(data['old_value'], nesting_lvl),
#                     )
#                 )
#                 output_parts.append('  + {0}: {1}'.format(
#                     key,
#                     to_str_like_json(data['new_value'], nesting_lvl),
#                     )
#                 )
#     return '{0}\n{1}\n{2}'.format('{', '\n'.join(output_parts), '}')
