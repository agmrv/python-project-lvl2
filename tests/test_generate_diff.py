# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

from gendiff import generate_diff
from os.path import abspath
import json


def test_generate_diff():
    """Test for flat JSON files."""
    file1_abspath = abspath('tests/fixtures/file1.json')
    file2_abspath = abspath('tests/fixtures/file2.json')
    expected_abspath = abspath('tests/fixtures/compare_file1_and_file2.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected
