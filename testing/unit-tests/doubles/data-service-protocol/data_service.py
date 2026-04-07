from typing import Protocol


class ServiceError(Exception):
    pass


class DataAccessError(Exception):
    pass

# DOC - Dependendent on Component
class DataAccess(Protocol):
    def load_data(self) -> list[float]:
        ...

    def save_data(self, data: list[float]) -> None:
        ...

# SUT - System Under Test
class DataService:
    dao: DataAccess # ---[1]-> DataAccess

    def __init__(self, dao: DataAccess) -> None:
        self.dao = dao

    def csv_data(self) -> str:
        try:
            values = self.dao.load_data()
            csv = ','.join(str(value) for value in values)
            return csv
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
