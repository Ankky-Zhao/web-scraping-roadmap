"""Stage 5 · retries, robots.txt, logging and resume / 阶段 5 · 重试、robots.txt、日志、断点续爬

Stop it with Ctrl+C halfway and run it again: finished pages are skipped.
中途按 Ctrl+C 中断后重新运行，已完成的页面会被跳过。
"""
import csv
import logging
import time
from functools import lru_cache
from pathlib import Path
from urllib import robotparser
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

AGENT = "LearningBot/0.1 (contact: you@example.com)"   # say who you are · 写清楚你是谁
DONE = Path("done.txt")
OUT = Path("quotes_robust.csv")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


def make_session():
    s = requests.Session()                       # reuses connections · 复用连接
    s.headers["User-Agent"] = AGENT
    retry = Retry(total=3, backoff_factor=1,     # waits 1 s, 2 s, 4 s · 依次等待 1、2、4 秒
                  status_forcelist=[429, 500, 502, 503, 504])
    s.mount("https://", HTTPAdapter(max_retries=retry))
    return s


@lru_cache(maxsize=None)
def robots_for(base):
    rp = robotparser.RobotFileParser(urljoin(base, "/robots.txt"))
    rp.read()
    return rp


def allowed(url):
    p = urlparse(url)
    return robots_for(f"{p.scheme}://{p.netloc}").can_fetch(AGENT, url)


session = make_session()
done = set(DONE.read_text().split()) if DONE.exists() else set()
new_file = not OUT.exists()

with OUT.open("a", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    if new_file:
        writer.writerow(["author", "text"])
    for n in range(1, 11):
        url = f"https://quotes.toscrape.com/page/{n}/"
        if url in done:
            logging.info("skip (done) %s", url)
            continue
        if not allowed(url):
            logging.warning("robots.txt disallows %s", url)
            continue
        r = session.get(url, timeout=10)
        r.raise_for_status()                     # stop on 4xx/5xx · 遇到错误状态码就停下
        soup = BeautifulSoup(r.text, "lxml")
        for q in soup.select("div.quote"):
            writer.writerow([q.select_one("small.author").get_text(strip=True),
                             q.select_one("span.text").get_text(strip=True)])
        f.flush()
        with DONE.open("a") as d:
            d.write(url + "\n")
        logging.info("%s -> %s", url, r.status_code)
        time.sleep(1)
