from page_model.base_page import BasePage
from locators.blog_page import BlogPageLocators

class BlogPage(BasePage):

    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)

    @property
    def posts_section(self):
        return self.driver.find_elements(*BlogPageLocators.POST_SECTION)

    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocators.HOME_LINK)

