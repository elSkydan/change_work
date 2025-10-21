from tests.pages.base_page import BasePage


class VisitorLogPage(BasePage):
    def is_log_saved(self, firstname, secondname):
        full_name = f"{firstname} {secondname}"
        return full_name in self.driver.page_source
