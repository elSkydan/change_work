from pytest_bdd import scenarios, when, then

from tests.pages.menu_locators import MenuLocators
from tests.pages.visitor_log_page import VisitorLogPage

scenarios("../features/test_comments_page.feature")


@when("I go to the visitor log page")
def step_go_to_comments_page(driver):
    comments_menu_item = driver.find_element(*MenuLocators.MENU_LOCATORS["Visitlog"])
    comments_menu_item.click()


@then("I verify that log is saved")
def verify_log_saved(driver, user_info):
    page = VisitorLogPage(driver)
    firstname = user_info["firstname"]
    secondname = user_info["secondname"]
    assert page.is_log_saved(firstname, secondname), \
        f"Log for {firstname} {secondname} not found"
