import unittest
from order import Order, OrderLine, Product

class OrderTest(unittest.TestCase):

    def test_delegation_fixture(self):
        # Setup
        order = self.create_order()
        # Exercise
        # Verify
        self.assertEqual(7, order.oid)

        self.assertEqual(3, order.lines[0].quantity)
        self.assertEqual('dvd', order.lines[0].product.description)
        self.assertEqual(1799, order.lines[0].product.price)

        self.assertEqual(2, order.lines[1].quantity)
        self.assertEqual('cd', order.lines[1].product.description)
        self.assertEqual(1299, order.lines[1].product.price)

    # Custom creation methods

    def create_order(self):
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))
        return order

if __name__ == '__main__':
    unittest.main()
