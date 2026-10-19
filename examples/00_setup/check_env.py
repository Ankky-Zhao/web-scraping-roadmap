"""Stage 0 · check that Python and the libraries are installed.
阶段 0 · 检查 Python 和各个库是否装好。

Run / 运行:  python check_env.py
"""
import importlib
import sys

print("Python", sys.version.split()[0])
if sys.version_info < (3, 10):
    print("!! Python 3.10+ is recommended / 建议使用 Python 3.10 或更新版本")

for name in ["requests", "bs4", "lxml", "pandas", "playwright", "scrapy"]:
    try:
        mod = importlib.import_module(name)
        print(f"  ok   {name} {getattr(mod, '__version__', '')}")
    except ImportError:
        print(f"  --   {name} not installed / 未安装  (pip install -r requirements.txt)")
