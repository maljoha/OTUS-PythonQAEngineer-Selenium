from selenium.webdriver.common.by import By

from pages.base import Base


class AdminPage(Base):
    """Класс страницы админки"""

    URL = "/admin/"

    ADMIN = {"login": "user",
             "password": "bitnami"}

    LOGO = (By.CSS_SELECTOR, "img[title=OpenCart]")
    """Страница авторизации"""
    USERNAME = (By.CSS_SELECTOR, "input#input-username")
    PASSWORD = (By.CSS_SELECTOR, "input#input-password")
    LOGIN_BTN = (By.XPATH, '//button[contains(text(), "Login")]')
    FOGOTTEN_PASSWORD = (By.XPATH, '//a[.="Forgotten Password"]')
    """Админка"""
    # шапка
    LOGOUT_LINK = (By.XPATH, '//span[.="Logout"]')
    # левое меню разделов админки
    CATALOG_LINK = (By.XPATH, '//ul[@id="menu"]/li/a[contains(text(), "Catalog")]')
    PRODUCTS_LINK = (By.XPATH, '//ul[@id="collapse1"]/li/a[contains(text(), "Products")]')
    """Раздел 'Products'"""
    ADD_BTN = (By.CSS_SELECTOR, "i.fa.fa-plus")
    DELETE_BTN = (By.CSS_SELECTOR, "button.btn.btn-danger")
    PRODUCT_CHKB = (By.XPATH, '//input[@type="checkbox"]')
    """Добавление нового товара"""
    SAVE_BUTTON = (By.CSS_SELECTOR, "i.fa.fa-save")
    DATA_TAB = (By.XPATH, '//li/a[@data-toggle="tab"][.="Data"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, "input#input-name1")
    META_TAG_TITLE = (By.CSS_SELECTOR, "input#input-meta-title1")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-dismissible")
    MODEL = (By.CSS_SELECTOR, "input#input-model")

    def open_page(self, page_url=""):
        """
        Открытие страницы + ожидание видимости логотипа как знак, что страница загрузилась.
        :param page_url: путь к странице без домена
        """
        self.driver.get(self.url + page_url)
        self.wait_element(self.LOGO)

    def check_page_elements(self):
        """Проверка наличия элементов на странице"""
        tabs = [{"name": "логотип", "loc": self.LOGO},
                {"name": "поле для ввода логина", "loc": self.USERNAME},
                {"name": "поле для ввода пароля", "loc": self.PASSWORD},
                {"name": "ссылка для восстановления пароля", "loc": self.FOGOTTEN_PASSWORD},
                {"name": "кнопка для авторизации", "loc": self.LOGIN_BTN}]
        self.check_all_tabs(tabs)

    def admin_login(self):
        """Авторизация админом + ожидание видимости ссылки для логаута, как знак успешной авторизации."""
        self.fill_field(self.USERNAME, self.ADMIN["login"])
        self.fill_field(self.PASSWORD, self.ADMIN["password"])
        self.click(self.LOGIN_BTN)
        self.wait_element(self.LOGOUT_LINK)

    def open_products_section(self):
        """Переход в раздел Products + ожидание наменования раздела, как знак успешного перехода."""
        self.click(self.CATALOG_LINK)
        self.click(self.PRODUCTS_LINK)
        self.wait_element(self.h1_name("Products"))

    def open_add_products_page(self):
        """Переход в раздел добавления нового товара + ожидание кнопки сохранения, как знак успешного перехода."""
        self.click(self.ADD_BTN)
        self.wait_element(self.SAVE_BUTTON)

    def check_alert_message(self):
        """
        Проверка сообщения после операций с товарами.
        В случае если тест запускается на localhost, метод завершается проверкой на успешное сохранение товара,
        если тест запускается на удаленном сервере, например на https://demo.opencart.com, - проверяется сообщение
        на отсутствии прав на сохранение нового товара.
        """
        text = self.wait_element(self.ALERT_MESSAGE).text.strip().replace("\n×", "")
        if "localhost" in self.url:
            assert text == "Success: You have modified products!", "Отсутствует сообщение об успешном изменении товара"
        else:
            assert text == "Warning: You do not have permission to modify products!", "Отсутствует ожидаемое сообщение"

    def add_new_product(self):
        """Добавление нового товара."""
        self.open_add_products_page()
        self.fill_field(self.PRODUCT_NAME, 'Test name')
        self.fill_field(self.META_TAG_TITLE, 'Test meta tag')
        self.click(self.DATA_TAB)
        self.fill_field(self.MODEL, 'Test model')
        self.click(self.SAVE_BUTTON)
        self.check_alert_message()

    def delete_product(self):
        """Удаление товара."""
        self.driver.find_elements(*self.PRODUCT_CHKB)[1].click()
        self.click(self.DELETE_BTN)
        self.driver.switch_to.alert.accept()
        self.check_alert_message()
