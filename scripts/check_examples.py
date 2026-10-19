"""Run every example against the practice sites and check the results.
Used by the weekly GitHub Actions job, and you can run it locally too.

在练习站上运行全部示例并检查结果。每周的 GitHub Actions 任务会调用它，本地也可以运行。

    python scripts/check_examples.py
"""
import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EX = ROOT / "examples"


def run(args, cwd):
    print(f"\n$ {' '.join(map(str, args))}", flush=True)
    res = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=600)
    print(res.stdout[-2000:])
    if res.returncode != 0:
        print(res.stderr[-4000:])
        raise SystemExit(f"FAILED: {args[-1]}")
    return res.stdout


def count_csv(path):
    with open(path, encoding="utf-8-sig") as f:
        return sum(1 for _ in csv.DictReader(f))


def main():
    py = sys.executable
    checks = []
    with tempfile.TemporaryDirectory() as tmp:
        out = run([py, EX / "02_first_scraper/quotes_v1.py"], tmp)
        checks.append(("stage 2: 10 quotes printed", out.count(" | ") >= 20))

        run([py, EX / "03_pagination/books.py"], tmp)
        checks.append(("stage 3: books.csv has 1000 rows", count_csv(Path(tmp, "books.csv")) == 1000))

        run([py, EX / "04_dynamic/api_quotes.py"], tmp)
        data = json.loads(Path(tmp, "api_quotes.json").read_text(encoding="utf-8"))
        checks.append(("stage 4a: API returns 100 quotes", len(data) == 100))

        out = run([py, EX / "04_dynamic/js_quotes.py"], tmp)
        checks.append(("stage 4b: Playwright renders 10 quotes", "10 quotes on page 1" in out))

        run([py, EX / "05_robust/polite_session.py"], tmp)
        checks.append(("stage 5: 100 rows written", count_csv(Path(tmp, "quotes_robust.csv")) == 100))
        run([py, EX / "05_robust/polite_session.py"], tmp)   # second run should skip everything
        checks.append(("stage 5: resume adds no duplicates", count_csv(Path(tmp, "quotes_robust.csv")) == 100))

        run([py, "-m", "scrapy", "runspider", EX / "06_scrapy/quotes_spider.py", "-O", "quotes.json"], tmp)
        data = json.loads(Path(tmp, "quotes.json").read_text(encoding="utf-8"))
        checks.append(("stage 6: Scrapy exports 100 quotes", len(data) == 100))

    print("\nResults")
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    if not all(ok for _, ok in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
