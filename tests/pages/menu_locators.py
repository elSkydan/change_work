from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage


class MenuLocators(BasePage):
    MENU_LOCATORS = {
        "Home": (By.ID, "Home"),
        "Profile": (By.ID, "Profile"),
        "Visit log": (By.ID, "VisitLog"),
        "Comments": (By.ID, "Comments"),
        "Exit": (By.ID, "Exit"),
    }
