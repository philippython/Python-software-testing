from page_model.base_page import BasePage

class  BlogPage(BasePage):

    def url(self):
        return super(BlogPage, self).url + '/blog'

    
