# encoding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.163.com/")
bsObj = BeautifulSoup(html, "html.parser", from_encoding="gbk")
names = bsObj.findAll("li", {"class": "cm_fb"})
for name in names:
    print(name.get_text())
