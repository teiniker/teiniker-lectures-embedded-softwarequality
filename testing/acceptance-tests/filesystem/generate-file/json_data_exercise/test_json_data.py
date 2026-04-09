import os
import json
import pytest

FILE_PATH = 'data.json'

# TODO: Implement Setup and Teardown

def test_deserialization_from_file():
    # Exercise
    with open(json_file, "r", encoding="UTF-8") as read_file:
        data = json.load(read_file)
    # Verify
    expected = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
    assert data == expected

def test_modify_json_file():
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
