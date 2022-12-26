import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DRIVER_PATH = 'C:/Development/chromedriver'
VOTING_URL = 'https://nigeriansdecide.com/gubernetorial-candidates/abia-state/'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get(VOTING_URL)
driver.add_argument("window-size=1200x600")

vote_btn = driver.find_element(By.XPATH, '//*[@id="totalpoll-poll-3875"]/form/div[2]/div/div/div[2]/label[7]/div/div/div[1]/div')
if vote_btn:
    print("found vote button")
    time.sleep(10)
    vote_btn.click()

driver.quit()
