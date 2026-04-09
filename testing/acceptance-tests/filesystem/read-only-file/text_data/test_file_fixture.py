import pytest

@pytest.fixture
def file():
    # Setup
    f = open('Sympathy.txt', 'rt', encoding="utf-8")
    # Exercise
    yield f
    # Teardown
    f.close()

def test_read_file(file):
    text = file.read()
    print(text)
    assert len(text) == 389

def test_read_lines(file):
    lines = file.readlines()
    print(lines)
    assert len(lines) == 16

def test_read_file_autoclose():
    with open('Sympathy.txt', 'rt', encoding="utf-8") as file:
        lines = file.readlines()
        print(lines)
        assert len(lines) == 16
