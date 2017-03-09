# encoding:utf-8
import requests

url = "https://oa.touus.com/"
loginAction = "common/login"
leaveListAction = "leave/list/queryData"
session = requests.session()

params = {'empAccount': 'dengyichen', 'loginPwd': 'Dengyc109'}
r = session.post(url + loginAction, params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print("--------------------------")
print("Going to the leave list page...")

# 服务端不是使用cookie保持登录的
r = session.get(url + leaveListAction)
print(r.text)
