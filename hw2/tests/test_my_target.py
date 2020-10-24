import os
from random import randint
from settings import LINK, EMAIL
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

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
        campaign_name = f"Campaign {randint(1, 100)}{randint(1, 100)}"
        self.go_to_campaign_creating()
        self.campaigns_page.click(self.campaigns_page.locators.TRAFFIC_BUTTON)
        link_field = self.campaigns_page.find(self.campaigns_page.locators.LINK_FIELD)
        link_field.clear()
        link_field.send_keys(LINK)
        campaign_name_field = self.campaigns_page.find(self.campaigns_page.locators.CAMPAIGN_NAME_FIELD)
        self.campaigns_page.click(self.campaigns_page.locators.CAMPAIGN_NAME_FIELD_CLEAR_BUTTON)
        campaign_name_field.send_keys(campaign_name)
        self.campaigns_page.click(self.campaigns_page.locators.BANNER_BUTTON)
        self.campaigns_page.click(self.campaigns_page.locators.PIN_BUTTON)
        # Попытка 1
        image_from_library = self.campaigns_page.find(self.campaigns_page.locators.IMAGE_FROM_LIBRARY)
        image_preview = self.campaigns_page.find(self.campaigns_page.locators.IMAGE_PREVIEW)
        ac = ActionChains(self.campaigns_page.driver)
        ac.drag_and_drop(image_from_library, image_preview).perform()
        # Попытка 2
        ac.click_and_hold(image_from_library).move_to_element(image_preview).release().perform()
        # Попытка 3
        file_input = self.campaigns_page.find(self.campaigns_page.locators.FILE_INPUT)
        filepath = os.path.abspath("63C08B.jpg")
        file_input.send_keys(filepath)
        self.campaigns_page.wait().until(EC.visibility_of(self.campaigns_page.locators.GREEN_SIGN))
        self.campaigns_page.click(self.campaigns_page.locators.CREATE_CAMPAIGN_LAST_BUTTON)
        assert campaign_name in self.campaigns_page.driver.page_source

    def go_to_campaign_creating(self):
        self.main_page.click(self.main_page.locators.CAMPAIGNS)
        try:
            self.campaigns_page.click(self.campaigns_page.locators.CREATE_CAMPAIGN_LINK)
        except TimeoutException:
            self.campaigns_page.click(self.campaigns_page.locators.CREATE_CAMPAIGN_BUTTON)
