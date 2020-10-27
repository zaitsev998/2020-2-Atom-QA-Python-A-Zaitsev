from random import randint
import os
from selenium.webdriver import ActionChains
from ui.pages.base_page import BasePage
from ui.locators.mytarget_locators import CampaignsPageLocators
from settings import LINK, EMAIL


class CampaignsPage(BasePage):
    locators = CampaignsPageLocators()

    def create_campaign(self, campaign_name=None):
        if campaign_name is None:
            campaign_name = f"Campaign {randint(1, 100)}{randint(1, 100)}"
        self.click(self.locators.TRAFFIC_BUTTON)
        link_field = self.find(self.locators.LINK_FIELD)
        link_field.clear()
        link_field.send_keys(LINK)
        campaign_name_field = self.find(self.locators.CAMPAIGN_NAME_FIELD)
        self.click(self.locators.CAMPAIGN_NAME_FIELD_CLEAR_BUTTON)
        campaign_name_field.send_keys(campaign_name)
        self.click(self.locators.BANNER_BUTTON)
        self.click(self.locators.PIN_BUTTON)
        # Попытка 1
        image_from_library = self.find(self.locators.IMAGE_FROM_LIBRARY)
        image_preview = self.find(self.locators.IMAGE_PREVIEW)
        ac = ActionChains(self.driver)
        ac.drag_and_drop(image_from_library, image_preview).perform()
        # Попытка 2
        ac.click_and_hold(image_from_library).move_to_element(image_preview).release().perform()
        # Попытка 3
        file_input = self.find(self.locators.FILE_INPUT)
        filepath = os.path.abspath("63C08B.jpg")
        file_input.send_keys(filepath)
        self.click(self.locators.CREATE_CAMPAIGN_LAST_BUTTON)
        return campaign_name
