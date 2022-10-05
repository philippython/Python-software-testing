from page_model.base_page import BasePage
from locators.blog_page import BlogPageLocators

class  BlogPage(BasePage):

    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def add_post_link(self):

