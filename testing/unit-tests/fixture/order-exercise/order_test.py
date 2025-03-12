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


if __name__ == '__main__':
    unittest.main()
