

from pytest_bdd import given


@given("I am on the home page")
def open_home(driver, base_url):
    driver.get(base_url)
