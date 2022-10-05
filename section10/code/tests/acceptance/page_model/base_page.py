from locators.base_page import BasePageLocators
from locators.home_page import HomePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAV_LINK)