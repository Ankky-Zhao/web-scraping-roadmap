"""Stage 6 · the same job with Scrapy / 阶段 6 · 用 Scrapy 完成同样的任务

Run / 运行:  scrapy runspider quotes_spider.py -O quotes.json
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]
    custom_settings = {
        "ROBOTSTXT_OBEY": True,       # obey robots.txt · 自动遵守 robots.txt
        "DOWNLOAD_DELAY": 1,          # 1 s between requests · 请求间隔 1 秒
        "AUTOTHROTTLE_ENABLED": True, # adapt to server speed · 根据服务器响应自动调速
        "USER_AGENT": "LearningBot/0.1 (contact: you@example.com)",
    }

    def parse(self, response):
        for q in response.css("div.quote"):
            yield {
                "text": q.css("span.text::text").get(),
                "author": q.css("small.author::text").get(),
                "tags": q.css("a.tag::text").getall(),
            }
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
