"""Engine of 'Difference Generator'."""

import json


def get_json(file_path):
    """Return JSON Object  # ???
    """
    return json.load(open(file_path))


def generate_diff(file_path1, file_path2):
    """Generate the diff between file_path1 and file_path2 files.
    
    Args:
        file_path1: path to first file
        file_path2: path to second file
    """
    first_json = get_json(file_path1)
    second_json = get_json(file_path2)
    common_json = first_json.copy()
    common_json.update(second_json)
    compare = []
    for key, value in common_json.items():
        if key not in second_json:
            compare.append('  - {0}: {1}'.format(key, value))
        elif key not in first_json:
            compare.append('  + {0}: {1}'.format(key, value))
        else:
            if value == first_json[key]:
                compare.append('    {0}: {1}'.format(key, value))
            else:
                compare.append('  - {0}: {1}'.format(key, first_json[key]))
                compare.append('  + {0}: {1}'.format(key, value))

    diff = '{0}\n{1}\n{2}'.format('{', '\n'.join(compare), '}')
    return diff
