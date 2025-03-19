import unittest
from unittest.mock import Mock
from data_service import DataService, DataAccessError, ServiceError

class DataServiceTest(unittest.TestCase):

    def test_csv_data(self):
        # Setup
        dao = Mock()  # Mock() replaces DataAccessObject
        dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        service = DataService(dao)  # Dependency Injection

        # Exercise
        values = service.csv_data()

        # State verification
        expected = "0.8273,0.7822,0.9731,0.1239,0.9898"
        self.assertEqual(expected, values)


    def test_data_access_error(self):
        # Setup
        dao = Mock()  # Mock() replaces DataAccessObject
        dao.read_data.side_effect = DataAccessError('Can not read data!')
        service = DataService(dao)
        # Exercise
        with self.assertRaises(ServiceError):
            service.csv_data()

if __name__ == '__main__':
    unittest.main()
