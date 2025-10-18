from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "firstname")
    PASSWORD = (By.ID, "secondname")
    LOGIN_BTN = (By.XPATH, "//button[text()='Enter']")
    DASHBOARD_TITLE = (By.TAG_NAME, "title")
    BASE_URL = "http://localhost:8000/"

    def login(self, firstname, secondname):
        self.type(self.USERNAME, firstname)
        self.type(self.PASSWORD, secondname)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        return self.wait.until(lambda d: "Dashboard" in d.title)

    def main_url(self):
        self.open(self.BASE_URL)



