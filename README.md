# Web Scraping Roadmap · 爬虫从零到实战

**[Open the site / 打开网页](https://ankky-zhao.github.io/web-scraping-roadmap/)** · [English](#english) · [中文](#中文)

A bilingual roadmap that takes complete beginners from installing Python to shipping their own scraping project. Every stage can be followed in two ways, by writing the code yourself or by building it with an AI assistant, and every example runs against sites made for scraping practice.

一份中英双语的爬虫学习路线，从安装 Python 一直带到完成自己的项目。每个阶段都提供两种学法，自己写代码，或者借助 AI 编程。全部示例都在专门供人练习的网站上运行。

---

## English

### What is inside

| Stage | Topic | Example |
|---|---|---|
| 0 | Python, VS Code, virtual environments, browser DevTools | [`check_env.py`](examples/00_setup/check_env.py) |
| 1 | HTTP, HTML as a tree, CSS selectors in the Console | [`console_snippets.js`](examples/01_read_the_page/console_snippets.js) |
| 2 | First scraper with requests and BeautifulSoup | [`quotes_v1.py`](examples/02_first_scraper/quotes_v1.py) |
| 3 | Pagination, encoding, saving CSV with pandas | [`books.py`](examples/03_pagination/books.py) |
| 4 | JavaScript pages, finding the JSON API, Playwright | [`api_quotes.py`](examples/04_dynamic/api_quotes.py), [`js_quotes.py`](examples/04_dynamic/js_quotes.py) |
| 5 | Retries, robots.txt, User-Agent, logging, resuming | [`polite_session.py`](examples/05_robust/polite_session.py) |
| 6 | Scaling up with Scrapy | [`quotes_spider.py`](examples/06_scrapy/quotes_spider.py) |
| 7 | Capstone project with a checklist | |

The site also covers a working loop for scraping with AI, common AI mistakes, ground rules on legality and courtesy, and a troubleshooting table.

### What makes it different

- **Two tracks on every stage.** The AI track gives prompt templates together with a checklist for verifying what the AI produced, because generating code is the easy part.
- **Examples are tested every week.** A GitHub Actions job runs all examples against [toscrape.com](https://toscrape.com/) and checks the results, so broken code is noticed early.
- **Courtesy and legality are part of the curriculum.** robots.txt, rate limits and personal data are taught alongside the code rather than in a footnote.

### Run the examples

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r examples/requirements.txt
playwright install chromium      # only needed for stage 4b

python examples/02_first_scraper/quotes_v1.py
python scripts/check_examples.py # runs and checks everything
```

### Build the site locally

```bash
python build.py                  # writes site/index.html, standard library only
```

Open `site/index.html` in a browser. Content lives in [`data/content.json`](data/content.json) and code is read from [`examples/`](examples), so the page and the runnable files never drift apart.

### Contributing

Corrections, translations and new exercises are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

### Disclaimer

This project is for learning. All exercises target sites built for scraping practice. Before collecting data from any other site, read its robots.txt and terms of use and follow the laws that apply to you. Nothing here is legal advice.

---

## 中文

### 内容

| 阶段 | 主题 | 示例 |
|---|---|---|
| 0 | Python、VS Code、虚拟环境、浏览器开发者工具 | [`check_env.py`](examples/00_setup/check_env.py) |
| 1 | HTTP、HTML 树结构、在 Console 里调试 CSS 选择器 | [`console_snippets.js`](examples/01_read_the_page/console_snippets.js) |
| 2 | 用 requests 和 BeautifulSoup 写第一个爬虫 | [`quotes_v1.py`](examples/02_first_scraper/quotes_v1.py) |
| 3 | 翻页、编码、用 pandas 保存 CSV | [`books.py`](examples/03_pagination/books.py) |
| 4 | JavaScript 页面、寻找 JSON 接口、Playwright | [`api_quotes.py`](examples/04_dynamic/api_quotes.py)、[`js_quotes.py`](examples/04_dynamic/js_quotes.py) |
| 5 | 重试、robots.txt、User-Agent、日志、断点续爬 | [`polite_session.py`](examples/05_robust/polite_session.py) |
| 6 | 用 Scrapy 扩展规模 | [`quotes_spider.py`](examples/06_scrapy/quotes_spider.py) |
| 7 | 毕业项目与检查清单 | |

网页里还有和 AI 协作写爬虫的工作循环、AI 常犯的错误、合规底线和排错速查表。

### 特点

- **每个阶段两条路线。** AI 路线除了提示词模板，还附带验收清单，教你检查 AI 生成的代码，因为生成代码本身并不难。
- **示例每周自动测试。** GitHub Actions 每周在 [toscrape.com](https://toscrape.com/) 上运行全部示例并核对结果，代码失效时能及早发现。
- **礼貌与合规是课程的一部分。** robots.txt、请求频率、个人信息和代码放在一起讲。

### 运行示例

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r examples/requirements.txt
playwright install chromium      # 只有阶段 4b 需要

python examples/02_first_scraper/quotes_v1.py
python scripts/check_examples.py # 运行并检查全部示例
```

### 本地生成网页

```bash
python build.py                  # 生成 site/index.html，只依赖标准库
```

用浏览器打开 `site/index.html` 即可。教程文字在 [`data/content.json`](data/content.json)，代码直接从 [`examples/`](examples) 读取，网页和可运行文件始终保持一致。

### 参与贡献

欢迎纠错、改进翻译、补充练习，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 免责声明

本项目仅用于学习，全部练习都针对专门供人练习爬虫的网站。抓取其他网站前，请先阅读其 robots.txt 和使用条款，并遵守所在地的法律。本项目内容不构成法律意见。

---

## Related · 相关项目

[LLM Agent Roadmap](https://github.com/Ankky-Zhao/llm-agent-roadmap) · a bilingual roadmap for learning LLM agents · 双语 LLM Agent 学习路线

## License · 许可

Code (`examples/`, `scripts/`, `build.py`, `template.html`) is released under the [MIT License](LICENSE). Tutorial text in `data/` is released under [CC BY 4.0](LICENSE-CONTENT).

代码以 [MIT](LICENSE) 许可发布，`data/` 中的教程文字以 [CC BY 4.0](LICENSE-CONTENT) 许可发布。
