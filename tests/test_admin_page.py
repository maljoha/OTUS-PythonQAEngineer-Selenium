from pages.admin_page import AdminPage


class TestAdminPage:

    def test_main_elements(self, driver):
        admin = AdminPage(driver)
        admin.open_page(AdminPage.URL)
        admin.check_page_elements()
