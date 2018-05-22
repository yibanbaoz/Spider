#coding:utf-8
import requests
from bs4 import BeautifulSoup

res = requests.get('https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_17045870298188545554%22%7D&n_type=0&p_from=1')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.content,'html.parser')
print(soup.text)
