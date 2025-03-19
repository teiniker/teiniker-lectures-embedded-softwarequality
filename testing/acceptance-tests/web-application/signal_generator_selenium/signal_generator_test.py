import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_happy_path(self):
        self.driver.get("http://localhost:8080/")
        self.driver.find_element(By.NAME, "amplitude").send_keys("5")
        self.driver.find_element(By.NAME, "offset").send_keys("-2.5")
        self.driver.find_element(By.NAME, "waveform").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(4)").click()
        self.driver.find_element(By.NAME, "action").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Signal: AC (square) : 5 [V], -2.5 [V] offset."
        self.driver.find_element(By.LINK_TEXT, "back").click()

    def test_invalid_amplitude(self):
        self.driver.get("http://localhost:8080/")
        self.driver.find_element(By.NAME, "amplitude").send_keys("11")
        self.driver.find_element(By.NAME, "offset").send_keys("2.5")
        self.driver.find_element(By.NAME, "waveform").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
        self.driver.find_element(By.NAME, "action").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Invalid signal configuration:"
        self.driver.find_element(By.LINK_TEXT, "back").click()

    def test_invalid_offset(self):
        self.driver.get("http://localhost:8080/")
        self.driver.find_element(By.NAME, "amplitude").send_keys("5")
        self.driver.find_element(By.NAME, "offset").send_keys("-11")
        self.driver.find_element(By.NAME, "waveform").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)").click()
        self.driver.find_element(By.NAME, "action").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Invalid signal configuration:"
        self.driver.find_element(By.LINK_TEXT, "back").click()

if __name__ == '__main__':
    unittest.main()
