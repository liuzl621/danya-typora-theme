#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把入口 CSS 里的 @import 递归内联，生成单文件主题。

什么时候用：个别 Typora 版本对 @import 支持不好、加载不出样式时；
或者想把主题打包成单个 css 发给别人时。

在项目根目录跑：
    python scripts/build.py

输出 dist/danya.css，可直接放进 Typora 主题目录使用
（除非启用 fonts.css 里的自带字体，否则不需要 danya/ 目录）。
仅用标准库，无第三方依赖。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ("danya.css",)

# 匹配四种常见写法（允许行尾带 /* 注释 */）：
#   @import "danya/xxx.css";            @import 'danya/xxx.css';
#   @import url("danya/xxx.css");       @import "danya/xxx.css"; /* 说明 */
IMPORT_RE = re.compile(
    r'^\s*@import\s+(?:url\(\s*)?["\']?([^"\')\s;]+)["\']?\s*\)?\s*;'
    r'[ \t]*(?:/\*(?P<note>[^\n]*?)\*/)?[ \t]*$',
    re.M,
)


def inline_css(entry: Path, seen: frozenset) -> str:
    """读取 entry，把其中的 @import 替换成目标文件内容（递归）。"""
    text = entry.read_text(encoding="utf-8")

    def repl(m: "re.Match[str]") -> str:
        rel = m.group(1)
        target = (entry.parent / rel).resolve()
        if str(target) in seen:
            return f"/* ! 跳过循环引用: {rel} */"
        if not target.is_file():
            return f"/* ! 找不到被导入的文件: {rel} */"
        body = inline_css(target, seen | {str(target)})
        note = m.group("note")
        note = f"  {note.strip()}" if note and note.strip() else ""
        header = f"/* ========== 内联自 {rel}{note} ========== */"
        return f"{header}\n{body.rstrip()}"

    return IMPORT_RE.sub(repl, text).rstrip() + "\n"


def main() -> int:
    out_dir = ROOT / "dist"
    out_dir.mkdir(exist_ok=True)
    failed = False
    for name in ENTRIES:
        entry = ROOT / name
        if not entry.is_file():
            print(f"[错误] 找不到入口文件: {entry}")
            failed = True
            continue
        css = inline_css(entry, frozenset({str(entry)}))
        dest = out_dir / name
        dest.write_text(css, encoding="utf-8")
        left = IMPORT_RE.findall(css)
        print(f"[完成] {dest}  ({len(css.splitlines())} 行)"
              + (f"  警告:仍有未内联的 @import -> {left}" if left else ""))
        if left:
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
