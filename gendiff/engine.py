"""Engine of 'Difference Generator'."""

from gendiff import agrparser
import json


def get_file_paths():
    """Return the file paths.
    """
    args = agrparser.get_args()
    return args.first_file, args.second_file


def get_json(file_path):
    """Return JSON Object  # ???
    """
    return json.load(open(file_path))


def generate_diff():
    """Generate the diff between first_file_path and second_file_path JSON files.
    
    Args:
        first_file_path: path to first JSON file
        second_file_path: path to second JSON file
    """
    first_file_path, second_file_path = get_file_paths()
    first_json = get_json(first_file_path)
    second_json = get_json(second_file_path)
    print(first_json)

    