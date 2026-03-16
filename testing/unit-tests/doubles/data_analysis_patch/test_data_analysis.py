import pytest
from data_analysis import DataAccessObject, DataAnalysisService


def test_mean_value():
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    # Exercise
    mean = service.mean_value()
    # Verify
    expected = (0.8273 + 0.7822 + 0.9731 + 0.1239 + 0.9898) / 5.0
    assert mean == pytest.approx(expected, abs=1e-3)


def test_max_value():
    # Setup
    dao = DataAccessObject("data.csv")
    service = DataAnalysisService(dao)
    # Exercise
    max_value = service.max_value()
    # Verify
    assert max_value == pytest.approx(0.9898, abs=1e-3)
