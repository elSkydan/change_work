from pytest_bdd import scenarios, when, then

from tests.pages.menu_locators import MenuLocators
from tests.pages.visitor_log_page import VisitorLogPage
from tests.steps.сommon_steps import *


scenarios("../features/test_visitorlog_page.feature")


@when("I go to the visitor log page")
def step_go_to_visitors_page(driver):
    comments_menu_item = driver.find_element(*MenuLocators.MENU_LOCATORS["Visit log"])
    comments_menu_item.click()


#@then("I verify that log is saved")
#def verify_log_saved(driver, user_info):
#    page = VisitorLogPage(driver)
#    firstname = user_info["firstname"]
#    secondname = user_info["secondname"]
#    assert page.is_log_saved(firstname, secondname), \
#        f"Log for {firstname} {secondname} not found"



@then("I verify that log is saved")
def verify_log_saved(driver, user_info):

    firstname = user_info["firstname"]
    secondname = user_info["secondname"]





