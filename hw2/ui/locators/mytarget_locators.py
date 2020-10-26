from selenium.webdriver.common.by import By


class BasePageLocators(object):
    AUDIENCES = (By.XPATH, '//a[@href="/segments"]')
    CAMPAIGNS = (By.XPATH, '//a[@href="/dashboard"]')


class WelcomePageLocators(BasePageLocators):
    LOGIN_BUTTON_FIRST = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    LOGIN_BUTTON_SECOND = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')


class MainPageLocators(BasePageLocators):
    USERNAME = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')
    CREATE_CAMPAIGN_LINK = (By.XPATH, '//a[@href="campaign/new/"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and '
                                        'contains(text(), "Создать кампанию")]')


class SegmentPageLocators(BasePageLocators):
    ADDING_SEGMENT_SOURCE = (By.CLASS_NAME, "adding-segments-source__expand js-expanded")
    APPS_AND_GAMES = (By.XPATH, '//div[contains(text(), "Приложения и игры в соцсетях")]')
    PAYING_CHECKBOX = (By.ID, 'view-374-pay')
    ADDING_CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments-source__checkbox")]')
    ADD_SEGMENT_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Добавить сегмент")]')
    SEGMENT_NAME_FIELD = (By.XPATH, '//input[@maxlength="60"]')
    CREATE_SEGMENT_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')
    CREATE_SEGMENT_LINK = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
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


class CampaignsPageLocators(BasePageLocators):
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and '
                                        'contains(text(), "Создать кампанию")]')
    TRAFFIC_BUTTON = (By.XPATH, '//div[contains(text(), "Трафик")]')
    LINK_FIELD = (By.XPATH, '//input[contains(@placeholder, "Введите ссылку")]')
    CAMPAIGN_NAME_FIELD = (By.XPATH, '//input[@maxlength="255"]')
    CAMPAIGN_NAME_FIELD_CLEAR_BUTTON = (By.XPATH, '//div[contains(@class, "input__clear")]')
    BANNER_BUTTON = (By.XPATH, '//span[contains(text(), "Баннер")]')
    IMAGE_FROM_LIBRARY = (By.XPATH, '//img[contains(@class, "mediaLibrary-module-image-")]')
    CREATE_CAMPAIGN_LAST_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')
    IMAGE_PREVIEW = (By.XPATH, '//div[contains(@class, "imagePreview-module-emptyImageText")]')
    PIN_BUTTON = (By.XPATH, '//div[@title="Открепить блок со ставкой"]')
    UNPIN_PANEL = (By.XPATH, '//div[contains(@class, "button-module-textWrapper") and '
                             'contains(text(), "Открепить панель")]')
    FILE_INPUT = (By.XPATH, '//input[@type="file"]')
    SAVE_IMAGE = (By.XPATH, '//input[contains(@class, "image-cropper__save")]')
    GREEN_SIGN = (By.XPATH, '//div[contains(@class, "patternTabs-module-green-")]')
