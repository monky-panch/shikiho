##
##
##


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
import sys

args = sys.argv

driver =  webdriver.Firefox()
driver.get('https://www.rakuten-sec.co.jp/')
mail = driver.find_element_by_name('loginid')
pass_wd = driver.find_element_by_name('passwd')
mail.send_keys(args[1]) #user-name
pass_wd.send_keys(args[2]) #password
pass_wd.submit()
