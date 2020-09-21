# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

from gendiff import generate_diff
import json


def test_generate_diff():
    """Test for flat JSON files."""
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/compare_file1_and_file2.txt', mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file_path1, file_path2)) == expected
