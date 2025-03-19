import unittest
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By

class Waveform(Enum):
    DC = 1
    AC_SINUSOIDAL = 2
    AC_SQUARE = 3
    AC_TRIANGULAR = 4

class SignalGeneratorPO:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://localhost:8080/')
        # Here we can configure default values
        self.amplitude = 0.0
        self.offset = 0.0
        self.waveform = Waveform.DC

    def set(self):
        self.driver.find_element(By.NAME, "amplitude").send_keys(str(self.amplitude))
        self.driver.find_element(By.NAME, "offset").send_keys(str(self.offset))
        self.driver.find_element(By.NAME, "waveform").click()
        if self.waveform == Waveform.DC:
            self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)").click()
        elif self.waveform == Waveform.AC_SINUSOIDAL:
            self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        elif self.waveform == Waveform.AC_SQUARE:
            self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(4)").click()
        self.driver.find_element(By.NAME, "action").click()
        return SettingsPO(self.driver)

class SettingsPO:
    def __init__(self, driver):
        self.driver = driver
        self.message = self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text

    def back(self):
        self.driver.find_element(By.LINK_TEXT, "back").click()
        return SignalGeneratorPO(self.driver)


class SeleniumTestSignalGeneratorPOTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.generator = SignalGeneratorPO(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_happy_path(self):
        self.generator.amplitude = 5.0
        self.generator.offset = -2.5
        self.generator.waveform = Waveform.AC_SQUARE
        result = self.generator.set()
        print(result.message)
        self.assertEqual('Signal: AC (triangular) : 5.0 [V], -2.5 [V] offset.', result.message)

    def test_invalid_amplitude(self):
        self.generator.amplitude = 11.0
        self.generator.offset = 2.5
        self.generator.waveform = Waveform.AC_TRIANGULAR
        result = self.generator.set()
        print(result.message)
        self.assertEqual('Invalid signal configuration:', result.message)

    def test_invalid_offset(self):
        self.generator.amplitude = 5.0
        self.generator.offset = -11.0
        self.generator.waveform = Waveform.DC
        result = self.generator.set()
        print(result.message)
        self.assertEqual('Invalid signal configuration:', result.message)

if __name__ == '__main__':
    unittest.main()
