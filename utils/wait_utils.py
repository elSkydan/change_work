import os
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Настраиваем простой логгер
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

class WaitUtils:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _save_screenshot(self, name):
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(path)
        logging.info(f"📸 Скриншот сохранён: {path}")

    def wait_for_text(self, text):
        logging.info(f"⏳ Ожидаем появления текста: '{text}'")
        try:
            return self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{text}')]")
                )
            )
        except Exception as e:
            logging.error(f"❌ Не найден текст: '{text}'")
            self._save_screenshot("wait_for_text_fail")
            raise e

    def wait_for_element(self, locator):
        logging.info(f"⏳ Ожидаем элемент: {locator}")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logging.error(f"❌ Элемент не найден или невидим: {locator}")
            self._save_screenshot("wait_for_element_fail")
            raise e

    def wait_and_click(self, locator):
        logging.info(f"🖱 Пытаемся кликнуть элемент: {locator}")
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            logging.info(f"✅ Клик выполнен: {locator}")
        except Exception as e:
            logging.error(f"❌ Не удалось кликнуть по элементу: {locator}")
            self._save_screenshot("wait_and_click_fail")
            raise e
