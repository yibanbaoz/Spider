#coding:utf-8
import requests
from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title attrs"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body></html>
"""
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(type(soup.p['class']))
for i in soup.find_all('a'):
    print(i.get('href'))
print('title name is '+soup.title.name)
print(soup.p['class'])

res = requests.get('https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_17045870298188545554%22%7D&n_type=0&p_from=1')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.content,'html.parser')
print(soup.text)
