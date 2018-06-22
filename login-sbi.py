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
driver.get('https://www.sbisec.co.jp/ETGate')
sleep(3)
mail = driver.find_element_by_name('user_id')
pass_wd = driver.find_element_by_name('user_password')
mail.send_keys(args[1]) #user-name
pass_wd.send_keys(args[2]) #password
pass_wd.submit()

sleep(3)

#ここからループ

#銘柄を検索ボックスに入力
meigara_code = driver.find_element_by_id('top_stock_sec')
meigara_code.send_keys('9984')
driver.find_element_by_id('searchStockFormSearchBtn').click()
sleep(3)

#四季報タブをクリック
#driver.find_element_by_link_text('四季報').click()
#sleep(3)

#driver.execute_script("showhide('id1').click()")
#driver.find_element_by_link_text('業績･財務').click()
#sleep(3)

#driver.find_element_by_link_text('資本移動').click()
#sleep(3)



