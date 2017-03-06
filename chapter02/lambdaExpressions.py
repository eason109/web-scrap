from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://news.163.com/17/0306/17/CES32ORE0001875N.html")
bsObj = BeautifulSoup(html, "html.parser")
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 5)
for tag in tags:
    print(tag)
