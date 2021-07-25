from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_url


class Base:
    """Базовый класс с общими селекторами и методами для всех/большинства страниц"""

    # верхняя навигационная панель
    NAV_TAB = (By.CSS_SELECTOR, "nav#top")
    # шапка сайта
    HEADER_TAB = (By.CSS_SELECTOR, "header>div.container")
    # логотип
    LOGO = (By.CSS_SELECTOR, "div#logo")
    # строка поиска
    SEARCH = (By.CSS_SELECTOR, "[name='search']")
    # панель меню
    MENU_TAB = (By.CSS_SELECTOR, "nav#menu")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.url = get_url()

    def wait_element(self, loc: tuple):
        """
        Ожидание появления элемента.
        :param loc: ожидаемый элемент
        """
        self.wait.until(lambda driver: Base(driver).check_element_exists(loc))

    def open_page(self, url=""):
        """
        Открытие страницы + ожидание видимости логотипа как знак, что страница загрузилась.
        :param url: путь к странице без домена
        """
        self.driver.get(self.url + url)
        self.wait_element(self.LOGO)

    def check_element_exists(self, loc: tuple) -> bool:
        """
        Проверка наличия элемента.
        :param loc: ожидаемый элемент
        """
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            return False
        else:
            return True

    def check_all_tabs(self, locs: List[dict]):
        """
        Проверка наличия необходимых локаторов на странице
        :param locs: перечень локаторов и их наименование, выводимое в ошибку при отсутствии
        """
        ok = True
        for tab in locs:
            exists = self.check_element_exists(tab["loc"])
            tab["ok"] = exists
            ok = ok * exists
        failed_tabs = [t["name"] for t in locs if not t["ok"]]
        assert ok, f"Отсутствует {failed_tabs}"

    def check_all_general_tabs(self):
        """Проверка наличия необходимых блоков в шапке страницы"""
        tabs = [{"name": "Панель навигации", "loc": self.NAV_TAB},
                {"name": "Шапка сайта", "loc": self.HEADER_TAB},
                {"name": "Панель меню", "loc": self.MENU_TAB}]
        self.check_all_tabs(tabs)
