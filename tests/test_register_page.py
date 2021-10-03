import allure

from pages.register_page import RegisterPage

@allure.parent_suite("Страница регистрации")
@allure.suite("Проверка форм")
class TestRegisterPage:

    @allure.sub_suite("Логика")
    @allure.title("Добавление нового польователя")
    def test_register_user(self, driver):
        page = RegisterPage(driver)
        page.open_register_page()
        page.add_new_user()
