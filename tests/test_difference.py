"""Difference test."""


from collections import OrderedDict

import pytest

from gendiff.difference import build
from gendiff.file_reader import read_data

diff = OrderedDict([
    ('common', ('nested', OrderedDict([
        ('follow', ('added', False)),
        ('setting1', ('unchanged', 'Value 1')),
        ('setting2', ('removed', 200)),
        ('setting3', ('changed', (True, {'key': 'value'}))),
        ('setting4', ('added', 'blah blah')),
        ('setting5', ('added', {'key5': 'value5'})),
        ('setting6', ('nested', OrderedDict([
            ('doge', ('nested', OrderedDict([
                ('wow', ('changed', ('too much', 'so much'))),
            ]))),
            ('key', ('unchanged', 'value')),
            ('ops', ('added', 'vops')),
        ]))),
    ]))),
    ('group1', ('nested', OrderedDict([
        ('baz', ('changed', ('bas', 'bars'))),
        ('foo', ('unchanged', 'bar')),
        ('nest', ('changed', ({'key': 'value'}, 'str'))),
    ]))),
    ('group2', ('removed', {
        'abc': 12345,
        'deep': {'id': 45},
    })),
    ('group3', ('added', {
        'fee': 100500,
        'deep': {'id': {'number': 45}},
    })),
    ('тест', ('added', None)),
])


@pytest.mark.parametrize(
    'before_dict, after_dict, expected_diff',
    [
        (
            read_data('tests/fixtures/before.json'),
            read_data('tests/fixtures/after.json'),
            diff,
        ),
        (
            read_data('tests/fixtures/before.yaml'),
            read_data('tests/fixtures/after.yml'),
            diff,
        ),
    ],
    ids=['JSON', 'YAML'],
)
def test_difference(before_dict, after_dict, expected_diff):
    """Test difference build function.

    Args:
        before_dict: before dict
        after_dict: after dict
        expected_diff: expected diff dict
    """
    assert build(before_dict, after_dict) == expected_diff
