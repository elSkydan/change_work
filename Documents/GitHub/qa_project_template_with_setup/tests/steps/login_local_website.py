import os

from pytest_bdd import parsers
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By

from tests.pages.login_page import LoginPage

# Подключаем feature-файл
#scenarios("features/login_local_web.feature")
feature_path = os.path.join(os.path.dirname(__file__), "..", "features", "login_local_web.feature")
scenarios(feature_path)


#@given("I am on the home page")
#def open_home(driver, base_url):
#    driver.get(base_url)


@given(parsers.parse('I login with username "{firstname}" and password "{secondname}"'))
def login(driver, firstname, secondname):
    page = LoginPage(driver)
    page.login(firstname, secondname)


#@when(parsers.parse('I login with username "{username}" and password "{password}"'))
#def login(driver, username, password):
#    driver.find_element(By.ID, "username").send_keys(username)
#    driver.find_element(By.ID, "password").send_keys(password)
#    driver.find_element(By.XPATH, "//button[text()='Enter']").click()


@then("I should see the dashboard")
def check_dashboard(driver):
    assert "Dashboard" in driver.title
