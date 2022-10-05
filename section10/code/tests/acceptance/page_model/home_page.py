from page_model.base_page import BasePage
from locators.home_page import HomePageLocators

class HomePage(BasePage):

    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAV_LINK)