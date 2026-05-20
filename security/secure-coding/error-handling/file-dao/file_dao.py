import csv
import logging

log = logging.getLogger(__name__)

class DataAccessError(Exception):
    pass

class DataAccessObject:
    def __init__(self, filename):
        self.filename = filename
        log.debug("DataAccessObject created for file '%s'", filename)

    def read_data(self):
        log.debug("Reading data from '%s'", self.filename)
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=',')
                data = list(reader)
                values = [float(row[1]) for row in data]
                log.debug("Read %d values from '%s'", len(values), self.filename)
                return values
        except FileNotFoundError as ex:
            log.exception("File '%s' not found", self.filename)
            raise DataAccessError(f"File {self.filename} not found!") from ex

