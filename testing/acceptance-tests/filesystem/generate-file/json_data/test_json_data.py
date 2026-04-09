import os
import json
import pytest

FILE_PATH = 'data.json'

@pytest.fixture
def json_file():
    # Setup
    data = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
    with open(FILE_PATH, "w", encoding="UTF-8") as write_file:
        json.dump(data, write_file, indent=2)
    # Exercise
    yield FILE_PATH
    # Teardown
    os.remove(FILE_PATH)

def test_deserialization_from_file(json_file):
    # Exercise
    with open(json_file, "r", encoding="UTF-8") as read_file:
        data = json.load(read_file)
    # Verify
    expected = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
    assert data == expected

def test_modify_json_file(json_file):
    # Setup
    data = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
    # Exercise
    data['person']['age'] = 50
    with open(json_file, "w", encoding="UTF-8") as write_file:
        json.dump(data, write_file, indent=2)
    # Verify
    with open(json_file, "r", encoding="UTF-8") as read_file:
        data = json.load(read_file)
    expected = {'person': {'name': 'John', 'age': 50, 'city': 'Graz'}}
    assert data == expected
