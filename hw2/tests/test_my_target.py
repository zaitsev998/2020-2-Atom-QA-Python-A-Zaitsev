from random import randint
from settings import LINK, EMAIL
import pytest
from base import BaseCase


class TestMyTarget(BaseCase):

    def test_authorization(self, authorized_driver):
        username = self.main_page.find(self.main_page.locators.USERNAME)
        assert username.get_attribute('title') == EMAIL

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

    def test_segment_creating(self, authorized_driver):
        segment_name = self.segment_page.create_segment()
        self.segment_page.find(self.segment_page.locators.segment_locator(segment_name=segment_name))
        self.segment_page.delete_segment(segment_name)

    def test_segment_deleting(self, authorized_driver):
        segment_name = self.segment_page.create_segment()
        self.segment_page.delete_segment(segment_name)
        assert segment_name not in self.segment_page.driver.page_source

    @pytest.mark.skip
    def test_campaign_creating(self, authorized_driver):
        self.main_page.go_to_campaign_creating()
        campaign_name = self.campaigns_page.create_campaign()
        assert campaign_name in self.campaigns_page.driver.page_source
