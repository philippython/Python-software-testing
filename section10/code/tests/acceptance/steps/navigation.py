from behave import *
from selenium import webdriver

DRIVER_PATH = 'C:/Development/chromedriver'

use_step_matcher('re')

@given('I am on the Homepage')
def step_impl(context):
    context.browser = webdriver.Chrome(DRIVER_PATH)
    context.browser.get('http://127.0.0.1:5000')  

#  testing second scenario
@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome(DRIVER_PATH)
    context.browser.get('http://127.0.0.1:5000/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url

@then('I am on the Homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.browser.current_url == expected_url
