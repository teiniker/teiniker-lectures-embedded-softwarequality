class ServiceError(Exception):
    pass


class DataAccessError(Exception):
    pass


class DataService:
    def __init__(self, dao):
        self.dao = dao

    def csv_data(self):
        try:
            values = self.dao.read_data()
            csv = ','.join(str(value) for value in values)
            return csv
        except DataAccessError as ex:
            raise ServiceError('Can not read data!') from ex
