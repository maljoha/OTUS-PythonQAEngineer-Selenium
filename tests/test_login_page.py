from pages.base import Base
from pages.login_page import LoginPage


class TestLoginPage:

    def test_general_tabs(self, driver):
        base = Base(driver)
        base.open_page(LoginPage.URL)
        base.check_all_general_tabs()

    def test_main_elements(self, driver):
        login = LoginPage(driver)
        login.open_page(LoginPage.URL)
        login.check_main_elements()

    def test_main_blocks(self, driver):
        login = LoginPage(driver)
        login.open_page(LoginPage.URL)
        blocks = login.get_blocks_names()
        assert blocks == ['New Customer', 'Returning Customer'], "Некорректный набор блоков авторизации"
