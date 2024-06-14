import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file_1, file_2, expected, format',
    [
    (
        'tests/fixtures/nested_1.json',
        'tests/fixtures/nested_2.json',
        'tests/fixtures/stylish.txt',
        'stylish'
    ),
    (
        'tests/fixtures/nested_1.yml',
        'tests/fixtures/nested_2.yml',
        'tests/fixtures/stylish.txt',
        'stylish'
    ),
    (
        'tests/fixtures/nested_1.json',
        'tests/fixtures/nested_2.json',
        'tests/fixtures/plain.txt',
        'plain'
    ),
    (
        'tests/fixtures/nested_1.yml',
        'tests/fixtures/nested_2.yml',
        'tests/fixtures/plain.txt',
        'plain'
    ),
    (
        'tests/fixtures/nested_1.json',
        'tests/fixtures/nested_2.json',
        'tests/fixtures/json.txt',
        'json'
    ),
    (
        'tests/fixtures/nested_1.yml',
        'tests/fixtures/nested_2.yml',
        'tests/fixtures/json.txt',
        'json'
    )
])
def test_gendiff(file_1, file_2, expected, format):
    result = generate_diff(file_1, file_2, format)
    with open(expected, 'r') as expected:
        assert result == expected.read()
