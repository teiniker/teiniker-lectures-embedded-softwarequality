import os
import shutil
import pytest

from csv_reader import CsvDataReader, Order

# TODO: Implement Setup and Teardown

def test_read_csv():
    # Exercise
    orders = reader.read_csv(data_file)
    # Verify
    assert len(orders) == 6

def test_save_csv():
    # Exercise
    orders = [
        Order(1, 'resistor 10K', 1),
        Order(3, 'resistor 100', 1),
        Order(3, 'resistor 100', 1)]
    reader.save_csv(data_file, orders)
    # Verify
    assert os.path.exists(data_file)
    assert os.path.getsize(data_file) > 0
