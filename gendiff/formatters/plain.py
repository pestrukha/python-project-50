def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def handle_added(full_path, new_value):
    formatted_value = format_value(new_value)
    return f"Property '{full_path}' was added with value: {formatted_value}"


def handle_removed(full_path):
    return f"Property '{full_path}' was removed"


def handle_updated(full_path, old_value, new_value):
    formatted_old_value = format_value(old_value)
    formatted_new_value = format_value(new_value)
    return (f"Property '{full_path}' was updated. "
            f"From {formatted_old_value} to {formatted_new_value}")


def generate_messages(diff, path=""):
    messages = []
    for item in diff:
        key = item['key']
        full_path = f"{path}.{key}" if path else key
        status = item['status']

        if status == 'nested':
            nested_diff = item['nested']
            messages.extend(generate_messages(nested_diff, full_path))
        elif status == 'added':
            messages.append(handle_added(full_path, item['new_value']))
        elif status == 'removed':
            messages.append(handle_removed(full_path))
        elif status == 'updated':
            messages.append(handle_updated(
                full_path, item['old_value'], item['new_value']
            ))
    return messages


def convert_to_plain(diff):
    messages = generate_messages(diff)
    return '\n'.join(messages)
