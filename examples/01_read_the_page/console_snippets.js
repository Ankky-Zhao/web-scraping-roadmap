// Stage 1 · paste these into the browser Console on https://quotes.toscrape.com/
// 阶段 1 · 在 https://quotes.toscrape.com/ 打开 F12，把下面几行粘贴到 Console 里运行

// How many quotes does this selector match? Expect 10.
// 这个选择器选中了几条名言？应该返回 10
document.querySelectorAll("div.quote span.text").length

// All author names on this page / 本页所有作者
[...document.querySelectorAll("small.author")].map(e => e.innerText)

// All tags of the first quote / 第一条名言的全部标签
[...document.querySelector("div.quote").querySelectorAll("a.tag")].map(e => e.innerText)

// The link to the next page (a relative path) / 下一页链接（相对路径）
document.querySelector("li.next a").getAttribute("href")
