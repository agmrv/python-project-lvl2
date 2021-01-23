"""Module of rendering to plain format function."""


def formatting(element):
    """Convert the value to the desired output format.

    Args:
        element: value to convert

    Returns:
        formatted string
    """
    if isinstance(element, dict):
        return "[complex value]"

    elif element is None:
        return "null"

    elif isinstance(element, bool):
        return "true" if element else "false"

    return "'{0}'".format(element) if isinstance(element, str) else element


def generate_string(diff, path):
    """Generate string diff to plain format.

    Args:
        diff: diff object
        path: current path

    Returns:
        plain format string
    """
    lines = []

    for item_key, item_value in diff.items():
        type_, current_value = item_value
        current_path = path + item_key

        if type_ == "removed":
            lines.append("Property '{0}' was removed".format(current_path))

        elif type_ == "added":
            lines.append(
                "Property '{0}' was added with value: {1}".format(
                    current_path,
                    formatting(current_value),
                )
            )

        elif type_ == "changed":
            lines.append(
                "Property '{0}' was updated. From {1} to {2}".format(
                    current_path,
                    formatting(current_value[0]),
                    formatting(current_value[1]),
                )
            )

        elif type_ == "nested":
            lines.append(
                generate_string(
                    current_value,
                    "{0}.".format(current_path),
                )
            )

    return "\n".join(lines)


def render(diff):
    """Start render the diff to plain format string with path=''.

    Args:
        diff: diff object

    Returns:
        plain format string
    """
    return generate_string(diff, "")
