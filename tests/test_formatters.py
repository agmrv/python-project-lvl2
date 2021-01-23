"""Formatters test."""

import json as j

import pytest

from gendiff.formatters import mapping_for_choose_formatter
from tests.fixtures.diff import diff


@pytest.mark.parametrize(
    "output_format, expected_output, diff",
    [
        ("json", "tests/fixtures/comparisons/json.json", diff),
        ("plain", "tests/fixtures/comparisons/plain.txt", diff),
        ("stylish", "tests/fixtures/comparisons/stylish.txt", diff),
    ],
    ids=["json", "plain", "stylish"],
)
def test_formatters(output_format, expected_output, diff):
    """Test formatter render functions.

    Args:
        output_format: output format
        expected_output: expected output path
        diff: diff dict
    """
    output = mapping_for_choose_formatter.get(output_format)(diff)

    with open(expected_output, mode="r", encoding="UTF-8") as expected:

        if output_format == "json":
            assert j.loads(output) == j.load(expected)

        else:
            assert output == expected.read()
