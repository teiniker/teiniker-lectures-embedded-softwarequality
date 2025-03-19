import csv

class DataAccessError(Exception):
    pass

class Order:
    def __init__(self, oid, part, quantity):
        self.oid = oid
        self.part = part
        self.quantity = quantity

    def __str__(self):
        return f'Order: id={self.oid}, part={self.part}, quantity={self.quantity}'


class CsvDataReader:
    def read_csv(self, filename):
        try:
            with open(filename, 'r', encoding="UTF-8") as file:
                reader = csv.reader(file, delimiter=',')
                orders = []
                for row in reader:
                    print(f"id: {row[0]} part:{row[1]} quantity:{row[2]}")
                    orders.append(Order(int(row[0]), row[1], row[2]))
                return orders
        except FileNotFoundError as ex:
            raise DataAccessError('File not found: ' + filename) from ex

    def save_csv(self, filename, orders):
        with open(filename, 'w', encoding="UTF-8") as file:
            csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            for order in orders:
                csv_writer.writerow([order.oid, order.part, order.quantity])
