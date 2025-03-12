import csv
import statistics


class DataAccessError(Exception):
    pass


class ServiceError(Exception):
    pass


class DataAccessObject:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r', encoding='UTF-8') as file:
                reader = csv.reader(file, delimiter=',')
                data = list(reader)
            values = []
            for value in data:
                values.append(float(value[1]))
            return values
        except FileNotFoundError as ex:
            raise DataAccessError('File not found: ' + self.filename) from ex


class DataAnalysisService:
    def __init__(self, dao):
        self.dao = dao

    def mean_value(self):
        try:
            values = self.dao.read_data()
            return statistics.mean(values)
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex

    def max_value(self):
        try:
            values = self.dao.read_data()
            values.sort()
            return values[-1]
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
