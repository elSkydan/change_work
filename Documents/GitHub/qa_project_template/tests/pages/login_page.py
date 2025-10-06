from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    DASHBOARD_TITLE = (By.CSS_SELECTOR, "h1.dashboard")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        return self.wait.until(lambda d: "Dashboard" in d.title or d.find_elements(*self.DASHBOARD_TITLE))
