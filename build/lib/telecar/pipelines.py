import json

from kafka import KafkaProducer

from telecar.items import TickerItem, TradeItem, KlineItem


class TelecarPipeline(object):
    def open_spider(self, spider):
        self.producer = KafkaProducer(bootstrap_servers='47.52.21.206:9092',
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def process_item(self, item, spider):

        if isinstance(item, TickerItem):
            self.producer.send('ticker-dev', [dict(item)])

        elif isinstance(item, TradeItem):
            self.producer.send('trade-dev', [dict(item)])

        else:
            self.producer.send('kline-dev', [dict(item)])

    def close_spider(self, spider):
        self.producer.close()
