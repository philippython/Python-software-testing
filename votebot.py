import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DRIVER_PATH = 'C:/Development/chromedriver'
VOTING_URL = 'https://nigeriansdecide.com/gubernetorial-candidates/abia-state/'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get(VOTING_URL)
# makes the chrome button have a fullscreen size so that no buttons can be disturbed from being clicked
driver.fullscreen_window()

candidate_btn = driver.find_element(By.XPATH, '//*[@id="totalpoll-poll-3875"]/form/div[2]/div/div/div[2]/label[7]/div/div/div[1]/div')
cookie_btn = driver.find_element(By.XPATH, '//*[@id="cookie_action_close_header"]')
vote_btn = driver.find_element(By.XPATH, '//*[@id="totalpoll-poll-3875"]/form/div[4]/button[2]')
if vote_btn:
    cookie_btn.click()
    candidate_btn.click()
    vote_btn.click()

