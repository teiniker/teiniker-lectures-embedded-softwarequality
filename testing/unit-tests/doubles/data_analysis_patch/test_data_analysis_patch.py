import pytest
from data_analysis import DataAccessError, DataAccessObject, DataAnalysisService, ServiceError


def test_mean_value_mocked(mocker):
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    mocker.patch("data_analysis.DataAccessObject.read_data", return_value=[1.0, 2.0, 3.0, 4.0, 5.0])
    # Exercise
    mean = service.mean_value()
    # Verify
    assert mean == pytest.approx((1.0 + 2.0 + 3.0 + 4.0 + 5.0) / 5.0, abs=1e-3)


def test_max_value_mocked(mocker):
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    mocker.patch("data_analysis.DataAccessObject.read_data", return_value=[1.0, 2.0, 3.0, 4.0, 5.0])
    # Exercise
    max_value = service.max_value()
    # Verify
    assert max_value == pytest.approx(5.0, abs=1e-3)


def test_mean_value_exception(mocker):
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    mocker.patch("data_analysis.DataAccessObject.read_data", side_effect=DataAccessError())
    # Exercise / Verify
    with pytest.raises(ServiceError):
        service.mean_value()


def test_max_value_exception(mocker):
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    mocker.patch("data_analysis.DataAccessObject.read_data", side_effect=DataAccessError())
    # Exercise / Verify
    with pytest.raises(ServiceError):
        service.max_value()
