# -*- coding:utf-8 -*-

"""Module for uplode file."""

import json
import types
from os.path import basename

import yaml

MAPPING_FOR_UPLOAD = types.MappingProxyType({
    'json': lambda path: json.load(open(path)),
    'yml': lambda path: yaml.safe_load(open(path)),
})

MAPPING_FOR_CONVERT_VALUE = types.MappingProxyType({
    'json': lambda element: json.dumps(element),
    'yml': lambda element: yaml.safe_dump(element).split('\n')[0],
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
        elif not isinstance(some_value, str):
            some_item[key] = MAPPING_FOR_CONVERT_VALUE[extension](some_value)


def get_file(filepath):
    """Upload file from filepath.

    Args:
        filepath: path to file.

    Returns:
        File Object.  # ???
    """
    filename = basename(filepath)
    _, extension = filename.split('.')
    file_object = MAPPING_FOR_UPLOAD[extension](filepath)
    convert_values(file_object, extension)  # convert data to initial format
    return file_object
