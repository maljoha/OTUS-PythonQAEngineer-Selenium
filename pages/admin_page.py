from selenium.webdriver.common.by import By

from pages.base import Base


class AdminPage(Base):
    """Класс страницы логина в админку"""

    URL = "/admin"

    # логотип
    LOGO = (By.CSS_SELECTOR, "img[title=OpenCart]")
    USERNAME = (By.CSS_SELECTOR, "input#input-username")
    PASSWORD = (By.CSS_SELECTOR, "input#input-password")
    LOGIN_BTN = (By.XPATH, '//button[contains(text(), "Login")]')
    FOGOTTEN_PASSWORD = (By.XPATH, '//a[.="Forgotten Password"]')

    def open_page(self, url):
        """
        Открытие страницы + ожидание видимости логотипа как знак, что страница загрузилась.
        :param url: путь к странице без домена
        """
        self.driver.get(self.url + url)
        self.wait_element(self.LOGO)

    def check_page_elements(self):
        """Проверка наличия элементов на страницеа"""
        tabs = [{"name": "логотип", "loc": self.LOGO},
                {"name": "поле для ввода логина", "loc": self.USERNAME},
                {"name": "поле для ввода пароля", "loc": self.PASSWORD},
                {"name": "ссылка для восстановления пароля", "loc": self.FOGOTTEN_PASSWORD},
                {"name": "кнопка для авторизации", "loc": self.LOGIN_BTN}]
        self.check_all_tabs(tabs)
