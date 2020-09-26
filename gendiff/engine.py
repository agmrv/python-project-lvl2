# -*- coding:utf-8 -*-

"""Engine of 'Difference Generator'."""

from gendiff.upload_file import get_file


def generate_diff(file_path1, file_path2):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file

    Returns:
        Return the diff.
    """
    compare = []
    before = get_file(file_path1)
    after = get_file(file_path2)
    common = before.copy()
    common.update(after)
    for key, some_data in common.items():
        if key not in after:
            compare.append('  - {0}: {1}'.format(key, some_data))
        elif key not in before:
            compare.append('  + {0}: {1}'.format(key, some_data))
        elif some_data == before[key]:
            compare.append('    {0}: {1}'.format(key, some_data))
        else:
            compare.append('  - {0}: {1}'.format(key, before[key]))
            compare.append('  + {0}: {1}'.format(key, some_data))

    return '{0}\n{1}\n{2}'.format('{', '\n'.join(compare), '}')
