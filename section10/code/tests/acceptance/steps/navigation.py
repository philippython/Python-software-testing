from behave import *
from selenium import webdriver
from page_model.blog_page import BlogPage
from page_model.home_page import HomePage


DRIVER_PATH = 'C:/Development/chromedriver'

use_step_matcher('re')

@given('I am on the Homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(DRIVER_PATH)
    page = HomePage(context.driver)
    page.driver.get(page.url)  
     

#  testing second scenario
@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(DRIVER_PATH)
    page = BlogPage(context.driver)
    page.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    page = BlogPage(context.driver)
    expected_url = page.driver.get(page.url)
    assert context.driver.current_url == expected_url

@then('I am on the Homepage')
def step_impl(context):
    page = HomePage(context.driver)
    expected_url = page.driver.get(page.url)
    assert context.driver.current_url == expected_url
