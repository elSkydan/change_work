import os

import pytest

from utils.browser_factory import get_browser


@pytest.fixture
def driver():
    driver = get_browser()
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    return "https://elskydan.github.io/free_domen/"

