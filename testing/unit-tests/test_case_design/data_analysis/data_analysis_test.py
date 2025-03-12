import unittest
from data_analysis import DataAccessObject, DataAnalysisService, DataAccessError, ServiceError


class AnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.dao = DataAccessObject('data.csv')
        self.service = DataAnalysisService(self.dao)

    def test_read_data(self):
        # Exercise
        values = self.dao.read_data()
        # Verify
        expected = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.assertEqual(expected, values)

    def test_mean_value(self):
        # Exercise
        mean_val = self.service.mean_value()
        # Verify
        expected = (0.8273 + 0.7822 + 0.9731 + 0.1239 + 0.9898) / 5.0
        self.assertEqual(expected, mean_val, 1E-3)

    def test_max_value(self):
        # Exercise
        min_val = self.service.max_value()
        # Verify
        self.assertEqual(0.9898, min_val, 1E-3)

    def test_read_data_file_not_found(self):
        with self.assertRaises(DataAccessError):
            # Setup
            dao = DataAccessObject('values.csv')
            dao.read_data()

    def test_mean_value_file_not_found(self):
        with self.assertRaises(ServiceError):
            # Setup
            dao = DataAccessObject('values.csv')
            service = DataAnalysisService(dao)
            service.mean_value()

    def test_max_value_file_not_found(self):
        with self.assertRaises(ServiceError):
            # Setup
            dao = DataAccessObject('values.csv')
            service = DataAnalysisService(dao)
            service.max_value()

if __name__ == '__main__':
    unittest.main()
