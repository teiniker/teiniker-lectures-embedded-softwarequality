import unittest
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By

class Language(Enum):
    DEUTSCH = 1
    FRANCAIS = 2

class TranslatorPO:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.driver.get('http://localhost:8080/index.html')
        # Here we can configure default values
        self.word = ''
        self.language = Language.DEUTSCH

    def translate(self):
        self.driver.find_element(By.NAME, "word").click()
        self.driver.find_element(By.NAME, "word").send_keys(self.word)
        self.driver.find_element(By.NAME, "language").click()
        # Decide which language should be selected
        if self.language == Language.DEUTSCH:
            self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)").click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3) > input").click()
        # Return an instance of the TranslatorResult PO
        return TranslatorResultPO(self.driver)


class TranslatorResultPO:
    def __init__(self, driver):
        self.driver = driver
        self.message = self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text
        self.driver.find_element(By.LINK_TEXT, "back").click()


class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.translator = TranslatorPO(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_cat_german(self):
        self.translator.word = 'cat'
        self.translator.language = Language.DEUTSCH
        result = self.translator.translate()
        print(result.message)
        self.assertEqual('Translate: cat into Katze', result.message)

    def test_horse_french(self):
        self.translator.word = 'horse'
        self.translator.language = Language.FRANCAIS
        result = self.translator.translate()
        print(result.message)
        self.assertEqual('Translate: horse into Cheval', result.message)

    def test_dog_german(self):
        self.translator.word = 'dog'
        self.translator.language = Language.FRANCAIS
        result = self.translator.translate()
        print(result.message)
        self.assertEqual('Translate: dog into unknown', result.message)

    def test_dog_french(self):
        self.translator.word = 'dog'
        self.translator.language = Language.FRANCAIS
        result = self.translator.translate()
        print(result.message)
        self.assertEqual('Translate: dog into unknown', result.message)

if __name__ == '__main__':
    unittest.main()
