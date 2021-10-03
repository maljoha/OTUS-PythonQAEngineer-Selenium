import allure
from selenium.webdriver.common.by import By

from pages.base import Base


class CatalogPage(Base):
    """Класс страницы каталога"""

    URL = "/index.php?route=product/category&path=20"

    # строка расположения каталога
    CATALOG_DIRECTORY = (By.CSS_SELECTOR, "ul.breadcrumb")
    # столбец разделов каталога
    CATALOG_SECTIONS = (By.CSS_SELECTOR, "div.list-group")

    # поля сортировки
    SORT_LABEL = (By.CSS_SELECTOR, 'label[for="input-sort"]')
    SORT_SELECT = (By.CSS_SELECTOR, 'select#input-sort')

    # поля пагинации
    PAG_LABEL = (By.CSS_SELECTOR, 'label[for="input-limit"]')
    PAG_SELECT = (By.CSS_SELECTOR, 'select#input-limit')
    PAG_SELECTED_OPTION = (By.CSS_SELECTOR, 'select#input-limit>option[selected=selected]')

    # карточка товара в каталоге
    PRODUCT_THUMBS = (By.CSS_SELECTOR, 'div.product-grid>div.product-thumb')

    @allure.step("Проверка наличия необходимых блоков в разделе каталога")
    def check_catalog_tabs(self):
        """Проверка наличия необходимых блоков в разделе каталога"""
        tabs = [{"name": "Строка расположения каталога", "loc": self.CATALOG_DIRECTORY},
                {"name": "Столбец разделов каталога", "loc": self.CATALOG_SECTIONS}]
        self.check_all_tabs(tabs)

    @allure.step("Проверка наличия сортировки товаров в каталоге")
    def check_sort_fields(self):
        """Проверка наличия сортировки товаров в каталоге"""
        tabs = [{"name": "Название поля сортировки", "loc": self.SORT_LABEL},
                {"name": "Выпадающий список с типами сортировки", "loc": self.SORT_SELECT}]
        self.check_all_tabs(tabs)

    @allure.step("Проверка наличия полей пагинации товаров в каталоге")
    def check_pagination_fields(self):
        """Проверка наличия полей пагинации товаров в каталоге"""
        tabs = [{"name": "Название поля пагинации", "loc": self.PAG_LABEL},
                {"name": "Выпадающий список с количеством страниц", "loc": self.PAG_SELECT}]
        self.check_all_tabs(tabs)

    @allure.step("Проверка соответствия выбранного количества элементов на стрнице с фактическим количеством")
    def check_pagination_limit(self):
        """Проверка соответствия выбранного количества элементов на стрнице с фактическим количеством"""
        limit = int(self.driver.find_element(*self.PAG_SELECTED_OPTION).text)
        actual_quantity = len(self.driver.find_elements(*self.PRODUCT_THUMBS))
        assert actual_quantity <= limit, "Некорректная пагинация страниц"
