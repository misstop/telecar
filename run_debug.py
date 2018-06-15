from scrapy import cmdline

name = 'kline_zb'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
