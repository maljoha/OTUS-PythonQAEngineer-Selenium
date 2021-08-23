from selenium.webdriver.common.by import By

from pages.base import Base


class MainPage(Base):
    """Класс Главной страницы"""

    # текущая картинка предлагаемых товаров
    PRODUCT_IMG = (By.CSS_SELECTOR, "div#slideshow0 div.swiper-slide-duplicate-active img.img-responsive")
    # кружки для переключения товаров
    PRODUCT_SWIPER_BULLET = (By.CSS_SELECTOR, "div.slideshow0 span.swiper-pagination-bullet")
    # предлагаемые товары
    FEATURED = (By.CSS_SELECTOR, "div.product-thumb.transition")
    # карусель с лейблами
    LABELS_CAROUSELE = (By.CSS_SELECTOR, "div#carousel0")
