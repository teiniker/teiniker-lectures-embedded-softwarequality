import csv
import statistics


class DataAccessError(Exception):
    pass

class ServiceError(Exception):
    pass


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
