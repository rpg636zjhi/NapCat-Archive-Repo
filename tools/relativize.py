#!/usr/bin/env python3
"""
把 VitePress 导出的静态站里的根路径绝对引用（/assets/...）改成相对路径，
以便部署到 GitHub Pages 的子目录（https://user.github.io/repo/）。

用法：
    python tools/relativize.py site
"""
import os
import re
import sys

# 匹配 src="/..."  href="/..." 以及 JSON 里的 "/assets/..."
ATTR_RE = re.compile(r'((?:src|href)=["\'])/(?!/)')
CSS_URL_RE = re.compile(r'url\((["\']?)/(?!/)')

def depth_of(rel_path: str) -> int:
    """返回该文件相对于 site 根目录的层级（根目录文件为 0）"""
    d = os.path.dirname(rel_path)
    if not d:
        return 0
    return len(d.split(os.sep))

def fix_html(text: str, depth: int) -> str:
    prefix = "../" * depth if depth else "./"
    text = ATTR_RE.sub(lambda m: m.group(1) + prefix, text)
    # 内联 style / JSON 里的 url(/...)
    text = CSS_URL_RE.sub(lambda m: "url(" + m.group(1) + prefix, text)
    return text

def fix_css(text: str, depth: int) -> str:
    prefix = "../" * depth if depth else "./"
    return CSS_URL_RE.sub(lambda m: "url(" + m.group(1) + prefix, text)

def fix_js(text: str, depth: int) -> str:
    """只处理明显的静态资源路径字符串，避免误伤"""
    prefix = "../" * depth if depth else "./"
    return re.sub(r'(["\'])/(assets/)', lambda m: m.group(1) + prefix + m.group(2), text)

def main(root: str):
    root = os.path.abspath(root)
    changed = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            depth = depth_of(rel)
            ext = os.path.splitext(name)[1].lower()

            if ext not in (".html", ".css", ".js", ".json"):
                continue

            try:
                with open(full, "r", encoding="utf-8") as f:
                    src = f.read()
            except (UnicodeDecodeError, OSError):
                continue

            if ext == ".html":
                out = fix_html(src, depth)
            elif ext == ".css":
                out = fix_css(src, depth)
            elif ext == ".js":
                out = fix_js(src, depth)
            else:  # .json
                out = fix_js(src, depth)

            if out != src:
                with open(full, "w", encoding="utf-8", newline="") as f:
                    f.write(out)
                changed += 1

    print(f"[relativize] 已处理 {changed} 个文件")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "site"
    if not os.path.isdir(target):
        print(f"目录不存在: {target}", file=sys.stderr)
        sys.exit(1)
    main(target)
