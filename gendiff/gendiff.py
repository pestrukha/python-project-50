from gendiff.parser import parse_data
from gendiff.build_diff import build_diff
from gendiff.formatting import format_diff


def generate_diff(file_1, file_2, format='stylish'):
    dict_1 = parse_data(file_1)
    dict_2 = parse_data(file_2)
    diff = build_diff(dict_1, dict_2)
    return format_diff(diff, format)
