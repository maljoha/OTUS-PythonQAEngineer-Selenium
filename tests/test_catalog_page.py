from pages.base import Base
from pages.catalog_page import CatalogPage


class TestCatalogPage:

    def test_general_tabs(self, driver):
        base = Base(driver)
        base.open_page(CatalogPage.URL)
        base.check_all_general_tabs()

    def test_catalog_tabs(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_catalog_tabs()

    def test_sort_fields(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_sort_fields()

    def test_pagination_fields(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_pagination_fields()

    def test_pagination(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        limit = int(driver.find_element(*CatalogPage.PAG_SELECTED_OPTION).text)
        actual_quantity = len(driver.find_elements(*CatalogPage.PRODUCT_THUMBS))
        assert actual_quantity <= limit, "Некорректная пагинация страниц"
