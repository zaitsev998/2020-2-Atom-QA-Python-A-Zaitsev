from ui.pages.base_page import BasePage
from ui.locators.mytarget_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_campaign_creating(self):
        self.click(self.locators.CAMPAIGNS)
        try:
            self.click(self.locators.CREATE_CAMPAIGN_LINK)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON)