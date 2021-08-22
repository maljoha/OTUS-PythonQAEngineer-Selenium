from pages.register_page import RegisterPage


class TestRegisterPage:

    def test_register_user(self, driver):
        page = RegisterPage(driver)
        page.open_register_page()
        page.add_new_user()
