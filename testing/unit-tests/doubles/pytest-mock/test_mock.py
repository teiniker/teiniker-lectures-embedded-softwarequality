import pytest


def test_return_value(mocker):
    doc = mocker.Mock()

    # setup
    doc.random.return_value = 666

    # exercise
    random_value = doc.random()

    # verify
    assert random_value == 666


def test_exception(mocker):
    doc = mocker.Mock()

    # setup
    doc.load.side_effect = ValueError("Load Error!")

    # exercise / verify
    with pytest.raises(ValueError):
        doc.load()


def test_called(mocker):
    doc = mocker.Mock()

    # exercise
    doc.save('{"key": "value"}')

    # verify
    doc.save.assert_called()
    doc.save.assert_called_once()
    doc.save.assert_called_with('{"key": "value"}')
    doc.save.assert_called_once_with('{"key": "value"}')


def test_called_once(mocker):
    doc = mocker.Mock()

    # exercise
    doc.loads('{"key": "value"}')
    doc.loads('{"key": "value"}')

    # verify
    with pytest.raises(AssertionError):
        doc.loads.assert_called_once()


def test_called_count(mocker):
    doc = mocker.Mock()

    # exercise
    doc.loads('{"key": "value"}')
    doc.loads('{"key": "value"}')

    # verify
    assert doc.loads.call_count == 2
