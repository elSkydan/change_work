from pytest_bdd import scenarios, when, given, parsers, then
from selenium.webdriver.common.by import By

from tests.pages.base_page import BasePage
from tests.pages.login_page import LoginPage
from tests.pages.menu_locators import MenuLocators
from tests.steps.сommon_steps import *

scenarios("../features/test_comments_page.feature")


@when("I go to the comments page")
def step_go_to_comments_page(driver):
    comments_menu_item = driver.find_element(*MenuLocators.MENU_LOCATORS["Comments"])
    comments_menu_item.click()


@when("I add a new comment to the comments page")
def add_new_comment(driver, context):
    comment = BasePage.generate_random_text()
    comment_section = driver.find_element(By.ID, "commentText")
    comment_section.send_keys(comment)

    submit_button = driver.find_element(By.XPATH, "//*[@id='commentForm']/div/div/button[1]")
    submit_button.click()

    context.comment_text = comment


@then("I verify that comment is saved")
def verify_new_comment(driver, context):
    expected_text = context.comment_text  # текст, который добавили ранее

    try:
        assert expected_text in driver.page_source
        print(f"✅ Комментарий найден: {expected_text}")
    except AssertionError:
        raise AssertionError(f"❌ Комментарий не найден на странице: {expected_text}")

