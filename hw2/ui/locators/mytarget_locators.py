from selenium.webdriver.common.by import By


class BasePageLocators(object):
    pass


class WelcomePageLocators(BasePageLocators):
    LOGIN_BUTTON_FIRST = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    LOGIN_BUTTON_SECOND = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')


class MainPageLocators(BasePageLocators):
    USERNAME = (By.CLASS_NAME, 'right-module-userNameWrap-34ibLS')
