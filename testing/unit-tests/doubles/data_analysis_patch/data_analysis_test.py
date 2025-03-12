import unittest
from unittest.mock import patch

from data_analysis import DataAccessObject, DataAnalysisService, DataAccessError, ServiceError


class AnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.dao = DataAccessObject('data.csv')
        self.service = DataAnalysisService(self.dao)

    # The following tests use the real DataAccessObject class, reading data
    # froma file.

    def test_mean_value(self):
        # Exercise
        mean = self.service.mean_value()
        # Verify
        expected = (0.8273 + 0.7822 + 0.9731 + 0.1239 + 0.9898) / 5.0
        self.assertEqual(expected, mean, 1E-3)

    def test_max_value(self):
        # Exercise
        max_value = self.service.max_value()
        # Verify
        self.assertEqual(0.9898, max_value, 1E-3)


    # The following tests replace the invocation of DataAccessObject.readData()
    # with a mocked version returning pre-configured data and exceptions.

    def test_mean_value_mocked(self):
        # Setup
        # patch('module.class.method')
        with patch('data_analysis.DataAccessObject.read_data') as mock_read_data:
            mock_read_data.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
            # Exercise
            mean = self.service.mean_value()
            # Verify
            self.assertEqual((1.0 + 2.0 + 3.0 + 4.0 + 5.0)/5.0, mean, 1E-3)

    def test_max_value_mocked(self):
        # Setup
        with patch('data_analysis.DataAccessObject.read_data') as mock_read_data:
            mock_read_data.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
            # Exercise
            min_value = self.service.max_value()
            # Verify
            self.assertEqual(5.0, min_value, 1E-3)

    def test_mean_value_exception(self):
        # Setup
        with patch('data_analysis.DataAccessObject.read_data') as mock_read_data:
            mock_read_data.side_effect = DataAccessError()
            # Exercise
            with self.assertRaises(ServiceError):
                self.service.mean_value()

    def test_max_value_exception(self):
        # Setup
        with patch('data_analysis.DataAccessObject.read_data') as mock_read_data:
            mock_read_data.side_effect = DataAccessError()
            # Exercise
            with self.assertRaises(ServiceError):
                self.service.max_value()


if __name__ == '__main__':
    unittest.main()
