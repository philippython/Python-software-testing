from section10.code.tests.acceptance.page_model.base_page import BasePage


from page_model.base_page import BasePage

class HomePage(BasePage):

    def url(self):
        return super(HomePage, self).url + '/'
