# encoding:utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.baidu.com")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.title)
