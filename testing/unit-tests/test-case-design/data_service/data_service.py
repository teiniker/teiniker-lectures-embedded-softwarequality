class ServiceError(Exception):
    pass


class DataAccessError(Exception):
    pass


class DataAccessObject:
    data :list[float]

    def __init__(self) -> None:
        self.data = []

    def read_data(self) -> list[float]:
        return self.data

    def save_data(self, data:list[float]) -> None:
        self.data = data


class DataService:
    dao: DataAccessObject # ---[1]-> DataAccessObject

    def __init__(self, dao:DataAccessObject) -> None:
        self.dao = dao

    def csv_data(self) -> str:
        try:
            values = self.dao.read_data()
            csv = ','.join(str(value) for value in values)
            return csv
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
