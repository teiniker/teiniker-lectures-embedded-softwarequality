import unittest

from resistor import Resistor

class ResistorTest(unittest.TestCase):

    def test_class_variable(self):
        # Setup
        # Exercise
        vendor = Resistor.vendor
        # Verify
        self.assertEqual('Neuhold Electronics', vendor)
        # Teardown

    def test_resistor_init(self):
        # Setup
        res = Resistor(470, 5)
        # Exercise
        value = res.value
        tol = res.tolerance
        # Verify
        self.assertEqual(470, value)
        self.assertEqual(5, tol)
        # Teardown

    def test_default_value(self):
        # Setup
        res = Resistor(1000)
        self.assertEqual(1000, res.value)
        self.assertEqual(2, res.tolerance)


    def test_add_resistors(self):
        # Setup
        res_1 = Resistor(1000)
        res_2 = Resistor(330)
        # Exercise
        res = res_1 + res_2
        # Verify
        self.assertEqual(1000+330, res.value)
        self.assertEqual(2, res.tolerance)
        # Teardown

if __name__ == '__main__':
    unittest.main()
