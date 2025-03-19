class ServiceError(Exception):
    pass


class DataAccessError(Exception):
    pass


class DataAccessObject:
    def __init__(self) -> None:
        self._data:list[float] = []

    def read_data(self) -> list[float]:
        return self._data

    def save_data(self, data:list[float]) -> None:
        self._data = data


class DataService:
    def __init__(self, dao:DataAccessObject) -> None:
        self.dao = dao

    def csv_data(self) -> str:
        try:
            values = self.dao.read_data()
            csv = ','.join(str(value) for value in values)
            return csv
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
