# encoding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://news.163.com/17/0306/17/CES32ORE0001875N.html")
bsObj = BeautifulSoup(html, "html.parser", from_encoding="gbk")
for child in bsObj.find("div", {"id": "endText"}).children:
    print(child)
