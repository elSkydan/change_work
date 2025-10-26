import os

from pytest_bdd import parsers
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By


from tests.steps.сommon_steps import *


feature_path = os.path.join(os.path.dirname(__file__), "..", "features", "login_local_web.feature")
scenarios(feature_path)


@then("I should see the dashboard")
def check_dashboard(driver):
    assert "Dashboard" in driver.title
    dashboard_element = driver.find_element(By.XPATH, "/html/body/main/img")
    assert dashboard_element.is_displayed(), "Dashboard header is not visible"
