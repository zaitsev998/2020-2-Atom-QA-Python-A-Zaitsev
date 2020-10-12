from random import randint

import pytest
from base import BaseCase


class TestMyTarget(BaseCase):

    def test_authorization(self, authorized_driver):
        print(self.driver.page_source)
        username = self.main_page.find(self.main_page.locators.USERNAME)
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

    def test_segment_creating(self, segment_creating):
        assert self.segment_page.find(self.segment_page.locators.segment_locator(segment_name=segment_creating))

    def test_segment_deleting(self, segment_creating):
        row = self.segment_page.find(self.segment_page.locators.segment_deleting_row(segment_name=segment_creating))
        id = row.get_attribute("data-test").split()[0].split("-")[1]
        self.segment_page.click(self.segment_page.locators.segment_deleting_button(id=id))
        self.segment_page.click(self.segment_page.locators.DELETE_BUTTON)
        self.segment_page.driver.refresh()
        assert segment_creating not in self.segment_page.driver.page_source

