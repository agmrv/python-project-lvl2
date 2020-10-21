# -*- coding:utf-8 -*-

"""Module for uplode file."""

import json
import types
from os.path import splitext

import yaml

MAPPING_FOR_UPLOAD = types.MappingProxyType({
    '.json': lambda fd: json.load(fd),
    '.yml': lambda fd: yaml.safe_load(fd),
    '.yaml': lambda fd: yaml.safe_load(fd),
})


def to_string(value_to_convert):
    """Convert value to string initial format.

    Args:
        value_to_convert: value to convert

    Returns:
        correct string
    """
    if value_to_convert is None:
        return 'null'
    elif isinstance(value_to_convert, bool):
        return 'true' if value_to_convert else 'false'
    elif isinstance(value_to_convert, str):
        return '"{0}"'.format(value_to_convert)
    return str(value_to_convert)


def convert_values(dict_to_convert):
    """Convert dict values to string initial format.

    Args:
        dict_to_convert: dict to convert
    """
    for item_key, item_value in dict_to_convert.items():
        if isinstance(item_value, dict):
            convert_values(item_value)
        else:
            dict_to_convert[item_key] = to_string(item_value)


def load_file(filepath):
    """Load file from filepath.

    Args:
        filepath: path to file.

    Returns:
        dict
    """
    _, extension = splitext(filepath)
    with open(filepath) as file_descriptor:
        file_object = MAPPING_FOR_UPLOAD[extension](file_descriptor)
        convert_values(file_object)  # convert data to string initial format
        return file_object


def was_string(element_to_check):
    """Check if it was a string before converting.

    Needed for correct output format with or without quotes
    in formatter functions.

    Args:
        element_to_check: value for check

    Returns:
        bool
    """
    return element_to_check.startswith('"') and element_to_check.endswith('"')


def remove_dubleqoutes(element_to_change):
    """Remove duble quotes from string.

    Needed for correct output format with or without quotes
    in formatter functions.

    Args:
        element_to_change: string to change

    Returns:
        string
    """
    return element_to_change[1:-1]
