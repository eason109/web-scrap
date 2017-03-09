# encoding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl, context=ssl._create_unverified_context())
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心，异常已处理")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newPage = link.attrs["href"]
                print("==============\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
