from behave import *
from locators.home_page import HomePageLocators

DRIVER_PATH = 'C:/Development/chromedriver'

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    title = context.browser.find_element(*HomePageLocators.TITLE)
    assert title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    title =  context.browser.find_element(*HomePageLocators.TITLE)
    assert title.text == content