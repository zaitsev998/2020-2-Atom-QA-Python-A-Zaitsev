import pytest
from base import BaseCase


class TestMyTarget(BaseCase):

    def test_authorization(self, authorization):
        username = self.main_page.find(self.main_page.locators.USERNAME)
        print(username)
        assert username.get_attribute('title') == 'test-mail-artz@yandex.ru'