"""Module for load file."""

import json
from os.path import splitext

import yaml

from gendiff.value_converter import convert_values


def parse(file_data, extension):
    """Parse data according to extension.

    Args:
        file_data: parsing data
        extension: file extension

    Returns:
        parsed data dictionary

    Raises:
        ValueError: unsupported extension
    """
    if extension == '.json':
        return json.load(file_data)
    if extension == '.yaml':
        return yaml.safe_load(file_data)
    if extension == '.yml':
        return yaml.safe_load(file_data)
    raise ValueError(extension)


def load_file(filepath):
    """Load file from filepath.

    Args:
        filepath: path to file

    Returns:
        dict
    """
    _, extension = splitext(filepath)

    with open(filepath) as file_descriptor:
        parsed_file = parse(file_descriptor, extension)
        convert_values(parsed_file)  # convert data to string initial format
        return parsed_file
