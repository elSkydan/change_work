import pytest
from utils.browser_factory import get_browser


@pytest.fixture
def driver():
    driver = get_browser()
    yield driver
    driver.quit()
