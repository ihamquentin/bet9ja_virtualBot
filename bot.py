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


creds_file= "cred.json"
f1 = open(creds_file)
request_data = json.load(f1)

#self.session = boto3.Session(aws_access_key_id=request_data['Accesss_Key'],aws_secret_access_key=request_data['Secret_Key'])
        
options = webdriver.ChromeOptions()

#/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
driver = webdriver.Chrome('/Applications/Google Chrome.app/Contents/MacOS/chromedriver')#options=optison)

driver.get ("https://sports.bet9ja.com/mobile/login")
time.sleep(7)

driver.find_element_by_xpath("//input[@placeholder=\"Username\"]").send_keys(request_data['username'])
driver.find_element_by_xpath("//input[@placeholder=\"Password\"]").send_keys(request_data["password"])
driver.find_element_by_xpath("//button[@class=\"btn w-full mt15\"]").click()
#time.sleep(7)
#driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/main/div[2]/div[1]/div/div/div/a").click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/main/div[2]/div[1]/div/div/div/a"))).click()