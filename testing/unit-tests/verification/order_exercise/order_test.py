import unittest

from order import Order, OrderLine, Product

class OrderTest(unittest.TestCase):

    def test_order(self):
        # Setup
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))

        # Verify
        expected = self.create_order()
        self.assert_equals_order(expected, order)

    # TODO: create the custom assert methods


    # Custom creation methods

    def create_order(self):
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))
        return order

if __name__ == '__main__':
    unittest.main()
