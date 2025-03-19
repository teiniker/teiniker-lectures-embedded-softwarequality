import unittest
from data_service import DataAccessObject, DataService

class DataServiceTest(unittest.TestCase):

    def test_csv_data(self):
        # Setup
        dao = DataAccessObject()
        dao.save_data([0.8273, 0.7822, 0.9731, 0.1239, 0.9898])
        service = DataService(dao)  # Dependency Injection

        # Exercise
        values = service.csv_data()

        # State verification
        expected = "0.8273,0.7822,0.9731,0.1239,0.9898"
        self.assertEqual(expected, values)

if __name__ == '__main__':
    unittest.main()
