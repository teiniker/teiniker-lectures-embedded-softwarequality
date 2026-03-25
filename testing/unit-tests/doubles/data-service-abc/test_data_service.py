import pytest

from data_service import DataAccess, DataAccessError, DataService, ServiceError


def test_csv_data(mocker):
    # Setup
    dao = mocker.Mock(spec=DataAccess)
    dao.load_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
    service = DataService(dao)

    # Exercise
    values = service.csv_data()

    # State verification
    expected = "0.8273,0.7822,0.9731,0.1239,0.9898"
    assert values == expected


def test_data_access_error(mocker):
    # Setup
    dao = mocker.Mock(spec=DataAccess)
    dao.load_data.side_effect = DataAccessError("Can not read data!")
    service = DataService(dao)

    # Exercise / Verify
    with pytest.raises(ServiceError):
        service.csv_data()
