# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

from gendiff import generate_diff
from os.path import abspath


def test_generate_diff_JSON_json_like():
    """Test for flat JSON files."""
    file1_abspath = abspath('tests/fixtures/before.json')
    file2_abspath = abspath('tests/fixtures/after.json')
    expected_abspath = abspath('tests/fixtures/compare_JSON.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath, output_format='JSON-like')) == expected


def test_generate_diff_YAML_json_like():
    """Test for flat YAML files."""
    file1_abspath = abspath('tests/fixtures/before.yml')
    file2_abspath = abspath('tests/fixtures/after.yml')
    expected_abspath = abspath('tests/fixtures/compare_YAML.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected


def test_generate_diff_tree_JSON_json_like():
    """Test for tree JSON files."""
    file1_abspath = abspath('tests/fixtures/before_tree.json')
    file2_abspath = abspath('tests/fixtures/after_tree.json')
    expected_abspath = abspath('tests/fixtures/compare_tree_JSON.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected


def test_generate_diff_tree_YAML_json_like():
    """Test for tree JSON files."""
    file1_abspath = abspath('tests/fixtures/before_tree.yml')
    file2_abspath = abspath('tests/fixtures/after_tree.yml')
    expected_abspath = abspath('tests/fixtures/compare_tree_YAML.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath)) == expected


def test_generate_diff_JSON_plain():
    """Test for flat JSON files."""
    file1_abspath = abspath('tests/fixtures/before.json')
    file2_abspath = abspath('tests/fixtures/after.json')
    expected_abspath = abspath('tests/fixtures/compare_JSON_plain.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath, output_format='plain')) == expected


def test_generate_diff_YAML_plain():
    """Test for flat YAML files."""
    file1_abspath = abspath('tests/fixtures/before.yml')
    file2_abspath = abspath('tests/fixtures/after.yml')
    expected_abspath = abspath('tests/fixtures/compare_YAML_plain.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath, output_format='plain')) == expected


def test_generate_diff_tree_JSON_plain():
    """Test for flat JSON files."""
    file1_abspath = abspath('tests/fixtures/before_tree.json')
    file2_abspath = abspath('tests/fixtures/after_tree.json')
    expected_abspath = abspath('tests/fixtures/compare_tree_JSON_plain.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath, output_format='plain')) == expected


def test_generate_diff__tree_YAML_plain():
    """Test for flat YAML files."""
    file1_abspath = abspath('tests/fixtures/before_tree.yml')
    file2_abspath = abspath('tests/fixtures/after_tree.yml')
    expected_abspath = abspath('tests/fixtures/compare_tree_YAML_plain.txt')
    with open(expected_abspath, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
    assert (generate_diff(file1_abspath, file2_abspath, output_format='plain')) == expected
