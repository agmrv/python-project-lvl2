"""Formatters test."""

import json as j

import pytest

from gendiff.formatters import json, plain, stylish
from test_difference import diff

mapping_for_choose_formatter = {
    'json': json.render,
    'plain': plain.render,
    'stylish': stylish.render,
}


@pytest.mark.parametrize(
    'output_format, expected_output',
    [
        ('json', 'tests/fixtures/comparisons/json.json'),
        ('plain', 'tests/fixtures/comparisons/plain.txt'),
        ('stylish', 'tests/fixtures/comparisons/stylish.txt'),
    ],
    ids=['json', 'plain', 'stylish'],
)
def test_formatters(output_format, expected_output):
    """Test formatter render functions.

    Args:
        output_format: output format
        expected_output: expected output path
    """
    output = mapping_for_choose_formatter.get(output_format)(diff)

    with open(expected_output, mode='r', encoding='UTF-8') as expected:

        if output_format == 'json':
            assert j.loads(output) == j.load(expected)

        else:
            assert output == expected.read()
