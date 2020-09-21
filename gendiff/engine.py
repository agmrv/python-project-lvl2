# -*- coding:utf-8 -*-

"""Engine of 'Difference Generator'."""

import json


def get_json(file_path):
    """Get JSON from file_path.

    Args:
        file_path: path to file.

    Returns:
        Return JSON Object  # ???
    """
    return json.load(open(file_path))  # noqa: WPS515


def generate_diff(file_path1, file_path2):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        Return the diff.
    """
    compare = []
    first_json = get_json(file_path1)
    second_json = get_json(file_path2)
    common_json = first_json.copy()
    common_json.update(second_json)
    for key, some_data in common_json.items():
        if key not in second_json:
            compare.append('  - {0}: {1}'.format(key, some_data))
        elif key not in first_json:
            compare.append('  + {0}: {1}'.format(key, some_data))
        elif some_data == first_json[key]:
            compare.append('    {0}: {1}'.format(key, some_data))
        else:
            compare.append('  - {0}: {1}'.format(key, first_json[key]))
            compare.append('  + {0}: {1}'.format(key, some_data))

    return '{0}\n{1}\n{2}'.format('{', '\n'.join(compare), '}')
