"""Stage 4b · render a JavaScript page with Playwright / 阶段 4b · 用 Playwright 渲染 JS 页面

Setup / 准备:
    pip install playwright
    playwright install chromium
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)   # headless=False shows the window · 改成 False 可以看到浏览器
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")
    page.wait_for_selector("div.quote")          # wait until JS has rendered · 等 JS 渲染完成
    quotes = page.locator("div.quote").all()
    for q in quotes:
        print(q.locator("small.author").inner_text(),
              "|", q.locator("span.text").inner_text()[:40])
    print(len(quotes), "quotes on page 1 / 第一页条数")
    browser.close()
