from selenium.webdriver.common.by import By

from pages.base import Base


class LoginPage(Base):
    """Класс страницы логина"""

    URL = "/index.php?route=account/login"

    EMAIL = (By.CSS_SELECTOR, "input[name=email]")
    PASSWORD = (By.CSS_SELECTOR, "input[name=password]")
    LOGIN_BTN = (By.CSS_SELECTOR, "input.btn-primary[value=Login]")
    # названия основных блоков
    BLOCKS = (By.CSS_SELECTOR, "div.well>h2")

    def check_main_elements(self):
        """Проверка наличия необходимых элементов в разделе карточки товара"""
        tabs = [{"name": "поле для ввода е-мэйла", "loc": self.EMAIL},
                {"name": "поле для ввода пароля", "loc": self.PASSWORD},
                {"name": "кнопка для авторизации", "loc": self.LOGIN_BTN}]
        self.check_all_tabs(tabs)

    def get_blocks_names(self):
        """Получение списка названий блоков страницы авторизации"""
        return [bl.text for bl in self.driver.find_elements(*self.BLOCKS)]
