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


def yaml_convert_value(element):
    """Convert element to initial YAML format.

    Args:
        element: value to convert

    Returns:
        string
    """
    if isinstance(element, str):
        new_element = yaml.safe_dump(element).split('\n')[0]
        return '"{0}"'.format(new_element)
    return yaml.safe_dump(element).split('\n')[0]


MAPPING_FOR_CONVERT_VALUE = types.MappingProxyType({
    '.json': lambda element: json.dumps(element),
    '.yml': yaml_convert_value,
    '.yaml': yaml_convert_value,
})


def convert_values(some_item, extension):
    """Convert dict values to initial format.

    Args:
        some_item: dict to convert
        extension: file extension
    """
    for key, some_value in some_item.items():
        if isinstance(some_value, dict):
            convert_values(some_value, extension)
        else:
            some_item[key] = MAPPING_FOR_CONVERT_VALUE[extension](some_value)


def get_file(filepath):
    """Upload file from filepath.

    Args:
        filepath: path to file.

    Returns:
        File Object.  # ???
    """
    _, extension = splitext(filepath)
    with open(filepath) as file_descriptor:
        file_object = MAPPING_FOR_UPLOAD[extension](file_descriptor)
        convert_values(file_object, extension)  # convert data to initial format
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
