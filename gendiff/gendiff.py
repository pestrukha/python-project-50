from gendiff.parser import parse_json, parse_yaml


def get_diff(data_1, data_2):
    result = {}
    all_keys = sorted(set(data_1.keys()).union(data_2.keys()))
    for key in all_keys:
        if key in data_1 and key in data_2:
            if data_1[key] == data_2[key]:
                result[f"  {key}"] = data_1[key]
            else:
                result[f"- {key}"] = data_1[key]
                result[f"+ {key}"] = data_2[key]
        elif key in data_1:
            result[f"- {key}"] = data_1[key]
        elif key in data_2:
            result[f"+ {key}"] = data_2[key]
    return result


def stringify(value, replacer=' ', space_count=2):
    def inner(current_value, depth=0):
        if not isinstance(current_value, dict):
            return str(current_value).lower()
        deep_indent = replacer * (depth + space_count)
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            line = f"{deep_indent}{key}: {inner(val, depth + space_count)}"
            lines.append(line)
        lines_joined = '\n'.join(lines)
        return f"{{\n{lines_joined}\n{current_indent}}}"
    return inner(value)


def generate_diff(file1, file2):
    if not parse_yaml(file1, file2):
        f1, f2 = parse_json(file1, file2)
    else:
        f1, f2 = parse_yaml(file1, file2)
    result = get_diff(f1, f2)
    string = stringify(result)
    return string
