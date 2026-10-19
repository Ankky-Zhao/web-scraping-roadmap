"""Stage 2 · your first scraper / 阶段 2 · 第一个爬虫"""
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
resp = requests.get(url, timeout=10)            # wait at most 10 s · 最多等 10 秒
print("status:", resp.status_code)              # expect 200 · 期望是 200

soup = BeautifulSoup(resp.text, "lxml")         # HTML text -> searchable tree · 把文本变成可查询的树

for q in soup.select("div.quote"):              # same selector as in the Console · 和 Console 里一样
    text = q.select_one("span.text").get_text(strip=True)
    author = q.select_one("small.author").get_text(strip=True)
    tags = [t.get_text() for t in q.select("a.tag")]
    print(author, "|", text[:40], "|", tags)
