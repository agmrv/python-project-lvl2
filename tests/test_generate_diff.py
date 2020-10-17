# -*- coding:utf-8 -*-

"""'generate_diff' function tests."""

import pytest

from gendiff import generate_diff

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

flat_files = [
    (before_json, after_json),
    (before_yaml, after_yaml),
]

flat_comparisons = [
    (json, 'json'),
    (plain, 'plain'),
    (string, 'json-like'),
]

tree_files = [
    (before_tree_json, after_tree_json),
    (before_tree_yaml, after_tree_yaml),
]

tree_comparisons = [
    (tree_json, 'json'),
    (tree_plain, 'plain'),
    (tree_string, 'json-like'),
]


@pytest.mark.parametrize(
    'compare_result, output_format',
    flat_comparisons,
    ids=['json', 'plain', 'string'],
)
@pytest.mark.parametrize('before, after', flat_files, ids=['json', 'yaml'])
def test_generate_diff_for_flat_files(before, after, compare_result, output_format):
    """Test for flat files.

    Args:
        before: before file path
        after: after file path
        compare_result: compare file path
        output_format: output format
    """
    with open(compare_result, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
        output = generate_diff(before, after, output_format)
        assert output == expected  # noqa: S101


@pytest.mark.parametrize(
    'compare_result, output_format',
    tree_comparisons,
    ids=['json', 'plain', 'string'],
)
@pytest.mark.parametrize('before, after', tree_files, ids=['tree_json', 'tree_yaml'])
def test_generate_diff_for_tree_files(before, after, compare_result, output_format):
    """Test for tree files.

    Args:
        before: before file path
        after: after file path
        compare_result: compare file path
        output_format: output format
    """
    with open(compare_result, mode='r', encoding='UTF-8') as compare:
        expected = compare.read()
        output = generate_diff(before, after, output_format)
        assert output == expected  # noqa: S101
