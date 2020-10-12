from random import randint

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.welcome_page import WelcomePage
from ui.pages.main_page import MainPage
from ui.pages.segment_page import SegmentPage


class UnsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def welcome_page(driver):
    return WelcomePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


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
def authorized_driver(welcome_page):
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
    yield welcome_page


@pytest.fixture(scope='function')
def segment_creating(authorized_driver, segment_page):
    go_to_segments_creating(segment_page)
    segment_name = create_segment(segment_page)
    yield segment_name


def create_segment(segment_page):
    segment_page.click(segment_page.locators.ADDING_CHECKBOX)
    segment_page.click(segment_page.locators.ADD_SEGMENT_BUTTON)
    segment_name_field = segment_page.find(segment_page.locators.SEGMENT_NAME_FIELD)
    segment_name_field.clear()
    segment_name = f'Segment {randint(1, 100)}{randint(1, 100)}'
    segment_name_field.send_keys(segment_name)
    segment_page.click(segment_page.locators.CREATE_SEGMENT_BUTTON)
    return segment_name


def go_to_segments_creating(segment_page):
    segment_page.click(segment_page.locators.AUDIENCES)
    segments_count = segment_page.find(segment_page.locators.SEGMENTS_COUNT)
    if segments_count.text == '0':
        segment_page.click(segment_page.locators.CREATE_SEGMENT_HREF)
    else:
        segment_page.click(segment_page.locators.CREATE_SEGMENT_BUTTON)
