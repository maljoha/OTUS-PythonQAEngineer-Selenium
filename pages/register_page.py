import allure
import mimesis
from mimesis import locales
from selenium.webdriver.common.by import By

from pages.base import Base


class RegisterPage(Base):
    """Класс регистрации нового пользователя."""

    FIRST_NAME = (By.CSS_SELECTOR, "input#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "input#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "input#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "input#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#input-confirm")
    AGREE_CHKB = (By.CSS_SELECTOR, 'input[name="agree"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'input[value="Continue"]')

    @allure.step("Открытие формы регистрации")
    def open_register_page(self):
        self.open_page()
        self.click(self.MY_ACCOUNT_MENU)
        self.click(self.REGISTER_LINK)
        self.wait_element(self.h1_name("Register Account"))

    @allure.step("Добавление нового пользователя")
    def add_new_user(self):
        person = mimesis.Person(locales.RU)
        self.fill_field(self.FIRST_NAME, person.name())
        self.fill_field(self.LAST_NAME, person.surname())
        self.fill_field(self.EMAIL, person.email(domains=["@mailforspam.com"]))
        self.fill_field(self.TELEPHONE, person.telephone())
        self.fill_field(self.PASSWORD, "123456789")
        self.fill_field(self.PASSWORD_CONFIRM, "123456789")
        self.click(self.AGREE_CHKB)
        self.click(self.CONTINUE_BTN)
        self.wait_element(self.h1_name("Your Account Has Been Created!"))
