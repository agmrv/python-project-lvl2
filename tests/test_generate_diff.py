# -*- coding:utf-8 -*-

"""The 'generate_diff' function tests."""

import json

import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    'before, after, compare_result, output_format',
    [
        (
            'tests/fixtures/before.json',
            'tests/fixtures/after.json',
            'tests/fixtures/comparisons/json.json',
            'json',
        ),
        (
            'tests/fixtures/before.json',
            'tests/fixtures/after.json',
            'tests/fixtures/comparisons/plain.txt',
            'plain',
        ),
        (
            'tests/fixtures/before.json',
            'tests/fixtures/after.json',
            'tests/fixtures/comparisons/stylish.txt',
            'stylish',
        ),
        (
            'tests/fixtures/before.yaml',
            'tests/fixtures/after.yml',
            'tests/fixtures/comparisons/json.json',
            'json',
        ),
        (
            'tests/fixtures/before.yaml',
            'tests/fixtures/after.yml',
            'tests/fixtures/comparisons/plain.txt',
            'plain',
        ),
        (
            'tests/fixtures/before.yaml',
            'tests/fixtures/after.yml',
            'tests/fixtures/comparisons/stylish.txt',
            'stylish',
        ),
        (
            'tests/fixtures/before_tree.json',
            'tests/fixtures/after_tree.json',
            'tests/fixtures/comparisons/tree_json.json',
            'json',
        ),
        (
            'tests/fixtures/before_tree.json',
            'tests/fixtures/after_tree.json',
            'tests/fixtures/comparisons/tree_plain.txt',
            'plain',
        ),
        (
            'tests/fixtures/before_tree.json',
            'tests/fixtures/after_tree.json',
            'tests/fixtures/comparisons/tree_stylish.txt',
            'stylish',
        ),
        (
            'tests/fixtures/before_tree.yml',
            'tests/fixtures/after_tree.yml',
            'tests/fixtures/comparisons/tree_json.json',
            'json',
        ),
        (
            'tests/fixtures/before_tree.yml',
            'tests/fixtures/after_tree.yml',
            'tests/fixtures/comparisons/tree_plain.txt',
            'plain',
        ),
        (
            'tests/fixtures/before_tree.yml',
            'tests/fixtures/after_tree.yml',
            'tests/fixtures/comparisons/tree_stylish.txt',
            'stylish',
        ),
    ],
    ids=[
        'json->json', 'json->plain', 'json->stylish',
        'yaml->json', 'yaml->plain', 'yaml->stylish',
        'tree_json->json', 'tree_json->plain', 'tree_json->stylish',
        'tree_yaml->json', 'tree_yaml->plain', 'tree_yaml->stylish',
    ],
)
def test_generate_diff(before, after, compare_result, output_format):
    """Test for 'generate_diff' function.

    Args:
        before: before file path
        after: after file path
        compare_result: compare file path
        output_format: output format
    """
    output = generate_diff(before, after, output_format)

    with open(compare_result, mode='r', encoding='UTF-8') as compare:

        if output_format == 'json':
            expected = json.load(compare)
            assert json.loads(output) == expected

        else:
            expected = compare.read()
            assert output == expected
