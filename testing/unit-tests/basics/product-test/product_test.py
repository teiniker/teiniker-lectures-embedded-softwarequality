import unittest

from product import Product

class ProductTest(unittest.TestCase):

    def test_product(self):
        # Setup
        product = Product('dvd', 1799)
        # Exercise + Verification
        self.assertEqual('dvd', product.description)
        self.assertEqual(1799, product.price)
        # Terdown

    def test_product_invalid_price(self):
        with self.assertRaises(ValueError): # context manager
            Product('dvd', -1790)

    # The block following with defines a context in which
    # the test checks whether the specified exception
    # (ValueError) is raised.

    def test_product_invalid_description(self):
        with self.assertRaises(ValueError):
            Product('', 1799)

if __name__ == '__main__':
    unittest.main()
