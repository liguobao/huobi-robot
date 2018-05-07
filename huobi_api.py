# encoding=utf8

import requests
import json
import redis
import urllib
import time
from util import get_config
config = get_config()


class HuobiAPI:
    usd_rate = None
    usd_rate_update = time.time()

    def get_symbol_detail(self, symbol):
        url = "http://api.huobipro.com/market/detail?symbol=%s"%(symbol)
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"
            }
        # proxies = {'http': 'http://127.0.0.1:1087'}
        # response = requests.request("GET", url, headers=headers, proxies=proxies)
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)

    def get_usd_rate(self):
        if time.time() - self.usd_rate_update > 3600 or self.usd_rate == None:
            url = "http://api.k780.com/"
            querystring = {"app": "finance.rate", "scur": "USD", "tcur": "CNY", "appkey": "10003", "sign": "b59bc3ef6191eb9f747dd4e83c99f2a4"}
            headers = {
                'cache-control': "no-cache",
                'postman-token': "fdbe1f99-4b93-de76-db7d-9b4bac84df51"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            response_json = json.loads(response.text)
            if response_json and response_json["success"] and response_json["success"]=="1":
                self.usd_rate_update = time.time()
                usd_rate = float(response_json["result"]["rate"])
                self.usd_rate = usd_rate
                return usd_rate
            else:
                return None
        else:
            return self.usd_rate