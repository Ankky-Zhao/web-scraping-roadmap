"""Stage 3 · follow pagination and save to CSV / 阶段 3 · 翻页并保存为 CSV"""
import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

RATING = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
url = "https://books.toscrape.com/catalogue/page-1.html"
rows = []

while url:
    resp = requests.get(url, timeout=10)
    resp.encoding = "utf-8"                     # fixes "Â£" · 修正 £ 的乱码
    soup = BeautifulSoup(resp.text, "lxml")

    for book in soup.select("article.product_pod"):
        title = book.select_one("h3 a")["title"]
        price = book.select_one("p.price_color").get_text()
        star = book.select_one("p.star-rating")["class"][1]   # e.g. "Three"
        rows.append({
            "title": title,
            "price_gbp": float(price.replace("£", "")),
            "rating": RATING.get(star),
        })

    nxt = soup.select_one("li.next a")           # the "next" link · 下一页链接
    url = urljoin(url, nxt["href"]) if nxt else None   # relative -> absolute · 相对路径转完整网址
    print(f"{len(rows)} books so far / 已抓 {len(rows)} 本")
    time.sleep(1)                                # be polite · 礼貌间隔

df = pd.DataFrame(rows)
df.to_csv("books.csv", index=False, encoding="utf-8-sig")  # utf-8-sig keeps Excel happy · 让 Excel 正确显示
print(df.groupby("rating")["price_gbp"].mean().round(2))
