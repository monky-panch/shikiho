##
##	事前準備：gecodriverを事前に入れておいてください。
##


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
import sys

args = sys.argv # >python3 login.py loginname loginpass

#login
driver =  webdriver.Firefox()
driver.get('https://s10.kabu.co.jp/_mem_bin/members/login.asp?/members/')
mail = driver.find_element_by_name('SsLogonUser')
pass_wd = driver.find_element_by_id('PASSWORD1')
mail.send_keys(args[1]) #user-name
pass_wd.send_keys(args[2]) #password
pass_wd.submit()

#ログインが完了するまで少し待ちます。これが重要
sleep(10)

#input and click searchbox
meigara_code = driver.find_element_by_name('SearchWord')
meigara_code.send_keys('9984')
#meigara_code.submit()


