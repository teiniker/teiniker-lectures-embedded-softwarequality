import statistics
from typing import Protocol


class DataAccessError(Exception):
    pass

class ServiceError(Exception):
    pass


class DataAccess(Protocol):
    def read_data(self) -> list[float]:
        ...


class DataAnalysisService:
    dao: DataAccess  # ---[1]-> DataAccess

    def __init__(self, dao: DataAccess) -> None:
        self.dao = dao

    def mean_value(self) -> float:
        try:
            values = self.dao.read_data()
            return statistics.mean(values)
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex

    def max_value(self) -> float:
        try:
            values = self.dao.read_data()
            values.sort()
            return values[-1]
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
