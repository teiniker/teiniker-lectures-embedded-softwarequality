import csv
import statistics


class DataAccessError(Exception):
    pass


class ServiceError(Exception):
    pass


class DataAccessObject:
    filename: str
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read_data(self) -> list[float]:
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=',')
                data = list(reader)
            values = []
            for value in data:
                values.append(float(value[1]))
            return values
        except FileNotFoundError as ex:
            raise DataAccessError('File not found: ' + self.filename) from ex


class DataAnalysisService:
    dao: DataAccessObject # ---[1]--> DataAccessObject

    def __init__(self, dao: DataAccessObject) -> None:
        self.dao = dao

    def mean_value(self) -> float:
        try:
            values = self.dao.read_data()
            print(values)
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
