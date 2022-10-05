from behave import *
from page_model.home_page import HomePage

DRIVER_PATH = 'C:/Development/chromedriver'

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = HomePage(context.driver)
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = HomePage(context.driver)
    assert page.title.text == content