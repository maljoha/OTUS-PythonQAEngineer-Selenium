from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import get_url


class Base:
    """Базовый класс с общими селекторами и методами для всех/большинства страниц"""

    # верхняя навигационная панель
    NAV_TAB = (By.CSS_SELECTOR, "nav#top")
    CURRENCY_MENU = (By.CSS_SELECTOR, 'button.btn.btn-link.dropdown-toggle')
    CURRENCIES = (By.CSS_SELECTOR, 'div.btn-group.open>ul.dropdown-menu>li')
    MY_ACCOUNT_MENU = (By.CSS_SELECTOR, 'a[title="My Account"]')
    REGISTER_LINK = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]/li/a[.="Register"]')
    # шапка сайта
    HEADER_TAB = (By.CSS_SELECTOR, "header>div.container")
    # логотип
    LOGO = (By.CSS_SELECTOR, "div#logo")
    # строка поиска
    SEARCH = (By.CSS_SELECTOR, "[name='search']")
    # панель меню
    MENU_TAB = (By.CSS_SELECTOR, "nav#menu")

    # заголовок страницы
    @staticmethod
    def h1_name(page_name=""):
        return (By.XPATH, f'//h1[contains(text(), "{page_name}")]')

    # текущая валюта в верхней навигационной панели
    @staticmethod
    def current_currency(cur_symb="$"):
        return (By.XPATH, f'//strong[contains(text(), "{cur_symb}")]')

    # валюта в выпадающем списке
    @staticmethod
    def currency_item(cur_symb="$"):
        return (By.XPATH, f'//ul[@class="dropdown-menu"]/li/button[contains(text(), "{cur_symb}")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.url = get_url()

    def wait_element(self, loc: tuple) -> WebElement:
        """
        Ожидание появления элемента.
        :param loc: ожидаемый элемент
        :return: возвращает веб-элемент
        """
        self.wait.until(lambda driver: Base(driver).check_element_exists(loc))
        return self.driver.find_element(*loc)

    def open_page(self, page_url=""):
        """
        Открытие страницы + ожидание видимости логотипа как знак, что страница загрузилась.
        :param page_url: путь к странице без домена
        """
        self.driver.get(self.url + page_url)
        self.wait_element(self.LOGO)

    def click(self, selector):
        """
        Клик по элементу с учётом ожидания его кликабельности.
        :param selector: селектор элемента
        """
        self.wait.until(EC.element_to_be_clickable(selector))
        self.driver.find_element(*selector).click()

    def fill_field(self, selector: tuple, text: str):
        """
        Заполнение текстом поля для ввода.
        :param selector: селектор заполняемого поля
        :param text: вводимый текст
        """
        self.driver.find_element(*selector).clear()
        self.driver.find_element(*selector).send_keys(text)

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

    def get_currencies(self) -> list:
        """Получение списка валют из открытого меню валют."""
        currencies = []
        for cur in self.driver.find_elements(*self.CURRENCIES):
            cur_symb = cur.text.split(" ", 1)
            currencies.append(cur_symb[0])
        return currencies
