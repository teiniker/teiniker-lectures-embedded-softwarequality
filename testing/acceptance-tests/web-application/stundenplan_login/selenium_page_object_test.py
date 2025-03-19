import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://stundenplan.fh-joanneum.at/')
        self.username = ""
        self.password = ""

    def login(self):
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(self.username)
        self.driver.find_element(By.NAME, "pass").send_keys(self.password)
        self.driver.find_element(By.NAME, "login").click()
        return LogoutPage(self.driver)


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_login_logout(self):
        login_page = LoginPage(self.driver)
        login_page.username = 'stm'
        login_page.password = 'stm'
        logout_page = login_page.login()
        # ...
        time.sleep(3)

        logout_page.logout()


if __name__ == '__main__':
    unittest.main()
