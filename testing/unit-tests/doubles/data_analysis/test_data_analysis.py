import pytest

from data_analysis import DataAccess, DataAccessError, DataAnalysisService, ServiceError


def test_mean_value(mocker):
    # Setup
    dao = mocker.Mock(spec=DataAccess)
    service = DataAnalysisService(dao)
    dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
    # Exercise
    mean = service.mean_value()
    # Verify
    expected = (0.8273 + 0.7822 + 0.9731 + 0.1239 + 0.9898) / 5.0
    assert mean == pytest.approx(expected, abs=1e-3)


def test_max_value(mocker):
    # Setup
    dao = mocker.Mock(spec=DataAccess)
    service = DataAnalysisService(dao)
    dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
    # Exercise
    maximum = service.max_value()
    # Verify
    assert maximum == pytest.approx(0.9898, abs=1e-3)


def test_mean_value_exception(mocker):
    # Setup
    dao = mocker.Mock(spec=DataAccess)
    service = DataAnalysisService(dao)
    dao.read_data.side_effect = DataAccessError()
    # Exercise / Verify
    with pytest.raises(ServiceError):
        service.mean_value()


def test_max_value_exception(mocker):
    # Setup
    dao = mocker.Mock(spec=DataAccess)
    service = DataAnalysisService(dao)
    dao.read_data.side_effect = DataAccessError()
    # Exercise / Verify
    with pytest.raises(ServiceError):
        service.max_value()
