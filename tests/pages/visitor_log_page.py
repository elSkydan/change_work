from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VisitorLogPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_logs_to_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, "visitorsTable"))
        )

    def get_all_logs(self):
        try:
            self.wait_for_logs_to_load()
        except Exception:
            print("⚠️ Logs did not appear within timeout")
            return []

        table = self.driver.find_element(By.ID, "visitorsTable")
        rows = table.find_elements(By.TAG_NAME, "tr")
        logs = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 2:
                firstname = cells[0].text
                secondname = cells[1].text
                logs.append({"firstname": firstname, "secondname": secondname})
        return logs

    def is_log_saved(self, firstname, secondname):
        logs = self.get_all_logs()
        print(f"All logs: {logs}")

        for log in logs:
            print(f"Checking log: {log}")
            if firstname.lower() in log['firstname'].lower() and secondname.lower() in log['secondname'].lower():
                return True
        return False
