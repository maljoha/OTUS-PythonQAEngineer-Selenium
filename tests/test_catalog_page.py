import allure

from pages.base import Base
from pages.catalog_page import CatalogPage


@allure.parent_suite("Каталог")
@allure.suite("Проверка форм")
class TestCatalogPage:

    @allure.sub_suite("Шапка")
    @allure.title("Наличие главных элементов страницы")
    def test_general_tabs(self, driver):
        base = Base(driver)
        base.open_page(CatalogPage.URL)
        base.check_all_general_tabs()

    @allure.sub_suite("Блоки меню")
    @allure.title("Вертикальное и горизонтальное")
    def test_catalog_tabs(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_catalog_tabs()

    @allure.sub_suite("Блок поиска")
    @allure.title("Поля сортировки")
    def test_sort_fields(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_sort_fields()

    @allure.sub_suite("Блок поиска")
    @allure.title("Поля пагинации")
    def test_pagination_fields(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_pagination_fields()

    @allure.sub_suite("Результаты поиска")
    @allure.title("Пагинация")
    def check_pagination_limit(self, driver):
        cat = CatalogPage(driver)
        cat.open_page(CatalogPage.URL)
        cat.check_pagination_limit()
