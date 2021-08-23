from selenium.webdriver.common.by import By

from pages.base import Base


class MainPage(Base):
    """Класс Главной страницы"""

    # текущая картинка предлагаемых товаров
    PRODUCT_IMG = (By.CSS_SELECTOR, "div#slideshow0 div.swiper-slide-duplicate-active img.img-responsive")
    # кружки для переключения товаров
    PRODUCT_SWIPER_BULLET = (By.CSS_SELECTOR, "div.slideshow0 span.swiper-pagination-bullet")
    # предлагаемые товары и их цены
    FEATURED = (By.CSS_SELECTOR, "div.product-thumb.transition")
    PRICE_NEW = (By.CSS_SELECTOR, "span.price-new")
    PRICE_OLD = (By.CSS_SELECTOR, "span.price-old")
    PRICE_TAX = (By.CSS_SELECTOR, "span.price-tax")
    # карусель с лейблами
    LABELS_CAROUSELE = (By.CSS_SELECTOR, "div#carousel0")

    def check_currency_change(self):
        """Проверка смены валют."""
        self.click(self.CURRENCY_MENU)
        currency_list = self.get_currencies()
        for curr_symb in currency_list:
            self.click(self.currency_item(curr_symb))
            self.wait_element(self.current_currency(curr_symb))
            for price_type in (self.PRICE_NEW, self.PRICE_OLD, self.PRICE_TAX):
                for price_elem in self.driver.find_elements(*price_type):
                    assert curr_symb in price_elem.text, f"В цене {price_elem.text} отсутствует валюта {curr_symb}"
            self.click(self.CURRENCY_MENU)
