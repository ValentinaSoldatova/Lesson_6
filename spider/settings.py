BOT_NAME = 'lesson6.hhru'

SPIDER_MODULES = ['lesson6.hhru.spiders']
NEWSPIDER_MODULE = 'lesson6.hhru.spiders'



USER_AGENT = '	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'


ROBOTSTXT_OBEY = False


CONCURRENT_REQUESTS = 16


DOWNLOAD_DELAY = 3



COOKIES_ENABLED = True


ITEM_PIPELINES = {
   'lesson6.hhru.pipelines.JobparserPipeline': 300,
}

