from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTranslator:

    def setup_method(self):
        self.driver = webdriver.Firefox()

    def teardown_method(self):
        self.driver.quit()

    def test_cat_german(self):
        self.driver.get("http://localhost:8080")
        # Enter word
        self.driver.find_element(By.NAME, "word").click()
        self.driver.find_element(By.NAME, "word").send_keys("cat")
        # Select language
        self.driver.find_element(By.NAME, "language").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)").click()
        # Click translate
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3) > input").click()
        # Assert text
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Translate: cat into Katze"
        # Click back link
        self.driver.find_element(By.LINK_TEXT, "back").click()

    def test_cat_french(self):
        self.driver.get("http://localhost:8080")
        # Enter word
        self.driver.find_element(By.NAME, "word").click()
        self.driver.find_element(By.NAME, "word").send_keys("cat")
        # Select language
        self.driver.find_element(By.NAME, "language").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        # Click translate
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(3) > input").click()
        # Assert text
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").text == "Translate: cat into Chatte"
        # Click back link
        self.driver.find_element(By.LINK_TEXT, "back").click()
