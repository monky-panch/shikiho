import requests
from bs4 import BeautifulSoup


target_url = 'http://yahoo.co.jp'
target_url = 'https://member.rakuten-sec.co.jp/app/info_jp_quarterly.do;BV_SessionID=307855EFEDC233C794EE3FB980892E16.47a66bab?eventType=init&dscrCd=99480'
htmldate = requests.get(target_url)
try:
    soup = BeautifulSoup(htmldate.text,'lxml')
except:
    soup = BeautifulSoup(htmldate.text,'html5lib')

print(soup)
