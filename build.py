"""Build the static site from data/content.json, the example files and template.html.
由 data/content.json、示例代码和 template.html 生成静态网页。

    python build.py                 # -> site/index.html
    python build.py --fragment out.html   # page body only, for embedding / previews

Only the Python standard library is needed. 只依赖 Python 标准库。
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/Ankky-Zhao/web-scraping-roadmap"
LANGS = ("zh", "en")


def fail(msg):
    sys.exit(f"build error: {msg}")


def check_bilingual(obj, where):
    """Every dict with a zh key must also have an en key and the other way round."""
    if isinstance(obj, dict):
        if ("zh" in obj) != ("en" in obj):
            fail(f"{where}: needs both zh and en")
        if "zh" in obj and isinstance(obj["zh"], list) and len(obj["zh"]) != len(obj["en"]):
            fail(f"{where}: zh and en lists differ in length")
        for k, v in obj.items():
            check_bilingual(v, f"{where}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            check_bilingual(v, f"{where}[{i}]")


def load():
    data = json.loads((ROOT / "data/content.json").read_text(encoding="utf-8"))
    check_bilingual(data, "content")
    seen = set()
    for st in data["stages"]:
        for key in ("id", "path", "name", "title", "time", "goal", "concepts", "hand", "ai", "tasks"):
            if key not in st:
                fail(f"stage {st.get('id', '?')} is missing '{key}'")
        for t in st["tasks"]:
            if t["id"] in seen:
                fail(f"duplicate task id {t['id']}")
            seen.add(t["id"])
        for block in st["hand"] + st["ai"] + st["concepts"]:
            if block["t"] == "code" and "file" in block:
                path = ROOT / block["file"]
                if not path.exists():
                    fail(f"stage {st['id']}: missing file {block['file']}")
                block["text"] = path.read_text(encoding="utf-8").rstrip("\n")
            elif block["t"] == "code" and "text" not in block:
                fail(f"stage {st['id']}: code block needs 'file' or 'text'")
    data["repo"] = REPO
    return data


def render(data):
    template = (ROOT / "template.html").read_text(encoding="utf-8")
    head, sep, body = template.partition("<!--BODY-->")
    if not sep:
        fail("template.html needs a <!--BODY--> marker")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    body = body.replace("__DATA__", payload)
    return head, body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragment", help="write head+body without the html/head/body wrapper to this path")
    args = ap.parse_args()

    data = load()
    head, body = render(data)

    if args.fragment:
        Path(args.fragment).write_text(head + body, encoding="utf-8")
        print(f"wrote {args.fragment}")
        return

    out = ROOT / "site"
    out.mkdir(exist_ok=True)
    page = (
        "<!doctype html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        + head + "</head>\n<body>\n" + body + "</body>\n</html>\n"
    )
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    n_tasks = sum(len(s["tasks"]) for s in data["stages"])
    print(f"wrote site/index.html · {len(data['stages'])} stages · {n_tasks} exercises · {len(page) // 1024} KB")


if __name__ == "__main__":
    main()
