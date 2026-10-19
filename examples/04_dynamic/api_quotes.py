"""Stage 4a · call the JSON API behind https://quotes.toscrape.com/scroll
阶段 4a · 直接调用 /scroll 页面背后的 JSON 接口"""
import json
import time

import requests

page, all_quotes = 1, []
while True:
    data = requests.get(
        "https://quotes.toscrape.com/api/quotes",
        params={"page": page}, timeout=10,
    ).json()                                     # already a Python dict · 直接得到字典
    for q in data["quotes"]:
        all_quotes.append({"author": q["author"]["name"], "text": q["text"], "tags": q["tags"]})
    if not data["has_next"]:
        break
    page += 1
    time.sleep(1)

with open("api_quotes.json", "w", encoding="utf-8") as f:
    json.dump(all_quotes, f, ensure_ascii=False, indent=2)
print(len(all_quotes), "quotes / 条")
