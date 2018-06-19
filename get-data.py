import requests
from bs4 import BeautifulSoup


target_url = 'http://yahoo.co.jp'
htmldate = requests.get(target_url)
try:
    soup = BeautifulSoup(htmldate.text,'lxml')
except:
    soup = BeautifulSoup(htmldate.text,'html5lib')

print(soup)
