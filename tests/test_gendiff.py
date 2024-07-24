import pytest
import os
from pathlib import Path
from gendiff import generate_diff

BASE_DIR = Path(__file__).parent


@pytest.mark.parametrize('file_1, file_2, expected, format', [
    (
        'nested_1.json',
        'nested_2.json',
        'stylish.txt',
        'stylish'
    ),
    (
        'nested_1.yml',
        'nested_2.yml',
        'stylish.txt',
        'stylish'
    ),
    (
        'nested_1.json',
        'nested_2.json',
        'plain.txt',
        'plain'
    ),
    (
        'nested_1.yml',
        'nested_2.yml',
        'plain.txt',
        'plain'
    ),
    (
        'nested_1.json',
        'nested_2.json',
        'json.txt',
        'json'
    ),
    (
        'nested_1.yml',
        'nested_2.yml',
        'json.txt',
        'json'
    )
])
def test_gendiff(file_1, file_2, expected, format):
    file_1_path = os.path.join(BASE_DIR, 'fixtures', file_1)
    file_2_path = os.path.join(BASE_DIR, 'fixtures', file_2)
    expected_path = os.path.join(BASE_DIR, 'fixtures', expected)

    result = generate_diff(file_1_path, file_2_path, format)
    with open(expected_path, 'r') as expected_file:
        assert result == expected_file.read()
