from pages.base import Base
from pages.main_page import MainPage


class TestMainPage:
    def test_title(self, driver):
        base = Base(driver)
        base.open_page()
        assert driver.title == "Your Store", "Наименование страницы не 'Your Store'"

    def test_tabs(self, driver):
        base = Base(driver)
        base.open_page()
        Base(driver).check_all_general_tabs()

    def test_featured_count(self, driver):
        main = MainPage(driver)
        main.open_page()
        assert len(driver.find_elements(*main.FEATURED)) == 4, \
            "Некорректное количество предлагаемых товаров"

    def test_label_list_exists(self, driver):
        main = MainPage(driver)
        main.open_page()
        assert main.check_element_exists(MainPage(driver).LABELS_CAROUSELE), \
            "Отсутствует карусель с лейблами производителей на главной странице"

    def test_click_by_swiper_bullet(self, driver):
        main = MainPage(driver)
        main.open_page()
        prew_link = ""
        for bullet in driver.find_elements(*main.PRODUCT_SWIPER_BULLET):
            bullet.click()
            actual_link = driver.find_element(*main.PRODUCT_IMG).get_attribute("src")
            assert actual_link != prew_link, "Картинка отсутствует или не изменилась после свайпа"
            prew_link = actual_link

    def test_currency_change(self, driver):
        main = MainPage(driver)
        main.open_page()
        main.check_currency_change()
