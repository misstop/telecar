import scrapy
import json

from telecar.items import TickerItem


class BitzSpider(scrapy.Spider):
    name = "ticker_bit_z"
    exchange_name = 'Bit-Z'

    def start_requests(self):
        yield scrapy.Request(url='https://www.bit-z.com/api_v1/tickerall',
                             callback=self.details)

    def details(self, response):
        """
        Response text is json contains:
        {
            "code":0,
            "msg":"Success",
            "data":{
                "ltc_btc":{
                    "date":1517798192,
                    "last":"0.01800401",
                    "buy":"0.01795001",
                    "sell":"0.01800400",
                    "high":"0.01882201",
                    "low":"0.01710096",
                    "vol":"161270.4395"
                        },
                "eth_btc":{
                    "date":1517798192,
                    "last":"0.10170000",
                    "buy":"0.10170000",
                    "sell":"0.10184829",
                    "high":"0.10525401",
                    "low":"0.09960498",
                    "vol":"59826.2376"
                        },
                ...
        }
        :param response:
        :return:
        """

        """
        Want to get 
            {
                "exchange":"Huobi",             # 交易所
                "high":16.275800000000000000,   # 最高
                "last":15.998900000000000000,   # 最新
                "low":12.178600000000000000,    # 最低
                "measurement":"market",         # 来源
                "onlyKey":"Huobi_ETC_USDT",     # 交易对
                "symbol":"ETC",                 # 左交易对
                "timestamp":1528784475145,      # 时间戳
                "unit":"USDT",                  # 右交易对
                "volume":2161458.418184043002585506 # 交易数量
            }
        """
        detail = json.loads(response.text)
        real_detail = detail['data']
        for k, v in real_detail.items():
            # 所用到的item类
            item = TickerItem()
            item['exchange'] = self.exchange_name
            item['high'] = v['high']
            item['last'] = v['last']
            item['low'] = v['low']
            item['measurement'] = "market"
            cur = k.split('_')
            cur_from = cur[0].upper()
            cur_to = cur[1].upper()
            item['onlyKey'] = self.exchange_name + "_" + cur_from + "_" + cur_to
            item['symbol'] = cur_from
            item['timestamp'] = v['date']
            item['unit'] = cur_to
            item['volume'] = v['vol']
            yield item
