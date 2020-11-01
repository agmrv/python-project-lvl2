"""Module of the difference generator."""

from gendiff.diff_structure_builder import build
from gendiff.file_loader import load_data
from gendiff.formatters import json, plain, stylish


def generate_diff(file_path1, file_path2, output_format='stylish'):
    """Generate the diff between file_path1 and file_path2 files.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        output_format: output format (json, plain or stylish)

    Returns:
        formatted diff
    """
    mapping_for_choose_formatter = {
        'json': json.render,
        'plain': plain.render,
        'stylish': stylish.render,
    }

    formatter = mapping_for_choose_formatter.get(output_format)

    if not formatter:
        return (
            "Invalid output format: '{0}'.\n".format(output_format)
            + "Try 'json', 'plain' or 'stylish'."
        )

    try:
        before = load_data(file_path1)
        after = load_data(file_path2)

    except ValueError as extension_error:
        return (
            "Unsupported file extension: '{0}'\n".format(extension_error)
            + "'.json' and '.yaml' are supported."
        )

    except FileNotFoundError as file_error:
        return "File not found.\n{0}: '{1}'".format(
            file_error.args[1],
            file_error.filename,
        )

    diff = build(before, after)

    return formatter(diff)
