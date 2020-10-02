# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

from gendiff import generate_diff
from os.path import abspath


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


def test_generate_diff_tree_JSON():
    """Test for tree JSON files."""
    file1_abspath = abspath('tests/fixtures/before_tree.json')
    file2_abspath = abspath('tests/fixtures/after_tree.json')
    expected_abspath = abspath('tests/fixtures/compare_tree_JSON.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected


def test_generate_diff_tree_YAML():
    """Test for tree JSON files."""
    file1_abspath = abspath('tests/fixtures/before_tree.yml')
    file2_abspath = abspath('tests/fixtures/after_tree.yml')
    expected_abspath = abspath('tests/fixtures/compare_tree_YAML.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected
