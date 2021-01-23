"""Module of the difference generator."""

from gendiff.difference import build
from gendiff.formatters import mapping_for_choose_formatter
from gendiff.io import read_data
from gendiff.error_constants import FORMAT_ERROR


def generate_diff(file_path1, file_path2, output_format="stylish"):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        output_format: output format (json, plain or stylish)

    Returns:
        formatted diff
    """
    formatter = mapping_for_choose_formatter.get(output_format)

    if not formatter:
        return FORMAT_ERROR.format(output_format)

    try:
        before = read_data(file_path1)
        after = read_data(file_path2)

    except ValueError as extension_error:
        return extension_error.args[0]

    except FileNotFoundError as file_error:
        return "File not found.\n{0}: '{1}'".format(
            file_error.args[1],
            file_error.filename,
        )

    diff = build(before, after)

    return formatter(diff)
