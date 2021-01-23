"""Difference test."""

import pytest

from gendiff.difference import build
from gendiff.io import read_data
from tests.fixtures.diff import diff as expected_diff


@pytest.mark.parametrize(
    "before_dict, after_dict, expected_diff",
    [
        (
            read_data("tests/fixtures/before.json"),
            read_data("tests/fixtures/after.json"),
            expected_diff,
        ),
        (
            read_data("tests/fixtures/before.yaml"),
            read_data("tests/fixtures/after.yml"),
            expected_diff,
        ),
    ],
    ids=["JSON", "YAML"],
)
def test_difference(before_dict, after_dict, expected_diff):
    """Test difference build function.

    Args:
        before_dict: before dict
        after_dict: after dict
        expected_diff: expected diff dict
    """
    assert build(before_dict, after_dict) == expected_diff
