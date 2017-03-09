import json
from urllib.request import urlopen


# 获取ip所属国家简码
# def getCountry(ipAddress):
#     response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
#     responseJson = json.loads(response)
#     return responseJson.get("country_code")
#
#
# print(getCountry("223.211.14.137"))


def getIpInfoByTaoBaoAPI(ipAddress):
    response = urlopen("http://ip.taobao.com/service/getIpInfo2.php?ip=" + ipAddress) \
        .read().decode("utf-8")
    responseJson = json.loads(response)
    return responseJson.get("data")


info = getIpInfoByTaoBaoAPI("223.211.14.137")

for key, value in info.items():
    print(key + ':' + value)
