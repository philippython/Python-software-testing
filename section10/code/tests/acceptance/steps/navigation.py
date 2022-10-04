from behave import *
from selenium import webdriver

DRIVER_PATH = 'C:/Development/chromedriver'

use_step_matcher('re')

@given('I am on the Homepage')
def step_impl(context):
    browser = webdriver.Chrome(DRIVER_PATH)
    browser.get('http://127.0.0.1:5000')  

