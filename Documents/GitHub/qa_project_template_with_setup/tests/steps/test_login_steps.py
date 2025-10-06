from pytest_bdd import scenarios, given, when, then, parsers

from tests.pages.login_page import LoginPage

scenarios("../features/login.feature")


@given("I am on the login page")
def main_url(driver):
    page = LoginPage(driver)
    page.open(page.BASE_URL)


@then("I should see the dashboard page")
def check_dashboard(driver):
    page = LoginPage(driver)
    assert page.is_logged_in()


@when(parsers.parse('I login with firstname "{firstname}" and secondname "{secondname}"'))
def login(driver, firstname, secondname):
    page = LoginPage(driver)
    page.login(firstname, secondname)