# -*- coding:utf-8 -*-

"""Exception test functions."""

from os import getcwd
from os.path import abspath

from gendiff import generate_diff


def test_invalid_output_format():
    """Test for 'Invalid Output Format' case."""
    file1 = 'tests/fixtures/before.json'
    file2 = 'tests/fixtures/after.json'
    expected = (
        "Invalid output format: 'invalid-format'.\n"
        +
        "Try 'json', 'plain' or 'stylish'."
    )
    assert generate_diff(file1, file2, output_format='invalid-format') == expected


def test_unsupported_file_extension():
    """Test for 'Unsuppported File Extension' case."""
    file1 = 'tests/fixtures/before.xml'
    file2 = 'tests/fixtures/after.json'
    expected = (
        "Unsupported file extension: '.xml'\n"
        +
        "'.json' and '.yaml' are supported."
    )
    assert generate_diff(file1, file2) == expected


def test_file_not_found():
    """Test for 'File Not Found' case."""
    file1_abspath = abspath('tests/fixtures/nonexistent.json')
    file2_abspath = abspath('tests/fixtures/after.json')
    cwd = getcwd()
    expected = (
        'File not found.\nNo such file or directory: '
        +
        "'{0}/tests/fixtures/nonexistent.json'".format(cwd)
    )
    assert generate_diff(file1_abspath, file2_abspath) == expected


