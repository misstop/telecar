from scrapy import cmdline

name = 'trade_zb'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
