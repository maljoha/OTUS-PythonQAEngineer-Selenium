import allure

from pages.base import Base
from pages.product_page import ProductPage

@allure.parent_suite("Страница карточки товара")
@allure.suite("Проверка форм")
class TestProductPage:

    @allure.sub_suite("Шапка")
    @allure.title("Наличие главных элементов страницы")
    def test_general_tabs(self, driver):
        base = Base(driver)
        base.open_page(ProductPage.URL)
        base.check_all_general_tabs()


    @allure.sub_suite("Контент страницы")
    @allure.title("Фото товара")
    def test_check_photo(self, driver):
        product = ProductPage(driver)
        product.open_page(ProductPage.URL)
        assert len(driver.find_elements(*ProductPage.PRODUCT_IMG_LINK)) > 0, "Нет фото в карточке товара"

    @allure.sub_suite("Контент страницы")
    @allure.title("Главные элементы карточки товара")
    def test_main_elements(self, driver):
        product = ProductPage(driver)
        product.open_page(ProductPage.URL)
        product.check_main_elements()
