import allure

from pages.base import Base
from pages.login_page import LoginPage

@allure.parent_suite("Страница авторизации")
@allure.suite("Проверка форм")
class TestLoginPage:

    @allure.sub_suite("Шапка")
    @allure.title("Наличие главных элементов страницы")
    def test_general_tabs(self, driver):
        base = Base(driver)
        base.open_page(LoginPage.URL)
        base.check_all_general_tabs()

    @allure.sub_suite("Форма авторизации")
    @allure.title("Наличие главных полей формы авторизации")
    def test_main_elements(self, driver):
        login = LoginPage(driver)
        login.open_page(LoginPage.URL)
        login.check_main_elements()

    @allure.sub_suite("Форма авторизации")
    @allure.title("Наличие основных блоков формы авторизации")
    def test_main_blocks(self, driver):
        login = LoginPage(driver)
        login.open_page(LoginPage.URL)
        login.check_main_blocks()

