from selenium import webdriver
from bs4 import BeautifulSoup   
import pandas as pd
import datetime
import time
import json
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import sys, csv
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
from selenium.webdriver.common.by import By
#import chromedriver_autoinstaller as chromedriver
#chromedriver.install()
#from webdriver_manager.chrome import ChromeDriverManager
import os


creds_file= "cred.json"
f1 = open(creds_file)
request_data = json.load(f1)

#self.session = boto3.Session(aws_access_key_id=request_data['Accesss_Key'],aws_secret_access_key=request_data['Secret_Key'])
        
#options = webdriver.ChromeOptions()

#/Applications/Google Chrome.app/Contents/MacOS/Google Chrome

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path = DRIVER_BIN) #'/Applications/Google Chrome.app/Contents/MacOS/chromedriver')#options=optison)

driver.get("https://sports.bet9ja.com/mobile/login")
time.sleep(10)

#WebDriverWait(driver, 20)
driver.find_element(by=By.XPATH, value="//input[@placeholder=\"Username\"]").send_keys(request_data['username'])
driver.find_element(by=By.XPATH, value="//input[@placeholder=\"Password\"]").send_keys(request_data["password"])
driver.find_element(by=By.XPATH, value="//button[@class=\"btn w-full mt15\"]").click() #login
print('click 1 Done')
time.sleep(7)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/main/div[2]/div[1]/div/div/div/a").click() #prompt
print('click 2 done')
driver.find_element(by=By.XPATH, value='//*[@id="iconslider_1549_league_element"]').click()
print('click 3 Done')
##########################################
#https://vsmobile.bet9ja.com/bet9ja-mobile/login/?game=league
driver.get("https://vsmobile.bet9ja.com/bet9ja-mobile/login/?game=league&mode=premier&lang=") #opening league
print('league opned ')
#/html/body/div[3]/div[1]/div[2]/div[7]/div[2]/ul/li[2]/a
av = 1
while av == 1:
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="li_tab_id_GoalGoal_NoGoal"]').click() #goal goal clicked
        print('goal goal clicked')
        av += 1
    except Exception as e:
        time.sleep(3)
        print(e)


########################################################################################



#driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/div/div").click()
#print('click 4 Done')
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/main/div[2]/div[1]/div/div/div/a"))).click()