import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_cat_german(self):
        pass

    def test_cat_french(self):
        pass

if __name__ == '__main__':
    unittest.main()
