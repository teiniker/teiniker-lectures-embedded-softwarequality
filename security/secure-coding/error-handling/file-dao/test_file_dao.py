import logging
import logging.config
import pytest
from file_dao import DataAccessObject, DataAccessError


@pytest.fixture(autouse=True, scope="session")
def configure_logging():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)


def test_read_data():
    dao = DataAccessObject('data.csv')
    value_list = dao.read_data()
    assert value_list == [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]


def test_read_data_file_not_found():
    dao = DataAccessObject('datx.csv')
    with pytest.raises(DataAccessError) as exc_info:
        dao.read_data()
    assert 'datx.csv not found' in str(exc_info.value)
