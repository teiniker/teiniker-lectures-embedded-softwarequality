import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_cat_german(self):
        self.driver.get("http://localhost:8080")
        self.driver.find_element(By.NAME, "word").click()
        self.driver.find_element(By.NAME, "word").send_keys("cat")
        self.driver.find_element(By.NAME, "language").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3) > input").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Translate: cat into Katze"
        self.driver.find_element(By.LINK_TEXT, "back").click()

    def test_cat_french(self):
        self.driver.get("http://localhost:8080")
        self.driver.find_element(By.NAME, "word").click()
        self.driver.find_element(By.NAME, "word").send_keys("cat")
        self.driver.find_element(By.NAME, "language").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3) > input").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Translate: cat into Chatte"
        self.driver.find_element(By.LINK_TEXT, "back").click()

if __name__ == '__main__':
    unittest.main()
