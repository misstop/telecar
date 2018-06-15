import time
import os


CYCLE_TIME = 1 * 60

spiders = ['kline_zb', 'trade_zb']

cmd = 'curl http://47.74.46.169:6800/schedule.json -d project=telecar -d spider={}'

while True:
    for spider in spiders:
        os.system(cmd.format(spider))
    time.sleep(CYCLE_TIME)
