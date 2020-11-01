"""Module for convert values to string initial format."""


def to_string(value_to_convert):
    """Convert value to string initial format.

    Args:
        value_to_convert: value to convert

    Returns:
        correct string
    """
    if value_to_convert is None:
        return 'null'
    elif isinstance(value_to_convert, bool):
        return 'true' if value_to_convert else 'false'
    elif isinstance(value_to_convert, str):
        return '"{0}"'.format(value_to_convert)
    return str(value_to_convert)


def convert(dict_to_convert):
    """Convert dict values to string initial format.

    Args:
        dict_to_convert: dict to convert
    """
    for item_key, item_value in dict_to_convert.items():
        if isinstance(item_value, dict):
            convert(item_value)
        else:
            dict_to_convert[item_key] = to_string(item_value)


def remove_doubleqoutes(element_to_change):
    """Remove dublequotes from string.

    Needed for correct output format with or without quotes
    in formatter functions.

    Args:
        element_to_change: string to change

    Returns:
        string
    """
    return element_to_change[1:-1]
