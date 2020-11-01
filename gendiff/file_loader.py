"""Module for load file."""

import json
from os.path import splitext

import yaml

from gendiff.converter_to_initial_format import convert


def parse(file_descriptor, extension):
    """Parse data according to extension.

    Args:
        file_descriptor: parsing data
        extension: file extension

    Returns:
        parsed data dictionary

    Raises:
        ValueError: unsupported extension
    """
    if extension == '.json':
        return json.load(file_descriptor)
    if extension in {'.yaml', '.yml'}:
        return yaml.safe_load(file_descriptor)
    raise ValueError(extension)


def load_converted_data(filepath):
    """Load converted file data from filepath.

    Args:
        filepath: path to file

    Returns:
        dict of file data
    """
    _, extension = splitext(filepath)

    with open(filepath) as file_descriptor:
        file_data = parse(file_descriptor, extension)
        convert(file_data)  # convert data to string initial format
        return file_data
