import os
import shutil
import pytest

from csv_reader import CsvDataReader, Order

@pytest.fixture
def setup():
    # Setup
    os.mkdir('test_data')
    data_file = 'test_data/order.csv'
    shutil.copyfile('data/data.csv', data_file)
    reader = CsvDataReader()
    # Exercise
    yield data_file, reader
    # Teardown
    shutil.rmtree('test_data')

def test_read_csv(setup):
    data_file, reader = setup
    # Exercise
    orders = reader.read_csv(data_file)
    # Verify
    assert len(orders) == 6

def test_save_csv(setup):
    data_file, reader = setup
    # Exercise
    orders = [
        Order(1, 'resistor 10K', 1),
        Order(3, 'resistor 100', 1),
        Order(3, 'resistor 100', 1)]
    reader.save_csv(data_file, orders)
    # Verify
    assert os.path.exists(data_file)
    assert os.path.getsize(data_file) > 0
