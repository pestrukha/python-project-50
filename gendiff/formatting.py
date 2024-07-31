from gendiff.formatters.stylish import convert_to_stylish
from gendiff.formatters.plain import convert_to_plain
from gendiff.formatters.json import convert_to_json


class FormatError(Exception):
    pass


def format_diff(diff, format):
    if format == 'stylish':
        return convert_to_stylish(diff)
    elif format == 'plain':
        return convert_to_plain(diff)
    elif format == 'json':
        return convert_to_json(diff)
    else:
        raise FormatError(f'Unknown format: {format}')
