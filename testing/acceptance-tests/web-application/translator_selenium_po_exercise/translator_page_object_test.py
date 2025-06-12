import unittest
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By

class Language(Enum):
    DEUTSCH = 1
    FRANCAIS = 2

class Translator:
    pass

class TranslatorResult:
    pass


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
