# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

from gendiff import generate_diff
from os.path import abspath
import json


def test_generate_diff_JSON():
    """Test for flat JSON files."""
    file1_abspath = abspath('tests/fixtures/before.json')
    file2_abspath = abspath('tests/fixtures/after.json')
    expected_abspath = abspath('tests/fixtures/compare_JSON.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected


def test_generate_diff_YAML():
    """Test for flat YAML files."""
    file1_abspath = abspath('tests/fixtures/before.yml')
    file2_abspath = abspath('tests/fixtures/after.yml')
    expected_abspath = abspath('tests/fixtures/compare_YAML.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected
