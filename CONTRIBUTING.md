# Contributing · 参与贡献

Thank you for helping. 感谢参与。

## How the repo fits together · 仓库结构

```
data/content.json        all tutorial text, in zh and en · 全部教程文字（中英）
examples/                runnable code shown on the page · 网页上展示的可运行代码
scripts/check_examples.py   runs and checks every example · 运行并检查全部示例
template.html            page layout, styles and rendering script · 页面布局、样式与渲染脚本
build.py                 combines the above into site/index.html · 生成 site/index.html
```

## Rules for content · 内容规则

- **Both languages, always.** Every text field has a `zh` and an `en` value, and lists in both languages have the same length. `python build.py` stops with an error otherwise.
  每个文字字段都要同时有 `zh` 和 `en`，两种语言的列表长度一致，否则 `build.py` 会报错。
- **Adapt, do not just translate.** Legal notes differ by audience. The Chinese text refers to Chinese law and the English text to the GDPR and other regulations.
  双语按读者调整，不必逐句直译。例如法律部分中文版以中国法律为主，英文版以 GDPR 等为主。
- **Code lives in `examples/`.** Do not paste long code into `content.json`. Add a file and reference it with `{"t": "code", "file": "examples/..."}`. Comments in example files are written as `English · 中文`.
  长代码放进 `examples/`，在 JSON 里用 `file` 引用。示例中的注释写成“英文 · 中文”。
- **Practice sites only.** Exercises must target sites that invite scraping, such as toscrape.com. Do not add examples aimed at real services.
  练习只针对允许抓取的练习站，不要加入针对真实网站的示例。
- **No evasion techniques.** Contributions that bypass CAPTCHAs, logins, paywalls or blocks, fake browser fingerprints or rotate proxies to avoid bans will not be merged.
  不接受绕过验证码、登录、付费墙或封禁的内容，也不接受伪造浏览器指纹或用代理轮换躲避封禁的内容。
- Text fields may contain simple HTML (`<b>`, `<code>`, `<a href='...'>`). Use single quotes inside JSON strings for attributes.
  文字字段可以包含简单 HTML，属性用单引号。

## Before opening a pull request · 提交前

```bash
python build.py                    # must succeed · 必须成功
python scripts/check_examples.py   # if you changed examples · 修改示例时运行
```

Open `site/index.html` and look at your change in both languages and in dark mode.
打开 `site/index.html`，在中英文和深色模式下检查修改效果。

## Licence · 许可

By contributing you agree that code is released under MIT and text under CC BY 4.0.
提交贡献即表示同意代码以 MIT、文字以 CC BY 4.0 许可发布。
