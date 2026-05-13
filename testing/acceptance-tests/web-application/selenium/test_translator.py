from selenium import webdriver

class TestTranslator:

    def setup_method(self):
        self.driver = webdriver.Firefox()

    def teardown_method(self):
        self.driver.quit()

    def test_open_homepage(self):
        self.driver.get("http://localhost:8080")
        assert "Translator" in self.driver.title
