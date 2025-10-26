import os

from pytest_bdd import given, when, parsers

from tests.pages.login_page import LoginPage


@given("I am on the home page")
def open_home(driver, base_url):
    driver.get(base_url)


@when(parsers.parse('I login with firstname "{firstname}" and secondname "{secondname}"'))
def login(driver, firstname, secondname, user_info):
    page = LoginPage(driver)
    page.login(firstname, secondname)
    user_info["firstname"] = firstname
    user_info["secondname"] = secondname