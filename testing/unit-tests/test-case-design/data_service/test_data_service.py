from data_service import DataAccessObject, DataService


def test_csv_data():
    # Setup
    dao = DataAccessObject()
    dao.save_data([0.8273, 0.7822, 0.9731, 0.1239, 0.9898])
    service = DataService(dao)
    # Exercise
    values = service.csv_data()
    # Verify
    assert values == "0.8273,0.7822,0.9731,0.1239,0.9898"
