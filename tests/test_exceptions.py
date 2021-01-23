"""Exception test functions."""

from os import getcwd
from os.path import abspath

import pytest

from gendiff import generate_diff
from gendiff.error_constants import VALUE_ERROR, FORMAT_ERROR, NOT_FOUND_ERROR


@pytest.mark.parametrize(
    "before, after, output_format, expected",
    [
        (
            "tests/fixtures/before.json",
            "tests/fixtures/after.json",
            "invalid-format",
            FORMAT_ERROR.format("invalid-format"),
        ),
        (
            "tests/fixtures/before.xml",
            "tests/fixtures/after.json",
            "stylish",
            VALUE_ERROR.format(".xml"),
        ),
        (
            abspath("tests/fixtures/nonexistent.json"),
            abspath("tests/fixtures/after.json"),
            "stylish",
            NOT_FOUND_ERROR.format(getcwd()),
        ),
    ],
    ids=[
        "Invalid Output Format",
        "Unsuppported File Extension",
        "File Not Found",
    ],
)
def test_exception(before, after, output_format, expected):
    """Test exception.

    Args:
        before: before filepath
        after: after filepath
        output_format: output format
        expected: expected string
    """
    assert generate_diff(before, after, output_format) == expected
