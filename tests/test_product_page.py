from pages.base import Base
from pages.product_page import ProductPage


class TestProductPage:

    def test_general_tabs(self, driver):
        base = Base(driver)
        base.open_page(ProductPage.URL)
        base.check_all_general_tabs()

    def test_check_photo(self, driver):
        product = ProductPage(driver)
        product.open_page(ProductPage.URL)
        assert len(driver.find_elements(*ProductPage.PRODUCT_IMG_LINK)) > 0, "Нет фото в карточке товара"

    def test_main_elements(self, driver):
        product = ProductPage(driver)
        product.open_page(ProductPage.URL)
        product.check_main_elements()
