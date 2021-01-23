"""Module of rendering to JSON format function."""

import json


def render(diff):
    """Render the diff to json format.

    Args:
        diff: diff object

    Returns:
        string json format
    """
    return json.dumps(diff, ensure_ascii=False, indent="    ", sort_keys=True)
