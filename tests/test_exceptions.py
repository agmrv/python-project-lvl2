"""Exception test functions."""

from os import getcwd
from os.path import abspath

import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    "before, after, output_format, expected",
    [
        (
            "tests/fixtures/before.json",
            "tests/fixtures/after.json",
            "invalid-format",
            "Invalid output format: 'invalid-format'.\n"
            + "Try 'json', 'plain' or 'stylish'.",
        ),
        (
            "tests/fixtures/before.xml",
            "tests/fixtures/after.json",
            "stylish",
            "Unsupported file extension: '.xml'\n"
            + "'.json' and '.yaml' are supported.",
        ),
        (
            abspath("tests/fixtures/nonexistent.json"),
            abspath("tests/fixtures/after.json"),
            "stylish",
            "File not found.\nNo such file or directory: "
            + "'{0}/tests/fixtures/nonexistent.json'".format(getcwd()),
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
