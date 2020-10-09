import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.welcome_page import WelcomePage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.welcome_page: WelcomePage = request.getfixturevalue('welcome_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
