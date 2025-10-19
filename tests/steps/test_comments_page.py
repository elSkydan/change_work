from pytest_bdd import scenarios, when, given, parsers, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v138 import page

from tests.pages.base_page import BasePage
from tests.pages.login_page import LoginPage
from tests.pages.menu_locators import MenuLocators

scenarios("../features/test_comments_page.feature")


@given("I am on the home page")
def open_home(driver, base_url):
    driver.get(base_url)


@when(parsers.parse('I login with firstname "{firstname}" and secondname "{secondname}"'))
def login(driver, firstname, secondname):
    page = LoginPage(driver)
    page.login(firstname, secondname)


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
    page = BasePage(driver)

    try:
        # простой способ — проверить, что текст есть в HTML страницы
        assert expected_text in driver.page_source
        print(f"✅ Комментарий найден: {expected_text}")
    except AssertionError:
        raise AssertionError(f"❌ Комментарий не найден на странице: {expected_text}")
    #driver = context.driver
    #expected_text = context.comment_text  # достаём текст, добавленный на предыдущем шаге

    #try:
    #    page.wait_for_text(expected_text)
    #    print(f"✅ Комментарий найден: {expected_text}")
    #except Exception:
    #    raise AssertionError(f"❌ Комментарий не найден на странице: {expected_text}")
