from pages.admin_page import AdminPage


class TestAdminPage:

    def test_main_elements(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.check_page_elements()

    def test_add_product(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.admin_login()
        admin.open_products_section()
        admin.add_new_product()

    def test_delete_product(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.admin_login()
        admin.open_products_section()
        admin.delete_product()
