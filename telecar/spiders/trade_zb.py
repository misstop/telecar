import scrapy
import json

from telecar.items import TradeItem


class ZbSpider(scrapy.Spider):
    name = "trade_zb"
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
            yield scrapy.Request(url='http://api.zb.com/data/v1/trades?market=%s' % sym,
                                 meta={
                                     'pair': sym,
                                 },
                                 callback=self.details)

    def details(self, response):
        """
        response text json
        [
            {
            amount: "0.0025",
            price: "6470.29",
            tid: 125945719,
            type: "sell",
            date: 1528947232,
            trade_type: "ask",
            },
            {
            amount: "0.0005",
            price: "6470.08",
            tid: 125945720,
            type: "sell",
            date: 1528947232,
            trade_type: "ask",
            },
            ...
        ]
        :param response:
        :return:
        """

        """
        Want to get
            {
                "exchange":"Huobi", # 交易所名
                "measurement":"trade", # 来源
                "onlyKey":"Huobi_BCH_USDT", # 交易对
                "price":947.870000000000000000, # 价格
                "side":"buy",
                "symbol":"BCH",
                "timestamp":1528772246223012133,
                "tradeId":"92028678095704059110",
                "unit":"USDT",
                "volume":0.056900000000000000
            }
        """
        k_detail = json.loads(response.text)
        pair = response.meta['pair'].split('_')
        cur_from = pair[0].upper()
        cur_to = pair[1].upper()
        item = TradeItem()
        item['exchange'] = self.exchange_name
        item['measurement'] = "trade"
        item['onlyKey'] = self.exchange_name + "_" + cur_from + "_" + cur_to
        item['symbol'] = cur_from
        item['unit'] = cur_to
        for d in k_detail:
            item['price'] = d['price']
            item['tradeId'] = d['tid']
            item['timestamp'] = d['date']
            item['volume'] = d['amount']
            item['side'] = d['type']
            yield item
