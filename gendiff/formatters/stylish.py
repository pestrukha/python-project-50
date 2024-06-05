def format_value(value, indent_level):
    indent = ' ' * (indent_level * 4)
    if isinstance(value, dict):
        items = [f'{indent}    {k}: {format_value(v, indent_level + 1)}' for k, v in value.items()]
        items_str = "\n".join(items)
        return f'{{\n{items_str}\n{indent}}}'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def convert_to_stylish(data, depth=1):
    indent_size = 4
    result = []

    for item in data:
        key = item['key']
        status = item['status']
        if status == 'nested':
            nested = convert_to_stylish(item['nested'], depth + 1)
            result.append(f"{' ' * (depth * indent_size)}{key}: {nested}")
        elif status == 'added':
            result.append(f"{' ' * (depth * indent_size - 2)}+ {key}: {format_value(item['new_value'], depth)}")
        elif status == 'removed':
            result.append(f"{' ' * (depth * indent_size - 2)}- {key}: {format_value(item['old_value'], depth)}")
        elif status == 'updated':
            result.append(f"{' ' * (depth * indent_size - 2)}- {key}: {format_value(item['old_value'], depth)}")
            result.append(f"{' ' * (depth * indent_size - 2)}+ {key}: {format_value(item['new_value'], depth)}")
        elif status == 'unchanged':
            result.append(f"{' ' * (depth * indent_size)}{key}: {format_value(item['old_value'], depth)}")

    result_str = "\n".join(result)
    indent = " " * ((depth - 1) * indent_size)

    if depth > 1:
        return f'{{\n{result_str}\n{indent}}}'
    else:
        return f'{{\n{result_str}\n}}'