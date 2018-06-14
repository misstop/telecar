# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TradeItem(scrapy.Item):
    """
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
    # 交易所
    exchange = scrapy.Field()
    # 来源
    measurement = scrapy.Field()
    # 交易对
    onlyKey = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # buy/sell类型
    side = scrapy.Field()
    # 左交易对
    symbol = scrapy.Field()
    # 时间戳
    timestamp = scrapy.Field()
    # 交易id
    tradeId = scrapy.Field()
    # 右交易对
    unit = scrapy.Field()
    # 数量
    volume = scrapy.Field()


class TickerItem(scrapy.Item):
    """
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
    # 交易所
    exchange = scrapy.Field()
    # 最高价
    high = scrapy.Field()
    # 最新价
    last = scrapy.Field()
    # 最低价
    low = scrapy.Field()
    # 来源
    measurement = scrapy.Field()
    # 交易对
    onlyKey = scrapy.Field()
    # 左交易对
    symbol = scrapy.Field()
    # 时间
    timestamp = scrapy.Field()
    # 右交易对
    unit = scrapy.Field()
    # 交易数量
    volume = scrapy.Field()


class KlineItem(scrapy.Item):
    """
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
    # 昨收价
    close = scrapy.Field()
    # 交易所
    exchange = scrapy.Field()
    # 最高
    high = scrapy.Field()
    # 最低
    low = scrapy.Field()
    # 来源
    measurement = scrapy.Field()
    # 交易对
    onlyKey = scrapy.Field()
    # 开盘价
    open = scrapy.Field()
    # 左交易对
    symbol = scrapy.Field()
    # 时间戳
    timestamp = scrapy.Field()
    # 右交易对
    unit = scrapy.Field()
    # 数量
    volume = scrapy.Field()
