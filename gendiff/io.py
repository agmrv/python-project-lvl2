"""Module of the file reader."""

import json
from os.path import splitext

import yaml


def load(file_descriptor, extension):
    """Load data according to extension.

    Args:
        file_descriptor: parsing data
        extension: file extension

    Returns:
        loaded data dictionary

    Raises:
        ValueError: unsupported extension
    """
    if extension == '.json':
        return json.load(file_descriptor)

    if extension in {'.yaml', '.yml'}:
        return yaml.safe_load(file_descriptor)

    raise ValueError(
        "Unsupported file extension: '{0}'\n".format(extension)
        + "'.json' and '.yaml' are supported.",
    )


def read_data(filepath):
    """Open file and read data from filepath.

    Args:
        filepath: path to file

    Returns:
        dict from file data
    """
    _, extension = splitext(filepath)

    with open(filepath) as file_descriptor:
        return load(file_descriptor, extension)
