from tests.pages.base_page import BasePage




class VisitorLogPage:

    def is_log_saved(self, firstname, secondname):
        # Получаем все логи для дебага
        logs = self.get_all_logs()
        print(f"All logs: {logs}")  # Печатаем все логи, чтобы понять, что ищется

        for log in logs:
            print(f"Checking log: {log}")  # Печатаем текущий лог для проверки
            if firstname.lower() in log['firstname'].lower() and secondname.lower() in log['secondname'].lower():
                return True
        return False
