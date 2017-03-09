# encoding:utf-8
import requests

url = "https://oa.touus.com/"
loginAction = "/common/login"
params = {"empAccount": "dengyichen", "loginPwd": "Dengyc109"}
r = requests.post(url + loginAction, data=params)
print(r.text)
