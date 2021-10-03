import datetime
import logging
import os

import allure
import pytest
from selenium import webdriver

DRIVERS = os.path.expanduser("~/drivers")
URL = ''

logging.basicConfig(level=logging.INFO, filename="../log/test.log", format='[%(asctime)s] %(message)s')


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://demo.opencart.com", help="This is request url")
    # parser.addoption("--url", action="store", default="http://localhost", help="This is request url")
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption('--executor', action='store', help='Flag for selecting host', default='local')
    parser.addoption('--vnc', action='store_true', help='Flag for vnc connection', default=True)


@pytest.fixture(scope="session", autouse=True)
def set_url(request):
    global URL
    URL = request.config.getoption("--url")


def get_url():
    return URL

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(autouse=True)
def driver(request):
    logger = logging.getLogger('BrowserLogger')
    logger.info(f"\nSTART test {request.node.name}")

    url = request.config.getoption("--url")
    logger.info(f'Url {url}')

    browser = request.config.getoption("--browser")
    logger.info(f'Browser {browser}')

    vnc = request.config.getoption('--vnc')
    logger.info(f'vnc {vnc}')

    executor = request.config.getoption('--executor')

    maximized = request.config.getoption("--maximized")

    if executor == 'local':
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
        elif browser == "opera":
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
        else:
            driver = None
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        caps = {
            'browserName': browser,
            "selenoid:options": {
                "enableVNC": vnc
            }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    def finalizer():
        logger.info('Run finalizer')
        if request.node.rep_call.failed:
            logger.warning('The test is Failed. Adding screenshot')
            allure.attach(driver.get_screenshot_as_png(),
                          name=datetime.datetime.now().strftime('%d_%H-%M-%S-%f'),
                          attachment_type=allure.attachment_type.PNG)
        driver.quit()
        logger.info(f"\nFINISH test {request.node.name}")

    request.addfinalizer(finalizer)
    driver.get(url)

    if maximized:
        driver.maximize_window()

    return driver
