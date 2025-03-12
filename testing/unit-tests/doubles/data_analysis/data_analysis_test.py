import unittest
from unittest.mock import Mock

from data_analysis import DataAnalysisService, DataAccessError, ServiceError


class AnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()                               # DOC
        self.dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.service = DataAnalysisService(self.dao)    # SUT

    def test_read_data_from_dao(self):
        data_list = self.dao.read_data()
        print(data_list)

    def test_mean_value(self):
        # Exercise
        mean = self.service.mean_value()
        # Verify
        expected = (0.8273 + 0.7822 + 0.9731 + 0.1239 + 0.9898) / 5.0
        self.assertEqual(expected, mean, 1E-3)

    def test_max_value(self):
        # Exercise
        maximum = self.service.max_value()
        # Verify
        self.assertEqual(0.9898, maximum, 1E-3)

    def test_mean_value_exception(self):
        # Setup
        self.dao.read_data.side_effect = DataAccessError()
        # Exercise
        with self.assertRaises(ServiceError):
            self.service.mean_value()

    def test_max_value_exception(self):
       # Setup
        self.dao.read_data.side_effect = DataAccessError()
        with self.assertRaises(ServiceError):
            self.service.max_value()

if __name__ == '__main__':
    unittest.main()
