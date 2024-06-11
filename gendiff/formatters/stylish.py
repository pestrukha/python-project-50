def format_value(value, indent_level):
    indent = ' ' * (indent_level * 4)
    if isinstance(value, dict):
        items = [
            f'{indent}    {k}: {format_value(v, indent_level + 1)}'
            for k, v in value.items()
        ]
        items_str = "\n".join(items)
        return f'{{\n{items_str}\n{indent}}}'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def format_item(key, status, value, depth):
    indent_size = 4
    indent = ' ' * (depth * indent_size)
    if status == 'added':
        return (
            f"{' ' * (depth * indent_size - 2)}+ {key}: "
            f"{format_value(value, depth)}"
        )
    elif status == 'removed':
        return (
            f"{' ' * (depth * indent_size - 2)}- {key}: "
            f"{format_value(value, depth)}"
        )
    elif status == 'updated':
        old_value, new_value = value
        return (
            f"{' ' * (depth * indent_size - 2)}- {key}: "
            f"{format_value(old_value, depth)}\n"
            f"{' ' * (depth * indent_size - 2)}+ {key}: "
            f"{format_value(new_value, depth)}"
        )
    elif status == 'unchanged':
        return f"{indent}{key}: {format_value(value, depth)}"
    return ''


def change_item(item, depth):
    key = item['key']
    status = item['status']
    if status == 'nested':
        nested = convert_to_stylish(item['nested'], depth + 1)
        return f"{' ' * (depth * 4)}{key}: {nested}"
    elif status == 'added':
        return format_item(key, status, item['new_value'], depth)
    elif status == 'removed':
        return format_item(key, status, item['old_value'], depth)
    elif status == 'updated':
        return format_item(
            key, status, (item['old_value'], item['new_value']), depth
        )
    elif status == 'unchanged':
        return format_item(key, status, item['old_value'], depth)
    return ''


def convert_to_stylish(diff, depth=1):
    result = [change_item(item, depth) for item in diff]
    result_str = '\n'.join(result)
    indent = ' ' * ((depth - 1) * 4)

    if depth > 1:
        return f'{{\n{result_str}\n{indent}}}'
    else:
        return f'{{\n{result_str}\n}}'
