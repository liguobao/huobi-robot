# 导入模块
from wxpy import *
import requests
import json
from util import get_redis
from huobi_api import HuobiAPI
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True)
redis_server = get_redis()
huobi_api = HuobiAPI()

symbol_list = [
    "BTC",
    "BCH",
    "ETH",
    "ETC",
    "LTC",
    "EOS",
    "XRP"
    "OMG",
    "DASH"
    "ZEC"
    "ONT",
    "IOST"
    "HT",
    "TRX",
    "DTA",
    "NEO",
    "QTUM",
    "ELA",
    "VEN",
    "THETA",
    "SNT",
    "ZIL",
    "XEM",
    "SMT",
    "NAS",
    "RUFF", 
    "HSR",
    "LET", 
    "MDS", 
    "STORJ", 
    "ELF",
    "ITC", 
    "CVC", 
    "GNT",
    "SOC",
    "IOST"]


@bot.register([Group, TEXT])
def auto_reply(msg):
    print(msg.text)
    msg_text = msg.text.replace("@火币偷鸡狗\u2005", "").upper()
    if isinstance(msg.chat, Group) and msg_text in symbol_list and msg.is_at:
        symbol_detail = huobi_api.get_symbol_detail("%susdt" % (msg_text.lower()))
        if symbol_detail and symbol_detail["status"] == "ok" and symbol_detail["tick"]:
            usd_rate = huobi_api.get_usd_rate()
            close = float(symbol_detail["tick"]["close"])
            high = float(symbol_detail["tick"]["high"])
            low = float(symbol_detail["tick"]["low"])
            close_rmb = close * usd_rate
            high_rmb = high * usd_rate
            low_rmb = low * usd_rate
            msg.reply("币种:%s\n当前价格:$%s(≈¥%.2f)\n24小时最高价:$%s(≈¥%.2f)\n最低价:$%s(≈¥%.2f)" % (msg_text, close, close_rmb, high, high_rmb, low, low_rmb))
bot.join()

