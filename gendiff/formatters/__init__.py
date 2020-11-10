"""Formatters package."""
from gendiff.formatters import json, plain, stylish

mapping_for_choose_formatter = {
    'json': json.render,
    'plain': plain.render,
    'stylish': stylish.render,
}
