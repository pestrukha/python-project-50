import pytest
from pathlib import Path
from gendiff import generate_diff

BASE_DIR = Path(__file__).parent

@pytest.mark.parametrize('file_1, file_2, expected, format', [
    (
        BASE_DIR / 'fixtures/nested_1.json',
        BASE_DIR / 'fixtures/nested_2.json',
        BASE_DIR / 'fixtures/stylish.txt',
        'stylish'
    ),
    (
        BASE_DIR / 'fixtures/nested_1.yml',
        BASE_DIR / 'fixtures/nested_2.yml',
        BASE_DIR / 'fixtures/stylish.txt',
        'stylish'
    ),
    (
        BASE_DIR / 'fixtures/nested_1.json',
        BASE_DIR / 'fixtures/nested_2.json',
        BASE_DIR / 'fixtures/plain.txt',
        'plain'
    ),
    (
        BASE_DIR / 'fixtures/nested_1.yml',
        BASE_DIR / 'fixtures/nested_2.yml',
        BASE_DIR / 'fixtures/plain.txt',
        'plain'
    ),
    (
        BASE_DIR / 'fixtures/nested_1.json',
        BASE_DIR / 'fixtures/nested_2.json',
        BASE_DIR / 'fixtures/json.txt',
        'json'
    ),
    (
        BASE_DIR / 'fixtures/nested_1.yml',
        BASE_DIR / 'fixtures/nested_2.yml',
        BASE_DIR / 'fixtures/json.txt',
        'json'
    )
])
def test_gendiff(file_1, file_2, expected, format):
    result = generate_diff(file_1, file_2, format)
    with open(expected, 'r') as expected:
        assert result == expected.read()
