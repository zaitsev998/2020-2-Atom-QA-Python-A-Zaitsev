import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.welcome_page import WelcomePage
from ui.pages.main_page import MainPage


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def welcome_page(driver):
    return WelcomePage(driver=driver)\


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    selenoid = config['selenoid']
    version = config['version']
    url = config['url']
    browser = config['browser']
    if not selenoid:
        if browser == 'chrome':
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install())
        elif browser == 'firefox':
            manager = GeckoDriverManager(version='latest')
            driver = webdriver.Firefox(executable_path=manager.install())
        else:
            raise UnsupportedBrowserException(f"Unsupported browser {browser}")
    else:
        pass
    driver.get(url=url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def authorization(welcome_page):
    email = 'test-mail-artz@yandex.ru'
    password = 'test_mail_12345'
    welcome_page.click(welcome_page.locators.LOGIN_BUTTON_FIRST)
    email_field = welcome_page.find(welcome_page.locators.EMAIL_FIELD)
    email_field.clear()
    email_field.send_keys(email)
    password_field = welcome_page.find(welcome_page.locators.PASSWORD_FIELD)
    password_field.clear()
    password_field.send_keys(password)
    welcome_page.click(welcome_page.locators.LOGIN_BUTTON_SECOND)
    yield welcome_page.driver
