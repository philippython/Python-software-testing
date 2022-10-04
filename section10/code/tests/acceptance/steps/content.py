from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


DRIVER_PATH = 'C:/Development/chromedriver'

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    assert context.browser.find_element(by=By.TAG_NAME, value='title').is_displayed()

@step('The title tag has content "(.*)"')