import scrapy
import json

from telecar.items import KlineItem


class ZbSpider(scrapy.Spider):
    name = "kline_zb"
    exchange_name = 'ZB'

    def start_requests(self):
        yield scrapy.Request(url='http://api.zb.com/data/v1/markets',
                             callback=self.symbols_parse)

    def symbols_parse(self, response):
        """
        response.text json
            {
                zb_qc: {
                amountScale: 2,
                priceScale: 4,
                },
                bcc_zb: {
                amountScale: 3,
                priceScale: 2,
                },
                ...
            }
        :param response:
        :return:
        """
        symbols_map = [k for k in json.loads(response.text)]
        for sym in symbols_map:
            yield scrapy.Request(url='http://api.zb.com/data/v1/kline?market=%s' % sym,
                                 meta={
                                     'pair': sym,
                                 },
                                 callback=self.details)

    def details(self, response):
        """
        response text json
        {
            "data": [
                [
                    1472107500000, # 时间戳
                    3840.46,        # 开
                    3843.56,        # 高
                    3839.58,        # 低
                    3843.3,         # 收
                    492.456         # 交易量
                ]...
            ],
            "moneyType": "btc",
            "symbol": "ltc"
        }
        :param response:
        :return:
        """

        """
        Want to get
            {
                "close":0.0112,       # 昨收价
                "exchange":"Okex",    # 交易所
                "high":0.0113,        # 最高
                "low":0.011,          # 最低
                "measurement":"kline",  # 来源
                "onlyKey":"Okex_WFEE_USDT", # 交易对
                "open":0.0113,          # 开盘价
                "symbol":"WFEE",        # 左交易对
                "timestamp":1528793220000,  # 时间戳
                "unit":"USDT",          # 右交易对
                "volume":206471.3       # 数量
            }
        """
        k_detail = json.loads(response.text)['data']
        pair = response.meta['pair'].split('_')
        cur_from = pair[0].upper()
        cur_to = pair[1].upper()
        item = KlineItem()
        item['exchange'] = self.exchange_name
        item['measurement'] = "kline"
        item['onlyKey'] = self.exchange_name + "_" + cur_from + "_" + cur_to
        item['symbol'] = cur_from
        item['unit'] = cur_to
        for d in k_detail:
            item['close'] = d[4]
            item['high'] = d[2]
            item['timestamp'] = d[0]
            item['volume'] = d[5]
            item['low'] = d[3]
            item['open'] = d[1]
            yield item