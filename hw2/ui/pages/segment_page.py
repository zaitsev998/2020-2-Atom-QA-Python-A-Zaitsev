from random import randint

from ui.pages.base_page import BasePage
from ui.locators.mytarget_locators import SegmentPageLocators


class SegmentPage(BasePage):
    locators = SegmentPageLocators()

    def create_segment(self, segment_name=None):
        self.driver.get("https://target.my.com/segments/segments_list/new/")
        self.click(self.locators.APPS_AND_GAMES, timeout=30)
        self.click(self.locators.ADDING_CHECKBOX)
        self.click(self.locators.ADD_SEGMENT_BUTTON)
        segment_name_field = self.find(self.locators.SEGMENT_NAME_FIELD)
        segment_name_field.clear()
        if segment_name is None:
            segment_name = f'Segment {randint(1, 100)}{randint(1, 100)}'
        segment_name_field.send_keys(segment_name)
        self.click(self.locators.CREATE_SEGMENT_BUTTON)
        return segment_name

    def delete_segment(self, segment_name):
        row = self.find(self.locators.segment_deleting_row(segment_name=segment_name))
        id = row.get_attribute("data-test").split()[0].split("-")[1]
        self.click(self.locators.segment_deleting_button(id=id))
        self.click(self.locators.DELETE_BUTTON)
        self.driver.refresh()
