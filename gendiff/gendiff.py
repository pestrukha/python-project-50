from gendiff.parser import parse_data
from gendiff.build_diff import build_diff
from gendiff.formatters.stylish import convert_to_stylish
from gendiff.formatters.plain import convert_to_plain


def generate_diff(file_1, file_2, format_name='stylish'):
    dict_1 = parse_data(file_1)
    dict_2 = parse_data(file_2)
    diff = build_diff(dict_1, dict_2)

    if format_name == 'stylish':
        return convert_to_stylish(diff)
    if format_name == 'plain':
        return convert_to_plain(diff)
    else:
        return None
