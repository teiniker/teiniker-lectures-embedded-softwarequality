import unittest
import os
import shutil

from csv_reader import CsvDataReader, Order

class CsvDataReaderTest(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_data')
        self.data_file = 'test_data/order.csv'
        shutil.copyfile('data/data.csv', self.data_file)
        self.reader = CsvDataReader()

    def tearDown(self):
        shutil.rmtree('test_data')


    def test_read_csv(self):
        # Exercise
        orders = self.reader.read_csv(self.data_file)
        # Verify
        self.assertEqual(6, len(orders))

    def test_save_csv(self):
        orders = [
            Order(1, 'resistor 10K', 1),
            Order(3, 'resistor 100', 1),
            Order(3, 'resistor 100', 1)]
        self.reader.save_csv(self.data_file, orders) 
        self.assertTrue(os.path.exists(self.data_file))
        self.assertTrue(os.path.getsize(self.data_file) > 0)


if __name__ == '__main__':
    unittest.main()
