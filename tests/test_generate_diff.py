# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

from gendiff import generate_diff
import pytest


# flat files
before_json = 'tests/fixtures/before.json'
after_json = 'tests/fixtures/after.json'
before_yaml = 'tests/fixtures/before.yml'
after_yaml = 'tests/fixtures/after.yml'

# tree files
before_tree_json = 'tests/fixtures/before_tree.json'
after_tree_json = 'tests/fixtures/after_tree.json'
before_tree_yaml = 'tests/fixtures/before_tree.yml'
after_tree_yaml = 'tests/fixtures/after_tree.yml'

# comparisons
json = 'tests/fixtures/comparisons/compare_json.txt'
plain = 'tests/fixtures/comparisons/compare_plain.txt'
string = 'tests/fixtures/comparisons/compare_string.txt'
tree_json = 'tests/fixtures/comparisons/compare_tree_json.txt'
tree_plain = 'tests/fixtures/comparisons/compare_tree_plain.txt'
tree_string = 'tests/fixtures/comparisons/compare_tree.txt'

FLAT_FILES = [
    (before_json, after_json),
    (before_yaml, after_yaml),
]

FLAT_COMPARISONS = [
    (json, 'json'),
    (plain, 'plain'),
    (string, 'json-like'),
]

TREE_FILES = [
    (before_tree_json, after_tree_json),
    (before_tree_yaml, after_tree_yaml),
]

TREE_COMPARISONS = [
    (tree_json, 'json'),
    (tree_plain, 'plain'),
    (tree_string, 'json-like'),
]


@pytest.mark.parametrize('result, output_format', FLAT_COMPARISONS, ids=['json', 'plain', 'string'])
@pytest.mark.parametrize('before, after', FLAT_FILES, ids=['json', 'yaml'])
def test_generate_diff_for_flat_files(before, after, result, output_format):
    with open(result, mode='r', encoding='UTF-8') as r:
        expected = r.read()
        output = generate_diff(before, after, output_format)
        assert output == expected


@pytest.mark.parametrize('result, output_format', TREE_COMPARISONS, ids=['json', 'plain', 'string'])
@pytest.mark.parametrize('before, after', TREE_FILES, ids=['tree_json', 'tree_yaml'])
def test_generate_diff_for_tree_files(before, after, result, output_format):
    with open(result, mode='r', encoding='UTF-8') as r:
        expected = r.read()
        output = generate_diff(before, after, output_format)
        assert output == expected
