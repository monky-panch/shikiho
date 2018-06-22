##
##	事前準備：gecodriverを事前に入れておいてください。
##


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
import sys
from selenium.common.exceptions import NoSuchElementException
import csv

datalist = []   #CSVなどに出力する用の変数

#引数チェック
args = sys.argv # >python3 login.py loginname loginpass

#CSVファイル出力
f = open('output.csv','w')
writer = csv.writer(f,lineterminator='\n')


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

#ここからループ 銘柄コード1301から9999
for corp_code in range(1300,9999):
    #銘柄を検索ボックスに入力
    meigara_code_searchbox = driver.find_element_by_id('codeSearch')
    meigara_code_searchbox.send_keys(corp_code)
    meigara_code_searchbox.submit()
    sleep(3)

    #入力コードが無効だった場合(四季報タブがない)の例外処理
    try:	
        #四季報タブをクリック
        driver.find_element_by_link_text('四季報').click()
        sleep(3)

        #企業情報タブ
        #サンプルコード
        #data[0] = driver.find_element_by_xpath("FirefoxからコピーしたXpath").text
        #print(data)

        #入力コードがETFなどの場合（企業概要タブはあるが、その下がない）の例外処理
        try:
            kihon_data = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[1]").text
        except:
            print('例外エラー：入力コード%dはETFまたはETNのようです' % corp_code)

        print('---企業概要タブ----')
    
        print('企業概要:紹介')
        print(kihon_data)
        datalist.append(kihon_data)

        kabunushi_data = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[2]/tbody/tr/td[1]").text
        print('企業概要：株主')
        print(kabunushi_data)
        datalist.append(kabushik_data)

        yakuin_data = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[2]/tbody/tr/td[3]").text
        print('企業概要：役員')
        print(yakuin_data)
        datalist.append(yakuin_data)

        #財務状況タブ
        print('---財務状況タブ---')
        driver.find_element_by_link_text('財務状況').click()
        sleep(3)

        zaimu_data = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[2]/tbody/tr[1]/td[1]/table/tbody").text
        print('財務状況：業績')        
        print(zaimu_data)
        datalist.append(zaimu_data)

        haitou_data = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[2]/tbody/tr[1]/td[3]/table[1]/tbody").text
        print('財務状況：配当')  
        print(haitou_data)
        datalist.append(haitou_data)

        yosou_haitou = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[2]/tbody/tr[1]/td[3]/table[2]/tbody").text
        print('財務状況：予想配当')  
        print(yosou_haitou)
        datalist.append(yosou_haitou)

        cf_data = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[3]/tbody/tr/td[1]/table[1]/tbody").text
        print('財務状況：時価総額・キャッシュフロー・指標')  
        print(cf_data)
        datalist.append(cf_data)

        zaimu_hyou = driver.find_element_by_xpath("/html/body/div[4]/div/table/tbody/tr/td[1]/div/div[8]/table[3]/tbody/tr/td[3]/table/tbody").text
        print('財務状況：財務')  
        print(zaimu_hyou )
        datalist.append(zaimu_hyou)

        #資本異動タブ
        print('---資本異動タブ---')
        driver.find_element_by_link_text('資本異動').click()
        sleep(3)

    except:
        print('例外エラー：入力コード%dが無効です' % corp_code)

        #ファイル出力
        writer.writerow(datalist)

 #end for

#ファイルCLOSE
f.close()

