from random import randint

import pytest
from base import BaseCase


class TestMyTarget(BaseCase):

    def test_authorization(self, authorization):
        username = self.main_page.find(self.main_page.locators.USERNAME)
        print(username)
        assert username.get_attribute('title') == 'test-mail-artz@yandex.ru'

    def test_wrong_authorization(self):
        self.welcome_page.click(self.welcome_page.locators.LOGIN_BUTTON_FIRST)
        email_field = self.welcome_page.find(self.welcome_page.locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(randint(1, 100))
        password_field = self.welcome_page.find(self.welcome_page.locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(randint(1, 100))
        self.welcome_page.click(self.welcome_page.locators.LOGIN_BUTTON_SECOND)
        assert 'Invalid login or password' in self.driver.page_source
