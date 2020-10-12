from selenium.webdriver.common.by import By


class BasePageLocators(object):
    AUDIENCES = (By.XPATH, '//a[@href="/segments"]')


class WelcomePageLocators(BasePageLocators):
    LOGIN_BUTTON_FIRST = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    LOGIN_BUTTON_SECOND = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')


class MainPageLocators(BasePageLocators):
    USERNAME = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')


class SegmentCreatingPageLocators(BasePageLocators):
    ADDING_SEGMENT_SOURCE = (By.CLASS_NAME, "adding-segments-source__expand js-expanded")
    PAYING_CHECKBOX = (By.ID, 'view-374-pay')
    ADDING_CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Добавить сегмент")]')
    SEGMENT_NAME_FIELD = (By.XPATH, '//input[@maxlength="60"]')
    CREATE_SEGMENT_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')
    CREATE_SEGMENT_HREF = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    DELETE_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Удалить")]')
    SEGMENTS_COUNT = (By.XPATH, '//a[@href="/segments/segments_list"]/span[contains(@class, "left-nav__count")]')

    @staticmethod
    def segment_locator(segment_name):
        segment_locator = (By.XPATH, f'//a[contains(@title, "{segment_name}")]')
        return segment_locator

    @staticmethod
    def segment_deleting_row(segment_name):
        row_locator = (By.XPATH, f'//*[contains(@title, "{segment_name}")]'
                                 f'/ancestor::div[contains(@class, "main-module-Cell")]')
        return row_locator

    @staticmethod
    def segment_deleting_button(id):
        button_locator = (By.XPATH, f'//div[contains(@data-test, "remove-{id}")]/span')
        return button_locator
