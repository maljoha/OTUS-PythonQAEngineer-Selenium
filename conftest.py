import pytest
from selenium import webdriver
import os

DRIVERS = os.path.expanduser("~/drivers")
URL = ''

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://demo.opencart.com", help="This is request url")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")

@pytest.fixture(scope="session", autouse=True)
def set_url(request):
    global URL
    URL = request.config.getoption("--url")

def get_url():
    return URL

@pytest.fixture(scope="session", autouse=True)
def driver(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        driver = None

    driver.get(url)

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
