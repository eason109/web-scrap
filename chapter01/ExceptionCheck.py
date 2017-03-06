# encoding:utf-8

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except(HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bszObj = BeautifulSoup(html.read(), "html.parser", from_encoding="gbk")
        title = bszObj.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title


title = get_title("http://news.163.com/17/0303/20/CEKL1NKC000189FH.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
