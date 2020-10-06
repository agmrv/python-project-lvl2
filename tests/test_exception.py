# -*- coding:utf-8 -*-

"""Exception test functions."""

from gendiff import generate_diff
from os.path import abspath


def test_file_not_found():
    """Test for 'File Not Found' case."""
    file1_abspath = abspath('tests/fixtures/nonexistent.json')
    file2_abspath = abspath('tests/fixtures/after.json')
    expected = ("File not found.\n"
                "No such file or directory: "
                "'/home/agmrv/python-project-lvl2/tests/fixtures/nonexistent.json'")
    assert (generate_diff(file1_abspath, file2_abspath)) == expected


def test_invalid_output_format():
    """Test for 'Invalid Output Format' case."""
    file1_abspath = abspath('tests/fixtures/before.json')
    file2_abspath = abspath('tests/fixtures/after.json')
    expected = ("Invalid output format: "
                "'invalid-format'.\nTry 'json', 'plain' or 'json-like'.")
    assert (generate_diff(
        file1_abspath,
        file2_abspath,
        output_format='invalid-format',
    )) == expected
