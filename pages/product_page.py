import allure
from selenium.webdriver.common.by import By

from pages.base import Base


class ProductPage(Base):
    """Класс страницы карточки товара"""

    URL = "/index.php?route=product/product&path=20&product_id=42&limit=15"

    # наименование товара
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-4>h1")
    # превью фото товара
    PRODUCT_IMG_LINK = (By.CSS_SELECTOR, "a.thumbnail")
    # цена товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-4 h2")
    # описание товара
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.tab-content>div#tab-description")
    # кнопка добавления в корзину
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button#button-cart")

    @allure.step("Проверка наличия необходимых элементов в разделе карточки товара")
    def check_main_elements(self):
        """Проверка наличия необходимых элементов в разделе карточки товара"""
        tabs = [{"name": "наименование товара", "loc": self.PRODUCT_NAME},
                {"name": "цена товара", "loc": self.PRODUCT_PRICE},
                {"name": "описание товара", "loc": self.PRODUCT_DESCRIPTION},
                {"name": "кнопка добавления в корзину", "loc": self.ADD_TO_CART_BTN}, ]
        self.check_all_tabs(tabs)
