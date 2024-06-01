import pytest
from gendiff import generate_diff


def test_gendiff():
    file_1 = 'tests/fixtures/1.json'
    file_2 = 'tests/fixtures/2.json'
    result = 'tests/fixtures/result.txt'
    diff = print(generate_diff(file_1, file_2))
    assert diff == print(result)