from gendiff.parser import parse_data


def generate_diff(file_1, file_2, format_name='stylish'):
    dict_1 = parse_data(file_1)
    dict_2 = parse_data(file_2)
    diff = build_diff(dict_1, dict_2)
    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        return None
