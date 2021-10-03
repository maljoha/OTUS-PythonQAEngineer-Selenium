import allure

from pages.admin_page import AdminPage

@allure.parent_suite("Раздел администратора")
class TestAdminPage:

    @allure.suite("Страница авторизации")
    @allure.sub_suite("Проверка форм")
    @allure.title("Наличие главных элементов страницы")
    def test_main_elements(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.check_page_elements()

    @allure.suite("Личный кабинет Администратора")
    @allure.sub_suite("Раздел Products")
    @allure.title("Добавление нового товара")
    def test_add_product(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.admin_login()
        admin.open_products_section()
        admin.add_new_product()

    @allure.suite("Личный кабинет Администратора")
    @allure.sub_suite("Раздел Products")
    @allure.title("Удаление товара")
    def test_delete_product(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.admin_login()
        admin.open_products_section()
        admin.delete_product()
