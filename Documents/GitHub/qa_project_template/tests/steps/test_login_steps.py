from pytest_bdd import scenarios, given, when, then, parsers

from tests.pages.login_page import LoginPage

scenarios("../features/test_comments_page.feature")


@given("I am on the login page")
def open_login_page(driver):
    page = LoginPage(driver)
    page.open("https://example.com/login")
    return page


@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login(open_login_page, username, password):
    open_login_page.login(username, password)


@then("I should see the dashboard page")
def verify_dashboard(driver):
    assert "Dashboard" in driver.title
